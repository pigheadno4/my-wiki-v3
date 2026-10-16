---
title: "Adyen for Platforms user-verification process"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-overview"
raw_files:
  - "adyen/docs/platforms/verification-overview/2026-09-15.md"
tags: [adyen, platforms, verification, capabilities, deadlines]
---

## Overview

This Adyen for Platforms **verification-process overview** (last modified 2023-12-29, captured 2026-09-15) explains Adyen's checks of platform users before it allows capabilities used to process payments, pay out funds or offer financial products. Capabilities are actions granted after verification, not merely a legal-entity record, account-holder creation or requested setting. The guide covers initial capability requests, later data changes, periodic data reviews, deadlines and asynchronous status updates. It does not establish any particular user's allowed capability, legal compliance, successful payment or money movement.

## Key takeaways

- During platform design, default capabilities are requested when each new user/account holder is onboarded; additional capabilities can be requested later and can require more verification. To decide if a user can perform a **specific** action, inspect that user's capability settings. The overview links to separate capability and verification-type detail pages rather than defining all eligibility rules or country/product matrices.
- A data change after a capability is allowed triggers reverification. If updated data fails, Adyen **may** set a deadline while previously allowed use continues; unresolved issues can disallow the capability. The page cautions that `balancePlatform.accountHolder.updated` occurs only for account-holder capability-related changes, **not** for legal-entity data changes alone. This limits what a platform can infer from the absence of that event.
- Required or platform-requested data review checks the user's existing legal entity/arrangement and associated entities such as UBOs and signatories. The user must confirm the data and, where necessary, correct errors by the deadline. Review is final only after **both** confirmation and resolution of verification errors. A proactive review also receives a deadline; allowed capabilities may continue during it, but failure to confirm/resolve leads to disallowance.
- Verification deadlines are available only in **Legal Entity Management API v3 and v4**. The table gives **standard** 30-day and 60-day groups by capability, but monitoring or further checks can shorten or remove a deadline. The final date is for required information/documents to be **submitted and verified by Adyen**; mere upload by the date is insufficient. Inspect the account holder in Customer Area or `GET /accountHolders/{id}` for actual deadline and capability state rather than applying a universal timer.
- The workflow is asynchronous. Multiple checks can produce errors while the overall capability status remains `pending`; the page recommends waiting for completion/`invalid` before contacting Adyen. A successful verification can allow the capability; a `rejected` status means Adyen has reasons not to allow it. Its sample account-holder response juxtaposes `allowed`, `requested`, `enabled`, `verificationStatus`, deadlines and errors, so none should be collapsed into a single “verified account” flag. Webhooks provide verification updates, but exact operational state requires the relevant account-holder/capability record.

## Detail locators

- Raw lines 15–29: KYC purpose, user capability decision and routes to settings.
- Raw lines 30–52: initial/default/additional capability requests, data-change reverification, optional deadline and account-holder webhook qualifier.
- Raw lines 56–72: periodic/proactive reviews, confirmation-plus-error condition, LEM v3/v4 deadline availability and deadline meaning.
- Raw lines 74–101: standard 30/60-day capability table, adjustability and account-holder lookup routes.
- Raw lines 103–155: illustrative account-holder response with capability flags, verification status, deadline and errors.
- Raw lines 157–208: asynchronous initial, changed-data and review workflows; `pending`, `invalid`, `rejected` and disallowance branches.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform-user/account-holder, onboarding and capability context.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-overview/2026-09-15|Platforms verification overview, fetched 2026-09-15]]
