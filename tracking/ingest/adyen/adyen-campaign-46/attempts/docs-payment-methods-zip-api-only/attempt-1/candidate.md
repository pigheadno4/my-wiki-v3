---
title: "Adyen Zip API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/api-only"
raw_files:
  - "adyen/docs/payment-methods/zip/api-only/2026-09-15.md"
tags: [adyen, zip, api-only, redirect, recurring-payments]
---

## Overview

This 2026-09-15 capture of Adyen's Zip API-only guide describes a merchant-built payment form, API payment initiation, redirect handling and recurring token use. Its metadata says last modified 2019-09-06. It requires an existing API-only integration and adding Zip in the test Customer Area. This historical guide does not establish current account enablement, eligibility, live operation or payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The guide encourages shopper name, email, date of birth when specified, phone, billing address and delivery preference for Zip risk checks. It calls delivery address required only when the shopper chooses delivery rather than Click and Collect. For `/paymentMethods` discovery, it says to specify countryCode AU or US, amount currency AUD or USD in minor units, and channel Web, iOS or Android; the returned type is `zip`. It does not expressly pair each listed country with a currency (pinned raw lines 28–51).
- The page labels `/sessions` the default for API-only v5.0.0 or later, and gives a separate `/payments` tab for an additional use case. The `/payments` flow sends `paymentMethod.type=zip`; `paymentMethod.clickAndCollect=true` is for pickup. Shopper/address/line-item fields and sample requests are at raw lines 63–1404; the source's endpoint framing needs the warning below (lines 55–65, 712–725).
- In the `/payments` response, `action.url` drives the Zip redirect. On return, POST `/payments/details` with URL-decoded `redirectResult`; use its `resultCode` for the shopper and `pspReference` as transaction identifier. The guide recommends SFSafariViewController or Chrome Custom Tabs instead of WebView for an in-app HTTP GET redirect, and strongly recommends the default browser for mobile redirects (lines 1406–1465).
- `Pending` or `Received` is not final: wait for an AUTHORISATION webhook. If the shopper never returns, use webhook outcomes, including AUTHORISATION success true/false and OFFER_CLOSED true for timeout. Other listed result codes are Authorised, Cancelled, Error and Refused (lines 1463–1483).
- For recurring Zip payments, the guide says to submit `storePaymentMethod=true` and a unique `shopperReference`; after settlement, `recurring.token.created` supplies `storedPaymentMethodId`. Later `/payments` requests use that token, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. A token is not promised before settlement (lines 1485–1518). Testing uses Zip test credentials and Adyen's test environment; accepting live Zip requires a request in the live Customer Area (lines 1718–1724).

> [!warning] Endpoint framing and examples
> The lead says to make a server-side `/payments` request, yet the next tab calls `/sessions` the API-only v5.0.0+ default (raw lines 55–65, 712–714). The `/sessions` examples do not show `paymentMethod.type=zip`, while the `/payments` curl block contains literal `{hint:...}` markup inside the JSON object (lines 728–750). Treat these as route-specific documentation/examples, not a single ready-to-run request; follow the selected endpoint's requirements.

## Detail locators

- API-only/test setup, risk-check shopper details, Click and Collect, method discovery: pinned raw lines 15–53.
- `/sessions` tab and language examples: lines 55–711; `/payments` tab, Click and Collect field, request examples: lines 712–1404.
- Redirect, `/payments/details`, outcomes and webhooks: lines 1406–1483.
- Recurring token creation/use and language examples: lines 1485–1716; test and live setup: lines 1718–1724.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-zip]] — Zip method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/api-only/2026-09-15|Zip API-only guide, captured 2026-09-15]]
