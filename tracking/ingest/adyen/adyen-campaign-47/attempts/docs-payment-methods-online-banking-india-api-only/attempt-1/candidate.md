---
title: "Adyen Online Banking India API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-india/api-only"
raw_files:
  - "adyen/docs/payment-methods/online-banking-india/api-only/2026-09-15.md"
tags: [adyen, online-banking-india, api-only, india, redirect]
---

## Overview

This 2026-09-15-captured [[adyen]] guide adds Online Banking India to an **existing API-only integration** for a custom payment form on Web, iOS, or Android. It covers available-method discovery, an issuer selection, required payment additions, and a redirect action; it delegates the base payment and redirect flow to the main integration guide. The captured page does not establish current merchant eligibility, live enablement, payment authorization, or settlement. See [[adyen-online-payments]] and the related method overview.

## Key takeaways

- **Prerequisites:** The existing API-only integration must handle redirect actions, and Online Banking India must be added in Customer Area. The related method overview separately says processing requires India regulatory compliance plus a local entity and local integration in India; contact the account manager or Support for details. Live acceptance requires submitting a request for Online Banking India in the live Customer Area. [Pinned raw: lines 23–29, 486–496; related overview raw: raw/adyen/docs/payment-methods/online-banking-india/2026-09-15.md, lines 25–27]
- **Discover issuers:** The /paymentMethods request should specify **countryCode IN**, **amount.currency INR**, and a channel of **Web**, **iOS**, or **Android**. Show the available banks from the returned Online Banking India method, pass the shopper's selected **issuer** value to the server, and build the form dynamically because the list can change. Showing the top ten issuers with a way to see more is a recommendation, not a requirement. [Pinned raw: lines 31–53]
- **Make payment:** The /payments additions table marks **paymentMethod.issuer** and **browserInfo** required. The example uses **paymentMethod.type=onlinebanking_IN**, issuer **CBI**, INR 1000, an HTTPS returnUrl and test Checkout endpoint; those values are examples, not a fixed issuer or a complete platform-specific return recipe. [Pinned raw: lines 55–95]
- **Continue redirect:** Handle the returned **action.type=redirect** using the main API-only integration flow. This page does not provide a final result response or prove success from initiating the redirect. Its test instruction points to the MyStore demo with India selected; its live instruction requires a live Customer Area request. [Pinned raw: lines 486–500]

> [!WARNING] Method type capitalization differs inside the page
> The bank-list instruction identifies the /paymentMethods response object as **onlineBanking_IN** (capital B, raw line 47), while every /payments request example uses **onlinebanking_IN** (lowercase b, starting at raw line 80). The captured page does not resolve the difference. Do not silently treat the two spellings as interchangeable or infer a fixed request type from the discovery prose; verify the actual response and API contract before implementation.

## Detail locators

- Add-on scope, requirements, and Customer Area setup: pinned raw lines 15–29.
- /paymentMethods geography, currency, channel, and dynamic issuer-list guidance: pinned raw lines 31–53.
- /payments required additions and sample requests across API libraries: pinned raw lines 55–484.
- Redirect action, test demo, and live request: pinned raw lines 486–500.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-india]] — method overview with India local-entity/integration prerequisites and capability matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-india/api-only/2026-09-15|Online Banking India API-only guide, captured 2026-09-15]]
