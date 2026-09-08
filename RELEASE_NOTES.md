<!-- release: v2.12.1251 -->

## What's Changed

**SolarEdge manual force-discharge max power works with an inactive network envelope**
Manual Force Discharge requests that leave Power (W) at 0 or blank now reach the inverter's rated/BMS maximum when Network Export Envelope is off, as documented. Active, monitoring, faulted, or changed envelopes continue to block that unbounded request before an actuator write.

**Tesla Fleet flow display no longer presents stale charge power as live**
Tesla Fleet charge-power readings older than the shared 90-second freshness limit are now marked unavailable across PowerSync's EV status surfaces. This prevents a stale value from being shown as a live EV draw in the energy-flow display while site accounting has already rejected it.

Update available via HACS
