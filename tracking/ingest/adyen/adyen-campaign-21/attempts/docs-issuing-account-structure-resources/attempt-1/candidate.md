---
title: "Adyen Issuing account structure and resources"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/account-structure-resources"
raw_files:
  - "adyen/docs/issuing/account-structure-resources/2026-09-15.md"
tags: [adyen, issuing, account-structure, balance-platform]
---

## Overview

This 2026-09-15 snapshot of Adyen's Issuing account-structure guide explains the enterprise and embedded integration roles, how the company's merchant accounts connect to a balance platform, and which balance-platform resources represent users, cards and the business. It is a structure guide, not evidence of current eligibility or a live card transaction. See [[adyen-issuing]] and [[adyen]].

## Key takeaways

- In **enterprise issuing**, the organization issues business cards to its own employees or departments and is the primary entity responsible for card funding through payments or top-ups. In **embedded issuing**, a platform or marketplace offers cards to independent business users; those users issue cards to their employees or departments and are responsible for funding them. The roles are distinct in the source's “Issuing integration types” section (raw lines 26–34).
- A company account represents the core business and holds one or more merchant accounts. A merchant account is where Adyen processes payments for the business and bills it for Adyen services. Merchant accounts connect to the balance platform, which accounts for funds within the business (raw lines 36–60).
- To allow a user to use Issuing, the guide says to create an account holder linked to that user's balance account and main legal entity, a balance account holding the user's funds, and a payment instrument linked to the balance account. An Adyen-issued-card payment deducts funds from that user's balance account (raw lines 67–71).
- The business also has a liable account holder and liable balance account on the balance platform. The latter holds business funds and **can be debited if user balance accounts become negative** (raw lines 73–79).

## Detail locators

- Merchant-account configuration, when processing payments with Adyen, and the single versus multiple merchant-account discussion: raw lines 38–45. The different regional merchant-account example is illustrative.
- The balance platform can manage funds users spend by card. With an Adyen for Platforms integration, the page also describes splitting incoming sales funds between platform and users and says a separate balance platform is required for each payment-acquiring region: raw lines 58–66. This is scoped to that integration and acquisition context.
- Management API and Configuration API navigation, plus the statement that Adyen creates the business-side balance-platform resources immediately listed above it: raw lines 47–56 and 73–79. The guide separately says you must create the user resources at lines 67–71.

## Related

- [[adyen-issuing]] — Issuing concept and related source routes.
- [[adyen-index]] — provider source index.

## Raw Sources

- [[raw/adyen/docs/issuing/account-structure-resources/2026-09-15|Adyen Issuing account structure, captured 2026-09-15]]
