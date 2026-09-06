<!-- release: v2.12.1240 -->

## What's Changed

**Keep Optimizer Explainer requests responsive**
The dashboard now applies a 35-second end-to-end response deadline to Optimizer Explainer Generate and Refresh requests. If Home Assistant, a browser proxy, or a network gateway does not return a response, the card leaves its loading state and shows a retryable response-timeout message. Refresh keeps the last successful explanation visible.

This changes only the dashboard request lifecycle. Optimizer planning, provider selection, API keys, battery/EV control, and hardware behavior are unchanged.

Update available via HACS
