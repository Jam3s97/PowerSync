<!-- release: v2.12.1267 -->

## What's Changed

**Sigenergy optimizer exports now retain their battery target**
When the optimizer requests battery export, PowerSync now keeps that battery-discharge target separate from Sigenergy's site grid-export ceiling. A PV surplus can no longer satisfy the ceiling by itself while the optimizer reports Force Discharge active and the battery remains idle.

The correction uses the documented battery-priority Remote EMS discharge mode only for optimizer commands with an explicit battery target. Manual and automation force-discharge commands retain their existing whole-site export-target behaviour. The configured DNSP export ceiling and configured/rated ESS discharge cap remain enforced.

Update available via HACS
