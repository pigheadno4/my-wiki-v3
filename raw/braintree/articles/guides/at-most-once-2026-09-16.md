<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/at-most-once -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: At-Most-Once
slug: /articles/guides/at-most-once/
createTime: '2025-04-01T23:29:43.396Z'
updateTime: '2025-04-01T23:29:43.451Z'
---



**NOTE**
 This page is limited to a select group of individuals or a specific audience and is not yet available to the general public. Please get in touch with the product team before sharing this link.

 


## At-Most-Once Processing

At-Most-Once Processing or Idempotency processing helps merchants ensure that duplicate API requests do not result in duplicate actions such as charging or refunding a payment multiple times. In contrast to transaction duplicate checking, this feature requires merchants to specify a unique request key, and the two features are mutually exclusive.

There are two primary categories of idempotency features:


- Network: a given request returns the same response, including network errors
- Logical Intent: a given request will run without causing incompatible, duplicative actions

Instead of network-level idempotency, Braintree has chosen to implement logical intent idempotency or, to avoid confusion, At-Most-Once Processing. This feature ensures that duplicate API requests do not result in duplicate actions, such as charging or refunding a payment multiple times. Duplicate requests do not reach payment networks and avoid overcharging merchants. Each identical request within a 30-day window will return the current state of that request's intent. This avoids unintended duplication and can safely retry requests when unexpected errors occur, for example, networking failures.


## Details

At-Most-Once processing requires the merchant to provide an ApiRequestKey with each request to identify the logical action being attempted uniquely. Identical ApiRequestKey values within a 30-day window are considered duplicate requests.

When duplicate requests are encountered, the following are possible outcomes:


- If other request details, such as amount, customer, or payment method, are the same as the original request, and the original request is still in progress, the gateway returns a retryable validation error.
- If other request details, such as amount, customer, or payment method, are the same as the original request, and the original request has been completed, the current state of that action's result is returned. For example, a Charge request will return a transaction record, but the state may now be Settled instead of Settling (as well as error states such as Declined).
- If other request details, such as amount, customer, or payment method, are not the same as the original request, the gateway returns a validation error.


## Supported Actions

Currently, we support following actions


- Authorize
- Charge
- Submit For Partial Capture
- Submit For Settlement
- Credit
- Refund
- Reverse


### Authorize

* authorizePaymentMethod * authorizePayPalAccount * authorizeVenmoAccount * authorizeCreditCard * authorizeInStoreCreditCard
##### Authorization (2-step) Scenarios (Excludes all capture scenarios)

| Scenario | Request Key | Request Params | Transaction stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | New Transaction object |  |
| 2 | Dupe | Unchanged | Yes | Concurrent | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | Yes | &lt; 30 days | 200 or 201 | Original Transaction object in current state (that state may not be successful) |  |
| 4 * | Dupe | Unchanged | No | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915234 | Generate new ApiRequestKey ; see footnote |
| 5 ** | Dupe | Changed | Maybe | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | N/A | &gt; 30 days | 200 or 201 | New Transaction object |  |

* **Footnote for use case (4)**: Unlike capture scenarios (where a transaction record is already present), validation error 915234 on an auth can only be returned when no transaction record was stored. Because transaction records are durably persisted prior to attempting authorization with payment networks, the absence of a transaction record means reattempting the request cannot result in multiple authorizations.   * **Footnote for use case (5)**: When receiving a validation error code 915232, it is the merchant’s responsibility to determine if generating a newApiRequestKeyand sending changed request parameters would result in a functional duplicate charge. Specifically, the merchant should understand why the parameters have changed. A few overlapping scenarios are possible:


- The original request


- Could have been successful, resulting in an authorization.
- Could have been unsuccessful, with no pending authorization.


- The changed parameters


- Could be correct, with theApiRequestKeybeing erroneously duplicative. For example, if the merchant has a bug in generatingApiRequestKeyvalues
- Could be incorrect, with theApiRequestKeybeing correct. For example, if the merchant had a bug that incorrectly mutated the parameters If a transaction record was created (whether or not the authorization was successful) the error response will contain an additional field with that transaction’s public identifier.


### Charge

* chargePaymentMethod * chargeUsBankAccount * chargePayPalAccount * chargeVenmoAccount * chargeCreditCard * chargeInStoreCreditCard
##### Charge (1-step) Scenarios

| Scenario | Request Key | Request Params | Transaction stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | New Transaction object |  |
| 2 | Dupe | Unchanged | Yes | Concurrent | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | Yes | &lt; 30 days | 200 or 201 | Original Transaction object in current state (that state may not be successful) |  |
| 4 * | Dupe | Unchanged | No | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915234 | Generate new ApiRequestKey ; see footnote |
| 5 ** | Dupe | Changed | Maybe | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | N/A | &gt; 30 days | 200 or 201 | New Transaction object |  |

* **Footnote for use case (4)**Multiple scenarios may lead to this outcome. If no transaction record was created, then retrying with a newApiRequestKeymay be safely attempted. If a transaction record was created the error response will contain an additional key with the transaction's public identifier, and further investigation (and potentially intervention by Braintree) is required.

* **Footnote for use case (5)**Similarly to the footnote for the use case (5) for authorization scenarios, the merchant must understand why their integration has either reused anApiRequestKeyor generated different request parameters. The error response will contain an additional key with the transaction's public identifier from the original request.


## Refund

* refundTransaction| Scenario | Request Key | Request Params | Transaction stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | New Transaction object |  |
| 2 | Dupe | Unchanged | Yes | Concurrent | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | Yes | &lt;30 days | 200 or 201 | Original Transaction object in current state (that state may not be successful) |  |
| 4 * | Dupe | Unchanged | No | &lt;30 days | 422 | [Validation Error](#Error-codes) 915234 | Generate new ApiRequestKey ; see footnote |
| 5 ** | Dupe | Changed | Maybe | &lt;30 days | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | N/A | &gt;30 days | undefined: depends on processor | undefined: depends on processor |  |

* **Footnote for use case (4)**Multiple scenarios may lead to this outcome. If the original transaction doesn't have a newly associated refund record retrying with a newApiRequestKeymay be safely attempted. Otherwise, further investigation (and potentially intervention by Braintree) is required.

* **Footnote for use case (5)**Similarly to the footnote for the use case (5) for authorization scenarios, the merchant must understand why their integration has either reused anApiRequestKeyor generated different request parameters. The error response will contain an additional key with the transaction's public identifier from the original request.


## Submit For Settlement

* captureTransaction
##### Capture Scenarios (Excludes all authorization scenarios)

| Scenario | Request Key | Request Params | Time since original capture request | Initial Capture Request Succeeded | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | Updated Transaction object |  |
| 2 | Dupe | Unchanged | Concurrent | N/A | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | &lt; 30 days | Yes | 200 or 201 | Transaction object in the current state |  |
| 4 * | Dupe | Unchanged | &lt; 30 days | No | 422 | [Validation Error](#Error-codes) 915234 | See footnote |
| 5 ** | Dupe | Changed | &lt; 30 days | Maybe | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | &gt; 30 days | N/A | 200 or 201 | Updated Transaction object |  |

* **Footnote for use case (4)**Multiple scenarios may lead to this outcome. If the transaction status is still Authorized, retrying with a newApiRequestKeymay be safely attempted. Otherwise, further investigation (and potentially intervention by Braintree) is required.

* **Footnote for use case (5)**Similarly to the footnote for the use case (5) for authorization scenarios, the merchant must understand why their integration has either reused anApiRequestKeyor generated different request parameters. The error response will contain an additional key with the transaction's public identifier from the original request.


## Submit For Partial Settlement

* partialCaptureTransaction| Scenario | Request Key | Request Params | Partial capture transaction stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | Partial capture transaction object |  |
| 2 | Dupe | Unchanged | Yes | Concurrent | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | Yes | &lt; 30 days | 200 or 201 | Partial capture transaction object in current state (that state may not be successful) |  |
| 4 * | Dupe | Unchanged | No | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915234 | Generate new ApiRequestKey ; see footnote |
| 5 ** | Dupe | Changed | Maybe | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | N/A | &gt; 30 days | 200 or 201 | Partial capture transaction object |  |

*_ **Footnote for use case (4)** Multiple scenarios may lead to this outcome. Because this request stores a new partial capture transaction record before attempting capture with payment networks, the absence of a partial capture transaction record means that it is safe to retry the request.

* **Footnote for use case (5)**Similarly to the footnote for the use case (5) for authorization scenarios, the merchant must understand why their integration has either reused anApiRequestKeyor generated different request parameters. If a partial capture transaction record was created by an earlier request the error response will contain an additional key with the partial capture transaction's public identifier.


## Credit

* refundCreditCard
* refundInStoreCreditCard
* refundUsBankAccount| Scenario | Request Key | Request Params | Refund stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | N/A | N/A | 200 or 201 | New Refund transaction object |  |
| 2 | Dupe | Unchanged | Yes | Concurrent | 422 | [Validation Error](#Error-codes) 915233 |  |
| 3 | Dupe | Unchanged | Yes | &lt; 30 days | 200 or 201 | Original Refund transaction object in current state (that state may not be successful) |  |
| 4 * | Dupe | Unchanged | No | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915234 | Generate new ApiRequestKey ; see footnote |
| 5 ** | Dupe | Changed | Maybe | &lt; 30 days | 422 | [Validation Error](#Error-codes) 915232 | See footnote |
| 6 | Dupe | Unchanged | N/A | &gt; 30 days | 200 or 201 | New Refund transaction object |  |


## Reverse

* reverseTransaction
* reverseEmvTransaction
* reverseRefund| Scenario | Request Key | Request Params | Voidable transaction * | Transaction stored w/ 1st request? | Time since original request | Legacy API HTTP code | Outcome and response format | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | New | Original | Yes | N/A | N/A | 200 or 201 | Updated transaction object |  |
| 2 | New | Original | No | N/A | N/A | 200 or 201 | New refund transaction object |  |
| 3 | Dupe | Unchanged | Yes | No | Concurrent | 422 | [Validation Error](##Error-codes) 915233 | Retry later |
| 4 | Dupe | Unchanged | No | Yes | Concurrent | 422 | [Validation Error](##Error-codes) 915233 | Retry Later |
| 5 | Dupe | Unchanged | Yes | No | &lt; 30 days | 200 or 201 | Original transaction object in current state |  |
| 6 | Dupe | Unchanged | No | Yes | &lt; 30 days | 200 or 201 | Refund transaction object in current state (that state may not be successful) |  |
| 7 ** | Dupe | Unchanged | No | No | &lt; 30 days | 422 | [Validation Error](##Error-codes) 915234 | Generate new ApiRequestKey; see footnote |
| 8 *** | Dupe | Changed | Yes | No | &lt; 30 days | 422 | [Validation Error](##Error-codes) 915232 | See footnote |
| 9 | Dupe | Changed | No | Maybe | &lt; 30 days | 422 | [Validation Error](##Error-codes) 915232 | See footnote |
| 10 | Dupe | Unchanged | Yes | N/A | &gt; 30 days | Undefined: depends on processor | Undefined: depends on processor | Undefined: depends on processor |
| 11 | Dupe | Unchanged | No | N/A | &gt; 30 days | Undefined: depends on processor | Undefined: depends on processor | Undefined: depends on processor |

* **Transactions are voidable if their status isauthorizedorsubmitted_for_settlement. * **Footnote for use case (7)** Multiple scenarios may lead to this outcome. If the original transaction doesn't have a newly associated refund record retrying with a new ApiRequestKey may be safely attempted. Otherwise, further investigation (and potentially intervention by Braintree) is required._

* **Footnote for use case (8)**Similarly to the footnote for the use case (5) for authorization scenarios, the merchant must understand why their integration has either reused an ApiRequestKey or generated different request parameters. The error response will contain an additional key with the transaction's public identifier from the original request.


## Error Codes

| Error Code | Error Message |
| --- | --- |
| 915232 | An ApiRequestKey may only be reused with parameters identical to the original request. |
| 915233 | A previous request with this ApiRequestKey is still in-flight. |
| 915234 | A previous request with this ApiRequestKey failed and cannot be retried. |

