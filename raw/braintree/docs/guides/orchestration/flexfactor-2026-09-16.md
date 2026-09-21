<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/orchestration/flexfactor -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: FlexFactor Integration Guide
slug: /docs/guides/orchestration/flexfactor/
createTime: '2026-05-12T08:25:29.977Z'
updateTime: '2026-05-19T14:32:35.483Z'
---



# FlexFactor Integration Guide

This guide is for developers integrating FlexFactor with Braintree through the PayPal Orchestration Platform. It covers supported capabilities, required fields, transaction status mapping, and testing for this integration.

When a transaction fails on PayPal Enterprise, FlexFactor's real-time decision engine evaluates it and can recover revenue from false declines.

This integration supports the following card brands:


- Visa
- Mastercard (credit and debit)

For a complete list of countries that this integration supports, contact your Braintree account manager (AM) or technical account manager (TAM).

For links to the Braintree documentation for transaction processing through the SDK or GraphQL, see [Related content](#related-content).


## Features

The following topics summarize the capabilities that this integration supports.


### Core transaction lifecycle

The following table describes support for the core transaction lifecycle operations with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | SDK | GraphQL | Support | Notes |
| --- | --- | --- | --- | --- |
| Charge (single step) | ✅ | ✅ | ❌ | Authorize and capture in the same call. |
| Charge (dual step) | ✅ | ✅ | ✅ | A separate capture call follows authorization. |
| Standalone authorization | ✅ | ✅ | ✅ | You must capture the authorization within 7 days. |
| Capture (full) | ✅ | ✅ | ✅ | Captures a previously authorized transaction |
| Partial capture | ✅ | ✅ | ❌ |  |
| Capture greater than authorized amount | ✅ | ✅ | ❌ |  |
| Adjust Authorization API (incremental authorization or partial reversal) | ✅ | ✅ | ❌ |  |


### Voids and refunds

The following table describes support for voids and refusals with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Full void (auth reversal) | ✅ | Voids cancel an authorized transaction prior to settlement. |
| Partial void | ❌ |  |
| Void on settled transaction | ❌ | Use a refund instead. |
| Full refund | ✅ | Refunds cannot exceed the settled amount. |
| Partial refund | ✅ | Refunds cannot exceed the settled amount. Partial refunds are limited to 60% of the original order price. |
| Multiple refunds | ✅ |  |
| Blind credits (refunds for transactions processed elsewhere) | ❌ | Refunds must reference the original transaction. |


### Payment instruments and methods

The following table lists payment instruments and methods that this integration supports.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Instrument or method | Support | Notes |
| --- | --- | --- |
| Credit cards | ✅ | Visa, Mastercard |
| Debit cards | ✅ | Visa, Mastercard |
| Prepaid cards | ❌ |  |
| PLCCs | ❌ |  |
| Gift cards | ❌ |  |
| Apple Pay | ❌ |  |
| Google Pay | ❌ |  |
| Android Pay or Samsung Pay | ❌ |  |
| Venmo or PayPal | ❌ |  |


### Data, descriptors, and fraud signals

The following table lists data fields, descriptors, and fraud signals and describes their support in this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Address Verification System (AVS) or Card Verification Value (CVV) response handling | ❌ |  |
| Dynamic descriptors | ⚠️ | Support is limited to only pre-approved descriptors. |
| Network tokens | ❌ | To enable network tokens, contact your AM or TAM. |
| Level 2, Level 3, or Lodging data | ❌ |  |
| 3D Secure (3DS) | ✅ |  |


### Verifications

The following table lists support for different card verification methods.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support |
| --- | --- |
| $0 verification | ❌ |
| Non-zero dollar verification | ❌ |


## Before you begin

To prepare for the FlexFactor integration, prepare the following requirements:


- **FlexFactor configuration and credentials:**Each merchant must have an account with FlexFactor. To securely share the[FlexFactor credentials](https://guides.flexfactor.io/docs/credentials/)with Braintree, work with your AM or TAM.
- **Merchant account setup:**To process transactions with FlexFactor, you need currency-specific merchant accounts for use in your integration. Your Braintree AM or TAM can help facilitate this setup.

If you do not have a dedicated AM or TAM for Braintree, contact[clientonboarding@braintreepayments.com](mailto:clientonboarding@braintreepayments.com)for support.After you complete this setup, continue with [FlexFactor integration](#flexfactor-integration) to configure the connection.


## FlexFactor integration

The FlexFactor integration uses a direct connection through Braintree. Transactions are routed directly to FlexFactor, bypassing intermediate processing steps.

The retry logic in this integration is merchant-driven: you first attempt the transaction, and then you decide when to trigger a retry attempt to FlexFactor.
## Transaction status mapping

The following table maps FlexFactor response statuses to Braintree transaction statuses.

| Operation | FlexFactor response | Braintree transaction status | Notes |
| --- | --- | --- | --- |
| Authorize | Declined | PROCESSOR_DECLINED |  |
| Authorize | Capture required | AUTHORIZED | This status is for dual-step transactions. The authorization window can be from 5 minutes to 7 days. You configure this window with FlexFactor. |
| Authorize | Cancelled | PROCESSOR_DECLINED |  |
| Authorize | API error | FAILED | You can configure a retry option in Braintree for this status or implement your own retry logic. |
| Capture | Success | SETTLED |  |
| Capture | Failed | SETTLEMENT_DECLINED | In the rare event that FlexFactor returns a failed status for capture after a successful authorization, it is because the capture amount differs from the authorized amount or due to technical issues with FlexFactor. |
| Capture | HTTP status 4xx or 5xx | SETTLING | Do not ship goods or consider the transaction successful until the status changes toSETTLED.  In the rare event that FlexFactor returns HTTP status 4xx/5xx for capture after successful authorization, it is due to: an invalid or malformed payload sent to FlexFactor, or a network or server overload error.  Retry logic: Braintree automatically retries this transaction on FlexFactor until a final status is received.  **Possible outcomes:**If approved by FlexFactor, status moves toSETTLED. If declined by FlexFactor, status moves toSETTLEMENT_DECLINED. |
| Charge (dual step) | Success | SETTLED | When performing a charge using the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)or[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--chargePaymentMethod/), Braintree orchestrates a dual-step transaction: it first authorizes the transaction, then it immediately captures it on a successful authorization. |
| Charge (dual step) | Failed | SETTLEMENT_DECLINED |  |
| Charge | HTTP status 4xx/5xx | SETTLING | Do not ship goods until the status changes toSETTLED.  In the rare event that FlexFactor returns HTTP status 4xx or 5xx for charge, it is due to a successful authorization but a capture error.  **Retry logic:**Braintree automatically retries this transaction on FlexFactor until a final status is received.  **Possible outcomes:**If FlexFactor approves the transaction, the status changes toSETTLED. If FlexFactor declines the transaction, the status changes toSETTLEMENT_DECLINED. |
| Refund | Success | SETTLED |  |
| Refund | Failed | SETTLEMENT_DECLINED | In the rare event that FlexFactor returns a failed status for a refund, it is due to technical issues with FlexFactor. |
| Refund | HTTP status 4xx/5xx | SETTLING | In the rare event that FlexFactor returns HTTP status 4xx or 5xx for a refund, it is due to an invalid or malformed payload sent to FlexFactor or a network or server overload error.  **Retry logic:**Braintree automatically retries this transaction on FlexFactor until it receives a final status.  **Possible outcomes:**If FlexFactor approves the transaction, the status changes toSETTLED. If FlexFactor declines the transaction, the status changes toSETTLEMENT_DECLINED. |
| Void | Voided | VOIDED |  |


## Required fields

All FlexFactor transactions require the fields in the following table.

| Field name | Type | Notes |
| --- | --- | --- |
| amount | Number | Transaction amount in the smallest currency unit (for example, cents for USD) |
| customer.firstName | String | Customer's first name |
| customer.lastName | String | Customer's last name |
| billing.streetAddress | String | Street for the billing address |
| billing.region | String | Region or state for the billing address |
| billing.locality | String | City or locality for the billing address |
| billing.postalCode | String | Postal code or ZIP code for the billing address |
| card.cardHolderName | String | Name on the card |
| card.expirationMonth | String | Card expiration month (MM) |
| card.expirationYear | String | Card expiration year (YYYY) |
| card.number | String | Card number |


## Testing

Use the following test cards to verify that your integration is working correctly.


### Test cards: Success

The following test cards return a [success response](#status-mapping) when the transaction goes through FlexFactor.

| Card brand | Braintree test card | FlexFactor test card | CVV | Automatically mapped? |
| --- | --- | --- | --- | --- |
| Visa | 4005519200000004 | 4000002760003184 |  | Yes |
| Visa | 4111111111111111 | 4111111111111111 | 123 | Yes |
| Mastercard | 5555555555554444 | 51002600235851 | 123 | Yes |


### Test cards: Failure

Any Braintree test cards that are not listed in [Success](#success) will return a [declined error](#status-mapping) from FlexFactor.


## Disputes

FlexFactor handles all disputes. FlexFactor supports dispute notifications and is responsible for handling chargebacks, including deflection strategies and re-presentment processes as needed.


## Related content

For more information about Braintree transaction processing, see the related topics in the Braintree documentation.


- **Authorization**with the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--authorizeCreditCard/)
- **Capture**with the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/submit-for-settlement/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--captureTransaction/)
- **Charge**with the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--chargePaymentMethod/)
- **Void**with the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/void/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--reverseTransaction/)
- **Refund**with the[SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/refund/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--refundTransaction/)
- **Verifying a card**with the[SDK](https://developer.paypal.com/braintree/articles/control-panel/vault/card-verification/)or with the[GraphQL API](https://developer.paypal.com/braintree/graphql/reference/#Mutation--verifyCreditCard/)

