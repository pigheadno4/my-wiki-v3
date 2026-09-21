<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/graphql-error-handling -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: GraphQL Error Handling
slug: /in-person/guides/graphql-error-handling/
createTime: '2024-11-20T19:03:17.274Z'
updateTime: '2024-11-20T19:03:17.605Z'
---



# GraphQL Error Handling

A response from the GraphQL API will always return with HTTP status 200. The JSON body of the response explains whether an error occurred. Because you can send multiple queries and mutations in a single request, and because GraphQL includes the concept of a "partial success", the request may contain a mix of data and error messages. The body is always a JSON object and MAY include any of the three top-level keys: data, errors, and extensions.


#### Data

A successful query MUST return a JSON object with a data key whose value is a JSON object with the data you requested. Each key in the data object will exactly match those specified in the query.


#### Errors

Unlike a conventional REST API, GraphQL APIs do not rely on HTTP status codes to signal request outcomes. Our GraphQL API always return a JSON body with the 200 status code, even when there are errors.

If an error occurred, the response body MUST include a top-level errors array that describes the error or errors. For example, the response for requesting a charge on a reader with an invalid readerId.

{ "data": { "requestChargeFromInStoreReader": null }, "errors": [ { "message": "Reader not found.", "extensions": { "legacyCode": "96704", } }], "extensions": { "requestId": "a-uuid-for-the-request" } }Each element in the **errors** array will have the following elements:


- message : The human-readable error message. This value is not intended to be parsed and may change at any time.


- extensions : Additional information about the error including...


- legacyCode : A unique code identifying the error, which can be used to look up a detail description in Table 1 - Error Code Explanations below.






#### Extensions

The API response MUST contain an extensions object. This object contains at least a requestId entry that is unique to the request and useful to Braintree Support should you need help debugging a request.


#### Point of Sale Logging

It is always recommended that the POS application parse and store the requestId, transactionId, and the API request and response for logging purposes. These data elements will be useful if anything goes wrong and if [troubleshooting](/braintree/in-person/post-launch-activities/contact-us/#for-software-api-integration-issues) is necessary. Our support teams can use this data to pull backend logs from the Braintree platform or to generally diagnose what may be causing an issue within your integration environment.


## Table 1 - Error Code Explanations

| **Code** | **Text** | **Explanation** |
| 96702 | Not authorized. | User is not authorized to perform this action. |
| 96703 | Reader offline. | The reader is offline. Ensure the reader is connected to a Wi-Fi network with access to the public internet. |
| 96704 | Reader not found. | A Reader with this ID was not found. Ensure the request includes the full readerId returned when calling pairInStoreReader mutation. Also ensure credentials for the same account used when pairing are used on the current request. |
| 96706 | Context in progress. | The reader is currently processing a different context with a status of PENDING or PROCESSING. |
| 96708 | Context not found. | A context with this ID was not found. |
| 96709 | Location not found. | A location with this ID was not found. |
| 96710 | OwnerId not present on request. | Request cannot be completed without providing OwnerId. |
| 96711 | User code expired. | The user code has expired. Try again using the current user code displayed on the reader. |
| 96712 | User code not found. | A user code with this ID was not found. |
| 96714 | Invalid Amount. | The amount is invalid. |
| 96715 | **Text will vary according to invalid field placement | Request cannot be completed due to an invalid field. |
| 96716 | The Context state change is invalid. | Context is in a "PROCESSING" or "COMPLETE" state, and cannot be cancelled. |
| 96717 | Duplicate store id. | Duplicate Internal name is not allowed during create/update location. |
| 96718 | Missing PayPal Payer id for qr-code enabled location. | QR code cannot be enabled if payer ID isn't provided. |
| 96722 | Invalid Payer ID. | Location cannot be created/updated due to invalid PayPal Payer ID. |
| 96723 | Error creating location. Please check input. | Location cannot be created/updated due to an invalid field. |
| 96724 | Payer ID cannot be changed. | it is not allowed to change Payer ID during updateLocation mutation. |
| 96725 | Internal name has to be unique. | Location cannot be updated due to a location with the same internal name. |
| 96726 | Invalid number of items. | The number of items requested has exceeded the first limit or is non-positive. |
| 96727 | Invalid cursor. | The supplied value of after for pagination is invalid. |
| 96728 | Error with location coordinates. Please check input. | Location cannot be created/updated due to PayPal validation error. Possible issue: there's no timezone for the given coordinates. |
| 96729 | Invalid reader parameters. | At least one of the input parameters must be populated. |
| 96730 | Invalid configuration parameters. | At least one of the input parameters must be populated. |
| 96731 | Configuration not found. | An associated configuration was not found. |
| 96733 | The printer is currently busy. Please retry. | The printer is currently busy. Please try your print request again later. |
| 96734 | The printer is out of paper or the head is open. | The reader printer is out of paper or the head of the reader is open. Please check and resend the print request. |
| 96735 | The battery of the reader is too low to support printing. | Please charge the reader and try again. |
| 96736 | Printing is not supported by this reader. | Printing is only supported on the V400M reader model. This request is not supported on this reader. |
| 96737 | The message exceeds the maximum allowed size. Please reduce the message length and try again. | The requested message is too long. Please reduce it and resend the print request. |


## Processor Response Codes

Braintree will also return raw processor response codes in the API response. You may want to parse and consume these detailed [processor response](/braintree/articles/control-panel/transactions/declines#additional-processor-responses) codes to provide detailed reason codes to your cashier or accounting team.


**NOTE**
Click on the link above. Try passing the number listed in the "code" column as the "amount in your request. This will simulate that processor response.

[Card Data Collections](/braintree/in-person/guides/card-data-collection/)[Offline Transactions](/braintree/in-person/guides/offline-transactions/)