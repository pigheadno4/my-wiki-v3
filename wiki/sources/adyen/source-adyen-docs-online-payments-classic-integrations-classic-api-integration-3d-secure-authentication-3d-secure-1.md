---
title: "Classic API 3D Secure 1 and 2 redirect authentication"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/2026-09-15.md"
tags: [adyen, classic-api, 3d-secure, 3ds1, 3ds2, redirect-authentication]
---

## Overview

Despite its `3d-secure-1` URL, this 2023-08-25-modified, 2026-09-15-captured page is titled **3D Secure 1 and 2 redirect authentication** for the legacy Classic Payment API `/authorise` integration. Adyen says it no longer develops or accepts **new Classic API integrations** and recommends the newer Checkout API redirect guide, which also requires migrating to Checkout API. This is historical flow evidence, not current 3DS1 scheme support, merchant enablement, legal compliance, authentication success or payment authorization. See [[adyen]] and [[adyen-3d-secure]] (raw lines 5–25).

## Key takeaways

- The page frames 3D Secure as issuer-side card-not-present authentication and mentions possible personal-card liability shift and conversion/redirect risks. Those are dated general statements; liability and regulatory treatment depend on transaction, scheme, region and flow and cannot be inferred for a specific payment. Its PSD2 section lists default Adyen handling, Dynamic 3DS rules and per-transaction preference; the latter overrides Adyen's default out-of-scope and exemption selection logic (raw lines 27–49).
- Its dated setup says to obtain a test account/API key and check 3DS1 enablement. It lists default test enablement and live default for Bancontact/MisterCash, Maestro, Mastercard and Visa; American Express, Diners/Discover and JCB require Support configuration in that snapshot. These lists are **not evidence of present-day scheme acceptance or live merchant configuration** (raw lines 51–76).
- The illustrated Classic flow starts with POST `/authorise`, payment reference/amount/card and browser/IP data. Raw card data is conditioned on full PCI compliance; otherwise the page directs use of Classic Client-Side Encryption. An `Authorised` result can be normal/frictionless or non-enrolled, while `RedirectShopper` returns `issuerUrl`, `paRequest` and `md`; `RedirectShopper` is a redirect instruction, not completed authentication (raw lines 78–190).
- For `RedirectShopper`, the page submits `PaReq`, uppercase `MD` and `TermUrl` by form POST to the issuer. The issuer returns `MD` and `PaRes` to the merchant return URL; the merchant then sends `md` and `paResponse` to Classic `/authorise3d`. This is the page's legacy redirect handoff, not a general rule for modern Checkout API 3DS2 (raw lines 193–250).
- The page instructs the merchant to present the result code from `/authorise` or `/authorise3d` and says the payment outcome also arrives asynchronously by webhook. It lists Authorised, Cancelled, Error and Refused; **manual capture remains required** for an authorised payment using manual capture. Its test-card sections include both redirect and native 3DS2 scenarios, which are test fixtures rather than proof of live availability or transaction outcome (raw lines 339–416).

## Detail locators

- Classic deprecation, migration and risk/PSD2 framing: raw lines 19–49.
- Historical test/live scheme setup: raw lines 51–76.
- Classic `/authorise` parameters, PCI caveat and response branch: raw lines 78–190.
- Issuer form/return and Classic `/authorise3d` completion request: raw lines 193–337.
- Result/webhook/capture boundary and test fixtures: raw lines 339–416.

## Related

- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication]]
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/3d-secure-1/2026-09-15|Pinned Classic 3DS redirect guide]]
