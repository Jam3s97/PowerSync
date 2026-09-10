<!-- release: v2.12.1270 -->

## What's Changed

**Sigenergy optimizer export target is retained during hardware refresh**
Sigenergy optimizer force-discharge commands now keep the planned battery-discharge target when the optimizer reissues its hardware control. This prevents a solar-rich site from falling back to PV-first discharge and satisfying the grid-export ceiling with solar alone when the optimizer selected battery export.

The configured PCC export limit, ESS discharge limit, Monitoring Mode and network-envelope safety gates remain unchanged. Manual targetless force-discharge controls keep their existing PV-first behaviour.

Update available via HACS
