---
title: "Adyen iDEAL | Wero React Native Component guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/ideal/react-native-component/2026-09-15.md"
tags: [adyen, ideal, wero, react-native, components, redirect, sepa, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing React Native Components integration. It explicitly says Sessions Components are unavailable and provides an Advanced redirect path, followed by a separate SEPA Direct Debit token route for later shopper-absent payments. Its title/heading say “React Component,” but the canonical URL, prerequisites and linked platform say React Native; the shorter label does not establish a distinct product. This snapshot does not prove current merchant enablement, token issuance or successful payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Advanced only:** React Native Components do not support Sessions flow. Advanced requires an existing React Native Components Advanced integration, `action.type: redirect` handling and iDEAL | Wero added in Customer Area. The page says no method-specific Component configuration or normal `/payments` parameters are needed. Its integration-type row links to a React Native **Drop-in** URL while the text and redirect/make-payment links say **Components**; use the named Components flow and verify the main integration route. No React Native SDK version or Checkout API minimum is stated here. (raw lines 25–53)
- **Recurring:** later iDEAL | Wero payments are described through **SEPA Direct Debit**, not another iDEAL redirect. Create a shopper token with standard tokenization parameters; `recurring.token.created` carries `storedPaymentMethodId`. The guide limits tokenised payments here to shopper-absent `UnscheduledCardOnFile` and `Subscription` scenarios. Its subscription examples use `paymentMethod.type: sepadirectdebit`, a stored method ID, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`. The Java sample uses EUR 15000 while the other examples use EUR 1000 and omits `shopperReference` shown by the others; the examples are illustrative rather than a single consistent request contract. (raw lines 55–280)
- **Outcome:** for the illustrated token payment, successful receipt returns `resultCode: Received` and `pspReference`; the guide directs actual payment-success tracking to webhooks. `Received` is not proof of authorization, capture or settlement. (raw lines 282–287)
- **Testing:** the source warns that its iDEAL | Wero TEST environment is unreliable and recommends live penny testing. Its LIVE procedure uses an issuer bank account, payment-page QR or issuer selection, shopper authorization and Customer Area status check. If TEST is available, `TESTNL2A` offers simulations for Authorised, Canceled, Pending/Received on expiration and Refused. These are conditional test paths, not evidence of current eligibility or a live payment. (raw lines 289–325)

## Detail locators

- Source identity/title mismatch, Sessions exclusion and Advanced prerequisite/link conflict: pinned raw lines 5–53.
- SEPA token creation, shopper-absent scope and multi-language examples: pinned raw lines 55–280.
- `Received` and webhook outcome boundary: pinned raw lines 282–287.
- TEST reliability, LIVE penny procedure and conditional simulations: pinned raw lines 289–325.

## Related

- [[adyen-online-payments]] — main redirect and outcome context
- [[adyen-tokenization]] — provider token lifecycle
- [[source-adyen-docs-payment-methods-ideal]] — iDEAL | Wero overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/react-native-component/2026-09-15|iDEAL | Wero React Native Component guide, 2026-09-15]]
