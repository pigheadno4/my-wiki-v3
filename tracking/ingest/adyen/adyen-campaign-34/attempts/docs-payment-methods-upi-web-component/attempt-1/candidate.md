---
title: "Adyen UPI Web Component integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/web-component"
raw_files:
  - "adyen/docs/payment-methods/upi/web-component/2026-09-15.md"
tags: [adyen, upi, web, component, intent, qr]
---

## Overview

This [[adyen]] guide adds **UPI** to existing Web Components integrations, with separate **Sessions** and **Advanced** sections. The pinned page supplies method setup, component import/init, an Advanced **Intent app ID** request field and TEST simulator guidance. It does not give a UPI Collect migration date or a LIVE onboarding procedure; those must come from separate evidence. Selecting UPI, showing a QR code or returning from a simulator is not proof of final authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The guide requires existing Web Components Sessions, **Checkout API v68 or later**, and UPI added in Customer Area. It says no extra UPI parameters for the base `/sessions` request or UPI configuration; import `UPI` from `@adyen/adyen-web` and initialize the Component. “No extra” is method-specific, not a waiver of the base session. The Sessions section does not separately state an additional action requirement. See raw lines 23–75.
- **Advanced:** The guide requires existing Web Components Advanced, handling an additional `action.type: await` action and Customer Area UPI setup. It imports and initializes `UPI`, says no extra UPI configuration, and requires `paymentMethod.appId` **when** `paymentMethod.type` is `upi_intent`; its table lists TPAP app IDs. The example uses `gpay`, INR/IN and TEST Checkout v72. That example version is not stated as a general Advanced minimum, and the Intent field must not be generalized to QR or Collect. See raw lines 99–175.
- **Snippet limits:** Both initialization snippets say `newUPI(checkout, ...)` without a space or declaration for `newUPI`, while prose says to use the `UPI` class; their comment also refers to a UPI configuration object despite prose saying no extra parameters. Treat these as source-example discrepancies, not copy-ready code or proof that configuration is required. See raw lines 55–75 and 121–143.
- **TEST outcomes:** The page says UPI Intent redirects to an Adyen-hosted Payment Simulator page and Web UPI QR uses a scanned QR to reach it; testers choose a simulated outcome and check handling. It asks them to check both webhook receipt and Customer Area transaction listing. Yet the webhook substep names `eventCode: AUTHORISED` for the “outcome that you selected,” which is not a reliable assertion for non-authorized simulated outcomes; preserve the inconsistency and verify each scenario's actual webhook. The page recommends testing modifications after outcomes. It does not provide a LIVE setup step despite the “Test and go live” heading. See raw lines 77–97 and 177–197.
- **Scope:** This page's substantive payment-option and TEST instructions cover Intent and Web QR. It does not set out a Collect cutoff, dated migration rule, UPI app-switch mechanics outside simulator testing, recurring mandate flow or final financial lifecycle. See raw lines 77–97 and 145–197.

## Detail locators

- Sessions prerequisites, request, import and initialization: raw lines 23–75.
- Advanced await action, conditional Intent app ID and example: raw lines 99–175.
- Duplicated TEST simulator/verification steps: raw lines 77–97 and 177–197.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-upi]]
- [[source-adyen-docs-payment-methods-upi-api-only]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/web-component/2026-09-15|Adyen UPI Web Component guide]]
