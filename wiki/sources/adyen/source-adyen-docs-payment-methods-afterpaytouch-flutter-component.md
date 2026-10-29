---
title: "Afterpay Flutter Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/flutter-component/2026-09-15.md"
tags: [adyen, afterpay, flutter, components, redirect, capture]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Afterpay to an existing Flutter Components integration. It separates Sessions and Advanced server flows and gives method-specific request data, redirect prerequisites, capture behavior and test/live setup. See [[adyen-online-payments]]. Its AU/AUD TEST examples and sandbox instructions do not prove present method availability or a successful payment.

## Key takeaways

- For Sessions, the page requires an existing Flutter Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Afterpay added in Customer Area. For Advanced, it requires an existing Flutter Components Advanced integration, the same redirect handling and Customer Area setup. The Requirements tables label Components but link their base-integration text to a Flutter **Drop-in** Advanced-flow URL; use the explicit Components redirect links and verify the appropriate base guide instead of treating that mismatched link as a Components implementation.
- The `/sessions` and `/payments` tables mark shopper name/email/reference, country code, billing/delivery address and `lineItems` required; telephone number is optional. Advanced also marks `paymentMethod` (`afterpaytouch`) required. The Sessions TEST curl sample uses Checkout API v69 and AU/AUD; Advanced uses v68 and AU/AUD. Language sample library versions differ. These examples do not establish other countries or live setup.
- No Afterpay-specific Flutter Component configuration parameters are required by either flow section. Advanced says its payment response includes `action.type: redirect`, with an example `RedirectShopper` response. Redirect handling is a prerequisite; this guide does not demonstrate a completed shopper return or final authorization.
- Capture may be automatic after authorisation or manual according to merchant configuration. Capturing after dispatch requires capture delay or manual capture; partial capture requires manual capture. Capture within 13 days of authorisation; otherwise Afterpay cancels and refunds the first installment charged at authorization. TEST authorization expires in one day. With one partial capture, unclaimed amount is automatically cancelled unless multiple partial capture is enabled on the account; that setting requires Support and each capture creates a new invoice.
- Testing requires an Afterpay sandbox shopper account per country/region when testing multiple markets, plus a test card; the page lists AU, NZ, US and Canada sandbox choices and test CVVs. Live acceptance requires a request for Afterpay in live Customer Area. Sandbox country choices are test setup, not a current production support matrix.

## Detail locators

- Sessions prerequisites, required request fields and AU/AUD example: pinned raw lines 15–112; Sessions configuration and repeated capture/test guidance around lines 650–760.
- Advanced prerequisites, request fields and `afterpaytouch` AU/AUD sample: around lines 760–1534; redirect response: lines 1536–1550.
- Capture and partial-capture conditions: lines 1552–1571; sandbox and live setup: lines 1573–1592. The same guidance appears earlier in the Sessions section.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/flutter-component/2026-09-15|Afterpay Flutter Component guide, captured 2026-09-15]]
