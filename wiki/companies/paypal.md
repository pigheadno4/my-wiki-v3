---
title: "PayPal"
type: company
tags: [paypal, payment-gateway, checkout, venmo, javascript-sdk, orders-api, vault, recurring-payments, payouts, disputes, reporting, agentic-commerce]
source_count: 160
---

## PayPal

PayPal is one of the world's largest online payment platforms, offering consumer wallets, merchant payment processing, and developer APIs. It owns Venmo and operates the PayPal Checkout product for e-commerce integrations.

## Key Products

### PayPal Checkout

Standard e-commerce integration that renders PayPal, Venmo, and Debit/Credit Card buttons on merchant websites via the JavaScript SDK. Supports both pop-up-based checkout and inline card fields.

### PayPal JS SDK

Client-side SDK injected via `<script>` tag. Renders payment buttons on the page and manages the checkout pop-up lifecycle. Accessed globally via `window.paypal`. Handles:

- Button rendering (PayPal, Venmo, Debit/Credit Card)
- `createOrder` / `onApprove` / `onShippingAddressChange` / `onShippingOptionsChange` callbacks
- Checkout pop-up launch and management

The package-qualified v6 surface in `@paypal/paypal-js@9.8.0` supports direct instance creation with client ID or client token, conditional components for PayPal, Venmo, guest payments, messages, subscriptions, Card Fields, Apple Pay, and Google Pay, plus eligibility hydration. `@paypal/react-paypal-js@9.3.0` exposes this integration through the `/sdk-v6` subpath. In the coordinated `10.0.0` releases, both the core v6 loader and React `PayPalProvider` require an explicit `production` or `sandbox` environment; the client ID does not choose the endpoint. Core `10.0.1` adds typed v6 DOM custom elements and legacy Buttons Venmo vault-without-purchase setup-token approval data, while React `10.1.0` requires the same environment choice for server eligibility. Core `10.0.2` corrects `/sdk-v6` resolution for condition-sensitive bundlers; React `10.1.1` only relocates v5 Storybook tooling. Core `10.0.3` adds v6 Venmo save-payment types that conflict with older product availability guidance; React `10.1.2` removes the ineffective Apple Pay disabled prop and types the Messages `TEXT` logo. Core `10.1.0` rejects inherited loader environment values and changes Messages failures to empty content, while React `10.2.0` adds Braintree Messages and corrects server eligibility naming and hydration reuse. React `10.2.1` coordinates server hydration with the client eligibility hook so no-payload SSR consumers do not issue a competing fetch.

The independent `paypal/paypal-checkout-components` history begins with `@paypal/checkout-components@4.1.47` and now extends through `5.0.425`. The v4 runtime implemented Zoid-based Buttons and Checkout with mobile-only secondary Venmo. The accumulated v5 runtime adds separate Card Fields, Payment Fields, Hosted Buttons, Wallet, Saved Payment Methods, Venmo, and QR component boundaries; its Venmo vault-without-purchase path is experiment-gated. These package-qualified facts do not replace current availability guidance.

### Braintree PayPal v6

Braintree merchants use a separate React provider backed by Braintree's `paypalCheckoutV6` module and a server-generated Braintree client token. React 9.3.0 provides one-time, billing-agreement, and checkout-with-vault flows; React 10.1.0 adds eligibility-gated Pay Later with a prebuilt button and custom hook; React 10.2.0 adds promotional and BNPL Messages with asynchronous instance creation and content fetching. Approval flows are tokenized into a Braintree payment-method nonce and completed with a Braintree server SDK, not PayPal's Orders API. See [[paypal-braintree-integration]].

### PayPal Orders REST API

Server-side API for order lifecycle management:

- `POST /v2/checkout/orders` — create order
- `POST /v2/checkout/orders/{orderID}/capture` — capture payment after buyer approval
- Also supports retrieve, update, and authorize operations

### PayPal Server SDK

Official server-side SDKs wrapping the REST API. Available for Node.js (`@paypal/paypal-server-sdk`), Java, PHP, Python, Ruby, and .Net.

### Venmo

PayPal-owned peer-to-peer payment network; surfaced as a payment button option in PayPal Checkout for US buyers. Two checkout flows: mobile (app switch) and desktop (QR code scan). US merchants + US buyers only, USD only. Buyers must have the Venmo app installed. Supported features: one-time payments, auth+capture, save during purchase, shipping module. Not supported: multi-seller payments, contact module, buy-now-pay-later.

`@paypal/paypal-js@10.0.3` declares a v6 Venmo save-payment session for vault setup without a purchase, contradicting the older product documentation's save-for-purchase-later limitation. Treat this as unresolved package-versus-product evidence until current runtime and merchant eligibility are confirmed.

## Developer Experience

- **Auth**: Client ID + Client Secret from Developer Dashboard. Access token for REST API calls.
- **Sandbox**: Full sandbox environment with personal and business test accounts creatable from Developer Dashboard.
- **Button placement**: Recommended on product detail pages, cart pages, and checkout pages.
- **Checkout flow**: Two-step — create order on server, capture order after buyer approves.

## Checkout Integration Flow

1. Load PayPal JS SDK via `<script>` tag
2. SDK renders buttons → buyer clicks → `createOrder` callback fires
3. Merchant server: `POST /v2/checkout/orders` → get Order ID
4. SDK launches checkout pop-up with Order ID
5. Buyer logs in, reviews order (default shipping address + shipping options from Orders API)
6. Buyer approves → `onApprove` callback fires
7. Merchant server: `POST /v2/checkout/orders/{orderID}/capture`
8. Payment complete

## PayPal Vault (Payment Method Tokens)

Tokenization system for storing buyer payment methods for future merchant-initiated charges. Used for subscriptions and recurring billing.

- **Setup token**: created during buyer consent flow; expires in 3 days; holds billing plan details
- **Payment token** (vault ID): persistent stored credential; used as `vault_id` in Orders API for subsequent charges
- **APIs**: Payment Method Tokens v3 API (`VaultController` in server SDK)
- **`stored_credential`**: required on recurring charge orders — includes `payment_initiator: "MERCHANT"`, `usage: "SUBSEQUENT"`, `usage_pattern`
- US buyers and merchants only (for the recurring payments module)

### Save during purchase (vault at checkout)

Supported for cards, PayPal Wallets, and Venmo via `payment_source.*.attributes.vault.store_in_vault: ON_SUCCESS` in the Create Order call. Available across JS SDK, Android SDK, and iOS SDK. 35-country support for cards; Venmo is US-only.

| Integration | Returning payer identification |
| --- | --- |
| JS SDK (cards/PayPal) | `target_customer_id` in user ID token request |
| Android SDK (cards) | `customer.id` in Create Order body |
| iOS SDK (cards) | `customer.id` in Create Order body |

APPROVED vs VAULTED: if `vault.status: APPROVED`, subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook.

See [[paypal-vault]] and [[paypal-subscriptions]].

## PayPal Subscriptions & Recurring Payments

Two paths for merchant-initiated recurring charges:

- **Orders API + Vault**: flexible; supports all 8 `usage_pattern` values (SUBSCRIPTION/RECURRING/UNSCHEDULED/INSTALLMENT × PREPAID/POSTPAID); works with cards, PayPal Wallet, Venmo; requires `stored_credential` on every MIT
- **Subscriptions API**: structured lifecycle (create product → plan → subscribe → charge automatically); up to 3 billing cycles per plan; 4 pricing models (fixed, quantity, volume, tiered); dashboard or REST API

See [[paypal-subscriptions]] and [[paypal-vault]].

## PayPal Payouts

Mass disbursement product for sending money to multiple recipients. Two tiers:

- **Standard**: 96 countries, 24 currencies, self-serve, 3 integration options (API / Large Batch SFTP / Payouts Web)
- **Advanced (Hyperwallet)**: 240+ countries, 50+ currencies, enterprise onboarding, additional rails (prepaid card, check, cash)

Key constraints: max 15,000 items per API call; $20,000 individual payout limit; funded from PayPal balance; Venmo US+USD only. Cancel only works on UNCLAIMED items (30-day auto-return). API rate limit: 400 POST/minute.

See [[paypal-payouts]] and [[source-paypal-payouts-overview]].

## Disputes

Two resolution paths for buyer-initiated transaction challenges:

- **Resolution Center**: no-code web UI; 9 manual actions (view, message, offer, escalate, accept, evidence, appeal, etc.)
- **Disputes API**: programmatic; base path `/v1/customer/disputes`; 9 action endpoints; HATEOAS-driven

Lifecycle: INQUIRY (20 days) → CHARGEBACK → PRE_ARBITRATION → ARBITRATION → RESOLVED. Key window: buyer has 180 days to file; PayPal adjudicates within 10 days of escalation. Pre-chargeback alert: 20-hour window to refund and avoid fees.

> [!warning] `CHARGEBACK` stage ≠ card chargeback — it's PayPal's internal label for an escalated claim. Check `dispute_channel` (INTERNAL vs EXTERNAL).

See [[disputes]] and [[source-paypal-disputes-api]].

## Reports & Analytics

Business data access across two tracks:

- **No-code**: Dashboard Downloads (CSV/PDF/TAB/IIF/QIF), Scheduled Reports via SFTP (Transaction Detail Report available by 12 PM daily), Basic Analytics
- **Pro-code**: Transaction Search API (`GET /v1/reporting/transactions`, 3-hour latency, 3-year history), Reporting APIs (DAILY/WEEKLY/MONTHLY schedules), Webhooks

**Activity Download Report**: 87 fields, 7-year retention, 12-month max per request, 50k row limit per CSV/TAB file (ZIP for larger).

See [[payment-reconciliation-reporting]] and [[source-paypal-reports-analytics]].

## Agentic Commerce

AI-powered shopping infrastructure enabling conversational purchasing. Access is gated (requires PayPal AI team approval).

- **Store Sync**: opens store to AI shopping assistants — product catalog integration + cart/order operations; partners: Wix, Cymbio, BigCommerce, Feedonomics, Shopware
- **Agent Ready**: accept payments via AI assistants (e.g. ChatGPT bots) using existing PayPal tools; PayPal handles cross-platform security and compatibility

See [[agentic-commerce]] and [[source-paypal-agentic-commerce]].

## App Switch (Mobile)

PayPal supports deep-linking into the native PayPal app on mobile ("App Switch"). Configuration:

- **Client**: `appSwitchWhenAvailable: true` in Buttons config; call `buttons.resume()` if `buttons.hasReturned()`
- **Server**: `appSwitchPreference.launchPaypalApp: true` + matching `returnUrl`/`cancelUrl` in `experienceContext`

## Error Handling Patterns

- `INSTRUMENT_DECLINED` (funding failure) → call `actions.restart()` to let buyer pick another payment method
- `onError` callback → catch-all; redirect to error page
- `onCancel` callback → buyer cancelled; return to cart

## Refunds

Via `PaymentsController.refundCapturedPayment({ captureId })` — server-side only, using `@paypal/paypal-server-sdk`.

## Sources

- [[source-paypal-agent-toolkit]] — Agent toolkit: 6 frameworks (Bedrock/CrewAI/LangChain/MCP/OpenAI/Vercel), TypeScript + Python, MCP config, 6 commerce agent types, Next.js frontend
- [[source-paypal-ai-developer-tools]] — PayPal AI developer tools: 3 paths (agent toolkit/LLM integration+MCP server/agentic commerce); agents handle payments/subscriptions/disputes/invoicing; PCI-compliant
- [[source-paypal-security-guidelines]] — Security guidelines: 12 principles, TLS 1.2+, webhook sig verification, CSP+SRI for SDK, OAuth examples in 7 languages, security tools table
- [[source-paypal-js-sdk-v6-setup]] — JS SDK v6 setup: script URLs, clientToken 15min expiry + domains[], 8 components, eligibility API, Pay Later/Credit sessions, web components, security rules
- [[source-paypal-orders-api-troubleshooting]] — Orders v2 troubleshooting: 31 error codes, 503/SERVICE_UNAVAILABLE, ORDER_ALREADY_AUTHORIZED/PAYER_ACTION_REQUIRED/PAYEE_NOT_CONSENTED fixes, 4 error samples
- [[source-paypal-payment-failures]] — Payment failures: 19 error codes (INSTRUMENT_DECLINED/CANNOT_BILL_PAST_DUE_BALANCE/REJECTED_DUE_TO_RISK_REVERSAL/etc.), actions.restart(), async failures, intelligent retry, webhook events (Orders+Subscriptions)
- [[source-paypal-rest-api-get-started]] — REST API getting started: OAuth token via POST /v1/oauth2/token (Basic Auth); expires_in 31668s; Business account required for go-live/non-US; sandbox personal+business accounts
- [[source-paypal-agent-ready]] — Agent Ready: Braintree-only ACP integration; ChatGPT app via requestCheckout(); MCP complete_checkout tool; allowance validation (4 fields); transaction.facilitator_details.oauth_application_name tracking
- [[source-paypal-store-sync-api-spec]] — Store Sync Cart API OpenAPI spec (v1.2.0, 2757 lines): PayPalCart schema, ValidationIssue typed contexts, CartTotals formula, 12 CheckoutField types, BusinessError structure
- [[source-paypal-store-sync-product-catalog]] — Store Sync product catalog: 3 feed specs (Google/OpenAI ACP/PayPal Enhanced), is_eligible_search/checkout flags, variant handling, 4GB limit, troubleshooting
- [[source-paypal-agentic-commerce]] — Agentic Commerce: Store Sync (product catalog + cart for AI assistants) + Agent Ready (payments via ChatGPT bots); gated access; partners: Wix/Cymbio/BigCommerce/Feedonomics/Shopware
- [[source-paypal-reports-fields-formats]] — Activity Download Report field reference: 87 fields, 5 formats (PDF/CSV/TAB/IIF/QIF), 50k row limit, 7yr retention, mandatory/selected/unselected states, Status values, Payment Source 20+ values
- [[source-paypal-reports-analytics]] — Reports & Analytics overview: no-code (dashboard/scheduled/basic) vs pro-code (Transaction Search API/Reporting APIs/Webhooks); CSV/PDF/JSON output
- [[source-paypal-disputes-api]] — Disputes API: 9 endpoints, INQUIRY→CHARGEBACK→PRE_ARBITRATION→ARBITRATION lifecycle, HATEOAS-driven actions, Accelerated Response, webhook pattern
- [[source-paypal-disputes-overview]] — Disputes overview: internal (180-day window, 20-day amicable, 10-day PayPal adjudication) vs external (chargeback + ACH return); pre-chargeback alert 20-hour refund window; 6 buyer issue types; 2 flow diagrams
- [[source-github-paypal-v6-samples]] — GitHub v6-web-sdk-sample-integration: 36 files, all payment flows (PayPal, card fields, Venmo, Google Pay, Apple Pay, ACH, SEPA, 6 EU APMs, subscriptions)
- [[source-github-paypal-js-v6]] — GitHub paypal/paypal-js: SDK v6 + React v9 source; PayPalProvider internals, session hook impl, card fields context, SSR utils, types
- [[source-npm-react-paypal-js-v9]] — @paypal/react-paypal-js v9.1.1 (SDK v6): PayPalProvider, 8 button components, session hooks, card fields, SSR, v8→v9 migration guide
- [[source-paypal-donate-sdk]] — Donate SDK: pop-up overlay, hosted_button_id vs business param, onComplete callback, multiple buttons on same page
- [[source-paypal-payment-method-tokens-api]] — Payment Method Tokens API v3: cards + PayPal wallet, setup→payment token, HATEOAS, SAQ D for cards, billing agreement for PayPal
- [[source-paypal-guest-payments-sdk-v6]] — Guest Payments SDK v6: paypal-guest-payments component, 3 patterns (standard/auto-start/shipping), onWarn shape
- [[source-paypal-card-fields-sdk-v6]] — Card Fields SDK v6: hosted iframes, advanced_cards eligibility, submit() 3 states, liabilityShift, PCI SAQ A-EP
- [[source-paypal-troubleshoot]] — Troubleshoot JS SDK v6: button not appearing, Invalid Client, multipage scoping/race condition fixes
- [[source-paypal-save-payment-method]] — Save PayPal for future payments: vault flow, token path, server-side charges (docs.paypal.ai)
- [[source-paypal-split-shipments]] — Split shipments: multiple purchase_units per order, each with own address and amount
- [[source-paypal-reauthorize]] — Reauthorize: extend holds days 4–29, 115% amount limit, single-use, new auth ID returned
- [[source-paypal-bopis]] — BOPIS: authorize at checkout, capture at pickup verification, 7-day/24-hour hold windows
- [[source-paypal-delayed-capture]] — Delayed capture: AUTHORIZE intent, 3-day honor period, 29-day expiry, partial captures
- [[source-paypal-void-authorization]] — Void authorization: Payments API v2, all-or-nothing, saves fees vs refund, expiry timing
- [[source-paypal-refund-payment]] — Refund integration: Payments API v2, full/partial, 180-day window, error codes, void vs refund tip
- [[source-paypal-payments-quickstart]] — Quickstart integration guide: JS SDK v6 + API-only flows, negative testing, shipping preferences, go-live checklist
- [[source-paypal-standard-payments]] — Standard payments overview: capture flows, use cases, sub-feature index (docs.paypal.ai, SDK v6)
- [[source-paypal-checkout-getting-started]] — Official getting started guide for PayPal Checkout integration
- [[source-paypal-checkout-integrate-one-time-payment]] — Full frontend + backend integration guide with code samples
- [[source-paypal-checkout-recurring-payment]] — Recurring payments / vault integration guide
- [[source-paypal-best-practices-pay-with-paypal]] — Best practices: three payment flows (one-time, recurring, vaulted)
- [[source-paypal-best-practices-one-time-payment]] — Best practices deep-dive: one-time payments (button placement, conversion, UX)
- [[source-paypal-best-practices-recurring-payment]] — Best practices deep-dive: recurring payments (integration patterns, review page, webhooks)
- [[source-paypal-best-practices-vault-payment]] — Best practices deep-dive: vaulted payments (O2O, preselection, frictionless login)
- [[source-paypal-checkout-customize-overview]] — Checkout customization feature catalog (20 extension points)
- [[source-paypal-checkout-authorize-and-capture]] — Authorize and capture: 2-step payment flow, timing windows, API endpoints
- [[source-paypal-checkout-contact-module]] — Contact module: 3 preference modes, gift order use case, US only
- [[source-paypal-checkout-display-funding-source]] — Display funding source: onClick handler, 5 fundingSource values, Pay Later localisation
- [[source-paypal-checkout-display-payment-methods]] — Display payment methods: Marks component, radio button toggle pattern
- [[source-paypal-checkout-handle-errors]] — Handle errors: onError catch-all, script load guard, error handler taxonomy
- [[source-paypal-checkout-handle-funding-failures]] — Handle funding failures: INSTRUMENT_DECLINED, actions.restart(), auto vs manual restart
- [[source-paypal-checkout-messaging-with-buttons]] — Messaging with buttons: Pay Later, message.amount, updateProps gotcha, US only
- [[source-paypal-checkout-overcharge-handling]] — Overcharge handling: PSD2/SCA, PAYER_ACTION_REQUIRED, re-authorization flow
- [[source-paypal-checkout-pass-buyer-identifier]] — Pass buyer identifier: email prefill for PayPal login, payment_source.paypal.email_address
- [[source-paypal-checkout-pass-line-items]] — Pass line items: items[] schema, amount breakdown constraints, PATCH for updates
- [[source-paypal-checkout-pay-another-account]] — Pay another account: payee object, email_address or merchant_id routing
- [[source-paypal-checkout-single-page-app]] — SPA integration: React/Vue/Angular driver API, defer script tag, Vue style-object gotcha
- [[source-paypal-checkout-recurring-payments-module]] — Recurring payments module: full usage_pattern table (8 values), billing plan structure, setup vs purchase paths
- [[source-paypal-checkout-save-payment-methods-recurring]] — Save payment methods for recurring: field-level RBA schema, 7 use cases, billing plan constraints, 422 errors
- [[source-paypal-checkout-shipping-module]] — Shipping module: server-side callbacks (PayPal + Venmo), 3 shipping prefs, amount consistency rules, 6 decline codes
- [[source-paypal-checkout-show-cancellation-page]] — Show cancellation page: onCancel callback, error handler taxonomy
- [[source-paypal-checkout-standalone-buttons]] — Standalone buttons: getFundingSources, isEligible, 4 patterns, Marks, funding-eligibility component
- [[source-paypal-checkout-update-order-details]] — Update order details: PATCH order, commit=false, Continue button trade-off
- [[source-paypal-checkout-validate-user-input]] — Validate user input: onInit/onClick sync pattern, async reject/resolve, validation order
- [[source-paypal-checkout-upgrade-integration]] — Upgrade integration: checkout.js → JS SDK migration map, callback renames, script tag changes
- [[source-paypal-expanded-checkout-getting-started]] — Expanded Checkout getting started: hosted card fields, 3DS liabilityShift, cardFields.submit()
- [[source-paypal-javascript-sdk-overview]] — JavaScript SDK overview: buttons/marks/card-fields/funding-eligibility components
- [[source-paypal-javascript-sdk-configuration]] — JS SDK configuration: all query params + data-* attributes, v5 CardFields reference
- [[source-paypal-javascript-sdk-reference]] — JS SDK reference: full API for Buttons/Marks/CardFields/funding-eligibility (3,727 lines, all 4 integration patterns)
- [[source-paypal-javascript-sdk-performance]] — JS SDK performance: instant vs delayed render, pre-caching, hidden container pattern
- [[source-paypal-javascript-sdk-best-practices]] — JS SDK best practices: CSP domains + nonce vs unsafe-inline, COOP same-origin-allow-popups
- [[source-paypal-react-paypal-js-readme]] — @paypal/react-paypal-js v8.x README: PayPalScriptProvider, all components, hooks, Card Fields vs Hosted Fields
- [[source-github-paypal-js]] — cumulative GitHub evidence for independently versioned packages; v8 baselines through core `10.1.0` and React `10.2.1`
- [[changelog-github-paypal-js]] — package-qualified paypal/paypal-js release ledger through core `10.1.0` and React `10.2.1`, with impact, migration action, contradictions, and immutable raw links
- [[source-github-paypal-checkout-components]] — cumulative checkout runtime evidence from `@paypal/checkout-components@4.1.47` through `5.0.425`
- [[changelog-github-paypal-checkout-components]] — package-qualified checkout-components release ledger through `5.0.425`
- [[source-github-react-paypal-js-v8]] — GitHub react-paypal-js v8 source: ScriptProvider internals, reducer state machine, Buttons lifecycle, CardFields architecture
- [[source-paypal-expanded-checkout-integrate]] — Expanded Checkout integration: CardFields+Buttons, 3DS SCA, billing address submit, authorize routes
- [[source-paypal-android-card-payments]] — Android SDK: CardClient, WebPayments, deprecated NativePayments, FraudProtection, 3DS SCA
- [[source-github-paypal-android]] — GitHub paypal-android: CardClient source, instance state, Demo ViewModels, Venmo funding source contradiction
- [[source-paypal-ios-card-payments]] — iOS SDK: CardClient/CardDelegate, WebPayments, PaymentButtons (UIKit+SwiftUI), FraudProtection
- [[source-github-paypal-ios]] — cumulative GitHub paypal-ios evidence through `paypal-ios@2.0.1`: v2 Result/async APIs, checkout and card vaulting, 3DS, cancellation fixes, buttons, fraud data, and no native Venmo funding-source case
- [[changelog-github-paypal-ios]] — package-qualified paypal-ios history: v1 delegate boundary, v2 migration, and exact `2.0.1` deep-link cancellation fixes
- [[source-paypal-ios-in-app-purchases]] — iOS in-app purchases: Apple external payment entitlement, 3 options (Payment Link, Buttons, Custom Checkout)
- [[source-paypal-expanded-checkout-customize-overview]] — Expanded Checkout customization catalog: 14 features, expanded vs standard comparison
- [[source-paypal-expanded-checkout-3d-secure]] — 3D Secure: liability shift, 36-country eligibility table, card brand/currency restrictions
- [[source-paypal-expanded-checkout-3ds-card-fields]] — 3DS CardFields integration: payment_source.card.verification, liabilityShift in onApprove, PSD2 billing address requirement
- [[source-paypal-expanded-checkout-3ds-orders-api]] — 3DS Orders API: HATEOAS payer-action redirect, empty-payload final capture, authentication_result structure
- [[source-paypal-3ds-response-parameters]] — 3DS response params: liability_shift/enrollment_status/authentication_status decision table, deprecated pre-2020 params
- [[source-paypal-3ds-test-scenarios]] — 3DS test cards: 9 scenarios × 10 countries (purchase) + 15 scenarios for save payment methods
- [[source-paypal-expanded-checkout-acquirer-reference-number]] — ARN: 3 retrieval endpoints, ARN field paths, not available immediately after capture
- [[source-paypal-expanded-checkout-card-field-style]] — Card Fields Style Guide: ~40 supported CSS properties, parent vs individual field scoping
- [[source-paypal-expanded-checkout-card-field-properties]] — Card Field Properties: 4 fields (3 required), inputEvents/style/placeholder options, stateObject
- [[source-paypal-expanded-checkout-card-fields-events]] — Card Fields Events & Methods: 4 events, 3 parent methods, 9 field methods, full type definitions
- [[source-paypal-expanded-checkout-fraud-protection]] — Fraud protection: no-integration ML risk toolkit, dashboard activation, send payer.phone + payer.email for signal
- [[source-paypal-expanded-checkout-fraud-protection-advanced]] — Fraud Protection Advanced (FPA): self-serve ML tool, risk score 0–100, filters/lists/review queue, 35 markets, per-transaction fee
- [[source-paypal-expanded-checkout-chargeback-protection]] — Chargeback Protection: automated ML decisions (no manual review), waives eligible chargeback fees, requires delivery evidence, 9 countries, mutually exclusive with FPA
- [[source-paypal-expanded-checkout-rtau]] — Real-Time Account Updater: recovers declined card-on-file payments; Mastercard (reactive) vs Visa (proactive) flows; expiry+last_digits in response; CARD_CLOSED error
- [[source-paypal-expanded-checkout-sca-payment-indicators]] — SCA payment indicators: stored_credential fields (payment_initiator/type/usage), 11 use case scenarios across one-time/recurring/unscheduled
- [[source-paypal-expanded-checkout-level-2-3-processing]] — Level 2/3 processing: IC++ interchange reduction, US/USD only, corp cards only, supplementary_data.card API path, PATCH deletion gotcha
- [[source-paypal-expanded-checkout-3rd-party-token-processing]] — Third-party network token processing: network_token object, ECI flag mapping, no reference transactions, bin_details in response, 32 countries
- [[source-paypal-expanded-checkout-update-order-details]] — Update order details (Expanded Checkout): commit=false → Continue button, PATCH /v2/checkout/orders, reduces payment methods
- [[source-paypal-expanded-checkout-reference-transactions]] — Reference transactions: Website Payments Pro only, payment_source.token with PAYPAL_TRANSACTION_ID or PNREF, 3-step create/authorize/capture flow
- [[source-paypal-expanded-checkout-card-decline-errors]] — Card decline errors: AVS/CVV codes for Visa/MC/Discover/Amex (alphabetical) and Maestro (numeric); codes that force decline
- [[source-paypal-expanded-checkout-eligibility]] — Eligibility: 37 countries, 22 currencies, country-specific card brand restrictions, 21 payment methods with refund windows; giropay/Sofort sunset
- [[source-paypal-expanded-checkout-upgrade]] — Upgrade guide: PayPal Checkout (script tag only) vs Express Checkout NVP/SOAP (full migration); NVP→Orders v2 method map; update+capture now 2 calls
- [[source-paypal-fastlane-getting-started]] — Fastlane: guest/member flows, client token (sdk_init), single_use_token payment source, SDK methods, OTP 111111, store_in_vault, PayPal member auto-handling
- [[source-github-fastlane-sample-application]] — GitHub fastlane-sample-application: 3 clients × 6 servers, Quick Start vs Flexible HTML structure, 3 token functions, Vue Composition API pattern
- [[source-paypal-fxaas-overview]] — FXaaS: contract-based currency conversion, 100+ display currencies, 25 holding currencies, rate locking, compatible with all Orders v2 payment methods
- [[source-paypal-pay-later]] — Pay Later by country (US/AU/CA/FR/DE): product tables, purchase ranges, eligibility; DE unique Pay in 30; recurring/reference transactions not eligible
- [[source-paypal-pay-with-venmo]] — Pay with Venmo: mobile app-switch + desktop QR code flows, eligibility (US/USD only), supported features table
- [[source-paypal-save-payment-methods]] — Save payment methods overview + JS SDK PayPal Wallet + Venmo vault: `data-user-id-token`, `target_customer_id`, Venmo US-only/no-sandbox
- [[source-paypal-payment-methods-reference]] — Full payment method catalog: 18 entries; doc errors (Google Pay as "bank redirect", Apple Pay "US only"); iDEAL BIC restriction; Multibanco absent
- [[source-paypal-apm-error-codes]] — APM error codes: 19 cancel_url error codes; `payee_not_enabled`, currency/country mismatch, idempotency errors, `order_completion_in_progress`
- [[source-paypal-apm-style-reference]] — APM style reference: 11 variables + 6 CSS rules for `paypal.PaymentFields()`; `paypal.FUNDING.OXXO` seen (Mexican voucher, unlisted)
- [[source-paypal-apm-js-sdk-reference]] — APM JS SDK reference: `paypal.FUNDING.*` constants (7 active + giropay/Sofort sunset); vertical-only layout; `isEligible()` pattern
- [[source-paypal-apm-handle-uncaptured-payments]] — APM uncaptured payment reference: `CHECKOUT.PAYMENT-APPROVAL.REVERSED`; 3-hour default capture window; cancel+refund
- [[source-paypal-apm-method-icons]] — APM icon reference: color+white SVGs for 6 APMs (iDEAL color-only); hosted at paypalobjects.com/images/checkout/alternative_payments/
- [[source-paypal-apm-subscribe-webhooks]] — APM webhook reference: 5 core events (APPROVED, REVERSED, PENDING, COMPLETED, DENIED); `POST /v1/notifications/webhooks`
- [[source-paypal-apm-overview]] — Alternative Payment Methods overview: 11 APMs (Apple/Google Pay, 7 bank redirects, Multibanco voucher, Pay upon Invoice); giropay/Sofort sunset; privacy disclosure requirement
- [[source-paypal-apm-apple-pay]] — Apple Pay integration: domain validation, 4 SDK touchpoints, non-Safari browser support, 34 countries/22 currencies, go-live onboarding
- [[source-paypal-apm-trustly]] — Trustly (12 EU countries/EUR+DKK+SEK+GBP+NOK): 365-day refunds; 7-day settlement; JS SDK + Orders API (unique `onApprove`, optional email, doc errors: Multibanco copy-paste, cancel_url placeholder)
- [[source-paypal-apm-przelewy24]] — Przelewy24 (Poland/PLN+EUR): JS SDK (`enable-funding=p24`, name+email); Orders API (email required in `payment_source.p24`); EUR support vs BLIK
- [[source-paypal-apm-mybank]] — MyBank (Italy/EUR): no minimum, bank redirect; JS SDK + Orders API (no mark image, no self-serve onboarding; doc error in Orders API webhook heading)
- [[source-paypal-apm-multibanco]] — Multibanco (Portugal/EUR): voucher, non-instant; JS SDK (BARCODE_URL); Orders API (2-step: create → confirm-payment-source, `payment_reference`+`payment_entity`, 7-day window)
- [[source-paypal-apm-ideal]] — iDEAL (Netherlands/EUR): 0.01 EUR min; ISU skips capabilities; JS SDK + Orders API; two onboarding failure scenarios; `experience_context` inside `payment_source.ideal`
- [[source-paypal-apm-swish]] — Swish (Sweden/SEK): push payment, 13-month refunds; Orders API (`payer` object required, auto+manual capture, `swish://` URL scheme, seller protection eligible)
- [[source-paypal-apm-crypto]] — Pay with Crypto (US merchants, global buyers): ~100 cryptos, auto local-currency settlement, PYUSD refunds; Orders API: `payment_source.crypto`, cancel_url handles errors, self-serve onboarding
- [[source-paypal-apm-pay-upon-invoice]] — Pay upon Invoice/Ratepay (Germany): BNPL; FraudNet + Legal Component required; `PHYSICAL_GOODS` only; `PENDING_APPROVAL` status; `payment_reference`+bank details; mandated Ratepay error messages
- [[source-paypal-apm-google-pay]] — Google Pay integration: 36 countries, all browsers, dual SDK (`config`/`confirmOrder`/`initiatePayerAction`), Japan PAN_ONLY override, 3DS handling; 38 test cards (5 countries)
- [[source-paypal-apm-eps]] — EPS (Austria/EUR): capture-only, no chargebacks; JS SDK (name-only fields); Orders API (auto-capture, no email in payment_source)
- [[source-paypal-apm-blik]] — BLIK (Poland/PLN): capture-only, no chargebacks; JS SDK (name+email fields); Orders API (optional email in `payment_source.blik`)
- [[source-paypal-apm-bancontact]] — Bancontact (Belgium/EUR): capture-only, no chargebacks; JS SDK (single/multi-page, name-only); Orders API (auto-capture, `application_context`); Progressive Onboarding not supported for APMs
- [[source-paypal-save-paypal-payment-tokens-api]] — Save PayPal Payment Method Tokens API: billing agreement approval required, `shipping_preference`, `payment_method_preference: IMMEDIATE_PAYMENT_REQUIRED`, 3-day expiry
- [[source-paypal-save-cards-payment-tokens-api]] — Save Cards Payment Method Tokens API: SAQ D, 3 setup token verification modes, smart auth (zero-value), 3DS, AVS/CVV test tables, off-session `vault_id`
- [[source-paypal-save-paypal-purchase-later-ios-sdk]] — Save PayPal Purchase Later iOS SDK: `PayPalVaultDelegate`, `PayPalVaultRequest`, `usage_type: PLATFORM`, `PAYER_ACTION_REQUIRED`
- [[source-paypal-save-cards-purchase-later-ios-sdk]] — Save Cards Purchase Later iOS SDK: `CardVaultDelegate`, `cardVaultDidCancel`, `CREATED` setup token status, `customer.id` in body
- [[source-paypal-save-paypal-purchase-later-android-sdk]] — Save PayPal Purchase Later Android SDK: `PayPalWebCheckoutClient.vault()`, `usage_type: PLATFORM` (vs MERCHANT elsewhere), `PAYER_ACTION_REQUIRED`
- [[source-paypal-save-cards-purchase-later-android-sdk]] — Save Cards Purchase Later Android SDK: `CardClient.vault()`, `CardVaultListener`, `CREATED` status, `customer.id` in setup token body
- [[source-paypal-save-paypal-purchase-later-js-sdk]] — Save PayPal Purchase Later JS SDK: Buttons with `createVaultSetupToken`, setup token `experience_context`, `merchant-id` param
- [[source-paypal-save-cards-purchase-later-js-sdk]] — Save Cards Purchase Later JS SDK: setup token→payment token, `createVaultSetupToken` replaces `createOrder`, 3DS option, 14 test cards
- [[source-paypal-save-paypal-orders-api]] — Save PayPal Orders API: reference transaction approval required, two-step flow, `experience_context`, `VAULT.PAYMENT-TOKEN.DELETION-INITIATED` webhook
- [[source-paypal-save-cards-orders-api]] — Save Cards Orders API: PCI SAQ D required, raw card in request, single-step capture+vault, no Venmo, RTAU
- [[source-paypal-save-applepay-js-sdk]] — Save Apple Pay JS SDK: vault flow, APPROVED vs VAULTED, VAULT.PAYMENT-TOKEN.CREATED webhook, merchant-initiated recurring
- [[source-paypal-save-cards-js-sdk]] — Save Cards JS SDK: checkbox UX, SCA_ALWAYS/SCA_WHEN_REQUIRED, APPROVED/VAULTED, 14 test cards
- [[source-paypal-save-paypal-ios-sdk]] — Save PayPal Wallet iOS SDK: `PayPalWebCheckoutClient`, `PayPalWebCheckoutDelegate`, 35 countries, `vault.id` for returning payers
- [[source-paypal-save-cards-ios-sdk]] — Save Cards iOS SDK: SwiftUI Toggle, `CardDelegate`, US-only availability (contradicts Android/JS SDK 35-country support)
- [[source-paypal-save-paypal-android-sdk]] — Save PayPal Wallet Android SDK: `PayPalWebCheckoutClient`, deep link scheme, `vault.id` for returning payers
- [[source-paypal-save-cards-android-sdk]] — Save Cards Android SDK: Compose checkbox, `customer.id` in Create Order for returning payers, `ApproveOrderListener` 3DS callbacks, RTAU
- [[source-github-paypal-messages-android]] — GitHub paypal-messages-android v1.3.0: PayPalMessageConfig/Callbacks API, Compose support, int-indexed enums
- [[source-github-paypal-messages-ios]] — GitHub paypal-messages-ios v1.3.0: PayPalMessageView/Delegate API, SwiftUI support, iOS vs Android differences
- [[source-paypal-subscriptions-overview]] — Subscriptions: 6-step flow, REST API vs dashboard, 12 customization capabilities, 4 pricing models (fixed/quantity/volume/tiered); volume vs tiered distinction; single currency per plan
- [[source-paypal-invoicing-overview]] — Invoicing: 4-step flow (draft→send→view→pay), REST API vs dashboard, QR payment + refunds + reminders; multi-country
- [[source-paypal-magnes]] — Magnes (limited release): mobile device fingerprinting SDK (iOS/Android); PayPal-Client-Metadata-Id bridge; formerly "Dyson"; FraudNet is non-mobile equivalent
- [[source-paypal-fraudnet]] — FraudNet (limited release): browser-based JS fraud fingerprinting; embed snippet + custom API header; web counterpart to Magnes
- [[source-paypal-customer-disputes]] — Disputes overview: two resolution paths (Resolution Center vs bank chargeback), buyer workflow, Disputes API actions (list/respond/evidence/accept/appeal)
- [[source-paypal-payouts-overview]] — Payouts: Standard (96 countries, 20+ currencies, self-serve) vs Advanced (240+ countries, 50+ currencies, enterprise, multiple rails)
- [[source-github-paypal-payouts-php-sdk]] — GitHub Payouts PHP SDK: PayoutsPostRequest/GetRequest/ItemGetRequest/ItemCancelRequest, PayPalHttpClient pattern (github-repo, 2026-04-16)
- [[source-paypal-login-with-paypal]] — Log in with PayPal: OAuth flow, 8h token expiry, payer ID scope for payouts, app review required (webpage, 2026-04-16)
- [[source-github-paypal-postman-collections]] — GitHub paypal/postman-collections: 3 collections (Public APIs, Checkout Flows, Partner APIs), paypal-postman-lib helper (github-repo, 2026-04-16)
- [[source-github-paypal-rest-api-specs]] — GitHub paypal-rest-api-specifications: 13 OpenAPI 3.0.3 specs (Orders/Payments/Payouts/Subscriptions/Disputes/Invoicing/Vault/Webhooks/+5) (github-repo, 2026-04-16)
- [[source-github-paypal-sdk-logos]] — GitHub paypal-sdk-logos: 117 SVG payment method logos (37+ methods), CDN URL pattern, LOGO_COLOR constants (github-repo, 2026-04-16)
- [[source-github-paypal-ts-server-sdk]] — GitHub PayPal-TypeScript-Server-SDK v2.3.0: 5 controllers (Orders/Payments/Vault/Subscriptions/TxSearch), 3 init patterns, header params (github-repo, 2026-04-16)
- [[source-github-paypal-googlepay-component]] — GitHub paypal-googlepay-component: googlePayConfig/confirmOrder/initiatePayerAction internals, GraphQL, 3DS via ZalgoPromise (github-repo, 2026-04-16)
- [[source-github-paypal-applepay-component]] — GitHub paypal-applepay-components: config/validateMerchant/confirmOrder, base64 session decode, countryCode uppercase fix (github-repo, 2026-04-16)
- [[source-github-paypal-php-server-sdk]] — GitHub PayPal-PHP-Server-SDK v2.2.0: 5 controllers, builder pattern, built-in retry/backoff/proxy (github-repo, 2026-04-16)
- [[source-paypal-payment-links-overview]] — Payment Links and Buttons: 4 no-code options, Payment Links vs Invoicing comparison (webpage, 2026-04-16)
