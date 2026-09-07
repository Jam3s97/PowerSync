<!-- release: v2.12.1242 -->

## What's Changed

**Fronius load-following now fails closed on stale telemetry**
PowerSync will no longer turn a retained Fronius GEN24 site snapshot into a new AC-inverter power limit when the upstream telemetry refresh has failed, is not ready, or is too old. Existing limits are left unchanged until a fresh sample is available, preventing obsolete home-load values from being re-applied during uneconomic export.

**Safer zero-load and recovery behaviour**
A valid zero-watt home-load sample remains usable. The AC-curtailment status continues to distinguish a verified inverter register limit from physical export convergence.

Update available via HACS
