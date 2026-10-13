---
title: "Payout webhook | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/online-payouts/payout-webhook"
raw_files:
  - "adyen/docs/online-payments/online-payouts/payout-webhook/2026-09-15.md"
tags: [adyen, payouts, payout-api, webhooks, legacy-api]
---

## Overview

This Adyen page explains webhook outcomes for the legacy Payout API's staged payouts to bank accounts or wallets and instant payouts to cards. The page says Adyen no longer accepts new Payout API integrations: new builds should use the Transfers API, and existing Payout API users should contact Adyen about migration. This 2026-09-15 snapshot reports `last_modified` 2020-10-23 and does not prove a merchant's current legacy access, payout execution, settlement, or receipt of funds.

## Key takeaways

- For bank-account or wallet payouts, `/submitThirdParty` acknowledges receipt of the request only. A payout webhook is needed to follow the request. After reviewer confirmation, `PAYOUT_THIRDPARTY` with `success=true` means Adyen received the payout request and will send it to the financial institution; the page says funds are paid out within two business days **when approved**. It is not itself proof that the financial institution approved or paid it. `success=false` means the request failed and gives a `reason` for possible correction and resubmission.
- In that staged bank/wallet flow, `PAYOUT_DECLINE` means the reviewer declined, and `PAYOUT_EXPIRE` means the reviewer neither confirmed nor declined within seven days. Both event types have `success=true` for the event, which must not be read as payout success. `PAIDOUT_REVERSED` means the financial institution rejected the payout and Adyen will return funds to the merchant account.
- For instant card payouts, the guide separately says `/payout` returns `resultCode=Received`; it describes a later `PAYOUT_THIRDPARTY`/`success=true` event for a successful payout and `success=false` if the issuer refuses it. Do not transfer the staged bank/wallet interpretation or its reviewer steps to the instant-card path.
- The JSON, SOAP and form examples are sample `PAYOUT_THIRDPARTY` notifications, not a validated production event. In the JSON and SOAP sample, `pspReference` is labeled as the payment PSP reference and `originalReference` as the payout PSP reference; use that as example-level reference navigation, not a universal correlation rule without the relevant current webhook contract.

## Detail locators

- Introductory migration notice — Payout API new-integration stop, Transfers API direction and existing-user contact route.
- `## Payouts to bank accounts or wallets` — `/submitThirdParty` acknowledgement, reviewer confirmation/decline/expiry, financial-institution decision, event codes and conditional payment timing.
- `## Instant payouts` — `/payout` `Received` response and issuer-dependent later event interpretation.
- `## Code examples` / `#### JSON`, `#### Soap`, `#### Form` — example event payloads and reference labels.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payouts]]
- Related event concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/online-payouts/payout-webhook/2026-09-15|2026-09-15 snapshot — legacy Payout API webhook outcomes]]
