---
title: "Legal entity management resources | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/account-structure-resources/legal-entity-management"
raw_files:
  - "adyen/docs/business-accounts/account-structure-resources/legal-entity-management/2026-09-15.md"
tags: [adyen, business-accounts, legal-entities, verification, platforms]
---

## Overview

This 2026-09-15-captured Business Accounts account-structure page defines the legal-entity-management resources used to supply user information for Adyen verification on a balance platform. It says verification is required before processing payments, paying out user funds, or offering financial products, and points to the Legal Entity Management API to manage the resources. The page is a resource map, not a verification outcome or a claim that an account is open. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- The page says to create a legal entity and associated resources for users so Adyen receives the information needed for verification. Its resource list names a **legal entity** with user details such as organization name, address and tax data; a **transfer instrument**, described as the user's verified bank account for receiving payouts; and a **supporting document** that helps verify information about the legal entity or transfer instrument. See raw lines 19–31.
- The Legal Entity Management API is identified as the management interface. The page references an image showing resource connections, but the captured Markdown does not describe those relationships in text. Do not infer a precise association cardinality or lifecycle from the inaccessible diagram. See raw lines 31–33.
- Creating these records or supplying a document does not itself establish that Adyen completed verification, that bank-account ownership was confirmed, or that a payout, Business Account opening, or funding occurred. Use the verification and account lifecycle guides for those separate outcomes.

## Detail locators

- Verification prerequisite framing: raw lines 17–21.
- Resource types and stated purposes: raw lines 23–29.
- LEM API and diagram pointer: raw lines 31–33.

## Related

- [[source-adyen-docs-business-accounts-account-structure-resources]] — broader Business Accounts structure map.
- [[source-adyen-docs-business-accounts-manage-legal-entities]] — legal-entity API management.
- [[source-adyen-docs-business-accounts-verification-overview]] — verification process and capability outcomes.
- [[adyen-business-accounts]] — product context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/account-structure-resources/legal-entity-management/2026-09-15|Legal entity management raw capture]]
