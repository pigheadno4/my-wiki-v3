---
title: "Adyen Issuing: Legal entity management resources"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/account-structure-resources/legal-entity-management"
raw_files:
  - "adyen/docs/issuing/account-structure-resources/legal-entity-management/2026-09-15.md"
tags: [adyen, issuing, legal-entities, verification, account-structure]
---

## Overview

This Adyen Issuing account-structure page names the Legal Entity Management resources the platform creates for its users so Adyen can collect information for verification. Adyen says users must be verified before payment processing, payouts, or financial products are offered. The page was captured 2026-09-15 and marked last modified that day. It describes resource roles for [[adyen-issuing]], not a completed verification or an account's eligibility.

## Key takeaways

- The platform must create legal entities and associated resources for its users and provide the information Adyen requires to verify them (raw lines 19–25).
- A **legal entity** contains user information such as organization name, address, and tax data for Adyen's verification checks. A **transfer instrument** is the user's verified bank account for receiving payouts; this is a distinct resource from the legal entity and from an Issuing card or balance account (raw lines 27–28).
- A **supporting document** helps Adyen verify information about the legal entity or transfer instrument. A **business line** records the user's industry and source of funds (raw lines 29–30). The page does not specify the full country-, entity-, or capability-dependent evidence checklist; follow the linked verification requirements for that detail.
- The Legal Entity Management API is named as the management interface for these resources (raw line 32). The linked diagram is navigation only in this text capture; the page does not prove resource creation or a successful verification outcome.

## Detail locators

- Verification purpose and prerequisite: raw lines 15–21.
- Four named resource definitions: `Resources`, raw lines 23–30.
- Legal Entity Management API and linked structural diagram: raw lines 32–34.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-account-structure-resources]] — broader Issuing account structure.
- [[source-adyen-docs-issuing-manage-legal-entities]] — legal-entity creation and management.

## Raw Sources

- [[raw/adyen/docs/issuing/account-structure-resources/legal-entity-management/2026-09-15|Adyen Issuing legal entity management resources, captured 2026-09-15]]
