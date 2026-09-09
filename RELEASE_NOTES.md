<!-- release: v2.12.1266 -->

## What's Changed

**Manual Generic Charger failure details remain visible**
When a manual EV command reaches a known, safe rejection such as a configured Generic Charger switch or amps service failure, the dashboard now shows that safe boundary instead of replacing it with the generic “Command failed” message. Unexpected server errors remain server errors and their details are not exposed.

This identifies the PowerSync/HA command boundary only. A completed service call is not charger acknowledgement, charger readback, or proof of physical charging.

Update available via HACS
