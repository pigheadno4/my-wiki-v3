---
title: "Affirm Web Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/web-component"
raw_files:
  - "adyen/docs/payment-methods/affirm/web-component/2026-09-15.md"
tags: [adyen, affirm, web, components, financing, capture]
---

## Overview

This 2026-09-15 Adyen guide adds Affirm to an **existing Web Components** Sessions or Advanced integration. It covers shopper/request data, version-specific Component mounting, optional address/form configuration, a consequential **28-day capture deadline**, and separate test/live credential gates. It does not prove current financing eligibility, approval, authorization, capture, settled funds or live activation. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Base setup:** build the matching Web Components Sessions or Advanced flow and add Affirm in Customer Area. For Web Components **v6**, import `AdyenCheckout` and `Affirm`; v6.0.0+ mounts `new Affirm(checkout)`, whereas v5.x.x or earlier uses `checkout.create('affirm')`. The v6 import link itself carries Drop-in parameters despite this Components page, so follow the Components flow for actual setup. The `/sessions` tab calls Components v5.0.0+ its default. See raw lines 19–53 and 1259–1289.
- **Both `/sessions` and `/payments` tables** mark `shopperName` (first/last), `telephoneNumber` and `shopperEmail` required. `shopperReference` is optional here with minimum length three. The `countryCode` Required cell is blank, but its description explicitly makes it **required for Canada or the UK**, because omission defaults to **US**. For billing/delivery addresses, `stateOrProvince` is required in Canada and US, optional in UK; absent delivery address falls back to billing address. `lineItems` are optional and recommended to improve approval rates, not required or a guarantee of approval. See raw lines 51–64 and 766–779.
- **Advanced sample scope:** `/payments` curl uses `paymentMethod.type=affirm` and a v72 TEST endpoint, while `/sessions` curl uses v69 TEST; neither example sets a universal API minimum. Both curl examples contain literal `{hint:...}billingAddress{/hint}` and delivery-address keys, so are not copy-ready JSON field names. The Advanced language samples vary in age/shape; rely on the endpoint table and current API reference for implementation. See raw lines 66–126, 781–844 and 845–1258.
- **Form options:** `allowedCountries` controls **address dropdown options**, default **US/CA**, with GB in the listed possible values. This is UI configuration, not evidence of approval or merchant market eligibility. `data` can pre-fill personal/billing/delivery fields; visibility groups can be `hidden`, `readOnly` or `editable`. A `readOnly` group **must** have corresponding pre-filled information. Defaults are company/bank hidden and personal/billing/delivery editable. See raw lines 1291–1397.
- **Capture:** after goods are sent, capture is required within **28 days**; the guide says capture starts the shopper's installment schedule, while an uncaptured authorization expires after 28 days. If fulfilling less than authorized, it instructs capturing the authorized amount and **refunding the difference after capture**, rather than a lower capture. This payment-method-specific instruction should not be replaced by a generic partial-capture assumption. See raw lines 1399–1403. [[adyen-payment-capture]]
- **Test/live:** obtain TEST credentials from Affirm; after reviewing test transactions, Affirm provides live-processing credentials. The merchant also submits an Affirm request in **live Customer Area** and provides its Affirm live credentials to Adyen before accepting live payments. A TEST transaction or form render does not prove that gate is complete. See raw lines 1405–1411.

## Detail locators

- Flow prerequisites, v6 import and endpoint tables: raw lines 19–64 and 766–779.
- Sessions/Advanced language request examples and literal hint keys: raw lines 66–765 and 781–1258.
- Component mounting by v6 versus v5: raw lines 1259–1289.
- Allowed-country dropdown, pre-fill and visibility rules: raw lines 1291–1397.
- Capture deadline/refund-after-capture and test/live gates: raw lines 1399–1411.

## Related

- [[adyen-online-payments]] — Web Components payment route.
- [[adyen-payment-capture]] — Affirm capture deadline and refund-after-capture qualification.

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/web-component/2026-09-15|Affirm Web Component, captured 2026-09-15]]
