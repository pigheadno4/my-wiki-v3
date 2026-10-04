---
title: "Braintree MB WAY Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/mbway"
raw_files:
  - "braintree/docs/guides/local-payment-methods/mbway-2026-09-16.md"
tags: [braintree, local-payment-methods, mb-way, javascript, webhooks]
---

## Overview

This collected Braintree guide describes MB WAY as a Local Payment Method that lets a customer place an order and then complete payment in the MB WAY mobile digital-wallet app. It is a retrieval route for the guide's limited-release pilot availability, merchant and customer applicability, JavaScript-client and server-side SDK scope, and the payment-ID-to-webhook-nonce handoff. The 2026-09-16 snapshot does not establish current availability, a merchant's enablement, buyer eligibility or a completed live payment.

## Key takeaways

- The guide marks MB WAY as a limited release for pilot merchants in selected countries and directs interested merchants to contact Braintree. Its applicability table identifies `mbway`, buyers in Portugal, sellers globally except Russia, Japan and Brazil, `EUR`, and a minimum customer transaction of `1 EUR`; those captured values remain snapshot scope rather than proof of current or individual eligibility.
- The stated prerequisites are a valid PayPal business account created, verified and linked in the Braintree Control Panel and use of the latest Client SDK. The page says MB WAY is available only through the JavaScript Client SDK and various server-side SDKs. Its loading example uses Braintree Web `3.111.0`, but an example script version is not a current support or minimum-version guarantee.
- This method circumvents the normal tokenization process. The guide says no pop-up launches and the merchant receives a payment ID rather than a single-use token in the initial client response; the example instructs the merchant to store that payment ID on its server so it can be mapped to a later Braintree webhook.
- The guide requires merchants to be signed up for Local Payment Method webhooks. It says the merchant receives the nonce needed to transact through the `local_payment_completed` webhook. That notification-and-nonce handoff is not itself evidence of settlement, funding or a particular completion speed.

## Evidence boundaries

> [!warning] Pilot and applicability scope
> Limited-release wording, the captured country/currency table and a fully read documentation snapshot do not prove current program availability, merchant enablement or customer eligibility. Recheck the live program and account-specific conditions before relying on the route.

> [!warning] Initiation, notification and payment outcome
> A successful `startPayment` call or receipt of a payment ID records initiation, not completed payment. The later `local_payment_completed` notification supplies the nonce needed for a subsequent transaction; this page does not say that notification proves settlement or funding, and it does not establish that the path is instant.

> [!warning] Nonce, platform and environment scope
> The initial client response has no single-use token. Keep that response separate from the webhook-delivered nonce, and preserve the guide's JavaScript-client plus server-side SDK boundary. The captured page and examples do not identify a Sandbox or Production execution environment and do not prove execution in either one.

## Detail locators

- Limited-release notice and participation route: `### Overview`, lines 20-21.
- Method identity, PayPal business-account prerequisite and latest-Client-SDK direction: `### Overview`, lines 23-26.
- Payment type, buyer/seller countries, currency and minimum transaction: `### Overview`, lines 28-30.
- Example Client SDK and Local Payments SDK script versions: `### Loading the SDK`, lines 33-42.
- Required Local Payment Method webhook registration and nonce delivery: `### Capturing MB WAY Transactions`, lines 43-46.
- Captured JavaScript-client and server-side SDK limitation: `### MB WAY with GraphQL`, lines 47-51.
- No-pop-up, no-initial-single-use-token and payment-ID behavior: `### Example Requests`, lines 54-58.
- Callback example fields, server-side payment-ID retention and initiation error handling: `### Callback`, lines 59-94.
- Promise-form example and the same payment-ID retention boundary: `### Promise`, lines 96-129.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local-method family guide: [[source-braintree-payment-methods-local-payment-methods]]
- Notification concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/mbway-2026-09-16|Braintree MB WAY guide]] - complete collected page covering pilot availability, applicability, SDK scope, initiation and webhook-nonce handoff
