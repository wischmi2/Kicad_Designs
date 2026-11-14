#!/usr/bin/env python3
"""Build the LittleFS credential image for the feather Pouch node.

Pouch reads /lfs1/credentials/crt.der and key.der at boot. The running firmware has
no UART or shell, so the files are written into the storage partition from outside:
this script builds the LittleFS image (as an Intel hex file loaded at the storage
partition address) and PRINTS the nrfutil commands. It never runs nrfutil.

The hex contains the private key. It is written to a new folder under the system temp
directory (never inside the repo). Delete it as soon as it has been programmed; the
script prints the command.

Needs littlefs-python 0.19.0 (same LittleFS 2.11 library NCS v3.4 mounts):
    py -3.11 -m pip install littlefs-python==0.19.0

Usage:
    python provision_credentials.py --crt device.crt.der --key device.key.der \
        --serial <J-Link serial> [--build-dir C:\\ncs\\pouch-builds\\feather_pouch]

The storage partition address and size are read from the build's zephyr.dts so they
always match the image that is on the chip. Geometry (must match the fstab node in
boards\\*.overlay): block 4096, read/prog 16, cache 64, lookahead 32, block cycles 512.
"""

import argparse
import re
import sys
import tempfile
from pathlib import Path

BLOCK_SIZE = 4096
READ_SIZE = 16
PROG_SIZE = 16
CACHE_SIZE = 64
LOOKAHEAD_SIZE = 32
BLOCK_CYCLES = 512

DEFAULT_BUILD = r"C:\ncs\pouch-builds\feather_pouch"


def storage_partition(build_dir: Path):
    """Return (address, size) of storage_partition from the build's zephyr.dts."""
    dts = build_dir / "feather_node" / "zephyr" / "zephyr.dts"
    if not dts.is_file():
        sys.exit(f"{dts} not found. Build first (build.ps1), or pass --build-dir.")
    text = dts.read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r"storage_partition:\s*partition@[0-9a-fA-F]+\s*\{.*?reg\s*=\s*<\s*(0x[0-9a-fA-F]+)\s+(0x[0-9a-fA-F]+)\s*>",
        text,
        re.S,
    )
    if not m:
        sys.exit("storage_partition not found in zephyr.dts")
    return int(m.group(1), 16), int(m.group(2), 16)


def build_image(crt: bytes, key: bytes, size: int) -> bytes:
    from littlefs import LittleFS, UserContext  # imported late for a clear error

    if size % BLOCK_SIZE:
        sys.exit(f"partition size {size:#x} is not a multiple of {BLOCK_SIZE}")
    block_count = size // BLOCK_SIZE
    ctx = UserContext(buffsize=size)
    fs = LittleFS(
        context=ctx,
        block_size=BLOCK_SIZE,
        block_count=block_count,
        read_size=READ_SIZE,
        prog_size=PROG_SIZE,
        cache_size=CACHE_SIZE,
        lookahead_size=LOOKAHEAD_SIZE,
        block_cycles=BLOCK_CYCLES,
        name_max=255,
        file_max=2147483647,
        attr_max=1022,
    )
    fs.mkdir("/credentials")
    for name, data in (("crt.der", crt), ("key.der", key)):
        with fs.open("/credentials/" + name, "wb") as fh:
            fh.write(data)
    fs.unmount()
    return bytes(ctx.buffer)


def intel_hex(data: bytes, base: int) -> str:
    """Intel hex with extended linear address records, 16 data bytes per line."""
    lines = []
    cur_upper = None
    for off in range(0, len(data), 16):
        addr = base + off
        upper = addr >> 16
        if upper != cur_upper:
            rec = bytes([2, 0, 0, 4, (upper >> 8) & 0xFF, upper & 0xFF])
            lines.append(":" + rec.hex().upper() + f"{(-sum(rec)) & 0xFF:02X}")
            cur_upper = upper
        chunk = data[off:off + 16]
        rec = bytes([len(chunk), (addr >> 8) & 0xFF, addr & 0xFF, 0]) + chunk
        lines.append(":" + rec.hex().upper() + f"{(-sum(rec)) & 0xFF:02X}")
    lines.append(":00000001FF")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--crt", required=True, type=Path, help="device certificate, DER")
    ap.add_argument("--key", required=True, type=Path, help="device private key, DER (PKCS#8)")
    ap.add_argument("--serial", required=True, help="J-Link serial number for the printed commands")
    ap.add_argument("--build-dir", type=Path, default=Path(DEFAULT_BUILD))
    args = ap.parse_args()

    for p in (args.crt, args.key):
        if not p.is_file():
            sys.exit(f"{p} not found")

    addr, size = storage_partition(args.build_dir)
    # Never write the hex inside a git checkout.
    out_dir = Path(tempfile.mkdtemp(prefix="feather-creds-"))
    image = build_image(args.crt.read_bytes(), args.key.read_bytes(), size)
    hex_path = out_dir / "creds.hex"
    hex_path.write_text(intel_hex(image, addr))

    end = addr + size
    print(f"Storage partition {addr:#x} size {size:#x} ({size // BLOCK_SIZE} blocks of {BLOCK_SIZE})")
    print(f"Credential hex (contains the private key): {hex_path}")
    print()
    print("Close J-Link RTT Viewer first. Nothing below has been run. Erase only the storage")
    print("pages, then program with ERASE_NONE (a chip erase or recover also wipes credentials):")
    print()
    print(f"  nrfutil device erase --serial-number {args.serial} --pages {addr:#x}-{end:#x}")
    print(f'  nrfutil device program --serial-number {args.serial} --firmware "{hex_path}" '
          "--options chip_erase_mode=ERASE_NONE,verify=VERIFY_READ,reset=RESET_SYSTEM")
    print()
    print("Then delete the hex (it holds the key):")
    print(f'  Remove-Item -Recurse -Force "{out_dir}"')


if __name__ == "__main__":
    main()
