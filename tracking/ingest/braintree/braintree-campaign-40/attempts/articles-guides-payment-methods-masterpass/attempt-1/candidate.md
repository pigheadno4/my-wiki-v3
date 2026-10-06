---
title: "Braintree Masterpass Historical Payment Method Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/masterpass"
raw_files:
  - "braintree/articles/guides/payment-methods/masterpass-2026-09-16.md"
tags: [braintree, masterpass, mastercard, digital-wallets, payment-methods, historical-snapshot]
---

## Overview

This collected [[braintree|Braintree]] article is a historical retrieval guide for Masterpass by Mastercard, which the page describes as a digital wallet for stored payment and shipping information. It records the page's replacement instruction, processing and dispute comparisons, fraud-tool behavior, and restricted vaulting route for [[braintree-payment-methods]]. It does not establish that Masterpass or its named successor is currently supported, enabled for a merchant, or successfully executable.

## Key takeaways

- The page says Masterpass has been replaced by Visa Secure Remote Commerce (SRC) and tells previous Masterpass users to integrate with SRC. The immediately following notice, however, says Visa Click to Pay (SRC) would no longer be supported effective January 20, 2026, and that transactions attempted after that date would receive a `Payment method not supported` error and risk decline. The article does not name a successor to SRC or resolve the resulting migration-path conflict.
- Historically, the page describes Masterpass as a Mastercard digital-wallet service in which customers could store payment and shipping information. It lists American Express, Diners Club, Discover, JCB, Maestro, Mastercard and Visa as wallet card types. Treat these as captured product descriptions, not present customer or card eligibility.
- The page says Masterpass transactions process and settle like credit-card transactions, use the same pricing as other credit-card transactions, and follow credit-card dispute behavior according to the merchant-account setup. These comparisons are page-scoped historical statements, not proof of current fees, settlement, dispute handling or transaction results for an account.
- The fraud section states compatibility with AVS, risk-threshold Basic Fraud Tools and Premium Fraud Management Tools, while saying CVV rules are bypassed because Masterpass wallets do not save CVV values. Exact current fraud configuration and account behavior require current Braintree authority.
- Vaulting is restricted to recurring transactions and requires Masterpass approval. The page says split shipments and one-off transactions using vaulted payment information are unsupported.

> [!warning] Historical replacement and current-support conflict
> This captured page directs former Masterpass users to SRC but also says Visa Click to Pay (SRC) is unsupported after January 20, 2026. Preserve both statements: the snapshot does not establish a currently supported successor, present Masterpass or SRC availability, merchant eligibility, or a safe executable migration path.

## Detail locators

- Masterpass-to-SRC replacement instruction: opening `**AVAILABILITY**`, raw line 18.
- Visa Click to Pay/SRC end-of-support date, error text and decline risk: opening `**NOTE**`, raw lines 23-24.
- Historical Masterpass identity and stored payment/shipping-information purpose: raw line 26.
- Listed wallet card types: `### Customer availability`, raw lines 29-40.
- Credit-card-like processing and Control Panel identification: `## Processing`, raw lines 43-45.
- Page-stated fee comparison: `### Fees`, raw lines 48-50.
- Dispute behavior and merchant-account qualification: `### Disputes`, raw lines 53-55.
- Fraud-tool compatibility and CVV bypass explanation: `### Fraud tools`, raw lines 58-60.
- Recurring-only vaulting, approval prerequisite, and split-shipment/one-off exclusions: `### Recurring billing and vaulting`, raw lines 63-65.
- Historical integration-docs route: `## Setup`, raw lines 68-70.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Named successor guide: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]] - named successor route; navigation only and not read as evidence for this entry
- [[raw/braintree/docs/guides/masterpass/overview-2026-09-16|Braintree Masterpass developer overview]] - historical setup route; navigation only and not read as evidence for this entry

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/masterpass-2026-09-16|Braintree Masterpass article]] - complete collected page covering the replacement and end-of-support notices, historical wallet identity, card list, processing, pricing, disputes, fraud behavior, vaulting restrictions and setup route
