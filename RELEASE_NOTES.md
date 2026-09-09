<!-- release: v2.12.1261 -->

## What's Changed

**Sungrow solar curtailment now recovers safely after a reload**
PowerSync records ownership and the prior export-limit setting before it applies
a temporary Sungrow zero-export curtailment. If Home Assistant reloads while
that temporary limit is active, PowerSync restores the captured setting instead
of leaving solar output constrained while reporting normal operation.

**Existing inverter limits remain protected**
PowerSync only restores a limit it recorded as its own. A native Sungrow, DNSP,
or other-controller export limit is left unchanged when ownership is unknown.

Update available via HACS
