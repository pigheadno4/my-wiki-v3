---
title: "Buy Now, Pay Later (Stripe)"
type: concept
category: technology
tags: [stripe, bnpl, buy-now-pay-later, klarna, affirm, afterpay, installments, payments]
---

## Definition

Stripe's November 7, 2026 overview lists 11 buy now, pay later (BNPL) methods: customers pay nothing or a portion at purchase time and repay a provider in installments. Its ten-row API table marks the listed methods as requiring redirect but omits Scalapay, so it does not establish Scalapay API or redirect behavior. For Klarna specifically, payment acceptance credits the order amount minus fees to the merchant's Stripe account and standard payout timing applies; this does not promise an immediate external payout. Buyer selection and return do not establish approval or completed payment. See [[source-stripe-bnpl-overview]] and [[source-stripe-klarna]].

## Supported Methods

| Method | API enum | Countries | Transaction limits | Notable |
| --- | --- | --- | --- | --- |
| Affirm | `affirm` | US, CA; GB private preview | US USD 35–30k across eligible options; CA CAD 50–30k; GB preview GBP 50–30k | Single-use; no recurring payments, SetupIntents, or off-session use; Terminal listed; November overview marks Customer Portal Supported and Subscriptions Unsupported, versus May overview Subscriptions via `send_invoice` and Portal Unsupported |
| Afterpay/Clearpay | `afterpay_clearpay` | AU, CA, NZ, UK, US | $1–$4k | — |
| Alma | `alma` | — | — | — |
| Billie | `billie` | 11 business/customer countries in November 2026 Billie overview | Minimum 0.01 EUR; maximum varies by country/currency | May 2026 cross-BNPL matrix marks setup_future_usage supported; November Billie-specific matrix marks PaymentIntents with it unsupported. See dated conflict below. |
| Klarna | `klarna` | 23 customer countries (May/November 2026 overview) | See dated country/currency tables | SetupIntents, Express Checkout, setup_future_usage, Subscriptions |
| Kriya | `kriya` | — | — | setup_future_usage |
| Mondu | `mondu` | — | — | setup_future_usage |
| Scalapay | `scalapay` | — | — | — |
| SeQura | `sequra` | — | — | November overview marks `setup_future_usage` Unsupported (May overview marked Supported); Invoicing `send_invoice` only |
| Sunbit | `sunbit` | — | — | `setup_future_usage` Supported; no manual capture (both May and November API tables) |
| Zip | `zip` | AU, US | AU: 0.01–50k AUD; US: $35–$1.5k | No manual capture, no setup_future_usage |

**Meses sin intereses** (Mexico): credit card installments 3–24 months; min 100 MXN/month.

## API Support

The November 2026 overview's API matrix has ten rows, omitting Scalapay. Its listed methods show PaymentIntents support and redirect required; this is not an all-eleven claim. Manual capture is supported for Affirm, Afterpay/Clearpay, Alma, Billie, Klarna, Kriya, Mondu, and SeQura, and unsupported for Sunbit and Zip. Klarna alone shows SetupIntents support. `setup_future_usage` is supported for Billie, Klarna, Kriya, Mondu, and Sunbit; SeQura changed from May Supported to November Unsupported. The API footnote says non-card/bank-debit methods either do not support the parameter or support only `off_session`; it does not promise every session mode. The Billie support cell conflicts with the November method-specific Billie matrix, which marks PaymentIntents with `setup_future_usage` unsupported; both Billie overviews mark recurring payments unsupported. Preserve this dated conflict and verify the integration route rather than inferring recurring support. Klarna alone shows Express Checkout Element support in the product matrix, where saving during payment via `setup_future_usage` is excluded. See [[source-stripe-bnpl-overview]].

**Connect conflict**: Both overview product matrices mark all eleven methods Supported on Connect, while the May method-specific captures for Kriya, Mondu, SeQura, and Scalapay say Connect No. This is an unresolved dated source conflict, not an established account entitlement; see [[source-stripe-bnpl-overview]] and the individual method sources.

## Affirm Details

**Domestic only** — customer country must equal merchant country. Buyer country determined by shipping address → geocoded IP.

**Financing packages**: Standard (default) and Enhanced (additional listed monthly 0% APR tiers); eligible businesses with Dashboard access can view or change the package, except platforms and connected accounts. The captured platform exclusion applies to Pay in 30 and monthly 0% APR plans; Pay in 4 is separately listed at 0% APR. GB Pay in 3 appears in the November Standard table but not Enhanced, so do not infer Enhanced GB availability.

**Refunds**: full or partial refunds can be submitted within 120 days; November describes asynchronous processing of up to two days and remaining scheduled payments canceled, with final `Refund.status` or `refund.updated`/`refund.failed` determining completion. May alone says no processing-fee credit, multiple partial refunds and no refund creation during an open dispute, and describes the customer plan as paused rather than canceled; retain those as dated claims.

**Disputes**: November capture says customers have 120 calendar days from purchase to file, merchants have 15 days from dispute creation to submit evidence, and Affirm issues a decision within 60 days of creation; repeated disputes are separate objects. **Dated conflict:** May capture said no customer filing limit, up to 30 days from creation for resolution and a decision within 15 days after evidence submission. Affirm's loss coverage is stated for customer fraud, with possible stop-or-pause-shipment requests; it is not a universal dispute guarantee. See [[source-stripe-affirm]].

**Prohibited**: B2B, home improvement, titled goods (cars/boats), professional services, NFTs, pre-orders.

**Connect**: requires `affirm_payments` capability + correct MCC.

**Integration notes (May 2026 guide)**: The guide describes a 12-hour no-action timeout for `requires_action` PaymentIntents, but its prose starts the clock after the Affirm redirect while its error table says after initial checkout creation; see [[source-stripe-affirm-accept-payment]] before choosing a start point. `affirm_checkout_canceled` is a charge outcome reason that does not distinguish buyer cancellation from Affirm loan rejection, not an error code. Checkout's `payment_intent_data[shipping]` can improve loan acceptance, and the guide recommends fallback methods such as cards. Its Elements and Direct API manual-capture sections also conflict on seven-day/partial versus 30-day/full-only capture; the ten-minute uncaptured expiry is test mode only.

## Afterpay / Clearpay Details

**US rebrand (2026-05-06 capture)**: Afterpay → Cash App Afterpay; the older page says no integration changes are needed **unless custom Afterpay components are used**. UK name: Clearpay. The 2026-11-07 overview does not repeat the US notice.

**Coverage**: AU, CA, GB, NZ and US merchants and customers. General availability is domestic only; the 2026-11-07 overview lists cross-border transactions in private preview. Dynamic Checkout/Payment Element eligibility uses shipping country then geocoded client IP; manually listed payment methods require merchant-side eligibility filtering. Pay in 4 maxima: AU AUD 4k, CA CAD 2k, NZ NZD 4k, GB GBP 1.2k, US USD 2k; US monthly installments reach USD 4k.

**US tiers**: Pay in 4 ($1–$399.99), Pay in 4 + monthly ($400–$2k), monthly only ($2k.01–$4k). All other markets: Pay in 4 only.

**Disputes**: one full dispute per payment, within 120 days of purchase; 14 calendar days from dispute creation for merchant evidence. The 2026-11-07 page says the final decision comes within 30 calendar days **of dispute creation**; the 2026-05-06 page says **of evidence submission**. Stripe withholds the amount, returning it on a merchant win and making the charge permanent on a loss. Afterpay covers customer fraud or installment nonpayment losses, subject to shipment stop/pause requests.

**Refunds**: full or partial submission within 120 days; asynchronous completion can take up to 10 business days and refunds cannot be canceled. Check Refund `status` and `refund.updated`/`refund.failed`; a failed amount returns to the Stripe balance and requires another customer refund method. Submission is not success.

**Eligibility**: B2C is supported, B2B is not. The 2026-11-07 short prohibited list names alcohol, donations, pre-orders and NFTs, plus B2B; its MCC table separately distinguishes prohibited from restricted categories. The 2026-05-06 short list also named bars/lounges. Omission in November does not establish permission; check the full MCC list and terms.

**Integration notes (2026-05-06 guide)**: After redirect, a `requires_action` Afterpay PaymentIntent with no customer action for 3 hours detaches its PaymentMethod and returns to `requires_payment_method`; the guide's separate `payment_intent_payment_attempt_expired` entry uses 3 hours after initial checkout creation for an unsuccessful authorization. In its legacy server-managed Direct API redirect, `payment_method_data.billing_details` and `return_url` are required; shipping is optional but recommended for authentication. The old Elements Payment Intents manual-capture section says 7 days, while legacy Direct API/mobile sections say 13 days and describe refund of the first installment if uncaptured. These variant-specific old statements conflict; the 2026-11-07 variant index does not resolve current timing. See [[source-stripe-afterpay-clearpay-accept-payment]].

## Alma Details

**Coverage and timing**: The 2026-11-07 Alma overview lists BE, ES, FR, IT, LU and NL for merchant and customer location, B2C domestic EUR transactions of 50–5,000 EUR, and interest-free Pay in 2, 3 or 4 (the first installment may be higher). Its property matrix says immediate confirmation, instant provisional access and settlement up to three business days (T+3), while the 2026-05-06 page labeled T+3 as payout timing. Upfront funds language does not prove instant settlement or actual payout arrival. See [[source-stripe-alma]].

**Refunds**: 180-day window; async (up to 5 min).

**Disputes and fraud**: Customers have 120 calendar days to file; merchants have 14 calendar days to submit evidence; Alma decides within 25 calendar days after submission. The 2026-11-07 overview says dispute fees are nonrefundable regardless of outcome. Alma covers losses from customer fraud, but may request that a merchant stop or pause shipment; rising fraud/dispute rates may cost access. A filing or evidence submission does not establish a winning decision. See [[source-stripe-alma]].

**Connect**: Alma is for eligible online marketplaces (for example Deliveroo or ManoMano), not platforms that only onboard other businesses to accept payments directly (for example Shopify). Marketplace onboarding requires a Dashboard request. The 2026-11-07 account-type and Connect charge checkmarks do not remove this same-page business-model restriction. See [[source-stripe-alma]].

**Prohibited**: sole proprietorships, B2B, education, professional services, transportation, travel, telecom/utilities, veterinary.

**Required customer terms**: merchants must add 4 clauses to general terms of sale (Alma T&Cs, non-approval may cancel purchase, 14-day withdrawal right).

**Integration notes (2026-05-06 guide)**: For an Alma PaymentIntent in `requires_action`, if the customer takes no action within one hour after redirect to Alma, its PaymentMethod is detached and the Intent transitions to `requires_payment_method`. The old Elements desktop flow uses a QR code (one-hour authentication session; up to 20 refreshes). A `return_url` is required when confirming an Alma PaymentIntent; the old hosted Checkout example instead uses `success_url`, while embedded Checkout uses `return_url`. The seven-day capture window applies when `capture_method: manual` is used. Old iOS/Android dynamic-method USD examples conflict with the guide's EUR-only Alma tables/error and do not establish USD Alma eligibility. See [[source-stripe-alma-accept-payment]].

## Billie Details

**B2B only** — Pay in 30 days. The November 2026 Billie overview lists 11 merchant/customer countries and EUR, SEK, NOK, DKK, GBP and CHF presentment, domestic rather than cross-border coverage, a 0.01 EUR minimum, and maxima varying by country/currency. The May Billie page stated the minimum but no maximum; that omission did not mean unlimited amounts.

**Line items**: the May Billie get-started section recommended `line_items` to improve approval rates and described early access. The November overview's omission does not establish removal.

**Disputes**: November gives customers 365 days from purchase to file, merchants 35 calendar days from dispute creation for evidence, and Billie seven calendar days after submission for a decision. May required evidence within 12 calendar days and gave fraud, double-payment and amount-discrepancy examples; the older 'shortest' comparison is unverified for November.

**Refunds**: November requires submission within 365 days of original payment, versus May's 180-day limit. Full/partial refunds are asynchronous, up to five minutes; the November page says they cannot be canceled. Track final `refund.updated`/`refund.failed` status rather than treating submission as completion.

**Connect**: `billie_payments` capability must be active on the platform and enabled connected accounts. Descriptor source depends on charge type: direct and `on_behalf_of` use the connected account; destination and separate-charge-and-transfer use the platform absent `on_behalf_of`.

**Category eligibility**: November lists prohibited MCCs, including gambling, adult content, financial institutions, crypto, construction, car rental, real-estate rental and tax payments; restricted categories might require more account information. Consult the full dated table before a merchant-specific decision.

**Integration notes (May 2026 guide)**: Payment terms 7–120 days (not just 30). Hosted Checkout's example uses `success_url`; Checkout Sessions with Elements examples use `return_url`, and PaymentIntent redirect confirmation provides `return_url`. Optional PaymentIntent manual capture has a 7-day window. Early-access Unified `line_items` data is recommended to improve approval rates. See [[source-stripe-billie-accept-payment]] for path details and the November 2026 navigation-only index.

## Kriya Details

**B2B only** — UK only, GBP only. Its May method-specific capture says **Connect No**, as do May Mondu, SeQura, and Scalapay captures. Both overview product tables mark Connect Supported for all eleven methods; the scope conflict remains unresolved. See [[source-stripe-bnpl-overview]].

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited** (~36 categories, most extensive of any BNPL): travel agencies, hotels, airlines, insurance, gambling, crypto, advertising, drugs, financial institutions, political/religious organizations, charities, and many more.

**Integration notes**: `return_url` required. Manual capture: 7-day window.

## Zip Details

**Consumer BNPL** — AU and US. AUD/USD. **Connect supported**. **No manual capture**.

**Three products**: Zip Pay (AU, up to $1k AUD, flexible repayment), Zip Money (AU, $1k-$50k AUD, up to 36-month interest-free), Zip Pay In 4 (US, $35-$1.5k USD, 4 installments over 6 weeks).

**Disputes**: 180-day customer window. Unique: customer must contact merchant first — **14-day direct resolution** before escalating to Zip. Zip covers fraud losses.

**Refunds**: 180-day window.

**Additional requirements**: delivery within 60 days; retain records 18 months; no surcharging. US: goods must be in US; no gift cards.

**Integration notes**: `return_url` required. No manual capture. Checkout recommended — Direct API uses `stripe.confirmZipPayment()` which is **deprecated** (Stripe may end support).

## Sunbit Details

**Consumer BNPL** — US only, USD only. Pay in 3, 6, 12, or 18 monthly installments. **Connect supported** (`sunbit_payments` capability). **No manual capture**.

**Transaction limits**: min $60, max ~$20,000.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited categories**: ~175 (general retail, services, digital goods, restaurants, travel, healthcare — very broad).

**Additional requirements**: no surcharging; financed amount ≤ price of goods delivered.

**Integration notes**: `return_url` required. No manual capture. $60–$20k enforced in Checkout Session.

## SeQura Details

**Consumer BNPL** — Spain (ES) only, EUR only. Pay in 3 interest-free or up to 12 installments. **No Connect support**.

**Transaction limits**: min €29. No stated maximum.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited categories**: ~160+ categories — the most extensive prohibited list of any payment method on Stripe. Includes restaurants, doctors, legal services, marketplaces, digital goods, bakeries, and many everyday categories.

**Integration notes**: Payment terms 7–120 days (flexible, not fixed installments). `return_url` required. Manual capture: 7-day window.

## Scalapay Details

**Consumer BNPL** — Pay in 3 or 4 installments. **EUR only** across all 28 merchant countries (including US, AU, CA, SG). **No Connect support**.

**Transaction limits**: min €5, max ~€5,000.

**Allowed categories**: "At discretion of Scalapay" — no published list; approval-based (vs other B2B BNPL's long prohibited lists).

**Disputes**: 12-day evidence window.

**Refunds**: **90-day** window (shorter than Billie/Kriya/Mondu's 180 days); async (up to 5 min).

**Integration notes**: `return_url` required. Manual capture: 7-day window. Checkout path limited to 8 EU countries (IT, FR, ES, DE, NL, BE, IE, FI) despite 28-country merchant base.

## Payment on Invoice Details

**Consumer BNPL for Germany/Austria** (not B2B). EUR only. DE merchant accounts only.

**14-day customer payment terms** — Stripe sends branded invoice to customer after approval. Merchant paid immediately (immediate notification).

**Risk-based approval**: buyer provides name, email, address, date of birth; risk assessment determines approval.

**Payout timing**: T+2 minimum. Connect: Yes. Manual capture: Yes.

## Mondu Details

**B2B only** — Pay in 30 days. EU/UK, 14 merchant countries. Multi-currency: EUR, CHF, GBP. **No Connect support**.

**Maximum**: ~€20,000 EUR. No stated minimum.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited** (~90 categories, most extensive of any payment method): transportation, cleaning/repair services, gambling, healthcare, government services, chemicals, fuel, utilities, crypto, pawn shops, timeshares, and many more.

**Integration notes**: `return_url` required. Manual capture: 7-day window. EUR only for Checkout integration path.

## Klarna Details

**Coverage**: 23 customer countries, 32 merchant countries, 13 currencies. Broadest BNPL on Stripe. **Klarna takes loss liability** if customer can't repay.

**Klarna prohibitions (2026-11-07 Stripe capture):** besides Stripe-wide restrictions, the Klarna list includes charities, political organizations, business-to-business (written “BTB” in November; “B2B” in May), money/crypto services, stored value/gift cards, bailiff/insolvency/debt/fines/court/bail services, gambling/lotteries, direct marketing, and fundraising/crowdfunding. The May three-item list was narrower; spelling alone does not show a B2B policy change. Check the full linked terms and account eligibility.

**Marketing (dated Stripe guidance):** UK Klarna BNPL advertising must use Klarna-approved messaging; the page warns of criminal-charge risk for noncompliance. Stripe recommends PMME because it handles **Klarna brand compliance**, not all legal disclosures. The 2026-11-07 page says marketing Klarna **credit products to EU consumers** has additional CCD2 disclosure requirements beginning **2026-11-20**, using Klarna pre-approved copy and applicable country guidance. Treat the prospective legal statement as the captured page's claim, not independently verified law or a universal merchant obligation.

**Termination**: Klarna can terminate for prohibited categories or high dispute rates.

**AU DDO:** most Stripe users need do nothing. Australian businesses actively promoting or recommending Klarna Pay in 4 **might** be considered distributors and **might** have TMD-consistent promotion and significant-adverse-dealing notification duties; complaint/adverse-dealing reports or information are supplied **if requested**. Both dated captures state these conditions, not automatic distributor status for every promoter.

**4 payment options**: Pay in full, Pay later (30-day single payment), Pay in 3 or 4 (interest-free installments), and Financing (up to 36 months, possibly with interest and subject to creditworthiness). The May 2026 Financing list has AT/CA/DE/FI/GB/NO/SE/US; the November 2026 table additionally lists **Italy for one-time Financing at 35-3,000 EUR**. These dated tables do not establish any particular buyer's approval.

**Recurring payments**: Pay in full, Pay later and Pay in 3 or 4 have documented subscription use cases with country and plan limits. `setup_future_usage` classifies a Klarna payment as recurring and can limit the plans displayed, including otherwise eligible plans; it does not categorically prevent recurring Klarna. **November source conflict**: individual Pay later country rows list subscriptions beyond DE/SE/US, while the same page's all-country footnote and limitations say only Germany, Sweden and the US support Pay later subscriptions and on-demand payments. Do not infer expanded eligibility from those rows.

**Cross-border**: The EEA, UK and Switzerland business rows permit customers in the EEA, UK or Switzerland with presentment in the customer-location currency. The other-countries row requires the customer and business locations to match and presentment in the business-location currency; the table alone does not establish account eligibility.

**Refunds**: Up to 180 days after payment completion; usually 5-7 business days, possibly longer. Full and partial refunds are supported up to the original charge. When a partial refund exceeds the remaining order balance, Klarna reduces that balance and returns the difference; when it is less, Klarna reduces that balance and spreads refunds across remaining payments. Klarna does not support refunding a payment escalated to a dispute.

**Disputes**: Under the captured [[source-stripe-klarna-disputes]] guide, customers generally have 180 calendar days from capture to file, with stated exceptions. Almost all cases begin with a 21-day inquiry: the customer may withdraw it or the business may refund the full disputed amount without a fee; Klarna takes no evidence then. Only unresolved inquiries escalate to chargeback, though fraud and other exceptions can go directly to chargeback. At chargeback, Stripe withholds the disputed funds and fee; a win releases both. Evidence is due 12 days from escalation, or 5 days for fraud, and is limited to one round. `charge.dispute.funds_withdrawn` marks escalation. The guide's fee table says assessed when a dispute is created, while its inquiry and chargeback prose locates fee avoidance during inquiry and withholding at escalation; do not infer an inquiry-opening charge.

**Connect**: all charge types. `klarna_payments` capability for Express/Custom accounts.

**Integration notes (May 6, 2026 acceptance guide)**: In its Direct API PaymentIntent path, Stripe recommends `payment_method_data.billing_details` and shipping details to help acceptance and reduce disputes; its deferred-payment prefill example also passes `payment_method_data.klarna.dob`. This corrects the earlier `payment_method_options.klarna` prefill attribution for that example. Optional PaymentIntent manual capture has a 28-day authorization deadline, after which capture is unavailable. The guide's amount `3500` in local currency is a production-testing tip for options other than Financing, not an eligibility guarantee. See [[source-stripe-klarna-accept-payment]].

**Conversion tips**: Place Express Checkout Element early. Add Payment Method Messaging on product pages. Pass payment line items (Checkout does this automatically) and optional shipping/billing address to improve Klarna fraud scoring.

**Supplementary purchase data** (Klarna-only public preview; API header `2025-11-17.preview` or a later preview version): pass `payment_method_options.klarna.supplementary_purchase_data` on PaymentIntent create, update or confirm for events, standalone insurance, vouchers, train, bus, ferry, organized trips, or marketplace sellers. The data can support underwriting and fraud assessment, but authorization-rate improvement is possible and variable, not assured. It does not change Klarna fees; Stripe and Klarna provide no feedback on whether particular well-formed data qualifies for improved outcomes. See [[source-stripe-klarna-supplementary-data]] for replacement and removal semantics and dated examples.

**Recurring/save (2026-05-06 full guide)**: Checkout `mode: 'setup'` or a SetupIntent can save Klarna for later use, with a reusable PaymentMethod attached to a Customer and the billing agreement authorized. For a subscription, keep the same `reference` on future charges; when a line item supplies `subscription_reference`, a mismatch causes an error. Passing `payment_method_options.klarna.subscriptions` helps show applicable options, but Pay in 3/4 depends on subscription length, use case and buyer country. The on-demand charge example's `klarna.on_demand` details are optional underwriting information, not a guaranteed improvement; that example sets `off_session: false`. Confirm authorization through Intent status or webhooks before reuse, and handle Klarna-side `mandate.updated` revocation by detaching the PaymentMethod. See [[source-stripe-klarna-set-up-future-payments]]; its 2026-11-07 capture is navigation only.

## Affirm Repayment Options

Pay in 4 interest-free installments or monthly payments up to 36 months. Max credit limit $20k USD/CAD; transactions up to $30k require customer down payment.

## Integration

Use Dynamic Payment Methods (enabled by default) via Checkout, Payment Element, or hosted Invoice page. No individual integration required per method. **Payment Method Messaging Element** (PMME) recommended for on-site BNPL messaging — dynamically shows relevant options. The legacy `affirmMessage` Element (Affirm-only) is deprecated in the latest Stripe.js.

## Android SDK `23.18.0` Evidence

PaymentSheet release notes announce SeQura and Scalapay support. The retained payments-core API adds `PaymentMethod.Type.Sequra`/`Scalapay` and corresponding creation overloads. These are version-qualified announcements and declarations, not proof of enabled merchant access, Android form/redirect implementation or changed commercial terms. Existing provider-specific details above are not revalidated by this SDK capsule. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## Sources

- [[source-github-stripe-android]] - Android 23.18.0 SeQura/Scalapay declarations and PaymentSheet support announcements

- [[source-stripe-bnpl-overview]] — product/API/transaction support matrices for 11 BNPL methods
- [[source-stripe-affirm]] — Affirm overview captured May and November 2026: domestic US/CA plus GB private preview, financing, eligibility/MCC rules, dated refund and dispute timing conflict, product limits and May Connect detail
- [[source-stripe-affirm-accept-payment]] — May 2026 Affirm guide: four web/API variants, Checkout constraints, outcome and capture conflicts; November 2026 index: six variant links including iOS and Android navigation
- [[source-stripe-affirm-messaging]] — Legacy affirmMessage Element (deprecated); use Payment Method Messaging Element instead
- [[source-stripe-afterpay-clearpay]] — Afterpay/Clearpay overview: November 2026 eligibility, private-preview cross-border, payment options, refund/dispute states; dated May 2026 rebrand, Invoicing and dispute-clock conflicts
- [[source-stripe-afterpay-clearpay-accept-payment]] — Afterpay/Clearpay acceptance: 2026-05-06 detailed variant guide, three-hour inactive state transition, variant-specific capture-window conflict; 2026-11-07 index adds navigation routes only
- [[source-stripe-afterpay-clearpay-messaging]] — Legacy afterpayClearpayMessage Element (deprecated); auto-localizes to Clearpay for UK locale
- [[source-stripe-alma]] — Alma overview (2026-05-06 and 2026-11-07): B2C domestic EUR eligibility and MCC caveats; single-use 2/3/4 installments; May T+3 payout wording versus November up-to-T+3 settlement label; marketplace-only Connect, refund/dispute outcomes, and customer terms
- [[source-stripe-alma-accept-payment]] — 2026-05-06 Alma integration guide: five Checkout/Elements/Direct API/iOS/Android paths; Elements one-hour authentication and desktop QR (up to 20 refreshes); `return_url` when confirming an Alma PaymentIntent (hosted Checkout uses `success_url`, embedded Checkout uses `return_url`); seven-day manual-capture window. The 2026-11-07 capture is a variant index, not refreshed behavior.
- [[source-stripe-billie]] — May and November 2026 full B2B Billie overviews: dated refund/dispute windows, country/currency/MCC limits, Connect, and conflicts with the older BNPL matrix on setup_future_usage and Invoicing; November Billing/Invoicing entry has a send_invoice footnote with route-specific ambiguity
- [[source-stripe-billie-accept-payment]] — May 2026 Billie integration guide: 7–120 day terms, path-specific return destinations, optional 7-day PaymentIntent capture; November 2026 variant index is navigation only
- [[source-stripe-klarna]] — Klarna: 4 payment options, 23 countries, cross-border rules, loss liability, refund mechanics, Connect
- [[source-stripe-klarna-accept-payment]] — Klarna integration: billing prefill, manual capture, per-country test data (23 countries), iOS webview
- [[source-stripe-klarna-set-up-future-payments]] — 2026-05-06 full Klarna save/recurring guide: Customer attachment, authorization status, reference matching, optional on-demand details and revocation; 2026-11-07 capture is a variant index only
- [[source-stripe-klarna-best-practices]] — Klarna conversion: Express Checkout placement, PMME on product pages, line items, shipping/billing for fraud
- [[source-stripe-klarna-compliance]] — Klarna rules: expanded November 2026 prohibitions, dated UK and prospective EU consumer-credit marketing guidance, termination/merchant duties, conditional AU DDO distributor status
- [[source-stripe-klarna-disputes]] — Klarna disputes: capture-based 180-day filing window with exceptions; inquiry resolution, direct-chargeback exceptions, chargeback evidence and fee handling, API states, and capture-dated sandbox triggers
- [[source-stripe-klarna-supplementary-data]] — Klarna-only supplementary purchase data preview: eight verticals, possible acceptance and fraud-assessment benefits, PaymentIntent update semantics, and May/November 2026 example provenance
- [[source-stripe-kriya]] — Kriya: B2B UK-only, no Connect, most extensive prohibited list (~36 categories), 12-day dispute window
- [[source-stripe-kriya-accept-payment]] — Kriya integration: return_url required, 7-day manual capture
- [[source-stripe-mondu]] — Mondu: B2B Pay-in-30, 14 EU/UK countries, multi-currency, no Connect, ~90 prohibited categories
- [[source-stripe-mondu-accept-payment]] — Mondu integration: return_url required, 7-day manual capture, EUR-only Checkout path
- [[source-stripe-payment-on-invoice]] — Payment on invoice: consumer BNPL DE/AT, 14-day terms, risk-based, branded invoice, T+2 payout
- [[source-stripe-scalapay]] — Scalapay: consumer BNPL, EUR-only (all 28 countries), 90-day refund window, approval-based categories
- [[source-stripe-scalapay-accept-payment]] — Scalapay integration: return_url required, 7-day capture, Checkout limited to 8 EU countries
- [[source-stripe-sequra]] — SeQura: consumer BNPL Spain-only, Pay in 3/12, most extensive prohibited list (~160+ categories)
- [[source-stripe-sequra-accept-payment]] — SeQura integration: 7-120 day terms, return_url required, 7-day manual capture
- [[source-stripe-sunbit]] — Sunbit: US-only, 3/6/12/18-month installments, Connect supported, no manual capture, $60-$20k
- [[source-stripe-sunbit-accept-payment]] — Sunbit integration: return_url required, no manual capture, $60-$20k Checkout enforcement
- [[source-stripe-zip]] — Zip: AU+US, 3 products (Zip Pay/Money/Pay-in-4), 14-day direct resolution, 180-day disputes/refunds
- [[source-stripe-zip-accept-payment]] — Zip integration: return_url required, no manual capture, Direct API deprecated (confirmZipPayment)
