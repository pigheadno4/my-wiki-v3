---
title: "Adyen Business Accounts: Accept UK direct debits"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/accept-direct-debits-uk"
raw_files:
  - "adyen/docs/business-accounts/accept-direct-debits-uk/2026-09-15.md"
tags: [adyen, business-accounts, direct-debit, bacs, uk, mandates]
---

## Overview

This UK Business Accounts guide was last modified in 2019 and captured on 2026-09-15. It describes a **limited-availability pilot** for a user's single or recurring direct debit, in which an authorized counterparty collects funds from the user's business account through Bacs. The platform must have Adyen for Platforms with Business Accounts, enable the user's `sendFundsToThirdParty` capability and contact Adyen to enable UK direct debits. These dated instructions do not establish present eligibility, a live approved mandate, a collected payment or beneficiary receipt. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- A mandate is the user's authorization for a counterparty to debit the user's business account. The user supplies mandate information to the counterparty, whose payment service provider forwards it through Bacs to Adyen. Adyen checks that the business account is active and has the required capability before approving the mandate and notifying the platform. Mandate approval is a separate step from any later collection.
- For a collection, the counterparty requests funds through its payment service provider and Bacs. Adyen checks that the business account is active, has the direct-debit capability, has an approved linked mandate and has enough available balance. The page says Adyen approves the collection only if those checks pass; otherwise it rejects it. It then describes Adyen notifying the platform, sending confirmation and funds to Bacs, and Bacs forwarding funds to the counterparty's provider. This described flow is not evidence that any specific debit or downstream receipt occurred.
- The guide says users can amend a mandate to use a different business account or cancel it to stop future direct debits. The depicted process extends beyond the platform API request: Adyen sends the change to Bacs, the counterparty's provider validates and applies it, and a confirmation returns through Bacs to Adyen before Adyen notifies the platform. A user action or submitted request alone does not prove the external mandate update completed.
- This UK Bacs pilot and its `sendFundsToThirdParty` requirement are distinct from the separately documented SEPA direct-debit route in [[source-adyen-docs-business-accounts-receive-funds]]. The page is a historical product guide, not current regional coverage or legal advice.

## Detail locators

- Pilot warning and UK-only prerequisites: raw lines 15–35.
- Bacs collection actors, validation and notification/funds path: lines 37–65.
- Mandate definition and user authorization fields: lines 67–73; creation/approval path: lines 75–91.
- Amendment/cancellation intent and external confirmation path: lines 93–113.
- The linked mandate-management child is navigation for API details (lines 115–119); this page does not provide those request schemas.

## Related

- [[adyen-business-accounts]] — product and capability context.
- [[source-adyen-docs-business-accounts-receive-funds]] — separate SEPA direct-debit scope.
- [[source-adyen-docs-business-accounts-third-party-transfer-webhooks]] — Transfer webhook examples for incoming direct-debit requests.

## Raw Sources

- [[raw/adyen/docs/business-accounts/accept-direct-debits-uk/2026-09-15|Adyen Docs: Accept direct debits in the UK (2026-09-15 snapshot)]]
