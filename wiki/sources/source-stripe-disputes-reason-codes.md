---
title: "Stripe — Dispute Reason Codes"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-reason-codes-2026.md"
tags: [stripe, disputes, chargebacks, reason-codes, visa, mastercard, amex, evidence, fraud, card-present, card-not-present]
---

## Summary

Narrative evidence guidance for dispute reason codes across Visa, Mastercard, and American Express, organized into 7 categories. Complements [[source-stripe-disputes-categories]] which covers all 7 payment methods with full code listings.

## Coverage

3 networks × 7 categories = detailed evidence examples per reason code. The cardholder's bank decides outcomes — not Stripe.

**Key cross-category rule**: Customer is obligated to contact merchant before filing a dispute. Absence of prior customer contact is itself evidence to submit.

## Visa Reason Codes by Category

| Category | Key Codes |
| --- | --- |
| Credit not processed | 13.6 (Credit Not Processed), 13.7 (Canceled Merchandise/Services) |
| Duplicate | 12.6.1 (Duplicate Processing), 12.6.2 (Paid by Other Means) |
| Fraudulent | 10.3 (Card-Present Fraud), 10.4 (Card-Not-Present Fraud) |
| General | 12.2 (Incorrect Transaction Code), 12.5 (Incorrect Amount) |
| Product not received | 13.1 (Merchandise/Services Not Received) |
| Product unacceptable | 13.3 (Not as Described/Defective), 13.4 (Counterfeit), 13.5 (Misrepresentation) |
| Subscription canceled | 13.2 (Canceled Recurring) |

## Mastercard Reason Codes by Category

| Category | Key Codes |
| --- | --- |
| Credit not processed | 4860 |
| Duplicate | 4834 |
| Fraudulent | 4837 (No Cardholder Authorization), 4870/4871 (Chip Liability Shift) |
| General | 4808, 4831, 4859 |
| Product not received | 4855 |
| Product unacceptable | 4853 |
| Subscription canceled | 4841 |
| Unrecognized | 4863 |

## American Express Reason Codes by Category

| Category | Key Codes |
| --- | --- |
| Credit not processed | A01, C02, C04, C05, C18, P03, P05 |
| Duplicate | C14, P08 |
| Fraudulent | F10, F24, F29, F30 (EMV Counterfeit), F31 (EMV Lost/Stolen), FR2/FR4/FR5/FR6 |
| General | A02, A08, P07 (Late Submission), P22, P23 |
| Product not received | C08 |
| Product unacceptable | C31, C32 |
| Subscription canceled | C28 |
| Unrecognized | 127, 176, 691 |

## Key Evidence Patterns

### Fraudulent — Card Present (Visa 10.3, MC 4837 CP)
EMV transaction data, signed receipt, surveillance footage, POS logs.

### Fraudulent — Card Not Present (Visa 10.4, MC 4837 CNP)
3DS authentication proof, AVS + CVV match results, device/IP data, order history showing prior legitimate purchases.

### Duplicate (Visa 12.6.1, MC 4834)
Transaction logs showing single charge; pre-auth vs settlement distinction; receipts for different services if charges are legitimately separate.

### Product Not Received (Visa 13.1, MC 4855)
Shipping tracking + delivery confirmation; digital access/login logs; service completion records.

### Subscription Canceled (Visa 13.2, MC 4841)
Cancellation policy agreed to at signup; no cancellation request on record; usage logs post-alleged-cancellation.

## Related Pages

- [[disputes]] — concept page
- [[source-stripe-disputes-categories]] — full code listings for all 7 payment methods + evidence field API params
- [[source-stripe-disputes-responding]] — evidence submission workflow

## Raw Sources

- [[stripe-disputes-reason-codes-2026]] — verbatim Stripe dispute reason codes guide (461 lines)
