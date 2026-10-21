---
title: "Adyen Payout Service: Getting paid"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/2026-09-15.md"
tags: [adyen, payouts, payout-service, balance-platform, transfer-instruments]
---

## Overview

This [[adyen]] Payout Service guide, last modified 2024-06-06 and captured 2026-09-15, explains how funds from payments processed for a merchant move from its merchant account to its balance platform and are held in its balance account before payout to its company bank payout account (a transfer instrument). Scheduled and on-demand payouts are the two routes. It belongs under [[adyen-payouts]], while its Payout Service/balance-platform model is distinct from the legacy Online Payout API described elsewhere in that concept. A request, schedule or processing estimate does not prove beneficiary bank receipt.

## Key takeaways

- The page requires a **Payouts integration**. Managing payout accounts in Customer Area requires **Merchant manage bank accounts**. The company's payout account is a transfer instrument; it can be created for a first account or additional currencies and used once its status is **valid** after verification. The source describes bank-login verification as instant, but a valid status is still the stated use gate. See raw lines 23–56.
- Editing a transfer instrument takes effect instantly. Deleting it stops future payouts to that instrument and **cannot be undone**; schedules and on-demand payouts still referencing the deleted ID fail. For rotation, the page instructs adding a new instrument, updating dependent schedules/requests, verifying receipt on the new one, then deleting the old. See raw lines 58–68.
- The guide distinguishes Regular, Instant, Fast, Wire, Cross-border and Internal priorities; higher priority may incur higher fees. Cross-border can involve intermediary delays, lifting fees and beneficiary receipt below the instructed amount. Its “Instant” description is geographically scoped to US, Australia, UK and SEPA, not a general arrival guarantee. See raw lines 70–86.
- Cut-off times, settlement delays, amount bounds and priorities vary by recipient location and currency. Before/after cut-off examples are illustrative. The SEPA wire example uses a 16:30 PM ET cut-off, while the table lists SEPA EUR Wire at 16:55 CET; do not reconcile these into a single operational cut-off. Consult the dated table and current provider settings before relying on a time or limit. See raw lines 88–155.
- To receive both local and cross-border payouts at one bank account, the guide says to create two transfer instruments with distinct account-identification types: local and `numberAndBic`. Local payouts are within the same country/currency; cross-border supports only `crossBorder` priority here, with a stated exception for USD to US banks when the legal entity is in Canada or Hong Kong. Arrival times are not guaranteed, and correspondent-bank fees/geographic restrictions may apply. See raw lines 215–287.
- Recipient-country/region and currency/priority/account-format tables are snapshot-specific (raw lines 157–213 and 246–287). The bank account data in the success/failure tables is **TEST-environment only**, for POST `/transfers` test flows; examples include return and failure reason codes, not live recipient instructions or real payout outcomes. See raw lines 289–435.

## Evidence boundary

The page opens with a link to separate third-party bank/card payout guides (raw lines 19–21). Its principal “getting paid” flow is the company's own payment proceeds to its payout-account transfer instrument, so references to a “user's account” in the priority paragraph (raw line 72) do not redefine the principal owner or authorize third-party disbursement by this page. The source does not establish current integration approval, payout eligibility, a live priority SLA, booking, final bank credit or bank receipt.

## Detail locators

- Own-account funds path, requirements, verification and irreversible deletion: raw lines 19–68.
- Priorities and dated cut-off table: raw lines 70–155.
- Supported destination regions and local/cross-border formats: raw lines 157–287.
- TEST payout and return/failure account fixtures: raw lines 289–435.

## Related

- [[adyen-payouts]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/2026-09-15|Payout Service getting-paid guide, 2026-09-15 capture]]
