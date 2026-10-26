---
title: "Adyen TWINT Flutter Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/twint/flutter-drop-in/2026-09-15.md"
tags: [adyen, twint, flutter, drop-in, sessions, advanced, redirect, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing Flutter Drop-in integration, with separate Sessions and Advanced server-side sections. Both cover redirect prerequisites and a recurring-token route. It does not describe the concrete redirect response, return/details step, capture limits or final payment outcome on this page; use the main flow and relevant method authority for those details. The snapshot does not prove current merchant enablement, created token, capture or successful payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Sessions:** requires existing Flutter Drop-in Sessions, **Checkout API v68 or later**, `action.type: redirect` handling and contacting Adyen Support to add TWINT in Customer Area. It says no TWINT-specific `/sessions` parameters or Drop-in configuration. The integration-type row's link points to an **Advanced** Flutter Drop-in URL, despite the Sessions label and Sessions redirect/session links; verify the correct main guide before implementation. (raw lines 25–48)
- **Advanced:** separately requires existing Flutter Drop-in Advanced, redirect handling and adding TWINT in Customer Area. It says no TWINT-specific Drop-in configuration or normal `/payments` parameters. This section does not repeat the Sessions v68 minimum or Support-contact setup wording; preserve the section-specific prerequisites. (raw lines 97–119)
- **Recurring in both sections:** token creation adds `storePaymentMethod: true` and a shopper-unique `shopperReference` of at least three characters to `/payments`. After details are stored, a `recurring.token.created` webhook carries `storedPaymentMethodId`, initial-payment `pspReference` as `eventId`, and shopper reference; the merchant server must receive recurring-token lifecycle events. Future `/payments` requests use the stored ID, matching shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. A token request or the described webhook does not prove a particular token was created or a later payment succeeded. (raw lines 50–89, 121–160)
- **Environment:** both sections direct TEST status checks to Customer Area and require a separate request in the **live** Customer Area before accepting live TWINT. The page provides no test simulation or live-activation evidence. (raw lines 91–95, 162–166)

## Detail locators

- Sessions prerequisites, misrouted integration-type link and no-extra-fields/configuration: pinned raw lines 25–48.
- Advanced prerequisites and no-extra-fields/configuration: pinned raw lines 97–119.
- Repeated recurring token creation/webhook and reuse fields: pinned raw lines 50–89 and 121–160.
- TEST status and LIVE request: pinned raw lines 91–95 and 162–166.

## Related

- [[adyen-online-payments]] — main provider redirect/outcome context
- [[adyen-tokenization]] — provider token lifecycle
- [[source-adyen-docs-payment-methods-twint]] — TWINT overview and shopper handoff

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/flutter-drop-in/2026-09-15|TWINT Flutter Drop-in guide, 2026-09-15]]
