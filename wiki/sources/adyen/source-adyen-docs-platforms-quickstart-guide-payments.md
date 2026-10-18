---
title: "Adyen for Platforms payments quickstart"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/payments"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/payments/2026-09-15.md"
tags: [adyen, platforms, quickstart, payments, split-payments, settlement]
---

## Overview

This Adyen for Platforms quickstart introduces online and in-person payment processing on behalf of a platform's users after account structure and necessary resources are designed and created. It names the merchant account, store, balance platform and user balance account, then sketches payment-method setup, payment processing, splits, settlement and payout. It is an orientation to separate procedures, not an implementation recipe or evidence of a completed payment or funds movement. [[adyen]] [[adyen-platforms]]

## Key takeaways

- **Actors and account route:** users are third-party sellers, service providers or contractors selling to their customers. Adyen describes payments passing through a user's store into the merchant account, with funds then moving into the balance platform and split between balance accounts. Settlement and later payout to the user's verified transfer instrument are subsequent stages. This narrative does not assign legal seller, merchant of record or fund ownership for a particular transaction.
- **Payment methods:** the page says methods are added to users' stores during onboarding and can be added or removed later. It lists Management API request, get and update routes for merchant payment-method settings. A request or settings read does not establish that a method is enabled, supported for a given user, or successful in a transaction; the separate method guide owns those qualifications.
- **Split choice:** per-transaction instructions can allocate sale amount, platform commission, transaction fees and other amounts among balance accounts. The page routes manual online splits to Checkout API, manual in-person splits to Terminal API, and store-based automatic profiles to Management API. Split instructions supplied in an API request override instructions in the profile.
- **Settlement timing:** captured user funds are assigned to independent balance-account settlement batches, each tied to a sales day. A configured settlement model controls which funds enter a batch, while a settlement delay controls when batch funds become available. The page gives no specific timing, currency, fee, capture or payout outcome.
- **Evidence boundary:** the flow-of-funds diagram and ordered steps are a conceptual path. No API payload, webhook, account state, bank receipt, legal-entity verification or completed split/settlement/payout is shown. The detailed general, online, POS, payment-method, automatic-split and payout guides remain separate routes.

## Detail locators

- Raw lines 15–29: after-resource prerequisite, online/POS scope and glossary of user, merchant, store, balance platform and balance account.
- Raw lines 31–38: illustrative payment-method-to-store-to-balance-to-settlement-to-payout sequence.
- Raw lines 40–54: payment-method onboarding and Management API request/read/update routes.
- Raw lines 56–66: sale/commission/fee split purpose, request-over-profile precedence and channel-specific API routes.
- Raw lines 68–78: flow diagram, independent balance-account settlement batches, settlement model and delay.

## Related

- [[source-adyen-docs-platforms-quickstart-guide]] — parent resource and account-structure orientation.
- [[source-adyen-docs-platforms-online-payments]] — online channel details.
- [[source-adyen-docs-platforms-in-person-payments]] — POS channel details.
- [[source-adyen-docs-platforms-automatic-split-configuration]] — store-linked automatic split rules.
- [[source-adyen-docs-platforms-payment-methods-api]] — payment-method settings and qualification details.

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/payments/2026-09-15|Platforms payments quickstart, fetched 2026-09-15]]
