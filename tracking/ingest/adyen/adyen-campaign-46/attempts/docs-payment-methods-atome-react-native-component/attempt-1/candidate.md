---
title: "Adyen Atome React Native Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/atome/react-native-component/2026-09-15.md"
tags: [adyen, atome, react-native, components, advanced-flow, redirect]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds Atome to an existing **React Native Components Advanced-flow** integration. It explicitly says React Native Components do **not** support Sessions flow. The page provides method-specific `/payments` fields, a redirect example, partial-refund note and test/live setup; it does not supply a standalone React Native Component implementation. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-atome|Atome overview]]. This snapshot does not establish current account eligibility or a completed payment.

## Key takeaways

- **Advanced-only setup:** Use an existing React Native Components Advanced integration with redirect handling and add Atome in Customer Area. No Atome-specific Component configuration parameters are required. The prerequisite integration link at raw line 39 is labeled React Native Components but its URL has `integration=Drop-in`; nearby redirect and payment links at lines 40 and 53 use `integration=Components`. Use the latter to navigate the relevant Components base steps; this page does not verify the mismatched prerequisite link's behavior.
- **Payment fields and regions:** The `/payments` table marks `paymentMethod.type: atome`, shopper full name, email, phone, billing address, line items and country code required. Delivery address is optional when it equals billing. The supported country/currency pairs stated are **MY/MYR** and **SG/SGD**. The TEST v72 sample uses SG/SGD and an HTTPS `returnUrl`; a React Native app must configure return/redirect handling for its actual flow rather than assume that Web URL example works in-app. The curl sample omits a shell continuation before `-d`, so is not copy-ready.
- **Redirect state:** The sample response has `resultCode: RedirectShopper` and `action.type: redirect`. Although its heading says “example response for a successful payment,” this response requests further shopper action, not a completed authorization or capture.
- **Refund and live boundary:** The method-specific partial-refund note specifies the refunded `amount` in `/payments/{paymentPspReference}/refunds`; the cancellations heading adds no method-specific cancel rule. Testing requires an Atome sandbox shopper account from an Adyen contact, a different account per country/region, and the page links QR test apps and test Customer Area status. Live acceptance requires Support to add Atome in live Customer Area. The separate overview contains a portable-electronics restriction and automatic-capture statement not repeated in this add-on.

## Detail locators

- Flow availability, Advanced requirements, link mismatch and no extra configuration: pinned raw lines 23–47. `/payments` fields, MY/MYR and SG/SGD pairs and TEST v72 request: lines 49–129. Language SDK variants: lines 131–779.
- Misleading successful-payment heading and redirect action: lines 781–793. Partial refund and test/live setup: lines 795–823. See [[source-adyen-docs-payment-methods-atome]] for method-level restrictions.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-atome]] — method overview and product restrictions

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/react-native-component/2026-09-15|Atome React Native Component guide, fetched 2026-09-15]]
