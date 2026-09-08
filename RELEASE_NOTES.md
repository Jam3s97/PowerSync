<!-- release: v2.12.1250 -->

## What's Changed

**SolarEdge confirmed force-charge state is kept truthful if restart persistence fails**
When SolarEdge confirms a manual force-charge command and its expiry timer is armed, a later failure to save restart state no longer turns the service into a generic failure or clears the active state. PowerSync now reports the confirmed force charge as active with a warning that only restart persistence needs attention, matching the existing force-discharge behaviour.

Update available via HACS
