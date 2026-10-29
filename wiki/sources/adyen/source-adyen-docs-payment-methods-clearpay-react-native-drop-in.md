---
title: "Clearpay React Native Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/clearpay/react-native-drop-in/2026-09-15.md"
tags: [adyen, clearpay, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen Docs page describes **Clearpay-specific additions** to an existing React Native Drop-in integration, separately for Sessions and Advanced server-side flows. The linked Clearpay overview identifies the UK brand and GB/GBP method matrix. This child uses GB/GBP TEST examples without proving account eligibility or a successful payment. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-clearpay]] and [[adyen]].

## Key takeaways

- Sessions calls for an existing React Native Drop-in **Sessions** flow, **Checkout API v68 or later**, redirect handling and Clearpay added in Customer Area (raw lines 25–36). Its `/sessions` table marks shopper name/email/reference (reference minimum three characters), country code, billing/delivery addresses and line items required; phone is optional (lines 40–53). The requirement row's linked “Sessions flow” base guide actually uses an **Advanced** URL at line 33, while the request and redirect links use Sessions URLs (lines 35, 42); use the matching flow rather than following that mislabeled route blindly.
- Sessions and Advanced each say no additional Clearpay-specific Drop-in configuration is needed (lines 116–120, 225–229). Their GB/GBP TEST curl examples put `-X POST` on one line and `-d` on the next without a continuation (lines 58–63 and 251–256), so the literal shell snippets are not verified copy-ready requests.
- Advanced requires an existing React Native Drop-in Advanced flow, redirect handling and Clearpay added in Customer Area (lines 213–223). Its `/payments` table marks the same shopper/country/address/item fields required, phone optional (lines 233–246); the example explicitly uses `paymentMethod.type: clearpay` (lines 248–310). The sample initial response is `RedirectShopper` with a redirect action (lines 312–326), not final authorisation or capture proof. The base integration guide owns returned-shopper and outcome handling.
- Capture can be automatic after authorisation or manual according to merchant-account configuration. Delayed capture needs delay setup or manual capture; partial capture needs manual capture. Clearpay requires capture within **13 days**, otherwise it cancels and refunds the first instalment charged during authorisation; test authorisations expire in **one day** (Sessions lines 124–132; Advanced lines 330–338). Partial manual capture cancels the unclaimed remainder unless the account is enabled for multiple partial captures, which requires Support setup and creates a new invoice per capture (lines 134–143 and 340–349).
- An uncaptured payment can be cancelled; a captured payment must be refunded to return funds. Full or partial refund requests specify `amount.value`, with `lineItems` optional (lines 145–156 and 351–360). For discounts, the text requires a negative amount, but says the example is **£1** off Item #2 while the example shows quantity **2** at **-100** minor units and lowers the total by 200; it also lacks a comma between the second item and discount object (lines 158–194 and 362–396). Treat the example as inconsistent, not copy-ready.
- Testing requires a Clearpay sandbox and test shopper account, with regional sandbox details and linked test-card references. Sandbox shows Adyen as merchant; live payments require a request in live Customer Area (lines 196–211 and 398–413). A sandbox payment-list result does not establish live enablement, successful capture, refund or settlement.

## Detail locators

- Scope, Sessions prerequisites and base-link mismatch: raw lines 15–36.
- Sessions request fields, GB/GBP TEST example, no-extra-configuration: lines 40–120.
- Sessions capture/refunds/discounts and sandbox/live: lines 122–211.
- Advanced requirements, no-extra-configuration, request table/example and redirect response: lines 213–326.
- Advanced capture/refunds/discounts and sandbox/live: lines 328–413.
- Discount prose/example mismatch and malformed JSON: lines 162–194 and 364–396.
- Linked overview UK/GB/GBP branding: `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-clearpay]] — UK product and GB/GBP matrix.

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/react-native-drop-in/2026-09-15|2026-09-15 Clearpay React Native Drop-in Sessions and Advanced guide]]
