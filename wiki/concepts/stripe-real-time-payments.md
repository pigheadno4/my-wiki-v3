---
title: "Real-Time Payments (Stripe)"
type: concept
category: technology
tags: [stripe, real-time-payments, paynow, payto, promptpay, swish, pay-by-bank, pix, open-banking, instant-transfer]
---

## Definition

Real-time payment methods let customers directly transfer money from their bank account or alternate funding source. Stripe supports real-time payments across multiple regions.

> Note: The real-time payments hub page ([[source-stripe-real-time-payments]]) listed "Pay by Bank" as a Brazil method — this was an error. Brazil's real-time payment method is **Pix** (`pix`), confirmed by the Pix product page ([[source-stripe-pix]]). The hub page Brazil entry has been removed from the table above.

## Supported Methods

| Method | API enum | Customer region | Redirect | SetupIntents | setup_future_usage | Mobile |
| --- | --- | --- | --- | --- | --- | --- |
| Pay by Bank (UK/Europe) | `pay_by_bank` | UK, Finland and Ireland generally available. Belgium, France and Germany private preview (2026-11-07 customer bank-account scope) | Yes | No | No | May matrix: No. November matrix: Yes |
| PayNow | `paynow` | Singapore | No | No | No | Yes |
| PayTo | `payto` | Australia | No | Yes | Yes | No |
| Pix | `pix` | Brazil | Bank app has no return redirect. Checkout/Elements can redirect at a terminal intent state. | Yes in the November Pix matrix. See Pix Automático mandate scope. | Yes in the November Pix matrix. See Pix Automático mandate scope. | Yes |
| PromptPay | `promptpay` | Thailand | No | No | No | Yes |
| Swish | `swish` | Sweden | Yes | No | No | Yes |
| UPI | `upi` | India | November API matrix Yes. Desktop QR and mobile app redirect in the overview. | November matrix Supported | November matrix Supported (`off_session` per its footnote) | Mobile Payment Element Unsupported in November matrix |

**No manual capture** for any real-time payment method.

## Key Differentiators

**PayTo** (Australia) supports SetupIntents, `setup_future_usage`, mandate-based recurring payments and Billing, with required identity verification. The May and November cross-method tables and November PayTo profile mark Express Checkout Element unsupported. The November cross-method matrix also lists SetupIntents and future-use support for UPI. See [[source-stripe-payto]] for the separate off-session qualification. The November Pix overview also lists SetupIntents and `setup_future_usage`, with a separate Pix Automático mandate flow.

**PayNow** (Singapore): the November 2026 overview lists Terminal public preview and requires manual listing.

**Redirect required.** The November 7, 2026 API support matrix marks Pay by Bank, Swish and UPI as requiring redirect. The direct UPI overview describes customers scanning a QR code in their UPI app on desktop and being redirected to the UPI app on mobile.

**Subscriptions/Invoicing**: Pay by Bank, PayNow, and PromptPay support subscriptions/invoicing only via `send_invoice` (not `charge_automatically`). For Swish, the May and November real-time matrices label Subscriptions `send_invoice` only and Invoicing unsupported, while the November method page lists Billing and Invoicing as unsupported. For Pay by Bank, this Billing scope is separate from the Bacs-backed Elements/Payment Intents private preview described below. **Pix** supports automatic recurring via **Pix Automático** (mandate-based, charge_automatically). **PayTo**. The November PayTo profile lists Billing and recurring payments as supported and marks off-session payments unsupported. The separate November payment-method matrix marks future usage supported and footnotes `off_session`-only support for eligible non-card and non-bank-debit methods. Billing `charge_automatically` remains unresolved. See [[source-stripe-payto]] for the dated evidence. The November acceptance capture only indexes variants.

> [!info] Evolving
> PayTo’s Billing collection method (`send_invoice` or `charge_automatically`) remains unresolved. See [[source-stripe-payto]] for the dated PayTo profile and payment-method matrix. The November acceptance selector supplies variant navigation only.

## Pix Details

**QR code or Pix string** real-time payment — Brazil customers only, BRL currency. Processed via **Ebanx** (Stripe's Brazil partner).

**Business locations and limits**. The November 7, 2026 Pix overview lists instant provisional access, with Brazilian accounts limited to one-time Pix and BRL settlement. May described Brazilian one-time access as invite-only. November documents a BRL 0.50 minimum and a default per-payment maximum equivalent to USD 3,000, with higher limits for enabled accounts. For Brazilian buyers paying a business outside Brazil, November lists USD 3,000 daily and USD 10,000 monthly per customer per business.

**Refunds and disputes**. Request a full or partial refund within 90 days. Refunds return to the original bank account. Refund-request status leaves bank credit unconfirmed. Stripe debits disputed funds after notice of partner acceptance. See [[source-stripe-pix]] for eligibility, timing and dispute conditions.

**IOF tax** (3.5% on international transactions): merchant chooses who pays via `amount_includes_iof` (`never` = customer pays, default; `always` = merchant absorbs). API users must display Ebanx T&C disclosures. Checkout/Elements handle disclosures automatically.

**Statement descriptor**: ignored — Ebanx shown as recipient; merchant name in `identifier` field only.

**Recurring**: via **Pix Automático** (separate sub-product with mandate-based authorization). Not available for BR accounts.

**Prohibited categories**. The November 7, 2026 Pix overview lists 12 prohibited MCCs and additional crypto and telehealth or medicine exclusions. It identifies the nonprofit and charity exclusion in Singapore. May used broader category wording. See [[source-stripe-pix]] for dated eligibility and the raw MCC table.

**Connect**: MoR-sensitive. Capability: `pix_payments`.

**Integration**. The May 6, 2026 guide documents one-time Pix using Checkout, Elements or Direct API. Checkout’s configurable expiry is up to 14 days, Direct API’s is up to three days, and Elements describes four hours from QR creation. The guide gives CPF/CNPJ requirements for cross-border transactions. See [[source-stripe-pix-accept-payment]] for integration details and the separate Pix Automático route for setup or recurring payments.

**May 2026 save/recurring (Pix Automático).** Checkout and Direct API require a customer-authorized mandate. The save guide illustrates `amount` and `payment_schedule`; the separate customization and subscription guides distinguish defaults from route-specific choices. Direct API uses `stripe.confirmPixSetup()` for setup without charging or `stripe.confirmPixPayment()` with off-session future usage to pay and save. QR instructions are available through the matching Intent's `next_action`. A saved method can charge once per specified cycle, and mandate revocation sends `mandate.updated` and calls for a new on-session mandate. See [[source-stripe-pix-save-payment-details]].

**Pix Automático — recurring mechanics**: the customer authorizes the amount and permitted billing cycle in their banking app. After the merchant confirms a recurring PaymentIntent, Stripe triggers the notice process and the bank sends the exact amount and a cancellation option. Stripe waits three days to attempt automatic capture. The PaymentIntent stays `processing` during the wait and retries. Confirmation usually takes three days after notice, up to seven with retries. Stripe retries a retryable capture failure once a day for the next three days by default. An opt-in Stripe Billing retry can run once after one day if the payment never scheduled. The default mandate amount is 400 BRL and a daily schedule causes payments to fail. The separate [[source-stripe-pix|Pix overview]] scopes eligibility to businesses outside Brazil collecting recurring Pix from customers in Brazil. See [[source-stripe-pix-automatico]] for the dated guide and PaymentIntent status scope.

## PayTo Details

**Mandate-based** real-time payment — Australia customers only, AUD only, AU merchant accounts only. **Identity verification required** before activation.

**Payment flows**: PayID (unique identifier linked to bank account) or Account + BSB numbers. Customer receives push notification or email to authorize mandate in banking app.

**Delayed notification**. Stripe typically reports the final payment outcome within 60 seconds after mandate authorization. Check the result for payment success.

**Mandates**. Stripe configures a fixed amount and ad hoc cadence for one-off payments, and merchants can override the inferred purpose. Use the least permissive terms for recurring payments. See [[source-stripe-payto]] for the mandate options and cancellation.

**Bank limits**. Both dated tables list 43 institutions. ANZ, CBA, Westpac and Macquarie reject mandates over AUD 25,000 and mandates without a maximum. Westpac separately declines ad hoc payments over AUD 1,000 for high-risk merchants. Business account coverage is lower than individual-account coverage. Keep bank limits separate from the November AUD 10,000 default account limit and AUD 100,000 method maximum with approval.

**Disputes**. The November PayTo profile supports full disputes only. Disputes are final. Stripe sends `charge.dispute.created` and `charge.dispute.closed`.

**Refunds**. Requests can be made up to two years after payment. A PayID refund can fail when the payment billing name differs from the bank-account name. Check refund status. See [[source-stripe-payto]] for the November conditions.

**Connect**. The May 6, 2026 PayTo overview lists direct charges, destination charges, and separate charges and transfers. Both dated overviews say the platform requests `payto_payments` for connected accounts using Express or a non-Stripe-hosted Dashboard. The November 7, 2026 overview says that for destination charges the statement uses the platform identity when `on_behalf_of` is omitted and the connected-account identity when it is set.

## Pay by Bank (UK/Europe) Details

**Open banking availability**. The November overview lists UK, Finland and Ireland bank accounts as generally available and Belgium, France and Germany in private preview. May listed France, Germany and Ireland in private preview. Merchant eligibility is separate, with 35 Stripe account locations in both overviews. UK accounts use GBP and listed European accounts use EUR.

**Transaction limits and payout**. £0.50–£10,000 default GBP range. Higher amounts require contacting Stripe. The one-off method lists standard payout. November states that an authorized payment can fail with `payment_method_provider_timeout` and Stripe returns funds arriving after failure.

**Disputes and refunds**. November scopes the no-chargeback description to inadequate-goods or services complaints. Both captures describe full or partial refunds to the original account within 730 days, with no refund fee and the original processing fee retained. Follow the Refund status to its outcome.

**Connect**. Direct charges, destination charges, and separate charges and transfers. Use Dashboard Payment methods where available or request `pay_by_bank_payments` for Express and non-Stripe dashboards. Check `active` through Accounts API or webhooks.

**Product support**. The overviews list Connect, Payment Links, Checkout and Elements, with Checkout subscription mode and Express Checkout Element excluded. The separate May real-time matrix excludes Mobile Payment Element and the November matrix lists it, while the November method overview drops the original mobile exclusion. The Bacs-backed recurring flow is a separate Elements and Payment Intents private preview. See [[source-stripe-pay-by-bank]].

**Integration**. The 2026-05-06 [[source-stripe-pay-by-bank-accept-payment|acceptance guide]] details Checkout and web Elements with Payment Intents. Its manual Checkout flow specifies a statement descriptor. Its Checkout business location table and manual currency examples have dated qualifications. The 2026-11-07 acceptance capture indexes Checkout, both Elements API routes, iOS and Android. May describes immediate success/failure notification, while the April [[source-stripe-checkout-dashboard-payment-methods|Dashboard-managed Checkout guide]] lists Pay by Bank under delayed notification. Bank authorization and browser return are separate from verified payment success, available funds and payout. See the acceptance source for the scope of each statement.

## PayNow Details

**QR payments**: Singapore customers and business accounts, domestic SGD. The November 2026 overview lists provisional access and SGD 0.50 to SGD 200,000.00 limits. The May guide quotes 1.3%, and November links to pricing. Stripe balance availability is one day after payment, with bank payout on the account schedule.

**Refunds**: Full and partial within 90 days. November documents asynchronous `pending` status, processing up to five minutes and no cancellation. Check the Refund object's final status. **Disputes**: Stripe attributes low fraud risk to app authentication and documents no standard dispute or chargeback process.

**QR authorization**: One-hour expiry. On `payment_intent_payment_attempt_expired`, the guide routes the customer back to create a new PaymentIntent and QR. Reusing a successful QR is rejected.

**Billing and UI**: Invoices and subscriptions use `send_invoice`. November lists the Payment Element at product level. Terminal is public preview and requires manual listing.

**Connect and references**: PayNow supports direct, destination and separate charges and transfers. Enable it on the platform, request `paynow_payments` for connected accounts accepting it, and set the correct MCC for accounts without the full Stripe Dashboard under the November guidance. Connect charge type controls the merchant name shown in the app flow. The bank statement has Stripe’s fixed name, amount and Stripe-generated reference. See [[source-stripe-paynow]] for the separate statement field, eligibility and capability rules.

**Integration**. The May 6, 2026 acceptance guide covers Checkout and Direct API. Its Direct API example displays an inline QR using `stripe.confirmPayNowPayment` and verifies successful payment on the server. November links both variants. The separate [[source-stripe-paynow|PayNow method overview]] lists Payment Element and excludes Express Checkout Element. See [[source-stripe-paynow-accept-payment]] for the May return and payment-state boundaries.

## UPI Details

**QR code (desktop) / redirect (mobile)** real-time payment — India customers only, INR only. Developed by NPCI.

**Transaction limits**: 1 INR – 100,000 INR. Recurring max: **15,000 INR**.

**UPI refunds.** The two 2026 method captures specify a 60-day window and asynchronous processing up to seven business days. Stripe returns a failed refund to the merchant's Stripe balance, and the merchant arranges an alternative refund.

**Disputes**: Supported but **non-contestable** — funds removed from Stripe balance immediately on acceptance.

**Recurring.** UPI AutoPay uses a customer-authorized e-mandate. The May and November direct overviews list Invoicing, Payment Links and Subscriptions without specifying a Billing collection mode.

**Business locations.** Both direct overviews list 35 Stripe account countries, separate from India customer location. See [[source-stripe-upi]].

**Connect**: Yes.

**Acceptance (May 6, 2026)**: Checkout, Elements with Checkout Sessions and Elements with Payment Intents. Checkout describes payment, setup and subscription with UPI AutoPay e-mandates and a five-minute QR window with `payment_intent.payment_failed` on expiry. The guide distinguishes immediate one-off and saving-case notifications from delayed off-session or recurring outcomes when the customer is absent. See [[source-stripe-upi-accept-payment]] for acceptance and [[source-stripe-upi-set-up-future-payments]] for the separate Direct API saving paths.

**Save/recurring (May 6, 2026 guide).** With customer permission and a mandate, save UPI through hosted Checkout setup mode, a Direct API SetupIntent confirmed with `stripe.confirmUpiSetup()`, or a UPI PaymentIntent confirmed with `setup_future_usage: 'off_session'` to initiate payment and save. The Direct API samples show a billing name and Indian address, including `line2`, without specifying requiredness for each field. For a later PaymentIntent, reuse the PaymentMethod ID and set `off_session: true` when the customer is outside checkout. On-session payments still redirect to the UPI app. The optional manual flow uses `upi_handle_redirect_or_display_qr_code` when the PaymentIntent requires action. Detach emits `mandate.updated` and `payment_method.detached`. See [[source-stripe-upi-set-up-future-payments]].

**UPI AutoPay (May and November 2026 guides)**: The customer authorizes setup with a UPI PIN. Stripe handles the initial charge window of up to five minutes. A SetupIntent debits and immediately refunds the customer to avoid AFA on the intended later charge. The guides attribute to RBI a requirement that customers receive an SMS or app notice with the exact amount and cancellation option at least 24 hours before each recurring charge. After merchant confirmation of the recurring PaymentIntent, Stripe sends the notice and waits at least 24 hours before attempting the charge. Sending alone leaves delivery and compliance unverified. The default and automatic charge maximum are 15,000 INR. `amount_type` defaults to `maximum`, and expiration defaults to 10 years from creation, with a 40-year scheme maximum from now. For a customer-initiated Adaptive Pricing subscription, automatic creation uses a supported selected currency. Explicit Checkout Session mandate parameters take precedence. See [[source-stripe-upi-autopay]].

## PromptPay Details

**PromptPay QR payments.** Thailand customers in THB, with instant Stripe confirmation on completion. May and November list TH as the standard Stripe account location. November separately describes a US-based Stripe-account private-preview waitlist, with Stripe review and contact for eligible applicants. See [[source-stripe-promptpay]].

**Statement descriptor**: ignored — `STRIPE PAYMENTS (THAILAND) LTD` shown with unique reference code.

**Refunds.** Stripe writes to the email provided at PaymentIntent confirmation for the number of the account that originally funded the payment, then processes the refund automatically after receiving it. Without that information the refund might fail. See [[source-stripe-promptpay]].

**Duplicate QR risk**: re-scanning a completed QR **can deduct funds again** (unlike PayNow which rejects duplicate scans). Stripe reimburses excess to merchant balance; merchant must refund customer outside Stripe.

**Disputes**: "Not applicable" — Stripe reviews irregularities directly.

**Billing**: `send_invoice` only. Mobile Payment Element: iOS only (not Android).

**Connect**: Yes. No payout timing specified.

**Integration**: The May 2026 [[source-stripe-promptpay-accept-payment|acceptance guide]] describes Checkout and Direct API. Its Direct API example uses a server-created THB PaymentIntent, client secret and `stripe.confirmPromptPayPayment()`. Email is the only billing-detail field in the new-method example. Confirm completion server-side through `payment_intent.succeeded`. The November acceptance selector links Checkout and Direct API. The separate method overviews list Elements at product level, exclude Express Checkout Element and limit Mobile Payment Element to iOS.

## Swish Details

**Mobile redirect or desktop QR** for Swedish customers using Swish and Swedish BankID. The November 2026 overview lists single-use B2C payments of SEK 3–150,000 and a three-minute authorization window. Expiry returns the PaymentIntent to `requires_payment_method` and successful payment reaches `succeeded`. Stripe reports the outcome immediately and follows its standard payout schedule.

**Stripe is the merchant of record** under the Swish factoring addendum and appears as recipient in the Swish app. The November 2026 overview distinguishes the automatic business-name Message, the conditional PPRO statement-descriptor forwarding of a custom reference, and the provider-returned bank reference. PPRO or the bank can display a different descriptor. See [[source-stripe-swish]] for the field and Connect scope.

**27 merchant countries** — European focus only (no US/AU/SG).

**Refunds** can be full or partial up to 365 days after payment completion, including multiple partials totaling up to the original payment amount. They usually take a few minutes. Check the asynchronous result using the Refund object's status or `refund.updated`/`refund.failed`.

**Product scope** in the November 2026 Swish overview includes Connect, Checkout (payment mode), Payment Links, Embedded form, Payment Element, and in-app payments. It excludes recurring payments, standard disputes, Billing, Invoicing, Express Checkout Element, and Checkout setup/subscription modes. Both dated real-time matrices separately show Payment Links unsupported and Subscriptions `send_invoice` only, with Invoicing unsupported.

**Prohibited categories**: Wine/Champagne producers, alcoholic beverage wholesalers, package liquor stores, pawn shops, art dealers, real estate rental agents, legal services/attorneys, precious metals/jewelry, digital wallet top-ups.

**Connect**: Direct, Destination, Separate charges and transfers.

**Integration** — The May 2026 guide covers Checkout, Elements, Direct API, and custom iOS, Android and React Native. Direct API and the custom mobile guides require an on-screen localized claim-acquisition notice before authorization. Stripe displays it for hosted forms and UI components such as Checkout and Payment Element. Direct API gives QR and hosted instructions in `next_action.swish_handle_redirect_or_display_qr_code`, plus an optional Swish order reference. The May desktop Elements QR can be refreshed up to 20 times. The guide describes merchant cancellation before expiry. See [[source-stripe-swish-accept-payment]].

## Bizum Details

**Real-time payment** — Spain customers only, EUR only, no recurring or manual capture. The customer enters a Bizum-registered phone number and approves in the bank app. **Connect changed by capture**: the 2026-05-06 overview listed No; the 2026-11-07 overview lists Yes and requires `bizum_payments` active on the platform and each accepting connected account. The capability can remain `pending` until onboarding verification, so support does not prove account activation. Direct charges use the connected-account descriptor; destination and separate charges/transfers use the platform's unless `on_behalf_of` selects the connected account. See [[source-stripe-bizum]].

**Transaction limits**: €0.50–€5,000. 28 merchant countries.

**Onboarding**: must provide tax/national ID and set `business_type` before capability activates.

**Disputes**: 120-day customer initiation window; **40-calendar-day** merchant evidence deadline; Bizum decision within 90 calendar days. Submission does not resolve the dispute.

**Refunds**: Full and partial refunds up to **395 days** after purchase; asynchronous, up to five minutes, with final `refund.updated` or `refund.failed` status. Neither raw overview proves a comparison against every reviewed payment method.

**Integration (2026-05-06 guide)**: four web variants—hosted Checkout, Elements Checkout Sessions API, Elements Payment Intents API, and Direct API. In the dated Direct API path, collect the customer's Bizum-registered phone number as `billing_details[phone]`; Stripe.js polls by default after confirmation until the PaymentIntent is `succeeded` or failed at `requires_payment_method`. This does not guarantee that no redirect occurs; the old Direct API text mentions redirect handling, and the Elements Payment Intents variant uses a `return_url` with possible intermediate redirect. The old guide also contains iOS StripePaymentsUI/webview and Android Kotlin `PaymentLauncher` examples. The 2026-11-07 canonical capture only indexes the four web variants and does not revalidate mobile support or SDK versions. See [[source-stripe-bizum-accept-payment]].

## Sources

- [[source-stripe-real-time-payments]] — overview: 5 methods, product/API support matrices, PayTo standout
- [[source-stripe-upi]] — May and November direct UPI overviews with 35 account locations, app authorization, AutoPay limits, refund outcomes and non-contestable disputes after bank or provider acceptance
- [[source-stripe-upi-accept-payment]] — May 2026 UPI acceptance guide covering Checkout and two Elements APIs, with November variant navigation
- [[source-stripe-upi-set-up-future-payments]] — May 2026 UPI setup and payment paths, consent, address examples, later payments and QR handling. The November index links Checkout and Direct API variants.
- [[source-stripe-upi-autopay]] — May and November UPI AutoPay guides on setup PIN, recurring PaymentIntent notice, mandate limits, and conditional Adaptive Pricing
- [[source-stripe-pix]] — dated Pix product overviews, including Brazilian QR payments, country and account eligibility, limits, refunds and disputes, cross-border IOF, and Pix Automático mandates.
- [[source-stripe-pix-accept-payment]] — May 2026 Pix one-time acceptance guide for Checkout, Elements and Direct API, with expiry and cross-border tax-ID scope. November links the variants.
- [[source-stripe-pix-save-payment-details]] — Pix save/recurring: Checkout + Direct API, confirmPixSetup/confirmPixPayment, next_action.pix_display_qr_code, mandate revocation
- [[source-stripe-pix-automatico]] — Pix Automático: bank pre-debit notice, mandate defaults, default retries after retryable capture failures and a separate opt-in Billing retry for unscheduled payments (May and November 2026).
- [[source-stripe-promptpay]] — PromptPay QR payments for Thai customers in THB, standard TH accounts and November US private preview, with refund and duplicate-payment guidance
- [[source-stripe-promptpay-accept-payment]] — May 2026 Checkout and Direct API implementations for THB QR payments and verified completion. The November capture indexes those two variants.
- [[source-stripe-swish]] covers the May and November 2026 overviews, Swedish customer eligibility, authorization states, asynchronous refunds, and PPRO reference and product scope.
- [[source-stripe-swish-accept-payment]] — May 2026 Swish implementation guide with custom-flow notice and authorization outcomes, plus the November 2026 implementation selector.
- [[source-stripe-payto]] — May and November 2026 Australian PayTo overviews, including 43 listed institutions, mandate terms, refund and dispute conditions, and Connect statement identity.
- [[source-stripe-pay-by-bank]] — May and November 2026 Pay by Bank overviews for bank-account eligibility, authorized-transfer timeout, refunds, Connect activation and the Bacs-backed recurring private preview.
- [[source-stripe-pay-by-bank-accept-payment]] — May 2026 Checkout and web Elements/Payment Intents guide with dated configuration and outcome qualifications. November 2026 selector indexes Checkout, both Elements API paths, iOS and Android.
- [[source-stripe-paynow]] — May and November 2026 PayNow overviews for Singapore SGD QR payments, balance availability and scheduled payout, refunds, Connect and Terminal preview.
- [[source-stripe-paynow-accept-payment]] — May 2026 Checkout and Direct API guide with dated return, inline QR and verified payment outcome details. November links the two variants.
- [[source-stripe-bizum]] — Bizum overview, May and November 2026 full captures: Spain customer/EUR scope, identity onboarding, disputes/refunds, and dated Connect No-to-Yes change with platform and connected-account `bizum_payments` capability and charge-type descriptor rules; pending capability is not active acceptance.
- [[source-stripe-bizum-accept-payment]] — Bizum acceptance: 2026-05-06 detailed Checkout, Elements, Direct API and mobile guide; 2026-11-07 web-variant navigation index only
