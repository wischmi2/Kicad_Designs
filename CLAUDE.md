You coordinate PCB and enclosure work.
- Send circuit and layout tasks to kicad-designer.
- Send firmware, devicetree and build tasks to firmware-dev.
- Send pre-fab and second-opinion design reviews to design-reviewer (read-only).
- Send BOM, stock, cost and part-substitution tasks to parts-sourcing.
- Send enclosure look, form and CMF concept work to industrial-designer. After Brian picks a concept, send it to fusion-enclosure to model.
- After a board change that affects the outline or connectors, send the STEP path and mechanical notes to fusion-enclosure.
- If fusion-enclosure reports a conflict, send it back to kicad-designer with the details.
- Run independent KiCad tasks in parallel; run Fusion tasks one at a time.
- Stop and ask Brian before architecture changes, fab output, or printing.
- End each session with a short report in C:\Personal-Agents\shared\reports\.
- In every subagent handoff, tell the agent to commit after each stage, and that if it is stuck on one problem for more than 10 minutes or 3 attempts, it stops that line of work and reports instead of trying more. Subagents have no SendMessage tool, so they can't send progress updates mid-run.
- While a background subagent runs, run a 5-minute cron check and show Brian a 2-4 line update. Use `git log --since="60 minutes ago"` (a bare date like "2026-10-25" means that date at the current time of day) and `ls -lt --time-style=+%m-%d_%H:%M` on the board folder. Don't judge progress from the task output file; it stays empty while the agent runs. Flag it as possibly stalled after 15 minutes with no commit or file change. After 25 minutes with no commit or file change, stop it with TaskStop (Brian 2026-10-25), then check `git status` in its folder, leave any uncommitted changes in place, and tell Brian what was stopped, its last commit and what's left uncommitted. Delete the cron when the agent finishes.
- Before each handoff, pick the cheapest model that can do the task well and pass it as `model` on the Agent call. Use Fable for RF and placement-critical layout (antenna, matching network, crystal, radio decoupling), new switching or isolated supply layouts, and reruns of tasks that failed or were caught by a review on Opus (Brian 2026-10-26). Use Opus for other layout and routing, design reviews, hard debugging and anything that sets placement or architecture. Use Sonnet for BOM and stock checks, STEP/ERC/DRC exports, STATUS.md updates, routine firmware builds and devicetree edits, concept research and write-ups, and Fusion edits to an existing model. Use Haiku for file moves and listings, and single kicad-cli runs. If a Sonnet or Haiku run fails, needs a redo, or misses something a review catches, rerun the task on Opus (Opus runs move up to Fable) and note it in the session report. Record the model and the outcome of each handoff in the session report, so the defaults can be tuned. parts-sourcing defaults to Sonnet in its agent file (Brian 2026-10-25); pass `model: "opus"` to override it.

## Status (keep updated)
- Done: 2026-10-23 wrote first STATUS.md for all six boards (ERC/DRC run with kicad-cli 10.0)
- Done: 2026-10-24 pouch gateway enclosure (Ledger, Abyss navy) modelled in Fusion; notes in shared\design\pouch_gateway\enclosure_ledger\. Waiting on Brian: brow print approach (fine layers, supports, or separate cap)
- Done: 2026-10-25 feather run 3: 6 of 7 unconnected fixed (SENS_SCL open), STEP 2026-10-25c. sens1 re-laid on the Feather outline, fully routed, STEP 2026-10-25. Feather enclosure concepts in shared\design\nrf54l15_feather\enclosure_concepts\. Report: shared\reports\2026-10-25-coordinator-feather-sens1-enclosure.md
- Done: 2026-10-25 sensor board template built (Sensor_Boards\feather_sensor_template, STEP 2026-10-25). Report: shared\reports\2026-10-25-coordinator-sensor-template.md. Waiting on Brian: H4 plating, isolated-supply default, SENSORS.md ID register, 3-ch isolator, FFC type
- Done: 2026-10-26 feather run 4: Brian routed SENS_SCL by hand (309ab2e); kicad-designer (Opus) fixed the 3 new DRC errors (2a074ab). DRC 4 errors (J1, accepted), 0 unconnected, 0 parity. STEP 2026-10-26. Branch not pushed: git auth fails from agent shells, Brian pushes manually
- Waiting on Brian (2026-10-25): X1.4 via-in-pad, sens1 antenna-corner keep-out, sens1 gap/standoffs/R5/interrupt, enclosure concept and use environment (full list in the report)
- Waiting on Brian: the other "Questions for Brian" in each STATUS.md
- Tooling: 2026-10-23 confirmed kicad-designer has working kicad-pro MCP (v4.4.0, kicad-cli 10.0.4), kicad MCP (swig backend) and WebFetch; no live KiCad GUI/IPC link. LCSC pages don't show stock, so use JLCPCB or the MCP lookup tools for stock checks
- Done: 2026-10-25 feather_water_level set up (non-isolated, ERC/DRC clean, STEP 2026-10-25; Sensor sheet circuit not drawn yet). Parts: shared\design\feather_water_level\parts.md (JST PH 4-pin, TPS63802). Enclosure concepts: shared\design\feather_water_level\enclosure_concepts\ (Bead recommended). Report: shared\reports\2026-10-26-coordinator-atlas-boards-restart.md. Waiting on Brian: sensor connector, container type, enclosure concept, battery target, probe measurements
- Stopped 2026-10-25 22:14 (session ended, no report): industrial-designer atlas_probe_nodes enclosure concepts (3 SVGs only, no concepts.md, shared\design\atlas_probe_nodes\enclosure_concepts\). Not restarted yet
- Done: 2026-10-26 feather_orp, feather_dissolved_oxygen, feather_conductivity placed, routed, ERC/DRC clean (0 unconnected, 0 parity), STEP 2026-10-26 in shared\handoff\<board>\. Report: shared\reports\2026-10-26-coordinator-atlas-boards-restart.md. Waiting on Brian: VDD_ISO 3.0 V at Atlas minimum (VBAT-fed isolated supply?), one Atlas footprint for all boards, SENSORS.md register, INT poll-only, EC connector/K value. Design review before fab
- Tooling: 2026-10-26 kicad MCP sync_schematic_to_board wrote the board despite reporting a refused save; use KiCad Python for schematic-to-board updates
- Next steps:
- Decisions made: 2026-10-23 the active boards are nrf54l15_feather (main) and nrf54l15_feather_sens1 (pH sensor). v4 is paused in favour of the Feather form factor; ph_sensor is superseded by sens1. 2026-10-25 (Brian): one sensor board per feather, each node in its own enclosure (e.g. pH node, salinity node). CN1 stays point-to-point and the SENS_ID resistor tells firmware the board type. New sensor boards start from Sensor_Boards\feather_sensor_template (built 2026-10-25). 2026-10-25 (Brian): first new sensor board is feather_water_level (ultrasonic from above, A02YYUW, UART), non-isolated, sensor on a 3.3 V buck-boost from VBAT with EN = VSENS; enclosure gets several options in the same family as the other enclosures.

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
| Feather sensor template | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_sensor_template | STATUS.md |
| Feather water level (new, ultrasonic) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_water_level | STATUS.md |
| Feather ORP (Atlas ORP OEM, isolated) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_orp | STATUS.md |
| Feather dissolved oxygen (Atlas DO OEM, isolated) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_dissolved_oxygen | STATUS.md |
| Feather conductivity (Atlas EC OEM, isolated) | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\Sensor_Boards\feather_conductivity | STATUS.md |
| XIAO pogo stack | C:\Personal-Agents\worktrees\nrf54l15-feather-branch\xiao_breakout | STATUS.md |
