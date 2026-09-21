<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/refund-authorizations -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Refund Authorizations
slug: /articles/guides/refund-authorizations/
createTime: '2025-04-02T00:22:27.064Z'
updateTime: '2025-10-01T10:45:50.081Z'
---



# Refund Authorizations


**NOTE**
 
- This functionality is currently available for all merchants in the US and selected merchants in Australia.
- Authorization and capture can incur merchant fees in some markets. For more information, see your[Braintree User Agreement](https://www.braintreepayments.com/legal).

 

The payments industry is moving to an authorization model for refund processing. As per scheme rules, refunds should be preceded by authorizations to allow the card issuer to weigh in before you send a refund to a cardholder. Refund authorizations will also appear on cardholder statements in real time, to improve transparency.


## Card networks affected


- Visa
- Discover
- Mastercard
- Amex


## Payment methods affected


- Credit cards
- Apple Pay
- Google Pay


## Statuses of refund authorizations


### Approved refunds

If a refund authorization is approved, the issuer has indicated, in real time, that they will accept the refund and deposit it into the cardholder’s account.


### Declined refunds

If the refund authorization is declined, the issuer has indicated, in real time, that the cardholder’s account is not capable of accepting the refund. A refund decline prevents the cardholder’s payment method from being refunded.

Common reasons for declines:


- Card account is closed
- Card account is frozen due to fraud
- Card account does not support refunds (e.g. some prepaid cards)



**NOTE**
Certain declined refund authorization transactions, depending on the network response code, may be force-captured due to high issuer decline rates.



## Background

Refund authorizations are intended to help solve two industry challenges:


### Cardholder transparency for refunds

Refunds do not immediately appear on cardholder statements, which can cause cardholder confusion and frustration. This confusion can lead to increased refund-related customer support inquiries.


### Refund resolution timeliness

Issuers are not required to accept refunds. However, without an authorization framework, it can take days for you to be notified after an issuer rejects a refund. Refund delays can increase the likelihood of cardholder disputes.


## Benefits

With the introduction of refund authorizations, cardholders can see the following benefits:


### Improved cardholder transparency

If a refund authorization is approved by the issuer, the issuer should immediately add a pending refund line item to the cardholder’s statement. This pending line item provides real time evidence to the cardholder that you’ve initiated the refund process. This transparency is expected to reduce refund-related customer support inquiries.


### Real time refund approval responses

If the cardholder’s account cannot accept the refund, the issuer will decline the refund authorization in real time. This real time response allows you to take immediate action if the refund is declined, such as requesting an alternate payment method in order to reattempt their refund. This allows you to be more proactive in resolving refund-related issues, which should reduce refund-related inquiries.


### Reduction in refund-related disputes

By being more proactive, you can increase the timeliness of refund resolutions, which should reduce disputes from cardholders anxious for their refunds.


## How to handle refund declines

You should first attempt to refund the original sale transaction via Braintree’s [refund API](/braintree/docs/reference/request/transaction/refund) or in the [Control Panel](/braintree/articles/control-panel/transactions/refunds-voids-credits#issuing-a-refund-within-the-control-panel). If the refund authorization attempt is declined by the issuer, you may refund your customer via an alternate method instead.


### Common alternate refund methods


- Cash
- Check
- In-store credit
- Prepaid card


### Refund policies

It’s important to note that your refund/return policy still allows you to restrict or refuse refunds, returns, cancellations, or exchanges, provided that your policy outlines this clearly and was properly disclosed to your customer during the original sale transaction.


## Integration changes


### Current refund workflow

Braintree’s refund API assumes success for credit card, Apple Pay, and Google Pay-based refunds. This means that refund responses indicate the success of the API request itself, but not the overall outcome of the refund. After receiving a refund success response, it’s still possible for the issuer to reject the refund.


### Future refund workflow

Once the refund authorization framework is released by Braintree by card network and region, [refund requests](/braintree/docs/reference/request/transaction/refund/all) will return real time [processor responses](/braintree/docs/reference/general/processor-responses/authorization-responses), similar to the processor responses returned from sale authorizations. In order to properly support this enhanced refund functionality, you will be required to update your integration to recognize refund processor responses.


## API Updates and Sandbox Testing


### Technical changes

To reduce integration friction, Braintree will introduce two refund decline workflows. The workflow that you experience will depend on the SDK version your integration uses to connect to Braintree: new SDK versions or previous SDK versions.


### New SDK versions


- Ruby 3.0 or newer
- Python 4.0 or newer
- Java 3.0.0 or newer
- Node.js 3.0.0 or newer
- PHP 5.0.0 or newer
- .NET 5.0.0 or newer

If your integration uses one of these new SDK versions, and the processor declines a refund, the response will have the processor response code available. The processor response code will pull from the existing pool of [2000-class decline codes](/braintree/docs/reference/general/processor-responses/authorization-responses#declines), allowing you to determine the cause of the decline in real time. Common refund decline codes include:


- **2004 - Expired Card**
- **2005 - Invalid Card Number**
- **2014 - Fraud Suspected**
- **2047 - Pick Up Card**


**NOTE**
 GraphQL users will receive processor response codes for all refund declines.

 


### Previous SDK versions

If your integration uses an SDK version older than those listed above, and the processor declines a refund, you will receive one of the following two [validation errors](/braintree/docs/reference/general/validation-errors/all#code-915200) in lieu of a processor response code:


- **Hard decline: 915200**- Failed to refund transaction.
- **Soft decline: 915201**- Failed to refund transaction. Please try again at a later time.


## Sandbox testing

These changes are currently available in the [Braintree sandbox](/braintree/docs/reference/general/testing). We recommend testing refund declines so that you can prepare for the upcoming launch of refund authorizations.

In order to simulate a refund decline in sandbox, follow these steps:


- Simulate a successful sale using an amount between $3001.00-4000.99
- Submit the sale for settlement; once the transaction updates to aSettledorSettlingstatus, it is eligible for a refund
- Specify the sale’s transaction ID in a refund request
- In order to simulate a refund decline, specify a refund amount between $2000-2999.99
- The amount specified will determine the decline code: for example, submitting a refund for $2004.00 will generate a decline response of**2004 - Expired Card**if using a current SDK version



