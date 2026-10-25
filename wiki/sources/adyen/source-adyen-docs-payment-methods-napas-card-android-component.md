---
title: "Adyen Napas card Android Component integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/android-component"
raw_files:
  - "adyen/docs/payment-methods/napas-card/android-component/2026-09-15.md"
tags: [adyen, napas, vietnam, android, components, cards]
---

## Overview

This [[adyen]] guide adds **Napas card** to an existing Android Components integration using Sessions or Advanced flow. It expressly targets Components **v5.0.0** (released October 2023) and links a separate earlier-version guide. See [[adyen-online-payments]] and [[adyen-android-sdk]]. This 2026-09-15 snapshot is not proof of current merchant eligibility, card authorization or settlement.

## Key takeaways

- Both flow tabs require the matching existing Android Components Sessions or Advanced integration at **minimum v5.0.0** and adding Napas card in Customer Area. The page does not state a Checkout API minimum. See raw lines 19–39.
- For Sessions `/sessions` and Advanced `/payments`, the guide says no additional **Napas-specific** fields are needed. It also says no additional Napas Component configuration in either flow. These are method add-on statements, not permission to omit the base request, card/gateway handoff or payment-result handling. Sessions links to checkout-session creation and Advanced to launching/showing the Component. See raw lines 41–67.
- The TEST section asks the shopper to select a bank and gives test-card/OTP fixtures for **successful, blocked, insufficient-funds and amount-limit** scenarios. It then points to the test Customer Area payment list for status. These fixtures are not live card credentials or proof that a particular authorization occurred; this page does not explain where the shopper enters the card number, PIN or OTP. The separately pinned Napas overview locates those steps on the provider gateway. See raw lines 69–80 and [[source-adyen-docs-payment-methods-napas-card]].
- Before live acceptance, the page requires submitting a Napas card request in the **live Customer Area**. It gives no full redirect-return, `/payments/details`, webhook, capture or settlement contract. The page also gives no explicit payment-method type value; do not infer that older-version `momo_atm` snippets are a v5 Components contract. See raw lines 41–88.

## Detail locators

- **v5 scope, prior-version route and flow prerequisites:** raw lines 19–39.
- **No extra method fields/configuration, Sessions/Advanced next links:** raw lines 41–67.
- **TEST scenarios and status:** raw lines 69–80.
- **Live Customer Area request:** raw line 82.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-napas-card]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/napas-card/android-component/earlier-versions/2026-09-15|Napas card Android Component earlier versions]] — linked historical route; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/android-component/2026-09-15|Napas card Android Component guide — captured 2026-09-15]]
