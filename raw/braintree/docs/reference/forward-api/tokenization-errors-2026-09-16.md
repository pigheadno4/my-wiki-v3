<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/forward-api/tokenization-errors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Tokenization Errors
slug: /docs/reference/forward-api/tokenization-errors/
createTime: '2025-04-02T00:38:44.542Z'
updateTime: '2025-11-06T20:16:23.218Z'
---



# Tokenization Errors


**AVAILABILITY**
 **Use of the production** [Forward API](/braintree/docs/reference/forward-api/overview/) is subject to eligibility. 

 Contact your Account Manager for more information or [submit an inquiry to our Business Development team](https://www.braintreepayments.com/products/braintree-extend#contact) .

Tokenization errors are returned in the response body. The body is a JSON structure with a format resembling this example:
### json
```json
{ 
    "error": "Invalid amount", 
    "message": { 
        "max_amount": "0.00" 
    }, 
    "request-uuid": "a-unique-identifier-for-the-request" 
}
```
| Error | Explanation | Message | HTTP Status Code |
| --- | --- | --- | --- |
| Cannot tokenize payment instrument | The payment instrument type does not support tokenization. | `payment_instrument_type`: the type of payment instrument | 400 |
| Card declined by issuer | Card verification failed. | None | 422 |
| Card is expired | Expired cards are unsupported. | None | 422 |
| Denied due to risk | Denied due to fraudulent behavior.Note: To prevent information disclosure, this reason should never be displayed to the customer. | None | 422 |
| Invalid amount | The specified `max_amount` was unsupported or invalid. | `max_amount`: The invalid value passed for the maximum amount | 422 |
| Invalid expire_at | The specified `expire_at` was in the past or invalid. | `expire_at`: The invalid value passed for the datetime after which the tokenized PAN should be considered invalid | 422 |
| PayPal billing agreement cancelled | The customer requested a cancellation of all future transactions on their PayPal account. Reach out to the customer for more information or an alternative payment method. | None | 422 |
| PayPal payer restriction | Either the customer's PayPal account is locked or the card has been flagged by the issuer. The customer will need to contact PayPal for more information or use an alternative payment method. | None | 422 |
| The provided payment instrument does not currently support tokenization with a cryptogram | Currently, only Visa cards are eligible for cryptograms. | None | 422 |
| Unsupported issuer | The issuer is based in an unsupported country, or does not support tokenization. | `issuer_country`: The ISO Alpha-2 country code of the issuer | 422 |
| Declined by Card Network | The request is declined by the network | Declined by Card Network | 422 |
| Ineligible by Card Network | PAN is NOT enabled for tokenization | Ineligible by Card Network | 422 |
| Network Validation Error | The network returned an input validation error for the provided request | Network Validation Error | 422 |
| Invalid Card by Card Network | The provided card is invalid and declined by the network | Invalid Card by Card Network | 422 |
| Invalid Format | The local field contains data in an invalid or unsupported format. | Invalid Format | 422 |
| Unable to Tokenize | The system was unable to tokenize the provided data. This may occur due to invalid input, unsupported data format, or an internal processing error. | Unable to Tokenize | 422 |
| Network Pan Not Enabled for Tokenization | The system was unable to tokenize the provided data. This may occur due to invalid input, unsupported data format, or an internal processing error | Network Pan Not Enabled for Tokenization | 422 |
| Invalid Token State | The requested operatation cannont be performed because the token is in an invalid or inappropriate state. This may occur if the token is expired, already used, revoked, or not yet activated. | Invalid Token State | 422 |
| Token Not Found | The specified token was not found or does not exist. This may occur if the tokeni is invalid, expired, revoked, or was never issued. | Token Not Found | 422 |
| Tokenization failed | An unhandled exception occurred. | None | 500 |




### Test credit card numbers and nonces

The following credit card numbers can be used to trigger specific unsuccessful tokenization responses in the sandbox environment.| Error | Test Value | Card Type | Corresponding Test Nonces |
| --- | --- | --- | --- |
| Card declined by issuer | `4000111111111115` | Visa | `fake-processor-declined-visa-nonce` |
|  | `5105105105105100` | Mastercard | `fake-processor-declined-mastercard-nonce` |
|  | `378734493671000` | American Express | `fake-processor-declined-amex-nonce` |
|  | `6011000990139424` | Discover | `fake-processor-declined-discover-nonce` |
|  | `3566002020360505` | JCB | `fake-processor-failure-jcb-nonce` |
| Denied due to risk | `4000111111111511` | Visa | `fake-gateway-rejected-fraud-nonce` |
| Unsupported issuer | `3530111333300000` | JCB | `fake-valid-jcb-nonce` |


### Negative testing with PayPal tokenization

Triggering a mock PayPal rejection currently leveragesmax_amountfor[parity with transaction processing](/braintree/docs/reference/general/testing#transaction-amounts).| Error | Test Value |
| --- | --- |
| PayPal billing agreement cancelled | 2070.00 |
| PayPal payer restriction | 2075.00 |

