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
| Alipay | `alipay` | Yes (2026-05-07 acceptance guide) | No | No |
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
| Samsung Pay | `samsung_pay` in November matrix | Yes (November PaymentIntent row) | No | Supported in November matrix; Checkout payment mode also listed |
| Satispay | `satispay` | Yes | Yes (November 2026 method guide) | No |
| Stablecoins/crypto | `crypto` | Yes | Invite only | No |
| Vipps | `vipps` | Yes | No | No |
| WeChat Pay | `wechat_pay` | May cross-method matrix No, November Yes. See [[source-stripe-wechat-pay]] for QR and native flow scope. | General overview Unsupported. November cross-method matrix Private preview. | Supported outside Japan in the method overviews. |

**Waitlist**: The November 2026 Wallets hub links an email preview request for MoMo and GCash for one-time and recurring payment interest in Vietnam and the Philippines. The request does not establish approval.

## Key Constraints

**Samsung Pay**: May's Wallets hub lists Terminal only. November retains Terminal and lists Checkout excluding setup and subscription modes, plus `samsung_pay` with PaymentIntents and redirect. See [[source-stripe-wallets#Wallet matrix changes]] for the South Korea selector and versioned no-saving qualification.

**Apple Pay / Google Pay**: No separate wallet API enum in the hub. The May table marks both as not displayed for Indian IP addresses. November limits its footnote to Google Pay on India-based Stripe accounts and removes Apple's marker. Both tables list Terminal.

**Link**: The dedicated May and November Link wallet overviews exclude India from general account and customer reach and specify Thailand and Brazil for the Payment Element restriction. The November Wallets hub footnote separately says Brazil or India. See [[stripe-link#Core Properties]] for the dedicated account-geography qualification.

**PayPay Connect**: The May and November method profiles exclude Connect. The May wallets table and the November wallets and payment-method support tables list Connect with a request-an-invite condition. See [[source-stripe-paypay]] for the dated disagreement.

**Stablecoins and crypto**: The November Wallets hub lists Subscriptions, SetupIntents and future-use access as invite only, Customer Portal supported and manual capture unsupported. In the same-date cross-method reference, the dedicated stablecoin product table marks Subscriptions and Customer Portal private preview and Invoicing supported with a `send_invoice` subscription footnote. Its dedicated API row marks SetupIntents and future use private preview and manual capture supported. The cross-method wallet rows use the same labels as the Wallets hub. The method guide marks manual capture unsupported and describes Billing for invoices and subscriptions. See all three scopes in [[source-stripe-wallets#Stablecoin capability references]].

## Subscription Caveats

Many wallets have limited recurring support. Before committing to wallet-based subscriptions, verify:

- Token or billing agreement creation for future charges
- Merchant-initiated recurring transactions (MIT) support
- Updating and continuity when the underlying card changes
- Retry and dunning behavior

Wallets with full subscription support: Amazon Pay, Apple Pay, Cash App Pay, Google Pay, Link, PayPal, Revolut Pay.

## Google Pay Details (2026-05-07 combined guide)

**Worldwide except India**. All supported presentment currencies. Same pricing as card.

**Three integration paths**: Android (`GooglePayLauncher`), React Native (`PlatformPayButton`), Web (Checkout auto; Elements via Express Checkout Element).

**Android**: add `com.google.android.gms.wallet.api.enabled` to AndroidManifest.xml. Request production access from Google Pay & Wallet Console.

**Web domain registration**: same as Apple Pay — all domains including `www`. Direct charges Connect: per-connected-account.

**Liability shift — three token types (2026-05-07 Google Pay capture)**:

1. **DPAN** (Android device card): described as supporting liability shift by default
2. **FPAN** (Chrome/Google property card): described as supporting global liability shift, including Visa, when 3D Secure is used; Radar rules can request 3D Secure
3. **E-commerce tokens**: described as having neither liability shift nor 3D Secure support **at that time**

The 2026-11-07 base-URL capture is a platform index only; current token-specific liability and 3D Secure support were not verified there. These dated descriptions do not guarantee a charge's liability outcome.

**Visa liability shift for non-Stripe-hosted**: enable "Fraud Liability Protection for Visa Device Tokens" in Google Pay & Wallet Console.

**Sigma**: `card_token_type` → `fpan` or `dpan_or_ecommerce_token`.

**Test**: physical Android device required; real card in Google Wallet first.

## Amazon Pay Details

**Worldwide customers**. The November 2026 overview lists 17 Stripe-account locations (US and 16 European) and 12 presentment currencies; its account table limits **US accounts to USD**, while the sixteen European locations have all twelve listed currencies. MCC 6051 (cryptocurrency exchanges and wallets) is prohibited. The May overview's US-exception prose conflicts with its all-currency table; November gives an explicit USD-only US row. Listed scope does not prove an individual account's enablement.

**Disputes**: The November 2026 overview gives customers 240 days from purchase for general Amazon Pay disputes, but 90 days for A-to-z Guarantee claims. Chargeback evidence is typically due within 10 calendar days; claim evidence within 6. Use the Dashboard or Dispute `evidence_details.due_by` for the actual deadline. Amazon Pay decides within 90 days after evidence submission; a claim has `payment_method_details.amazon_pay.dispute_type = claim` and no dispute fee. The May overview gave a generic 10-day evidence window.

**Manual capture**: Yes — unique among reviewed wallets.

**Refunds**: 90-day, async. Non-card method refunds can take up to 14 calendar days.

**Recurring**: November 2026 overview marks recurring, Billing, Invoicing, PaymentIntents with `setup_future_usage`, SetupIntents and off-session payments supported. It does not establish invite-free access for every account, an identical flow on every UI or a successful future charge.

**Alternative payment methods in Amazon Pay**: US (Amazon Store Card, Affirm, Citi Flex Pay, installments, Shop with Points); EU (SEPA Direct Debit).

**Integration**: Checkout, Elements, Direct API, iOS, Android. **Authorization timing**: the November overview says Amazon controls its hosted checkout step and Stripe sets no authorization-session timeout there; consult the separately dated accept-payment guide for path-specific PaymentIntent timing. **Separate auth + capture**: `capture_method: 'manual'`, 7-day window. Direct API: `confirmPayment` with `payment_method_data: { type: 'amazon_pay' }` + `return_url`.

**Save/recurring**: Checkout (setup mode) or Direct API via `stripe.confirmAmazonPaySetup()` (SetupIntent) or PaymentIntent + `setup_future_usage: off_session`. Authorization text required before first save. `next_action.type: 'redirect_to_url'`. iOS: `STPPaymentHandler.confirmSetupIntent()`. Android: `PaymentLauncher.confirm()`.

## Apple Pay Details

**Worldwide except India**. All supported presentment currencies. Same pricing as card — no extra fees.

**Setup**: Apple Developer enrollment → Apple Merchant ID → Stripe Dashboard CSR (must use Stripe-provided CSR, not self-generated) → Apple Pay certificate → Xcode capability.

**Web domain registration**: all domains showing Apple Pay button must be registered (including `www` subdomains). Direct charges via Connect require per-connected-account registration.

**Apple Pay merchant tokens**: `PKPaymentRequest.recurringPaymentRequest` supports the recurring path under the dated version conditions summarized below from [[source-stripe-apple-pay-merchant-tokens]]. Order tracking via `applePayContext(willCompleteWithResult:)`.

**App Clips**: `StripeApplePay` module is lightweight and App Clip-optimized.

**In-app purchase**: physical goods direct; digital goods (US/EEA only) redirect to Checkout/Elements/Payment Links.

**Test limitation**: real card + test API keys required — cannot save test cards to Apple Pay wallet.

**Web Checkout `embedded_page`**: Safari 17+ / iOS 17+ only.

**Certificate renewal**: valid 25 months. Notifications at 30/15/7 days before expiry. Always use new Stripe CSR (never reuse). Upload to Stripe before activating on Apple Developer account. Keep both old and new certificates in Stripe Dashboard during transition (~5 min switch). No app update needed.

**Conversion best practices**: add button to product pages/search results (Indiegogo reported a 250% conversion-rate increase after express checkout); default to Apple Pay for capable devices (Wish reported a “2X higher conversion rate increase” in its A/B test of new Apple Pay-ready users, not a doubled overall conversion rate); skip mandatory sign-up; collect account info post-payment.

**Cartes Bancaires via Apple Pay**: EUR only. iOS: `StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]` (one line). Web: automatic via Payment Element, Express Checkout Element, Checkout, Payment Request Button. Connect: verify `on_behalf_of` account supports Cartes Bancaires.

**React Native network restriction**: `@stripe/stripe-react-native@0.74.0` adds `applePay.supportedNetworks` on iOS. Unlike `additionalEnabledNetworks`, it restricts the Apple Pay sheet to the supplied `PKPaymentNetwork` raw values and overrides the default and additionally enabled network set for that payment request.

**Apple Pay recurring — DPAN vs MPAN**: The May 7, 2026 recurring guide says a device-tied DPAN can be unintentionally deactivated when a customer switches devices and adds the same card; the November merchant-token guide says a DPAN might stop working after device replacement or card removal. An MPAN is tied to the customer, underlying card and business and is described as more reliable across device switches, without guaranteeing every saved payment succeeds. Each returned credential has an expiring one-time cryptogram; conduct the first customer-initiated transaction (CIT) promptly, before expiration, using a SetupIntent 0 USD validation or a charge. If that CIT fails, later merchant-initiated transactions (MITs) using the same Card will likely also fail. For `usage=on_session` while the customer is in the flow, Apple Pay terms forbid reusing the saved payment method: the customer must authorize the transaction and generate a new cryptogram. Stripe discourages legacy Tokens and Charges for recurring Apple Pay and recommends PaymentIntents and SetupIntents; these captures do not announce a formal deprecation. See [[source-stripe-apple-pay-recurring]] and [[source-stripe-apple-pay-merchant-tokens]].

**MPAN request types**: `recurringPaymentRequest` (subscriptions), `automaticReloadPaymentRequest` (store card top-ups), `deferredPaymentRequest` (hotels/reservations). The May 7, 2026 guide lists iOS >16.0 for recurring and reload, but >16.4 for deferred; its table is not repeated in November. For Elements with Payment Intents, pass the use-case `applePay` object to Express Checkout Element or web Payment Element. Stripe Checkout and Elements with Checkout Sessions request MPANs automatically when needed. If Apple Pay or the issuer lacks MPAN support, a DPAN is returned. Stripe stores the returned credential with the resulting `PaymentMethod` for standard saved off-session reuse. For an MPAN card update, `payment_method.automatically_updated` carries supported `data.object.card` fields (`exp_month`, `exp_year`, `last4`) for cached-value updates. Sigma `charges.card_token_type = 'mpan'` supports authorization-rate monitoring. See [[source-stripe-apple-pay-merchant-tokens]] for dated support and lifecycle details.

**Liability shift**: The dated Apple Pay disputes guide describes global support for major networks, with a **Visa exception**: iOS 16.2+ is required globally; below 16.2, Visa liability shift applies only if the card was issued in Europe. **Saved off-session exception**: The May 7, 2026 recurring guide says saved DPAN/MPAN `usage=off_session` payments outside checkout do not get network liability shift and might have lower than average authorization rates. Disputes and refunds follow the card-payment process. See [[source-stripe-apple-pay-disputes-refunds]] and [[source-stripe-apple-pay-recurring]].

## Cash App Pay Details

**US only** (excluding territories), USD only. US merchants only.

**Two flows**: mobile redirect to Cash App or desktop QR code scan for authentication. The 2026-11-07 overview gives customers 10 minutes to authenticate in the app; the 2026-05-07 acceptance guide separately describes a 60-minute authentication session and a 10-minute no-action-after-redirect `requires_action` deadline. A redirect or QR scan alone does not prove payment success.

**Payment limits**: customer-level variable limits; recommend below $2,000. No split balance+debit for same order.

**Manual capture**: Yes (one of few wallets supporting this).

**Refunds**: 90-day submission window; asynchronous, up to 10 business days in the 2026-11-07 overview, noncancelable and never reversals. Cash App returns funds to the original balance or linked source; verify Refund `status` or final refund events, since submission is not success.

**Dispute liability (critical)**:

- **On-session**: Cash App bears fraud liability
- **Off-session (saved PM)**: **merchant bears fraud liability**
- 120-day dispute window, 13-day evidence, 58-day decision; November says full and once-only disputes and nonrefundable fees. The May overview started the 120 days at expected receipt for nondelivery, whereas November says purchase date; use the case's `evidence_due_by` and verify the applicable filing deadline.

**Statement descriptor**: `CashApp*` prefix + company name. Dynamic descriptor: Cash App app only (not external statements).

**Eligibility**: The 2026-11-07 overview lists US B2C domestic USD payments, a USD 0.50 minimum, post-activation review, and Prohibited versus conditionally Restricted MCCs. The 2026-05-07 overview explicitly prohibited B2B businesses, financial services, gift-card purchases, and fundraising/donation/alcohol-focused platforms; November also marks specified financial-services MCCs Prohibited. November's restricted alcohol-related MCC rows do not alone authorize those platform models. May's US-traveler exception versus November's domestic-US matrix remains unresolved. See [[source-stripe-cash-app-pay]].

**Connect**: `cashapp_payments` capability. PaymentMethod **cannot be cloned** across connected accounts when connected account is business of record.

**Integration (dated 2026-05-07 guide):** Checkout, Elements with Checkout Sessions or Payment Intents, Direct API, iOS, Android, and React Native. Checkout compatibility text lists setup and subscription modes. The 60-minute period describes an authentication session with up to 20 desktop QR refreshes; a separate requires_action failure section says 10 minutes after redirect, an unresolved historical timing distinction. The web PaymentIntent/Direct API manual-capture sections describe a seven-day window, while the React Native test section says uncaptured test manual-capture PaymentIntents auto-expire after 60 minutes; do not treat seven days as universal. Live-mode wording says there is no in-app approve/decline control after redirect, but the guide also documents declines, timeouts, and status/event checks, so redirect does not prove payment success. The 2026-11-07 base capture is a variant index only. See [[source-stripe-cash-app-pay-accept-payment]].

**Save for later (2026-05-07 guide)**: The Checkout sample creates a Customer-linked `mode: 'setup'` Session with `payment_method_types: ['card', 'cashapp']`; the browser Direct API path uses `stripe.confirmCashappSetup()` for a SetupIntent. These are separate routes. The same guide describes a 10-minute SetupIntent authentication session, up to 20 desktop QR refreshes, and a `mobile_auth_url` that expires after 30 seconds (retrieve the SetupIntent for a new URL if missed). A custom form shows future-use authorization terms on the first save of a customer's $Cashtag. Cash App revocation sends `mandate.updated`, after which the merchant detaches the PaymentMethod; merchant-initiated detach is another route, and detach sends `payment_method.detached`. iOS uses `STPPaymentHandler.confirmSetupIntent()` and Android uses `PaymentLauncher.confirm()`. The 2026-11-07 canonical capture lists four variants but no current behavior; see [[source-stripe-cash-app-pay-set-up-payment]] for the dated setup and outcome boundaries.

## PayPal (via Stripe) Details

**Stripe's PayPal integration** — processing through Stripe infrastructure for 30 European merchant countries. Worldwide customers. 14 currencies (EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD). Distinct from using your own PayPal account.

**Funding**: PayPal wallet, linked card/bank, or BNPL.

**Connect (online marketplaces).** PayPal is unavailable to platforms that onboard businesses so those businesses can accept payments directly. Eligible marketplaces use destination charges or separate charges and transfers. Direct charges and `on_behalf_of` are excluded. The November 2026 guides describe requesting access in Payment method settings, Stripe and PayPal review that can take several weeks, Dashboard tracking and instructions to link the PayPal account after approval. Connected-account payment method configuration is unnecessary for the supported charge types. The May guide describes progress emails. See [[source-stripe-paypal]] and [[source-stripe-payment-method-connect-support]].

**Recurring**: Yes — may require additional approval.

**Refunds.** The window is 180 days from the original payment. With Stripe settlement, refunds use available Stripe funds. With PayPal settlement, refunds use the PayPal balance or another funding source available on that PayPal account. See [[source-stripe-paypal]].

**Fees**: listed in Balance reports but **not** in Stripe tax invoice — access from PayPal dashboard.

**Disputes (May and November 2026 guides)**: Customers can file on PayPal within 180 calendar days from purchase or use the original funding provider's separate route. Evidence is due in 2–19 calendar days by category. PayPal aims to decide within 30 calendar days of evidence submission. PayPal may offer direct customer contact or allow an appeal of a loss in eligible cases. Stripe keeps an appealed case open pending final PayPal resolution. A category change can reopen one PayPal case and create a new Stripe dispute. PayPal may charge a dispute fee and Stripe adds none. See [[source-stripe-paypal-disputes]] for both guides and the seven test scenarios.

**PayPal Seller Protection** applies to eligible transactions.

**PayPal button or redirect.** Stripe decides which to show. In Express Checkout Element both dated guides list phone collection and shipping collection for recurring payments as blockers. May also lists billing collection and requires `billingAddressRequired: false` for recurring payments. November omits that billing guidance. In Stripe Checkout both guides list billing or consent collection, custom fields, phone collection, recurring shipping collection, tax-ID collection and PayPal as the sole method as redirect conditions. Both checkout examples disable automatic tax and use `billing_address_collection: 'auto'`. May explicitly lists card and PayPal, and the November request omits the list. See [[source-stripe-paypal-button]] for the dated options and version-specific method selection.

**Activation**: The May and November 2026 guides cover eligible Stripe accounts in the EU except Hungary, plus Liechtenstein, Norway, the UK and Switzerland. Choose Stripe-balance or PayPal-balance settlement, then check status after returning from PayPal. Eligible Connect use has separate onboarding. Connect platforms and connected accounts cannot switch. For supported switches, the previous account continues processing until the new one is connected, and earlier payments remain eligible for refunds and disputes. Switching disables previously enabled recurring payments and requires re-enablement and new customer mandates. See [[source-stripe-paypal-activate]].

**Integration**: Checkout, Direct API, iOS, Android, React Native. **Auth windows**: settlement-to-Stripe = 10 days (Stripe auto-reauthorizes for 10 more = 20 days total); settlement-to-PayPal = 3 days (extends to 3 more; up to 10-day "honor period" via PayPal support). Direct API: `stripe.confirmPayPalPayment(clientSecret, { return_url })` → redirect → handle `payment_intent` + `payment_intent_client_secret` query params on return. Manual server-side: create+confirm with `payment_method_data: { type: 'paypal' }` + `confirm: true` → `next_action.redirect_to_url`. iOS: `STPPaymentMethodPayPalParams` + `STPPaymentHandler.confirmPayment()` (webview). Android: `PaymentLauncher.confirm()`. React Native: `stripe.confirmPayPalPayment()`.

**Preferred locale**: `payment_method_options.paypal.preferred_locale` — 21 locales (cs-CZ through sv-SE).

**Statement descriptor**: `PAYPAL *BUSINESS_NAME` set by PayPal; custom `statement_descriptor` appended, 22-char total cap.

**Payer details** in `charge.payment_method_details.paypal`: `payer_email`, `payer_name`, `payer_id`, `transaction_id`.

**Settlement to PayPal balance**: Stripe balance transaction amount = 0; funds go to PayPal balance. Fees still recorded. Gross/Net volume charts do not reflect PayPal sales — use Payment methods report. Must maintain positive balance in both accounts for refunds/disputes. Manual reconciliation required (two methods below). Connect users always settle on Stripe (no choice). Changing settlement requires Stripe support ticket.

**PayPal transaction reconciliation**. When funds settle on PayPal, match the merchant’s customer-visible `payment_method_options.paypal.reference` to **Invoice ID**. Refunds and disputes derived from the original payment are associated with that reference. Use the PayPal capture ID as the recommended fallback if no business order ID is available. After capture, `Charge.payment_method_details.paypal.transaction_id` matches **Transaction ID**. The PayPal report covers 24 hours of balance-impacting transactions and is available from the business account or through PayPal-enabled sFTP. See [[source-stripe-paypal-reconciliation]] for the dated Stripe creation examples and the separate Stripe payout report scope.

**Async payment methods**: synchronous only by default; enable by contacting Stripe support.

**Recurring enablement** — The May 2026 guide says PayPal activation automatically enables recurring payments for most users. For those needing manual enablement in the Dashboard, access shows as pending and usually takes up to five business days. Testing environments enable recurring by default. See [[source-stripe-paypal-set-up-future-payments]].

**Save/recurring (Checkout)**: `mode: 'setup'` → `checkout.session.completed` webhook → extract `setup_intent` → retrieve SetupIntent → get `payment_method` ID.

**Save and reuse with Direct API** — The May 2026 guide sends the customer to PayPal with `confirmPayPalSetup` for billing agreement authorization and verifies it with `setup_intent.succeeded`. It places `payer_id` and `billing_agreement_id` on the Mandate and `payer_email` and `payer_id` in `PaymentMethod.paypal`. A later off-session charge uses its own PaymentIntent with `off_session: true` and `confirm: true`. On-session `confirmPayPalPayment` can omit `return_url` for a PayPal method previously set up through a SetupIntent or PaymentIntent `setup_future_usage`. See [[source-stripe-paypal-set-up-future-payments]].

**Fraudnet/Magnes risk libraries**: required for server-side on-session payments with saved PM. Pass `payment_method_options.paypal.risk_correlation_id`; missing → `paypal_risk_correlation_id_missing`. Stripe.js handles Fraudnet automatically.

**Mandate cancellation**: customer cancels PayPal billing agreement → `mandate.updated` webhook; all subsequent PIs with that PM fail. Detach: `paymentMethods.detach()` cancels billing agreement on PayPal side.

**Import existing billing agreements**: SetupIntent with `payment_method_options.paypal.billing_agreement_id` (existing BAID) + `confirm: true` + `usage: 'off_session'` + `mandate_data.customer_acceptance.type: 'offline'`. No customer redirect needed. Caveat: PayPal only sends cancellation webhooks for agreements **created through Stripe** — imported BAIDs don't get cancellation webhooks.

**Accounts v2**: use `customer_account` instead of `customer` on SetupIntent (public preview for non-Connect users).

## Link Details

**Link** saves and autofills customer payment details. The general Link wallet overview gives account and customer reach outside India, with Payment Element excluded for Thailand- or Brazil-based accounts. In an existing Link integration, eligible US Stripe accounts can surface alternative funding. See [[source-stripe-link-payment-methods]] for the separately scoped US guide.

See [[stripe-link]] for full coverage (two integration paths, eligibility criteria, customer flow, Authentication Element).

## MobilePay Details

**Denmark and Finland** card wallet with DKK, EUR, NOK and SEK presentment and 29 listed business locations in both 2026 captures. Stripe processes the underlying Visa/Mastercard transaction. Customers approve via mobile redirect or desktop phone and push. The November minimum depends on payout settlement currency after conversion.

**Manual capture**: Yes. The 2026-11-07 [[source-stripe-mobilepay|overview]] also documents partial capture as final, with the remainder released and no second capture. The 2026-05-07 [[source-stripe-mobilepay-accept-payment|acceptance guide]] specifies full-amount manual capture for Checkout, Elements and Direct API. The captures leave the effective change date and individual variant and account support unverified. **Disputes**: Yes (same as cards). Full and partial refunds.

**Card retries**: customer can retry with different card in-app.

**3D Secure**. The May capture estimated step-up at 1–7%, varying by country and card network. The November overview describes app-based 3DS with no extra integration step, no merchant enforcement option and liability shift only where authentication occurred.

**Dankort**. The November overview says Stripe uses Visa for co-branded Visa/Dankort cards.

**Fees**. November documents a daily surcharge and a monthly membership fee for applicable active Danish merchants of record, with inactivity, platform and contract qualifications. The 35 DKK amount is dated to May. Fees appear separately on the monthly tax invoice.

**Business categories**. May lists eight plain-language categories. November uses a named list and prohibited MCC table. The [[source-stripe-mobilepay|overview]] preserves the dates and directs readers to the eligibility details.

**Branding**. The app uses the configured merchant icon or a default. The 250×250 recommendation comes from May.

**Integration (2026-05-07 guide)**: Checkout, Elements, Direct API, iOS, Android and React Native. The customer has five minutes to authenticate while the PaymentIntent is in `requires_action`. Timeout detaches the PaymentMethod and returns the PaymentIntent to `requires_payment_method`. Direct API sends the customer to `next_action.redirect_to_url.url`. The guide documents cancelling the associated PaymentIntent before expiry, iOS `STPPaymentMethodMobilePayParams` with a custom return scheme, and Visa/Mastercard rules for refunds and disputes. See [[source-stripe-mobilepay-accept-payment]] for the dated capture and SDK qualifications.

## MB WAY Details

MB WAY serves **customers in Portugal** with EUR presentment and can use international phone numbers. The November 2026 capture lists 40 business locations subject to supported settlement currency and marks B2C supported. Both captures document EUR 0.50–5,000 per payment and a EUR 1,000 default daily cumulative user limit adjustable up to EUR 10,000. In November, the customer has four minutes to approve in the app, while the merchant page polls without a browser redirect or method-level return URL. Stripe documents immediate notification when it confirms success or failure. App approval and return from the app precede that separate payment confirmation. The standard payout schedule applies. See [[source-stripe-mb-way-accept-payment]] for Checkout Session return settings, payment states and May sandbox simulations.

- Full disputes are supported. Partial disputes are excluded in November. Stripe holds the balance during resolution and the evidence window is seven calendar days.
- Full or partial refunds can be issued up to 365 days from completion, typically processing in minutes. Cumulative partials cannot exceed the payment. November documents checking the Refund status and arranging another refund method if it fails and Stripe returns the amount to the balance.
- May specifies `Stripe Inc` on statements and excludes Mobile Payment Element. November says Stripe's name cannot be overridden and separately marks in-app payments supported. See [[stripe-ios-sdk]] for iOS 26.6.0 PaymentSheet evidence.
- Checkout remains one-time, with no setup or subscription mode, future usage or off-session payments. November Billing and Invoicing describe `send_invoice` with separately authorized hosted invoices, including subscription invoices. Manual capture remains unsupported.
- Connect platforms can use all charge types. Enable it through the applicable Dashboard or Capabilities API path and verify the connected account's `mb_way_payments` capability in the account API or webhooks. See [[source-stripe-mb-way]] for the dated overview and version-specific notes.

**Integration (May 2026 guide)**: Checkout, web Elements using PaymentIntents, and Direct API. The May HTML/JS and React Payment Element examples use `mb_way_pm_beta_1`. The Direct API new-PaymentMethod example supplies its linked phone to `stripe.confirmMbWayPayment`. Stripe.js polls by default, and `handleActions: false` allows manual status retrieval. See [[source-stripe-mb-way-accept-payment]] for sandbox simulations and the separate November Stripe.js reference's existing and attached PaymentMethod paths.

## GrabPay Details

**Singapore and Malaysia only** (SG/MY merchants and customers). SGD and MYR. Digital wallet with stored balance. OTP redirect authentication.

**No recurring. No manual capture. No standard disputes or chargebacks.** GrabPay OTP authentication reduces fraud and unrecognized-payment risk, while a customer contacting GrabPay may still be directed to the merchant for a refund; OTP does not rule out fraud or complaints. The November 2026 overview also marks Billing, SetupIntents, `setup_future_usage` and off-session payments unsupported. See [[source-stripe-grabpay]] for dated eligibility and payment-state detail.

**Refunds**: 90-day, async (up to 5 min).

**Branding guidelines**: mandatory — GrabPay provides PDF brand guidelines and logos/buttons zip. Must follow for checkout UI.

**2 merchant countries** (narrowest wallet coverage reviewed).

**Integration (2026-05-07 guide)**: Checkout, Direct API, iOS, Android, and React Native are five documented variants. The guide says GrabPay has no minimum charge and a PaymentIntent API `amount` may be as low as `1` with SGD or MYR; it does not state a one-whole-SGD/MYR minimum. Subscriptions and future payments were unsupported in that guide. Android collects a billing full name; Direct API uses `stripe.confirmGrabPayPayment()`. Native iOS permits a custom URL scheme **or universal link** for app return and forwards the URL to Stripe; React Native separately requires a custom URL scheme and says universal links are unsupported. The 2026-11-07 canonical root capture is a variant index only; it does not reverify those behavior rules. See [[source-stripe-grabpay-accept-payment]].

## Revolut Pay Details

**Customer and business scope.** The dated overviews list UK and EU customers and 30 Stripe-account business locations. The six currencies are EUR, GBP, RON, HUF, PLN and DKK, with GBP the UK customer default and EUR the default for other EU customers. The May 2026 opening mentions first-time checkout and saving after a first purchase for non-Revolut customers. Both Disputes sections require account login for authentication. The November opening describes account holders confirming in the app. Guest eligibility remains unresolved. See [[source-stripe-revolut-pay]].

**Full feature set**: recurring ✓, Connect ✓, disputes ✓, manual capture ✓.

**Product support**: Connect, Checkout, Payment Links, Elements, Subscriptions, Invoicing.

**Refunds** can be full or partial up to 180 days after purchase. Both overviews describe asynchronous processing up to five minutes and final `refund.updated` or `refund.failed` events. On failure the amount returns to the Stripe balance and the merchant needs another refund method.

**Disputes** follow Revolut’s Buyer Protection Policy. The customer has up to 120 calendar days from purchase. The merchant has 14 calendar days to supply the requested evidence. Revolut decides within 35 calendar days of evidence submission. See [[source-stripe-revolut-pay]].

**Integration**: Checkout, Elements, Direct API, iOS, Android, React Native. Reusable PM (supports subscriptions). Two auth flows: mobile redirect (1-hour expiry) and desktop QR code (refreshable 20×, 1-hour expiry). Manual capture: 7-day window. The May acceptance guide's Elements testing subsections describe live-mode automatic approval after redirect or scan, while its authentication instructions describe customer authorization and the November overview explicitly describes app confirmation. The November acceptance capture is a variant selector. See [[source-stripe-revolut-pay]] and [[source-stripe-revolut-pay-accept-payment]]. Failed payments detach PM → `requires_payment_method`.

**May 2026 save and reuse.** On-session payments redirect to the Revolut app even with a saved method. Obtain opt-in and retain the written agreement. Custom-form sections require authorization notice before confirmation and also say to display it after the first save. Separate SetupIntent setup from PaymentIntent charge-and-save (`setup_future_usage: 'off_session'`) and later charging. May’s Intent examples distinguish Accounts v2 `customer_account` and Customers v1 `customer`. Detach sends `mandate.updated` and `payment_method.detached`. See [[source-stripe-revolut-pay-set-up-future-payments]].

## PayPay Details

**Japan only** — JP merchants and customers, JPY only. Popular digital wallet in Japan.

**PayPay capabilities (November 7, 2026)**: Single-use only. The method profile excludes recurring payments, standard disputes, and manual capture. Radar is in private preview. The usual authorization flow redirects to PayPay, and eligible custom integrations can instead keep their page open and present a separate QR variant. PayPay authorization expires five minutes after redirect, while Stripe expires the attempt one hour after its creation.

**Refunds**: full and partial, 365-day window, instant.

**Charge limits**: min 50 JPY, max 1,000,000 JPY.

**Product support**: Payment Links, Checkout (not subscription/setup mode), Elements (not Express Checkout Element).

**Prohibited**: The November table lists cryptocurrency exchanges and wallets (MCC 6051). The May profile also mentioned other categories at PayPay's discretion.

**Connect**: Both method profiles exclude it. The May wallets table and November wallets and payment-method support tables show invite-qualified support. The tables and method profiles do not resolve any particular platform's eligibility. See [[source-stripe-paypay]].

**Integration (May 7, 2026)**: Hosted Checkout and Checkout Sessions Elements document payment mode only, with JPY and one currency per Session. The hosted sample uses `success_url`. Elements and Direct API describe `return_url` on their documented paths. iOS configures an app return, while the Android Kotlin sample omits an explicit return URL. The two web Elements paths document the sandbox approve/decline simulation. See [[source-stripe-paypay-accept-payment]] for the surface details and November variant navigation.

## Alipay Details

**Currencies and eligibility (2026-11-07)**: CNY is the Alipay default and also shown to customers. An account must have a bank account in a mapped currency. Presentment currencies are AUD, CAD, CHF, CNY, EUR, GBP, HKD, JPY, MYR, NZD, SGD and USD across 39 listed merchant countries; CHF maps to Switzerland and EUR/GBP/USD cover broader country lists than the May 2026 table (which listed CNY plus ten others and USD only for US). The new customer-location field says CN; the May page described Chinese consumers, overseas Chinese and travelers, so do not infer traveler eligibility solely from either field.

**Refunds and disputes**: full/partial refunds must be submitted within 90 days, are asynchronous (up to five minutes), cannot be canceled and are never reversals. Check Refund `status` or `refund.updated`/`refund.failed`; failure restores the Stripe balance and requires another customer refund method. Alipay has no standard customer chargeback/dispute process; a customer may instead be referred to the merchant for a refund.

**Recurring**: the 2026-11-07 standard matrix marks recurring, off-session, SetupIntents and `setup_future_usage` unsupported; recurring Invoicing, Checkout subscription/setup and saving details are available only through an invite-only recurring-payments private preview requiring individual Alipay approval. The May page also said recurring subscriptions/Invoicing required invitation. Do not treat preview documentation as merchant access.

**Connect**: destination charges and separate charges/transfers are supported. Connected accounts with standard Dashboard access can enable Alipay; otherwise the platform must request `alipay_payments`, with API capability requests in private preview. Contact Stripe Support before direct charges or `on_behalf_of`; the general Connect support checkmark does not grant these paths.

**Dual prohibited list**: Stripe's standard + Alipay's own list (stripe.com/legal/alipay).

**Integration**: Checkout, iOS, Android, React Native, Direct API. All redirect to Alipay for auth. iOS/React Native: custom URL scheme + `safepay/` host required. Android: Alipay SDK (app-to-app) or WebView fallback; **Alipay Android SDK cannot test in sandbox — live mode only**. Direct API: `stripe.confirmAlipayPayment()`.

## Satispay Details

**Italy customers only**, EUR only. Stored-value wallet. Redirect to Satispay website for auth. Immediate confirmation.

The May 2026 method guide lists 20 merchant locations. The November guide lists 37 business account locations for domestic and cross-border B2C payments, with Italy customers and EUR presentment. See [[source-stripe-satispay#Account and payment eligibility]] for dates and limits.

**Capture**: Both method guides list manual capture, and November also lists partial capture. **Disputes**: May gives 12 calendar days to submit evidence. November gives customers 120 days from purchase to file a full dispute, merchants 15 days from creation to submit evidence, and Satispay 25 days from creation for the final decision. **Refunds**: Full or partial, asynchronous, within 180 days. November documents wallet balance as the refund destination.

**Recurring payments and product support**: The May 2026 method guide marks recurring payments unsupported and links Subscriptions in Dashboard guidance. The November method guide lists recurring, SetupIntents, Billing, Invoicing and Customer Portal. The November wallet matrix still lists Subscriptions, Invoicing and Customer Portal unsupported. The separate June 24 Dahlia changelog documents scoped Intent, Subscription and Invoice support. See [[source-stripe-satispay#Recurring payments and mandates]] for those distinctions and mandate handling.

**Connect**: `satispay_payments` capability. Standard charge type descriptor rules apply (`on_behalf_of` → connected account).

**Prohibited categories**: May lists 13 named categories and a discretion catch-all. November lists 33 prohibited MCC entries. See the dated eligibility section in [[source-stripe-satispay]].

**Integration (May 8, 2026 guide)**: Checkout and Elements with Checkout Sessions support EUR payment mode and exclude setup and subscription modes. The guide also covers Elements with Payment Intents, Direct API, iOS and Android. For Direct API, Stripe.js `stripe.confirmPayment` handles client-side confirmation and redirect. The optional server-side `stripe.paymentIntents.confirm` path requires the merchant to handle the redirect after `requires_action`. Check the payment status after return. The May method overview marks recurring payments unsupported and lists Subscriptions among Dashboard products where Satispay can be added. That Dashboard listing does not establish recurring Satispay charges. The May acceptance guide documents separate authorization and capture with a seven-day window. See [[source-stripe-satispay-accept-payment]] for the mobile samples, test behavior and November 7 variant navigation.

## Vipps Details

**Vipps** is a private-preview card wallet for customers in Norway paying in NOK. The customer enters a linked phone number and authorizes in the Vipps app after a push notification. API requests that include Vipps use `vipps_preview=v1`. The November overview adds an email access-request path using `vipps_beta_preview` in its registration example. See [[source-stripe-vipps]] for the separate documented activation and payment conditions.

**Underlying mechanism**: Stripe receives card data from Vipps and processes as a Visa/Mastercard card transaction. Processing is invisible to the merchant integration.

**29 European business countries** (AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK).

**Manual capture**: Yes. **Disputes**: Yes — same process as card payments. **Refunds**: full + partial, multiple partials allowed.

**No recurring payments.**

**Product support**: Connect (all 3 charge types — Direct, Destination, Separate), Checkout (not subscription/setup mode), Payment Links (API-created only), Elements (not Express Checkout Element).

**Connect**: `vipps_payments` capability. Connected account name shown in Vipps app during checkout.

**BankAxept not supported** — BankAxept-branded cards processed on Visa/Mastercard instead.

**Fee structure**: Stripe card processing fees + applicable taxes (deducted from transaction, same as standard card) + **Vipps per-transaction fee** (billed daily, not deducted from individual transaction — deducted from Stripe balance once per day).

**Restricted business categories**. Both overviews introduce their lists as prohibited and specifically label cryptocurrencies **Restricted** in the first bullet. See [[source-stripe-vipps]] for the exact wording and account eligibility route.

**Integration**: The May 8, 2026 guide covers payment-mode Checkout, Elements and Direct API. It documents desktop phone-number/push approval and mobile app redirection, with a landing-page fallback and card retry described for Direct API. The guide distinguishes a five-minute authentication window from a seven-day hold for optional full-amount manual capture. See [[source-stripe-vipps-accept-payment]] for dated preview configuration, cancellation states and currency qualifications. Visa and Mastercard rules govern refunds and disputes.

## WeChat Pay Details

**Dated WeChat Pay overview.** May 2026 describes Chinese consumers, overseas Chinese and travelers, with more than 800 million wallet users and more than 1 billion WeChat monthly active users. November lists B2C, CN customer location, 22 Stripe account locations (AT, AU, BE, CA, CH, DE, DK, ES, FI, FR, GB, HK, IE, IT, JP, LU, NL, NO, PT, SE, SG and US), domestic and cross-border payments and account-mapped presentment. CNY is available in all those account locations and is the amount shown to the buyer. Eligibility includes a working website accessible for review and both providers' business rules.

**November capabilities.** Single use in the general overview, with independently gated off-session recurring and mini-program private previews. General Checkout continues to exclude setup and subscription modes. The method has no manual capture or standard chargebacks. Full and partial refunds are asynchronous and noncancelable, within 180 days of payment. Failed refunds return to the Stripe balance. See [[source-stripe-wechat-pay]] for the dated matrix, authorization, refund and Connect details.

**Product support**: Connect (partial), Checkout (not subscription/setup mode), Payment Links, Elements (not Express Checkout/Mobile Payment Element), Invoicing (`send_invoice` only), Terminal (not Japan).

**Connect**: **partial** — Destination + Separate charges GA; Direct + `on_behalf_of` private preview. Capability: `wechat_pay_payments` (private preview for non-Dashboard accounts).

**Integration**. The May 8, 2026 Checkout guide uses one-time line items in a single currency and lists 35 business-location codes. Its hosted and full embedded examples configure separate return parameters. The May Direct API web example uses Stripe.js QR display and server-side payment status to decide fulfillment. The November acceptance capture links Checkout, Direct API, iOS and Android. See [[source-stripe-wechat-pay-accept-payment]] for dated request fields and [[source-stripe-wechat-pay]] for the distinct November product overview and its 22-location list.

### Stripe.js 10.1.0 WeChat client typing

`@stripe/stripe-js@10.1.0` expands `ConfirmWechatPayPaymentData.payment_method_options.wechat_pay.client` from optional `'web'` to optional `'web' | 'mobile_web'`. This is the direct `confirmWechatPayPayment()` data contract, not evidence of the same option for Checkout Sessions, native SDKs or Mobile Payment Element. `ConfirmWechatPayPaymentOptions.handleActions` remains a required boolean whose comment instructs `false`; the merchant remains responsible for handling `next_action` and verifying payment outcome. See [[source-github-stripe-js]].

> [!warning] Contradiction
> The older collected integration guide describes a web-only QR flow, while the 10.1.0 declaration explicitly accepts `mobile_web`. Preserve the guide as historical flow evidence, not a universal current restriction. The new union alone does not establish country/account eligibility, redirect details or hosted-runtime availability. No payment/browser test was run. See [[source-github-stripe-js]] for exact-version evidence.

## Sources

- [[source-github-stripe-js]] - WeChat Pay `mobile_web` confirmation typing in 10.1.0, with explicit outcome/availability limits
- [[source-stripe-wallets]] — May and November 2026 Wallets hub matrices, preview request and method-specific coverage. Compare the dated Samsung Pay, WeChat Pay, Satispay, stablecoin, MB WAY, TWINT and Alipay qualifications.
- [[source-stripe-apple-pay]] — Apple Pay: iOS/RN/Web, Stripe CSR required, domain registration, request-type-dependent merchant-token support, real card test
- [[source-stripe-pmd-registration]] covers the May 2026 embedded-web guide for six methods, including required Apple Pay domain registration, plus test/live, iframe, enable/disable and Connect account rules. The November capture links Dashboard and API variants.
- [[source-stripe-apple-pay-best-practices]] — Apple Pay best practices: certificate renewal (25 mo, new CSR, dual certs in transition), express checkout, default to Apple Pay
- [[source-stripe-apple-pay-cartes-bancaires]] — Cartes Bancaires + Apple Pay: EUR only, iOS one-line config, web automatic, Connect on_behalf_of caveat
- [[source-github-stripe-react-native]] — React Native `0.74.0` evidence for per-request Apple Pay `supportedNetworks` restriction semantics
- [[source-stripe-apple-pay-recurring]] — May 2026 recurring guide, with November presentation-only capture: conditional DPAN continuity, expiring cryptogram and prompt first CIT via SetupIntent validation or charge, likely MIT failure after a failed CIT, saved `usage=on_session` restriction, and Tokens/Charges migration advice without formal deprecation
- [[source-stripe-apple-pay-merchant-tokens]] — May and November 2026 merchant-token guide: request types, dated platform support, Payment Intents versus Checkout Sessions configuration, MPAN/DPAN fallback, PaymentMethod reuse and update notifications
- [[source-stripe-apple-pay-disputes-refunds]] — dated Apple Pay disputes/refunds guide: Visa iOS 16.2+/Europe liability condition and card dispute process; saved off-session liability exception is documented separately above
- [[source-stripe-cash-app-pay]] — Cash App Pay overview (2026-05-07 and 2026-11-07): US/USD eligibility, provisional method access, payment settlement, refund and dispute boundaries, and Connect business-of-record limits
- [[source-stripe-cash-app-pay-accept-payment]] — May 2026 detailed Cash App Pay acceptance guide with seven paths, scoped authentication/capture timing and outcome checks; November 2026 base capture supplies variant navigation only.
- [[source-stripe-cash-app-pay-set-up-payment]] — Cash App Pay save/recurring: confirmCashappSetup(), mobile_auth_url 30-sec expiry, authorization text, revocation
- [[source-stripe-google-pay]] — May 2026 combined Google Pay Android/RN/Web guide: dated DPAN/FPAN/e-commerce token liability scope, domain registration and Sigma card_token_type; November base URL is a navigation index
- [[source-stripe-grabpay]] — GrabPay: SG/MY only, OTP redirect, no disputes/recurring/manual capture, mandatory branding guidelines
- [[source-stripe-grabpay-accept-payment]] — 2026-05-07 detailed GrabPay acceptance guide for five variants (Checkout, Direct API, iOS, Android, React Native), with dated no-minimum PaymentIntent wording, platform-specific return links and payment outcome bounds; 2026-11-07 root capture is navigation only
- [[source-stripe-link]] — May and November 2026 general Link wallet overviews cover integration and eligibility outside India, with separate Thailand and Brazil Payment Element restrictions.
- [[source-stripe-link-payment-methods]] — US Link funding guides for an existing Link integration, with session eligibility, Dashboard labels, Charge group fields and dated settings.
- [[source-stripe-mb-way]] — May 7 and November 7, 2026 wallet overviews covering eligibility, app authorization, hosted invoice support, disputes and refunds.
- [[source-stripe-mb-way-accept-payment]] — May 2026 Checkout, web Payment Element and Direct API guide with app authorization, payment outcome and sandbox boundaries. The November variant index is navigation only. The linked Endive changelogs document HTTP 400 for writable `payment_method_types` on `2026-09-30.endive` Checkout Session and PaymentIntent create. The acceptance source distinguishes MB WAY polling from the May Checkout Session return settings.
- [[source-stripe-mobilepay]] — May and November 2026 product overviews for the DK/FI wallet, eligibility, activation, final partial capture, refunds, disputes and dated restrictions.
- [[source-stripe-mobilepay-accept-payment]] — 2026-05-07 MobilePay acceptance guide covering Checkout, Elements, Direct API, iOS, Android and React Native, with dated customer authentication and capture guidance. The 2026-11-07 capture indexes the same six variants.
- [[source-stripe-paypal]] — Stripe-processed PayPal for 30 listed European business locations, including CH, GB, LI and NO, with dated marketplace approval, 180-day refunds and reporting
- [[source-stripe-paypal-button]] covers the dated May and November 2026 button and redirect conditions for Express Checkout Element and Stripe Checkout, and the Checkout Session examples.
- [[source-stripe-paypal-activate]] — PayPal activation for eligible Stripe accounts in the EU except Hungary, plus Liechtenstein, Norway, the UK and Switzerland. See dated settlement, Connect onboarding, cutover and prior-payment servicing.
- [[source-stripe-paypal-accept-payment]] — PayPal accept-a-payment: 5 paths (Checkout/Direct API/iOS/Android/RN), auth windows by settlement preference, preferred locale, statement descriptor format, payer details fields
- [[source-stripe-paypal-set-up-future-payments]] — May 2026 PayPal setup and reuse guide with agreement lifecycle and risk-library qualifications, plus the November 2026 implementation selector.
- [[source-stripe-paypal-settlement]] — PayPal settlement preference: Stripe vs PayPal balance, Dashboard reporting differences, reconciliation, changing requires support ticket
- [[source-stripe-paypal-disputes]] — PayPal filing window, evidence deadlines, 30-calendar-day decision aim, eligible PayPal appeals, settlement and dated test examples
- [[source-stripe-paypal-reconciliation]] — May and November 2026 guides to reconciling transactions settled on PayPal, with the reference and capture ID report keys, dated PaymentIntent creation examples and report access.
- [[source-stripe-paypal-import]] — PayPal billing agreement import: billing_agreement_id on SetupIntent, offline mandate, no cancellation webhooks for imported BAIDs
- [[source-stripe-amazon-pay]] — May and November 2026 Amazon Pay overviews: worldwide customers, US USD-only currency row, claim-specific dispute deadlines, refund status and optional Charge transaction ID; account and path qualifications apply
- [[source-stripe-amazon-pay-accept-payment]] — Amazon Pay integration: 5 paths, 10-min auth window, 7-day manual capture, confirmPayment()
- [[source-stripe-amazon-pay-set-up-future-payments]] — Amazon Pay save/recurring: confirmAmazonPaySetup(), redirect_to_url, authorization text required, iOS/Android
- [[source-stripe-alipay]] — Alipay overview: 39 merchant countries, November 2026 expanded currency map/eligibility, standard one-time versus recurring preview, refund and Connect state boundaries; dated May currency and traveler context
- [[source-stripe-alipay-accept-payment]] — 2026-05-07 Alipay acceptance guide: Checkout, Direct API and three mobile paths; iOS/React Native safepay return handling, Android app-to-app live-mode test limit versus WebView, and web Direct API `confirmAlipayPayment`. The 2026-11-07 canonical capture is a variant index only.
- [[source-stripe-revolut-pay]] covers the May and November 2026 overviews, customer scope, app and QR confirmation, six currencies, asynchronous refunds and the dispute evidence timeline.
- [[source-stripe-revolut-pay-accept-payment]] covers the May integration paths, mobile redirect and desktop QR (up to 20 refreshes), dated testing wording and a seven-day manual capture window. The November acceptance capture is a variant selector.
- [[source-stripe-revolut-pay-set-up-future-payments]] — May 2026 setup, consent wording, later charges and detach. The November variant index provides navigation.
- [[source-stripe-paypay]] — Japanese JPY wallet, May and November Connect documentation, authorization and expiry, and 365-day refunds
- [[source-stripe-paypay-accept-payment]] — May 2026 PayPay acceptance and return handling across six surfaces, with November variant navigation
- [[source-stripe-satispay]] — May and November 2026 Satispay method guides for Italy/EUR, business-account eligibility, recurring and mandate guidance, and dated dispute and refund rules.
- [[source-stripe-satispay-accept-payment]] — May 2026 Satispay acceptance and manual capture guide for four web and two mobile paths. The November 2026 capture links those variants.
- [[source-stripe-vipps]] — May and November 2026 Vipps overviews with private-preview access, Stripe card processing, API-created Payment Links, Connect activation and separate daily Vipps fee.
- [[source-stripe-vipps-accept-payment]] — May 2026 full guide and November variant index for Vipps acceptance. See dated authorization, capture, preview and business-location qualifications.
- [[source-stripe-wechat-pay]] — May and November WeChat Pay overviews with dated geography and eligibility, desktop and native authorization, independent previews, refunds and Connect reconciliation
- [[source-stripe-wechat-pay-accept-payment]] — May 2026 Checkout and Direct API web guide with 35 listed Checkout business locations, QR and fulfillment terms. November indexes Checkout, Direct API, iOS and Android.
