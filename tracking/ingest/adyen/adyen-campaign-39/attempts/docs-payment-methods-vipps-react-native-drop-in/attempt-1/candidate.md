---
title: "Adyen Vipps React Native Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/vipps/react-native-drop-in/2026-09-15.md"
tags: [adyen, vipps, react-native, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes Vipps-specific additions to an existing React Native Drop-in integration, separately for Sessions and Advanced server-side flows. It covers redirect readiness, method-specific request information, and test/live setup. It is a dated guide, not current merchant eligibility or evidence that a payment was executed. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires an existing Sessions React Native Drop-in integration, Checkout API v68 or later, `action.type: redirect` handling, and Vipps in Customer Area. It lists `shopperStatement` as the description shown in the Vipps app, defaulting to `reference` when omitted, and states a minimum `amount.value` of 100 minor units, or 1.00 NOK. The table's Required cells are blank, so the table does not establish that `shopperStatement` is mandatory. No Vipps-specific configuration parameters are stated. The Sessions Integration type label links to an Advanced-flow URL, while later Sessions links point to Sessions flow. (raw lines 25–74)
- **Advanced:** The page requires an existing Advanced React Native Drop-in integration, `action.type: redirect` handling, and Vipps in Customer Area. It lists `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` with the same reference fallback, a relevant `channel`, and the same 100-minor-unit/1.00-NOK minimum. These table rows have blank Required cells; do not promote the listed examples to unconditional field requirements. No Vipps-specific configuration parameters are stated. The Advanced section does not separately state the Sessions v68+ API minimum. (raw lines 104–160)
- **Redirect and outcome:** The Advanced sample returns `resultCode: RedirectShopper` with `action.type: redirect`; this is a handoff state, not payment authorization or settlement. For live low-amount tests, the guide tells the merchant to receive an `AUTHORISATION` webhook on its server and inspect the live payment list for status. The page does not provide a complete return/details or capture/refund procedure. (raw lines 160–174, 194–202)
- **TEST and LIVE:** The test path uses a Vipps developer test app, adds Vipps to the test merchant account, makes a test request and has the shopper authorize the test-app notification. Live acceptance requires a separate request in the live Customer Area; after Adyen adds Vipps there, the guide calls for low-amount live payments and status checks. Test-app authorization and redirect response are not themselves proof of a live payment. (raw lines 76–102, 176–202)
- **Example caution:** The Sessions prerequisite's Advanced-flow link conflicts with its Sessions label. Both curl samples put `-X POST` on a line without a continuation marker before `-d`. The Advanced table suggests relevant channel values such as Web, iOS or Android, while its sample says `React-native`; treat the sample as illustrative and check the base integration's versioned field contract. (raw lines 33, 49–68, 126–158)

## Detail locators

- Sessions requirements, request rows, example and no-extra-configuration statement: raw lines 25–74.
- Sessions TEST app and live request/status process: raw lines 76–102.
- Advanced requirements, request rows and sample redirect action: raw lines 104–174.
- Advanced repeated TEST and LIVE process: raw lines 176–202.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/react-native-drop-in/2026-09-15|Adyen Vipps React Native Drop-in guide, 2026-09-15 snapshot]]
