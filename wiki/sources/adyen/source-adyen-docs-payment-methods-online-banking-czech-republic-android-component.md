---
title: "Online banking Czech Republic Android Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/android-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15.md"
tags: [adyen, online-payments, online-banking-czech-republic, android, components]
---

## Overview

This 2026-09-15-captured Adyen add-on explains Online banking Czech Republic in an existing Android Components integration, separately for Sessions and Advanced flows. It covers the method module, optional button setting, Component launch, redirect handling, and test/live steps. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK method context. It is not evidence of current account enablement or completed payment.

## Key takeaways

- Sessions requires an existing Android Components Sessions integration, Checkout API v68 or later, redirect handling for action.type redirect, and Customer Area method setup. The page says no extra method parameters are needed in /sessions. Import the onlineBankingCZ module, plus components-compose when using Jetpack Compose. See raw lines 25–65.
- Both flows offer optional setSubmitButtonVisible configuration: false hides the submit button and true is the stated default. The Required cell is blank. The guide names OnlineBankingCZComponent for launch, shows Compose and view attachment variants, and uses PaymentMethodTypes.ONLINE_BANKING_CZ in the examples. The Compose examples state that a new key is needed for a new Component across screens/sessions or when resetting it. See raw lines 67–143 and 186–263.
- Advanced requires an existing Android Components Advanced integration, action handling for action.type redirect, and Customer Area method setup. Its example selects the method from a /paymentMethods response, and the page says no additional parameters are needed for the method in /payments. This is scoped to the Android Components guide, not a claim that a custom API-only bank-selection flow omits its issuer. See raw lines 153–183 and 209–270; compare [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- The test section instructs testing with real payment details and small amounts, checking test payment status in the test Customer Area Payment list, and adding the method in Customer Area for live acceptance. These are captured instructions, not evidence of actual test or live payments. See raw lines 145–151 and 272–278.

## Detail locators

- Sessions prerequisites and no extra /sessions fields: raw `## Sessions flow Component`, lines 25–42.
- Module imports with/without Compose: raw `## Import the Component for Online banking Czech Republic`, lines 44–65 and 163–184.
- Button configuration and Component launch: raw lines 67–143 and 186–263.
- Advanced redirect/action prerequisites and no extra /payments fields: raw `## Advanced flow Component`, lines 153–161 and 266–270.
- Test/live instructions: raw `## Test and go live`, lines 145–151 and 272–278.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/android-component/2026-09-15|Online banking Czech Republic Android Component, captured 2026-09-15]]
