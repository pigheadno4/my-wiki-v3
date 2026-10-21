---
title: "Adyen Marketplaces verification process overview"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-overview"
raw_files:
  - "adyen/docs/marketplaces/verification-overview/2026-09-15.md"
tags: [adyen, marketplaces, platforms, verification, capabilities, onboarding]
---

## Overview

This 2023-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** page explains how Adyen verifies marketplace users and controls the actions they may perform through **account-holder capabilities**. The page says to check capability settings to determine whether a particular user can use an action; requesting a capability, sending data or seeing an example status is not verification approval. [[adyen-platforms]]

## Triggers and gates

- Marketplace default capabilities are requested when a new account holder is created; a nondefault capability needs a separate request and can require more verification. Adyen checks asynchronously and sends verification updates through webhooks. A successful check allows the capability; a `rejected` verification status does not. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 30–40, 165–180]].
- Changing data after capabilities are allowed causes reverification. Adyen **may** set a deadline after a failed check; previously allowed capabilities can continue during an active deadline, then are disallowed if the issues remain unresolved. The page says `balancePlatform.accountHolder.updated` fires for **capability-related account-holder changes**, not legal-entity data changes alone. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 44–52, 182–196]].
- In **staggered verification**, moving to a higher tier **disallows payout-related capabilities**. For accepting-payment capabilities, the page says Adyen **might in the future** add a deadline that would permit continued use while extra data is supplied; do not treat that future option as an existing guaranteed grace period. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 56–60, 198–212]].
- Periodic or proactive data review triggers checks on the main legal entity and associated people/entities. The review is finalized only when the user **confirms the data and resolves all verification errors**. Previously allowed capabilities can continue during an active deadline, but failure to confirm or resolve errors disallows them. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 64–72, 214–225]].

## Deadline and evidence boundaries

- Verification deadlines are described as available only in **Legal Entity Management API v3/v4**. The table lists standard **30-day** and **60-day** capability groups, but Adyen can shorten or remove a standard deadline after monitoring/verification. A deadline is the final date for required information and documents to be **submitted and verified**, and an active deadline can preserve only capabilities previously allowed. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 74–106]]. The table is general to the listed verification events; it does not override the page’s higher-tier future-tense caveat for accepting payments.
- Customer Area account-holder details or Balance Platform API `GET /accountHolders/{id}` show deadlines; the sample response has 2022 example dates, `verificationStatus: invalid` with `allowed`/`enabled` shown as string values, and an error. Treat it as an illustration, not current account state or an operation schema guarantee. See [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 106–161]].

## Detail locators

- Identity, capability checking and initial/change/tier/review triggers: [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 15–72]].
- Versioned, adjustable deadlines and dated response example: [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 74–161]].
- Asynchronous workflows, webhooks and trigger-specific outcomes: [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|raw lines 165–225]].

## Related

- [[adyen-platforms]] — modern Platforms verification and capability model.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15|Marketplaces verification process (captured 2026-09-15)]]
