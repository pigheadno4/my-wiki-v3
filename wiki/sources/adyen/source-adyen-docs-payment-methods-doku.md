---
title: "Adyen DOKU Indonesia bank transfer and convenience-store payments"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/doku"
raw_files:
  - "adyen/docs/payment-methods/doku/2026-09-15.md"
tags: [adyen, doku, indonesia, bank-transfer, convenience-store, online-payments]
---

## Overview

This Adyen page, last modified 2023-02-06 and captured 2026-09-15, describes **Indonesia DOKU** bank-transfer and convenience-store cash payment methods. DOKU is identified as Adyen's partner; the shopper either transfers into an order-specific virtual account or pays a unique voucher at a store. This is an overview plus Web, API-only and Pay by Link navigation, not evidence of current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Scope and matrix:** The page labels the product Cash and ATM, an additional-action flow for **ID/IDR**. Its historical matrix marks **refunds** with a check but recurring, partial/multiple partial refunds, separate/partial/multiple partial captures and chargebacks with x. This matrix does not prove a merchant can currently use a variant, that a refund has completed, or that any settlement occurred. (raw lines 23–30)
- **Bank transfer:** The merchant collects first name, last name and email, then submits a payment request. Adyen describes creating a **virtual account unique to the order** on an interbank network. The response supplies its number, expiry time and instruction link; the merchant shows these to the shopper, who must transfer before expiry via ATM, mobile or internet banking. **Only when payment is authorised** does the guide say the merchant receives a webhook, can inspect Customer Area status and then delivers the order. Issuing an account number is not receipt of funds or authorization. The page gives no fixed lifetime value. (raw lines 32–62)
- **Bank variants:** The table lists Permata (`doku_permata_lite_atm`), BCA (`doku_bca_va`), BNI (`doku_bni_va`), BRI (`doku_bri_va`), CIMB, Danamon and Mandiri virtual-account variants. **BCA and BRI are each marked only available with a local entity**; do not extend that condition to every bank or omit it for those two. The table is a dated availability description, not live account approval. (raw lines 64–76)
- **Convenience-store cash:** The merchant again collects first name, last name and email and requests payment. Adyen describes creating a **voucher unique to the order** and returning its code, expiry time and instructions; the merchant shows them to the shopper, who presents the voucher and pays cash to a cashier. The guide places the authorization webhook/Customer Area status check before order delivery. Voucher issuance or presentation alone is not payment authorization. It names Alfamart (`doku_alfamart`) and Indomaret (`doku_indomaret`) variants. (raw lines 78–113)
- **Integration routes:** The chooser links a Web guide for prebuilt UI, an API-only guide whose card mentions website/iOS/Android custom UI, and Pay by Link. These are navigation descriptions; this page does not specify SDK/API versions, `/payments` fields, callback semantics, expiry durations, or live onboarding details for those child channels. (raw lines 115–133)

## Detail locators

- DOKU partner, ID/IDR flow and historical capabilities: raw lines 15–30.
- Bank-transfer shopper data, virtual-account response, payment and webhook sequence: raw lines 32–62.
- Bank variant types and BCA/BRI local-entity conditions: raw lines 64–76.
- Cash voucher lifecycle, Alfamart and Indomaret types: raw lines 78–113.
- Web/API-only/Pay by Link chooser routes: raw lines 115–133.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-doku-doku-web]]
- [[source-adyen-docs-payment-methods-doku-doku-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/doku/2026-09-15|Adyen DOKU Indonesia method overview, 2026-09-15 snapshot]]
