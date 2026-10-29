---
title: "Online banking Finland React Native Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/react-native-drop-in/2026-09-15.md"
tags: [adyen, finland-online-banking, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland to an existing React Native Drop-in integration** through Sessions or Advanced server-side flow. It covers required shopper email, conditional Advanced issuer, redirect action and Paytrail testing. A redirect action is not proof of completed payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-finland-online-banking]] for Paytrail/FI/EUR context and bank-selection/refund-note qualifications.

## Key takeaways

- **Sessions flow** requires an existing React Native Drop-in Sessions integration, Checkout API **v68 or later**, redirect handling and Customer Area method addition (raw lines 25–36). Its prerequisite's “Sessions flow” link incorrectly points to an **Advanced-flow** URL, while the redirect and session-creation links point to Sessions; verify the correct base guide (raw lines 33–42).
- Sessions `/sessions` adds required `shopperEmail`. The FI/EUR test examples repeatedly show `s.hopper@@example.com`, which has two `@` signs, so it is not a valid email value to copy (raw lines 40–339). The page says no Finland-specific Drop-in configuration is needed (raw lines 342–346).
- **Advanced flow** requires an existing React Native Drop-in Advanced integration, redirect handling and Customer Area setup; no Checkout API minimum is stated in its requirements (raw lines 354–364). It also says no Finland-specific configuration is needed (raw lines 366–370).
- Advanced `/payments` explicitly requires `paymentMethod.type: ebanking_FI` and `shopperEmail`. `paymentMethod.issuer` is relevant and required **only for the Issuer redirect flow**; `returnUrl` is listed without a required mark and has a 1024-character maximum (raw lines 372–383). The curl and SDK request examples **omit `paymentMethod` entirely** despite the required type (raw lines 385–668). Treat those as incomplete illustrations, not full executable requests, and do not convert the conditional issuer into a universal requirement.
- The Advanced sample response gives `resultCode: RedirectShopper` and `action.type: redirect` (raw lines 670–684). Before accepting live payments, both sections direct testing with Paytrail's test environment/sample data and state **testing multiple partial refunds is currently unavailable** (raw lines 348–352, 686–690). This captured test limitation is distinct from the overview's matrix mark for multiple partial refunds.
- The Sessions and Advanced curl snippets omit a continuation after `-X POST` before `-d` (raw lines 53–69, 389–405); use the field table and API contract rather than copying these as complete commands.

> [!warning] Advanced request examples omit a required field
> The Advanced table marks `paymentMethod.type: ebanking_FI` required (raw line 380), but all displayed `/payments` examples omit `paymentMethod` (raw lines 385–668). Verify the applicable API contract; `issuer` is required only in the Issuer redirect flow (raw line 381).

## Detail locators

- Sessions prerequisite and mismatched base-guide link: raw `## Sessions flow Drop-in`, lines 25–42.
- Sessions required email, sample requests and no-configuration claim: raw lines 44–346.
- Sessions Paytrail testing/refund limit: raw lines 348–352.
- Advanced prerequisites and no-configuration claim: raw `## Advanced flow Drop-in`, lines 354–370.
- Advanced conditional issuer, incomplete examples and redirect response: raw lines 372–684.
- Advanced Paytrail testing/refund limit: raw lines 686–690.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/react-native-drop-in/2026-09-15|Online banking Finland React Native Drop-in, captured 2026-09-15]]
