---
title: "Online banking Thailand iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/ios-drop-in/2026-09-15.md"
tags: [adyen, online-banking, thailand, ios, drop-in, redirect]
---

## Overview

This [[adyen]] page, captured 2026-09-15, describes **Online banking Thailand-specific additions** to an existing iOS Drop-in integration for Sessions or Advanced server-side flow. It relies on the base integration guides. For the method's TH/THB, bank-redirect and asynchronous-result context, see [[source-adyen-docs-payment-methods-online-banking-thailand]] and [[adyen-online-payments]]. This page alone does not show current merchant eligibility or an executed payment. See raw lines 15–23.

## Key takeaways

- **Sessions:** an existing iOS Sessions Drop-in integration must use Checkout API **v68+** and add Online banking Thailand in Customer Area. The page says no extra method-specific `/sessions` request fields or configuration parameters are needed. The stated v68+ prerequisite is in the Sessions section; the Advanced section does not state that minimum. See raw lines 25–46.
- **Advanced:** an existing iOS Advanced Drop-in integration must be set up to handle `action.type: redirect` and add the method in Customer Area. The page says no extra method-specific configuration parameters or `/payments` request fields are needed. This does not remove the base integration's ordinary requirements, and redirect handling is a shopper-flow step rather than proof of final authorization. See raw lines 58–80.
- **TEST and live:** both sections suggest test payments with any issuer ID available for the Online banking Thailand Component for the relevant country/region, followed by a status check in the TEST Customer Area. The page does not list the issuer IDs or guarantee their availability. Before live acceptance, it directs a **separate request** for Online banking Thailand in the live Customer Area. Test instructions and a status-check route are not evidence of a successful live payment or settlement. See raw lines 48–56 and 82–90.

## Detail locators

- Purpose and dependency on existing flow: raw lines 15–23.
- Sessions v68+ prerequisite, setup and no additional session/configuration parameters: raw lines 25–46.
- Advanced redirect prerequisite, setup and no additional configuration/payment parameters: raw lines 58–80.
- TEST issuer/status instructions and separate live request: raw lines 48–56 and 82–90.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-thailand]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/ios-drop-in/2026-09-15|Online banking Thailand iOS Drop-in guide — captured 2026-09-15]]
