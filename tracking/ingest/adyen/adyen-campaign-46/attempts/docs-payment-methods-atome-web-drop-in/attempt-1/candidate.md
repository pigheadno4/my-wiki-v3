---
title: "Adyen Atome Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/atome/web-drop-in/2026-09-15.md"
tags: [adyen, atome, web, drop-in, malaysia, singapore, redirect]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds Atome to an existing **Web Drop-in** integration through separate Sessions and Advanced flow instructions. It covers method-specific request fields, redirect handling, partial refunds, and test/live setup; base integration remains in the linked main guides. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-atome|Atome overview]] for method-level restrictions. This snapshot does not prove present merchant eligibility or completed payment.

## Key takeaways

- **Prerequisites and regions:** Sessions requires existing Web Drop-in Sessions, Checkout API v68+, redirect handling, and Atome enabled in Customer Area. Advanced requires existing Web Drop-in Advanced, redirect handling, and Customer Area enablement. Both flow tables require shopper full name, email, phone, billing address, line items and `countryCode`; delivery address is optional if it equals billing. Supported pairs stated here are **MY/MYR** and **SG/SGD**. The Advanced request also requires `paymentMethod.type: atome`. These are method request rules in the captured guide, not proof of a live account configuration.
- **Redirect and examples:** The Sessions TEST `/sessions` sample uses v71, SG/SGD, and `adyencheckout://your.package.name` for `returnUrl`, an app-style scheme in a Web guide. The Advanced TEST `/payments` sample uses v72, SG/SGD, and an HTTPS return URL. Configure the actual Web return path rather than copying the Sessions app-scheme placeholder. The Advanced response contains `resultCode: RedirectShopper` with a redirect action. Although the raw heading calls it an “example response for a successful payment,” this response shows a redirect step, not completed authorization or capture. Both curl examples lack a shell continuation before `-d`, so are not copy-ready.
- **Refunds and test setup:** Both flow sections say a partial refund uses the `amount` in `/payments/{paymentPspReference}/refunds`; their cancellation headings give no additional method-specific cancellation rule. Test payments need an Atome sandbox shopper account obtained through the Adyen contact, with a separate test account for each country/region tested. The page links regional QR test apps and says to check payment status in test Customer Area. Live acceptance requires contacting Adyen Support to add Atome in live Customer Area.
- **Method-level boundary:** The separate captured Atome overview states portable electronics such as phones and laptops are excluded, requiring checkout logic to disable Atome for that category. This integration add-on does not repeat the restriction; use the overview when assessing product eligibility. The overview also says capture is automatic after authorization; this page does not supply a separate capture procedure.

## Detail locators

- Page purpose, Sessions requirements and field table: pinned raw lines 15–52. Sessions v71 test example and SDK variants: lines 54–730. Optional tree-shaken import: lines 732–742.
- Sessions partial-refund note and test/live route: lines 744–774. Advanced prerequisites, optional import and fields: lines 776–815. Advanced v72 sample and SDK variants: lines 817–1530.
- Redirect response with misleading heading: lines 1532–1544. Advanced refund, test account and live enablement: lines 1546–1576. Compare method-level portable-electronics and capture notes in [[source-adyen-docs-payment-methods-atome]].

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-atome]] — method overview and product restrictions

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/web-drop-in/2026-09-15|Atome Web Drop-in guide, fetched 2026-09-15]]
