<!-- release: v2.12.1260 -->

## What's Changed

**EV status refresh now handles unavailable charging power safely**
When an active EV loadpoint has unavailable power, the canonical EV status
refresh now preserves that unknown display state without passing it into solar
surplus arithmetic. The EV API and dashboard remain available, while known
power from other loadpoints still contributes to the surplus estimate.

Update available via HACS
