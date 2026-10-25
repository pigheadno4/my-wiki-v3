---
title: "Adyen Rakuten Pay API-only guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/api-only"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/api-only/2026-09-15.md"
tags: [adyen, rakuten-pay, japan, api-only, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen page describes **Rakuten Pay-specific additions** to an existing API-only Web integration: merchant-owned payment form, JP/JPY method discovery, redirect handling and conditional recurring-model guidance. Its request/example contradictions require verification against the matching base/API guide; it does not establish current merchant eligibility or an authorized payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Base integration and form:** The page requires an existing API-only integration, redirect handling for **`action.type: redirect`**, and Rakuten Pay added in Customer Area. It says to list Rakuten Pay on the merchant payment form, with **no additional form fields** for this method. The shopper selects it and the existing integration handles the redirect. Those steps are not themselves final payment confirmation. (raw lines 23–40)
- **Discovery scope and mislabeled sample:** The `/paymentMethods` prose requests **`countryCode: JP`** and **`amount.currency: JPY`** so Rakuten Pay can be returned. But its “Example request for available payment methods” calls a **v72 TEST `/payments` URL**, includes `paymentMethod.type: rakutenpay`, and is paired with a `paymentMethods` response example. The sample cannot be treated as a trustworthy `/paymentMethods` request or as an executed payment; use the endpoint-specific reference/base guide to resolve the discrepancy. (raw lines 44–86)
- **Item-data contradiction:** The “How it works” list says to include **additional information about the purchased items** in the payment request, while the later `/payments` section says **no additional parameters** are needed. This snapshot gives no item schema or rule resolving the difference. Do not silently claim that item fields are mandatory or unnecessary for every merchant/use case. (raw lines 31–36, 88–90)
- **Recurring restrictions:** The page says that for subscription and unscheduled card-on-file business models, Rakuten Pay permits **one-off card-on-file transactions after a review process**. Without periodic charging cadence, it says initiating the card-on-file Recurring Processing Model is prohibited, primarily allowing it in Food & Beverage, and every Recurring Processing Model requires an application when requesting Rakuten Pay. It routes tokenization implementation elsewhere and **strongly recommends** explicit shopper permission for future recurring charges; that recommendation is not phrased as an unqualified mandate. Nothing here proves a merchant's recurring model has been approved. (raw lines 92–98)
- **TEST scope:** The page names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST, says testing redirects to a DGFT simulator without the Rakuten Pay app, and points to Customer Area transaction-status checks. Despite “Test and go live,” it gives no separate live setup procedure or final result/webhook semantics. A simulator route or status-list instruction is not authorization/settlement proof. (raw lines 100–106)

## Detail locators

- API-only/redirect/Customer Area requirements and no-extra-form-fields claim: raw lines 23–40.
- JP/JPY discovery prose versus `/payments` example/`paymentMethods` response mismatch: raw lines 44–86.
- Purchased-item instruction versus no-extra-`/payments` contradiction: raw lines 31–36, 88–90.
- Recurring review, cadence/category, per-model application and shopper-permission recommendation: raw lines 92–98.
- DGFT TEST simulator and Customer Area status route: raw lines 100–106.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/api-only/2026-09-15|Adyen Rakuten Pay API-only, 2026-09-15 snapshot]]
