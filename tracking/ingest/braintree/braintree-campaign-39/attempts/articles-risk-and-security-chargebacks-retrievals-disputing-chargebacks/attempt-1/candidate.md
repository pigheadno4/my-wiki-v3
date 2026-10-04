---
title: "Braintree Disputing Chargebacks"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks"
raw_files:
  - "braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks-2026-09-16.md"
tags: [braintree, disputes, chargebacks, evidence, refunds, pre-arbitration]
---

## Overview

This collected Braintree article is a general decision-and-evidence guide for accepting or disputing a customer bank chargeback. The page says the actual notification, acceptance, dispute, and evidence process depends on the merchant's account setup and directs merchants to bank-specific articles for those procedures. It is not the separate PayPal-disputes guide, independent current bank or card-brand policy, or a guarantee of any dispute outcome.

## Key takeaways

- The article presents acceptance and dispute as context-dependent choices. It says merchants typically accept when the amount does not justify evidence work, the transaction is known to be fraudulent, or a refund is warranted; merchants typically dispute when they believe the transaction was legitimate, have compelling evidence, or the amount justifies the work. Accepting issues the funds to the cardholder, retains the chargeback fee, and ends further merchant action without necessarily conceding the cardholder's claim.
- Evidence varies with the chargeback reason and available records. For fraud or merchandise/services-not-received chargebacks that the page identifies as requiring card-brand-defined compelling evidence, the merchant must provide at least one listed form of evidence; if required evidence cannot be provided, the page says the dispute will not be accepted by the card brand and the case must be accepted. The article says there is no limit to how much evidence can be provided, but this does not establish that more evidence guarantees acceptance or a favorable outcome.
- The beta Dispute Evidence Recommendations offering uses machine-learning models to prioritize likely-helpful evidence categories. The article expressly frames those recommendations as guidance that does not restrict different or additional evidence and says enablement requires requesting beta access through a Customer Success Manager or Braintree contact route.
- A refund does not automatically cancel an existing chargeback or prevent a future one. Because the merchant is still debited for the chargeback amount, separately refunding a transaction that is also charged back can produce a loss of twice the original amount. For an already-refunded transaction, the article strongly encourages disputing: Braintree automatically adds refund evidence when the refund was issued through Braintree, while an external refund may require the merchant to provide evidence when compelling evidence is required. Braintree states it is not liable for the chargeback loss if the merchant loses or accepts a chargeback after already issuing a refund.
- The pre-arbitration guidance says merchants rarely win without new and compelling evidence, recommends reviewing the original dispute evidence, and says accepting is usually best when no additional evidence exists; a processing fee applies regardless of outcome. Separately and narrowly, the snapshot states that as of August 27, 2025 Braintree auto-accepts pre-arbitrations under USD 1,000 for U.S. flat-rate merchants and permits representation above USD 1,000. That dated, region-, pricing-, and account-qualified statement is not universal or confirmed-current policy.

## Detail locators

- Account-setup dependency and bank-specific notification, acceptance, dispute, and evidence routes: opening, raw lines 16-18.
- Typical acceptance considerations and acceptance effects: `## When to accept`, raw lines 21-32.
- Typical dispute considerations, including the already-refunded-transaction case: `## When to dispute`, raw lines 35-44.
- General evidence examples and recordkeeping guidance: `### Submitting evidence`, raw lines 47-63.
- Card-brand-defined required evidence conditions, examples, absence of an evidence-quantity limit, and consequence of missing required evidence: `#### Required evidence`, raw lines 66-86.
- Beta Dispute Evidence Recommendations purpose, guidance-only qualification, and access route: `#### Dispute Evidence Recommendations`, raw lines 89-99.
- Separate PayPal dispute-management route: `### PayPal disputes`, raw lines 102-104.
- Refund/chargeback double-loss risk, Braintree-versus-external refund-evidence responsibility, and Braintree liability warning: `## Refunds`, raw lines 107-117.
- Pre-arbitration success qualification, dated U.S. flat-rate auto-accept rule, additional-evidence decision, and fee effect: `## Pre-arbitrations`, raw lines 122-134.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Product-specific protection context: [[braintree-chargeback-protection]]

## Related raw API references

- [[raw/braintree/docs/reference/response/dispute/node-2026-09-16|Braintree Node.js Dispute response reference]] - linked reason-code reference route; not read as behavioral evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks-2026-09-16|Braintree Disputing Chargebacks]] - fully read 2026-09-16 snapshot covering acceptance and dispute considerations, evidence, refund overlap, and pre-arbitration guidance
