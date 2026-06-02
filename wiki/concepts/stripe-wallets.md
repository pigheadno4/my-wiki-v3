---
title: "Wallets (Stripe)"
type: concept
category: technology
tags: [stripe, wallets, alipay, amazon-pay, apple-pay, cash-app, google-pay, grabpay, link, mb-way, mobilepay, paypal, paypay, revolut-pay, samsung-pay, satispay, stablecoins, vipps, wechat-pay]
---

## Definition

Wallet payment methods let customers pay using either a saved payment credential (tokenized card or bank account) or a stored wallet balance. The wallet authenticates the customer and passes payment details to Stripe without the merchant handling sensitive data directly.

## Supported Wallets

| Wallet | API enum | Redirect | SetupIntents | Terminal |
| --- | --- | --- | --- | --- |
| Alipay | `alipay` | No | No | No |
| Amazon Pay | `amazon_pay` | Yes | Yes | No |
| Apple Pay | (no enum) | No | Yes | Yes |
| Cash App Pay | `cashapp` | Yes | Yes | No |
| Google Pay | (no enum) | No | Yes | Yes |
| GrabPay | `grabpay` | Yes | No | No |
| Link | `link` | No | Yes | No |
| MB WAY | `mb_way` | No | No | No |
| MobilePay | `mobilepay` | Yes | No | No |
| PayPal | `paypal` | Yes | Yes | No |
| PayPay | `paypay` | Yes | No | No |
| Revolut Pay | `revolut_pay` | Yes | Yes | No |
| Samsung Pay | (no enum) | N/A | No | Yes only |
| Satispay | `satispay` | Yes | No | No |
| Stablecoins/crypto | `crypto` | Yes | Invite only | No |
| Vipps | `vipps` | Yes | No | No |
| WeChat Pay | `wechat_pay` | No | No | No |

**Waitlist**: MoMo (Vietnam), GCash (Philippines).

## Key Constraints

**Samsung Pay**: Terminal only — no online product support at all.

**Apple Pay / Google Pay**: No explicit API enum (routed via card). Not displayed for Indian IP addresses. Terminal supported.

**Link**: Payment Element doesn't support Link in Brazil or India.

**PayPay Connect**: requires invite.

**Stablecoins/crypto**: SetupIntents invite-only; no manual capture.

## Subscription Caveats

Many wallets have limited recurring support. Before committing to wallet-based subscriptions, verify:

- Token or billing agreement creation for future charges
- Merchant-initiated recurring transactions (MIT) support
- Updating and continuity when the underlying card changes
- Retry and dunning behavior

Wallets with full subscription support: Amazon Pay, Apple Pay, Cash App Pay, Google Pay, Link, PayPal, Revolut Pay.

## Google Pay Details

**Worldwide except India**. All supported presentment currencies. Same pricing as card.

**Three integration paths**: Android (`GooglePayLauncher`), React Native (`PlatformPayButton`), Web (Checkout auto; Elements via Express Checkout Element).

**Android**: add `com.google.android.gms.wallet.api.enabled` to AndroidManifest.xml. Request production access from Google Pay & Wallet Console.

**Web domain registration**: same as Apple Pay — all domains including `www`. Direct charges Connect: per-connected-account.

**Liability shift — three token types**:

1. **DPAN** (Android device card): liability shift by default
2. **FPAN** (Chrome/Google property card): 3D Secure required for global Visa liability shift; customize via Radar rules
3. **E-commerce tokens**: **no liability shift, no 3D Secure**

**Visa liability shift for non-Stripe-hosted**: enable "Fraud Liability Protection for Visa Device Tokens" in Google Pay & Wallet Console.

**Sigma**: `card_token_type` → `fpan` or `dpan_or_ecommerce_token`.

**Test**: physical Android device required; real card in Google Wallet first.

## Amazon Pay Details

**Worldwide customers**. 12 currencies (USD, AUD, GBP, DKK, EUR, HKD, JPY, NZD, NOK, ZAR, SEK, CHF). 17 merchant countries (US + 16 European).

**Disputes**: **240-day** customer window — longest of any payment method reviewed. 10-day evidence submission, 90-day Amazon decision. A-to-z Guarantee claims (`dispute_type = claim`) don't incur dispute fees.

**Manual capture**: Yes — unique among reviewed wallets.

**Refunds**: 90-day, async. Non-card method refunds can take up to 14 calendar days.

**Recurring**: Yes — full subscriptions, no invite required.

**Alternative payment methods in Amazon Pay**: US (Amazon Store Card, Affirm, Citi Flex Pay, installments, Shop with Points); EU (SEPA Direct Debit).

**Integration**: Checkout, Elements, Direct API, iOS, Android. **10-minute authorization window** (Elements/Direct API). **Separate auth + capture**: `capture_method: 'manual'`, 7-day window. Direct API: `confirmPayment` with `payment_method_data: { type: 'amazon_pay' }` + `return_url`.

**Save/recurring**: Checkout (setup mode) or Direct API via `stripe.confirmAmazonPaySetup()` (SetupIntent) or PaymentIntent + `setup_future_usage: off_session`. Authorization text required before first save. `next_action.type: 'redirect_to_url'`. iOS: `STPPaymentHandler.confirmSetupIntent()`. Android: `PaymentLauncher.confirm()`.

## Apple Pay Details

**Worldwide except India**. All supported presentment currencies. Same pricing as card — no extra fees.

**Setup**: Apple Developer enrollment → Apple Merchant ID → Stripe Dashboard CSR (must use Stripe-provided CSR, not self-generated) → Apple Pay certificate → Xcode capability.

**Web domain registration**: all domains showing Apple Pay button must be registered (including `www` subdomains). Direct charges via Connect require per-connected-account registration.

**iOS 16+**: merchant tokens (`PKPaymentRequest.recurringPaymentRequest`) enable MIT/recurring. Order tracking via `applePayContext(willCompleteWithResult:)`.

**App Clips**: `StripeApplePay` module is lightweight and App Clip-optimized.

**In-app purchase**: physical goods direct; digital goods (US/EEA only) redirect to Checkout/Elements/Payment Links.

**Test limitation**: real card + test API keys required — cannot save test cards to Apple Pay wallet.

**Web Checkout `embedded_page`**: Safari 17+ / iOS 17+ only.

**Certificate renewal**: valid 25 months. Notifications at 30/15/7 days before expiry. Always use new Stripe CSR (never reuse). Upload to Stripe before activating on Apple Developer account. Keep both old and new certificates in Stripe Dashboard during transition (~5 min switch). No app update needed.

**Conversion best practices**: add button to product pages/search results (Indiegogo +250%); default to Apple Pay for capable devices (Wish 2×); skip mandatory sign-up; collect account info post-payment.

**Cartes Bancaires via Apple Pay**: EUR only. iOS: `StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]` (one line). Web: automatic via Payment Element, Express Checkout Element, Checkout, Payment Request Button. Connect: verify `on_behalf_of` account supports Cartes Bancaires.

**Apple Pay recurring — DPAN vs MPAN**: DPAN is device-tied (deactivates on device switch); MPAN (merchant token) persists across devices. Each generates a one-time expiring cryptogram — **must consume via CIT (SetupIntent 0 USD validation) immediately**; if CIT fails, all subsequent MITs also fail. Apple Pay terms **forbid** using saved payment method for on_session payments. Tokens API deprecated for recurring — use PaymentIntents/SetupIntents.

**MPAN request types** (iOS 16+): `recurringPaymentRequest` (subscriptions), `automaticReloadPaymentRequest` (store card top-ups), `deferredPaymentRequest` (hotels/reservations, iOS 16.4+). Pass as `applePay` param to Express Checkout Element or Payment Element. Checkout auto-handles. Fallback to DPAN if issuer doesn't support MPAN. Sigma `charges.card_token_type = 'mpan'` for auth rate monitoring.

**Liability shift**: globally supported for all major networks. **Visa exception**: iOS 16.2+ required globally; below 16.2 only gets liability shift if card issued in Europe. Disputes/refunds same process as card payments.

## Cash App Pay Details

**US only** (excluding territories), USD only. US merchants only.

**Two flows**: mobile redirect (auto-authenticated in Cash App app) or desktop QR code scan.

**Payment limits**: customer-level variable limits; recommend below $2,000. No split balance+debit for same order.

**Manual capture**: Yes (one of few wallets supporting this).

**Refunds**: 90-day, async. To original form of payment (balance or debit).

**Dispute liability (critical)**:

- **On-session**: Cash App bears fraud liability
- **Off-session (saved PM)**: **merchant bears fraud liability**
- 120-day window, 13-day evidence, 58-day decision

**Statement descriptor**: `CashApp*` prefix + company name. Dynamic descriptor: Cash App app only (not external statements).

**Prohibited**: B2B, financial services, gift cards, fundraising/donations/alcohol.

**Connect**: `cashapp_payments` capability. PaymentMethod **cannot be cloned** across connected accounts when connected account is business of record.

**Integration**: 4 web paths + iOS/Android. Checkout supports setup + subscription modes. **60-minute authorization window** (desktop QR refreshable 20×). **Separate auth+capture**: `capture_method: 'manual'`, 7-day window. **Live mode auto-approves** after redirect — no in-app approval option (sandbox shows approve/decline test page).

**Save/recurring**: Checkout (setup mode) or Direct API via `stripe.confirmCashappSetup()` (SetupIntent). **`mobile_auth_url` expires 30 seconds** — must redirect immediately. SetupIntent: 10-min session; desktop QR refreshable 20×. Authorization text required (first save of customer's $Cashtag). Revocation: `mandate.updated` → `detachPaymentMethod`. iOS: `STPPaymentHandler.confirmSetupIntent()`. Android: `PaymentLauncher.confirm()`.

## PayPal (via Stripe) Details

**Stripe's PayPal integration** — processing through Stripe infrastructure for 30 European merchant countries. Worldwide customers. 14 currencies (EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD). Distinct from using your own PayPal account.

**Funding**: PayPal wallet, linked card/bank, or BNPL.

**Connect**: online marketplaces only (Deliveroo/ManoMano type). **NOT** for platforms onboarding other businesses. Requires manual approval. Destination + Separate charges only; Direct and `on_behalf_of` not supported.

**Recurring**: Yes — may require additional approval.

**Refunds**: **180-day** window. Funding from Stripe or PayPal balance based on settlement preference.

**Fees**: listed in Balance reports but **not** in Stripe tax invoice — access from PayPal dashboard.

**Disputes**: 180-day window (same as refund). Can be filed via PayPal or customer's bank. Evidence: 2–19 days to submit; PayPal decides within 30 days. Direct customer contact not supported via Stripe — use PayPal. Appeals not supported via Stripe — use PayPal. Multiple disputes per payment possible: category change = new Stripe dispute (same PayPal dispute). PayPal dispute fees charged by PayPal; Stripe charges none. 7 test email patterns available (`dispute_not_received`, `dispute_fraudulent`, etc.).

**PayPal Seller Protection** applies to eligible transactions.

**PayPal button** (vs redirect): Stripe decides which to show. Button blockers for ECE: billing/shipping/phone collection. Button blockers for Checkout: billing/consent/custom fields/phone/shipping-recurring/tax ID collection, or PayPal as the **only** payment method. Maximize button: set `billing_address_collection: 'auto'`, disable auto-tax, include multiple PM types.

**Activation**: EU (except Hungary), Liechtenstein, Norway, UK, Switzerland. Settlement preference chosen at activation (Stripe balance vs PayPal balance). Connect requires separate manual onboarding with PayPal rep. **Account switching disables recurring** — must re-enable and collect mandates again.

**Integration**: Checkout, Direct API, iOS, Android, React Native. **Auth windows**: settlement-to-Stripe = 10 days (Stripe auto-reauthorizes for 10 more = 20 days total); settlement-to-PayPal = 3 days (extends to 3 more; up to 10-day "honor period" via PayPal support). Direct API: `stripe.confirmPayPalPayment(clientSecret, { return_url })` → redirect → handle `payment_intent` + `payment_intent_client_secret` query params on return. Manual server-side: create+confirm with `payment_method_data: { type: 'paypal' }` + `confirm: true` → `next_action.redirect_to_url`. iOS: `STPPaymentMethodPayPalParams` + `STPPaymentHandler.confirmPayment()` (webview). Android: `PaymentLauncher.confirm()`. React Native: `stripe.confirmPayPalPayment()`.

**Preferred locale**: `payment_method_options.paypal.preferred_locale` — 21 locales (cs-CZ through sv-SE).

**Statement descriptor**: `PAYPAL *BUSINESS_NAME` set by PayPal; custom `statement_descriptor` appended, 22-char total cap.

**Payer details** in `charge.payment_method_details.paypal`: `payer_email`, `payer_name`, `payer_id`, `transaction_id`.

**Settlement to PayPal balance**: Stripe balance transaction amount = 0; funds go to PayPal balance. Fees still recorded. Gross/Net volume charts do not reflect PayPal sales — use Payment methods report. Must maintain positive balance in both accounts for refunds/disputes. Manual reconciliation required (two methods below). Connect users always settle on Stripe (no choice). Changing settlement requires Stripe support ticket.

**Reconciliation (PayPal settlement only)**: Two methods — (1) `payment_method_options.paypal.reference` (recommended): merchant order ID appears as Invoice ID in PayPal settlement report, cascades to refunds/disputes; (2) `charge.payment_method_details.paypal.transaction_id` (fallback, only after capture): appears as Transaction ID in settlement report. PayPal Settlement Report: 24-hour view, accessible via paypal.com or sFTP.

**Async payment methods**: synchronous only by default; enable by contacting Stripe support.

**Recurring enablement**: auto-enabled at PayPal activation for most users. Manual path: Dashboard → Payment methods → PayPal → Enable (Recurring payments section); takes up to 5 business days; enabled by default in test.

**Save/recurring (Checkout)**: `mode: 'setup'` → `checkout.session.completed` webhook → extract `setup_intent` → retrieve SetupIntent → get `payment_method` ID.

**Save/recurring (Direct API)**: `stripe.confirmPayPalSetup(clientSecret, { return_url, mandate_data })` → billing agreement approval → `setup_intent.succeeded`. Mandate fields: `payer_email`, `payer_id`, `billing_agreement_id` (BAID). Off-session: PaymentIntent with `off_session: true` + `confirm: true`. On-session with saved PM: `confirmPayPalPayment()` — `return_url` not required when PM was set up via SetupIntent or `setup_future_usage`.

**Fraudnet/Magnes risk libraries**: required for server-side on-session payments with saved PM. Pass `payment_method_options.paypal.risk_correlation_id`; missing → `paypal_risk_correlation_id_missing`. Stripe.js handles Fraudnet automatically.

**Mandate cancellation**: customer cancels PayPal billing agreement → `mandate.updated` webhook; all subsequent PIs with that PM fail. Detach: `paymentMethods.detach()` cancels billing agreement on PayPal side.

**Import existing billing agreements**: SetupIntent with `payment_method_options.paypal.billing_agreement_id` (existing BAID) + `confirm: true` + `usage: 'off_session'` + `mandate_data.customer_acceptance.type: 'offline'`. No customer redirect needed. Caveat: PayPal only sends cancellation webhooks for agreements **created through Stripe** — imported BAIDs don't get cancellation webhooks.

**Accounts v2**: use `customer_account` instead of `customer` on SetupIntent (public preview for non-Connect users).

## Link Details

**Stripe's payment network** — saves and autofills payment details; also surfaces alternative LPMs (Instant Bank Payments, Klarna, Pix, UPI, Stablecoins) for US merchants with zero integration. Worldwide except India; Payment Element not supported in Thailand or Brazil.

See [[stripe-link]] for full coverage (two integration paths, eligibility criteria, customer flow, Authentication Element).

## MobilePay Details

**Denmark and Finland** card wallet. DKK, EUR, NOK, SEK. 30 European merchant countries. Underlying Visa/Mastercard transaction processed invisibly. Mobile redirect or desktop phone+push flows.

**Manual capture**: Yes. **Disputes**: Yes (same as cards). Full and partial refunds.

**Card retries**: customer can retry with different card in-app.

**3D Secure**: 1–7% of transactions (Finland Mastercard highest at ~7%). Handled invisibly — **liability shift only if 3DS occurred; merchant cannot enforce 3DS**.

**Dankort not supported** — processed on Visa/Mastercard instead.

**Fees**: Stripe fees + MobilePay per-transaction fee (billed daily) + **35 DKK/month** membership fee (Denmark-only). Listed as separate entry on monthly tax invoice.

**Prohibited categories** (8): cryptocurrencies, stock trade, gambling, betting, bonds, money transfers, debt collection, MLM/pyramid schemes.

**Branding**: merchant icon in MobilePay app from Branding settings (250×250px).

**Integration**: Checkout, Elements, Direct API, iOS, Android. **5-minute authorization window** across all paths. Manual capture (full amount only). Direct API: `next_action.redirect_to_url`. Cancellation supported. iOS: `STPPaymentMethodMobilePayParams` + custom URL scheme. Refunds/disputes subject to Visa/Mastercard rules.

## MB WAY Details

**Portugal customers only**, EUR only. Phone number-based (push notification → app authorization). Immediate confirmation.

**Transaction limits**: €0.50 – €5,000. Daily default: €1,000 (customer can adjust to €10,000).

**40 merchant countries** — broad for Portugal-only wallet (includes MX, HK, JP, NZ, US).

**Disputes**: Yes — 7-day evidence submission. Stripe holds amount until resolution.

**Refunds**: 365-day. Minutes. Full and partial. Multiple partials allowed.

**Statement descriptor**: ignored — `Stripe Inc` shown on bank statements.

**No recurring, no manual capture, no Mobile Payment Element.**

**Checkout restrictions**: no subscription mode, no setup mode, no `setup_future_usage`.

**Connect**: all charge types. Capability: `mb_way_payments`.

**Integration**: Checkout, Elements (**beta** — requires `betas: 'mb_way_pm_beta_1'`), Direct API. Direct API: `stripe.confirmMbWayPayment()` with phone number in billing details. Stripe.js auto-polls; `handleActions: false` to poll manually. Test phones: `+351911111112` (30-sec succeed), `+351911111113–116` (various errors), any other (immediate succeed).

## GrabPay Details

**Singapore and Malaysia only** (SG/MY merchants and customers). SGD and MYR. Digital wallet with stored balance. OTP redirect authentication.

**No recurring. No manual capture. No disputes** (OTP prevents chargebacks).

**Refunds**: 90-day, async (up to 5 min).

**Branding guidelines**: mandatory — GrabPay provides PDF brand guidelines and logos/buttons zip. Must follow for checkout UI.

**2 merchant countries** (narrowest wallet coverage reviewed).

**Integration**: Checkout, iOS, Android, React Native, Direct API. **No minimum charge amount** (can be as low as 1 SGD/MYR). Subscriptions explicitly not supported. Android: `name` required in billing details. Direct API: `stripe.confirmGrabPayPayment()`. Custom URL scheme required for iOS/React Native.

## Revolut Pay Details

**UK and EU** — 30 merchant countries. Currencies: EUR, GBP, RON, HUF, PLN, DKK (GBP default for UK, EUR default for EU). Non-Revolut customers can save details after first purchase.

**Full feature set**: recurring ✓, Connect ✓, disputes ✓, manual capture ✓.

**Product support**: Connect, Checkout, Payment Links, Elements, Subscriptions, Invoicing.

**Refunds**: full + partial, 180-day window, async up to 5 minutes.

**Disputes**: 120-day customer window. Evidence submission: 14 days. Revolut decision: within 35 days. Revolut Buyer Protection Policy applies.

**Integration**: Checkout, Elements, Direct API, iOS, Android, React Native. Reusable PM (supports subscriptions). Two auth flows: mobile redirect (1-hour expiry) and desktop QR code (refreshable 20×, 1-hour expiry). Manual capture: 7-day window. Live mode auto-approves after redirect/scan. Failed payments detach PM → `requires_payment_method`.

**Save/recurring**: On-session payments always redirect to Revolut app even with saved PM. Authorization text required before first save. Two save paths: (1) SetupIntent + `stripe.confirmRevolutPaySetup()` with `mandate_data`; (2) PaymentIntent + `setup_future_usage: 'off_session'`. Detach triggers `mandate.updated` + `payment_method.detached`. Accounts v2 supported (`customer_account`).

## PayPay Details

**Japan only** — JP merchants and customers, JPY only. Popular digital wallet in Japan.

**No recurring. No Connect support. No dispute support. No manual capture.**

**Refunds**: full and partial, 365-day window, instant.

**Charge limits**: min 50 JPY, max 1,000,000 JPY.

**Product support**: Payment Links, Checkout (not subscription/setup mode), Elements (not Express Checkout Element).

**Prohibited**: cryptocurrency exchanges/wallets + additional categories at PayPay discretion.

**Connect**: requires invite.

**Integration**: Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, Android. Payment mode only (no setup/subscription). Redirect-based — `return_url` required. Testing: sandbox shows approve/decline page; live mode redirects directly to PayPay with no approve/decline. 5 error codes documented.

## Alipay Details

**CNY default** (always shown to customer) + 10 settlement currencies by merchant country (AUD, CAD, EUR, GBP, HKD, JPY, MYR, NZD, SGD, USD). 39 merchant countries.

**Refunds**: 90-day, async, up to 5 minutes. No disputes.

**Recurring**: invite-only (subscriptions and invoicing).

**Connect**: Destination + Separate charges supported; Direct charges and `on_behalf_of` private preview. Capability: `alipay_payments`.

**Dual prohibited list**: Stripe's standard + Alipay's own list (stripe.com/legal/alipay).

**Integration**: Checkout, iOS, Android, React Native, Direct API. All redirect to Alipay for auth. iOS/React Native: custom URL scheme + `safepay/` host required. Android: Alipay SDK (app-to-app) or WebView fallback; **Alipay Android SDK cannot test in sandbox — live mode only**. Direct API: `stripe.confirmAlipayPayment()`.

## Satispay Details

**Italy customers only**, EUR only. Stored-value wallet. Redirect to Satispay website for auth. Immediate confirmation.

**20 eurozone merchant countries** (AT, BE, CY, DE, EE, ES, FI, FR, GR, HR, IE, IT, LT, LU, LV, MT, NL, PT, SI, SK).

**Manual capture**: Yes. **Disputes**: Yes — 12 calendar days to submit evidence. **Refunds**: full + partial, 180-day window, async up to 5 minutes.

**No recurring payments.**

**Product support**: Connect, Payment Links, Checkout, Elements (not Express Checkout Element), Subscriptions.

**Connect**: `satispay_payments` capability. Standard charge type descriptor rules apply (`on_behalf_of` → connected account).

**14 prohibited categories**: automobile associations, gambling/betting, counseling, credit reporting, detective agencies, direct marketing (catalog + telemarketing), door-to-door sales, employment/temp agencies, financial institutions, cryptocurrency exchanges/wallets, pawn shops, security brokers/dealers, plus additional at Satispay's discretion.

**Integration**: Checkout, Checkout Sessions API, Payment Intents API, Direct API, iOS, Android. Payment mode only (no setup/subscription). Redirect-based — `return_url` required. Direct API: `stripe.confirmSatispayPayment()`. iOS: `STPPaymentMethodSatispayParams` + `STPPaymentHandler.confirmPayment()`. Android: `PaymentMethodCreateParams.createSatispay()` + `PaymentLauncher.confirm()`. **Separate auth+capture**: `capture_method: 'manual'`, 7-day window. Accounts v2 supported (`customer_account`). Sandbox: approve/decline test page; live mode redirects directly. 5 error codes documented.

## Vipps Details

**Norway customers only**, NOK only. Card wallet — **private preview** (requires `vipps_preview=v1` header on all API requests). Phone number entry → push notification → Vipps app authorization.

**Underlying mechanism**: Stripe receives card data from Vipps and processes as a Visa/Mastercard card transaction. Processing is invisible to the merchant integration.

**29 European business countries** (AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK).

**Manual capture**: Yes. **Disputes**: Yes — same process as card payments. **Refunds**: full + partial, multiple partials allowed.

**No recurring payments.**

**Product support**: Connect (all 3 charge types — Direct, Destination, Separate), Checkout (not subscription/setup mode), Payment Links (API-created only), Elements (not Express Checkout Element).

**Connect**: `vipps_payments` capability. Connected account name shown in Vipps app during checkout.

**BankAxept not supported** — BankAxept-branded cards processed on Visa/Mastercard instead.

**Fee structure**: Stripe card processing fees + applicable taxes (deducted from transaction, same as standard card) + **Vipps per-transaction fee** (billed daily, not deducted from individual transaction — deducted from Stripe balance once per day).

**8 prohibited categories**: cryptocurrencies (restricted), stock trade, gambling, betting, bonds, money transfers, debt collection, MLM/pyramid schemes.

**Integration**: Checkout (Stripe-hosted + embedded), Elements (Payment Element), Direct API. Payment mode only (no setup/subscription). Requires `vipps_preview=v1` header; Elements also requires `betas: 'vipps_pm_beta_1'`. Two auth flows: mobile redirect (directly to Vipps app) and desktop (phone number → push notification). **5-minute authentication window** — PM detaches on expiry. **Separate auth+capture**: `capture_method: 'manual'`, 7-day hold, **full amount only** (no partial capture). Failed card → customer can retry with different card in Vipps app. Refunds/disputes subject to Visa/Mastercard network rules.

## WeChat Pay Details

**Chinese consumers, overseas Chinese, and Chinese travelers**. Part of WeChat super app (1B+ MAU); WeChat Pay has 800M+ users. Top verticals: gaming, e-commerce, travel, online education, food, nutrition.

**13 presentment currencies**: CNY (default, always shown to customer) + AUD, CAD, EUR, GBP, HKD, JPY, SGD, USD, DKK, NOK, SEK, CHF — mapped by merchant country.

**22 merchant countries** (AT, AU, BE, CA, CH, DE, DK, ES, FI, FR, GB, HK, IE, IT, JP, LU, NL, NO, PT, SE, SG, US).

**No recurring. No manual capture. No disputes** — customer authenticates in WeChat app, low fraud risk, no chargeback process.

**Refunds**: full + partial, 180-day window, async. Failed refunds return to Stripe balance.

**Product support**: Connect (partial), Checkout (not subscription/setup mode), Payment Links, Elements (not Express Checkout/Mobile Payment Element), Invoicing (`send_invoice` only), Terminal (not Japan).

**Connect**: **partial** — Destination + Separate charges GA; Direct + `on_behalf_of` private preview. Capability: `wechat_pay_payments` (private preview for non-Dashboard accounts).

**Integration** (Checkout + Direct API, web only):

- **Checkout**: add `wechat_pay` to `payment_method_types`, set `payment_method_options.wechat_pay.client = 'web'`, all line items same currency. Supports 37 business locations (more than overview's 22 — adds BG, CY, CZ, EE, GR, HU, LV, LT, MT, PL, RO, SK, SI).
- **Direct API**: `stripe.confirmWechatPayPayment()` → QR from `next_action.wechat_pay_display_qr_code.image_data_url` (or `.data`); stay on QR page until webhook confirms. Web only.
- **Fulfillment**: `payment_intent.succeeded` / `payment_intent.payment_failed` webhooks.

## Sources

- [[source-stripe-wallets]] — hub page: 17 wallets, product/API matrices, subscription caveats, MoMo/GCash waitlist
- [[source-stripe-apple-pay]] — Apple Pay: iOS/RN/Web, Stripe CSR required, domain registration, merchant tokens (iOS 16+), real card test
- [[source-stripe-pmd-registration]] — Domain registration guide: 6 PMs requiring it (Apple Pay required, + Amazon Pay/Google Pay/Klarna/Link/PayPal), PaymentMethodDomain API, iframe origin rules, Connect charge-type routing
- [[source-stripe-apple-pay-best-practices]] — Apple Pay best practices: certificate renewal (25 mo, new CSR, dual certs in transition), express checkout, default to Apple Pay
- [[source-stripe-apple-pay-cartes-bancaires]] — Cartes Bancaires + Apple Pay: EUR only, iOS one-line config, web automatic, Connect on_behalf_of caveat
- [[source-stripe-apple-pay-recurring]] — Apple Pay recurring: DPAN/MPAN cryptogram expiry, consume via SetupIntent CIT immediately, on_session forbidden, Tokens deprecated
- [[source-stripe-apple-pay-merchant-tokens]] — Apple Pay MPAN types: recurring/auto-reload/deferred, Express Checkout Element config, Sigma card_token_type monitoring
- [[source-stripe-apple-pay-disputes-refunds]] — Apple Pay disputes/refunds: liability shift (Visa iOS 16.2+ global, Europe below 16.2), same as card disputes
- [[source-stripe-cash-app-pay]] — Cash App Pay: US-only, off-session merchant bears liability, no PM cloning across Connect, 90-day refunds
- [[source-stripe-cash-app-pay-accept-payment]] — Cash App Pay integration: 4 paths + mobile, 60-min auth, 20× QR refresh, manual capture, live auto-approves
- [[source-stripe-cash-app-pay-set-up-payment]] — Cash App Pay save/recurring: confirmCashappSetup(), mobile_auth_url 30-sec expiry, authorization text, revocation
- [[source-stripe-google-pay]] — Google Pay: Android/RN/Web, DPAN/FPAN/e-commerce token liability shift, domain registration, Sigma card_token_type
- [[source-stripe-grabpay]] — GrabPay: SG/MY only, OTP redirect, no disputes/recurring/manual capture, mandatory branding guidelines
- [[source-stripe-grabpay-accept-payment]] — GrabPay integration: 4 paths + mobile, no minimum charge, confirmGrabPayPayment(), Android needs billing name
- [[source-stripe-link]] — Link: two PM type paths (link vs card+wallet), Instant Bank Payments exclusive, Thailand/Brazil Payment Element caveat
- [[source-stripe-link-payment-methods]] — Link payment methods (US-only): Instant Bank Payments/Klarna/Pix/UPI/Stablecoins, zero integration, 5 eligibility criteria, customer flow, disabling rules
- [[source-stripe-mb-way]] — MB WAY: Portugal phone-number wallet, 365-day refunds, 7-day dispute evidence, €1k daily limit, Stripe Inc descriptor
- [[source-stripe-mb-way-accept-payment]] — MB WAY integration: Checkout + Elements (beta betas flag) + Direct API (confirmMbWayPayment), 5 test phone numbers
- [[source-stripe-mobilepay]] — MobilePay: DK/FI card wallet, 3DS 1–7% invisible, Dankort→Visa/MC, 35 DKK/month Denmark fee, liability shift only with 3DS
- [[source-stripe-mobilepay-accept-payment]] — MobilePay integration: 4 paths + mobile, 5-min auth window, manual capture full only, redirect_to_url
- [[source-stripe-paypal]] — PayPal via Stripe: EU merchants, 14 currencies, marketplace Connect only, 180-day refunds, fees not in Stripe tax invoice
- [[source-stripe-paypal-button]] — PayPal button: Stripe decides button vs redirect, blockers list for ECE + Checkout, maximize by disabling billing/tax collection
- [[source-stripe-paypal-activate]] — PayPal activation: EU (except Hungary), settlement preference, Connect manual onboarding, account switch disables recurring
- [[source-stripe-paypal-accept-payment]] — PayPal accept-a-payment: 5 paths (Checkout/Direct API/iOS/Android/RN), auth windows by settlement preference, preferred locale, statement descriptor format, payer details fields
- [[source-stripe-paypal-set-up-future-payments]] — PayPal save/recurring: enablement flow, Checkout setup mode, confirmPayPalSetup(), Fraudnet risk_correlation_id, mandate BAID, on-session return_url rules
- [[source-stripe-paypal-settlement]] — PayPal settlement preference: Stripe vs PayPal balance, Dashboard reporting differences, reconciliation, changing requires support ticket
- [[source-stripe-paypal-disputes]] — PayPal disputes: 180-day window, 2–19 day evidence, 30-day decision, no Stripe appeals, multiple disputes per payment, 7 test patterns
- [[source-stripe-paypal-reconciliation]] — PayPal reconciliation: reference field (Invoice ID) vs transaction_id (Transaction ID), PayPal settlement report access
- [[source-stripe-paypal-import]] — PayPal billing agreement import: billing_agreement_id on SetupIntent, offline mandate, no cancellation webhooks for imported BAIDs
- [[source-stripe-amazon-pay]] — Amazon Pay: worldwide, 12 currencies, 240-day disputes, manual capture, SEPA+installments via Amazon
- [[source-stripe-amazon-pay-accept-payment]] — Amazon Pay integration: 5 paths, 10-min auth window, 7-day manual capture, confirmPayment()
- [[source-stripe-amazon-pay-set-up-future-payments]] — Amazon Pay save/recurring: confirmAmazonPaySetup(), redirect_to_url, authorization text required, iOS/Android
- [[source-stripe-alipay]] — Alipay: CNY+10 currencies, 39 countries, 90-day refunds, recurring invite-only, Connect partial
- [[source-stripe-alipay-accept-payment]] — Alipay integration: 5 paths, safepay/ URL scheme, Android SDK live-mode only, confirmAlipayPayment()
- [[source-stripe-revolut-pay]] — Revolut Pay: UK/EU, 6 currencies, full feature set (recurring/Connect/disputes/manual capture), 120-day disputes, 35-day Revolut decision
- [[source-stripe-revolut-pay-accept-payment]] — Revolut Pay integration: 6 platforms, mobile redirect + desktop QR (20× refresh), 7-day manual capture, live mode auto-approves
- [[source-stripe-revolut-pay-set-up-future-payments]] — Revolut Pay save/recurring: on-session always redirects, confirmRevolutPaySetup(), authorization text required, detach triggers mandate.updated
- [[source-stripe-paypay]] — PayPay: Japan/JPY only, no recurring/Connect/disputes, 365-day instant refunds, 50–1M JPY limits
- [[source-stripe-paypay-accept-payment]] — PayPay integration: 6 platforms, payment mode only, redirect-based, live mode no approve/decline, 5 error codes
- [[source-stripe-satispay]] — Satispay: Italy/EUR only, 20 eurozone merchant countries, 12-day dispute evidence, 180-day refunds, 14 prohibited categories
- [[source-stripe-satispay-accept-payment]] — Satispay integration: 4 web paths + iOS/Android, payment mode only, manual capture 7-day, confirmSatispayPayment(), 5 error codes
- [[source-stripe-vipps]] — Vipps: Norway/NOK card wallet, private preview, card transaction underneath, daily Vipps fee billing, BankAxept→Visa/MC
- [[source-stripe-vipps-accept-payment]] — Vipps integration: 3 paths (Checkout/Elements/Direct API), 5-min auth window, full-amount-only capture, card retry in app
- [[source-stripe-wechat-pay]] — WeChat Pay: 800M+ users, CNY+12 currencies, 22 merchant countries, no disputes/recurring/manual capture, partial Connect
- [[source-stripe-wechat-pay-accept-payment]] — WeChat Pay integration: Checkout + Direct API (web only), confirmWechatPayPayment(), QR from next_action, 37 business locations
