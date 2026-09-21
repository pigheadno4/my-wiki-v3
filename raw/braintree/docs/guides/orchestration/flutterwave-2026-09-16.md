<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/orchestration/flutterwave -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Flutterwave Integration Guide
slug: /docs/guides/orchestration/flutterwave/
createTime: '2026-05-04T10:34:05.338Z'
updateTime: '2026-05-20T08:20:13.674Z'
---



# Flutterwave Integration Guide

PayPal's Braintree partnership with Flutterwave enables merchants to use their existing Braintree integration to process card-not-present transactions through the PayPal Orchestration platform. Flutterwave's network focuses on Africa and emerging markets. It provides direct card acquisition in regions where traditional global processors have limited reach.

This guide helps developers at merchant sites complete the integration in their environment.

The Flutterwave connector uses a non-public, card-direct API that lets you submit raw card numbers without a preceding tokenization step. This API is distinct from Flutterwave's public-facing products.
## Features

The following topics summarize the capabilities that this integration supports.


### Core transaction lifecycle

The following table describes support for the core transaction lifecycle operations with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Charge (dual-step) | ✅ | Flutterwave orchestrates authorization and capture as a dual-step call. Braintree performs them as separate steps.  For more information and charge outcomes, see[Transaction status mapping](#transaction-status-mapping). Also see the documentation for authorization ([Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--authorizeCreditCard/)) or capture ([Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/submit-for-settlement/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--captureTransaction/)). |
| Charge (single-step) | ❌ |  |
| Standalone authorization | ✅ | You must capture authorization within 7 days (before it expires). For more information, see the authorization documentation for[Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--authorizeCreditCard/). |
| Capture (full) | ✅ | This integration captures a previously authorized transaction synchronously. Note that you must capture an authorization within 7 days. For more information, see the documentation forcapture for[Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/submit-for-settlement/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--captureTransaction/). |
| Partial capture | ❌ |  |
| Capture greater than authorized amount | ❌ |  |
| Adjust authorization API (incremental auth) | ❌ |  |
|  |


### Voids and refunds

The following table describes support for voids and refusals with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Full void (auth reversal) | ✅ | A full void cancels an authorized transaction before settlement. For more information, see the documentation for voids for[Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/void/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--reverseTransaction/). |
| Partial void | ❌ |  |
| Void on settled transaction | ❌ | Use a refund instead. |
| Full refund | ✅ | Refunds cannot exceed the settled amount. For more information about refunds, see the applicable refund documentation for[Braintree SDK](https://developer.paypal.com/braintree/docs/reference/request/transaction/refund/)or[GraphQL](https://developer.paypal.com/braintree/graphql/reference/#Mutation--refundTransaction/). |
| Partial refund | ✅ | Each partial refund creates an independent refund transaction. You can perform multiple partial refunds. |
| Multiple refunds | ✅ | Each refund receives its own transaction ID. |
| Blind credits | ❌ | A refund must reference the original transaction. |
|  |


### Payment instruments and methods

The following table describes support for payment instruments and methods with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Credit cards | ✅ | This integration supports these credit cards: Visa, Mastercard, Verve, American Express, Discover, and Afrigo. For regional, configuration-dependent card brand availability, contact Flutterwave. |
| Debit cards | ✅ | Where the acqiring network supports debit cards, this integration supports these cards: Visa Debit, Mastercard Debit, and Verve Debit. |
| Prepaid cards | ⚠️ | The support for prepaid cards depends on your configuration and region. |
| PLCCs | ❌ |  |
| Gift cards | ❌ |  |
| Apple Pay | ❌ |  |
| Google Pay | ❌ |  |
| Venmo or PayPal | ❌ |  |
|  |


### Data, descriptors, and fraud signals

The following table describes support for data, descriptors, and fraud signals with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| Network tokens | ❌ |  |
| Card Verification Value (CVV) response handling | ✅ | Ensure that CVV match and no-match codes are returned and that they map to standard Braintree CVV response codes. |
| Address Verification System (AVS) response handling | ❌ | This integration does not return AVS. |
| Dynamic descriptors | ❌ |  |
| Level II or Level III data | ❌ |  |
| 3D Secure (3DS) | ❌ |  |
|  |


### Verifications

The following table describes support for verifications with this integration.

**Legend:** ✅ Supported | ❌ Not supported | ⚠️ Conditional or varies by merchant configuration

| Capability | Support | Notes |
| --- | --- | --- |
| $0 verification | ✅ | Braintree sends $0 verification to Flutterwave as aVERIFYoperation. |
| Non-zero verification | ✅ | Braintree passes the non-zero verificationamount to Flutterwave for the verification. |
| VoidCardVerification | ✅ | VoidCardVerification always returnsVOIDEDimmediately, without making a network call. |


## Before you begin

Integrating Flutterwave with Braintree requires configuration in both:


- **In Braintree:**To process card transactions through Flutterwave, you need a Braintree merchant account that you configure for the Flutterwave connector. For help with setting up this account and securely storing your credentials, contact your Braintree account manager (AM) or technical account manager (TAM).
- **In Flutterwave:**To obtain access to Flutterwave's card-direct API, contact Flutterwave. When your account is provisioned, Flutterwave provides a merchant username and password for the sandbox and production environments. To securely share these credentials with Braintree, work with your Braintree AM or TAM.

If you do not have a dedicated AM or TAM for Braintree, contact[clientonboarding@braintreepayments.com](mailto:clientonboarding@braintreepayments.com)for support.For more information that could affect your integration, see[Known limitations](#known-limitations)and[Supported currencies](#supported-currencies).
## Transactions

The following topics describe the requirements for this integration.

Use the Braintree platform for all transaction operations. Performing operations directly with Flutterwave (outside of Braintree) can cause discrepancies or synchronization errors.For general information about Braintree transactions, see:


- [Transactions guide (SDK)](https://developer.paypal.com/braintree/docs/guides/transactions/)
- [Transactions guide (GraphQL)](https://developer.paypal.com/braintree/graphql/guides/transactions/)
- [Transaction response object](https://developer.paypal.com/braintree/docs/reference/response/transaction/)


### Transaction creation

When you create a transaction, include the required fields and any optional fields that are appropriate for your use case.

The following table lists the fields that transactions require.

| Field | Location | How to provide | Notes |
| --- | --- | --- | --- |
| amount | Transaction | In transaction | Transaction amount in the currency's standard decimal format |
| currencyIsoCode | Transaction | In transaction | ISO 4217 currency code (for example, USD, GBP, CAD, NGN, GHS, ZAR)  For the full list of supported currencies, see[Supported currencies](#supported-currencies). |
| paymentMethod.number | Payment method | During tokenization | Raw card number, mapped to Flutterwave test cards in the sandbox evironment |
| paymentMethod.expirationMonth | Payment method | During tokenization | Two-digit expiration month (MM) |
| paymentMethod.expirationYear | Payment method | During tokenization | Four-digit expiration year (YYYY)  **Note:**Braintree sends only the last 2 digits to Flutterwave. |
| paymentMethod.cvv | Payment method | During tokenization | (Optional) Card security code  **Note:**Braintree sends an empty string if this data is not present (for example, for recurring transactions).  For more information, see[CVV handling](#cvv-handling). |


### Fields that Braintree passes to Flutterwave

The following tables list the fields Braintree passes to Flutterwave for each operation.


#### Authorize, charge, and verify card

The following table lists the fields that Braintree passes to Flutterwave for authorization, charge, and verification purposes.

| Braintree field | Flutterwave field | Required | Notes |
| --- | --- | --- | --- |
| amount | order.amount/transaction.amount | ✅ | Passed as-is |
| currencyIsoCode | order.currency/transaction.currency | ✅ | Passed as-is |
| orderId | order.reference,transaction.reference |  | The Braintree order ID, if provided |
| paymentMethod.number | sourceOfFunds.provided.card.number | ✅ | Test card remapping that is applied in the sandbox and development environments |
| paymentMethod.expirationMonth | sourceOfFunds.provided.card.expiry.month | ✅ | Passed as-is |
| paymentMethod.expirationYear | sourceOfFunds.provided.card.expiry.year | ✅ | Braintree sends only the last 2 digits. For example, for 2027, Braintree sends 27. |
| paymentMethod.cvv | sourceOfFunds.provided.card.securityCode |  | Braintree sends an empty string if this data is not present.  For more information, see[CVV handling](#cvv-handling). |


#### Capture

The following table lists the fields that Braintree passes to Flutterwave for capturing transactions.

| Braintree field | Flutterwave field | Required | Notes |
| --- | --- | --- | --- |
| amount | transaction.amount | ✅ | Must not exceed the originally authorized amount |
| currencyIsoCode | transaction.currency | ✅ | Must match the currency of the original authorization |
| orderId | order.reference,transaction.reference |  | The Braintree order ID |
| originResponse.id | URL pathorderId | ✅ | The Flutterwave order ID from the Authorize response |


#### Refund

The following table lists the fields that Braintree passes to Flutterwave for refunds.

| Braintree field | Flutterwave field | Required | Notes |
| --- | --- | --- | --- |
| amount | transaction.amount | ✅ | Must not exceed the settled amount |
| currencyIsoCode | transaction.currency | ✅ | Must match the currency for the original transaction |
| orderId | order.reference,transaction.reference |  | The Braintree order ID |
| originalTransaction.originResponse.id | URL pathorderId | ✅ | The Flutterwave order ID from the original transaction |


#### Void

The following table lists the fields that Braintree passes to Flutterwave for voided transactions.

| Braintree field | Flutterwave field | Required | Notes |
| --- | --- | --- | --- |
| originResponse.id | URL pathorderId | ✅ | The Flutterwave order ID from the Authorize response |
| orderId | transaction.reference |  | The Braintree order ID |


### Customer creation

Creating a customer is optional for the Flutterwave integration. To create a customer, you can use either the Braintree SDKs or the GraphQL API. For more information, see the [customer creation guide (SDK)](https://developer.paypal.com/braintree/docs/guides/customers/ruby/#create) or the [customer creation guide (GraphQL)](https://developer.paypal.com/braintree/graphql/reference/#Mutation--createCustomer).


### Vaulted payment methods

Vaulting a tokenized payment method creates an entity that can be authorized or charged multiple times. A tokenized payment method also can be vaulted during authorization. For more information, see the [vault guide (SDK)](https://developer.paypal.com/braintree/docs/reference/request/payment-method/create) or the [vault guide (GraphQL)](https://developer.paypal.com/braintree/graphql/reference/#Mutation--vaultPaymentMethod).

Recurring transactions (for example, subscriptions) or transactions that use a vaulted card might not include a CVV. This can affect approval rates with some card issuers. To adjust CVV handling, contact your Braintree AM or TAM.
### CVV handling

For merchant-initiated transactions, such recurring transactions, or when using vaulted cards, Braintree does not send the CVV to Flutterwave. Instead, Braintree sends an empty string ( "" ). While Flutterwave accepts transactions without CVV, some card issuers might decline these transactions.


### Supported transaction operations

The following table lists the transaction operations that the Flutterwave integration supports.

| Operation | Supported |
| --- | --- |
| Sale (Authorize or Charge) | ✅ |
| Void | ✅ |
| Refund | ✅ |
| Submit for Settlement (Capture) | ✅ |
| Find or Search | ✅ |
| Clone | ✅ |
| Adjust Authorization | ❌ |
| Hold in Escrow | ❌ |
| Release from Escrow | ❌ |
| Submit for Partial Settlement | ❌ |
| Cancel Release | ❌ |


## Transaction status mapping

The following table maps Flutterwave results to Braintree transaction statuses. For general information about Braintree result objects, see [result objects](https://developer.paypal.com/braintree/docs/reference/general/result-objects/).

| Operation | Flutterwave result | Braintree transaction status | Additional information |
| --- | --- | --- | --- |
| Authorize | SUCCESS | AUTHORIZED | Authorization places a hold on funds |
| Authorize | FAILURE (acquirer code 68 or BB) | FAILED | Treated as a system-level failure, not a soft decline |
| Authorize | FAILURE (other codes) | PROCESSOR_DECLINED | Hard decline from the acquirer |
| Authorize | ERROR | FAILED | Gateway-level error from Flutterwave (for example, validation failure or server error) |
| Capture | SUCCESS | SETTLED | Synchronous capture is confirmed. |
| Capture | FAILURE | SETTLEMENT_DECLINED | A hard decline that occurs during capture |
| Capture | ERROR (voided auth) | VOIDED | Authorization was voided before capture, indicated by an error message that contains "been voided" |
| Capture | ERROR (retryable) | SETTLING | Retryable gateway error (SERVER_BUSY,SERVER_FAILED, or unrecognized error cause) |
| Capture | ERROR (non-retryable) | SETTLEMENT_DECLINED | Permanent failure |
| Refund | SUCCESS | SETTLED | Refund confirmed synchronously |
| Refund | FAILURE | SETTLEMENT_DECLINED | Refund declined by the acquirer |
| Refund | ERROR (retryable) | SETTLING | Retryable gateway error (SERVER_BUSY,SERVER_FAILED, or unrecognized error cause) |
| Refund | ERROR (non-retryable) | SETTLEMENT_DECLINED | Permanent refund failure |
| Void | SUCCESS | VOIDED | Authorization successfully cancelled |
| Void | FAILURE | FAILED | Void declined |
| Void | ERROR | FAILED | Gateway-level error from Flutterwave |
| VerifyCard | SUCCESS | VERIFIED | Card is valid |
| VerifyCard | FAILURE | PROCESSOR_DECLINED | Card declined during verification |
| VerifyCard | ERROR | FAILED | Gateway-level error from Flutterwave |
| VoidCardVerification | Any | VOIDED |  |


### SETTLING status and reconciliation

In rare cases, Flutterwave may return a retryable error ( SERVER_BUSY, SERVER_FAILED, or an unrecognized error cause) after an otherwise-valid capture or refund request. When this occurs, the transaction is placed in SETTLING and Braintree automatically polls Flutterwave for the actual outcome.

Reconciliation behavior varies by operation:


- **Capture reconciliation:**If Flutterwave has not yet processed the capture (transaction still inAUTHORIZATION), returnsAUTHORIZEDfor another reconciliation cycle. If the authorization was voided before capture, returnsVOIDED.
- **Refund reconciliation:**Queries use the compoundorderId|transactionIdfrom the refund's origin response.

Possible outcomes after reconciliation:


- Flutterwave confirms success → status changes toSETTLED.
- Flutterwave returns a 4xx error → status changes toSETTLEMENT_DECLINED.
- Flutterwave returns a 5xx error → status remainsSETTLINGfor another reconciliation cycle.

Do not ship goods or provide services until the transaction status has transitioned to SETTLED. Do not build a duplicate capture or refund retry loop when you see SETTLING.


### Charge operations

Charge for Flutterwave is dual-step. Braintree first performs an authorization and then immediately captures it. The resulting transaction status follows the same outcomes as Capture. For more information, see [Transaction status mapping](#transaction-status-mapping).


## Retries

Do not implement a retry loop when you observe success: true with a status of SETTLING. Braintree handles reconciliation automatically. Always check transaction status before fulfilling an order.

If your request times out or you are unsure whether a transaction was created, query the transaction using Find or Search with your internal transaction reference before attempting a second create.

Retry behavior on FAILED authorization can be configured at the Merchant Account ID (MAID) level. To enable automatic retries, contact your Braintree AM or TAM.


## Response codes

Flutterwave uses ISO 8583-style two-digit acquirer codes for declines. Braintree maps these to standardized Braintree response codes. When a Flutterwave acquirer code is not present in the mapping, Braintree surfaces the raw acquirer code and message in the additionalProcessorResponse field.

To query for the Flutterwave raw response message, use:


- **SDK:**additional_processor_response. For more information, see the[core documentation](https://developer.paypal.com/braintree/docs/reference/response/transaction#additional_processor_response).
- **GraphQL:**PaymentStatusEvent.processorResponse.additionalInformation. For more information, see the[core documentation](https://developer.paypal.com/braintree/graphql/reference/#interface--paymentstatusevent).


### CVV response code mapping

The following table maps Flutterwave CVV codes to their Braintree equivalents.

| Flutterwave CVV code | Flutterwave message | Braintree CVV code | Braintree message |
| --- | --- | --- | --- |
| M | MATCH | M | CVV matches |
| N | NO_MATCH | N | CVV is not verified |
| P | NOT_PROCESSED | U | CVV is not verified |
| S | NOT_PRESENT | I | CVV not provided |
| U | NOT_SUPPORTED | S | Issuer does not participate |
| X | NOT_PROCESSED | U | CVV skipped |


### Failure response code mapping

The following table maps Flutterwave acquirer failure codes to their Braintree equivalents. If a Flutterwave acquirer code is not in this list, Braintree passes through the raw code and message in the additionalProcessorResponse field without a mapped genericResponseCode.

Acquirer codes68andBBare not in this table. Braintree handles these codes as system-level failures. For more information, see[Transaction status mapping](#transaction-status-mapping).| Flutterwave code | Flutterwave message | Braintree code | Braintree message |
| --- | --- | --- | --- |
| 03 | Invalid Merchant | 2026 | Invalid Merchant ID |
| 04 | Pick Up Card | 2047 | Call Issuer. Pick Up Card |
| 05 | Do Not Honour | 2000 | Do Not Honor |
| 06 | Error | 2005 | Invalid Credit Card Number |
| 07 | Pick Up Card, Special | 2047 | Call Issuer. Pick Up Card |
| 08 | Honour With Identification | 1001 | Approved, check customer ID |
| 09 | Request In Progress | 2105 | Processor Declined |
| 10 | Approved For Partial Amount | 1004 | Approved for Partial Amount |
| 11 | Approved, VIP | 1000 | APPROVED |
| 12 | Invalid Transaction | 2019 | Invalid Transaction |
| 13 | Invalid Amount | 2048 | Invalid Amount |
| 14 | Invalid Card Number | 2005 | Invalid Credit Card Number |
| 15 | No Issuer | 2009 | No Such Issuer |
| 16 | Approved, Update Track 3 | 1000 | APPROVED |
| 19 | Re-enter Last Transaction | 3000 | Processor Network Unavailable – Try Again |
| 21 | No Action Taken | 2034 | No Action Taken |
| 22 | Suspected Malfunction | 2034 | No Action Taken |
| 23 | Unacceptable Transaction Fee | 2034 | No Action Taken |
| 25 | Unable to Locate Record On File | 2009 | No Such Issuer |
| 30 | Format Error | 2005 | Invalid Credit Card Number |
| 31 | Bank Not Supported By Switch | 2025 | Bank Not Supported By Switch |
| 33 | Expired Card, Capture | 2004 | Expired Card |
| 34 | Suspected Fraud, Retain Card | 2014 | Processor Declined – Fraud Suspected |
| 35 | Card Acceptor, Contact Acquirer, Retain Card | 2047 | Call Issuer. Pick Up Card |
| 36 | Restricted Card, Retain Card | 2047 | Call Issuer. Pick Up Card |
| 37 | Contact Acquirer Security Department, Retain Card | 2047 | Call Issuer. Pick Up Card |
| 38 | PIN Tries Exceeded, Capture | 2103 | PIN try exceeded |
| 39 | No Credit Account | 2050 | Invalid Credit Plan |
| 40 | Function Not Supported | 2019 | Invalid Transaction |
| 41 | Lost Card | 2012 | Processor Declined – Possible Lost Card |
| 42 | No Universal Account | 2019 | Invalid Transaction |
| 43 | Stolen Card | 2013 | Processor Declined – Possible Stolen Card |
| 44 | No Investment Account | 2019 | Invalid Transaction |
| 51 | Insufficient Funds | 2001 | Insufficient Funds |
| 52 | No Cheque Account | 2007 | No Account |
| 53 | No Savings Account | 2007 | No Account |
| 54 | Expired Card | 2004 | Expired Card |
| 55 | Incorrect PIN | 2102 | Incorrect PIN |
| 56 | No Card Record | 2007 | No Account |
| 57 | Function Not Permitted to Cardholder | 2019 | Invalid Transaction |
| 58 | Function Not Permitted to Terminal | 2019 | Invalid Transaction |
| 59 | Suspected Fraud | 2014 | Processor Declined – Fraud Suspected |
| 60 | Acceptor Contact Acquirer | 2019 | Invalid Transaction |
| 61 | Exceeds Withdrawal Limit | 2002 | Limit Exceeded |
| 62 | Restricted Card | 2057 | Issuer or Cardholder has put a restriction on the card |
| 63 | Security Violation | 2021 | Security Violation |
| 64 | Original Amount Incorrect | 2048 | Invalid Amount |
| 66 | Acceptor Contact Acquirer, Security | 2021 | Security Violation |
| 67 | Capture Card | 2014 | Processor Declined – Fraud Suspected |
| 75 | PIN Tries Exceeded | 2103 | PIN try exceeded |
| 82 | CVV Validation Error | 2010 | Card Issuer Declined CVV |
| 90 | Cutoff In Progress | 2104 | Offline Issuer Declined |
| 91 | Card Issuer Unavailable | 2104 | Offline Issuer Declined |
| 92 | Unable To Route Transaction | 2105 | Processor Declined |
| 93 | Cannot Complete, Violation Of The Law | 2020 | Violation |
| 94 | Duplicate Transaction | 2016 | Duplicate Transaction |
| 96 | System Error | 2034 | No Action Taken |
| RF1 | Invalid Refund | 2019 | Invalid Transaction |
| RF2 | Transaction ID must be unique | 2019 | Invalid Transaction |


## Testing

Braintree provides a set of [test card numbers](https://developer.paypal.com/braintree/docs/reference/general/testing#credit-card-numbers/) for sandbox testing. With the Flutterwave integration, certain Braintree test card numbers are automatically remapped to Flutterwave test card numbers to support end-to-end sandbox testing. In production, Braintree sends card numbers to Flutterwave directly (without modification).

Flutterwave test card behavior is controlled by**the expiration month and year that you provide**, not just the card number. Use the data in the following tables to trigger specific outcomes.Because card numbers are remapped in the sandbox environment to facilitate end-to-end testing, you might find discrepancies in the corresponding reporting.
### Test card mappings

| Card brand | Braintree test number | Flutterwave test number | Automatically mapped? |
| --- | --- | --- | --- |
| Visa (decline) | 4000111111111115 | 4012000033330026 | ✅ |
| Mastercard (decline) | 5105105105105100 | 5111111111111118 | ✅ |
| Mastercard (approve) | 5555555555554444 | 5111111111111118 | ✅ |
| Visa (approve) | 4012888888881881 | 4012000033330026 | ✅ |


### Expiration date-controlled outcomes

The expiration date you provide determines the outcome from Flutterwave for mapped test cards. Use the combinations that are in the following tables when you test your integration in the sandbox environment.


#### Mastercard (5105105105105100 → 5111111111111118)

| Expiry month | Expiry year | Flutterwave response |
| --- | --- | --- |
| 01 | 2039 | APPROVED |
| 05 | 2039 | DECLINED (Do Not Honor) |
| 04 | 2027 | EXPIRED_CARD |
| 08 | 2028 | TIMED_OUT |
| 01 | 2037 | ACQUIRER_SYSTEM_ERROR |
| 02 | 2037 | UNSPECIFIED_FAILURE |
| 05 | 2037 | UNKNOWN |


#### Visa (4000111111111115 → 4012000033330026)

| Expiry month | Expiry year | Flutterwave response |
| --- | --- | --- |
| 01 | 2039 | APPROVED |
| 05 | 2039 | DECLINED (Do Not Honor) |
| 04 | 2027 | EXPIRED_CARD |
| 08 | 2028 | TIMED_OUT |
| 01 | 2037 | ACQUIRER_SYSTEM_ERROR |
| 02 | 2037 | UNSPECIFIED_FAILURE |
| 05 | 2037 | UNKNOWN |


## Known limitations

Review the following known behaviors and limitations before processing transactions through Flutterwave.


- **Duplicate transaction reference handling:**If Flutterwave returnsINVALID_REQUESTwith a message about "Merchant Transaction Reference must be set to a unique value," the error is treated as retryable (SETTLING). This can occur during the propagation delay between when a Flutterwave merchant account is provisioned and when it is fully active.
- **CVV not sent for recurring or vaulted transactions:**When a vaulted card is used for a subsequent transaction (for example, a subscription renewal), the CVV is not available. The connector sends an empty string.
- **No 3DS, network token, or AVS support:**This integration does not support 3DS data pass-through, network tokens (Braintree-managed or bring-your-own), or AVS response fields. If your use case requires any of these, contact your TAM to discuss alternative integration options.


## Supported currencies

The Flutterwave connector supports the following currencies: GBP, CAD, XAF, CLP, COP, EGP, EUR, GHS, GNF, KES, MWK, MAD, NGN, RWF, SLL, STD, ZAR, TZS, UGX, USD, XOF, ZMW.


## Related content

The following resources provide additional information about the Flutterwave integration and Braintree platform:


- [Flutterwave API documentation (Postman collection)](https://documenter.getpostman.com/view/9228909/UVXqDsES#3af17261-3785-412b-9b13-bd4766f9d284/)
- [Braintree testing guide](https://developer.paypal.com/braintree/docs/reference/general/testing/)
- [Braintree transaction guide (SDK)](https://developer.paypal.com/braintree/docs/guides/transactions/)
- [Braintree transaction guide (GraphQL)](https://developer.paypal.com/braintree/graphql/guides/transactions/)
- [Braintree GraphQL API reference](https://developer.paypal.com/braintree/graphql/reference/)
- [Braintree AVS or CVV response codes](https://developer.paypal.com/braintree/docs/reference/general/processor-responses/avs-cvv-responses#cvv)

