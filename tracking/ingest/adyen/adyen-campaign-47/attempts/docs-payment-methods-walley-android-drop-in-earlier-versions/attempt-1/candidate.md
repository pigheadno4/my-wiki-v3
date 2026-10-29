---
title: "Adyen Walley Android Drop-in earlier versions"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/walley/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, walley, android, drop-in, redirect, earlier-versions, online-payments]
---

## Overview

This captured [[adyen]] page is titled **Walley Android Drop-in v4.x.x integration**. It describes method discovery, a server-side `/payments` request from Drop-in data, redirect/return handling, details-result presentation, asynchronous webhook outcomes, and test data. Its requirements also say Walley works with **all** Drop-in versions, while the title says v4.x.x; read it as this captured earlier-version guide, not a universal exact-version recipe. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and methods:** The page assumes Android Drop-in and contacting Adyen Support to add Walley in test Customer Area. For `/paymentMethods`, its table pairs DK/DKK, FI/EUR, NO/NOK and SE/SEK. It distinguishes `walley` B2C from `walley_b2b` B2B; Denmark or DKK is B2C-only. These discovery values and a test setup step do not prove a merchant's current availability or live setup (raw lines 15–43).
- **Client/server redirect sequence:** Drop-in returns `paymentComponentData.paymentMethod` to the app, which passes it to the server for `/payments`. The page says to derive the return URL from `RedirectComponent.getReturnUrl(context)`, with a 1024-character maximum, then pass the `/payments` redirect `action` back to the client. After app return, the server posts Drop-in `actionComponentData.details` to `/payments/details`; its `resultCode` is for shopper presentation. `RedirectShopper` is an intermediate action, not final success (raw lines 45–58, 340–397).
- **Result finality:** The table covers `Authorised`, `Cancelled`, `Error`, `Pending`/`Received`, and `Refused`. `Authorised` may still require capture if manual capture is used. `Pending`/`Received` means final outcome is unknown and requires an `AUTHORISATION` webhook; webhook outcomes also matter if the shopper never returns. The listed webhook cases have `AUTHORISATION` success true or false (raw lines 395–414). An example `Authorised` response does not show a real completed transaction.
- **Test data and example conflicts:** The page points to Walley test scenarios, says to send `CivRegNo` as `socialSecurityNumber`, and shows company name/registration data for B2B testing (raw lines 416–429). Its `/payments` examples use `countryCode: NO` with `EUR`, contrary to the page's own NO/NOK discovery table; do not treat that pair as an endorsed Norway configuration. The curl item values shown do not visibly reconcile to the 1000 request amount without other amounts, and examples vary in line-item count; inspect actual order totals. The title's v4.x.x label, all-version statement, and Sessions-flow base links coexist with this page's server `/payments`/details route (raw lines 15–27, 36–41, 60–99, 102–146, 431–436).

## Detail locators

- Identity, requirements and B2C/B2B country/currency discovery: pinned raw lines 15–43.
- Client/server payment request and examples: pinned raw lines 45–338.
- Redirect action, return/details and result/webhook paths: pinned raw lines 340–414.
- Test instructions and related base routes: pinned raw lines 416–436.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-walley]] — captured Walley overview; use this page for Android earlier-version workflow.

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/android-drop-in/earlier-versions/2026-09-15|Walley Android Drop-in earlier versions, captured 2026-09-15]]
