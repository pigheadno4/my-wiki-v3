---
title: "Adyen Capital webhook structures and event types"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/webhook-types"
raw_files:
  - "adyen/docs/capital/webhook-types/2026-09-15.md"
tags: [adyen, capital, platforms, webhooks, grants, transfers]
---

## Overview

This 2026-09-15 Adyen Capital navigation/reference page maps business-financing events to **Capital offer/grant**, **Transfer** and **Transaction** webhook families. An offer or grant lifecycle notification has a different subject from a grant-related funds movement or booked balance-account transaction. The page identifies event names and correlation fields; it supplies no specific user's successful offer, funded grant, debt outcome or bank receipt.

## Key takeaways

- Capital webhooks include dynamic-offer `balancePlatform.capital.dynamicOffer.created`, static-offer `balancePlatform.balanceAccountHolder.capitalOffer.created`, and grant `balancePlatform.grants.created`/`balancePlatform.grants.updated`. Offer creation is for an account holder and does not mean an offer was accepted or a grant paid out. The page says **grant initiation status updates generate only Capital notifications**, not Transfer or Transaction notifications.
- Grant-related movement uses `balancePlatform.transfer.created` and `balancePlatform.transfer.updated`. Identify relevant transfers with `category=grants`, then preserve the **transfer's** `type` and `direction`: grant disbursement is `grant`/incoming; regular repayment is `repayment`/outgoing; unscheduled repayment involves `capitalFundsCollection` **and** `repayment` with incoming and outgoing directions. The counterparty can identify a balance account or transfer instrument. The envelope event `type` and the nested transfer `type` answer different questions.
- `balancePlatform.transaction.created` is described as a transaction notification after a transfer is **booked in a balance account**, used to confirm when grant funds are deposited into a user's balance or credited for repayment. The stated join is `transfer.id` to the grant-fund-movement transfer ID, and `transfer.reference` to the grant ID listed in the related transfer. A transaction event needs matching identifiers, account/direction and real event state before inferring its meaning; it is not evidence of an external bank's receipt.
- The overview says the webhooks have a `type` and a `status` field to differentiate event and outcome, but this hub page does **not** enumerate status values or full payload schemas. Follow its child Capital/grant and fund-transfer pages or API references for stage semantics. It does not list a Configuration webhook or a deprecation/migration rule for any event name; do not infer either from this taxonomy.

## Detail locators

- Opening and `## Capital dynamic offer webhook` / `## Capital static offer webhook` / `## Capital grant webhook`: event families, offer/grant subjects and initiation-notification boundary.
- `## Transfer webhook`: transfer-created/updated event names; grant-related category, subtype, direction and counterparty matrix.
- `## Transaction webhook`: post-booking event and transfer-ID/grant-reference join fields.
- `## Next steps`: detailed grant-lifecycle and fund-transfer webhook children.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-webhook-types-capital-webhooks]] — grant/offer child reference.
- [[source-adyen-docs-capital-webhook-types-fund-transfers-webhooks]] — fund-transfer child reference.
- [[adyen-platforms]] — platform webhook context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/webhook-types/2026-09-15|Adyen Capital webhook types guide (fetched 2026-09-15)]]
