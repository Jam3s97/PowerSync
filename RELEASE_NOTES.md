<!-- release: v2.12.1252 -->

## What's Changed

**Unavailable site telemetry stays visibly unavailable in the energy-flow dashboard**
When a battery coordinator has no current telemetry, the generated PowerSync dashboard keeps the energy-flow card available for diagnosis and displays `--` for unknown solar, grid, battery, and battery-SOC values. A measured zero remains `0`; PowerSync no longer draws flow arrows from synthetic zero values.

**EV loadpoint status no longer serializes stale site data as zero**
The canonical EV/loadpoint site snapshot now returns null core measurements when coordinator telemetry is explicitly stale or missing. Optimizer control remains fail-closed while the snapshot is unavailable; this release does not establish an inverter readback or physical effect.

Update available via HACS
