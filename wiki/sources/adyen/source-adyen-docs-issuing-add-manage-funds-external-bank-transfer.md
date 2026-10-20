---
title: "Adyen Issuing: External bank transfer funding"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/external-bank-transfer"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/external-bank-transfer/2026-09-15.md"
tags: [adyen, issuing, balance-accounts, bank-transfers, funding]
---

## Overview

This 2026-09-15-captured Adyen Issuing guide describes **push-based** funding: the sender initiates a bank transfer from an onboarded external bank account to an Adyen-provided funding account. Adyen matches the incoming transfer to the verified transfer instrument and books it to the **account holder's primary balance account**, where funds become available for the associated issued card. This is distinct from Adyen-initiated pull top-ups.

## Key takeaways

- Adyen provides the platform's funding bank-account details (for example, IBAN or routing/account number). The sending bank account must be onboarded as a `transferInstrument` linked to the account holder's main legal entity and verified before funds are sent. The transfer must originate from that onboarded account; Adyen says it cannot match funds from an unregistered account. See raw lines 33–45, 59 and 84–94.
- Confirm that the account holder's **primary** balance account is the one linked to the card being funded. The guide says incoming transfers are booked there; to fund a non-primary account, first fund the primary account and then transfer internally. See raw lines 49–57.
- Issuing support, Transfer webhook subscription and the account holder's `receiveFromTransferInstrument` capability are requirements. Request and complete verification for the account holder, legal entity and transfer instrument; the capability must be **allowed** before sending. Sending earlier can delay funding. See raw lines 23–31 and 59–67, 94.
- Processing may take the same day to a few business days and varies with region, currency, bank network, cutoffs and holidays. For incoming `category: bank`, `type: bankTransfer`, `direction: incoming` webhooks, `received` and `authorised` are intermediate; `balancePlatform.transfer.updated` with `status: booked` indicates that funds have been added to the primary balance account and are available. The page also gives Customer Area and `GET /balanceAccounts/{id}` balance checks. See raw lines 69–82 and 96–125.

## Detail locators

- Funding-account destination, primary-account selection, onboarding and verification: [[raw/adyen/docs/issuing/add-manage-funds/external-bank-transfer/2026-09-15|raw lines 33–67]].
- Timing, send-from-registered-account rule and availability confirmation: [[raw/adyen/docs/issuing/add-manage-funds/external-bank-transfer/2026-09-15|raw lines 69–125]].

## Related

- [[adyen-issuing]] — Issuing balance-platform model and source catalog.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/external-bank-transfer/2026-09-15|External bank transfer (captured 2026-09-15)]]
