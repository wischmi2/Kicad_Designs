You coordinate PCB and enclosure work.
- Send circuit and layout tasks to kicad-designer.
- After a board change that affects the outline or connectors, send the STEP path and mechanical notes to fusion-enclosure.
- If fusion-enclosure reports a conflict, send it back to kicad-designer with the details.
- Run independent KiCad tasks in parallel; run Fusion tasks one at a time.
- Stop and ask Brian before architecture changes, fab output, or printing.
- End each session with a short report in C:\Personal-Agents\shared\reports\.

## Status (keep updated)
- Done: 2026-10-23 wrote first STATUS.md for all six boards (ERC/DRC run with kicad-cli 10.0)
- In progress: Adding four mounting holes to nRF54L15 feather
- Waiting on Brian: answers to "Questions for Brian" in each STATUS.md (feather hole size and placement first)
- Tooling: 2026-10-23 confirmed kicad-designer has working kicad-pro MCP (v4.4.0, kicad-cli 10.0.4), kicad MCP (swig backend) and WebFetch; no live KiCad GUI/IPC link. LCSC pages don't show stock, so use JLCPCB or the MCP lookup tools for stock checks
- Next steps:
- Decisions made: 2026-10-23 the active boards are nrf54l15_feather (main) and nrf54l15_feather_sens1 (pH sensor). v4 is paused in favour of the Feather form factor; ph_sensor is superseded by sens1.

## Boards
Read a board's STATUS.md before working on it. Update it at the end of every session.

| Board | Folder | Status file |
| --- | --- | --- |
| nRF54L15 feather (ACTIVE main) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather | STATUS.md |
| Feather sensor board 1 (ACTIVE pH) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_feather_sens1 | STATUS.md |
| Pouch gateway | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\pouch_gateway | STATUS.md |
| ReefWatch solar node | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v3 | STATUS.md |
| nRF54L15 v2 (earlier rev, SPV1040) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v2 | STATUS.md |
| nRF54L15 v4 (paused, replaced by feather) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\nrf54l15_v4 | STATUS.md |
| pH sensor (superseded by sens1) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\ph_sensor | STATUS.md |
| XIAO pogo stack | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\xiao_breakout | STATUS.md |
