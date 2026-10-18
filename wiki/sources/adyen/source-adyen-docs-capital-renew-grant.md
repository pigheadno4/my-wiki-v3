---
title: "Adyen Capital grant renewal"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/renew-grant"
raw_files:
  - "adyen/docs/capital/renew-grant/2026-09-15.md"
tags: [adyen, capital, platforms, grant-renewal, financing]
---

## Overview

This 2026-09-15 Adyen Capital guide describes a **limited-availability pilot** for configuring a subsequent grant while a prior grant is partially repaid. Subject to separate renewal eligibility and offer conditions, Adyen says it disburses the full subsequent grant amount and reserves the prior grant's outstanding principal for repayment. The prior and subsequent grants remain distinct. This is a documented flow, not evidence that a particular user qualifies, that principal was settled, or that new funds were paid out.

## Key takeaways

- Pilot access requires contacting Adyen. Prerequisites include an Adyen for Platforms integration supporting Capital, Balance Platform API credentials with Capital Configuration and Grant Initiation roles, user `getGrantOffers` and `receiveGrants` capabilities, Capital/Transfer/Transaction webhooks, and Capital compliance and renewal-eligibility review. The page says only **one disbursement per grant** is supported at this snapshot.
- Observe the prior grant's `balancePlatform.grants.updated` webhook or GET `/grants` for `renewal.eligible=true`, `renewal.minimumAmount`, and the prior-grant `id`. The page also points to separate eligibility requirements. These signals do not themselves supply a selected valid offer or prove that the user can receive new funds.
- For the account holder, obtain dynamic or static financing offers and present offers meeting the webhook's `renewal.minimumAmount`. The guide separately says a renewal offer must be at least **150% of the prior grant's outstanding balance**; available offers are recalculated weekly and expire after seven days. Do not treat a previously viewed offer as still valid. After selection, `receiveGrants` is disallowed until the user accepts **new** Terms of Service. Underwriting can change repayment percentage, fee, maximum amount and terms from the prior grant.
- Configure the subsequent grant by POST `/grants` with the selected `grantOfferId`, Adyen-provided `grantAccountId`, and `renewsGrantId` identifying the prior grant. The guide shows a recipient balance account or transfer instrument; omitted `counterparty.balanceAccountId` pays to the account holder's primary balance account according to its parameter table. A `Requested` API response is asynchronous acknowledgment, **not** final grant configuration or payout; wait for relevant webhook evidence.
- Track `balancePlatform.grants.created` for configuration, transfer-created/updated events for received, authorised and booked transfer stages, and `balancePlatform.transaction.created` for the described payout to a balance account or payment instrument. A later `balancePlatform.grants.updated` can report full repayment, reconfiguration or write-off. These are distinct observations; a booked transfer or sample transaction is not bank-receipt proof, and the page does not show a separate accounting record that the prior principal was actually repaid from reserved funds.
- The JSON snippets are **test examples**, not a single internally consistent live trace. The eligibility sample has `renewal.minimumAmount.value=9440625` while the illustrated transfer amount is `1850000`; grant-event outer and nested IDs also differ in ways that should not be normalized into a guaranteed join. Use actual grant, transfer, transaction, status and amount records for a real case.

## Detail locators

- Opening, `## Requirements`, and `## How it works`: pilot, prior/subsequent distinction, principal reservation, roles/capabilities/webhooks, one-disbursement limit and sequence.
- `## 1. Get a notification of grant eligibility for grant renewal`: eligibility flag, minimum amount, prior-grant ID, GET alternative and test example.
- `## 2. Get financing offers` and `## 3. Present the user with the new Terms of Service`: 150% rule, weekly recalculation, seven-day expiry, offer presentation and renewed consent.
- `## 4. Configure a subsequent grant`: POST identifiers/counterparty, `Requested` response and asynchronous final-result warning.
- `## 5. Get updates` and its five tabs: configured grant, received/authorised/booked transfer, payout transaction and subsequent-grant repayment examples.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-grant-lifecycle-and-status]] — grant-status reference.
- [[adyen-platforms]] — platform/account-holder context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/renew-grant/2026-09-15|Adyen Capital renew-a-grant guide (fetched 2026-09-15)]]
