<!-- release: v2.12.1262 -->

## What's Changed

**SolarEdge force controls now retain a confirmed cleanup timer when a replacement fails**
When a Force Charge, Force Discharge, or restore request is rejected or becomes
uncertain, PowerSync now keeps the previously confirmed local force state and
its expiry cleanup intact. A new state is published only after SolarEdge
confirms the replacement control transition.

**SolarEdge restore status remains coherent with confirmed control state**
PowerSync now clears force timers and user-visible force states together only
after SolarEdge confirms normal operation. Safety gates, monitoring mode,
reconciliation, and command confirmation remain fail-closed; no automatic
inverter retry is introduced.

Update available via HACS
