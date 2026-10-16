---
title: "Adyen Platforms legal entity management resources"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/account-structure-resources/legal-entity-management"
raw_files:
  - "adyen/docs/platforms/account-structure-resources/legal-entity-management/2026-09-15.md"
tags: [adyen, platforms, legal-entities, verification]
---

## Overview

This 2026-09-15 Adyen for Platforms orientation page identifies the **Legal Entity Management (LEM) resources** created to provide information for verification of platform users before payment processing, payout of their funds or financial-product offerings. It names legal entities, transfer instruments, supporting documents and business lines, and routes to the LEM API and separate onboarding, account-holder and balance-account guides. Resource creation and the diagram are not proof that a particular user passed verification, holds an allowed capability, can process a payment, received a payout or is merchant of record. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- A **legal entity** carries user information such as legal name, address and tax data for verification checks. A **business line** records the user's industry and source of funds. Neither is the account holder API resource or a balance account, and this brief page does not state a universal one-to-one mapping among them.
- A **transfer instrument** is described here as the user's verified bank account for receiving payouts; a **supporting document** helps Adyen verify information about a legal entity or transfer instrument. That type description does not establish that any named bank account or document has passed review, that funds were sent, or that a bank received them.
- The page says these resources are created for platform users and can be managed with the **Legal Entity Management API**. Its linked verification-requirements URL is under the Issuing path; this is navigation, not evidence that every platform user has issuing or other optional products. The diagram asset is an account-structure illustration, not a transaction or legal-role determination.
- The page links separate onboarding steps, legal-entity, account-holder and balance-account management guides. Those linked guides own operation details, roles, version/country rules and status consequences; none is established by this 39-line orientation page alone.

## Detail locators

- Verification purpose and prerequisite framing: pinned raw lines 15–21.
- Four LEM resource descriptions and API/diagram route: pinned raw lines 23–34.
- Separate onboarding/account-holder/balance-account guides: pinned raw lines 36–39.

## Related

- [[adyen-platforms]] — provider hub for the wider platform resource and payment-flow model.
- [[source-adyen-docs-platforms-account-structure-resources]] — broader current-Platforms account-resource map, separate from this LEM-specific orientation.

## Raw Sources

- [[raw/adyen/docs/platforms/account-structure-resources/legal-entity-management/2026-09-15|Adyen Legal entity management resources, captured 2026-09-15]]
