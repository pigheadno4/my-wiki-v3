---
title: "Stripe — Dispute Reason Codes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/reason-codes-defense-requirements"
raw_files:
  - "stripe-disputes-reason-codes-defense-requirements-2026-11-07.md"
  - "stripe-disputes-reason-codes-2026.md"
tags: [stripe, disputes, chargebacks, reason-codes, visa, mastercard, amex, evidence, fraud, card-present, card-not-present]
---

## Summary

Stripe's 2026-11-07 guide describes common Visa, Mastercard, and American Express dispute reason codes in seven categories, with possible evidence examples for each code. It is a selection of common codes, not a comprehensive network rulebook. The 2026-05-09 capture covered the same three-network, seven-category guide; the newer capture adds Mastercard 4999 under General. The cardholder's bank, not Stripe, decides the dispute outcome. Evaluate the claim and evidence for each case; the examples do not guarantee a successful challenge.

## Coverage and scope

The card-network code tables below are **highlights from this guide**, not complete lists. For comprehensive requirements, the guide directs readers to official network documentation. Card-network codes on this page apply to Visa, Mastercard, and American Express. Local payment methods use provider-defined reason codes; consult their payment-method guidance.

> [!warning] Contradiction
> This reason-code guide broadly says local payment method codes map to the same seven categories as card disputes. The separately captured [[source-stripe-disputes-categories]] guide explicitly says Instant Bank Payments disputes do not map to its eight-category framework: they use `debit_not_authorized` with an underlying ACH return code. Do not apply this guide's broad LPM mapping sentence to Instant Bank Payments. The reason-code guide's Instant Bank Payments link is navigation, not evidence of return-specific requirements or live availability.

Selected Visa evidence-example cells discuss contacting a merchant before a dispute. That wording is not a universal cross-network customer-contact prerequisite, nor does this guide establish that lack of prior contact by itself decides a case. Mastercard 4834 and 4831, for example, ask for communications **if** the cardholder contacted the merchant. Submit relevant records when they exist and fit the claim.

## Visa reason-code highlights

| Category | Codes in this guide |
| --- | --- |
| Credit not processed | 13.6 (Credit Not Processed), 13.7 (Canceled Merchandise/Services) |
| Duplicate | 12.6.1 (Duplicate Processing), 12.6.2 (Paid by Other Means) |
| Fraudulent | 10.3 (Card-Present Fraud), 10.4 (Card-Not-Present Fraud) |
| General | 12.2 (Incorrect Transaction Code), 12.5 (Incorrect Amount) |
| Product not received | 13.1 (Merchandise/Services Not Received) |
| Product unacceptable | 13.3 (Not as Described/Defective), 13.4 (Counterfeit), 13.5 (Misrepresentation) |
| Subscription canceled | 13.2 (Canceled Recurring) |

## Mastercard reason-code highlights

| Category | Codes in this guide |
| --- | --- |
| Credit not processed | 4860 |
| Duplicate | 4834 |
| Fraudulent | 4837 (No Cardholder Authorization; card-present and card-not-present examples) |
| General | 4831 (Transaction Amount Differs), 4846 (Currency Errors), 4999 (Domestic Chargeback Dispute, Europe Region Only) |
| Product not received | 4855 |
| Product unacceptable | 4853 |
| Subscription canceled | 4841 |

Mastercard 4999 is described for a centrally acquired domestic transaction or domestic transaction processed through Mastercard when an applicable domestic rule allows a chargeback but a different message reason code cannot be used. The guide limits it to Europe Region transactions. Its possible evidence includes authorization receipts or confirmations, correct-processing records, prior communications, and documentation supporting the charge under the applicable domestic rule. Mastercard 4846 was already present in the 2026-05-09 capture.

The previous source entry also listed Mastercard 4870/4871, 4808, 4859, and 4863. Neither pinned capture of **this guide** contains those codes. Their existence elsewhere is not assessed here; independent provenance is needed before attributing them to this guide.

## American Express reason-code highlights

| Category | Codes in this guide |
| --- | --- |
| Credit not processed | A01, C02, C04, C05, C18, P03, P05 |
| Duplicate | C14, P08 |
| Fraudulent | F10, F24, F29, F30 (EMV Counterfeit), F31 (EMV Lost/Stolen), FR2 |
| General | A02, A08, M10, R03, R13, P01, P04, P07, P22, P23 |
| Product not received | C08 |
| Product unacceptable | C31, C32 |
| Subscription canceled | C28 |

The previous source entry also listed Amex FR4/FR5/FR6 and 127/176/691. Neither pinned capture of **this guide** contains those codes. Their existence elsewhere is not assessed here; independent provenance is needed before attributing them to this guide.

## Key evidence patterns

### Fraudulent — card present (Visa 10.3, Mastercard 4837)

Possible evidence includes EMV transaction data, a signed receipt if captured, available surveillance images, and point-of-sale or authorization logs. Mastercard 4837 separates card-present examples from card-not-present examples.

### Fraudulent — card not present (Visa 10.4, Mastercard 4837)

Possible evidence includes 3D Secure authentication proof if used, AVS and CVV results, IP and device data, and relevant customer or order history. These are evidence examples, not a fraud finding or a guaranteed defense.

### Duplicate (Visa 12.6.1, Mastercard 4834)

Possible evidence includes transaction logs showing one charge, a void or refund record if a duplicate occurred, receipts for genuinely separate purchases, and the distinction between a pending authorization and settlement.

### Product not received (Visa 13.1, Mastercard 4855)

Possible evidence includes shipping and delivery confirmation, digital access or login records, and service completion records, as relevant to what was sold.

### Subscription canceled (Visa 13.2, Mastercard 4841)

Possible evidence includes the subscription agreement and cancellation terms, whether a cancellation request was recorded before billing, and relevant usage logs.

## Detail locators

- New capture, Visa reason-code tables: [[raw/stripe-disputes-reason-codes-defense-requirements-2026-11-07|2026-11-07 guide]], lines 17–140.
- New capture, Mastercard tables and 4837 environment split: same raw, lines 142–235; 4999 at lines 198–201.
- New capture, American Express tables: same raw, lines 237–433.
- Local payment method boundary and links: same raw, lines 435–445.
- Historical Mastercard 4846: [[raw/stripe-disputes-reason-codes-2026|2026-05-09 guide]], lines 205–208.

## Related Pages

- [[disputes]] — dispute concept and evidence context.
- [[source-stripe-disputes-categories]] — category and payment-method mapping; consult its Instant Bank Payments exception.
- [[source-stripe-disputes-responding]] — evidence submission workflow.

## Raw Sources

- [[raw/stripe-disputes-reason-codes-defense-requirements-2026-11-07|Stripe dispute reason-code guide, captured 2026-11-07]]
- [[raw/stripe-disputes-reason-codes-2026|Stripe dispute reason-code guide, captured 2026-05-09]]
