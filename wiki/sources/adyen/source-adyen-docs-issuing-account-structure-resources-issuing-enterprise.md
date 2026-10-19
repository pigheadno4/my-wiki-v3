---
title: "Adyen Enterprise Issuing account structure"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/account-structure-resources/issuing-enterprise"
raw_files:
  - "adyen/docs/issuing/account-structure-resources/issuing-enterprise/2026-09-15.md"
tags: [adyen, issuing, enterprise-issuing, account-structure, funding]
---

## Overview

This Adyen Enterprise Issuing guide (last modified and captured 2026-09-15) describes an **organization issuing business cards to its own employees or departments** for business expenses and supplier payments. That organization is the primary entity responsible for funding the cards. The guide contrasts funding with Adyen-acquired payments against standalone top-ups from a verified transfer instrument; its hotel and consultancy resource counts are examples, not universal account requirements. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- **Enterprise with acquiring:** The organization's customer/guest payments are processed through Adyen and fund its issued cards. The guide says a balance platform and merchant account are needed in each region where the organization is registered **and wishes to acquire payments**. In the hotel example, processed guest transactions settle in regional/currency merchant accounts; each merchant account's funds then settle to **one** balance account, although several merchant accounts may settle to the same balance account. Funds from one merchant account cannot be split across several balance accounts.
- **Acquiring resources and conditions:** The example has a company account, regional merchant accounts and balance platforms, an account holder defining cardholder capabilities, balance accounts, at least one issued card per balance account, verified transfer instruments usable for payout or top-up, and a business legal entity for verification. A business line in each acquiring region supplies industry information for KYC checks that must pass before card issuance. A store tied to a merchant account is required **only when processing in-person payments**; the branch/currency examples do not make three merchant accounts or two platforms universal.
- **Standalone enterprise:** The organization does **not** process payments through Adyen to fund the cards; it tops up its balance accounts from a **verified transfer instrument/bank account**. The consultancy example still has a merchant account for linking resources, a linked balance platform, an account holder, a balance account for each expected business-payment currency, at least one issued card per balance account, a verified transfer instrument for each balance account's top-up, and a legal entity for verification. A merchant-account resource in this structure does not turn standalone funding into Adyen acquiring.
- This is an account-structure and funding-model description. It does not demonstrate an organization's current regional eligibility, KYC completion, a successful top-up or settlement, an active card, or an authorised/captured supplier payment. The payment recipients in its examples are the organization's expense suppliers, rather than the card-issuing organization.

## Detail locators

- Enterprise user/funding roles and two model definitions: pinned raw lines 19–27.
- Acquiring hotel example, conditional region/store/business-line rules and regional resource structure: pinned raw lines 29–80.
- One merchant-account settlement destination versus many-to-one balance-account mapping: pinned raw lines 70–72.
- Standalone consultancy example, merchant-account link, currency accounts, cards and verified-bank top-ups: pinned raw lines 82–106.

## Related

- [[source-adyen-docs-issuing-account-structure-resources]] — parent Issuing resource model and enterprise/embedded distinction.
- [[source-adyen-docs-issuing-account-structure-resources-issuing-embedded]] — independent-business-user model with different card-funding responsibility.
- [[source-adyen-docs-issuing-payment-stages]] — issued-card payment hold, capture and debit flow.

## Raw Sources

- [[raw/adyen/docs/issuing/account-structure-resources/issuing-enterprise/2026-09-15|Adyen Enterprise Issuing account structure, captured 2026-09-15]]
