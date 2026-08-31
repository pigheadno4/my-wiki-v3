---
title: "Stripe"
type: company
tags: [stripe, payment-gateway, payment-intents, checkout, subscriptions, elements, webhooks, payment-links]
source_count: 664
---

## Stripe

Stripe is a global payments infrastructure company providing APIs and SDKs for accepting payments, managing subscriptions, invoicing, and financial automation. It competes directly with PayPal in the payment processing space but targets developers with a code-first integration model.

## Key Products

### Checkout Sessions API (Recommended)

Stripe's recommended API for most payment integrations. Manages the full checkout lifecycle with built-in tax, discounts, shipping, subscriptions, and Adaptive Pricing. Requires significantly less code than Payment Intents.

**3 UI modes**: Stripe-hosted page (redirect), Embedded form, Custom (`ui_mode: "custom"` with Stripe Elements).

Use Payment Intents instead only if you need full checkout state control or plan to build discount/tax/subscription/currency logic yourself.

See [[source-stripe-checkout-sessions]].

### Payment Intents API

The modern Stripe payment flow. Every payment uses a `PaymentIntent` object that tracks the full lifecycle: `requires_payment_method` → `requires_confirmation` → `processing` → `succeeded`/`requires_payment_method` (on failure).

Key rule: **retry a failed payment by confirming the same PaymentIntent** with new payment details — do not create a new one. This increases conversion rates.

**Full lifecycle**: `requires_payment_method` → `requires_confirmation` → `requires_action` (3DS) → `processing` → `succeeded`; or `requires_capture` (auth+capture flow).

> [!info] Stripe recommends **Checkout Sessions over Payment Intents** for most integrations — same use cases, less code. Adaptive Pricing only available with Checkout Sessions.

### PaymentMethod

API object representing stored payment credentials (card, bank, wallet). Can be saved for future charges via the SetupIntents API.

### Charge

Created when a PaymentIntent is confirmed. Represents one specific attempt to move money. If it fails, the PaymentIntent returns to `requires_payment_method` for retry.

### Stripe Elements

Drop-in UI components for custom integrations. Enables custom-built checkout flows while Stripe handles PCI compliance and UI rendering.

The `@stripe/stripe-js` npm package is the web loader and TypeScript declaration layer for Stripe.js, not a self-hosted runtime. The retained history covers v8.11.0 on `clover`, the v9.12.1 transition to `dahlia`, and approved deltas through v9.14.0, while preserving standard and deferred `/pure` entrypoints and server-side `null` behavior. V9.13.0 adds Checkout Form promotion-code display control and makes wallet visibility creation-only; v9.14.0 adds updateable wallet contact requirements, embedded Custom Payment Method rendering, a beta Express Checkout CPM surface, and an Embedded Checkout dynamic-shipping deprecation. See [[source-github-stripe-js]].

`@stripe/react-stripe-js` is the separate React binding layer. Its retained `6.8.0` baseline provides standard Elements, provider-specific Checkout Elements and beta Checkout Form hooks, Embedded Checkout, SSR-safe initialization, and typed component lifecycle. It requires `@stripe/stripe-js >=9.5.0 <10.0.0`; typed exports do not independently prove runtime rollout or merchant eligibility. See [[source-github-react-stripe-js]].

`@stripe/stripe-react-native` is the mobile bridge to Stripe's native iOS and Android SDKs. The cumulative source preserves the legacy `0.65.1` capsule and adds the approved `0.72.0` baseline: PaymentSheet and Embedded Payment Element, Platform Pay, CustomerSheet, Financial Connections, Connect embedded components, crypto onramp, and private-preview Link Controller. In `0.72.0`, Link SetupIntent confirmation became an explicit post-selection step. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

`stripe-android` is the native Android SDK behind Stripe's prebuilt and low-level mobile payment surfaces. The cumulative source preserves the legacy `23.8.0` capsule and adds the approved `23.13.1` baseline: builder-first PaymentSheet, FlowController, Embedded Payment Element, direct Intent APIs, Google Pay, and specialized Connect, Identity, Financial Connections, Crypto Onramp, messaging, and card-scan modules. A completed SDK result can still represent a processing payment, so fulfillment remains webhook-gated. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

`stripe-ios` is the native Swift SDK behind Stripe's prebuilt and low-level iOS payment surfaces. The cumulative source preserves the legacy `25.14.0` capsule and adds the approved `26.4.1` baseline: PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Apple Pay, low-level Intent and 3DS APIs, and specialized Connect, Identity, Financial Connections, Issuing, and alpha Crypto Onramp modules. Version 26 requires iOS 15+, and a completed SDK result can still represent a processing payment, so fulfillment remains event-gated. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

`stripe-terminal-ios` is the separate native SDK for card-present checkout and reader control. The retained `StripeTerminal@5.8.0` baseline covers backend-issued ConnectionTokens, reader discovery and connection, Tap to Pay, split and combined payment/SetupIntent flows, in-person refunds, offline forwarding, reader updates, QR methods, and the v5 iOS 15 migration boundary. Manual capture and authoritative reconciliation remain backend responsibilities. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

### AI Developer and Token-Billing Tooling

The `stripe/ai` repository supplies independently versioned LLM token-billing packages, a local bridge to Stripe's remote MCP server, TypeScript and Python agent toolkits, provider-specific agent skills/plugins, and integration benchmarks. At the retained SHA, token billing is private preview, the Stripe AI SDK proxy does not support tool calling, native token-meter delivery is fire-and-forget, and the agent toolkits require remote MCP availability. See [[source-github-ai]] and [[changelog-github-ai]].

### Operational Data Synchronization

`stripe/sync-engine` is an experimental Stripe-to-Postgres synchronization framework with OpenAPI-driven discovery, resumable backfill, event and webhook live paths, account-qualified records, PostgreSQL projection, and Temporal orchestration. The retained baseline is exact default-branch commit `93321ab`, not a tagged `0.2.5` release. It assumes trusted internal deployment, exposes an unauthenticated internal query endpoint, and redirects active development to a separately owned fork. See [[source-github-sync-engine]] and [[changelog-github-sync-engine]].

### Stripe Apps

`stripe/stripe-apps` provides manifest schemas and examples for embedding custom UI extensions in the Stripe Dashboard. The retained `default-branch@9b14b71` baseline covers standard, local-development, and extension manifests plus a full-page React example. The example is fully mock-backed, its manifest drifts from the retained standard schema, and payment-related permission enums do not establish a live Checkout flow or merchant eligibility. See [[source-github-stripe-apps]], [[changelog-github-stripe-apps]], and [[stripe-apps]].

### Stripe CLI

`stripe-cli@1.50.0` is Stripe's command-line developer and test tool for direct API requests, fixtures, synthetic event triggers, local webhook forwarding, request-log streaming, and account or sandbox contexts. Its embedded trigger payloads are test recipes rather than canonical API lifecycle evidence. The exact `1.50.0` release note adds agent identity metadata to telemetry; it does not establish the rest of the baseline as new in that release. See [[source-github-stripe-cli]], [[changelog-github-stripe-cli]], and [[stripe-cli]].

### Link CLI for Agents

`@stripe/link-cli@0.13.0` is a separate consumer-wallet tool for agents, not the merchant developer Stripe CLI. It uses user-approved Link spend requests to issue a virtual card for standard checkout, a one-time Shared Payment Token for Stripe MPP `402` payments, or a merchant-bound Link Pay Token for supported AI-agent steering surfaces. It also exposes read-only financial-insight commands, local and HTTP MCP modes, and credential-file protections. The internal `@stripe/link-sdk` is private, and the retained Web Bot Auth code is not registered as a CLI command. See [[source-github-link-cli]], [[changelog-github-link-cli]], and [[stripe-link-cli]].

### Stripe PHP SDK

`stripe-php@21.2.0` is Stripe's retained server-side PHP SDK baseline, pinned to Stripe API `2026-07-29.dahlia` and requiring PHP 7.2+. It covers Checkout, PaymentIntents, SetupIntents, Payment Links, subscriptions, webhooks and event notifications, and Terminal server operations. Public webhooks still require signature verification; the v21.2.0 `WithoutVerification` helpers are only for previously verified or trusted payloads. See [[source-github-stripe-php]], [[changelog-github-stripe-php]], and [[stripe-php-sdk]].

### Express Checkout Element

Single component that renders multiple one-click payment buttons (Link, Apple Pay, Google Pay, PayPal, Klarna, Amazon Pay). Buttons are dynamically sorted by customer location. New payment methods activate from the Dashboard — no frontend changes needed. See [[stripe-express-checkout-element]].

### Stripe Checkout

Hosted payment page. Stripe creates the PaymentIntent and handles confirmation, events, and responses.

### Payment Links

No-code shareable payment URLs — Stripe handles the entire flow. 40+ payment methods, Adaptive Pricing (150+ countries, always enabled), browser language auto-detection (30+ languages).

**3 sharing surfaces**: direct URL (email/SMS/social), embeddable buy button (`<stripe-buy-button>` web component), QR code (never expires).

**Key customization**: payment limits (`restrictions.completed_sessions.limit`), adjustable quantities, custom fields (text/number/dropdown), address/phone/name collection, Stripe Tax, ToS consent, custom domain (`pay.example.com` instead of `buy.stripe.com`), UTM tracking + `client_reference_id` for reconciliation.

**Supports subscriptions** via recurring price; Smart Retries + reminders apply to subscription links only.

See [[stripe-payment-links]].

### Subscriptions & Invoicing

Recurring billing via Subscription objects. Also supports standalone Invoicing.

### Events & Webhooks

`Event` objects represent activity (e.g. charge succeeded/failed). Integrations respond via webhook endpoints. Checkout and Payment Links integrations have pre-written event responses; custom integrations write their own.

## API Deprecations

| API | Status |
| --- | --- |
| Sources API (local payment methods) | Deprecated + **being turned off** — migrate to Payment Methods API required |
| Sources API (card payments) | Deprecated — not being turned off (yet) |
| Charges API | Unsupported but available; no future development |
| ACH (old) | Unsupported but available; no future development |

Current APIs: Payment Intents + Setup Intents + Payment Methods. SCA-ready, Terminal support, and all future features.

## Core Philosophy

- **Everything is an object** — all activity (balance, subscriptions, payment methods) maps to an API object, even Dashboard actions
- **Objects are state machines** — track process state via `status` field
- **Integrations are cooperating objects** — combine PaymentIntent + PaymentMethod + Charge + Event + Customer etc.

## 5 Integration Paths

| Path | Who controls flow |
| --- | --- |
| Payment Intents (direct) | Developer |
| Stripe Elements | Developer (UI) + Stripe (PCI) |
| Stripe Checkout | Stripe |
| Payment Links | Stripe (no-code) |
| Subscriptions/Invoicing | Developer + Stripe |

## Sources

- [[source-github-stripe-js]] — cumulative `stripe/stripe-js` v8.11.0 through v9.14.0 loader, Elements, Checkout, and public TypeScript history
- [[changelog-github-stripe-js]] — package-qualified Stripe JS release history
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Stripe Tax on Metronome-created Stripe invoices, including customer and product mapping
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — Stripe product mapping, invoice voiding, and retry boundary for a Metronome-gated commit
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — contract invoice-routing transitions between Stripe, NetSuite, and marketplaces
- [[source-github-stripe-postman]] — Stripe API Postman collection: 107 endpoint groups, 4 versioned collections in public workspace, fork/import setup, 2024-04-15 changelog
- [[source-github-stripe-android]] — cumulative stripe-android SDK source: legacy v23.8.0 plus v23.13.1 PaymentSheet, Embedded Payment Element, direct Intents, Google Pay, Connect, Identity, Financial Connections, and onramp
- [[changelog-github-stripe-android]] — package-qualified Android release history and exact v23.13.1 Alipay test-mode reconciliation fix
- [[source-github-stripe-ios]] — cumulative stripe-ios SDK source: legacy v25.14.0 plus v26.4.1 PaymentSheet, Embedded Payment Element, Apple Pay, low-level Intents, Connect, Identity, Financial Connections, Issuing, and onramp
- [[changelog-github-stripe-ios]] — package-qualified iOS release history, iOS 15 migration boundary, and exact v26.4.1 Alipay result fix
- [[source-github-stripe-terminal-ios]] — `StripeTerminal@5.8.0` card-present iOS SDK baseline: readers, Tap to Pay, payments, SetupIntents, offline processing, refunds, and updates
- [[changelog-github-stripe-terminal-ios]] — package-qualified Stripe Terminal iOS v5 history and exact `5.8.0` reader-setting, SetupIntent, logging, disconnect, and Tap to Pay changes
- [[source-github-stripe-react-native]] — stripe-react-native cumulative SDK source: legacy v0.65.1 plus v0.72.0 PaymentSheet, Embedded Payment Element, Platform Pay, Connect, onramp, and Link Controller
- [[changelog-github-stripe-react-native]] — package-qualified release history and v0.72.0 explicit Link SetupIntent confirmation migration
- [[source-github-ai]] — exact-SHA Stripe AI implementation baseline: LLM token billing, MCP bridge, agent toolkits, skills/plugins, and benchmarks
- [[changelog-github-ai]] — package-qualified `stripe/ai` component baseline and future comparison rules
- [[source-github-stripe-cli]] — `stripe-cli@1.50.0` baseline: API commands, fixtures, triggers, webhook forwarding, authentication contexts, and telemetry
- [[changelog-github-stripe-cli]] — package-qualified Stripe CLI history and exact `1.50.0` telemetry change
- [[source-github-link-cli]] — `@stripe/link-cli@0.13.0` agent wallet baseline: virtual cards, SPT/MPP, Link Pay Token, spend requests, MCP, and financial insights
- [[changelog-github-link-cli]] — package-qualified Link CLI baseline and exact `0.13.0` financial-insight and duplicate-request messaging changes
- [[source-github-sync-engine]] — `default-branch@93321ab` operational data baseline: Stripe discovery, backfill, live events, Postgres destination, state, and Temporal workflows
- [[changelog-github-sync-engine]] — commit-qualified Sync Engine baseline, documentation drift, trust boundaries, and future comparison rule
- [[source-github-stripe-apps]] — `default-branch@9b14b71` Stripe Apps baseline: manifest schemas, Dashboard UI extensions, full-page example, and mock-data boundaries
- [[changelog-github-stripe-apps]] — commit-qualified Stripe Apps baseline, schema/example drift, and future comparison rule
- [[source-github-stripe-php]] — `stripe-php@21.2.0` server SDK baseline: client services, encoding, retries, webhooks, Checkout, subscriptions, and Terminal
- [[changelog-github-stripe-php]] — package-qualified Stripe PHP baseline and exact v21.2.0 event helper changes
- [[source-stripe-billing-benchmarks]] — billing benchmarking: k-NN peer matching, ≥5 subs access, peer eligibility ≥100 subs, 7 metrics benchmarked, percentile display
- [[source-stripe-billing-analytics]] — billing analytics: MRR + 6 growth components, ARPU, LTV, cohort retention, configurable settings, 3 CSV reports
- [[source-stripe-subscriptions-backdate]] — backdating: classic vs flexible line items, 3 patterns (charge/no-charge/anchor), coupon duration counts from backdate not API call
- [[source-stripe-subscriptions-schedules]] — subscription schedules: phases, dual proration settings, metadata merge rules, direct update auto-split, installment plans, 10 use cases
- [[source-stripe-billing-taxes-migration]] — migrating subscriptions to Stripe Tax: automated tooling (Dashboard), manual 5-step process, tax_behavior immutability, schedule approach
- [[source-stripe-billing-customer-tax-ids]] — Customer Tax IDs: 130+ types/100+ countries, reverse charge flag, AU/EU/GB auto-validation, VIES tooltip, test magic IDs
- [[source-stripe-billing-taxes-collect]] — collecting taxes on subscriptions: Stripe Tax (Elements without Intent, address validation, invoice.finalization_failed) vs Tax Rates (cascade, Checkout dynamic)
- [[source-stripe-subscriptions-third-party]] — billing with 3rd party processors: custom PMs + payment records (23h window, retry logic, refunds) vs out-of-band legacy, 43 business countries
- [[source-stripe-subscriptions-pause-payment]] — pause payment collection: 3 behaviors (void/keep_as_draft/mark_uncollectible), distinct from true pause, resumes_at
- [[source-stripe-subscriptions-ideal]] — iDEAL→SEPA subscription: Checkout + Direct API, 0.01 EUR free trial charge, generated_sepa_debit, off_session updates
- [[source-stripe-subscriptions-twint]] — TWINT subscription: CHF only, 3 paths, mandate_data+return_url required, QR via Stripe-hosted redirect
- [[source-stripe-subscriptions-stablecoins]] — Stablecoin subscription: 3 paths (Checkout/PaymentIntents/SetupIntents), crypto PM type, USDC native currency, testnet via MetaMask+Amoy
- [[source-stripe-subscriptions-sepa-debit]] — SEPA subscription: Checkout + Payment Element, delayed notification, 20+ country IBAN test tables (8 scenarios each)
- [[source-stripe-subscriptions-acss-debit]] — Canadian PAD (acss_debit) subscription: Checkout NOT supported, no auto-retry, manual default PM webhook, 10-day microdeposit window
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: KRW-only, 3 paths, naver_pay PM type (identical structure to kr_card/kakao_pay)
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: KRW-only, 3 paths, kakao_pay PM type (identical structure to kr_card)
- [[source-stripe-subscriptions-kr-card]] — South Korean card subscription: KRW-only, 3 paths, off_session+mandate_data, local processor redirect
- [[source-stripe-subscriptions-revolut-pay]] — Revolut Pay subscription: 3 paths (SetupIntents/Subscriptions API/Checkout), off_session+mandate_data required
- [[source-stripe-subscriptions-pix]] — Pix subscription (Brazil/BRL): Pix Automático mandate, 3 paths, tax_id CPF/CNPJ required, mandate_options.amount tip, 6 email test scenarios
- [[source-stripe-subscriptions-paypal]] — PayPal subscription: Checkout + Direct API (off_session required), billing agreement ID, mandate.updated on revoke, detach cancels BAID
- [[source-stripe-subscriptions-klarna]] — Klarna subscription: Checkout + Payment Element, 23 countries, BNPL options vary by country, email-based test approve/deny
- [[source-stripe-subscriptions-cash-app-pay]] — Cash App Pay subscription: 3 paths (SetupIntents/Subscriptions API/Checkout), QR code + redirect auth, mandate_data, US-only
- [[source-stripe-subscriptions-becs-debit]] — BECS subscription (AU): SetupIntents + DDR compliance, no auto-retry, mandatory mandate URL sharing, 10 test accounts
- [[source-stripe-subscriptions-bank-transfers]] — Bank transfer subscription: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, Accounts v2 path
- [[source-stripe-subscriptions-bacs-debit]] — Bacs subscription: Checkout-only, delayed notification, 9 test accounts (debitNotAuthorized/insufficientFunds mandate behavior), inline pricing
- [[source-stripe-subscriptions-amazon-pay]] — Amazon Pay subscription: 3 paths (SetupIntents/PaymentIntents/Checkout), mandate_data, off_session, redirect flow
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription setup: 10-day microdeposit window, default PM webhook step, trial SetupIntent flow, Checkout delayed events, 11 test scenarios
- [[source-stripe-subscriptions-payment-methods-setting]] — Per-subscription PM settings: payment_method_types pitfall, save_default_payment_method, payment update links (30-day, card-only, active/past_due/trialing only)
- [[source-stripe-billing-collection-method]] — Collection methods: charge_automatically vs send_invoice, payment_behavior, 23h incomplete_expired rule, unpaid draft behavior, enterprise wire transfers
- [[source-stripe-subscriptions-invoices]] — Subscription invoices: lifecycle, 4-level payment priority chain, draft window, void rules, metadata propagation
- [[source-stripe-billing-ios-sdk]] — BillingSDK for iOS (private preview): Customer Sessions auth, buy buttons, hasEntitlement, getCustomerPortal, vs stripe-ios comparison
- [[source-stripe-subscriptions-prebilling]] — Prebilling (public preview, flexible billing only): billing_schedules, bill_until, applies_to, 8 limitations, invoice timing via proration_behavior
- [[source-stripe-subscriptions-pause]] — True pause (flexible billing only): bill_for param, 6 blocking conditions, resume invoice 23h window, 4 webhook events
- [[source-stripe-subscriptions-cancel]] — Cancel subscriptions: 4 methods (immediate/period-end/custom-date/schedule), invoice item handling, dispute config, anchor behavior
- [[source-stripe-subscriptions-pending-updates]] — Pending updates: payment_behavior=pending_if_incomplete, 27 supported PMs, expiry logic, metered item edge cases, 3 webhook events
- [[source-stripe-subscriptions-prorations]] — Prorations: 6 triggers, exhaustive non-trigger list, classic vs flexible credit prorations, preview locking, unpaid invoice handling
- [[source-stripe-subscriptions-change-price]] — Change price (upgrade/downgrade): item-ID pitfall (omit ID → adds item), quantity resets to 1, billing period rules, zero-amount edge cases
- [[source-stripe-subscriptions-modify]] — Modify subscriptions hub: billing-related vs non-billing updates, discount+proration mixed-call behavior, pending updates
- [[source-stripe-billing-entitlements]] — Entitlements: feature-to-product mapping, `lookup_key`, `entitlements.active_entitlement_summary.updated` webhook, 10-entitlement cap in payload, polling API, archive rules
- [[source-stripe-products-prices]] — Products & Prices: custom product IDs, price immutability (archive+new), price_data, compatibility table (tiered/usage-based Disallowed in Payment Links), 3yr max interval
- [[source-stripe-payment-records]] — Payment Records API: unified on+off-Stripe ledger, 3-level hierarchy (PaymentRecord→Attempt→Entry), 4 reporting methods, requires Orchestration
- [[source-stripe-payment-methods]] — Payment Methods API: 3 customer action types, immediate (cards) vs delayed (ACH/SEPA) notification, single-use vs reusable, PaymentMethod object structure
- [[source-stripe-checkout-sessions]] — Checkout Sessions API: 3 UI modes, 5 built-in features (tax/discounts/shipping/subscriptions/Adaptive Pricing), vs Payment Intents comparison
- [[source-stripe-payment-intents]] — PaymentIntents + SetupIntents lifecycle: all statuses (requires_action/requires_capture/canceled), cancel rules, Checkout Sessions recommendation, SetupIntent mandate creation
- [[source-stripe-api-tour]] — Stripe API tour: PaymentIntent lifecycle, Charge, PaymentMethod, Elements, Events, 5 integration paths
- [[source-stripe-legacy-apis]] — Legacy APIs: Sources/Charges/ACH deprecation status, Charges vs PaymentIntents flow comparison, statement descriptor rules
- [[source-stripe-glossary]] — Stripe Glossary: 130+ terms — payment APIs, SCA/3DS, Connect, billing, Radar, interchange, payout schedules
- [[source-stripe-building-with-ai]] — AI developer tools: MCP server, agent skills (npx/Claude Code/Cursor), AI coding platforms, plain text docs, VS Code AI assistant
- [[source-stripe-accept-a-payment]] — Accept a payment: 4 web UI modes, PaymentSheet (iOS/Android/React Native), webhooks, saved PMs, auth+capture, test cards
- [[source-stripe-payment-links]] — Payment Links: no-code shareable URLs, 40+ methods, Adaptive Pricing, buy button, Invoicing vs Payment Links comparison
- [[source-stripe-build-payments-page]] — Build a payments page: Checkout Page vs Elements comparison, feature matrix, hosting modes, maintenance tradeoffs
- [[source-stripe-checkout-quickstart]] — Checkout quickstart: 3 modes, key session params, React client, test cards, customer handling
- [[source-stripe-checkout-form]] — Checkout form (custom path): single iframe, 100+ methods, built-in returning UI, Appearance API, 2 layouts (single-page + multi-step)
- [[source-stripe-how-checkout-works]] — How Checkout works: 24-feature table, mixed cart, session expiry, save payment details, guest customers, Checkout for agents
- [[source-stripe-checkout-appearance]] — Checkout appearance: branding_settings API, logo/icon logic, Connect override, 24-font compatibility table
- [[source-stripe-checkout-card-brands]] — Card brand blocking: brands_blocked param, 4 brands (discover_global_network covers Discover/Diners/JCB/UnionPay/Elo), filters Link/Apple Pay/Google Pay/saved PMs
- [[source-stripe-checkout-product-images]] — Product images: products.create images param, inline price_data.product_data, drives conversion
- [[source-stripe-checkout-shipping]] — Charge for shipping: ShippingRate API, shipping_options, delivery estimates, shipping tax, payment mode only
- [[source-stripe-checkout-taxes]] — Collect taxes: automatic_tax param, new/existing customer flows, Accounts v2 + Customers v1, customer_update, wallet constraints
- [[source-stripe-checkout-manual-tax-rates]] — Manual Tax Rates: TaxRate API, fixed + dynamic rates, 30-country list, wallet constraints, Dashboard reporting exports
- [[source-stripe-checkout-custom-shipping-options]] — Dynamic shipping: embedded only, permissions.update_shipping_details, onShippingDetailsChange callback, server endpoint pattern
- [[source-stripe-checkout-custom-components]] — Custom fields (3 types), custom text (4 placements), ToS consent, payment method reuse agreement, localization, Dashboard policies
- [[source-stripe-checkout-build-subscriptions]] — Full subscription integration: product/price setup, Checkout Session, webhook provisioning, customer portal, flexible billing mode
- [[source-stripe-checkout-dashboard-payment-methods]] — Dashboard payment methods: migration guide, Apple Pay/Google Pay defaults, delayed notification PM webhook pattern, test table
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing: 150+ countries, 20 local PMs, presentment_details, 0% merchant / 2–4% customer fee, restrictions, refunds
- [[source-stripe-checkout-discounts]] — Discounts: Coupon API, session apply, promotion codes, restriction params, uniqueness rules, lifecycle
- [[source-stripe-checkout-optional-items]] — Optional items: optional_items API, adjustable_quantity, cross-sells, limitations table
- [[source-stripe-checkout-save-and-reuse]] — Setup mode: session creation, SetupIntent retrieval, off-session charging, 402 handling
- [[source-stripe-checkout-save-during-payment]] — Save during payment: setup_future_usage vs payment_method_save, allow_redisplay, customer_creation, PM removal, GDPR note
- [[source-stripe-checkout-fulfillment]] — Fulfill orders: dual-trigger pattern, fulfill_checkout function, webhook handler, delayed PMs, landing page config
- [[source-stripe-checkout-receipts]] — Receipts + paid invoices: automatic setup, branding, invoice_creation param, invoice_data hash, delayed PM behavior, localization
- [[source-stripe-checkout-custom-success-page]] — Redirect behavior: hosted success page, embedded return page + session status, redirect_on_completion (3 modes), onComplete callback
- [[source-stripe-checkout-abandoned-carts]] — Abandoned cart recovery: consent + after_expiration.recovery, checkout.session.expired, recovery URL, anti-spam, conversion tracking
- [[source-stripe-checkout-conversion-funnel]] — GA4 conversion funnel: gtag instrumentation, begin_checkout event, Measurement Protocol, client ID linking
- [[source-stripe-checkout-embedded-analytics]] — Embedded analytics (private preview): onAnalyticsEvent, 6 event types, client_metadata, failureReason, TypeScript types
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents for Elements: feature matrix, IC+ scenarios, integration effort comparison
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart: CheckoutElementsProvider, useCheckout hook, 4 elements, return page, Adaptive Pricing, Stripe Tax
- [[source-stripe-payment-intents-quickstart]] — Payment Intents quickstart: Elements wiring, confirmPayment, return page status, Stripe Tax, email receipts, off-session charging
- [[source-stripe-web-elements-overview]] — Stripe Elements overview: 7 elements, Checkout Sessions vs Payment Intents API comparison, features
- [[source-stripe-payment-element]] — Payment Element: layout (3 options), Appearance API, 8 options, element combining, 17 auto-handled error codes
- [[source-stripe-payment-element-best-practices]] — Payment Element best practices: LLM instruction, HTML confirm pattern, 7-item + 5-item checklists
- [[source-stripe-payment-element-vs-card-element]] — Payment Element vs Card Element: 7 comparison tables, Card Element legacy status, migration guide
- [[source-stripe-payment-element-migration]] — Payment Element migration: CardElement → PaymentElement (PI + SI paths), 11 Elements options, elements.submit() pattern
- [[source-stripe-payment-element-migration-ewcs]] — Payment Element migration to Checkout Sessions (recommended): one-time + future paths, 12 session options, actions.confirm()
- [[source-stripe-express-checkout-element]] — Express Checkout Element: 6 one-click wallets, browser support matrix, per-wallet button types/themes, `ready` event, payment method controls
- [[source-stripe-express-checkout-element-accept-payment]] — ECE integration guide: Checkout Sessions + Payment Intents paths, payment method type mappings, customer detail collection, wallet events, testing credentials, Connect
- [[source-stripe-express-checkout-element-migration]] — ECE migration guide: Payment Request Button → Express Checkout Element, before/after code, confirmPayment vs confirmCardPayment, MPAN
- [[source-stripe-address-element]] — Address Element: shipping/billing modes, PaymentIntent field routing, autocomplete (26 countries), Link autofill, combining with other elements
- [[source-stripe-currency-selector-element]] — Currency Selector Element: Checkout Sessions only, Adaptive Pricing toggle, placement best practices, legal requirement to render
- [[source-stripe-link-authentication-element]] — Link Authentication Element: dual-purpose email + Link auth, onChange event, defaultValues prefill, combining with other elements
- [[source-stripe-payment-method-messaging-element]] — Payment Method Messaging Element: BNPL promo messaging (Affirm/Afterpay/Klarna), no clientSecret needed, info modal, Connect, Appearance API
- [[source-stripe-tax-id-element]] — Tax ID Element (beta): 100+ countries, auto/always visibility, Address Element integration, CustomerSession for save/redisplay
- [[source-stripe-checkout-sessions-vs-payment-intents]] — Checkout Sessions vs Payment Intents: 11-row feature matrix, session expiration, webhook lifecycle, Adaptive Pricing exclusivity
- [[source-stripe-payment-element-design-integration]] — Payment Element design guide: 2×2 decision framework (when to create Intent × where to confirm), deferred vs eager, client vs server confirmation
- [[source-stripe-payment-element-custom-payment-methods]] — Custom Payment Methods: cpmt_ IDs, static/embedded display types, elements.submit() routing, reportPayment recording, XSS warning
- [[source-stripe-payment-element-customize-payment-methods]] — Customize payment methods: paymentMethodOrder (apple_pay/google_pay valid), auto-hide, visibleAccordionItemsCount, Finland/Sweden regulation
- [[source-stripe-migrate-payment-methods-dashboard]] — Migrate to Dashboard payment methods: both API paths, Apple Pay/Google Pay defaults, delayed notification webhooks, full test credentials
- [[source-stripe-collect-addresses]] — Collect addresses: Checkout Sessions vs Payment Intents API diff, syncAddressCheckbox, getValue(), blockPoBox, autocomplete with own Maps key + CSP
- [[source-stripe-payment-element-billing-details]] — Control billing details: auto/never/if_required modes, never requires manual injection at confirm, if_required trade-offs (network fees, auth rate)
- [[source-stripe-charge-shipping]] — Charge for shipping: Checkout Sessions (full support) vs Payment Intents (no native support), client-side updateShippingOption, delivery estimates, shipping tax
- [[source-stripe-build-subscriptions-elements]] — Subscriptions with Elements: full flow, entitlements pattern, plan change, proration preview, cancel-cannot-reactivate, Accounts v2
- [[source-stripe-checkout-dynamic-shipping]] — Dynamic shipping (beta): permissions.update_shipping_details=server_only, runServerUpdate, server endpoint pattern, 4 use cases
- [[source-stripe-checkout-dynamic-line-items]] — Dynamic line items (beta): runServerUpdate, line item update rules, 20s timeout, security guidelines, subscription interval toggle
- [[source-stripe-checkout-dynamic-trials]] — Dynamic trial durations (private preview): trial_period_days/trial_end mutual exclusion, removal rules, subscription mode only
- [[source-stripe-checkout-dynamic-discounts]] — Dynamic discounts (private preview): permissions.update_discounts=server_only, inline coupon_data, remove via [], loyalty/cart/promo use cases
- [[source-stripe-checkout-dynamic-amounts]] — Dynamic amounts: Checkout Sessions (runServerUpdate + price_data) vs Payment Intents (paymentIntents.update), timing constraints, security rules
- [[source-stripe-checkout-adjustable-quantities]] — Adjustable quantities: updateLineItemQuantity client API, session setup, sessions.listLineItems post-payment, metadata reconciliation tip
- [[source-stripe-checkout-update-customer]] — Update customer mid-checkout: attach Customer after session creation, guest→login flow, preserves entered data
- [[source-stripe-checkout-add-discounts]] — Add discounts (Elements): applyPromotionCode/removePromotionCode client API, removePromotionCode removes ALL codes, permanent inactivation rules
- [[source-stripe-checkout-collect-taxes]] — Collect taxes: CS (automatic_tax, taxExclusive/Inclusive display, Tax ID Element + real-time verification) + PI (Tax API: calculate, record, reverse)
- [[source-stripe-checkout-redeem-credits]] — Credits (private access): store credit/gift card, applied after tax+shipping, merchant manages balance, reconcile post-session
- [[source-stripe-checkout-local-currency]] — Local currency hub: Adaptive Pricing vs FX Quotes API vs Manual currency prices (FX Quotes and Manual not yet ingested)
- [[source-stripe-adaptive-pricing-elements]] — Adaptive Pricing (Elements): adaptivePricing.allowed required, CurrencySelectorElement React, 20 local PMs, +location_XX testing, restrictions
- [[source-stripe-fx-quotes-api]] — FX Quotes API (preview): locked exchange rates, fee pass-through, Group 1/2 pricing, PaymentIntent integration, expired quote handling
- [[source-stripe-manual-currency-prices]] — Manual currency prices: currency_options on Price, overrides Adaptive Pricing, auto-localization requirements, CS API only
- [[source-stripe-payment-element-saved-pms]] — Saved PMs: allow_redisplay values, CVC re-collection, subscription removal warning, unspecified legacy PMs, consent override
- [[source-stripe-save-during-payment-elements]] — Save during payment: both API paths, CustomerSession setup for PI, setup_future_usage vs payment_method_save_usage, Bancontact→SEPA conversion
- [[source-stripe-save-and-reuse-elements]] — Save without payment: CS mode=setup + Setup Intents, confirmSetup, retrieveSetupIntent, Apple Pay MPANs, Radar note, Link prefill
- [[source-stripe-email-receipts]] — Email receipts: CS (invoice_creation, invoice_data) vs PI (receipt_email additional, no invoices, no browser locale), Charge update rule
- [[source-stripe-checkout-manual-approval]] — Manual approval (CS only): server-side fraud/inventory/PM checks before finalizing, compatible with dynamic line items
- [[source-stripe-auth-and-capture]] — Auth+capture: validity windows (Visa MIT=5d, Japan JPY=30d), per-PM windows, per-PM capture_method, automatic_delayed preview, partial capture
- [[source-stripe-checkout-elements-beta-changelog]] — Beta changelog: Clover (initCheckout sync, React import paths, useCheckout disjoint union) + Basil migration, method renames
- [[source-stripe-inapp-payments-overview]] — In-App Payments: Payment Sheet/Flow Controller/Payment Element UIs, PaymentIntent/SetupIntent/setup_future_usage patterns, saved PMs
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet detail: layout options, Appearance API, wallets, address collection, CVC recollection, card brand filtering (8 images)
- [[source-stripe-inapp-custom-payment-methods]] — Mobile CPMs: iOS/Android/React Native handlers, billing details opt-in, FlowController cancel requirement, payment recording
- [[source-stripe-inapp-appearance-api]] — Mobile Appearance API: fonts/colors/shapes/primary button across iOS/Android/RN, dark mode patterns, font name conventions (7 images)
- [[source-stripe-inapp-finalize-payments-server]] — Server confirmation: ConfirmationToken flow, FlowController update() retry requirement, Apple Pay setup, mobile_payment_element CustomerSession
- [[source-stripe-inapp-save-during-payment]] — Save during mobile payment: setup_future_usage mobile limitation (card+US bank only), mobile_payment_element component, allowsDelayedPaymentMethods
- [[source-stripe-inapp-set-up-future-payments]] — Mobile setup (no initial charge): SetupIntent supports card/Bancontact/iDEAL/Link/SEPA/Sofort/US bank, setupIntentClientSecret, FlowController
- [[source-stripe-inapp-filter-card-brands]] — Card brand filtering: allowed/disallowed, discover=full Global Network (JCB/UnionPay/Elo), filters Apple Pay + Google Pay too
- [[source-stripe-inapp-payment-element]] — Mobile Payment Element: embeds in app screen (vs Payment Sheet full-screen), radio/checkmark/floating layouts, inline wallets
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement integration: UIScrollView required, height delegate, update(), formSheetAction, mandate display, clearPaymentOption
- [[source-stripe-inapp-embedded-appearance-api]] — Embedded Appearance API: selectedBorderWidth, 4 row styles, flatWithDisclosure requires immediateAction, per-style separators/colors
- [[source-stripe-inapp-embedded-custom-payment-methods]] — EmbeddedPaymentElement CPMs: EmbeddedPaymentElementResult, paymentMethodOrder, billing details opt-in, platform handler differences
- [[source-stripe-inapp-embedded-filter-card-brands]] — EmbeddedPaymentElement card brand filtering: 4 brands, allowed/disallowed modes, platform API diff vs PaymentSheet variant
- [[source-stripe-inapp-address-element]] — Mobile Address Element overview: 236 regional formats, autocomplete, prefill, Payment Sheet + Payment Element integration
- [[source-stripe-inapp-collect-addresses]] — Mobile Address Element integration: AddressViewController (iOS UIKit), AddressElement SwiftUI, AddressLauncher Android (Google Places required), AddressSheet React Native
- [[source-stripe-inapp-payment-method-messaging-element]] — Mobile BNPL messaging overview: iOS + Android, auto-determines plans and localized messaging
- [[source-stripe-inapp-display-bnpl-messaging]] — Mobile BNPL messaging integration (beta): iOS UIKit/SwiftUI, Android separate dependency, async create/noContent/failed, phase builder, Content() composable
- [[source-stripe-inapp-ios-android-purchases]] — Platform rules: iOS digital goods must redirect to Checkout; Android can go in-app; 3 acceptance paths + customer portal
- [[source-stripe-inapp-digital-goods-checkout]] — iOS digital goods app-to-web: origin_context=mobile_app, Universal Links, SKPaymentQueue gate, Safari open, webhook fulfillment
- [[source-stripe-inapp-digital-goods-payment-links]] — iOS digital goods via Payment Links (no server): Apple Pay US+EEA only, client_reference_id URL param, success URL in Dashboard
- [[source-stripe-inapp-digital-goods-custom-checkout]] — iOS digital goods via Elements (own checkout): default_incomplete subscription, expand latest_invoice, invoice webhooks, Universal Links return
- [[source-stripe-inapp-digital-goods-customer-portal]] — iOS subscription management portal: billingPortal.sessions.create, open in Safari, customer.subscription.* webhooks, Connect platform-only
- [[source-stripe-inapp-customer-sheet]] — CustomerSheet (Payment Method Settings Sheet): app settings PM management, CustomerSession+SetupIntent endpoints, iOS UIKit/SwiftUI/Android/RN, ACH optional
- [[source-stripe-inapp-migrate-confirmation-tokens]] — PaymentMethod → ConfirmationToken migration: auto shipping/mandate/return_url, server-side CVC recollection, client vs server confirmation modes
- [[source-stripe-inapp-without-card-auth]] — Legacy simple integration (US/Canada only): error_on_requires_action, synchronous decline of 2FA cards, no webhooks needed
- [[source-stripe-inapp-save-card-without-auth]] — Legacy save-card (US/Canada only): PM → Customer → charge later, setup_future_usage=on_session, CVC re-collection; non-compliant in India
- [[source-stripe-inapp-upgrade-to-handle-actions]] — Upgrade basic card integration: remove error_on_requires_action, add confirmation_method=manual + use_stripe_sdk, two-round-trip + 1-hour re-confirm window
- [[source-stripe-managed-payments-overview]] — Managed Payments (MoR): Stripe handles tax/fraud/disputes/support, 80+ countries, Checkout+Payment Links only, no Connect/Elements
- [[source-stripe-managed-payments-eligibility]] — Managed Payments eligibility: ~38 business countries, 60+ tax codes, 195+ buyer countries (9 restricted), fully-automated-only rule, 60-day refund window
- [[source-stripe-managed-payments-tax-compliance]] — Tax coverage: 80+ countries auto-handled, Japan all + Singapore B2B exceptions, Stripe Tax only for unsupported (free), Serbia VAT caveat
- [[source-stripe-managed-payments-how-it-works]] — Operational: Link as customer MoR, 48h response rule, refund tax handling, subscription email schedule, payment methods, data deletion
- [[source-stripe-managed-payments-changelog]] — Timeline: GA 2026-04-22 (39 countries+Australia), one-time/in-app (Sep 2025), Adaptive Pricing (Feb 2026), Radar support (Aug 2025)
- [[source-stripe-managed-payments-setup]] — Checkout integration: managed_payments.enabled, API 2025-03-31.basil required, all-products-eligible rule, tax behavior, webhooks
- [[source-stripe-managed-payments-update-checkout]] — Migration: existing subscriptions NOT eligible; unsupported params tables for subscriptions + one-time payments
- [[source-stripe-managed-payments-mobile]] — iOS digital goods with Managed Payments: managed_payments.enabled + origin_context=mobile_app, MoR alternative to non-MoR app-to-web
- [[source-stripe-managed-payments-payment-links]] — Payment Links with Managed Payments: managed_payments.enabled on paymentLinks.create(), immutable MoR state, variable pricing
- [[source-stripe-recurring-payments-overview]] — Recurring payments overview: 3 types, 6-product comparison, subscription creation patterns, flexible billing_mode, Accounts v2 customer_account
- [[source-stripe-terminal-overview]] — Terminal: in-person card readers, 5 integration paths (custom POS/Tap to Pay/apps on readers/third-party POS/gateway), 4 SDKs, offline payments, Connect-compatible
- [[source-stripe-terminal-collect-tips]] — Terminal tipping: on-reader (reader-prompted, wide country support) vs on-receipt (US only, tip added at capture); mandatory tips in original amount
- [[source-stripe-terminal-on-receipt-tipping]] — On-receipt tipping detail: overcapture flow, 50%/50 USD limit, eligible MCCs, fallback via incremental auth or generated_card
- [[source-stripe-terminal-on-reader-tipping]] — On-reader tipping detail: Configuration API (smart/pct/fixed), tip lifecycle, skip tipping, tip-eligible amounts, 38-country list
- [[source-stripe-terminal-save-payment-details]] — Save payment details: generated_card for online reuse, off-session charging, card fingerprints, compliance requirements
- [[source-stripe-terminal-save-directly]] — Save directly (SetupIntent): CNP caveat, card network support, allow_redisplay consent, SDK compatibility, mobile wallet caveats
- [[source-stripe-terminal-save-after-payment]] — Save after payment (PaymentIntent): setup_future_usage, allow_redisplay at collect, generated_card retrieval, fallback when absent
- [[source-stripe-terminal-incremental-authorizations]] — Incremental authorizations: Visa/MC/Amex (all MCCs), Discover (restricted), max 10 attempts, setup, API, auto-increment at capture
- [[source-stripe-terminal-extended-authorizations]] — Extended authorizations: capture up to 30 days later, card/MCC eligibility, capture_before field, Amex caveat
- [[source-stripe-terminal-refunds]] — Refunds and cancellations: cancel pre-capture, online vs in-person refunds, Interac mandatory in-person
- [[source-stripe-terminal-receipts]] — Receipts: prebuilt email receipts via receipt_email, custom receipts with required EMV fields, cardholder preferred_locales
- [[source-stripe-terminal-display-cart]] — Display cart details: setReaderDisplay API, display-only amounts, pre-dip (US only)
- [[source-stripe-terminal-collect-inputs]] — Collect on-screen inputs: 6 input types, up to 5 per call, customization, webhooks, 7-day signature storage
- [[source-stripe-terminal-collect-data]] — Collect swiped data (private preview): magstripe non-PCI data, gift cards, token + server-side retrieval, 24h storage
- [[source-stripe-terminal-collect-nfc-data]] — Collect NFC tapped data (private preview): NFC UID from non-payment instruments, offline-capable, S700/S710/M2 only
- [[source-stripe-terminal-apps-on-devices]] — Apps on Devices: deploy Android POS on smart readers, two integration modes, AOSP differences, permissions allowlist
- [[source-stripe-terminal-apps-on-devices-build]] — Apps on Devices build/test: DevKit setup, SDK deps, serverless init, discovery, transition animations, adb testing
- [[source-stripe-terminal-apps-on-devices-app-review]] — Apps on Devices app review: automated vs manual, 2-5 day timeline, guidelines (no keyed input, sandbox, self-contained instructions)
- [[source-stripe-terminal-apps-on-devices-submit]] — Apps on Devices submit: Dashboard upload flow, compatible device types, status via email/Dashboard/webhook
- [[source-stripe-terminal-apps-on-devices-deploy-dashboard]] — Apps on Devices deploy: deploy groups, three entry points, progressive rollout, Alpha/Beta/General best practice
- [[source-stripe-terminal-apps-on-devices-deploy-api]] — Apps on Devices deploy via API (private preview): deploy groups + locations, same behavior as Dashboard
- [[source-stripe-terminal-apps-on-devices-monitor]] — Apps on Devices monitor: Dashboard deployment status per release version (Pending/Served/Installed/Failed)
- [[source-stripe-terminal-apps-on-devices-troubleshooting]] — Apps on Devices troubleshooting: upload timeout, sandbox/live resubmit, admin settings, IPC limit, crash loops
- [[source-stripe-terminal-order-and-return-readers]] — Hardware orders: ordering, statuses, self-service returns (33 countries), shipping table, permissions, Hardware Orders API
- [[source-stripe-terminal-warranty-claims]] — Warranty claims: 1-year coverage on readers, Dashboard flow, 48h review, replacement warranty carryover
- [[source-stripe-terminal-register-readers]] — Register readers: 3 smart reader methods (pairing code/serial/order), mobile reader locationId at connect time
- [[source-stripe-terminal-locations-and-zones]] — Locations and zones: address requirements by country, zone hierarchy, connection token scoping, Connect patterns
- [[source-stripe-terminal-configurations]] — Terminal configurations: account→location hierarchy, 10-min propagation, API CRUD, zone config preview
- [[source-stripe-terminal-admin-menu-passcode]] — Admin menu passcode: default 07139, 5-digit, same hierarchy, permission tiers for view/modify
- [[source-stripe-terminal-splash-screen]] — Splash screen: per-reader-type, resolutions, image limits, WisePad 3 PNG/B&W, Files API upload + Configuration object
- [[source-stripe-terminal-offline-mode-config]] — Offline mode config: enable/disable via Configuration object `offline.enabled`, 10-min propagation
- [[source-stripe-terminal-reboot-time]] — Reboot time window: default midnight, custom `reboot_window` per location timezone, staggered reboots, midnight-crossing logic
- [[source-stripe-terminal-tipping-config]] — On-reader tips (fleet): 3 tip types, `tipping.{currency}` Configuration API field, smart_tip_threshold, 10-min propagation
- [[source-stripe-terminal-wifi-config]] — WiFi network config: remote push to smart readers, 3 security types (PSK/EAP-PEAP/EAP-TLS), no validation, EAP-TLS via Files API
- [[source-stripe-terminal-cellular-config]] — Cellular config: S710 only, WiFi fallback, monthly billing if enabled, `cellular.enabled` on Configuration object
- [[source-stripe-terminal-monitor-readers]] — Monitor readers: Dashboard readers list, smart reader health/connectivity details, 30-day event log (public preview)
- [[source-stripe-terminal-js-sdk-reference]] — JS SDK API reference: 29 methods, 17 error codes, changelog (surcharge consent, print preview, cancelable operations)
- [[source-stripe-terminal-mobile-readers]] — Mobile readers overview: M2/Chipper 2X BT (US), WisePad 3 (25 non-US countries), BLE/USB, auto-updates, 24h reboot
- [[source-stripe-terminal-bbpos-wisepad3]] — WisePad 3 firmware reference: software version format, latest 4.01.03.00, config regions, key identifiers (APAC/EU/NA)
- [[source-stripe-terminal-stripe-m2]] — M2 firmware reference: latest 2.01.01.00, power button 4s/14s, NFC UID added 2.01.00.31, LED status tables
- [[source-stripe-terminal-smart-readers]] — Smart readers overview: availability table (S700/S710/WisePOS E/Verifone), internet-connected, midnight PCI restart
- [[source-stripe-terminal-s700-s710]] — S700/S710 firmware reference: 4-component software, latest 2.41.2.0/1.00.03.00, diagnostics, payment sounds, changelog
- [[source-stripe-terminal-bbpos-wisepos-e]] — WisePOS E firmware reference: 4-component, latest 2.41.2.0/5.01.03.00, tap sounds same for success+failure, Ethernet dock rule
- [[source-stripe-terminal-tap-to-pay-readers]] — Tap to Pay overview: iPhone 38 countries (JP not GI), Android 38 countries (GI not JP), MPoC compliance status
- [[source-stripe-terminal-sdk-migration-guide]] — SDK v5 migration: unified process methods, customer cancel default, easyConnect, iOS 15 min, Handoff→AppsOnDevices rename
- [[source-stripe-terminal-sdk-v4-migration-guide]] — SDK v4 migration: consolidated connectReader, auto-reconnect default, allow_redisplay global, iOS 14 min, LocalMobile→TapToPay
- [[source-stripe-terminal-sdk-v3-migration-guide]] — SDK v3 migration: processPayment→confirmPaymentIntent, readReusableCard removed, per-type DiscoveryConfig, iOS 13/Android 26 min
- [[source-stripe-terminal-deployment-checklist]] — Deployment checklist: 10 items (ConnectionToken, capture, receipts, reconcile, Chipper updates, registration, Locations, reader UI, SDK, passcode)
- [[source-stripe-terminal-reader-product-sheets]] — Reader product sheets index: S700/S710/M2/BBPOS/Verifone PDF specs and operating info
- [[source-stripe-payment-methods-overview]] — All Stripe payment methods: 8 categories (cards/bank debits/redirects/transfers/BNPL/real-time/vouchers/wallets), regional tables
- [[source-stripe-payment-method-integration-options]] — Integration options: 5 paths (Payment Links→Advanced), dynamic vs manual, wallet domain registration
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: dynamic payment methods as default, allow_redirects option, 3 server-side confirmation paths
- [[source-stripe-cards]] — Cards: 8 brand capabilities table, Amex/CUP/JCB/CB/eftpos country restrictions, SCA/3DS, EU co-badged, India RBI
- [[source-stripe-cit-mit]] — CIT/MIT: definitions, MIT compliance requirements, card brand change blocks MIT, Card Account Updater event
- [[source-stripe-how-cards-work]] — How cards work: 4-step flow, manual update limits, change default PM, automatic card updates, fingerprint change
- [[source-stripe-card-product-codes]] — Card product codes: brand_product field, Visa 41 + Mastercard 200+ codes, test card PMs
- [[source-stripe-cartes-bancaires]] — Cartes Bancaires: France local network, >95% co-badged, EUR only, 41 countries, 0 EUR dispute fee, cannot contest
- [[source-stripe-mastercard-tlid]] — Mastercard TLID: 2026 requirement (Jun 2 retain, Oct 23 send with MIT), 22-char identifier, Stripe auto-handles
- [[source-stripe-eftpos-australia]] — eftpos AU: local debit network, >90% co-branded, no manual capture, LCR routing, disclosure requirement, 7 excluded MCCs
- [[source-stripe-co-badged-cards-compliance]] — Co-badged cards compliance (EU 2015/751): 3 requirements, all Elements + mobile + Terminal integration guides, test cards
- [[source-stripe-installments]] — Installments index: Mastercard Installments (4×), Mexico meses sin intereses, Japan 分割払い
- [[source-stripe-jp-installments]] — Japan installments: JP only, JPY, 3 plan types, brand support table, bonus payment windows
- [[source-stripe-jp-installments-accept-payment]] — Japan installments integration: Checkout/Elements/Direct API (4-step)/Invoices/Payment Links, test cards
- [[source-stripe-mastercard-installments]] — Mastercard Installments: auto-enrolled, 4× interest-free, 7 countries, prohibited MCCs, recurring caveat
- [[source-stripe-mx-installments]] — Mexico meses sin intereses: 6 plans (3–24mo), fees 5–22.5%, 33 issuers, consumer cards only, Connect
- [[source-stripe-mx-installments-accept-payment]] — Mexico meses sin intereses integration: Checkout/Elements/Direct API/Invoices/Payment Links, custom settings, test cards
- [[source-stripe-balance-pay]] — Pay with Stripe Balance: Connect subscriptions only, Accounts V2 preview, T+0/T+1 settlement, insufficient_funds handling, consent required
- [[source-stripe-stablecoin-payments]] — Stablecoin payments: USDC/USDP/USDG, US businesses only, settles in USD, no chargebacks, refunds in stablecoins
- [[source-stripe-accept-stablecoin-payments]] — Accept stablecoin payments: Dashboard enablement, Checkout/Elements/PaymentIntents, MetaMask+Polygon Amoy testnet
- [[source-stripe-crypto-deposit-mode]] — Crypto deposit mode: API-only, USDC Tempo/Base/Solana, exact amount, auto-capture, access required
- [[source-stripe-bank-debits]] — Bank debits: 6 methods (ACH/Bacs/AU-BECS/NZ-BECS/ACSS/SEPA), API enums, product support matrix, Bacs/ACSS caveats
- [[source-stripe-ach-direct-debit]] — ACH Direct Debit: T+4/T+2 settlement, mandates, final disputes, blocked accounts, Connect, test accounts
- [[source-stripe-ach-accept-payment]] — ACH integration guide: Checkout/Elements/PaymentIntents, verification, Financial Connections, payment reference, target date
- [[source-stripe-ach-set-up-payment]] — ACH save for future: Checkout setup mode + SetupIntents, Financial Connections, microdeposit verification, balance check
- [[source-stripe-ach-migration]] — ACH legacy migration: T+6→T+4, balance type change, mandate enforcement, webhook mapping, legacy identification
- [[source-stripe-ach-migrate-bank-accounts]] — ACH migrate bank accounts: mandate creation, BankAccount as PaymentMethod, Checkout saved accounts, Invoices/Subscriptions
- [[source-stripe-ach-migrate-from-processor]] — ACH migrate from another processor: Stripe-managed vs self-service, verification skip, raw bank details SetupIntent
- [[source-stripe-twint]] — TWINT: Switzerland mobile payment, CHF/5000 CHF max, mobile redirect + QR code flows, disputes, refunds, onboarding requirements, Connect
- [[source-stripe-twint-accept-payment]] — TWINT integration: Checkout + Direct API (confirmTwintPayment), redirect flow, save-during-payment
- [[source-stripe-twint-save-during-payment]] — TWINT save during payment: setup_future_usage, off-session charging, return_url not required for saved method
- [[source-stripe-twint-set-up-future-payments]] — TWINT setup-only (no payment): SetupIntent via Checkout/Elements/Direct API, confirmTwintSetup, mandate_data
- [[source-stripe-wero]] — Wero: Germany/EUR, QR+app auth, under 10s, no disputes/recurring, 2-year refunds, 30 business countries
- [[source-stripe-wero-accept-payment]] — Wero integration: Checkout + Elements + Direct API (confirmWeroPayment), server-side manual path, 1-hour auth expiry, error codes
- [[source-stripe-usage-based-billing-how-it-works]] — Usage-based billing: 4-component lifecycle, Meter/meter event/meter event summary concepts, Meter API (billing v2)
- [[source-stripe-usage-based-billing-use-cases]] — Usage-based pricing models: pay-as-you-go, flat fee+overages (v1 only), credit-based
- [[source-stripe-usage-based-billing-payg]] — Pay-as-you-go end-to-end: meter creation, metered price, subscription, meter events (value=string), billing_mode, event summaries
- [[source-stripe-usage-based-billing-flat-fee-overages]] — Flat fee + overages: two-product approach (graduated tiered + licensed flat), Decimal.from() for tiers, invoice timing
- [[source-stripe-usage-based-billing-credits]] — Credit-based pricing: credit grants API, burn-at-invoice-end, balance summary/transactions, funding flow, meter dimensions
- [[source-stripe-usage-based-billing-recording-usage]] — Usage ingestion methods: API, Dashboard CSV, Amazon S3; async processing
- [[source-stripe-usage-based-billing-meters-configure]] — Meter config attributes, Raw vs Pre-aggregated ingestion, immutability, Meter Event Adjustment API
- [[source-stripe-usage-based-billing-recording-usage-api]] — API ingestion: rate limits (1k/s), API v2 high-throughput streams (10k/s), timestamp rules, async error events
- [[source-stripe-usage-based-billing-recording-usage-dashboard]] — Dashboard ingestion: manual input + CSV upload (5 MB limit, field schema, error file workflow)
- [[source-stripe-usage-based-billing-recording-usage-s3]] — Amazon S3 ingestion: connector setup (IAM role), polling (5 min), rate limits, two-tier error handling
- [[source-stripe-usage-based-billing-configure-grace-period]] — Invoice finalization grace period: default 1h, max 72h, cycling vs threshold, rules system
- [[source-stripe-usage-based-billing-credits-overview]] — Billing credits overview: prohibited uses, 5 grant states, eligibility, priority ordering, 100-grant limit
- [[source-stripe-usage-based-billing-credits-setup]] — Billing credits setup: create grant, price-level scoping via billable_items, funding flow
- [[source-stripe-usage-based-billing-monitor-usage-alerts]] — UBB monitoring: usage alerts vs billing thresholds, limits and constraints
- [[source-stripe-usage-based-billing-alerts-setup]] — Usage alert setup: create API, one-time per-customer type, billing.alert.triggered webhook
- [[source-stripe-usage-based-billing-thresholds-setup]] — Billing thresholds: monetary + usage APIs, reset_billing_cycle_anchor, volume tiers negative line item edge case
- [[source-stripe-usage-based-billing-manage-setup]] — UBB management: transform_quantity, mid-cycle price updates, backdated subscriptions, cancellation
- [[source-stripe-bank-transfers]] — Bank transfers: virtual account model, customer balance (75/90 day rules), international wires, disputes (USD/CAD), sender info API, Connect
- [[source-stripe-bank-transfers-accept-payment]] — Bank transfers integration: PI creation per region, status lifecycle, reconciliation modes, Checkout constraints, testing API
- [[source-stripe-customer-balance]] — Customer balance: cash vs invoice balance, retrieve API, pay-from-balance, 7 transaction types
- [[source-stripe-customer-balance-reconciliation]] — Reconciliation: automatic priority order, manual API, cash_balance.funds_available webhook, 75/90-day rules
- [[source-stripe-customer-balance-funding-instructions]] — Funding instructions: createFundingInstructions API, per-region financial_addresses schemas, EU VBAN limit
- [[source-stripe-bank-transfers-vban]] — VBAN permanence, allocation triggers, best practices, per-region daily/lifetime limits
- [[source-stripe-bank-transfers-refunds]] — 4 refund flows (payment/cash balance), refund lifecycle, 45-day/180-day limits, no SWIFT refunds
- [[source-stripe-fr-meal-vouchers]] — France titres-restaurant: CNTR approval, SIRET provisioning, off-Stripe settlement, no refunds, 25 EUR daily cap, split tender
- [[source-stripe-fr-meal-vouchers-accept-payment]] — Integration: PaymentIntent + SIRET, CVC save, test card + test SIRETs
- [[source-stripe-fr-meal-vouchers-connect]] — Connect: platform/direct charges only, fee collection via transfers, ConfirmationToken identification
- [[source-stripe-fr-meal-vouchers-check-balance]] — Balance check API (non-binding), response structure, test card, split tender order
- [[source-stripe-fr-meal-vouchers-save-payment]] — SetupIntent save, 0.30 EUR temp auth charge, on-session reuse with saved card
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — SIRET provisioning: Dashboard flow, postal code matching, immutability, Connect path, test SIRETs
- [[source-stripe-bnpl-overview]] — BNPL overview: 11 methods, product/API/transaction support matrices, Klarna standout, Affirm/Afterpay/Zip limits
- [[source-stripe-affirm]] — Affirm: financing packages (Standard/Enhanced), payment tiers, refunds, disputes, prohibited categories
- [[source-stripe-affirm-accept-payment]] — Affirm integration: 3 paths (Checkout/Elements/PI), 12-hour expiry, error codes, shipping tip
- [[source-stripe-affirm-messaging]] — Legacy affirmMessage Element (deprecated); Payment Method Messaging Element is recommended
- [[source-stripe-afterpay-clearpay]] — Afterpay/Clearpay: Cash App rebrand, country limits (5 countries), US tiers, dispute/refund windows
- [[source-stripe-afterpay-clearpay-accept-payment]] — Afterpay integration: 3-hour expiry, billing_details required, 3 paths
- [[source-stripe-afterpay-clearpay-messaging]] — Legacy afterpayClearpayMessage Element (deprecated); auto-localizes Clearpay for UK
- [[source-stripe-alma]] — Alma: EUR only (50-5k), T+3 payout, marketplace-only Connect, required customer terms
- [[source-stripe-alma-accept-payment]] — Alma integration: 1-hour expiry, QR code desktop auth, return_url required, 7-day manual capture
- [[source-stripe-billie]] — Billie: B2B Pay-in-30, multi-currency EU (EUR/SEK/NOK/DKK/GBP/CHF), 12-day dispute window
- [[source-stripe-billie-accept-payment]] — Billie integration: 7-120 day terms, return_url required, 7-day manual capture
- [[source-stripe-klarna]] — Klarna: 4 payment options, 23 countries, 13 currencies, cross-border rules, loss liability, refund mechanics
- [[source-stripe-klarna-accept-payment]] — Klarna integration: billing prefill, manual capture, 23-country test data, iOS webview
- [[source-stripe-klarna-set-up-future-payments]] — Klarna save/recurring: subscription reference consistency, on_demand metadata, mandate revocation
- [[source-stripe-klarna-best-practices]] — Klarna conversion: Express Checkout placement, PMME on product pages, line items, shipping/billing
- [[source-stripe-klarna-compliance]] — Klarna compliance: prohibited categories, UK FCA criminal risk, termination rights, AU DDO
- [[source-stripe-klarna-disputes]] — Klarna disputes: 180-day window, inquiry→chargeback, fee model (reversed if win), 5-day fraud evidence
- [[source-stripe-klarna-supplementary-data]] — Klarna supplementary data (preview): 8 verticals, acceptance/fraud improvement
- [[source-stripe-kriya]] — Kriya: B2B UK-only GBP, no Connect, ~36 prohibited categories, 12-day dispute window
- [[source-stripe-kriya-accept-payment]] — Kriya integration: return_url required, 7-day manual capture
- [[source-stripe-mondu]] — Mondu: B2B Pay-in-30, 14 EU/UK countries, multi-currency, no Connect, ~90 prohibited categories
- [[source-stripe-mondu-accept-payment]] — Mondu integration: return_url required, 7-day manual capture
- [[source-stripe-payment-on-invoice]] — Payment on invoice: consumer BNPL DE/AT, 14-day terms, risk-based, branded invoice, T+2
- [[source-stripe-scalapay]] — Scalapay: consumer BNPL, EUR-only all countries, 90-day refunds, no Connect, approval-based categories
- [[source-stripe-scalapay-accept-payment]] — Scalapay integration: return_url required, 7-day capture, Checkout limited to 8 EU countries
- [[source-stripe-sequra]] — SeQura: consumer BNPL Spain-only, Pay in 3/12, most extensive prohibited list (~160+ categories)
- [[source-stripe-sequra-accept-payment]] — SeQura integration: 7-120 day terms, return_url required, 7-day manual capture
- [[source-stripe-sunbit]] — Sunbit: US-only, 3/6/12/18-month installments, Connect supported, no manual capture, $60-$20k
- [[source-stripe-sunbit-accept-payment]] — Sunbit integration: return_url required, no manual capture, $60-$20k Checkout enforcement
- [[source-stripe-zip]] — Zip: AU+US, 3 products (Zip Pay/Money/Pay-in-4), 14-day direct resolution, 180-day disputes/refunds
- [[source-stripe-zip-accept-payment]] — Zip integration: return_url required, no manual capture, Direct API deprecated
- [[source-stripe-real-time-payments]] — Real-time payments: Pay by Bank/PayNow/PayTo/PromptPay/Swish, PayTo standout (SetupIntents)
- [[source-stripe-pay-by-bank]] — Pay by Bank (UK/Europe): open banking, 730-day refunds, no disputes, 35 merchant countries
- [[source-stripe-pay-by-bank-accept-payment]] — Pay by Bank integration: Checkout + Elements, statement_descriptor required, DE/GB Checkout only
- [[source-stripe-paynow]] — PayNow: SG-only QR code, 1.3% pricing, T+1 payout, 90-day refunds, no statement descriptor, Terminal
- [[source-stripe-paynow-accept-payment]] — PayNow integration: Checkout + Direct API, confirmPayNowPayment(), inline QR (no redirect)
- [[source-stripe-payto]] — PayTo: AU mandate-based, disputes (final), recurring, 44 banks, mandate field details
- [[source-stripe-pix]] — Pix: Brazil QR/string, Ebanx partner, IOF 3.5%, Pix Automático, non-challengeable disputes
- [[source-stripe-pix-accept-payment]] — Pix integration: 3 paths, setup/subscription Checkout mode, expires_after_seconds, CPF/CNPJ required
- [[source-stripe-pix-save-payment-details]] — Pix save/recurring: Checkout + Direct API, confirmPixSetup/Payment, QR code data fields, mandate revocation
- [[source-stripe-pix-automatico]] — Pix Automático: 3-day pre-debit notification, mandate fields, retry logic, daily schedule prohibited
- [[source-stripe-promptpay]] — PromptPay: TH-only QR, refund requires customer bank input, duplicate QR risk, send_invoice only
- [[source-stripe-promptpay-accept-payment]] — PromptPay integration: Checkout + Direct API, confirmPromptPayPayment(), email only billing field
- [[source-stripe-swish]] — Swish: SE-only mobile redirect + desktop QR, Stripe as MoR, 365-day refunds, no billing
- [[source-stripe-swish-accept-payment]] — Swish integration: 3 paths + mobile SDK, Direct API legal notice, next_action QR data, 20 refreshes, cancelable
- [[source-stripe-upi]] — UPI: India QR/redirect, 60-day refunds, 15k INR recurring limit, non-contestable disputes, UPI AutoPay
- [[source-stripe-upi-accept-payment]] — UPI integration: 4 paths, Checkout setup/subscription mode, 5-min QR expiry, delayed off-session notifications
- [[source-stripe-upi-set-up-future-payments]] — UPI save/recurring: confirmUpiSetup(), full address required, next_action QR data, on-session still redirects
- [[source-stripe-upi-autopay]] — UPI AutoPay: RBI AFA + 24-hour pre-debit notification, mandate defaults (15k INR, 10yr), Adaptive Pricing caveat
- [[source-stripe-vouchers]] — Vouchers hub: Boleto/Konbini/Multibanco/OXXO, cash in-person, 1-day confirmation, no immediate delivery
- [[source-stripe-boleto]] — Boleto: Brazil cash voucher, no refunds, 1-day confirmation, T+2 payout, 5–49,999.99 BRL
- [[source-stripe-boleto-accept-payment]] — Boleto integration: 4 paths, hosted_voucher_url, expires_after_days, confirmBoletoPayment(), next-biz-day webhook
- [[source-stripe-boleto-subscription]] — Boleto subscriptions: both send_invoice + charge_automatically, tax ID required for auto-charge
- [[source-stripe-boleto-invoices]] — Boleto invoices: auto_advance, charge_automatically still requires customer to pay voucher (not true auto-debit)
- [[source-stripe-konbini]] — Konbini: Japan cash voucher, instant confirmation, T+4 payout, 120–300k JPY, 19+ prohibited categories
- [[source-stripe-konbini-accept-payment]] — Konbini integration: confirmKonbiniPayment(), confirmation_number, product_description, expiration buffer, refund bank input
- [[source-stripe-multibanco]] — Multibanco: Portugal voucher, 2 flows (online/ATM), delayed confirmation, 365-day refunds, send_invoice only
- [[source-stripe-multibanco-accept-payment]] — Multibanco integration: 3 paths + mobile, 7-day expiry + 4-day buffer, confirmMultibancoPayment(), entity+reference
- [[source-stripe-oxxo]] — OXXO: Mexico cash voucher, next-biz-day confirmation, 10–10k MXN, no refunds, no subscriptions
- [[source-stripe-oxxo-accept-payment]] — OXXO integration: 4 paths + mobile, confirmOxxoPayment(), expires_after (not expires_at), 1–7 day expiry
- [[source-stripe-wallets]] — Wallets hub: 17 methods, Samsung Pay Terminal-only, MoMo/GCash waitlist, subscription caveats
- [[source-stripe-alipay]] — Alipay: CNY+10 currencies, 39 countries, 90-day refunds, recurring invite-only, Connect partial
- [[source-stripe-alipay-accept-payment]] — Alipay integration: 5 paths, safepay/ URL scheme, Android SDK live-mode only, confirmAlipayPayment()
- [[source-stripe-amazon-pay]] — Amazon Pay: worldwide, 240-day disputes, manual capture, 12 currencies, SEPA+installments via Amazon
- [[source-stripe-amazon-pay-accept-payment]] — Amazon Pay integration: 5 paths, 10-min auth window, 7-day manual capture, confirmPayment()
- [[source-stripe-amazon-pay-set-up-future-payments]] — Amazon Pay save/recurring: confirmAmazonPaySetup(), redirect_to_url, authorization text, iOS/Android
- [[source-stripe-apple-pay]] — Apple Pay: iOS/RN/Web, Stripe CSR required, domain registration, merchant tokens (iOS 16+), real card test only
- [[source-stripe-apple-pay-best-practices]] — Apple Pay best practices: certificate renewal, express checkout placement, default to Apple Pay
- [[source-stripe-apple-pay-cartes-bancaires]] — Cartes Bancaires + Apple Pay: EUR only, iOS one-line config, web automatic
- [[source-stripe-apple-pay-recurring]] — Apple Pay recurring: DPAN/MPAN cryptogram expiry, immediate SetupIntent CIT required, on_session forbidden
- [[source-stripe-apple-pay-merchant-tokens]] — Apple Pay MPAN types: recurring/auto-reload/deferred (iOS 16+), Express Checkout Element config, Sigma monitoring
- [[source-stripe-apple-pay-disputes-refunds]] — Apple Pay: liability shift (Visa iOS 16.2+ global, Europe below 16.2), disputes/refunds same as card
- [[source-stripe-cash-app-pay]] — Cash App Pay: US-only, off-session merchant bears fraud liability, no PM cloning in Connect
- [[source-stripe-cash-app-pay-accept-payment]] — Cash App Pay integration: 4 paths + mobile, 60-min auth, 20× QR refresh, manual capture, live auto-approves
- [[source-stripe-cash-app-pay-set-up-payment]] — Cash App Pay save/recurring: confirmCashappSetup(), mobile_auth_url 30-sec expiry, authorization text
- [[source-stripe-google-pay]] — Google Pay: Android/RN/Web, DPAN/FPAN/e-commerce token liability shift, domain registration, Sigma card_token_type
- [[source-stripe-grabpay]] — GrabPay: SG/MY only, OTP redirect, no disputes/recurring, mandatory branding guidelines
- [[source-stripe-grabpay-accept-payment]] — GrabPay integration: 4 paths + mobile, no minimum charge, confirmGrabPayPayment(), Android billing name
- [[source-stripe-link]] — Link: two PM type paths (link vs card+wallet), Instant Bank Payments exclusive, Thailand/Brazil caveat
- [[source-stripe-mb-way]] — MB WAY: Portugal phone-number wallet, 365-day refunds, 7-day disputes, €1k daily limit, Stripe Inc descriptor
- [[source-stripe-mb-way-accept-payment]] — MB WAY integration: Checkout + Elements (beta flag) + confirmMbWayPayment(), 5 test phone numbers
- [[source-stripe-mobilepay]] — MobilePay: DK/FI card wallet, 3DS 1–7% invisible, Dankort→Visa/MC, 35 DKK/month Denmark fee, liability shift only with 3DS
- [[source-stripe-mobilepay-accept-payment]] — MobilePay integration: 4 paths + mobile, 5-min auth window, manual capture full only, redirect_to_url
- [[source-stripe-paypal]] — PayPal via Stripe: EU merchants only, marketplace Connect, 180-day refunds, fees not in Stripe tax invoice
- [[source-stripe-paypal-button]] — PayPal button: Stripe decides button vs redirect, blockers for ECE + Checkout, PayPal must not be sole PM type
- [[source-stripe-paypal-activate]] — PayPal activation: EU (ex Hungary), settlement preference, Connect manual onboarding, account switch disables recurring
- [[source-stripe-paypal-accept-payment]] — PayPal accept-a-payment: 5 platforms, auth windows by settlement type, preferred locale, statement descriptor, payer fields
- [[source-stripe-paypal-set-up-future-payments]] — PayPal save/recurring: Checkout setup mode, confirmPayPalSetup(), Fraudnet risk_correlation_id, mandate BAID, on-session return_url rules
- [[source-stripe-paypal-settlement]] — PayPal settlement preference: Stripe vs PayPal balance, Dashboard reporting, reconciliation, support ticket to change
- [[source-stripe-paypal-disputes]] — PayPal disputes: 180-day window, 2–19 day evidence, 30-day decision, no Stripe appeals, multiple disputes per payment
- [[source-stripe-paypal-reconciliation]] — PayPal reconciliation: reference field (Invoice ID) vs transaction_id (Transaction ID), PayPal settlement report
- [[source-stripe-paypal-import]] — PayPal billing agreement import: billing_agreement_id on SetupIntent, offline mandate, no cancellation webhooks for imported BAIDs
- [[source-stripe-revolut-pay]] — Revolut Pay: UK/EU, 6 currencies, full feature set, 120-day disputes, 35-day Revolut decision
- [[source-stripe-revolut-pay-accept-payment]] — Revolut Pay integration: 6 platforms, mobile redirect + desktop QR (20× refresh), 7-day manual capture, live auto-approves
- [[source-stripe-revolut-pay-set-up-future-payments]] — Revolut Pay save/recurring: on-session always redirects, confirmRevolutPaySetup(), authorization text, detach triggers mandate.updated
- [[source-stripe-paypay]] — PayPay: Japan/JPY only, no recurring/Connect/disputes, 365-day instant refunds, 50–1M JPY limits
- [[source-stripe-paypay-accept-payment]] — PayPay integration: 6 platforms, payment mode only, redirect-based, live mode no approve/decline, 5 error codes
- [[source-stripe-satispay]] — Satispay: Italy/EUR only, 20 eurozone merchant countries, 12-day dispute evidence, 180-day refunds, 14 prohibited categories
- [[source-stripe-satispay-accept-payment]] — Satispay integration: 4 web paths + iOS/Android, payment mode only, manual capture 7-day, confirmSatispayPayment(), 5 error codes
- [[source-stripe-secure-remote-commerce]] — SRC/Click to Pay: US only, replaces Visa Checkout + Masterpass, card.masterpass PM type, Masterpass deprecated
- [[source-stripe-vipps]] — Vipps: Norway/NOK card wallet, private preview, card transaction underneath, daily Vipps fee billing, BankAxept→Visa/MC
- [[source-stripe-vipps-accept-payment]] — Vipps integration: 3 paths (Checkout/Elements/Direct API), 5-min auth window, full-amount-only capture, card retry in app
- [[source-stripe-wechat-pay]] — WeChat Pay: 800M+ users, CNY+12 currencies, 22 merchant countries, no disputes/recurring/manual capture, partial Connect
- [[source-stripe-wechat-pay-accept-payment]] — WeChat Pay integration: Checkout + Direct API (web only), confirmWechatPayPayment(), QR from next_action, 37 business locations
- [[source-stripe-local-payment-methods-by-country]] — hub: Nigeria (Naira cards) + South Korea (KakaoPay, local cards), no local entity required
- [[source-stripe-nigeria-payment-methods]] — Nigeria MoR model: Naira cards/bank transfer/wallet, NGN/US only, 365-day refunds, no dispute challenge
- [[source-stripe-ng-bank-transfer-accept-payment]] — Naira bank transfer integration: ng_bank_transfer, 500–100M NGN limits, confirmPayment(), redirect flow
- [[source-stripe-ng-card-accept-payment]] — Naira card integration: ng_card, setup+subscription mode, 500–100M NGN limits, same MoR redirect flow
- [[source-stripe-ng-card-set-up-future-payments]] — Naira card save/recurring: SetupIntent + confirmNgCardSetup(), PaymentIntent setup_future_usage, off_session reuse, detach events
- [[source-stripe-korea-payment-methods]] — South Korea: local processor model, KR cards + Kakao/Naver/Samsung/PAYCO, KRW, 28 countries, installments, 30-day subscription notice
- [[source-stripe-kr-card-accept-payment]] — KR card integration: kr_card, 100 KRW minimum, NICEPAY disclosure required, confirmPayment(), redirect flow
- [[source-stripe-kr-card-set-up-future-payments]] — KR card save/recurring: Accounts v2 + v1, confirmKrCardSetup(), setup_future_usage, automatic capture only for recurring
- [[source-stripe-kakao-pay-accept-payment]] — Kakao Pay integration: buyer email required, 100 KRW min/2M KRW stored value max, not in SG, NICEPAY disclosure
- [[source-stripe-kakao-pay-set-up-future-payments]] — Kakao Pay save/recurring: Accounts v2 + v1, confirmKakaoPaySetup(), NICEPAY account authorization, automatic capture only
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay integration: naver_pay, funding source card/points, 28 countries (incl. SG), no email required, NICEPAY + branding
- [[source-stripe-naver-pay-set-up-future-payments]] — Naver Pay save/recurring: Accounts v2 + v1, confirmNaverPaySetup(), automatic capture only, currency:ngn bug
- [[source-stripe-payco-accept-payment]] — PAYCO integration: payco, payment mode only (no recurring), 28 countries incl. SG, NICEPAY disclosure
- [[source-stripe-custom-payment-methods]] — Custom PMs overview: type:'custom'/cpmt_ IDs, integration matrix, marks compliance, crypto restriction (ID/TH), Stripe disclaimer
- [[source-stripe-paypal-custom-payment-method]] — PayPal as CPM: low-code adapter for Checkout, EU→standard PM vs global→CPM adapter decision rule
- [[source-stripe-payment-method-support]] — comprehensive reference: 36 PMs country/currency + product support matrices + API support (setup_future_usage, return_url)
- [[source-stripe-payment-method-connect-support]] — Connect reference for 31 PMs: capability names, MoR tables, notable restrictions (Alma/PayPal marketplace-only, ACH cloning, iDEAL compliance)
- [[source-stripe-pmd-registration]] — Domain registration: 6 PMs (Apple Pay required), PaymentMethodDomain API, iframe Safari 17+ rules, Connect charge-type routing
- [[source-stripe-dynamic-payment-methods]] — Dynamic PMs: migration guide, excluded_payment_method_types (wallets exception), 6 eligibility criteria, AI ordering models
- [[source-stripe-a-b-testing-payment-methods]] — A/B testing: Dashboard-only, 50/50 default, 80K sessions for 100 BPS detection, z-test, 35 PMs, Connect platform-level only
- [[source-stripe-payment-method-rules]] — PM rules: amount/location conditions, no-code Dashboard setup, subscription caveat, currency auto-conversion, location testing via email
- [[source-stripe-payment-method-configurations]] — PM configurations: named pmc_ sets, Web/iOS/Android integration, Apple Pay on/Google Pay off defaults, config vs exclusion decision rule
- [[source-stripe-link-payment-methods]] — Link payment methods (US-only): Instant Bank Payments/Klarna/Pix/UPI/Stablecoins, zero integration, 5 eligibility criteria, BNPL individually configurable
- [[source-stripe-instant-bank-payments]] — Instant Bank Payments: 2-day guaranteed settlement, < $5K limit, ACH priority rule workaround, Stripe-funded cash back, 5 test scenarios
- [[source-stripe-klarna-on-link]] — Klarna on Link: US-only, Payment Links/Checkout/PE only, immediate merchant settlement, test cards
- [[source-stripe-pix-on-link]] — Pix on Link: US/BRL only, 5 BRL–3K USD limit, Ebanx provider, IOF 3.5% customer tax, one-time/on-session only
- [[source-stripe-stablecoins-on-link]] — Stablecoins on Link: US/USD only, 1–10K USD, any crypto wallet, USD settlement guaranteed, refunds as stablecoins, no disputes
- [[source-stripe-upi-on-link]] — UPI on Link: US/INR only, 1–100K INR, QR/app redirect, virtual payment address saved, 60-day refunds, uncontestable disputes
- [[source-stripe-checkout-link]] — Link with Checkout: dynamic vs manual listing (card required), OTP test codes, sandbox warning, Connect, disable per PMC
- [[source-stripe-elements-link]] — Link Auth Element (Elements): page order, multi-page support, React integration, onChange event, supported PMs for signup
- [[source-stripe-express-checkout-link]] — Link in Express Checkout Element: 6 one-click PMs, dynamic button sorting, no frontend changes needed
- [[source-stripe-payment-element-link]] — Link in Payment Element: pass-email vs collect-email, prefill tool (page scan/local memory), accelerated sign-up
- [[source-stripe-payment-request-button-link]] — Link in Payment Request Button (deprecated, 90-day auth window); use ECE/PE/Auth Element instead
- [[source-stripe-card-element-link]] — Link in Card Element (deprecated): 90-day auth, 350px/28px min size, disableLink param, detailed Connect eligibility rules
- [[source-stripe-mobile-payment-element-link]] — Link in Mobile PE: iOS/Android/React Native, defaultBillingDetails prefill, sandbox OTP 000000
- [[source-stripe-invoicing-link]] — Link with Invoicing: Dashboard-only, Hosted Invoice Page, Invoices + Subscriptions APIs, zero code
- [[source-stripe-link-payment-integrations]] — Link integration paths: PM vs card-integration, IC+ caveat, backup payment source, non-card fixed values (last4=0000)
- [[source-stripe-add-link-elements-integration]] — Full custom checkout guide: 3 email strategies, React+HTML+JS, shipping/prefill/manual capture (7 days), submit flow (1424 lines)
- [[source-stripe-link-save-and-reuse]] — SetupIntent save-and-reuse: same 3 strategies + Accounts v2, confirmSetup, charge-later off_session (1263 lines)
- [[source-stripe-payments-optimization]] — Authorization Boost: Adaptive Acceptance + card updater + network tokens, probabilistic recovery calc, IC+ cost savings
- [[source-stripe-authorization-boost-ab-test]] — Auth Boost A/B test: 30-day free test, CAU runs on both groups, 12-month cooldown, 37-day results, paid add-on
- [[source-stripe-payments-recommendations]] — General recommendations: NTID for MIT, AVS/Visa postal codes, Radar rule swap, 3DS reduction, 3DS integration check
- [[source-stripe-3d-secure-authentication-flow]] — 3DS auth: 3DS2 flow, manual API trigger, web iframe rules, iOS/Android/RN integration, liability shift, 6 web test cards
- [[source-stripe-sca-exemptions]] — SCA exemptions (EEA/CH/UK): Low Value, TRA limits (EEA ≤250 EUR / UK ≤220 GBP), MIT, Data Only (no liability shift)
- [[source-stripe-standalone-3ds]] — Standalone 3DS: decouple auth from authorization, IC+ only, cryptogram to any PSP, no Malaysia/Thailand
- [[source-stripe-3ds-import]] — Import 3DS results: travel/third-party 3DS, confirm+error_on_requires_action, exemption import, Cartes Bancaires cb_avalgo
- [[source-stripe-3ds-sigma-query]] — Sigma authentication_report_attempts: is_final_attempt dedup, auth rate calc, SCA exemption columns
- [[source-stripe-sca-readiness]] — SCA readiness: EEA scope, grandfathering (EU Dec 2020/UK Sep 2021), off-session checklist, MIT mandate, Charges API not SCA-ready
- [[source-stripe-currencies]] — Supported currencies: minor units formatting, ISK/HUF/TWD/UGX special rules, min/max charge amounts, EEA card definition
- [[source-stripe-react-stripejs]] — React Stripe.js reference: CheckoutElementsProvider/useCheckoutElements + Elements/useStripe/useElements/ElementsConsumer
- [[source-github-stripe-node]] — cumulative `stripe` Node SDK history through `22.4.0`: server/runtime boundary, typed resources, retries/idempotency, webhooks, pagination, Checkout, PaymentIntents, SetupIntents, billing, and refunds
- [[changelog-github-stripe-node]] — package-qualified stripe-node release history retaining `22.1.1` and `22.4.0`
- [[source-github-react-stripe-js]] — cumulative react-stripe-js history: legacy v6.3.0 plus `@stripe/react-stripe-js@6.8.0` providers, hooks, lifecycle, SSR, compatibility, and beta Terms Element
- [[changelog-github-react-stripe-js]] — package-qualified react-stripe-js release history
- [[source-stripe-bizum]] — Bizum: Spain-only real-time, phone auth, 395-day refunds, 40-day evidence, onboarding required
- [[source-stripe-declines-overview]] — Declines overview: 3 failure types (issuer/blocked/invalid), outcome object fields, Radar block reasons, Adaptive Acceptance blocking, allow list
- [[source-stripe-card-declines]] — Card declines: network codes, advice_code retry table, max 8 retries, on/off-session handling, geographic + FSA/HSA restrictions
- [[source-stripe-decline-codes]] — Decline codes reference: 50 card codes + 19 LPM codes, fraud codes to mask, deprecated codes
- [[source-stripe-network-decline-codes]] — Network decline codes: ACH/BECS/Bacs/SEPA/CAD PAD/Cash App Pay raw→Stripe code mapping tables
- [[source-stripe-disputes-how-disputes-work]] — Dispute lifecycle: EFWs (80% convert), inquiries (AmEx/Discover), timing, fees, unchallengeable disputes, LPM differences
- [[source-stripe-disputes-responding]] — Dispute response: 7–21d deadline, Visa CE 3.0, compliance disputes (500 USD fee), evidence rules (one-shot, 4.5 MB, 19p Mastercard)
- [[source-stripe-disputes-categories]] — 8 dispute categories + Visa Noncompliant; evidence fields by product type; prevention guidance; 7 payment methods mapped
- [[source-stripe-disputes-reason-codes]] — Dispute reason codes: Visa/MC/Amex per-code evidence guidance; CP vs CNP fraud evidence; customer pre-dispute obligation rule
- [[source-stripe-disputes-visual-evidence]] — Visual evidence packets: 7 categories, approved/denied scenarios, 62 illustrative images in raw/assets/
- [[source-stripe-disputes-best-practices]] — Evidence best practices: win likelihood table (5 dots=60%), file limits, CE 3.0, auto-populated fields, partial refund handling
- [[source-stripe-disputes-api]] — Disputes API: retrieve/update/list, text vs file evidence, 150k char limit, file upload workflow, multiple disputes per payment
- [[source-stripe-disputes-visa-ce3]] — Visa CE 3.0 API: qualifying criteria (10.4, 2 prior txns 120-364 days), enhanced_evidence object, status lifecycle, test card
- [[source-stripe-disputes-visa-compliance]] — Visa compliance disputes: identify, close (no fee) vs respond (fee_acknowledged required), 500 USD fee, test card
- [[source-stripe-disputes-withdrawals]] — Dispute withdrawals: withdrawn ≠ won, still counts vs rate, only chargebacks withdrawable, evidence still required, late withdrawals
- [[source-stripe-disputes-high-risk-lists]] — MATCH (code 4: >1% MC chargebacks + $5k) and VMSS (code 22: 1000 disputes + 1.8%) criteria, removal rules
- [[source-stripe-disputes-measuring]] — Dispute activity (by dispute date, for monitoring) vs dispute rate (by charge date, for fraud analysis); 0.75% threshold; EFW/VAMP
- [[source-stripe-disputes-monitoring-programs]] — VAMP/VSEFP (Visa), ECM/HECM/EFM (Mastercard), AusPayNet FMP: thresholds, fine schedules, prevention best practices
- [[source-stripe-disputes-prevention]] — Dispute prevention: resolution (Radar rules, no rate impact), deflection (Verifi/Order Insights), Smart Disputes (AI evidence)
- [[source-stripe-disputes-prevention-how-it-works]] — RDR/Ethoca/OI/CE3.0 mechanics: OI data fields, CE 3.0 pre-dispute block criteria, RDR limitations
- [[source-stripe-smart-disputes]] — Smart Disputes: AI evidence auto-submission, win-only fee model, eligibility factors, no integration required
- [[source-stripe-smart-disputes-setup]] — Smart Disputes setup: intended_submission_method, smart_disputes.status/recommended_evidence, data quality fields at charge+dispute time
- [[source-stripe-smart-disputes-auto-respond]] — Smart Disputes auto-respond: direct/Connect/connected account config, preference (on/off/inherit) API field
- [[source-stripe-radar-how-it-works]] — Radar: 3 tiers (base/Fraud Teams/Platforms), pricing, screened payment methods, 6 core features
- [[source-stripe-radar-optimize-risk-factors]] — Risk factors: advanced +36%, IP +12%, email +11%; integration ranking; Stripe.js on every page; Customer object best practices
- [[source-stripe-radar-sessions]] — Radar Sessions: for direct API/third-party tokenization; createRadarSession(); on/off-session attachment strategy
- [[source-stripe-radar-risk-evaluation]] — Risk levels (highest/elevated/normal), 0-99 score, outcome fields, object support, feedback loop, 92%/82%/71% network coverage
- [[source-stripe-radar-custom-fraud-models]] — Custom fraud models: business metadata + global signals, per-merchant training, no integration changes needed
- [[source-stripe-radar-customer-evaluation]] — Customer Evaluation API: multi_accounting + account_sharing upfunnel signals, same Customer ID constraint
- [[source-stripe-radar-free-trial-abuse]] — Free trial abuse: blocks high-risk trial starts, auto-detected, Sigma monitoring via rule_decisions table
- [[source-stripe-radar-payg-abuse]] — PAYG abuse: non_payment_abuse signal for usage-based billing, fail-open Payment Evaluation API
- [[source-stripe-radar-bot-abuse]] — Bot score (0-99, Checkout only): anti-scripting enforcement via Dashboard/Sigma/:bot_score: rules
- [[source-stripe-radar-multiprocessor]] — Multiprocessor: evaluate non-Stripe payments with Radar; 3 signals; card-only PaymentMethod required
- [[source-stripe-radar-issuing]] — Radar for Issuing: IssuingAuthorizationEvaluation API, real-time fraud scoring before authorization decision
- [[source-stripe-radar-risk-settings]] — Risk settings (3 presets), 4 risk controls, 5 scores (fraudulent_dispute/EFW/bot/risk_score deprecated)
- [[source-stripe-radar-supported-payment-methods]] — Radar PM coverage: cards/ACH/SEPA fully supported; BNPL/wallets/stablecoin in preview
- [[source-stripe-radar-reviews]] — Review queue: Smart Refunds (72% very high), actions, assignments, review.opened/closed webhooks
- [[source-stripe-radar-risk-insights]] — Risk insights: fraud factor multipliers, top factors, related payments, 6-month data limit
- [[source-stripe-radar-reviews-auth-capture]] — Auth-capture review: approve ≠ capture; review.closed webhook auto-capture pattern
- [[source-stripe-radar-lists]] — Lists: default (Cards/ACH/SEPA), 11 custom types, 50k limit, 30-day allowlist max, fraud report auto-populates block lists
- [[source-stripe-radar-rules]] — Rules: 4 actions, built-in rules, syntax, 3DS attributes, Radar Assistant, 200 rule limit
- [[source-stripe-radar-rules-reference]] — Rules reference: processing order, attribute types, operators, velocity buckets, missing attributes, metadata scopes
- [[source-stripe-radar-rules-supported-attributes]] — Supported attributes: 5 categories, 827-line reference (risk/IP/email/distance/fingerprint/time/crypto)
- [[source-stripe-radar-testing]] — Test cards for highest/elevated risk, rule backtesting (6-month historical), when to implement each rule type
- [[source-stripe-radar-rules-disputes]] — Dispute resolution rules: Resolve dispute action, is_fraudulent + network_reason_code attributes
- [[source-stripe-radar-analytics]] — Radar analytics: fraud/dispute/block rate charts, benchmarks, rule match breakdown, 24hr delay
- [[source-stripe-radar-fraud-alerts]] — Fraud alerts: auto-detected attack patterns, email+bell, investigation page, Fraud Teams extra actions
- [[source-stripe-radar-fraud-insights]] — Fraud insights: Insights tab, default filters (risk>65+velocity), pivot chart, drill-down transaction list
- [[source-stripe-radar-for-platforms]] — Radar for Platforms: connected account risk scores (highest≥90%/elevated 50-89%), investigation, reject (7 codes), reserves
- [[source-stripe-radar-account-risk-signals]] — Account Signals API: 3 signal types (fraudulent merchant/delinquency/website), webhook-driven
- [[source-stripe-disputes-prevention-overview]] — Dispute prevention nav page (links to fraud types, card testing, identify fraud, best practices)
- [[source-stripe-disputes-fraud-types]] — 7 fraud types: stolen cards, overpayment, card testing, alternative refunds, marketplace, friendly fraud + key rules
- [[source-stripe-disputes-card-testing]] — Card testing: identification symptoms, prevention (Stripe integration + CAPTCHA/rate limits/velocity rules)
- [[source-stripe-disputes-identifying-fraud]] — Fraud indicators: shipping patterns, scripted comms, "preferred shipper", donation credit-limit test, digital goods
- [[source-stripe-disputes-verification]] — CVC/AVS verification: how they work, Radar rules, limitations (wallets/off-session/country support)
- [[source-stripe-disputes-prevention-best-practices]] — Fraud prevention best practices: 3 tiers (everyone/Fraud Teams/developers), ToS full text rule, auth+capture, CE 3.0
- [[source-stripe-disputes-advanced-fraud-detection]] — Advanced fraud detection: device+activity risk factors via Stripe.js/SDKs, hCaptcha, disable options
- [[source-stripe-disputes-customer-abuse]] — Customer abuse: refund/resale/trial abuse, Sigma refund query, Radar velocity rules for resellers
- [[source-stripe-payouts]] — Payouts: initial timing (7-14d), schedule options, multi-currency settlement, 80+ country bank account formats
- [[source-stripe-payouts-reconciliation]] — Payout reconciliation: API flow (BalanceTransactions), expand pattern, manual payout caveat
- [[source-stripe-payouts-trace-ids]] — Payout trace IDs: 3 statuses, 10-day window, unsupported countries, Connect support
- [[source-stripe-payouts-statement-descriptors]] — Payout statement descriptors: 2 levels, precedence (payout>account>STRIPE), bank display caveat
- [[source-stripe-payouts-multicurrency]] — Multi-currency settlement: 10 regions, no FX fees, 1 bank account per currency, minimum balance
- [[source-stripe-payouts-next-day]] — Next-day settlement: US only, 0.6%/month, ACH excluded, >$1M adds 1 day, vs Instant Payouts
- [[source-stripe-payouts-instant]] — Instant Payouts: 37 countries, within 30 min, 1–1.5% fee, 10/day limit, instant_available balance
- [[source-stripe-payouts-start-of-day]] — Customized start of day: APAC only (10 countries), local timezone grouping, not retroactive
- [[source-stripe-payouts-minimum-balance]] — Minimum balance: retain fixed amount after payout, 4-5× daily vol, Connect API, not BR/IN/TH
- [[source-stripe-receipts]] — Receipts: 30-day expiry, auto/manual send, refund receipts, invoice itemized, Connect branding rules
- [[source-stripe-refunds]] — Refunds: reversal vs refund, ARN tracing, 7 failed reasons, cancel rules, Connect behavior, events
- [[source-stripe-payments-existing-customers]] — Existing customer checkout: 4 paths, allow_redisplay rules, prefill conditions/priority, 30-min timeout
- [[source-stripe-two-step-confirmation]] — Two-step checkout: ConfirmationToken flow, Elements options, saved PMs, tax, layouts (906 lines)
- [[source-stripe-surcharge]] — Surcharges (preview): US/CA/AU/NZ, enforce_validation, amount-inclusive rule, refund proration, multicapture
- [[source-stripe-accept-payment-deferred]] — Deferred intent: render Element before PI/SI, elements.submit(), dynamic amount updates, payment+setup modes
- [[source-stripe-finalize-payments-server]] — Server-side confirmation: paymentMethodCreation='manual', ConfirmationToken→server confirm, handleNextAction
- [[source-stripe-moto]] — MOTO: SCA out-of-scope exemption, PCI compliance required, moto parameter on PI/SI
- [[source-stripe-payments-without-auth]] — Legacy US/CA-only: CardElement + createPaymentMethod, error_on_requires_action=true, synchronous
- [[source-stripe-save-card-without-auth]] — Legacy save card (US/CA): createPaymentMethod→Customer, error_on_requires_action, setup_future_usage=on_session
- [[source-stripe-migrate-basic-card-integration]] — Migrate legacy to auth-handling: remove error_on_requires_action, confirmation_method='manual', handleCardAction
- [[source-stripe-vault-and-forward]] — Vault and Forward API: forward card details to 30+ processors, replacement fields, wallet support, PGP encryption
- [[source-stripe-forwarding-third-party]] — Payment Element multiprocessor: paymentMethodCreation='manual', createPaymentMethod→ForwardingRequest
- [[source-stripe-forwarding-token-vault]] — Own token vault: PCI compliance, HTTPS/JSON only, bearer token, CVC one-time, 15-sec timeout
- [[source-stripe-payment-line-items]] — Payment line items: L2/L3 interchange savings, Klarna/PayPal auth rates, field requirements, MCC eligibility, arithmetic validation
- [[source-stripe-payment-line-items-flexible]] — Payment line items with flexible payments: multicapture aggregation rules, overcapture, incremental auth, partial auth mismatch handling, surcharge
- [[source-stripe-industry-metadata]] — Industry metadata (T&E): car rental/lodging/flight fields, MCC eligibility, card vs Klarna field split, array behavior, Klarna-exclusive verticals
- [[source-stripe-multicapture]] — Multicapture: IC+ feature, 50-capture limit, final_capture, Connect rules, refund limitations, test cards
- [[source-stripe-overcapture]] — Overcapture: IC+ feature, percent limits by network/category, SCA constraints, amount_authorized field, test cards
- [[source-stripe-extended-authorization]] — Extended authorization (online): IC+ feature, 30-day window by network/category, capture_before field, 2023 changes
- [[source-stripe-incremental-authorization]] — Incremental authorization (online): IC+ feature, 10-increment limit, per-increment cap, SCA MIT handling, does not extend auth window
- [[source-stripe-partial-authorization]] — Partial authorization: IC+ feature, debit/prepaid insufficient balance, AmEx/Visa restrictions, overcapture excluded, partial+incremental combo
- [[source-stripe-flexible-features-migration]] — Beta-to-GA migration for incremental auth, overcapture, extended auth, multicapture: param renames, new mandatory steps, multicapture 400 edge case
- [[source-stripe-off-session-payments-api]] — Off-Session Payments API (v2): smart retries via AI, multi-processor routing, cadence/retry_strategy params
- [[source-stripe-orchestration]] — Orchestration (private preview): rule-based routing across processors, retry on different processor, processor-of-record rule
- [[source-stripe-orchestration-route-payments]] — Orchestration implementation: payments_orchestration API param, Payment Records replace Charges, Balance Transaction/webhook changes
- [[source-stripe-orchestration-rules]] — Orchestration rules: 7 conditions, left-to-right execution, one-active-set limit, cannot edit active rules
- [[source-stripe-orchestration-retries]] — Orchestration cross-processor retries: 3DS/ineligible features no-retry, Radar blocks retry, Adaptive Acceptance interaction
- [[source-stripe-orchestration-feature-support]] — Orchestration feature matrix: Adyen/Braintree/Worldpay WPG, orchestration_unsupported error, error protection
- [[source-stripe-orchestration-wallet-payments]] — Orchestration wallet payments: Apple Pay/Google Pay routing, off_session=true for saved wallets
- [[source-stripe-crypto-onramp]] — Fiat-to-crypto onramp: Stripe as merchant of record, 3 integration modes, KYC handled, application required
- [[source-stripe-crypto-onramp-stripe-hosted]] — Stripe-hosted onramp: currencies (ETH/SOL/BTC/USDC+), geo restrictions, frontend redirect URL vs backend session API
- [[source-stripe-crypto-onramp-embedded]] — Embedded onramp: credit/debit/ApplePay/ACH, instant delivery post-KYC, Link for returning users, webhook per status change
- [[source-stripe-crypto-onramp-embedded-quickstart]] — Embedded quickstart: Node.js server, React client, OnrampSession API, CryptoElements, dark mode, sandbox values
- [[source-stripe-crypto-onramp-embedded-setup]] — Embedded extended setup: session states, customer info pre-population, Quotes API, 14 error codes, mobile integration, session persistence
- [[source-stripe-crypto-onramp-embedded-components]] — Embedded Components (headless, private preview): Link OAuth, state machine, SDK methods, headless session, quote refresh
- [[source-stripe-crypto-onramp-embedded-components-integration]] — Embedded Components integration guide: Web/RN/Android, 13 networks, last_error codes, full SDK reference, LinkAuthIntent APIs
- [[source-stripe-crypto-onramp-kyc-integration]] — KYC tier system: L0/L1/L2 tiers, verification status values, session error codes + next-step logic
- [[source-stripe-agentic-commerce-for-sellers]] — Agentic Commerce Suite: catalog feed (v2 API), order fulfillment, order approval + customization hooks, manual capture
- [[source-stripe-agentic-commerce-custom-integration]] — ACS custom integration (third-party processors): reverse API hooks, SPT resolve + credential types, payment recording
- [[source-stripe-mcp-monetize]] — MCP app monetization: Redirect (public) vs Instant Checkout (OpenAI private beta), feature comparison
- [[source-stripe-mcp-accept-payment]] — MCP accept payment: Redirect (Checkout Session) + Instant Checkout (window.openai.requestCheckout + SPT) integration
- [[source-stripe-agentic-commerce-for-agents]] — ACS for agents: OCA lifecycle, SFTP product feeds, RequestedSession checkout, payment methods, next actions, mobile SDK
- [[source-stripe-machine-payments]] — Machine Payments (Frontier): agent-to-API pay-per-use, MPP + x402 protocols, Base/Solana/Tempo, min 0.01 USDC, NY+TX excluded
- [[source-stripe-machine-payments-mpp]] — MPP implementation: mppx library, HTTP 402 middleware, crypto + SPT flows, link-cli testing
- [[source-stripe-machine-payments-mpp-quickstart]] — MPP Hono quickstart: /crypto/paid + /spt/paid endpoints, NodeCache deposit address caching
- [[source-stripe-machine-payments-x402-quickstart]] — x402 Hono quickstart: Base network, @x402/hono middleware, facilitator, purl CLI testing
- [[source-stripe-machine-payments-x402]] — x402 integration guide: USDC contract addresses for Tempo/Base/Solana, CDP mainnet facilitator
- [[source-stripe-shared-payment-tokens]] — SPT: seller (use granted token) + agent (issue token, handle next actions, revoke) flows, webhooks
- [[source-stripe-agentic-commerce-product-feed]] — ACS catalog feed: 4 feed types, field reference (shipping/tax/variants/relationships/compliance), upsert vs replace
- [[source-stripe-agentic-commerce-sftp-catalog]] — ACS SFTP ingestion (agent side): directory structure, manifest pattern, deletion rules, idempotency
- [[source-stripe-ucp]] — Universal Commerce Protocol: open standard, 4 capabilities, Stripe as UCP Tech Council member
- [[source-stripe-acp]] — Agentic Commerce Protocol: co-built by Stripe/OpenAI/Meta, 5 capabilities (checkout/cart/payment/auth/orders)
- [[source-stripe-billing-apis]] — Billing API objects overview: Subscription→Invoice→PaymentIntent chain, 11 objects, Entitlements, Account v2 vs Customer v1
- [[source-stripe-subscriptions-overview]] — Subscription lifecycle: 8 statuses, payment behavior, 23h window, async PM behavior, payment status matrix
- [[source-stripe-checkout-subscriptions-quickstart]] — Checkout subscription quickstart: lookup_key, customer portal, 5 webhook events, trial/billing-anchor/auto-tax
- [[source-stripe-subscriptions-design-integration]] — Subscriptions design guide: 4 pricing models, 7 checkout interfaces, 3 billing timing models, integration matrix
- [[source-stripe-build-subscriptions]] — Full subscriptions integration guide: 3 UI paths, billing_mode:flexible, provision access, test payment methods
- [[source-stripe-recurring-pricing-models]] — Recurring pricing models reference: flat rate, per-seat, tiered, usage-based
- [[source-stripe-flat-rate-pricing]] — Flat rate pricing setup: Product + monthly/yearly Price + Subscription API, can't edit after subscription created
- [[source-stripe-per-seat-pricing]] — Per-seat pricing: flat rate API + quantity param in subscription items (seats = units)
- [[source-stripe-usage-based-pricing]] — Usage-based pricing: fixed fee+overage (licensed+metered prices), pay-as-you-go, credit burndown via billing.creditGrants
- [[source-stripe-tiered-pricing]] — Tiered pricing: volume vs graduated math, flat_amount per tier, quantity=0 edge case
- [[source-stripe-pricing-table]] — Pricing table: no-code embed, CustomerSession pass-through, custom CTA, limitations (no usage-based, no Connect)
- [[source-stripe-subscriptions-setup-intents]] — SetupIntents for zero-payment subs: auto-created, auth vs authorization failures, doesn't auto-cancel
- [[source-stripe-subscriptions-migration]] — Subscription migration: Zuora/Recurly/Chargebee → toolkit or APIs, PAN import, decision matrix
- [[source-stripe-subscriptions-migration-toolkit]] — Billing toolkit: 3 CSV types, 24h go-live buffer, 10h cancel window, timing advice, validation errors
- [[source-stripe-subscriptions-migration-api]] — API migration: Subscription Schedules (>30d future), legacy pricing, mid-cycle continuity, test clocks
- [[source-stripe-subscriptions-webhooks]] — Subscription webhooks: 22 events, invoice.created 72h risk, access expiration pattern, EventBridge/Event Grid
- [[source-stripe-subscriptions-billing-cycle]] — Billing cycle anchor: billing_cycle_anchor_config (monthly/yearly), direct timestamp, reset to now, trial-as-anchor
- [[source-stripe-subscriptions-trial-offers]] — Trial Offers API (preview): 4 use cases, flexible billing required, status behavior, opt-in cancellation, billing anchor
- [[source-stripe-subscriptions-trial-compliance]] — Trial compliance: 7-day reminder emails, statement descriptor 22-char limit + * TRIAL OVER, manual path
- [[source-stripe-subscriptions-free-trials]] — Legacy trial_end: trial_period_days, missing_payment_method (cancel/pause/create_invoice), resume, combine with billing anchor
- [[source-stripe-subscriptions-billing-mode]] — Flexible billing mode: migrate API, proration_discounts, schedule inheritance, API version defaults, cannot revert
- [[source-stripe-subscriptions-billing-mode-compare]] — Classic vs flexible: prorations, usage billing, cancellation, trials, mixed intervals comparison
- [[source-stripe-subscriptions-mixed-interval]] — Mixed interval subscriptions: item-level periods, interval alignment rules, dunning behavior, limitations
- [[source-stripe-subscriptions-coupons]] — Coupons and promotion codes: duration behaviors, stackable discounts, promo code restrictions, update rules
- [[source-stripe-bizum-accept-payment]] — Bizum accept-a-payment: 4 integration paths, Direct API phone collection, iOS/Android SDK
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Metronome-documented Indian-card flow in which Stripe creates and manages the SetupIntent mandate, reports action-required handling, and owns mandate lifecycle
