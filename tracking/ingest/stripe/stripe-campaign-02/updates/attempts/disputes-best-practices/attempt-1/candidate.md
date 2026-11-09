---
title: "Stripe — Dispute Evidence Best Practices"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/best-practices
raw_files:
  - "stripe-disputes-best-practices-2026-11-07.md"
  - "stripe-disputes-best-practices-2026.md"
tags: [stripe, disputes, chargebacks, evidence, best-practices, visa-ce-30, radar, fraud]
---

## Summary

Stripe's November 7, 2026 capture describes evidence organization, estimated win likelihood, dispute-specific page limits and the API page-limit error, authorization and delivery proof, partial refunds, and Visa compelling evidence. Stripe does not influence the bank's final decision. This is guidance for a response, not a guarantee that evidence is accepted or a dispute is won.

## Win Likelihood (Radar Plus)

The November capture calls the Dashboard prediction **Radar Plus**; the May capture called it **Radar for Fraud Teams**. This observed label change does not establish an account's enrollment or a specific dispute's eligibility. If a Radar-enrolled account has no prediction, Stripe lists non-credit-card payment, inquiry rather than dispute, or a prediction error as possible reasons.

The 1–5 dot ranking estimates the chance of winning **after relevant evidence is submitted**. Stripe gives these expected percentages, unchanged between the two captures:

| Dots | Expected win percentage |
| --- | --- |
| 5 | 60% |
| 4 | 40% |
| 3 | 25% |
| 2 | 15% |
| 1 | 5% |

The estimate is not an outcome guarantee. The dispute type, Visa CE 3.0 eligibility, evidence strength, payment type, and purchase type can affect the chance of overturning a dispute.

## Evidence Organization Rules

- Present the chronology of events, group receipts, customer communication, policies, and logs by type, and briefly explain what each item proves.
- Match the evidence to the dispute reason or network reason code. For a cancellation-policy claim, submit the relevant policy excerpt and emphasize the disputed provision; do not upload the entire Terms of Service.
- Keep language neutral, factual, concise, and legible. Emails and text exchanges can support a claim but do not by themselves verify customer identity. Include relevant excerpts and remove duplicate quoted messages.
- Upload evidence itself rather than external links. Issuers might not follow links to separate sites or drives.
- A receipt should show the disputed items' date, currency, and amount; shipping proof should show delivery date and full address; customer communication should identify the customer and relevant message.

## File Limits and Presentation

| Item | November capture |
| --- | --- |
| Accepted file types | PDF, JPEG, PNG |
| Combined uploaded file size | No more than 4.5 MB |
| Formatting-list page count | Less than 50 pages combined |
| Dispute-specific page limit | Keep evidence within the applicable limit for that dispute; it can vary |

> [!warning] Contradiction across dated captures
> The May capture separately stated a 19-page Mastercard maximum. The November capture omits that network-specific figure and instead says the applicable limit can vary by dispute. Omission does not establish that the older Mastercard figure was repealed or remains current; do not use 19 or 50 as a universal acceptance threshold.

For legibility, Stripe **recommends** a 12-point font or larger, US Letter or A4 portrait documents (screenshots may be landscape), clear images, and callouts or arrows rather than color highlighting. These are presentation recommendations, not stated API validation rules. Crop screenshots to the relevant area and describe them in the evidence form. Stripe says the issuer will not review a response with illegible data.

Specify an evidence type for each uploaded file. Only one file can be submitted per evidence type, so combine multiple emails or screenshots of customer communication into one file.

### Handle page-limit errors on API evidence updates

When a page limit applies, Stripe estimates the final compiled evidence PDF from text and uploaded files already saved on the dispute **plus the proposed update**. If that estimate exceeds the applicable limit, the update returns HTTP `400`, `error.type=invalid_request_error`, and `error.code=dispute_evidence_page_limit_exceeded`. This can happen with `submit=true` **or** `submit=false`.

Handle `error.code` programmatically. Use `error.message` to explain the applicable limit and text/file breakdown to a human, then shorten text or reduce uploaded file pages and retry. Do not parse the message for a fixed page threshold: Stripe's example of 17 allowed pages and 36 uploaded pages is illustrative, and the limit varies by dispute.

## Authorization and Delivery Proof

For a fraudulent dispute, useful authorization evidence includes AVS matches, CVC confirmation, a signed receipt or contract, and an IP address matching the cardholder's verified billing address. Stripe includes available AVS/CVC results and purchase IP **if available from the integration**. Add other authorization proof such as 3DS authentication when available.

For a physical product, include shipment and delivery proof with the **full delivery address**, not only city and postal code. Explain a different ship-to name when relevant. For digital goods or services, include an IP address, system log, download record, or usage record supporting delivery or use.

For returns or refunds, show how the relevant Terms of Service or refund policy was presented at checkout and the provision relevant to the case. Use a clear screenshot of the checkout presentation and a relevant excerpt, not the entire policy.

## Background and Discrediting Evidence

When the integration collects and passes the data, Stripe can pre-populate many background fields in the Dashboard and API evidence object; these fields are conditional on availability:

| API evidence parameter | Relevant data |
| --- | --- |
| `billing_address` | Customer billing address, when AVS succeeded |
| `customer_name` | Customer name |
| `customer_email_address` | Customer email |
| `customer_purchase_ip` | Purchase IP, with geographic data when captured |
| `receipt` | Stripe-generated email receipt, if one was sent |
| `product_description` | Product or service details |

Other useful evidence includes `customer_signature` for a signed document, `customer_communication` for relevant correspondence or dispute withdrawal, and `refund_refusal_explanation` for prior compensation. Consolidate multiple communications in one file. See the raw table for Dashboard evidence categories and API parameter mappings.

## Accepting, Withdrawing, and Partial Refunds

Accepting a dispute is not an admission of wrongdoing. The dispute fee still applies, and disputes received count toward dispute activity whether won or lost. Accept when you do not intend to respond or recover the funds. For a misunderstanding, a cardholder may withdraw with their issuer, but Stripe recommends submitting evidence of validity; a withdrawal still counts as a dispute.

A customer can dispute the full original amount after a partial refund. Respond with the **amount and date** of the refund and, when helpful, a Dashboard screenshot, even if you will accept the unrefunded portion. In most cases the issuer cancels the original dispute and creates a corrected-amount dispute. Stripe tracks the overall outcome on the existing dispute; if not fully resolved in the merchant's favor, its status is `lost` and the merchant receives only the partially refunded amount. Cartes Bancaires merchants cannot contest these disputes, so they cannot request issuer consideration of an existing partial refund.

## Visa Compelling Evidence and CE 3.0

For a **Visa fraudulent** dispute, Visa's Compelling Evidence specification calls for at least one qualifying item; without it, Stripe says the likelihood of overturning the dispute is very low. More relevant evidence can help, but it does not guarantee a win. Stripe recommends applying the practice more broadly even though Visa names this specification.

Visa CE 3.0 can use qualifying prior non-fraudulent cardholder history against friendly fraud. For eligible disputes, Stripe says it searches prior transactions, flags eligibility, notifies through email and the dispute details page, adds qualifying transactions, marks required form elements, pre-populates available required information, and supports API evidence submission. Eligibility and pre-populated data depend on the actual dispute and available history; the November page does not name a particular Visa reason code here.

## Related Pages

- [[disputes]] — dispute concept and evidence workflow context
- [[stripe]] — provider overview
- [[source-stripe-disputes-responding]] — responding and submission workflow
- [[source-stripe-disputes-visual-evidence]] — visual evidence packet examples
- [[stripe-3d-secure]] — 3DS as possible authorization evidence

## Raw Sources

- [[raw/stripe-disputes-best-practices-2026-11-07|Stripe dispute evidence best practices, 2026-11-07 capture]] — current captured guidance and API page-limit error
- [[raw/stripe-disputes-best-practices-2026|Stripe dispute evidence best practices, 2026-05 capture]] — earlier guidance including historical 19-page Mastercard statement
