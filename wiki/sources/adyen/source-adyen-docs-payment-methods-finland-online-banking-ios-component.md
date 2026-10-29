---
title: "Online banking Finland iOS Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/ios-component"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/ios-component/2026-09-15.md"
tags: [adyen, finland-online-banking, ios, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland to an existing iOS Components integration**, with Sessions and Advanced server-side flow instructions. It covers required shopper email, `InstantPaymentComponent`, redirect action and Paytrail testing. Redirect presentation is not proof of final payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-finland-online-banking]] for Paytrail/FI/EUR context and its bank-selection and refund-note qualifications.

## Key takeaways

- **Sessions flow** requires existing iOS Components Sessions integration, Checkout API **v68 or later**, `action.type: redirect` handling, and Online banking Finland added in Customer Area. Its `/sessions` addition is required `shopperEmail` (raw lines 25–46). The examples use FI/EUR and an iOS-style return URL, but repeatedly show `s.hopper@@example.com` (two `@` signs); do not copy that address as valid test data (raw lines 48–339).
- Sessions needs no Finland-specific Component configuration. The Swift example checks for payment method `.other("ebanking_FI")`, creates an `InstantPaymentComponent`, assigns the session as delegate and calls `initiatePayment()` (raw lines 342–368). This is Component initiation, not authorization.
- **Advanced flow** requires existing iOS Components, redirect handling, and Customer Area setup. Its “iOS Components integration” link points to an **iOS Drop-in** base URL (`integration=Drop-in`), while the redirect-handling link points to Components; verify the correct base guide (raw lines 376–386). It likewise needs no Finland-specific configuration and uses `InstantPaymentComponent` with the Component's own delegate (raw lines 388–413).
- Advanced `/payments` explicitly requires `paymentMethod.type: ebanking_FI` and `shopperEmail`. `paymentMethod.issuer` is required **only for the Issuer redirect flow**; `returnUrl` is listed without a required mark and has a 1024-character maximum (raw lines 415–426). The examples at raw lines 430–710 **omit `paymentMethod` entirely**, despite the required type. Treat them as incomplete illustrations, not executable full requests; do not infer that the issuer is always required or never required.
- The Advanced sample response gives `resultCode: RedirectShopper` and `action.type: redirect` (raw lines 713–727). The guide says to test with Paytrail's test environment/sample data before live acceptance and states **testing multiple partial refunds is currently unavailable** (raw lines 370–374, 729–733). This is a captured test limitation, not a reversal of the approved method overview's matrix mark for multiple partial refunds, whose own refund note is absent.

> [!warning] Required field missing from Advanced examples
> The Advanced field table marks `paymentMethod.type: ebanking_FI` required (raw line 423), but curl and SDK request examples omit `paymentMethod` (raw lines 430–710). Follow the field table and API contract, and check whether the Issuer redirect flow applies before providing `paymentMethod.issuer` (raw line 424).

## Detail locators

- Sessions prerequisites, email field and request examples: raw `## Sessions flow Component`, lines 25–339.
- Sessions no-configuration claim and Swift Component initiation: raw lines 342–368.
- Advanced base-link mismatch, configuration and Swift initiation: raw `## Advanced flow Component`, lines 376–413.
- Advanced conditional issuer and required type/email; incomplete examples: raw lines 415–710.
- Redirect response and Paytrail testing/refund limitation: raw lines 713–733.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/ios-component/2026-09-15|Online banking Finland iOS Component, captured 2026-09-15]]
