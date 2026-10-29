---
title: "Multibanco"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco"
raw_files:
  - "adyen/docs/payment-methods/multibanco/2026-09-15.md"
tags: [adyen, multibanco, portugal, payments]
---

## Overview

This 2026-09-15 Adyen method overview describes Multibanco for online payments in Portugal. At checkout the shopper receives a payment voucher, then pays using a debit card at an ATM or through online banking. It is a method overview and integration router, not a complete API or SDK implementation guide. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The voucher includes a payment reference, entity number, payable amount, and expiry date. The guide says merchants can ask Adyen Support to set voucher expiry according to business needs. See raw lines 23–32.
- The capability table labels Multibanco as **Cash and ATM**, **Direct**, **PT**, and **EUR**. It marks recurring and all listed capture variants unsupported; refunds, partial refunds, and multiple partial refunds supported; and chargebacks unsupported. These are the table's method-level labels, not evidence that payment is completed at checkout. The shopper still needs to redeem the voucher. See raw lines 23 and 34–36.
- This page routes to Web, iOS, Android, React Native, Flutter, API-only, Pay by Link, and in-person guidance. The API-only link is described as a way to build your own UI; the platform links are navigation, not behavioral evidence for those unread child guides. See raw **How do you want to integrate?**, lines 38–86.

> [!warning] Contradiction — API-only fulfillment wording
> [[source-adyen-docs-payment-methods-multibanco-api-only|The API-only child guide]] lists fulfillment immediately after the payment-request step (child raw lines 31–36), while this overview describes later voucher redemption at an ATM or through online banking (overview raw lines 23–32). The child also treats test payments as pending offers until promotion (child raw lines 93–104). Preserve the conflict; a request or issued voucher is not proof that payment was made. Use the applicable result and reconciliation guidance before fulfillment.

## Detail locators

- Voucher lifecycle and fields: raw lines 23–32.
- Method capability matrix: raw lines 34–36.
- Integration choices and child-guide links: raw lines 38–86.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/2026-09-15|Multibanco overview, captured 2026-09-15]]
