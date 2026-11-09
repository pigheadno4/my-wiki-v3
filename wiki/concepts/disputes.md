---
title: "Disputes & Chargebacks"
type: concept
category: framework
tags: [disputes, chargebacks, resolution-center, fraud, consumer-protection]
---

## Definition

A **dispute** occurs when a buyer challenges a transaction — typically because goods were not received, were not as described, or the transaction was unauthorized. A **chargeback** is a specific type of dispute filed through the buyer's bank or card issuer (rather than directly with the merchant or payment platform), resulting in a forced reversal of the charge.

## How Disputes Work

### Direct (Platform) Disputes

- Buyer files in the payment platform's resolution center (e.g., PayPal Resolution Center)
- Seller has opportunity to respond with evidence
- Platform adjudicates; buyer refunded if dispute upheld

### Chargebacks (Bank/Card Issuer)

- Buyer disputes with their bank or card issuer
- Bank initiates reversal; payment platform creates corresponding dispute record
- Seller responds via platform; bank/card network makes final decision
- Merchant typically charged a chargeback fee regardless of outcome

> [!warning] Account-specific fee-outcome qualification
> Provider and account terms qualify chargeback-fee outcomes. In the captured Braintree NAB article, a bank ruling in the merchant's favor credits the transaction amount back and does not charge a fee, while losing or accepting returns the disputed amount to the cardholder and incurs a chargeback fee. [[source-braintree-articles-nab-chargebacks-retrievals-prearbs]]

## Common Dispute Reasons

- Item not received (INR)
- Item significantly not as described (SNAD)
- Unauthorized transaction / fraud
- Billing issue (duplicate charge, wrong amount)

## Common Fraud Types

| Type | Description |
| --- | --- |
| Stolen cards | Stolen card/details used online; if the issuer dispute is resolved for the cardholder, the business loses the payment amount and goods or services already supplied and is subject to a dispute fee |
| Overpayment fraud | Stolen card + fake third-party; business pays out then faces dispute |
| Card testing | Validating stolen cards on low-friction sites (donations, PWYL) |
| Alternative refunds | Overpay → request refund via different channel — **never refund differently** |
| Marketplace fraud | Fraudulent seller on Connect platform; platform bears unrecoverable liability |
| Friendly fraud | Legitimate cardholder disputes own purchase; Visa CE 3.0 challenges this |

**Key rule**: partially refunded payments can still be disputed for the full original amount. See [[source-stripe-disputes-fraud-types]].

**Card testing** (carding/enumeration): validating stolen cards via Card Setup or small Payments. Identify by spike in failed payments / 402 errors / small suspicious payments. Prevention: use Payment Element or Checkout (automated CAPTCHA+AI); add CAPTCHA, login requirement, rate limits (limit cards/customers per IP); plan-supported Radar velocity rules. Single heuristic insufficient. See [[source-stripe-disputes-card-testing]].

**Fraud identification indicators**: false/scripted communication (search phrase in quotes), same card+different shipping, many cards+same shipping, rush orders, "preferred shipper" requests (red flag), overcharge+pay-third-party, post-order address change. Donations: a large-donation request to "refund the difference" can be a suspected stolen-card credit-limit test; Stripe says a full refund might be prudent in that scenario, not an automatic requirement or proof of fraud. See [[source-stripe-disputes-identifying-fraud]].

**Fraud prevention best practices** (3 tiers):

- *Everyone*: Stripe recommends showing the full terms and policy at checkout or in a popup and says businesses can require agreement; a link-only checkbox might be rejected as insufficient issuer evidence. Use tracking screenshots, a clear descriptor, distinct accounts per business, and conditional refund/shipping-delay strategies. Shipping to an AVS-verified billing address is described as safest, while a different destination is allowed with risk mitigation and order review.
- *Radar users*: manual review is available if the account plan supports it; reviewed payments are normally processed and charged unless authorization and capture are separated. Rules can use country and card attributes; manual capture in review also depends on plan support.
- *Developers*: Stripe processing and complete customer/transaction data help it identify qualifying Visa CE 3.0 history but do not by themselves establish eligibility or a dispute win. 3D Secure-authenticated payments might receive liability-shift protection from most fraudulent disputes, while EFWs can still count toward monitoring. Identity verification adds customer friction; uncaptured card authorizations cannot be disputed, whereas captured payments can. See [[source-stripe-disputes-prevention-best-practices]] (https://docs.stripe.com/disputes/prevention/best-practices; May `raw/stripe-disputes-prevention-best-practices-2026.md:18-24,66-90,121-159`; November `raw/stripe-disputes-prevention-best-practices-2026-11-07.md:19-25,67-91,122-160`).

See [[source-stripe-disputes-prevention-best-practices]].

**Customer abuse** (policy exploitation — not payment fraud): **Refund abuse** (Sigma query by refund frequency; notify/restrict/fee); **Resale abuse** (account sharing: OTP friction on geo-dispersed IPs; account transfers: velocity rules on same card+promo across accounts); **Trial abuse**: Radar trial abuse control. See [[source-stripe-disputes-customer-abuse]].

**CVC and AVS verification**: Stripe recommends collecting CVC, postal code, and billing street address to enable applicable issuer checks; wallets such as Apple Pay and off-session payments do not require CVC. A configured Radar rule can block a **failed** CVC or postal code check in specified situations, but the failed-CVC rule does not affect a payment when that check cannot run or is unavailable. CVC is less likely to be obtained through a computer breach because businesses cannot store it, but it does not protect against physical card theft or insecure computers/websites. AVS support varies by country and issuer, and legitimate address errors or moves can cause failures; most US, Canadian, and UK cards support street address checks. A check result alone does not guarantee authorization or a dispute outcome. See [[source-stripe-disputes-verification]].

## Stripe Dispute Categories

The eight-category framework in [[source-stripe-disputes-categories]] maps reason codes for the listed Visa, Mastercard, Amex, Discover, Klarna, PayPal, and Cash App Pay methods; categories vary by method. Visa additionally has a `noncompliant` mapping for certain Visa compliance disputes.

> [!warning] Category scope across guides and captures
> The 2026-05-09 categories guide introduces eight categories broadly, while [[source-stripe-disputes-reason-codes]] broadly says local payment method codes map to seven card-dispute categories. The 2026-11-07 categories capture explicitly excepts Instant Bank Payments from its eight-category framework: every dispute has reason `debit_not_authorized`, with an underlying ACH return network code (R10, R07, R08, R11, R29, R05, or R31). Do not infer a card-category mapping or card-network reason code for Instant Bank Payments. Use its mapping in [[source-stripe-disputes-categories]]; the linked Instant Bank Payments evidence guide was not read here, so no response requirements are inferred from it.

| Category | Claim type |
| --- | --- |
| `credit_not_processed` | Entitled to refund but not received |
| `duplicate` | Duplicate charge or paid by other means |
| `fraudulent` | Unauthorized transaction |
| `general` | Auth issues, technical errors, other |
| `product_not_received` | Goods/services not delivered |
| `product_unacceptable` | Not as described, defective, counterfeit |
| `subscription_canceled` | Recurring billing after cancellation |
| `unrecognized` | Cardholder doesn't recognize the charge |
| `noncompliant` | Visa network rule violation (Visa only, C0xx codes) |

Evidence requirements differ by **product type**: physical (shipping proof), digital (usage/login logs), offline service (cancellation policy key). See [[source-stripe-disputes-categories]] for full evidence field reference and per-category prevention guidance.

**Customer-contact evidence**: Several category tables ask whether the customer contacted the business before filing and say to state when they did not. Selected Visa reason-code examples discuss prior contact, while Mastercard examples request communications if contact occurred. Neither [[source-stripe-disputes-categories]] nor [[source-stripe-disputes-reason-codes]] establishes a universal prior-contact obligation or makes absent contact dispositive; submit relevant records when they exist and fit the claim.

**Fraudulent evidence by environment**:

- Card-present: EMV data, signed receipt, surveillance, POS logs
- Card-not-present: 3DS proof, AVS/CVV match, device/IP data, prior purchase history

See [[source-stripe-disputes-reason-codes]] for per-code evidence guidance (Visa, Mastercard, Amex).
See [[source-stripe-disputes-visual-evidence]] for seven categories of illustrative, non-exhaustive evidence packets. **Credit not processed** and **Duplicate** have explicit Approved and Denied example sections; the other categories offer category-specific counter-evidence examples. Each captured Markdown page has 66 image references to 64 distinct paths; the May capture uses local saved assets and the November capture uses remote Stripe CDN URLs. These examples do not show actual issuer outcomes or guarantee a win.

### Stripe Evidence Best Practices

- **Win likelihood**: November 2026 page names Radar Plus; 1–5 dots estimate expected win percentages of 5%, 15%, 25%, 40%, and 60% after relevant evidence, subject to eligibility and without an outcome guarantee.
- **File limits**: PDF/JPEG/PNG; combined files no more than 4.5 MB; formatting list says <50 pages, while the applicable page limit varies by dispute. One file per evidence type. An API evidence update exceeding the compiled-PDF limit returns HTTP 400 and `dispute_evidence_page_limit_exceeded` even with `submit=false`; handle `error.code`, reduce evidence, and retry.
- **Authorization**: for fraudulent disputes, include relevant AVS/CVC, IP and 3DS evidence; Stripe includes available AVS/CVC results and purchase IP if the integration supplies it.
- **Accepting disputes**: fee still applies; disputes received count toward dispute activity regardless of outcome.
- **Partially refunded**: respond with refund amount and date; issuer commonly cancels and recreates the dispute for the corrected amount, subject to the Cartes Bancaires contesting limitation.

> [!warning] Contradiction across dated captures
> The May 2026 page separately stated a 19-page Mastercard maximum. The November best-practices page does not state that figure and instead describes a dispute-specific applicable limit. Its omission does not prove repeal or continued validity of 19 pages; the <50-page formatting rule alone is not an acceptance guarantee.

See [[source-stripe-disputes-best-practices]] for full guidance including auto-populated API evidence fields and Visa CE 3.0 details.

### Stripe Disputes API

| Operation | Method |
| --- | --- |
| Retrieve dispute | `stripe.disputes.retrieve(id)` |
| Update a Dispute with evidence | `stripe.disputes.update(id, { evidence: {...} })` in the May 2026 Node example; November shows the same operation in curl |
| List by PaymentIntent | `stripe.disputes.list({ payment_intent: id })` |
| List by Charge | `stripe.disputes.list({ charge: id })` |

Evidence fields: text-based (strings) or file-based (`file_upload` object ID from File Upload API with `purpose: "dispute_evidence"`). Text limit: 150,000 combined characters. The May/November API guides also name `uncategorized_text` and `uncategorized_file` for catch-all evidence; use specific fields where possible. Deadline in `evidence_details.due_by`. See [[source-stripe-disputes-api]].

The November 7, 2026 guide adds `charge.dispute.created`. A Dispute exposes a Charge reference and nullable PaymentIntent reference, with no direct invoice or subscription reference. For an associated subscription, follow its linked subscription webhook procedure and that procedure's version/null-ID conditions; a payment filter alone is not a subscription lookup. Evidence updates, event delivery and these references do not establish acceptance, cancellation, a won case or settlement.

### Visa CE 3.0 API Details

Eligibility: Visa 10.4 disputes + 2 prior undisputed transactions (same payment method, 120–364 days prior, paid, not validation charges) + product descriptions for all 3 + `merchandise_or_services` field + matching 2 main OR 1 main + 1 secondary evidence elements across all transactions.

CE 3.0 status (`evidence_details.enhanced_eligibility.visa_compelling_evidence_3.status`): `requires_action` → check `required_actions[]`; `qualified` → ready; `not_qualified` → fallback to standard submission. **Also fill standard `evidence` object as fallback.**

Test card: `4000000404000038` / `pm_card_createCe3EligibleDispute`. See [[source-stripe-disputes-visa-ce3]].

### Visa Compliance Disputes (API)

Identify via: `payment_method_details.card.case_type = "compliance"`, `enhanced_eligibility_types` contains `"visa_compliance"`, or `reason = "noncompliant"`.

Two options: **close** (acknowledges loss, avoids this Visa compliance network fee, irreversible) or **respond** (must set `evidence.enhanced_evidence.visa_compliance.fee_acknowledged: true` — otherwise Stripe rejects evidence; contesting incurs a 500 USD or local-equivalent Visa network fee in addition to applicable Stripe dispute fees, withdrawn asynchronously after submission, typically within 1–2 days, and refunded if won). The `fee_acknowledged` status records acknowledgment, not a won dispute. See [[source-stripe-disputes-visa-compliance]] for the 2026-05-10 and 2026-11-07 guide captures.

Test card: `4000008400000779` / `pm_card_createComplianceDispute`. See [[source-stripe-disputes-visa-compliance]].

### Dispute Withdrawals

Withdrawn ≠ won — a cardholder's request to the issuer does not itself close the chargeback or return funds. To seek a win, submit evidence by the deadline or the issuer may treat silence as liability. Withdrawn disputes still count against dispute rate and do not resolve faster; only financial chargebacks can be fully withdrawn (not EFWs or inquiries). A refund on the disputed charge stays blocked until the issuer decides for the merchant. All card networks permit late withdrawal requests, even post-loss, but a particular issuer may not support one; the issuer might take weeks or months to process an adjustment, while the date it appears in Stripe is hard to predict. See [[source-stripe-disputes-withdrawals]].

## Merchant Implications

- Dispute management requires seller response within time windows
- Chargeback fees typically $15–$20+ per dispute (platform/card-network dependent)
- High chargeback rates (>1% of transactions) risk account termination or increased processing fees
- Evidence types: tracking numbers, delivery confirmation, communication records, invoices

## Measuring Disputes (Stripe)

| Metric | By | Purpose |
| --- | --- | --- |
| Dispute activity | Dispute date | Used by card network monitoring programs |
| Dispute rate | Charge date | Fraud analysis; identifies problematic payments |

The May and November 2026 [[source-stripe-disputes-measuring]] captures define both metrics over successful payments: dispute activity cohorts disputes by receipt date, while dispute rate cohorts disputed payments by their original charge date (https://docs.stripe.com/disputes/measuring; May `raw/stripe-disputes-measuring-2026.md:8-18`; November `raw/stripe-disputes-measuring-2026-11-07.md:9-19`).

Stripe's May and November 2026 measuring guide calls >0.75% dispute activity excessive as an industry standard, while a sudden spike or steep upward trend can trigger monitoring earlier; network-set thresholds exceeded for a prolonged period may lead to fines. All disputes, won or lost, count in the guide's monitoring discussion. Charge-date dispute rate can change for dates under 120 days old, and cardholders can sometimes dispute later, so day 120 is no guaranteed finality boundary. Issuer-generated EFWs on Visa, Mastercard, and JCB are a separate suspected-fraud signal; Visa counts them toward VAMP identification. See [[source-stripe-disputes-measuring]] (https://docs.stripe.com/disputes/measuring; May `raw/stripe-disputes-measuring-2026.md:22,29,34-49`; November `raw/stripe-disputes-measuring-2026-11-07.md:23,30,35-50`).

### Stripe Dispute Prevention Tools

| Tool | How it works | Rate impact |
| --- | --- | --- |
| **Resolution** (Radar rules) | Auto-refund specific disputes via custom rules | Resolved disputes don't count toward rate; no dispute received fee |
| **Deflection** (Visa Order Insights / Verifi; Mastercard Consumer Clarity / Ethoca) | Sends available charge details for issuer/cardholder recognition lookups | Can reduce filings when details help recognition; Visa OI with qualifying CE 3.0 prior-transaction data requires an issuer block |
| **Smart Disputes** | AI builds + submits evidence automatically for eligible disputes | Handles disputes that get through prevention; **Smart Disputes fee only on wins; other dispute fees are separate** |

RDR and Ethoca Alerts need no separate product integration, but resolution onboarding requires Radar rules to define refunds. Dashboard onboarding collects business details for Visa OI and Mastercard CC lookups; useful transaction-time data supports deflection. See [[source-stripe-disputes-prevention]] and [[source-stripe-disputes-prevention-how-it-works]].

**Smart Disputes API**: set `intended_submission_method: "prefer_smart_disputes"` on dispute update to merge your evidence with AI-generated evidence. Check `smart_disputes.status` (`available` / `requires_evidence` / `unavailable`) and `smart_disputes.recommended_evidence` array for what to add. See [[source-stripe-smart-disputes-setup]].

**Auto-respond config**: toggle at Dashboard → Settings → Disputes. For Connect platforms: control per connected account via `accounts.update({ settings: { smart_disputes: { auto_respond: { preference: 'on'|'off'|'inherit' } } } })`. `inherit` immediately tracks platform default; explicit override is sticky until reset. See [[source-stripe-smart-disputes-auto-respond]].

**RDR limitation**: only resolves full-amount disputes on non-refunded transactions.

**CE 3.0 pre-dispute block (Visa OI, 10.4 card-absent fraud)**: if at least two prior non-fraud transactions with the cardholder have complete product descriptions and matching IP addresses plus a matching email address or customer delivery address, the issuer **must block filing** (no dispute fees or rate impact). Stripe advises providing IP address, customer email, and product descriptions broadly at transaction time, plus shipping or customer address where possible, to improve the chance that qualifying prior data is available; this is guidance, not a universal lookup prerequisite. See [[source-stripe-disputes-prevention-how-it-works]].

## PayPal Implementation

PayPal provides two paths for dispute management:

1. **PayPal Resolution Center** (manual) — web UI for sellers to view and respond to disputes
2. **Disputes API** (automated) — programmatic access to list, respond to, provide evidence, escalate, accept, or appeal disputes

The exact REST-contract baseline at `90e8041` defines 15 Disputes 1.11 operations: list/get/patch plus evidence, appeal, accept, adjudicate, require-evidence, escalate, message, offer, return acknowledgement, and supporting-information actions. This contract inventory is broader than older guide summaries that counted only selected actions. See [[source-github-paypal-rest-api-specifications]].

### Internal vs External disputes

| Type | Filed via | Adjudicated by | Notes |
| --- | --- | --- | --- |
| Internal | PayPal Resolution Center (or chatbot/IVR) | PayPal | INR + SNAD start at INQUIRY; billing errors/unauthorized go directly to CHARGEBACK |
| External | Buyer's bank or card issuer | Bank / card network | PayPal acts as intermediary only |

**Pre-chargeback alert**: merchant has **20 hours** to issue a refund to avoid the chargeback and associated fees.

**ACH return**: distinct from card chargeback — bank requests PayPal to reverse a payment.

### Dispute lifecycle stages (API)

> [!warning] `CHARGEBACK` stage ≠ card chargeback
> In the Disputes API, `dispute_life_cycle_stage: CHARGEBACK` means PayPal has taken over adjudication of an escalated internal claim. It is NOT a credit/debit card chargeback. Always check `dispute_channel` (INTERNAL vs EXTERNAL) alongside the stage.

| Stage | Meaning |
| --- | --- |
| `INQUIRY` | Pre-claim; INR/SNAD only; 20-day window; internal disputes only; opt-out available via account manager |
| `CHARGEBACK` | Escalated claim; PayPal adjudicates; merchant can accept/contest/offer |
| `PRE_ARBITRATION` | First merchant appeal |
| `ARBITRATION` | Second appeal; card network adjudicates external cases |

**Status transitions** triggered by specific events:

| Trigger | Resulting status |
| --- | --- |
| Buyer files dispute | `OPEN` |
| PayPal notifies merchant | `WAITING_FOR_SELLER_RESPONSE` |
| Merchant submits evidence/offer | `WAITING_FOR_BUYER_RESPONSE` |
| Escalation or deadline missed | `UNDER_REVIEW` |
| PayPal adjudicates | `RESOLVED` |

**Key rule**: missing `seller_response_due_date` auto-closes in buyer's favor.

### Key time windows

- **180 days**: buyer window to file a dispute from payment date
- **20 days**: amicable resolution window (INQUIRY stage)
- **10 days**: PayPal adjudicates after escalation to claim
- **20 hours**: pre-chargeback alert window to refund and avoid chargeback fees
- **30 days**: unclaimed payouts auto-returned (separate from disputes)

### API actions by stage × status

| Stage | Status | Available actions |
| --- | --- | --- |
| INQUIRY | WAITING_FOR_SELLER_RESPONSE | send-message, make-offer, accept-claim, escalate, provide-evidence, acknowledge-returned-item |
| CHARGEBACK/PRE_ARB/ARB | WAITING_FOR_SELLER_RESPONSE | provide-evidence, accept-claim, make-offer, appeal (if lost) |
| CHARGEBACK/PRE_ARB/ARB | UNDER_REVIEW | provide-supporting-info only |
| Any | WAITING_FOR_BUYER_RESPONSE or RESOLVED | None |

Use HATEOAS `links[]` in the show-dispute response — it lists exactly which actions are valid at that moment.

### `allowed_response_options` — offer types

- `make_offer.offer_types`: REFUND, REFUND_WITH_RETURN, REFUND_WITH_REPLACEMENT, REPLACEMENT_WITHOUT_REFUND
- `accept_claim.accept_claim_types`: REFUND, PARTIAL_REFUND, REFUND_WITH_RETURN, REFUND_WITH_RETURN_SHIPMENT_LABEL
- `acknowledge_return_item.acknowledgement_types`: ITEM_RECEIVED, ITEM_NOT_RECEIVED, DAMAGED, EMPTY_PACKAGE_OR_DIFFERENT, MISSING_ITEMS

### Evidence types and file constraints

| Evidence type | What to provide |
| --- | --- |
| `PROOF_OF_FULFILLMENT` | Tracking info (`carrier_name` + `tracking_number`) OR delivery document |
| `PROOF_OF_REFUND` | `refund_ids` array |
| `OTHER` | Notes or documents |

**File constraints**: `.jpg`, `.jpeg`, `.gif`, `.png`, `.pdf` — max **10 MB per file**, **50 MB total per API call**

### 9 dispute reasons

MERCHANDISE_OR_SERVICE_NOT_RECEIVED, MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED, UNAUTHORISED, CREDIT_NOT_PROCESSED, DUPLICATE_TRANSACTION, INCORRECT_AMOUNT, PAYMENT_BY_OTHER_MEANS, CANCELED_RECURRING_BILLING, OTHER

### Accelerated Response (rolling out)

Merchant submits docs within 10 days of inquiry start. Post-escalation window: 3 days if buyer escalates after day 10 with message/offer sent, otherwise no additional time (case closed in buyer's favor).

### Sandbox-only endpoints

- `POST /v1/customer/disputes` — create dispute as buyer
- `POST /v2/customer-support/process-chargeback` — create chargeback
- `POST /v1/customer/disputes/{id}/change-reason` — change dispute reason

See [[source-paypal-disputes-api]] for full endpoint reference, test values, and webhook event details.
See [[source-paypal-disputes-overview]] for setup guide, Resolution Center actions, and workflow diagrams.

PayPal also offers [[paypal-fraud-risk]] products (Chargeback Protection, Fraud Protection Advanced) that can automatically absorb or manage chargeback liability.

## Stripe Implementation

### Pre-Dispute Phase

**Early Fraud Warnings (EFWs)**: Visa TC40 + Mastercard SAFE reports usually signal suspected fraud before a dispute, but an EFW can arrive even after a fraud dispute because network reporting and dispute systems are separate and can be out of sync. Stripe's 2026-11-07 guide estimates that about 40% of **unrefunded Visa and Mastercard** EFWs become fraud disputes, varying by network and payment amount; its 2026-05-09 guide gave an older 80% estimate for ignored EFWs without liability shift. With 3DS liability shift, a dispute can still occur and Stripe says it auto-provides some evidence. Stripe's refund heuristic is for charges roughly at or below the dispute fee; a reversal usually within two hours of capture can prevent the fraud report itself, not guarantee prevention of a later dispute. See [[source-stripe-disputes-how-disputes-work]].

**Inquiries**: Preliminary issuer requests, most often for AmEx and Discover (the guide says Mastercard/Visa no longer use them); Mexico Domestic disputed charges across brands also use them. Satisfactory evidence or a full refund can resolve an inquiry without a dispute fee. An unanswered inquiry can escalate to a likely unwinnable chargeback. API statuses include `warning_needs_response` and `warning_under_review`; `warning_closed` applies after 120 days open without chargeback escalation and is not an issuer win message. See [[source-stripe-disputes-how-disputes-work]].

### Dispute Lifecycle

1. Card network debits Stripe; Stripe debits merchant (disputed amount + fee)
2. Refunds blocked while dispute is open
3. Merchant submits evidence within 7–21 days (varies by network)
4. Issuer reviews: 60–75 days. Full lifecycle: 2–3 months

**Dispute status**: `won` (funds returned) or `lost` (no movement — funds already with issuer). `late win` is rare but possible.

### Dispute Fees (Stripe)

- **Dispute received fee**: generally nonrefundable outside Mexico unless the Stripe contract says otherwise; in Mexico it might be returned if the merchant wins or the cardholder withdraws. No received fee applies to card payments processed on Cartes Bancaires for SEPA businesses. See [[source-stripe-disputes-how-disputes-work]].
- **Dispute countered fee**: charged when evidence submitted; refunded if won; not in Mexico/Japan

### Unchallengeable Disputes (Stripe)

Immediately closed as lost, no evidence allowed:

- Discover inquiries not responded to
- Cartes Bancaires (SEPA merchants only)
- Nigerian payment methods (local regulation)

### Disputed Amount Differences

Currency conversion rate drift, bundled recurring disputes, partial disputes, or partially-refunded charge where customer disputes the full amount.

### Stripe vs PayPal Dispute Comparison

| Dimension | Stripe (card) | PayPal (internal) |
| --- | --- | --- |
| Decision-maker | Card issuer | PayPal |
| Dispute window | ~120 days | 180 days |
| Pre-dispute phase | EFWs + inquiries (AmEx/Discover) | INQUIRY stage (INR/SNAD) |
| Response window | 7–21 days | 20 days (INQUIRY); 10 days (CHARGEBACK) |
| Fee | Dispute received + countered fee | No explicit per-dispute fee (Chargeback Protection optional) |
| Arbitration | Not supported | PRE_ARBITRATION + ARBITRATION stages |

See [[source-stripe-disputes-how-disputes-work]] for full lifecycle details.

### Responding to Disputes (Stripe)

**Deadline**: 7–21 days; missing it = automatic loss with no recovery.

**Special cases**:

- **Visa compliance disputes**: if contested, the captured guides say a 500 USD or local-equivalent **network fee** applies in addition to applicable Stripe dispute fees and is returned if won. See [[source-stripe-disputes-visa-compliance]] for the separate Visa API procedure and fee acknowledgment.
- **Mastercard compliance disputes**: the November 2026 responding capture separately says a contested case incurs a 500 USD or local-equivalent **network fee** in addition to applicable Stripe dispute fees, returned if won; an issuer-filed pre-compliance case can escalate to full compliance. Its linked Mastercard API procedure is not specified here.
- **Stripe fee distinction**: the dispute countered fee is returned on a win and does not apply to Mexico and Japan businesses; the dispute received fee is generally retained unless the Stripe contract says otherwise. Network compliance fees above are separate.
- **Visa CE 3.0**: Stripe evaluates Visa 10.4 fraud disputes for eligibility; if eligible, it usually improves win likelihood but is no guarantee. In most cases Stripe pre-populates required fields; do not edit already populated fields, and fill requested empty fields. 3DS/ECI evidence may be supplied for disputes that **might** have liability shift, without proving coverage.
- **Accepting an inquiry ≠ resolving it**: submit evidence to counter an inquiry; if it becomes a chargeback, send a separate response. See [[source-stripe-disputes-responding]] for these response paths.

**Dashboard evidence submission**: one final submission opportunity; combined files no more than 4.5 MB; one file per evidence type; no external audio/video, calls or email requests, or links for the issuer to follow. The November responding capture states a combined 19-page Mastercard evidence maximum, and the May best-practices capture also gives that figure. The November best-practices capture omits the number and describes a dispute-specific applicable page limit; its omission proves neither repeal nor acceptance for every case. Check the actual dispute limit. The best-practices captures allow PDF/JPEG/PNG files; an API evidence update exceeding its compiled-PDF page limit can fail with `dispute_evidence_page_limit_exceeded` even at `submit=false`, before final submission. Reduce the evidence and retry. See [[source-stripe-disputes-best-practices]] and [[source-stripe-disputes-responding]]. Submitting sends evidence for issuer consideration; the issuer decides whether the case is won or lost.

See [[source-stripe-disputes-responding]] for full evidence submission workflow.

## Key Players

- [[paypal]] — Disputes API + Resolution Center
- [[stripe]] — Stripe disputes handled via Dashboard, webhooks, and API

## Sources

- [[source-braintree-docs-reference-response-dispute-node]] - 2026-09-16 unversioned Braintree Node.js website response-reference route for the Dispute object, preserving the results-limitation policy notice and Control Panel access qualification; not a request-operation contract, exact SDK package/version evidence, current merchant eligibility, successful execution, lifecycle transition, or dispute outcome proof

- [[source-braintree-docs-guides-disputes-automating-node]] - unversioned Braintree Node.js webpage captured 2026-09-16 presenting an account-qualified, webhook-triggered dispute automation pattern and a reason-conditioned shipping-confirmation example; not an exact SDK package/version contract, current availability, lifecycle-transition, execution or outcome proof

- [[source-braintree-docs-guides-disputes-overview]] - unversioned Braintree webpage captured 2026-09-16 introducing account-qualified access to API dispute management and the accept-or-respond flow through evidence finalization and bank review; not current merchant eligibility, independent current bank/card-network policy, successful API execution, evidence acceptance, dispute outcome, settlement, or recovered-funds proof

- [[source-braintree-docs-guides-disputes-testing-go-live-node]] - 2026-09-16 unversioned Braintree Node route for sandbox-only disputed-sale creation and deterministic `won`/`lost` simulations through evidence finalization, with Control Panel access qualification and a separate production deadline and real-adjudication boundary; not an exact Node SDK-version contract, direct PayPal Disputes API authority, current card-network policy, or real dispute outcome proof

- [[source-braintree-docs-guides-disputes-paypal-disputes-node]] - unversioned Braintree Node.js webpage captured 2026-09-16 for Control Panel-eligible merchants responding to PayPal disputes reflected in the Braintree gateway, with categorized evidence and deadline-bound finalization; not direct PayPal Disputes API authority, current access proof or outcome proof

- [[source-braintree-docs-guides-disputes-managing]] - unversioned Braintree website guide captured 2026-09-16 for API dispute management by Control Panel-eligible merchants, covering open-dispute discovery, acceptance versus evidence response, the reply-by cutoff, expiration and loss of contest rights, and required finalization before evidence is forwarded for bank review; not independent current bank/card-network policy, GitHub implementation evidence, current merchant eligibility, execution proof, or evidence of a win, settlement, or returned funds
- [[source-braintree-graphql-integration-guides-uploading-files]] - 2026-09-16 unversioned Braintree GraphQL guide for the single-file multipart transport used by `createDisputeFileEvidence`, including PNG/JPG/JPEG/PDF and 4 MB limits, required `operations`/`map` parts and standard GraphQL version/authorization headers; not current service-support, merchant-access, evidence-acceptance, finalization, business-approval or dispute-outcome proof
- [[source-braintree-articles-nab-chargebacks-retrievals-prearbs]] - captured 2026-09-16 Braintree-hosted NAB account/processor article for credit-card dispute notifications, response deadlines, chargeback/retrieval/pre-arbitration handling, statuses and reporting
- [[source-braintree-articles-risk-and-security-chargebacks-retrievals-chargeback-reason-codes]] - Braintree-hosted 2026-09-16 snapshot of a reason-code table generated 2025-09-22 for received credit-card disputes, organized by card brand and dispute type with separate JCB retrieval codes, region/network variability, a changeable and potentially incomplete inventory, and Visa decimal-code normalization; not independent current card-network authority or ACH return-code evidence
- [[source-braintree-articles-risk-and-security-chargebacks-retrievals-disputing-chargebacks]] - 2026-09-16 general Braintree guide for account-dependent chargeback acceptance and dispute choices, card-brand-defined evidence conditions, refund-overlap risk, beta evidence recommendations and narrowly qualified pre-arbitration guidance; not bank-specific procedure, current universal policy or an outcome guarantee
- [[source-braintree-articles-risk-and-security-chargebacks-retrievals-overview]] - captured 2026-09-16 general Braintree overview of chargeback, retrieval, and pre-arbitration roles; banking-partner and merchant-account qualifications govern fund and fee handling, and its dated U.S. flat-rate pre-arbitration auto-accept statement is not independent current bank or card-network policy
- [[source-braintree-articles-risk-and-security-chargebacks-retrievals-reducing-chargebacks]] - 2026-09-16 Braintree general guidance article routing to customer-data collection, purchase/subscription transparency, support/refunds/descriptors, internal monitoring, CAPTCHA and fraud tools intended to reduce chargeback frequency; it says chargebacks cannot be eliminated and is not current independent bank/card-network policy or an outcome guarantee
- [[source-braintree-articles-risk-and-security-card-brand-monitoring-programs-overview]] - 2026-09-16 Braintree-hosted overview of Visa/Mastercard monthly threshold-based chargeback and fraud monitoring, ratio definitions, first-chargeback-only dispute-ratio treatment, program-specific outbound routes, and notification limited to merchant accounts provided through Braintree; not independent current card-network rules, numeric-threshold authority, compliance or enrollment proof, or transferable account behavior

- [[source-braintree-articles-br-chargebacks-retrievals-prearbs]] - 2026-09-16 Braintree-hosted BR/Brazil-route credit-card dispute snapshot covering account-sensitive notifications, interface-qualified management, reply-by expiration, chargeback/retrieval/pre-arb effects, statuses and reports; not a transferable price or currency schedule, independent current bank/network policy, sibling-account behavior, or execution and fund-arrival proof

- [[source-braintree-articles-apac-chargebacks-retrievals-prearbs]] - 2026-09-16 Braintree-hosted APAC-route credit-card dispute snapshot covering account-qualified notification and response channels, reply-by expiration, bank adjudication, net-disbursement and settlement-currency fee effects, retrieval/pre-arb distinctions, statuses and a non-reconciliation report boundary; not PayPal-dispute authority, independent current bank/card-network policy, a universal price schedule, or transferable sibling-account behavior
- [[source-braintree-articles-au-chargebacks-retrievals-prearbs]] - 2026-09-16 captured Braintree AU credit-card-dispute article covering account-sensitive notifications, Control Panel and stated API management routes, reply-by expiration, chargeback/retrieval/pre-arb effects, $25 AUD fee statements, statuses, and report purposes; not independent current bank/card-network policy, execution proof, a merchant-specific agreement, or transferable pricing for another region or account context

- [[source-braintree-articles-aib-af-chargebacks-retrievals-prearbs]] - 2026-09-16 captured Braintree AIB AF credit-card-dispute article covering account-sensitive notifications, Control Panel and stated API management routes, reply-by expiration, chargeback/retrieval/pre-arb effects, statuses, and the non-reconciliation report boundary; not AIB BF behavior, independent current bank/card-network authority, or a merchant-specific pricing agreement, and its linked targets were not used to establish broader agreement

- [[source-braintree-articles-aib-bf-chargebacks-retrievals-prearbs]] - 2026-09-16 Braintree-hosted AIB BF credit-card dispute snapshot covering chargeback, retrieval and pre-arbitration definitions, evidence and response cutoff, payout and fee effects, Control Panel/API routes, statuses and reports; not independent current bank authority, a defined region/pricing model, or transferable AF/Wells policy

- [[source-braintree-articles-wells-flat-pre-dispute-programs]] - 2026-09-16 Braintree Wells Flat-route article describing US-supported Visa RDR, direct Visa enrollment, merchant-rule outcomes, liability acceptance and qualified Visa dispute-ratio treatment; this is captured Braintree documentation, not independent current Visa policy or universal account eligibility.

- [[source-braintree-articles-wells-flat-chargebacks-retrievals-prearbs]] - captured 2026-09-16 Braintree Wells Flat credit-card dispute article covering retrieval, chargeback, pre-arbitration and arbitration boundaries, response cutoff, Control Panel/API routes, and a dated US flat-rate pre-arbitration auto-accept policy; not independent current Wells or universal Braintree policy
- [[source-braintree-articles-wells-ic-chargebacks-retrievals-prearbs]] - 2026-09-16 Braintree Wells IC webpage snapshot routing to the credit-card retrieval, chargeback, pre-arbitration and arbitration lifecycle, account-qualified notification and deadline handling, Wells IC fee/reporting details, and the boundary that arbitration is not managed end to end or represented as a Braintree dispute; not current independent bank policy or transferable Wells Flat pricing
- [[source-braintree-articles-risk-and-security-overview]] - 2026-09-16 Braintree umbrella navigation page identifying chargebacks as a standard online-payment business concern and routing merchants to the dedicated handling and minimization guide
- [[source-braintree-payment-methods-paypal-disputes]] - PayPal-specific Braintree Control Panel dispute route covering linked-account setup, Retrieval/Claim/Chargeback roles, reply-by cutoff, fee boundary, customer-resolution-first guidance and status interpretation; its Control Panel labels are not PayPal Disputes API lifecycle-stage enum authority, which remains with the existing PayPal API evidence on this concept
- [[source-braintree-payment-methods-unionpay]] - Braintree guide stating a UnionPay standard chargeback fee of USD 25 or settlement-currency equivalent, non-refundable regardless of outcome and inclusive of pre-arbitrations

- [[source-braintree-payment-methods-local-payment-methods]] - Braintree guide stating that disputes are currently unsupported for Local Payment Methods and customers must work directly with their bank

- [[source-braintree-fraud-tools-premium-effortless-chargeback-protection]] - Braintree Effortless Chargeback Protection purpose, country and card-transaction scope, transaction and chargeback eligibility, reason-code-specific evidence treatment, and non-waived acquiring-bank or card-network fee boundary
- [[source-braintree-fraud-tools-premium-chargeback-protection]] - Braintree's Chargeback Protection and Effortless Chargeback Protection tools, with eligible-transaction and evidence conditions, real-time decline behavior, bypass service-payment consequence and unresolved indemnity direction, and account, region, payment and processor limits
- [[source-braintree-fraud-tools-3d-secure]] - Braintree 3DS authentication and conditional fraud-chargeback liability shift, including the warning that a shift does not always trigger automatic representation and merchants must still monitor and act on chargebacks

- [[source-braintree-transactions-guide-node]] - Braintree Node.js transaction-level route to account-qualified dispute details on the transaction response, disputed-transaction search by dispute date, and banking-partner-dependent handling

- [[source-braintree-dispute-add-text-evidence-node]] - Braintree Node.js text-evidence addition for `open` disputes, restricted to merchants with Control Panel dispute access, with plain and categorized evidence routes and a separate finalization boundary for submission to the banks

- [[source-braintree-dispute-remove-evidence-node]] - Braintree Node.js removal of one evidence item by dispute and evidence IDs while the dispute is `Open`, restricted to merchants with Control Panel dispute access and distinct from evidence submission or finalization

- [[source-braintree-dispute-search-node]] - Braintree Node.js dispute search with callback `response.forEach()` result access, raw routes for criteria and operators, Control Panel access qualification, and the preserved results-limitation notice

- [[source-braintree-dispute-find-node]] - Braintree Node.js single-dispute lookup by dispute ID, restricted to merchants with Control Panel dispute access and preserving the results-limitation policy notice

- [[source-braintree-dispute-finalize-node]] - Braintree Node.js dispute finalization for `Open` disputes, restricted to merchants with Control Panel dispute access, requiring the finalize call to submit evidence to the banks and transition status to `Disputed`

- [[source-braintree-dispute-accept-node]] - Braintree Node.js dispute acceptance by ID, restricted to merchants with Control Panel dispute access, with the prior-refund do-not-accept warning and an unreconstructed missing status-eligibility value

- [[source-braintree-webhooks-dispute-node]] - Braintree Node.js dispute webhook notification kinds, event-specific trigger conditions, and notification-attribute routes

- [[source-paypal-disputes-api]] — Disputes API guide, test & go-live, reasons/evidence reference, test values, file types
- [[source-paypal-disputes-overview]] — overview, setup, Resolution Center guide
- [[source-paypal-customer-disputes]] — older disputes API coverage from developer.paypal.com
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Disputes 1.11 operation and schema contract
- [[source-stripe-disputes-how-disputes-work]] — Stripe dispute lifecycle: EFWs, inquiries, timing, fees, LPM differences

## Open Questions

- What are typical chargeback rates by industry vertical?
