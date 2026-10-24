---
title: "Adyen KakaoPay iOS Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15.md"
tags: [adyen, kakaopay, ios, components, tokenization]
---

## Overview

This 2026-09-15 Adyen guide describes KakaoPay-specific additions to an **existing iOS Components** integration, with separate Sessions and Advanced server-side flows. It is not a complete payment integration or evidence of current merchant eligibility. [[adyen]] [[adyen-ios-sdk]]

## Key takeaways

- The Sessions path requires an existing iOS Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling, and KakaoPay added in Customer Area. The Advanced path requires an existing iOS Components Advanced flow, redirect handling and the Customer Area addition; this page states no separate Advanced API minimum. It says there are no KakaoPay-specific configuration parameters, no extra base `/sessions` fields, and no extra base `/payments` fields. These statements do not waive the underlying flow's ordinary request, return and outcome handling.
- Both paths use `InstantPaymentComponent` for payment method `.other("kakaopay")`, guard that the method was returned before presenting it, and call `initiatePayment()`. Sessions delegates to `session`; Advanced delegates to the integration object (`self`). The Advanced integration-type prose says Components but its link includes `integration=Drop-in`; use the correct main Components guide and selected SDK version before copying the snippet.
- **Recurring is an explicit exception to the no-extra-base-fields text.** The guide says a shopper first logs into Kakao and confirms the recurring transaction. For token creation, the initial `/payments` request includes `storePaymentMethod: true` and a unique `shopperReference`; the server must receive Recurring tokens lifecycle events. It says `recurring.token.created` arrives after settlement and carries `storedPaymentMethodId`. A later token `/payments` request uses that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. Authentication/confirmation and a token request do not by themselves establish settlement or success of a later charge.
- The repeated example requests use TEST endpoints or clients, `kakaopay`, and KRW amounts. These examples do not establish a universal currency or country eligibility rule; the Java example uses KRW 15000 while nearby examples use KRW 1000. Library-version comments include Node v16.1.0, Python v12.0.0 and Ruby v9.1.0, so snippets need version-specific review.
- The test/live section says a real mobile number registered with a KakaoPay account is needed to test successful KakaoPay **live** payments, yet it also directs readers to the **test** Customer Area for test-payment status. This wording does not establish a test-account recipe or prove live readiness. Before accepting live KakaoPay payments, the guide says to submit a request in the live Customer Area. It gives no final payment-result or webhook-outcome instructions here; use the main integration and applicable webhook guidance before treating a redirect or Component callback as authorization, capture or settlement.

## Detail locators

- Page scope and flow selection: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 15–23.
- Sessions prerequisites, no extra base parameters/configuration and Component example: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 25–70.
- Sessions recurring creation, Kakao login/confirmation, settlement-linked token webhook and later ContAuth fields: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 72–111.
- Sessions TEST recurring payment examples, method/currency/version details and test/live wording: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 113–320.
- Advanced Components-versus-Drop-in link, redirect prerequisite, Component example and no-extra-base-fields statement: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 322–365.
- Advanced recurring requirements, examples and repeated test/live section: [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|KakaoPay iOS Component raw]], lines 367–615.

## Related

- [[adyen-ios-sdk]] — iOS Component and Sessions/Advanced architecture.
- [[adyen-tokenization]] — stored-method lifecycle and consent context.
- [[adyen-online-payments]] — merchant server and payment-outcome context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15|Adyen KakaoPay iOS Component guide (2026-09-15 snapshot)]]
