# Braintree C45 fixed-query audit E — positions 17–20

Outcome: **PASS — 8/8 fixed questions.** No correction requested.

Timing (UTC): start `2026-10-07T13:50:38Z`; analysis end `2026-10-07T13:53:48Z`; handoff `2026-10-07T13:54:32Z`.

## Shared checks

- Scope is exactly manifest positions 17–20. The four primary raw SHA-256 values match the manifest pins: `0fa2cb…0b61`, `386e5e…c24d`, `ab5ac1…dd10`, and `57c87b…829d`.
- Every source target exists; its `canonical_url`, `raw_files` owner, raw header URL, and pinned raw object/action agree. Each canonical URL and factual raw path has exactly one source owner.
- Retrieval and reciprocity hold: `[[index]]` routes to `[[braintree-index]]`; the provider index routes to each main concept; each source links its concept and each concept links back to its source. Direct provider-catalog rows for these new pages are coordinator-close work and are not content failures.
- Bounded gap sweep found the settlement request/response and Control Panel siblings, native Mobile Checkout siblings, and Channel API retailer/retry plus generic Node webhook authorities. Only the retry delegation/contrast retained by position 20 required extra authority: the complete `keeping-track-of-retailers` source/raw and complete generic Node parse source/raw were read. Their HTTP-200-under-10-seconds/12-hour Channel API rule and HTTPS-`2xx`-within-30-seconds/environment-specific generic rule support the retained separation. No old snapshot was opened automatically.

## 17 — Settlement Batch Summaries (Node.js)

Route: `[[index]]` → `[[braintree-index]]` → `[[payment-reconciliation-reporting]]` → `[[source-braintree-docs-guides-reports-settlement-batch-summaries-node]]` → `[[raw/braintree/docs/guides/reports/settlement-batch-summaries/node-2026-09-16]]`.

- **Q1 — PASS; object/action match.** Braintree unversioned website guide, Node.js server SDK context; object is a date-scoped Settlement Batch Summary and action is `gateway.settlementBatchSummary.generate()`. It covers callback/Promise retrieval of `records` and optional one-custom-field grouping. It does not establish an exact SDK/package version, environment, account eligibility or merchant-account selection, actual report execution, transaction submission, settlement/funding/disbursement/deposit effect, completeness, timezone, or cutoff. **Locator:** source `## Overview`, `## Key takeaways`; primary raw lines 14–24, 27–41.
- **Q2 — PASS; matched report-generation answer.** The report displays total sales and credits for each batch on a specified settlement date; `groupByCustomField` is optional, and the shown record array is explicitly an example rather than a required/exhaustive schema. Exact calls, parameters, and displayed fields remain directly retrievable. **Locator:** primary raw line 16; callback lines 17–24; Promise lines 27–34; parameters lines 37–41; example structure lines 44–67.

## 18 — Client API Authorization

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-docs-reference-client-api-authorization]]` → `[[raw/braintree/docs/reference/client-api/authorization-2026-09-16]]`.

- **Q1 — PASS; object/action match.** Braintree unversioned Client API reference; object is the `authorizationFingerprint` carried by a client request and action is authorizing that Client API action, illustrated by listing payment methods. It is not Braintree Auth OAuth, a server gateway credential/action, payment authorization/completion, account/environment enablement, current endpoint support, or exact SDK/GitHub behavior. **Locator:** source `## Overview`, `## Key takeaways`; primary raw lines 14–24.
- **Q2 — PASS; matched fingerprint-retrieval answer.** The fingerprint is a signed collection of the merchant public ID and client-token-generation values and is contained in a client token. Tokens are JSON; versions 2+ base64-encode that JSON; content varies by requested version, and the minimal version-3 illustration shows `authorizationFingerprint`, `version`, and `configUrl` without promising an exhaustive stable schema. **Locator:** primary raw lines 23–29 and JSON lines 30–37.

## 19 — PayPal Mobile Checkout at JavaScript v3 route

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-paypal-mobile-checkout-javascript-v3]]` → `[[raw/braintree/docs/guides/paypal/mobile-checkout/javascript/v3-2026-09-16]]`.

- **Q1 — PASS; object/action match.** The URL is JavaScript v3-routed, but the evidence object is historical PayPal Mobile Checkout availability/removal for eligible merchants using custom native clients: Android v4.13+ and iOS v5.11+. The action is migration to the linked platform web-checkout routes. The body expressly excludes JavaScript and Drop-in; do not infer JavaScript implementation, native setup/tokenization, an exact removal version, current/package-qualified support, merchant enablement, migration success, or payment execution. **Locator:** source `## Overview`, `## Evidence boundaries`; primary raw removal line 17 and availability lines 20–21.
- **Q2 — PASS; matched availability/removal answer.** The notice says removal occurs in an unnamed next major version; eligible merchant and customer regions are US, Canada, Europe, and UK; other-region customers get the standard web experience; in-person PoS and multi-seller payments are unsupported. The page provides no implementation procedure beyond migration navigation. **Locator:** primary raw lines 16–17 and 20–27.

## 20 — PayPal Commerce Channel API Receiving Order Updates

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-webhooks]]` (with provider context `[[braintree-payment-platform]]`) → `[[source-braintree-docs-guides-paypal-commerce-channel-api-receiving-order-updates]]` → `[[raw/braintree/docs/guides/paypal-commerce-channel-api/receiving-order-updates-2026-09-16]]`.

- **Q1 — PASS; object/action match.** Braintree unversioned PayPal Commerce Channel API guide; object is a retailer ecommerce-system update for a channel-initiated order, materially retailer-confirmed fulfillment, and action is Braintree attempting an order-update webhook to the Channel API destination also used for retailer onboarding/offboarding messages. No SDK/version/environment is named; do not infer current API/channel/retailer eligibility, endpoint setup, successful delivery/user display/fulfillment, or payment authorization, capture, settlement, or funding. **Locator:** source `## Overview`, `## Key takeaways`; primary raw lines 14–19 and 35–37.
- **Q2 — PASS; matched order-update answer.** The illustrative message is `POST /paypal_notifications` with `topic: order`, `action: update`, and an `order` containing `partner_order_id` and `status: fulfilled`; it is not an exhaustive schema. Delivery is attempted immediately after retailer fulfillment confirmation. Retry/failure behavior is explicitly delegated: the retained Channel API authority requires HTTP 200 in under 10 seconds and otherwise several redeliveries over the next 12 hours with increasing delay; generic Node webhook signature/cadence/environment rules do not transfer. **Locator:** primary raw purpose/trigger lines 16–19, example lines 20–34, immediate-attempt/delegation lines 35–37; extra authority raw `keeping-track-of-retailers`, lines 62–67; generic-contrast raw `webhooks/parse/node`, lines 16–24 and 77–79.
