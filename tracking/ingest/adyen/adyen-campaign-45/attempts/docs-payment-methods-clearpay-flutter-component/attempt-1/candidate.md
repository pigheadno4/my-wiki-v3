---
title: "Adyen Clearpay Flutter Components integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/clearpay/flutter-component/2026-09-15.md"
tags: [adyen, clearpay, flutter, components, redirect, capture, refund]
---

## Overview

This 2026-09-15 Adyen Docs page describes Clearpay-specific additions to an **existing Flutter Components** integration with Sessions or Advanced server flow. Both paths require Clearpay in Customer Area and redirect handling. The GB/GBP request examples and sandbox instructions do not establish live merchant eligibility, a completed redirect, authorization or capture. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The Sessions requirement specifies Checkout API v68 or later, while its sample uses a v71 test URL; the Advanced sample uses v72. Both paths refer back to the appropriate base integration and say no additional Clearpay configuration parameters are needed. The page does not give Flutter Component initialization code of its own (pinned raw lines 25–40, 53–118, 207–229).
- Both request tables mark shopper name, email, reference (minimum three characters), country code, billing and delivery addresses, and `lineItems` required, with telephone number optional. The Advanced request example includes `paymentMethod.type: clearpay` and the response example has a redirect action and `RedirectShopper`; that is a handoff step, not a final payment result (lines 42–51, 231–320).
- Depending on merchant-account configuration, capture is automatic after authorization or manual. Capturing after shipment requires a delay or manual capture; partial capture requires manual capture. Clearpay says capture within 13 days after authorization. It charges the first installment during authorization, then cancels and refunds that installment if the payment is not captured in time. In test, manual capture has a one-day limit (lines 120–130 and 322–332).
- Manual `/payments/{paymentPspReference}/captures` uses full or partial `amount.value`, with optional `lineItems`. An initial partial capture cancels the unclaimed remainder unless multiple partial captures are enabled through Support; each enabled partial capture creates a new invoice. Cancel an uncaptured payment; refund a captured one via `/payments/{paymentPspReference}/refunds`, with optional line items (lines 132–152 and 334–354).
- The guide includes negative-line discount examples and a Clearpay sandbox shopper/test-card route. A live Customer Area request is stated before live acceptance; test instructions are not proof of live operation (lines 154–205 and 356–407).

> [!warning] Example and link inconsistencies
> Both Flutter **Components** requirement links point to an **Advanced Drop-in** URL, including the Sessions requirement (raw lines 31 and 215); their redirect links instead name the respective Sessions/Advanced Components paths (lines 33 and 216). The discount prose says 1 GBP off Item #2, but the sample uses quantity 2 at `-100` minor units and drops the total from 1000 to 800, a 2 GBP reduction; it also has an ellipsis and no comma between item objects, so it is not copy-ready JSON (lines 156–188 and 358–390). Both curl examples omit a line continuation after `-X POST` before `-d` (lines 60–61 and 249–250); verify shell syntax before use.

## Detail locators

- Sessions requirements, fields, example and configuration statement: pinned raw lines 25–118.
- Sessions capture/refund, discount and test/live route: lines 120–205.
- Advanced requirements, request/redirect, lifecycle and test/live route: lines 207–407.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-clearpay]] — Clearpay GB/GBP method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/flutter-component/2026-09-15|Clearpay Flutter Components guide, captured 2026-09-15]]
