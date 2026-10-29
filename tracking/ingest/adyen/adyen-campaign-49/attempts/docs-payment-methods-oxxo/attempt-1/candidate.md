---
title: "Adyen OXXO payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oxxo"
raw_files:
  - "adyen/docs/payment-methods/oxxo/2026-09-15.md"
tags: [adyen, oxxo, mexico, voucher, cash, online-payments]
---

## Overview

This 2026-09-15-captured Adyen overview describes OXXO as a Mexican voucher-based method: the shopper orders online, receives a voucher, and pays cash at an OXXO store. It summarizes the delayed confirmation and voucher-expiry behavior, a method capability table, and integration routes. It is not a complete API or SDK recipe, merchant-eligibility determination, or evidence that any issued voucher was paid. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Shopper payment journey:** At online checkout, the shopper selects OXXO and receives a voucher, then prints and presents it to an OXXO cashier to pay cash. Voucher issuance does not itself mean the shopper paid. When payment succeeds, OXXO sends confirmation to Adyen, typically within one business day but possibly later depending on OXXO processing. [Raw: lines 23–29]
- **Unpaid voucher timing:** The page says a voucher unpaid before its due date leaves the corresponding transaction open in Customer Area for seven days, after which the voucher expires. It does not define the due-date calculation or say that every issued voucher expires exactly seven days after issuance. Treat pending/open state separately from confirmed payment. [Raw: lines 29–31]
- **Captured capability matrix:** The table labels OXXO **Cash and ATM**, voucher flow, **MX** country and **MXN** currency. It marks recurring, refunds (including partial and multiple partial), separate/partial/multiple partial captures, and chargebacks unavailable. These are captured method-level indicators, not a merchant-specific configuration or a current eligibility guarantee. [Raw: lines 33–35]
- **Integration routes:** The page links Web prebuilt UI, API-only merchant-built UI for website/iOS/Android, Pay by Link, and in-person payments. The linked routes are navigation; this overview does not specify their request fields, action types, SDK versions, or redemption procedure. [Raw: lines 37–61]

## Detail locators

- Mexican cash-voucher journey, confirmation latency and unpaid expiry: pinned raw lines 23–31.
- MX/MXN and capability matrix: pinned raw lines 33–35.
- Web, API-only, Pay by Link and in-person routes: pinned raw lines 37–61.
- General related links: pinned raw lines 63–68; these do not add OXXO-specific 3DS or capture behavior.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/oxxo/2026-09-15|OXXO overview, captured 2026-09-15]]
