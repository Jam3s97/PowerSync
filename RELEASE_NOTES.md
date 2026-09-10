<!-- release: v2.12.1269 -->
## What's Changed

- Added an optional local OpenAI-compatible plan-explanation provider, including Open WebUI-compatible chat-completions endpoints, a selected model, and optional write-only bearer authentication.
- Local endpoints are limited to private or loopback addresses, do not follow redirects, and preserve HTTPS certificate validation. HTTP is clearly identified as exposing household plan data and any bearer key on the local network.
- Added a separately opt-in automatic explanation refresh. It remains off by default; when enabled, only materially changed committed plans queue background work with debounce, cooldown, coalescing, and one provider request at a time.
- Generate and Refresh remain manual by default, and explanations remain descriptive-only with no effect on optimizer decisions or hardware commands.

Update available via HACS
