### Minor Changes

- 7689364: Add v6 types for `updateClientToken()` on the SDK instance
- 051a03e: Increase the v6 `loadCoreSdkScript` per-attempt script load timeout from 30 seconds to 60 seconds so slow networks have more time to load the Core SDK script before the load is reported as timed out.

### Patch Changes

- 83e6ca1: Only treat a v6 SDK on the window namespace as a loaded V6 core script, so a v5 SDK already on `window.paypal` no longer resolves `loadCoreSdkScript` after a failed or timed out load.