"""Part data for prog_adapter (shared by schematic, board and BOM generators)."""
LIB = 'prog_adapter'

# symbol source: (kicad lib, symbol name)
SYMSRC = {
    'R': ('Device', 'R'), 'C': ('Device', 'C'), 'LED': ('Device', 'LED'),
    'Polyfuse': ('Device', 'Polyfuse'), 'SW_Push': ('Switch', 'SW_Push'),
    'Jumper_2_Open': ('Jumper', 'Jumper_2_Open'),
    'Conn_02x03_Odd_Even': ('Connector_Generic', 'Conn_02x03_Odd_Even'),
    'Conn_02x05_Odd_Even': ('Connector_Generic', 'Conn_02x05_Odd_Even'),
    'Conn_01x06': ('Connector_Generic', 'Conn_01x06'),
    'Conn_01x03': ('Connector_Generic', 'Conn_01x03'),
    'USB_C_Receptacle_USB2.0_16P': ('Connector', 'USB_C_Receptacle_USB2.0_16P'),
    'TLV75530PDBV': ('Regulator_Linear', 'TLV75530PDBV'),
    'PWR_FLAG': ('power', 'PWR_FLAG'),
    'MountingHole': ('Mechanical', 'MountingHole'),
}

# footprint source: local name -> (kicad .pretty, kicad name) or None for custom
FPSRC = {
    'R_0805_2012Metric': ('Resistor_SMD', 'R_0805_2012Metric'),
    'C_0805_2012Metric': ('Capacitor_SMD', 'C_0805_2012Metric'),
    'LED_0805_2012Metric': ('LED_SMD', 'LED_0805_2012Metric'),
    'Fuse_1206_3216Metric': ('Fuse', 'Fuse_1206_3216Metric'),
    'SOT-23-5': ('Package_TO_SOT_SMD', 'SOT-23-5'),
    'SW_PUSH_6mm': ('Button_Switch_THT', 'SW_PUSH_6mm'),
    'PinHeader_1x02_P2.54mm_Vertical': ('Connector_PinHeader_2.54mm', 'PinHeader_1x02_P2.54mm_Vertical'),
    'PinHeader_1x03_P2.54mm_Vertical': ('Connector_PinHeader_2.54mm', 'PinHeader_1x03_P2.54mm_Vertical'),
    'PinHeader_1x06_P2.54mm_Vertical': ('Connector_PinHeader_2.54mm', 'PinHeader_1x06_P2.54mm_Vertical'),
    'USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal': ('Connector_USB', 'USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal'),
    'MountingHole_3.2mm_M3': ('MountingHole', 'MountingHole_3.2mm_M3'),
    'BoxHeader_SSK05-BH-254-B3_2x03_P2.54mm_Vertical': None,
    'BoxHeader_CNC_3220-10-0100-00_2x05_P1.27mm_Vertical': None,
    'FTDI_WirePads_3x_D1.0mm_ZipTie': None,
}

def P(mpn, mfr, dk, mouser):
    return {'MPN': mpn, 'Manufacturer': mfr, 'DigiKey': dk, 'Mouser': mouser}

SSK = P('SSK05-BH-254-B3', 'Same Sky', '2223-SSK05-BH-254-B3-ND', '179-SSK05BH254B3')
R330 = P('RC0805FR-07330RL', 'YAGEO', '311-330CRCT-ND', '603-RC0805FR-07330RL')
R1K = P('RC0805FR-071KL', 'YAGEO', '311-1.00KCRCT-ND', '603-RC0805FR-071KL')
R5K1 = P('RC0805FR-075K1L', 'YAGEO', '311-5.10KCRCT-ND', '603-RC0805FR-075K1L')
C10U = P('CC0805KKX5R8BB106', 'YAGEO', '311-1869-1-ND', '603-CC805KKX5R8BB106')
SW = P('B3F-1000', 'Omron (Aratas)', 'SW400-ND', '653-B3F-1000')
NOPART = {}

# ref: dict(sym, value, fp, pos(x,y) schematic, nets{pin:net}, nc[pins], fields, bom)
COMPS = {
    # ---------------- Section A: XM125 UART ----------------
    'J1': dict(sym='Conn_02x03_Odd_Even', value='XM125 TC2030-IDC', fp='BoxHeader_SSK05-BH-254-B3_2x03_P2.54mm_Vertical',
               pos=(76.2, 63.5), nets={'1': 'XM_NRST', '2': 'XM_1V8', '3': 'XM_BOOT0', '4': 'XM_RX', '5': 'GND', '6': 'XM_TX'}, f=SSK),
    'J7': dict(sym='Conn_01x03', value='FTDI_WIRES', fp='FTDI_WirePads_3x_D1.0mm_ZipTie',
               pos=(30.48, 63.5), nets={'1': 'GND', '2': 'FTDI_TXD', '3': 'FTDI_RXD'}, f=NOPART, bom=False),
    'R1': dict(sym='R', value='330', fp='R_0805_2012Metric', pos=(50.8, 58.42), nets={'1': 'FTDI_TXD', '2': 'XM_RX'}, f=R330),
    'R2': dict(sym='R', value='330', fp='R_0805_2012Metric', pos=(63.5, 58.42), nets={'1': 'XM_TX', '2': 'FTDI_RXD'}, f=R330),
    'R3': dict(sym='R', value='1k', fp='R_0805_2012Metric', pos=(43.18, 91.44), nets={'1': 'XM_1V8', '2': 'BOOT_JP'}, f=R1K),
    'JP1': dict(sym='Jumper_2_Open', value='BOOT0', fp='PinHeader_1x02_P2.54mm_Vertical', pos=(68.58, 88.9),
                nets={'1': 'BOOT_JP', '2': 'XM_BOOT0'}, f=P('PEC02SAAN', 'Sullins Connector Solutions', '35-PEC02SAAN-ND', '-')),
    'SW1': dict(sym='SW_Push', value='XM RESET', fp='SW_PUSH_6mm', pos=(99.06, 86.36), nets={'1': 'XM_NRST', '2': 'GND'}, f=SW),
    # ---------------- Section B/C: SWD ----------------
    'J2': dict(sym='Conn_02x03_Odd_Even', value='SWD TC2030-IDC', fp='BoxHeader_SSK05-BH-254-B3_2x03_P2.54mm_Vertical',
               pos=(182.88, 63.5), nets={'1': 'SWD_VTREF', '2': 'SWD_SWDIO', '3': 'SWD_NRESET', '4': 'SWD_SWCLK', '5': 'GND', '6': 'SWD_SWO'}, f=SSK),
    'J3': dict(sym='Conn_02x05_Odd_Even', value='Cortex10 to DK Debug out', fp='BoxHeader_CNC_3220-10-0100-00_2x05_P1.27mm_Vertical',
               pos=(233.68, 63.5), nets={'1': 'SWD_VTREF', '2': 'SWD_SWDIO', '3': 'GND', '4': 'SWD_SWCLK', '5': 'GND', '6': 'SWD_SWO', '9': 'GND', '10': 'SWD_NRESET'},
               nc=['7', '8'], f=P('3220-10-0100-00', 'CNC Tech', '1175-1627-ND', '-')),
    'J4': dict(sym='Conn_01x06', value='SWD 0.1in breakout', fp='PinHeader_1x06_P2.54mm_Vertical', pos=(233.68, 99.06),
               nets={'1': 'SWD_VTREF', '2': 'SWD_SWDIO', '3': 'SWD_SWCLK', '4': 'SWD_NRESET', '5': 'SWD_SWO', '6': 'GND'},
               f=P('PEC06SAAN', 'Sullins Connector Solutions', '35-PEC06SAAN-ND', '-')),
    'SW2': dict(sym='SW_Push', value='SWD RESET', fp='SW_PUSH_6mm', pos=(193.04, 93.98), nets={'1': 'SWD_NRESET', '2': 'GND'}, f=SW),
    # ---------------- Section D: USB-C 3.0 V ----------------
    'J6': dict(sym='USB_C_Receptacle_USB2.0_16P', value='USB4105-GF-A', fp='USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal',
               pos=(38.1, 152.4), nets={'A4': 'VBUS', 'A1': 'GND', 'SH': 'GND', 'A5': 'CC1', 'B5': 'CC2'},
               nc=['A6', 'B6', 'A7', 'B7', 'A8', 'B8'], f=P('USB4105-GF-A', 'GCT', '2073-USB4105-GF-ACT-ND', '640-USB4105-GF-A')),
    'R4': dict(sym='R', value='5.1k', fp='R_0805_2012Metric', pos=(73.66, 160.02), nets={'1': 'CC1', '2': 'GND'}, f=R5K1),
    'R5': dict(sym='R', value='5.1k', fp='R_0805_2012Metric', pos=(81.28, 160.02), nets={'1': 'CC2', '2': 'GND'}, f=R5K1),
    'F1': dict(sym='Polyfuse', value='0.5A', fp='Fuse_1206_3216Metric', pos=(91.44, 129.54), nets={'1': 'VBUS', '2': '5V_F'},
               f=P('MF-NSMF050-2', 'Bourns', 'MF-NSMF050-2CT-ND', '652-MF-NSMF050-2')),
    'C1': dict(sym='C', value='10u', fp='C_0805_2012Metric', pos=(106.68, 144.78), nets={'1': '5V_F', '2': 'GND'}, f=C10U),
    'U1': dict(sym='TLV75530PDBV', value='TLV75530PDBVR', fp='SOT-23-5', pos=(132.08, 139.7),
               nets={'1': '5V_F', '2': 'GND', '3': '5V_F', '5': '3V0'}, nc=['4'],
               f=P('TLV75530PDBVR', 'Texas Instruments', '296-TLV75530PDBVRCT-ND', '595-TLV75530PDBVR')),
    'C2': dict(sym='C', value='10u', fp='C_0805_2012Metric', pos=(157.48, 144.78), nets={'1': '3V0', '2': 'GND'}, f=C10U),
    'R6': dict(sym='R', value='1k', fp='R_0805_2012Metric', pos=(170.18, 144.78), nets={'1': '3V0', '2': 'LED_A'}, f=R1K),
    'D1': dict(sym='LED', value='GRN', fp='LED_0805_2012Metric', pos=(185.42, 152.4), nets={'1': 'GND', '2': 'LED_A'},
               f=P('LTST-C171GKT', 'Lite-On', '160-1423-1-ND', '859-LTST-C171GKT')),
    'J5': dict(sym='Conn_01x03', value='3V0 OUT to TP9 TP10', fp='PinHeader_1x03_P2.54mm_Vertical', pos=(205.74, 139.7),
               nets={'1': '3V0', '2': '3V0', '3': 'GND'}, f=P('PEC03SAAN', 'Sullins Connector Solutions', '35-PEC03SAAN-ND', '-')),
    '#FLG01': dict(sym='PWR_FLAG', value='PWR_FLAG', fp='', pos=(106.68, 129.54), nets={'1': '5V_F'}, f=NOPART, bom=False, power=True),
    '#FLG02': dict(sym='PWR_FLAG', value='PWR_FLAG', fp='', pos=(119.38, 160.02), nets={'1': 'GND'}, f=NOPART, bom=False, power=True),
    'H1': dict(sym='MountingHole', value='M3', fp='MountingHole_3.2mm_M3', pos=(30.48, 185.42), nets={}, f=NOPART, bom=False),
    'H2': dict(sym='MountingHole', value='M3', fp='MountingHole_3.2mm_M3', pos=(40.64, 185.42), nets={}, f=NOPART, bom=False),
    'H3': dict(sym='MountingHole', value='M3', fp='MountingHole_3.2mm_M3', pos=(50.8, 185.42), nets={}, f=NOPART, bom=False),
    'H4': dict(sym='MountingHole', value='M3', fp='MountingHole_3.2mm_M3', pos=(60.96, 185.42), nets={}, f=NOPART, bom=False),
}
