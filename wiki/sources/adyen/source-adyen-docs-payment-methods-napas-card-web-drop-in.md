---
title: "Napas card Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/napas-card/web-drop-in/2026-09-15.md"
tags: [adyen, napas-card, web, drop-in, vietnam]
---

## Overview

This 2026-09-15 snapshot describes adding Napas card online-banking payments to an existing Adyen Web Drop-in integration. It is a method-specific supplement and assumes the underlying Drop-in is already built. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Before this add-on, the merchant should have an existing Web Drop-in integration and add Napas card in the test Customer Area. The page says no Napas-specific API fields or Drop-in configuration steps are required. See raw lines 19–37.
- The API reference identifies `/sessions` as the default with Drop-in v5.0.0 or later, while `/payments` is for an additional use case. This is the page's historical version/flow wording; it does not set a new Checkout API minimum or establish that both endpoints are used in one payment. See raw lines 28–33.
- The TEST section gives four scenario fixtures: successful, card blocked, insufficient funds and amount over limit, with a bank selection, test card details and one-time password. It directs checking test payment status in Customer Area Payment list. These fixture labels are scenario inputs, not proof of a completed transaction or production behavior. See raw lines 39–50.
- The page separately requires a request for Napas card in live Customer Area before accepting live payments. Test setup does not imply live enablement. See raw lines 25–26 and 52.
- This guide does not specify a payment-method identifier, redirect action, details request or webhook outcome procedure. Follow its linked base integration and webhook references for those topics rather than inferring them from the test-card table. See raw lines 28–58.

## Detail locators

- Integration/setup and API/configuration scope: raw lines 19–37.
- TEST fixture table and status location: raw lines 39–50.
- Separate live request and related guides: raw lines 52–58.

## Related

- [[adyen-online-payments]] — main online-payments concept.
- [[source-adyen-docs-payment-methods-napas-card]] — separate method overview.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/web-drop-in/2026-09-15|Napas card Web Drop-in (2026-09-15)]]
