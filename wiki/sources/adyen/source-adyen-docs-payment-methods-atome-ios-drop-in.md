---
title: "Adyen Atome iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/atome/ios-drop-in/2026-09-15.md"
tags: [adyen, atome, ios, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide describes Atome-specific additions to an existing iOS Drop-in integration, separately for Sessions and Advanced server-side flows. It links to the main integration guides for shared steps. It does not establish current merchant eligibility, final payment success or live enablement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing iOS Sessions Drop-in integration using Checkout API v68 or later and Atome added in Customer Area. The `/sessions` table marks shopper name, email, phone, billing address, line items and `countryCode` required. Delivery address is optional when the same as billing. The supported country/currency combinations stated are MY/MYR and SG/SGD (pinned raw lines 25–50).
- **Advanced flow:** Requires an existing iOS Advanced Drop-in integration, redirect handling for `action.type=redirect`, and Atome added in Customer Area. The `/payments` table marks `paymentMethod.type=atome` and the same shopper, billing, line-item and country fields required, with the same conditional delivery-address optionality and MY/MYR or SG/SGD pairing. The v68+ API version is specified in the Sessions requirements, not repeated in this Advanced table (lines 768–801).
- Both flow sections state that no Atome-specific Drop-in configuration parameters are needed (lines 730–734, 780–784). The Advanced example returns `resultCode=RedirectShopper` and a GET redirect action; follow the linked main iOS flow for return and result handling (lines 1518–1530).
- Partial refunds specify an `amount` in `/payments/{paymentPspReference}/refunds`. Testing requires an Atome sandbox shopper account requested through an Adyen contact, and a different account for each country/region if testing multiple. The page lists QR-code test apps for MY and SG. Live Atome acceptance requires contacting Support to add Atome in the live Customer Area (lines 736–766, 1532–1562).

> [!warning] Redirect result label
> The Advanced section calls its sample a “response for a successful payment,” yet the response is `RedirectShopper` with a redirect action (raw lines 1518–1530). This is an intermediate shopper action, not a final authorization or settlement result.

> [!warning] Example request details
> The Sessions curl example repeats `countryCode=SG` and puts `-X POST` before `-d` without a shell continuation (raw lines 52–76). Its returnUrl example uses `adyencheckout://your.package.name`; the Advanced example uses an HTTPS checkout URL (lines 52–71, 805–827). Treat these as placeholders and consult the linked iOS flow for the app's actual return URL and redirect setup.

## Detail locators

- Sessions prerequisites and request fields: pinned raw lines 15–50; language examples: lines 52–728.
- Sessions configuration, partial refund and test/live: lines 730–766.
- Advanced prerequisites, configuration and `/payments` fields: lines 768–801; examples: lines 803–1516.
- Redirect response, partial refund and test/live: lines 1518–1562.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-atome]] — Atome method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/ios-drop-in/2026-09-15|Atome iOS Drop-in guide, captured 2026-09-15]]
