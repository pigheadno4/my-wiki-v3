---
title: "Adyen Marketplace legal-entity-management resources"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/account-structure-resources/legal-entity-management"
raw_files:
  - "adyen/docs/marketplaces/account-structure-resources/legal-entity-management/2026-09-15.md"
tags: [adyen, marketplaces, platforms, legal-entities, verification]
---

## Overview

This 2026-09-15 Marketplace account-structure page identifies the **Legal Entity Management resources** used to give Adyen information for user verification: a legal entity, transfer instrument and supporting document. It says Adyen must verify marketplace users before processing payments, paying out their funds or offering financial products. Creating the resources supplies verification information; the page does not say creation alone passes checks or enables those activities. [[adyen]] [[adyen-platforms]]

## Key takeaways

- A **legal entity** carries user information such as organization legal name, address and tax information for Adyen's verification checks. A **transfer instrument** is described as the user's verified bank account for payouts. A **supporting document** helps verify information about a legal entity or transfer instrument. These are separate resources with different roles, not an account holder or balance account (raw lines 23–29).
- The guide directs management of these resources through the Legal Entity Management API. Its diagram and links route to onboarding steps and separate legal-entity, account-holder and balance-account guides; it gives no request sequence, response, verification result or payout status of its own (raw lines 31–38).
- The verification prerequisite is stated across payment processing, payout and optional financial products. The page does not identify a specific user's verification status or current financial-product eligibility, and a resource label such as 'verified bank account' is not proof that a newly created transfer instrument has passed verification (raw lines 19–29).

## Detail locators

- Verification prerequisite and creation as information provision: raw lines 17–21. Resource definitions and distinct verification roles: lines 23–29. LEM API, diagram and related-guide routes: lines 31–38.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Platforms model and Marketplace route.
- [[source-adyen-docs-marketplaces-account-structure-resources-marketplace-structure]] — broader marketplace/company/user resource example.
- [[source-adyen-docs-marketplaces-manage-balance-accounts]] — separate balance-account operations.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/account-structure-resources/legal-entity-management/2026-09-15|Marketplace Legal Entity Management resources — 2026-09-15 snapshot]]
