<!-- release: v2.12.1238 -->

## What's Changed

**Scheduled updates now continue correctly after midnight**
When a late-evening PowerSync auto-update schedule is delayed past midnight, its four-hour retry window now remains active. The scheduler also records the original scheduled day, preventing duplicate attempts after restart while allowing the following evening's schedule to run normally.

Update available via HACS
