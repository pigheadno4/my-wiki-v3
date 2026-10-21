---
title: "Adyen Marketplaces: Configure sales-day closing time"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/settle-funds/configure-closing-time"
raw_files:
  - "adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15.md"
tags: [adyen, marketplaces, platforms, sales-day, settlement, balance-accounts]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplaces guide configures a **balance account's local sales-day closing time**. The page says the default is midnight in that account's local timezone and illustrates a restaurant moving its cutoff to 03:00 so after-midnight sales stay in the prior sales day. It also describes a separate settlement-delay setting and payment-method schedule exceptions. Configuration and its webhook are not proof of a completed settlement batch, available balance, payout or bank receipt. [[adyen-platforms]]

## Requirements and setting

- A Configuration API credential needs the **Balance Platform BCL role**. The guide calls for **Configuration webhooks**, with `balancePlatform.balanceAccount.created` for a new balance account and `.updated` for an existing one after the new time is applied. Use POST `/balanceAccounts` at creation or PATCH `/balanceAccounts/{id}` to update `platformPaymentConfiguration`. See [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 21–43, 315–320]].
- `salesDayClosingTime` uses `HH:MM` with hours **00–07** and minutes **00**; default **00:00**. The separate `settlementDelayDays` field is conditional when it differs from the merchant-account default, with **1–20 business days** or `null` for default. A later closing time does not by itself set a two-day delay or prove when funds will actually be available. See [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 19, 45–51]].
- The page states that **Afterpay, alipay_sg_pos, Clearpay, maestro_USA and PayPal** funds follow their payment-method schedule instead of the sales-day closing time. This is the Marketplace page's list; do not substitute the different exception list from the related Platforms-path source. See [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 30–34]].

## Example and evidence boundary

The sample prose describes a **01:00** sales-day cutoff with funds available after **two business days**, but the displayed TEST `/bcl/v2/balanceAccounts/{id}` PATCH body sets only `salesDayClosingTime=01:00` and does **not** set `settlementDelayDays`. Its illustrative response repeats **01:00**, while a later `balancePlatform.balanceAccount.updated` webhook sample displays **06:00** and different placeholder account IDs. These fragments do not prove that the sample PATCH established a two-day delay or that the webhook reports that same update. A response/configuration webhook reports settings, not actual transaction settlement or payout. See [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 49–69, 289–313, 315–343]].

## Detail locators

- Local sales-day definition, roles/webhooks, 07:00 limit and method exceptions: [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 15–34]].
- POST/PATCH route and configuration-field constraints: [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 36–51]].
- TEST PATCH, versioned SDK illustrations, response and webhook example: [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|raw lines 53–343]].

## Related

- [[adyen-platforms]] — platform balance-account and settlement route.
- [[source-adyen-docs-platforms-settle-funds-configure-closing-time]] — related Platforms-path closing-time guide with its own exception list.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15|Marketplace sales-day closing-time guide (captured 2026-09-15)]]
