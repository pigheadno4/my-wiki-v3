---
title: "Adyen DOKU Web Components"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/doku/component"
raw_files:
  - "adyen/docs/payment-methods/doku/component/2026-09-15.md"
tags: [adyen, doku, indonesia, web-components, bank-transfers, convenience-stores]
---

## Overview

This [[adyen]] guide adds DOKU's Indonesian **bank-transfer and convenience-store** payment methods to an existing **Web Components** integration. It covers Sessions/Advanced prerequisites, DOKU variant selection, versioned Component creation, account/voucher expiry and test/live setup. See [[adyen-online-payments]]. The raw page was last modified in **2019** and captured 2026-09-15; its version and availability claims are historical, not proof of current merchant eligibility or a completed payment. See raw lines 15–21 and 23–122.

## Integration and method variants

- The guide requires an existing Web Components integration in either **Sessions** or **Advanced** flow and adding the desired DOKU payment methods in Customer Area. It says no additional DOKU-specific API fields are needed. It describes `/sessions` as the default with Components **v5.0.0 or later**, and `/payments` for an additional use case; these are route descriptions, not a claim that a base request can omit general payment fields. See raw lines 23–54.
- With **Web Components v6**, import `Doku` from `@adyen/adyen-web`; the import-resource link at raw line 43 points to a **Drop-in** integration despite this page saying **Components**, so use the stated Components context and version-specific source rather than that URL as proof of matching prerequisites. For **v6.0.0 or later**, the Alfamart example uses `new Doku(checkout).mount(...)`; for **v5.x.x or earlier**, it uses `checkout.create('doku_alfamart').mount(...)`. Alfamart is the **example variant**, not the only DOKU method. The raw contains a stray `**` marker between version sections at line 94; it is not an instruction. See raw lines 41–47 and 72–102.
- The variant table distinguishes convenience-store **Alfamart** (`doku_alfamart`) and **Indomaret** (`doku_indomaret`) from seven bank-transfer methods: Permata, BCA, BNI, BRI, CIMB, Danamon and Mandiri. **BCA** (`doku_bca_va`) and **BRI** (`doku_bri_va`) are marked **only available with a local entity**. The table's type strings are method-specific; choosing `Doku` or the Alfamart example does not imply every variant is enabled for a merchant. See raw lines 56–72.
- Virtual bank accounts and convenience-store vouchers are valid for **48 hours by default**; changing validity requires contacting Support. Voucher language can be set to Indonesian using locale `id-ID`. These are validity and presentation settings, not proof funds arrived, payment was authorized or expiry was changed. See raw lines 104–108.

## Testing and outcome boundary

- The page points to **test vouchers and card numbers** to simulate DOKU payments, and to the **test Customer Area** Payments list for status. Before **live** acceptance, it says to submit a request for one or more DOKU Indonesian online-banking or convenience-store payment methods in the **live Customer Area**. Submission is not approval; simulator or list lookup is not evidence that a particular bank transfer/cash voucher was paid. See raw lines 110–116.
- This Component guide links Webhooks but does not itself specify which notification/final-state event to use for fulfillment. The separate DOKU overview covers authorization-webhook timing. Do not treat Component mount, account/voucher issue or redirect as final payment proof. See raw lines 118–122.

## Detail locators

- **Sessions/Advanced prerequisites and API routes:** raw lines 23–54.
- **Variant table and local-entity restrictions:** raw lines 56–72.
- **Web v6 import and v5/v6 Component creation:** raw lines 41–47 and 74–102.
- **48-hour default validity and locale:** raw lines 104–108.
- **TEST simulation/status and live method request:** raw lines 110–116.

## Related

- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/doku/2026-09-15|DOKU overview]] — payment lifecycle and authorization-webhook context; separate from this Component setup.
- [[raw/adyen/docs/payment-methods/doku/doku-api-only/2026-09-15|DOKU API-only]] — separate request and outcome flow.

## Raw Sources

- [[raw/adyen/docs/payment-methods/doku/component/2026-09-15|DOKU Web Components — captured 2026-09-15]]
