---
title: "Bancontact card Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/web-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/web-component/2026-09-15.md"
tags: [adyen, bancontact, card, web-components, 3d-secure, tokenization]
---

## Overview

This 2026-09-15 capture of Adyen's Bancontact **card** Web Component guide adds the method to an existing Sessions or Advanced Web Components integration. The page's `last_modified` metadata is 2021-10-27. Its Component collects card data and redirects the shopper for 3D Secure authentication; it is distinct from Bancontact Mobile's app-switch/QR route. This document alone does not establish current SDK support, merchant eligibility or a completed payment (raw lines 5–45).

## Key takeaways

- Bancontact card behaves like a card payment with **no CVC** (a CVC field may still appear for co-badged cards), **mandatory 3D Secure authentication**, and **no separate captures**. The page says the Component securely collects card information and redirects for authentication; it does not give a standalone authorization/capture-result workflow (raw lines 19–27).
- The prerequisites are an existing **Sessions or Advanced** Web Components flow and adding Bancontact card in Customer Area. The API-reference section says no Bancontact-specific additional fields are needed; it points to `/sessions` as the default for Components v5.0.0+ and `/payments` for an additional use case (raw lines 29–60). These are flow-specific routes, not proof the method is enabled for a merchant.
- For Web Components v6, the guide imports `Bancontact` and mounts `new Bancontact(checkout)`; v5.x.x or earlier uses `checkout.create('bcmc')`. Configuration can optionally show/require holder name, display a save-details checkbox and customize brands; the example enables holder name and storage, but those are **optional configuration**, not baseline required card fields. Bancontact can also be included in a Cards Component `brands` array as `bcmc` (raw lines 47–53, 72–168).
- Recurring is a separate **Bancontact Wallet Initiated Program (WIP)** path. Explicit shopper permission for future charges is strongly recommended; WIP requires signup, eligibility and Support enablement, with transaction limits. The page says the first consent transaction uses SCA, later transactions do not, and no liability shift occurs because the issuer remains liable. Token creation uses `storePaymentMethod: true` plus a shopper reference of at least three characters in `/sessions` or `/payments`; only after settlement does the `recurring.token.created` webhook provide `storedPaymentMethodId`. Subsequent `/payments` use that token and shopper reference with `ContAuth` and `Subscription` or `UnscheduledCardOnFile`. Test recurring configuration also needs Support (raw lines 170–225). The v72/TEST recurring request is an example, not evidence of WIP access or successful execution (raw lines 227–250).
- The testing section lists co-badged test cards and a `holderName: DECLINED` refusal fixture. It warns that the Visa Debit example may route to Bancontact **or Visa depending on payment-method setup**. It directs readers to test Customer Area for payment status and separately to add Bancontact card in live Customer Area; these instructions and fixtures do not establish a live payment or current account setup (raw lines 566–599).

## Detail locators

- Bancontact card distinctions, Component function and Sessions/Advanced prerequisites: raw lines 15–45.
- v6 import, v6/v5 mounting, optional configuration and combined Cards Component: raw lines 47–168.
- WIP eligibility, consent/SCA, settlement-triggered token and later recurring fields: raw lines 170–250.
- Language-specific recurring TEST request examples: raw lines 252–564.
- Test credentials, conditional co-badged routing, decline fixture and separate live setup: raw lines 566–599.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bancontact|Bancontact card/mobile overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/web-component/2026-09-15|Bancontact card Web Component, fetched 2026-09-15]]
