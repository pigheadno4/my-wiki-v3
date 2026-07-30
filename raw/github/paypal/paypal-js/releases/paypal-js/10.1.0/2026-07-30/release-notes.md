### Minor Changes

- d9c0200: Narrow `PayPalMessagesSession.fetchContent` to return `Promise<MessageContent>` (previously `Promise<MessageContent | null>`). The evergreen SDK never resolves to `null` — on an API error it returns an empty sentinel `MessageContent` (empty `messageItems`) so the `<paypal-message>` element recognizes the error state and collapses. Existing `=== null` checks against the result become dead code but continue to compile.

### Patch Changes

- 09f2994: Fix incomplete prototype-pollution protection in `processOptions`. The `environment` option was still read via destructuring, which reads through the prototype chain, so `Object.prototype.environment = "sandbox"` could downgrade a production checkout to the sandbox SDK URL. `environment` is now read with a `hasOwnProperty` guard, matching the existing `sdkBaseUrl` protection.