---
title: "Adyen Payout Service custom payout schedules"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/scheduled-payouts"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/scheduled-payouts/2026-09-15.md"
tags: [adyen, payouts, payout-service, schedules, balance-accounts]
---

## Overview

This 2022-modified, 2026-09-15-captured [[adyen]] Payout Service guide configures **custom scheduled payouts** from a balance account to a verified bank-account transfer instrument. A schedule defines when and how much to transfer, possibly retaining a balance or waiting for a minimum trigger. When all conditions are met it **initiates a transfer request**; schedule creation or triggering does not itself prove debit, payout completion, or bank receipt. Bank-method and region cutoff times affect expected arrival. This is separate from legacy Online Payout API staged review. [[adyen-payouts]]

## Key takeaways

- The page requires a Payouts integration, a Transfers API credential with **TransferService Webservice Initiate**, Customer Area **Balance platform base** and **Configure scheduled payouts** roles, the user's **sendToTransferInstrument** capability, and account holder and transfer instrument linked to the same legal entity. Transfer/transaction webhook subscription is offered for tracking, and route calculation is recommended to reduce failure risk. See raw lines 23–38.
- In Customer Area, create a schedule for a balance account, select **Pay out to another account** and a transfer instrument, and configure currency, all available/fixed/maintained balance behavior, optional minimum trigger, frequency/timing and transfer priority. Weekly/monthly schedules require a day. Higher priority incurs higher fees. The date/time, balance/amount and trigger conditions jointly govern initiation. See raw lines 40–95.
- The example describes USD 150 at the start of each month only if balance exceeds USD 250, but its displayed field table does **not** show a minimum-balance trigger; do not infer that the shown configuration by itself enforces USD 250. See raw lines 73 and 101–117.
- The guide calls the beneficiary reference a statement identifier, but bank-visible characters vary by route and can be zero in the related [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-statement]] matrix. Configuring a reference is not proof of its display. See raw line 88 and that source's route-specific matrix.
- After a sweep triggers a transfer request, use Customer Area or Transfer webhooks for transfer status, and Transaction webhooks for the balance-account debit. The `event` array carries prior transfer events and `sequenceNumber` counts webhooks; neither schedule setup nor `transfer.created` alone proves funds were deducted. See raw lines 119–141. Scheduled-transfer details can show upcoming and completed entries (raw lines 143–159).

## Detail locators

- **Requirements, roles, capability and same-legal-entity condition:** raw lines 23–38.
- **Schedule conditions and Customer Area configuration:** raw lines 40–95.
- **Example and omitted trigger field:** raw lines 101–117.
- **Transfer versus transaction webhook tracking:** raw lines 119–141.
- **Customer Area schedule detail view:** raw lines 143–159.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-statement]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/scheduled-payouts/2026-09-15|Adyen custom payout schedules — collected 2026-09-15]]
