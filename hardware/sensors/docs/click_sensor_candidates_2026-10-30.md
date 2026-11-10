# MikroE Click boards as reference designs for feather sensor boards (2026-10-30)

Source: catalog of about 2,000 Clicks from github.com/MikroElektronika/mikrosdk_click_v2 (driver READMEs), filtered by name; IC and schematic availability read from each mikroe.com product page via Chrome on 2026-10-30. Every board listed has a schematic PDF link on its page (download.mikroe.com/documents/add-on-boards/click/<name>/...).

Access note: mikroe.com and download.mikroe.com return 403 to curl/WebFetch (bot protection). They work through Brian's Chrome (claude-in-chrome); the TDS schematic PDF fetched 200 / application/pdf / 424 kB that way. Agents without Chrome (kicad-designer) need the PDF saved to disk first.

Fit to our boards: CN1 gives I2C, SPI, INT, AIN, VSENS (3.0 V, 100 mA budget) and VBAT. In-water probes go on the isolated side (ADuM1250 = I2C only, 2 channels), so I2C front ends fit the template as-is; SPI/UART parts need a different isolator.

## Tier 1 - best fit (in-water, cheap, I2C)

| Click (MIKROE-) | Core parts | Builds | Why it matters |
| --- | --- | --- | --- |
| pH 2 (5596) | MCP607 op-amp + MCP3221 12-bit I2C ADC + DS18B20 | Low-cost pH node | Replaces the Atlas pH OEM (biggest cost item, pH node $267 at N=1). Discrete AFE on VDD_ISO; needs good guarding/low-leakage layout and 2-point cal in firmware |
| TDS (6597) | CD4060B oscillator (AC excitation) + LMV324 + MCP3221, LP2985 | Low-cost conductivity/TDS/salinity | Alternative to Atlas EC OEM. AC drive avoids electrode plating. Range/accuracy for seawater (~53 mS/cm) needs checking; TDS probes target fresh water |
| Temp Probe (4301) | LTC2986 (RTD/thermistor/TC) | Precision water temp | Temperature compensation for pH/EC/DO; LTC2986 is SPI |
| RTD (2815) | MAX31865 | PT100/PT1000 water temp | Simple, well-known; SPI |
| RTD 4 (6966) | ADS122U04 (UART) | PT100 temp | UART would need UART isolation |
| Hydro Probe (4131) | MIC1557 oscillator + MCP3221 | Capacitive soil/media moisture | Hydroponics / planter node; I2C |

## Tier 2 - level, leak and flow-line sensing

| Click | Core parts | Builds | Notes |
| --- | --- | --- | --- |
| Moisture (3084) | FDC2112 capacitance-to-digital (I2C) | Non-contact level through a tank/sump wall | Electrodes on the outside of the container: no wetted parts, no isolation needed |
| Water Detect 2 (5820) | OPB350L250 optical tube sensor | Liquid present/absent in a clear tube (dosing lines, ATO) | GPIO out; non-isolated |
| Water Detect / 3 (2786, 5848) | MCP606 comparator + sense pads | Leak/flood alarm | GPIO to INT; very low power |
| Ultrasonic 5 (5804) | TUSS4470 transducer driver | Level with an external sealed transducer | Alternative to the A02YYUW module on feather_water_level |
| Ultrasonic 3 / 4 (4870, 6601) | TDK ICU-10201 / ICU-20201 | Small ToF level sensor | SPI; needs a protected/vented port above the water |
| TPS Pressure 500PG (6924) / Pressure 13 (4294) | Gauge pressure / KP229E2701 analog | Hydrostatic level via air tube (bubbler style) | Sensor stays dry; tube goes in the water |

## Tier 3 - environment around the tank / node

| Click | Core parts | Builds |
| --- | --- | --- |
| CO2 3 (5646) / NDIR CO2 (3134) | Infineon PAS CO2 / Figaro CDM7160 | Room CO2 (drives reef pH swings); PAS CO2 needs 12 V emitter supply - check |
| Temp&Hum 15 (4496), Environment 4 (5526) | SHT40 / SHT41 + SGP41 | Room temp/RH/VOC |
| Spectral 2 (2973), Light 5 (6905) | AS7262 6-ch / OPT4041 | Light-intensity/spectrum logger (rough PAR proxy, not a calibrated PAR meter) |
| UVA (4911), UV 3 (2736) | GUVA-C32SM / VEML6070 | UV lamp/steriliser check or outdoor UV |
| Temp ISO 2 (6999) | ISOTMP35R (5 kV reinforced) | Isolated temp on a heater/mains part |
| ISO ADC 5 (4758) | MAX22530 isolated 4-ch ADC | Isolated analog front end idea for future boards |

## Skip
- Ammonia (4151, MQ-137): gas-phase heater sensor, not dissolved ammonia; heater power far beyond VSENS.
- Ozone 3 (4654): air-side O3 only (ozone reactor exhaust), niche.
- Turbidity (4276, Amphenol TSD-10): appliance sensor, not sealed for immersion.
- LightRanger ToF (VL53/TMF88xx): optical ToF off a water surface is unreliable.
- EZO Carrier pH/ORP/EC/RTD, pH Click: Atlas modules we already use.

## Caveats
- MikroE publishes the schematics but I found no open-hardware licence; use them as reference circuits (they largely follow the IC datasheets), don't copy layouts or branding.
- Stock/price at DigiKey/Mouser not checked for any of these parts yet (parts-sourcing).
