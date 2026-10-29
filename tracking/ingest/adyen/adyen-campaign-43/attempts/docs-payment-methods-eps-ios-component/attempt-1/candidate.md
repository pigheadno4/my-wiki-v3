---
title: "EPS iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/ios-component"
raw_files:
  - "adyen/docs/payment-methods/eps/ios-component/2026-09-15.md"
tags: [adyen, eps, ios, components, redirect, sepa-direct-debit, tokenization]
---

## Overview

This 2026-09-15-captured EPS iOS Component guide adds EPS-specific steps to an **existing** iOS Components integration. It has separate Sessions and Advanced sections; both use `EPSComponent` to present an issuer-list payment method and require the host integration to handle an `action.type: redirect` return. It does not itself document a full redirect-result or final payment-status workflow, and its setup text is not proof of merchant enablement or completed payment (raw lines 15–36, 50–73, 122–168).

## Key takeaways

- **Sessions:** Requires an existing iOS Components Sessions flow, **Checkout API v68 or later**, redirect handling and EPS added in Customer Area. The page says no EPS-specific `/sessions` parameters or Component configuration are needed. Its sample resolves `IssuerListPaymentMethod`, creates `EPSComponent`, sets the **session as delegate**, then presents the view controller (raw lines 25–73). The no-extra-configuration prose coexists with a sample argument `configuration: epsConfiguration`; verify how that object is supplied before copying the snippet, rather than treating it as a newly required EPS setting (raw lines 46–69).
- **Advanced:** Requires an existing iOS Components Advanced flow, redirect handling and EPS added in Customer Area. It says no additional EPS configuration or `/payments` parameters are needed. Its sample again uses `IssuerListPaymentMethod` and `EPSComponent`, but sets **self as delegate**. The Advanced requirement table labels the integration as Components while its integration-type link points to a Drop-in URL; follow the actual Advanced Components integration guide before implementing that linked step (raw lines 122–168). Unlike Sessions, the Advanced section does not state a Checkout API version minimum (raw lines 126–132).
- Both flow sections describe EPS recurring transactions **through SEPA Direct Debit**, not ordinary repeat EPS redirects. Explicit shopper permission, payment schedule and amount disclosure are strongly recommended to reduce chargeback risk. Token creation is specified on a `/payments` request with `storePaymentMethod: true` and a shopper reference of at least three characters; **after settlement**, a `recurring.token.created` webhook provides `storedPaymentMethodId`, and the server must receive token lifecycle events. Later `/payments` use that token and shopper reference with `ContAuth` plus `Subscription` or `UnscheduledCardOnFile` (raw lines 75–114, 170–209). The Sessions section also names `/payments` for token creation, so do not silently rewrite it to `/sessions` (raw lines 84–93).
- Test payment status is checked in test Customer Area. Before accepting **live** EPS, the page says to submit an EPS request in live Customer Area. These are separate setup/status steps, not evidence of a live approval, authorization, settlement or recurring charge (raw lines 116–120, 211–215).

## Detail locators

- Sessions requirements, redirect action and API v68+: raw lines 25–36.
- Sessions no-extra-fields/configuration and `EPSComponent` delegate sample: raw lines 38–73.
- Advanced requirements, link mismatch, no-extra-fields/configuration and self-delegate sample: raw lines 122–168.
- SEPA Direct Debit recurring-token path repeated under Sessions and Advanced: raw lines 75–114, 170–209.
- Test status lookup and separate live EPS request: raw lines 116–120, 211–215.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-eps|EPS overview]]
- [[source-adyen-docs-payment-methods-sepa-direct-debit|SEPA Direct Debit overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/ios-component/2026-09-15|EPS iOS Component, fetched 2026-09-15]]
