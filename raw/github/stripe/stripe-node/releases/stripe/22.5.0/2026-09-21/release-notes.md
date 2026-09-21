* [#2805](https://github.com/stripe/stripe-node/pull/2805) Emit Claude Code plugin hint at module load time
  - Emits new Claude Code plugin hint when `CLAUDECODE` or `CLAUDE_CODE_CHILD_SESSION` environment variables are detected.
* [#2794](https://github.com/stripe/stripe-node/pull/2794) add/adjust event parsing helpers
  
  - Added methods that return their respective `Event`/`EventNotification` objects without verifying authenticity. Use them when you've previously verified an event (e.g. you verified, put the event in a queue, and are now processing). Supports events from [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge) and [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) natively.
    - `stripe.webhooks.constructEventWithoutVerification(payload)`
    - `stripe.constructEventWithoutVerification(payload)`
    - `stripe.parseEventNotificationWithoutVerification(payload)`
* [#2799](https://github.com/stripe/stripe-node/pull/2799) Add `stripe.major_api_version` constant

See [the changelog for more details](https://github.com/stripe/stripe-node/blob/v22.5.0/CHANGELOG.md).
