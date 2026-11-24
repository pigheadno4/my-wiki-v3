# Stripe S06 proposed changed-capture review

S01–S05 independently reviewed 450 of the 512 changed captures. S06 proposes the remaining 62, each mapped to a different existing summary. Completing this review would leave zero changed captures awaiting review.

The target is 100 captures per round. S06 closes the changed-capture queue with 62. All 4,265 new candidates remain queued for separate semantic triage.

The manifest pins the old and new captures, current summary and stored diff for each job. The review requires 124 answers and three fixed coordinator audits. The S05 publication refreshed the existing Legacy APIs summary pin used by the Sources comparison. The Terminal landing-page pair retains its historical Stripe host spelling for review.

The company header still lists 666 sources against 668 Stripe-owned source pages. All 62 selected summaries are linked from both the Stripe company page and index.

Status is awaiting exact review-scope approval.

[Exact manifest](manifest.proposed.json) · [Provider contract](dispatch-contract.proposed.md) · [Query prompts](proposed-queries.md) · [Activation context](activation-context.proposed.json) · [Preflight](preflight-validation.json)

## Scope by documentation section

| Section | Captures |
| --- | ---: |
| radar | 11 |
| receipts | 1 |
| recurring-payments | 1 |
| refunds | 1 |
| sdks | 1 |
| secure-remote-commerce | 1 |
| sources | 1 |
| strong-customer-authentication | 1 |
| subscriptions | 3 |
| terminal | 41 |

## Review jobs

| Canonical URL | Existing summary |
| --- | --- |
| https://docs.stripe.com/radar/pay-as-you-go-abuse | `wiki/sources/source-stripe-radar-payg-abuse.md` |
| https://docs.stripe.com/radar/radar-session | `wiki/sources/source-stripe-radar-sessions.md` |
| https://docs.stripe.com/radar/reviews/auth-and-capture | `wiki/sources/source-stripe-radar-reviews-auth-capture.md` |
| https://docs.stripe.com/radar/reviews/risk-insights | `wiki/sources/source-stripe-radar-risk-insights.md` |
| https://docs.stripe.com/radar/risk-settings | `wiki/sources/source-stripe-radar-risk-settings.md` |
| https://docs.stripe.com/radar/rules | `wiki/sources/source-stripe-radar-rules.md` |
| https://docs.stripe.com/radar/rules/disputes | `wiki/sources/source-stripe-radar-rules-disputes.md` |
| https://docs.stripe.com/radar/rules/reference | `wiki/sources/source-stripe-radar-rules-reference.md` |
| https://docs.stripe.com/radar/rules/supported-attributes | `wiki/sources/source-stripe-radar-rules-supported-attributes.md` |
| https://docs.stripe.com/radar/supported-payment-methods | `wiki/sources/source-stripe-radar-supported-payment-methods.md` |
| https://docs.stripe.com/radar/testing | `wiki/sources/source-stripe-radar-testing.md` |
| https://docs.stripe.com/receipts | `wiki/sources/source-stripe-receipts.md` |
| https://docs.stripe.com/recurring-payments | `wiki/sources/source-stripe-recurring-payments-overview.md` |
| https://docs.stripe.com/refunds | `wiki/sources/source-stripe-refunds.md` |
| https://docs.stripe.com/sdks/stripejs-react | `wiki/sources/source-stripe-react-stripejs.md` |
| https://docs.stripe.com/secure-remote-commerce | `wiki/sources/source-stripe-secure-remote-commerce.md` |
| https://docs.stripe.com/sources | `wiki/sources/source-stripe-legacy-apis.md` |
| https://docs.stripe.com/strong-customer-authentication | `wiki/sources/source-stripe-sca-readiness.md` |
| https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing | `wiki/sources/source-stripe-flat-rate-pricing.md` |
| https://docs.stripe.com/subscriptions/pricing-models/per-seat-pricing | `wiki/sources/source-stripe-per-seat-pricing.md` |
| https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing | `wiki/sources/source-stripe-tiered-pricing.md` |
| https://docs.stripe.com/terminal | `wiki/sources/source-stripe-terminal-overview.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/app-review | `wiki/sources/source-stripe-terminal-apps-on-devices-app-review.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/build | `wiki/sources/source-stripe-terminal-apps-on-devices-build.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/monitor | `wiki/sources/source-stripe-terminal-apps-on-devices-monitor.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/overview | `wiki/sources/source-stripe-terminal-apps-on-devices.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/submit | `wiki/sources/source-stripe-terminal-apps-on-devices-submit.md` |
| https://docs.stripe.com/terminal/features/apps-on-devices/troubleshooting | `wiki/sources/source-stripe-terminal-apps-on-devices-troubleshooting.md` |
| https://docs.stripe.com/terminal/features/collect-data | `wiki/sources/source-stripe-terminal-collect-data.md` |
| https://docs.stripe.com/terminal/features/collect-inputs | `wiki/sources/source-stripe-terminal-collect-inputs.md` |
| https://docs.stripe.com/terminal/features/collect-nfc-data | `wiki/sources/source-stripe-terminal-collect-nfc-data.md` |
| https://docs.stripe.com/terminal/features/collecting-tips/on-reader | `wiki/sources/source-stripe-terminal-on-reader-tipping.md` |
| https://docs.stripe.com/terminal/features/collecting-tips/on-receipt | `wiki/sources/source-stripe-terminal-on-receipt-tipping.md` |
| https://docs.stripe.com/terminal/features/display | `wiki/sources/source-stripe-terminal-display-cart.md` |
| https://docs.stripe.com/terminal/features/extended-authorizations | `wiki/sources/source-stripe-terminal-extended-authorizations.md` |
| https://docs.stripe.com/terminal/features/incremental-authorizations | `wiki/sources/source-stripe-terminal-incremental-authorizations.md` |
| https://docs.stripe.com/terminal/features/receipts | `wiki/sources/source-stripe-terminal-receipts.md` |
| https://docs.stripe.com/terminal/features/refunds | `wiki/sources/source-stripe-terminal-refunds.md` |
| https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment | `wiki/sources/source-stripe-terminal-save-after-payment.md` |
| https://docs.stripe.com/terminal/features/saving-payment-details/save-directly | `wiki/sources/source-stripe-terminal-save-directly.md` |
| https://docs.stripe.com/terminal/fleet/admin-menu-passcode | `wiki/sources/source-stripe-terminal-admin-menu-passcode.md` |
| https://docs.stripe.com/terminal/fleet/cellular | `wiki/sources/source-stripe-terminal-cellular-config.md` |
| https://docs.stripe.com/terminal/fleet/configurations-overview | `wiki/sources/source-stripe-terminal-configurations.md` |
| https://docs.stripe.com/terminal/fleet/locations-and-zones | `wiki/sources/source-stripe-terminal-locations-and-zones.md` |
| https://docs.stripe.com/terminal/fleet/offline-mode | `wiki/sources/source-stripe-terminal-offline-mode-config.md` |
| https://docs.stripe.com/terminal/fleet/order-and-return-readers | `wiki/sources/source-stripe-terminal-order-and-return-readers.md` |
| https://docs.stripe.com/terminal/fleet/reboot-time | `wiki/sources/source-stripe-terminal-reboot-time.md` |
| https://docs.stripe.com/terminal/fleet/register-readers | `wiki/sources/source-stripe-terminal-register-readers.md` |
| https://docs.stripe.com/terminal/fleet/splash-screen | `wiki/sources/source-stripe-terminal-splash-screen.md` |
| https://docs.stripe.com/terminal/fleet/tipping | `wiki/sources/source-stripe-terminal-tipping-config.md` |
| https://docs.stripe.com/terminal/fleet/wifi | `wiki/sources/source-stripe-terminal-wifi-config.md` |
| https://docs.stripe.com/terminal/mobile-readers | `wiki/sources/source-stripe-terminal-mobile-readers.md` |
| https://docs.stripe.com/terminal/readers/bbpos-wisepad3 | `wiki/sources/source-stripe-terminal-bbpos-wisepad3.md` |
| https://docs.stripe.com/terminal/readers/bbpos-wisepos-e | `wiki/sources/source-stripe-terminal-bbpos-wisepos-e.md` |
| https://docs.stripe.com/terminal/readers/stripe-m2 | `wiki/sources/source-stripe-terminal-stripe-m2.md` |
| https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710 | `wiki/sources/source-stripe-terminal-s700-s710.md` |
| https://docs.stripe.com/terminal/references/api/js-sdk | `wiki/sources/source-stripe-terminal-js-sdk-reference.md` |
| https://docs.stripe.com/terminal/references/sdk-migration-guide | `wiki/sources/source-stripe-terminal-sdk-migration-guide.md` |
| https://docs.stripe.com/terminal/references/sdk-v3-migration-guide | `wiki/sources/source-stripe-terminal-sdk-v3-migration-guide.md` |
| https://docs.stripe.com/terminal/references/sdk-v4-migration-guide | `wiki/sources/source-stripe-terminal-sdk-v4-migration-guide.md` |
| https://docs.stripe.com/terminal/smart-readers | `wiki/sources/source-stripe-terminal-smart-readers.md` |
| https://docs.stripe.com/terminal/tap-to-pay-readers | `wiki/sources/source-stripe-terminal-tap-to-pay-readers.md` |
