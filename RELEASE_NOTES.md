<!-- release: v2.12.1269 -->

## What's Changed

**Optional local OpenAI-compatible explanations**
You can now choose a local OpenAI-compatible chat-completions service, including Open WebUI-compatible endpoints, select its model, and optionally supply a write-only bearer key. The service is opt-in and continues to use the existing descriptive-only explanation experience.

**Local-network safeguards**
Configured local endpoints are restricted to private or loopback addresses, redirects are refused, and HTTPS certificate validation remains enabled. HTTP is explicitly identified as allowing household plan data and any bearer key to travel without transport encryption on the local network.

**Optional automatic refresh**
Automatic explanation generation is separately opt-in and remains disabled by default. When enabled, only materially changed committed plans queue background work; debounce, cooldown, coalescing, and a single in-flight request bound that work. Generate and Refresh continue to be manual by default, and explanations do not affect optimizer decisions or hardware commands.

Update available via HACS
