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

## Common Dispute Reasons

- Item not received (INR)
- Item significantly not as described (SNAD)
- Unauthorized transaction / fraud
- Billing issue (duplicate charge, wrong amount)

## Common Fraud Types

| Type | Description |
| --- | --- |
| Stolen cards | Stolen card/details used online; business bears loss + dispute fee |
| Overpayment fraud | Stolen card + fake third-party; business pays out then faces dispute |
| Card testing | Validating stolen cards on low-friction sites (donations, PWYL) |
| Alternative refunds | Overpay → request refund via different channel — **never refund differently** |
| Marketplace fraud | Fraudulent seller on Connect platform; platform bears unrecoverable liability |
| Friendly fraud | Legitimate cardholder disputes own purchase; Visa CE 3.0 challenges this |

**Key rule**: partially refunded payments can still be disputed for the full original amount. See [[source-stripe-disputes-fraud-types]].

**Card testing** (carding/enumeration): validating stolen cards via Card Setup or small Payments. Identify by spike in failed payments / 402 errors / small suspicious payments. Prevention: use Payment Element or Checkout (automated CAPTCHA+AI); add CAPTCHA, login requirement, rate limits (limit cards/customers per IP); Radar velocity rules. Single heuristic insufficient. See [[source-stripe-disputes-card-testing]].

**Fraud identification indicators**: false/scripted communication (search phrase in quotes), same card+different shipping, many cards+same shipping, rush orders, "preferred shipper" requests (red flag), overcharge+pay-third-party, post-order address change. Donations: "refund the difference" request = credit limit test → refund entire amount. See [[source-stripe-disputes-identifying-fraud]].

**Fraud prevention best practices** (3 tiers):

- *Everyone*: full ToS text at checkout (link-only rejected by issuers), tracking screenshots (not links), clear statement descriptor, one account per business, proactive refund if sure it's fraud, 24-48hr shipping delay
- *Radar Fraud Teams*: review queue + auth-capture, country/card blocking rules, ship only to AVS-verified addresses
- *Developers*: process on Stripe (CE 3.0 eligibility), collect full data, 3DS, auth+capture, Stripe Identity

See [[source-stripe-disputes-prevention-best-practices]].

**Customer abuse** (policy exploitation — not payment fraud): **Refund abuse** (Sigma query by refund frequency; notify/restrict/fee); **Resale abuse** (account sharing: OTP friction on geo-dispersed IPs; account transfers: velocity rules on same card+promo across accounts); **Trial abuse**: Radar trial abuse control. See [[source-stripe-disputes-customer-abuse]].

**CVC and AVS verification**: always collect CVC + postal + billing address at checkout. CVC protects against computer breaches (not physical theft); doesn't apply to wallets or off-session payments. AVS checks postal + street address — can fail for legitimate payments; mainly US/CA/UK. Enable Radar built-in rules to block failures. See [[source-stripe-disputes-verification]].

## Stripe Dispute Categories (8 standardized)

Stripe maps all payment method reason codes into 8 categories (plus Visa-only `noncompliant`). Covered payment methods: Visa, Mastercard, Amex, Discover, Klarna, PayPal, Cash App Pay.

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

**Cross-category rule**: Customer is obligated to contact merchant before filing — absence of prior contact is itself evidence to submit.

**Fraudulent evidence by environment**:

- Card-present: EMV data, signed receipt, surveillance, POS logs
- Card-not-present: 3DS proof, AVS/CVV match, device/IP data, prior purchase history

See [[source-stripe-disputes-reason-codes]] for per-code evidence guidance (Visa, Mastercard, Amex).
See [[source-stripe-disputes-visual-evidence]] for visual evidence packet examples (approved vs denied scenarios, 62 illustrative images).

### Stripe Evidence Best Practices

- **Win likelihood**: Radar scores 1–5 dots (5 dots = 60% win, 1 dot = 5%) — disputes are hard to overturn even at best
- **File limits**: 4.5 MB / <50 pages total / 19 pages Mastercard / PDF+JPEG+PNG only; one file per evidence type
- **Fraudulent = >50% of disputes**: include AVS, CVC, IP, 3DS; Stripe auto-populates these when available
- **Accepting disputes**: fee still applies; counts toward dispute rate regardless — prevention > acceptance
- **Partially refunded**: always respond with refund proof; issuer cancels + re-issues for corrected amount

See [[source-stripe-disputes-best-practices]] for full guidance including auto-populated API evidence fields and Visa CE 3.0 details.

### Stripe Disputes API

| Operation | Method |
| --- | --- |
| Retrieve dispute | `stripe.disputes.retrieve(id)` |
| Submit evidence | `stripe.disputes.update(id, { evidence: {...} })` |
| List by PaymentIntent | `stripe.disputes.list({ payment_intent: id })` |
| List by Charge | `stripe.disputes.list({ charge: id })` |

Evidence fields: text-based (strings) or file-based (`file_upload` object ID from File Upload API with `purpose: "dispute_evidence"`). Text limit: 150,000 characters. Deadline in `evidence_details.due_by`. See [[source-stripe-disputes-api]].

### Visa CE 3.0 API Details

Eligibility: Visa 10.4 disputes + 2 prior undisputed transactions (same payment method, 120–364 days prior, paid, not validation charges) + product descriptions for all 3 + `merchandise_or_services` field + matching 2 main OR 1 main + 1 secondary evidence elements across all transactions.

CE 3.0 status (`evidence_details.enhanced_eligibility.visa_compelling_evidence_3.status`): `requires_action` → check `required_actions[]`; `qualified` → ready; `not_qualified` → fallback to standard submission. **Also fill standard `evidence` object as fallback.**

Test card: `4000000404000038` / `pm_card_createCe3EligibleDispute`. See [[source-stripe-disputes-visa-ce3]].

### Visa Compliance Disputes (API)

Identify via: `payment_method_details.card.case_type = "compliance"`, `enhanced_eligibility_types` contains `"visa_compliance"`, or `reason = "noncompliant"`.

Two options: **close** (no 500 USD fee, irreversible) or **respond** (must set `evidence.enhanced_evidence.visa_compliance.fee_acknowledged: true` — submitting without it returns an error; fee withdrawn 1–2 days later, refunded if won).

Test card: `4000008400000779` / `pm_card_createComplianceDispute`. See [[source-stripe-disputes-visa-compliance]].

### Dispute Withdrawals

Withdrawn ≠ won — must still submit evidence or issuer may treat silence as liability. Withdrawn disputes still count against dispute rate and don't resolve faster. Only chargebacks can be withdrawn (not EFWs or inquiries). Refunds remain blocked until issuer decides. Late withdrawals (even post-loss) are allowed by all networks but take weeks/months to process. See [[source-stripe-disputes-withdrawals]].

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

Industry threshold: >0.75% dispute activity = excessive. All disputes (won or lost) count. Dispute rate is mutable for dates <120 days old. EFWs counted by Visa toward VAMP monitoring program. See [[source-stripe-disputes-measuring]].

### Stripe Dispute Prevention Tools

| Tool | How it works | Rate impact |
| --- | --- | --- |
| **Resolution** (Radar rules) | Auto-refund specific disputes via custom rules | Resolved disputes don't count toward rate; no dispute received fee |
| **Deflection** (Order Insights / Verifi) | Sends transaction data to cardholder before they dispute | Reduces inbound disputes; CE 3.0 eligible data can block entirely |
| **Smart Disputes** | AI builds + submits evidence automatically for eligible disputes | Handles disputes that get through prevention; **fee only on wins** |

No integration required — Stripe connects directly to Verifi. Configure at Dashboard → Dispute settings. See [[source-stripe-disputes-prevention]].

**Smart Disputes API**: set `intended_submission_method: "prefer_smart_disputes"` on dispute update to merge your evidence with AI-generated evidence. Check `smart_disputes.status` (`available` / `requires_evidence` / `unavailable`) and `smart_disputes.recommended_evidence` array for what to add. See [[source-stripe-smart-disputes-setup]].

**Auto-respond config**: toggle at Dashboard → Settings → Disputes. For Connect platforms: control per connected account via `accounts.update({ settings: { smart_disputes: { auto_respond: { preference: 'on'|'off'|'inherit' } } } })`. `inherit` immediately tracks platform default; explicit override is sticky until reset. See [[source-stripe-smart-disputes-auto-respond]].

**RDR limitation**: only resolves full-amount disputes on non-refunded transactions.

**CE 3.0 pre-dispute block (OI)**: if ≥2 prior transactions with cardholder have matching IP + email/delivery address + complete product descriptions → issuer **must block the dispute** (never filed, no fees, no rate impact). Requires IP address, customer email, and product descriptions on all transactions. See [[source-stripe-disputes-prevention-how-it-works]].

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

**Early Fraud Warnings (EFWs)**: Visa TC40 + Mastercard SAFE reports flag suspected fraud before a dispute is filed. 80% convert to fraud disputes if ignored. With 3DS liability shift, Stripe auto-provides evidence. Optimal refund threshold: charges ≤ dispute fee; reversal window is 2 hours post-capture.

**Inquiries**: Pre-dispute phase used by AmEx and Discover (not Mastercard/Visa). Resolve by submitting evidence or issuing full refund — no dispute fee. Unanswered inquiry → likely unwinnable chargeback. Inquiry statuses: `warning_needs_response` → `warning_under_review` → `warning_closed` (120 days).

### Dispute Lifecycle

1. Card network debits Stripe; Stripe debits merchant (disputed amount + fee)
2. Refunds blocked while dispute is open
3. Merchant submits evidence within 7–21 days (varies by network)
4. Issuer reviews: 60–75 days. Full lifecycle: 2–3 months

**Dispute status**: `won` (funds returned) or `lost` (no movement — funds already with issuer). `late win` is rare but possible.

### Dispute Fees (Stripe)

- **Dispute received fee**: non-refundable (Mexico: refundable if won; SEPA/Cartes Bancaires: no fee)
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

- **Visa compliance disputes**: extra 500 USD network fee on top of standard dispute fee; refunded if won
- **Visa CE 3.0**: Stripe auto-evaluates for Visa 10.4 fraud disputes; pre-populates evidence — don't edit pre-populated fields
- **Accepting an inquiry ≠ resolving it**: must submit evidence to counter inquiries; accepting inquiry does not close it

**Evidence submission**: one-shot only; 4.5 MB max; 19-page max (Mastercard); one file per evidence type; no external links/audio/video.

See [[source-stripe-disputes-responding]] for full evidence submission workflow.

## Key Players

- [[paypal]] — Disputes API + Resolution Center
- [[stripe]] — Stripe disputes handled via Dashboard, webhooks, and API

## Sources

- [[source-paypal-disputes-api]] — Disputes API guide, test & go-live, reasons/evidence reference, test values, file types
- [[source-paypal-disputes-overview]] — overview, setup, Resolution Center guide
- [[source-paypal-customer-disputes]] — older disputes API coverage from developer.paypal.com
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Disputes 1.11 operation and schema contract
- [[source-stripe-disputes-how-disputes-work]] — Stripe dispute lifecycle: EFWs, inquiries, timing, fees, LPM differences

## Open Questions

- What are typical chargeback rates by industry vertical?
