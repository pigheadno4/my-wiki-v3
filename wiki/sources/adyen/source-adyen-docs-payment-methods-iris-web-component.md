---
title: "Adyen IRIS Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/iris/web-component"
raw_files:
  - "adyen/docs/payment-methods/iris/web-component/2026-09-15.md"
tags: [adyen, iris, web, components, redirect, qr-code]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds IRIS to an existing **Web Components** integration. It separates Sessions and Advanced flows and, in Advanced, issuer redirect from QR code payment. See [[adyen-online-payments]]. The TEST examples and simulator do not establish current merchant enablement, a live payment, or settlement.

## Key takeaways

- **Prerequisites and live setup:** Sessions requires an existing Web Components Sessions integration and Checkout API v68 or later; Advanced requires an existing Advanced integration that handles both `redirect` and `qrCode` actions. Both sections say to add IRIS in Customer Area. Before live use, the merchant must request IRIS from its Greek bank and Adyen, supplying its DIAS code, merchant account and stores for activation; the test/live section also says to enable IRIS on the live merchant account in Customer Area (raw lines 29–35, 90–96, 1088–1097). These steps do not prove approval for a particular merchant.
- **Sessions Component:** The method-specific Sessions section adds no `/sessions` parameters and no IRIS configuration parameters. It imports `Iris` from `@adyen/adyen-web`, constructs `new Iris(checkout, ...)` and mounts it to a page container. The existing base Sessions integration remains necessary (raw lines 39–75).
- **Advanced choice of action:** The `/payments` table requires `paymentMethod.type: iris`. For **issuer redirect**, it says `paymentMethod.issuer` and `returnUrl` are required; with an issuer ID, the response contains a redirect URL. Without an issuer ID, it says the response contains QR code data and `returnUrl` is not required for that flow (raw lines 128–136). The QR TEST request nevertheless includes `returnUrl`; its presence there is an example, not a QR requirement (lines 742–768). The 10 EUR examples do not define a complete country/currency eligibility matrix.
- **Redirect result:** The issuer-redirect example returns `RedirectShopper` and `action.type: redirect`; send the shopper to `action.url`. On return to the website, POST `/payments/details` with the URL-decoded `redirectResult`. The details response uses `resultCode` for shopper presentation and `pspReference` as transaction identifier. Its example `Authorised` is a TEST sample, not proof of capture or settlement (raw lines 460–488, 728–740). The mobile browser advice embedded in this Web guide is conditional on a mobile integration (lines 478–484).
- **QR result and time limit:** The issuer-omitted example returns `Pending`, `action.type: qrCode` and `qrCodeData`; render the QR from that data. The shopper has **10 minutes** after initiation to complete the transaction; showing a timer is recommended. After the shopper scans and completes payment, Adyen says it sends a webhook with the result, which the merchant presents. `Pending` and a QR scan do not themselves establish final success (raw lines 1060–1086).
- **Sample caveat and testing:** The redirect curl includes `paymentMethod.issuer`, but its Java, PHP, C#, Go and TypeScript examples omit that field under the same redirect heading; per the request table, omission selects QR data, so do not treat those snippets as verified redirect requests (raw lines 146–165, 183–199, 220–242, 263–286, 339–360, 443–457). Both curl `/payments` examples put `-X POST` on a line without a shell continuation before `-d`, so they are not copy-ready (lines 151–152, 755–756). The IRIS simulator lets a tester select Successful, Refused or Cancelled outcomes on an Adyen-hosted page; test payment status is checked in test Customer Area (lines 77–86, 1088–1097).

## Detail locators

- Identity, Sessions requirements and Component setup: pinned raw lines 15–75; Sessions simulator/live notes: lines 77–86.
- Advanced requirements, action handling, import and initialization: lines 88–124; conditional payment fields: lines 126–136.
- Issuer-redirect TEST request and SDK examples: lines 138–458; redirect response and `/payments/details` path: lines 460–740.
- QR TEST request, action, ten-minute completion and webhook: lines 742–1086; Advanced test/live notes: lines 1088–1097.

## Related

- [[adyen-online-payments]] — provider online-payments concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/iris/web-component/2026-09-15|IRIS Web Component guide, captured 2026-09-15]]
