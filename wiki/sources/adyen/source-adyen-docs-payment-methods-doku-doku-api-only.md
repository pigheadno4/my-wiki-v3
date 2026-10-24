---
title: "Adyen DOKU Indonesia API-only integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/doku/doku-api-only"
raw_files:
  - "adyen/docs/payment-methods/doku/doku-api-only/2026-09-15.md"
tags: [adyen, doku, indonesia, api-only, bank-transfer, convenience-store, online-payments]
---

## Overview

This Adyen page, last modified 2019-11-12 and captured 2026-09-15, describes adding **Indonesian DOKU bank-transfer and convenience-store methods** to an existing API-only integration and building a merchant-owned payment form. It supplies a voucher example and asynchronous status handling; it does not prove current method availability, merchant approval or any completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and scope:** The guide requires an existing API-only integration and addition in the **test** Customer Area. The merchant collects shopper `firstName`, `lastName` and `shopperEmail`. Its `/paymentMethods` request uses `countryCode: ID` with `amount.currency: IDR`, then selects a returned DOKU `type`. The table includes Alfamart and Indomaret convenience-store options and Permata, BCA, BNI, BRI, CIMB, Danamon and Mandiri bank-transfer options. The BCA and BRI VA rows each say **only available with a local entity**; the page does not attach that condition to every variant. (raw lines 17–62)
- **Server request:** The merchant's server sends `/payments` with the chosen `paymentMethod.type`, shopper name/email fields and `amount.value` in minor units. The example uses Alfamart, `IDR`, a TEST v68 endpoint and a `returnUrl` placeholder; it is one variant's sample request, not a requirement that all DOKU variants respond identically or proof of a payment result. (raw lines 64–95)
- **Example discrepancy:** The prose/table, curl, Node, Go, Python and Ruby examples identify Alfamart as `doku_alfamart`, while the PHP example calls `setType("alfamart")`; language-specific SDK enum examples also differ in representation. Treat the PHP spelling as a source discrepancy to check against the matching library/API version, not a universal type value. The Go block says library v10.4.0 while its import paths contain `/v9/`. (raw lines 52–68, 87–92, 117–132, 158–177, 259–299)
- **Voucher response versus payment:** The page's sample `/payments` response is `resultCode: PresentToShopper` plus an `action` voucher object with expiry, instruction URL and reference. This indicates a voucher to show, not completed payment. For this **offline voucher** flow the guide says no acquirer return redirect needs handling; a webhook reports status. Its `PENDING`/success=true row means a voucher reference was created and payment is pending; `AUTHORISATION`/success=false means reference creation failed; `AUTHORISATION`/success=true means the shopper completed payment; `OFFER_CLOSED`/success=true means the voucher expired unpaid. The `success` flag must be read with the event code, particularly for `OFFER_CLOSED`. Do not extrapolate the voucher-specific response/status table to every bank-transfer variant. (raw lines 402–445)
- **Expiry and environment:** The page says virtual-account or voucher validity is **48 hours by default**, and directs merchants to Support to change that period. It points to test vouchers, test Customer Area status checks and a **separate live Customer Area request** for one or more DOKU methods before live acceptance. Default validity and TEST examples do not establish live configuration or receipt of funds. (raw lines 447–457)

## Detail locators

- Indonesia/DOKU/API-only purpose and test setup: raw lines 15–28.
- Form fields, ID/IDR selection, method types and BCA/BRI entity caveats: raw lines 30–62.
- Server `/payments` fields, Alfamart TEST example and variant/type discrepancy: raw lines 64–95, 158–177.
- Voucher `PresentToShopper` response and asynchronous status table: raw lines 402–445.
- Default validity, support customization, TEST/live gates: raw lines 447–457.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-doku]]
- [[source-adyen-docs-payment-methods-doku-doku-web]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/doku/doku-api-only/2026-09-15|Adyen DOKU API-only integration, 2026-09-15 snapshot]]
