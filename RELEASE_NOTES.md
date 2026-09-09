<!-- release: v2.12.1265 -->

## What's Changed

**Generic Charger manual-start diagnostics**
Manual Generic Charger starts now report the safe failed boundary when Home Assistant rejects a configured amps or switch service, such as `number.set_value` or `switch.turn_on`. This makes a dashboard failure actionable without exposing provider exception text.

The result still distinguishes a completed Home Assistant service call from later switch readback, charger acknowledgement, and measured charging power. This release does not change charger control eligibility or claim that an EV began charging.

Update available via HACS
