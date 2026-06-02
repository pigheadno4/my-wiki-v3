<!-- Source URL: https://docs.paypal.ai/growth/disputes/reference/test-values -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Disputes API - test values for simulations

Developers and QA engineers can use these predefined test values to simulate negative Disputes API responses in a sandbox while they develop and test their integration.

<Note>Test values are case-sensitive.</Note>

## Prerequisites

- Access to the Disputes API sandbox.
- Valid API credentials and authentication set up.
- An HTTP client (for example, cURL, Postman, or your application).

For more information, see [Set up accounts and environment](/business/payments/disputes/set-up).

## Simulate negative responses

1. Pick the Disputes API operation and the error you want to test.
2. Find the matching test value in the tables below and send a request that uses it in the path or query parameter.
3. Confirm that the response and your integration’s behavior match the simulated error described in the table.

## List disputes

Use the query parameter in the request URL to simulate the negative responses.

**Endpoint**: `GET /v1/customer/disputes?disputed_transaction_id={TRANSACTION-ID}`

| Query parameter                                           | Simulated error response                                   |
| --------------------------------------------------------- | ---------------------------------------------------------- |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS023` | `FORBIDDEN`                                                |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS024` | `INVALID_RESOURCE_ID`                                      |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS025` | `NOT_ACCEPTABLE`                                           |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS026` | `UNSUPPORTED_MEDIA_TYPE`                                   |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS027` | `RATE_LIMIT_REACHED`                                       |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS028` | `SERVICE_UNAVAILABLE`                                      |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS029` | `INTERNAL_SERVICE_ERROR`                                   |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS030` | `AUTHORIZATION_ERROR`                                      |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS031` | `VALIDATION_ERROR`<br />(issue: DATE_CAN_NOT_BE_IN_FUTURE) |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS032` | `VALIDATION_ERROR`<br />(issue: INVALID_PAGE_SIZE)         |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS033` | `VALIDATION_ERROR`<br />(issue: INVALID_START_TIME_FORMAT) |
| `/v1/customer/disputes?disputed_transaction_id=ERRDIS034` | `VALIDATION_ERROR`<br />(issue: INVALID_START_TIME_RANGE)  |

## Show dispute details

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `GET /v1/customer/disputes/{ID}`

| Path parameter                    | Simulated error response |
| --------------------------------- | ------------------------ |
| `/v1/customer/disputes/ERRDIS015` | `FORBIDDEN`              |
| `/v1/customer/disputes/ERRDIS016` | `INVALID_RESOURCE_ID`    |
| `/v1/customer/disputes/ERRDIS017` | `NOT_ACCEPTABLE`         |
| `/v1/customer/disputes/ERRDIS018` | `UNSUPPORTED_MEDIA_TYPE` |
| `/v1/customer/disputes/ERRDIS019` | `RATE_LIMIT_REACHED`     |
| `/v1/customer/disputes/ERRDIS020` | `SERVICE_UNAVAILABLE`    |
| `/v1/customer/disputes/ERRDIS021` | `INTERNAL_SERVICE_ERROR` |
| `/v1/customer/disputes/ERRDIS022` | `AUTHORIZATION_ERROR`    |

## Send message to other party

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/send-message`

| Path parameter                                 | Simulated error response |
| ---------------------------------------------- | ------------------------ |
| `/v1/customer/disputes/ERRDIS091/send-message` | `FORBIDDEN`              |
| `/v1/customer/disputes/ERRDIS092/send-message` | `INVALID_RESOURCE_ID`    |
| `/v1/customer/disputes/ERRDIS093/send-message` | `NOT_ACCEPTABLE`         |
| `/v1/customer/disputes/ERRDIS094/send-message` | `UNSUPPORTED_MEDIA_TYPE` |
| `/v1/customer/disputes/ERRDIS095/send-message` | `RATE_LIMIT_REACHED`     |
| `/v1/customer/disputes/ERRDIS096/send-message` | `SERVICE_UNAVAILABLE`    |
| `/v1/customer/disputes/ERRDIS097/send-message` | `INTERNAL_SERVICE_ERROR` |
| `/v1/customer/disputes/ERRDIS098/send-message` | `AUTHORIZATION_ERROR`    |
| `/v1/customer/disputes/ERRDIS099/send-message` | `UNPROCESSABLE_ENTITY`   |

## Make offer to resolve dispute

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/make-offer`

| Path parameter                               | Simulated error response |
| -------------------------------------------- | ------------------------ |
| `/v1/customer/disputes/ERRDIS100/make-offer` | `FORBIDDEN`              |
| `/v1/customer/disputes/ERRDIS101/make-offer` | `INVALID_RESOURCE_ID`    |
| `/v1/customer/disputes/ERRDIS102/make-offer` | `NOT_ACCEPTABLE`         |
| `/v1/customer/disputes/ERRDIS103/make-offer` | `UNSUPPORTED_MEDIA_TYPE` |
| `/v1/customer/disputes/ERRDIS104/make-offer` | `RATE_LIMIT_REACHED`     |
| `/v1/customer/disputes/ERRDIS105/make-offer` | `SERVICE_UNAVAILABLE`    |
| `/v1/customer/disputes/ERRDIS106/make-offer` | `INTERNAL_SERVICE_ERROR` |
| `/v1/customer/disputes/ERRDIS107/make-offer` | `AUTHORIZATION_ERROR`    |
| `/v1/customer/disputes/ERRDIS108/make-offer` | `UNPROCESSABLE_ENTITY`   |

## Accept claim

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/accept-claim`

| Path parameter                                 | Simulated error response                                                |
| ---------------------------------------------- | ----------------------------------------------------------------------- |
| `/v1/customer/disputes/ERRDIS051/accept-claim` | `FORBIDDEN`                                                             |
| `/v1/customer/disputes/ERRDIS052/accept-claim` | `INVALID_RESOURCE_ID`                                                   |
| `/v1/customer/disputes/ERRDIS053/accept-claim` | `NOT_ACCEPTABLE`                                                        |
| `/v1/customer/disputes/ERRDIS054/accept-claim` | `UNSUPPORTED_MEDIA_TYPE`                                                |
| `/v1/customer/disputes/ERRDIS055/accept-claim` | `RATE_LIMIT_REACHED`                                                    |
| `/v1/customer/disputes/ERRDIS056/accept-claim` | `SERVICE_UNAVAILABLE`                                                   |
| `/v1/customer/disputes/ERRDIS057/accept-claim` | `INTERNAL_SERVICE_ERROR`                                                |
| `/v1/customer/disputes/ERRDIS058/accept-claim` | `AUTHORIZATION_ERROR`                                                   |
| `/v1/customer/disputes/ERRDIS059/accept-claim` | `UNPROCESSABLE_ENTITY`                                                  |
| `/v1/customer/disputes/ERRDIS060/accept-claim` | `VALIDATION_ERROR`<br />(issue: AMOUNT_SHOULD_NOT_BE_PASSED)            |
| `/v1/customer/disputes/ERRDIS061/accept-claim` | `VALIDATION_ERROR`<br />(issue: INSUFFICIENT_FUNDS)                     |
| `/v1/customer/disputes/ERRDIS062/accept-claim` | `VALIDATION_ERROR`<br />(issue: INTANGIBLE_ITEM_CANNOT_BE_RETURNED)     |
| `/v1/customer/disputes/ERRDIS063/accept-claim` | `VALIDATION_ERROR`<br />(issue: INVALID_RETURN_SHIPPING_ADDRESS_FORMAT) |
| `/v1/customer/disputes/ERRDIS064/accept-claim` | `VALIDATION_ERROR`<br />(issue: MISSING_RETURN_SHIPPING_ADDRESS)        |
| `/v1/customer/disputes/ERRDIS065/accept-claim` | `UNPROCESSABLE_ENTITY`                                                  |

## Provide evidence

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/provide-evidence`

| Path parameter                                     | Simulated error response                                                     |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| `/v1/customer/disputes/ERRDIS035/provide-evidence` | `FORBIDDEN`                                                                  |
| `/v1/customer/disputes/ERRDIS036/provide-evidence` | `INVALID_RESOURCE_ID`                                                        |
| `/v1/customer/disputes/ERRDIS037/provide-evidence` | `NOT_ACCEPTABLE`                                                             |
| `/v1/customer/disputes/ERRDIS038/provide-evidence` | `UNSUPPORTED_MEDIA_TYPE`                                                     |
| `/v1/customer/disputes/ERRDIS039/provide-evidence` | `RATE_LIMIT_REACHED`                                                         |
| `/v1/customer/disputes/ERRDIS040/provide-evidence` | `SERVICE_UNAVAILABLE`                                                        |
| `/v1/customer/disputes/ERRDIS041/provide-evidence` | `INTERNAL_SERVICE_ERROR`                                                     |
| `/v1/customer/disputes/ERRDIS042/provide-evidence` | `AUTHORIZATION_ERROR`                                                        |
| `/v1/customer/disputes/ERRDIS043/provide-evidence` | `UNPROCESSABLE_ENTITY`                                                       |
| `/v1/customer/disputes/ERRDIS044/provide-evidence` | `VALIDATION_ERROR`<br />(issue: INVALID_EVIDENCE_FILE)                       |
| `/v1/customer/disputes/ERRDIS045/provide-evidence` | `VALIDATION_ERROR`<br />(issue: INVALID_EVIDENCE_TYPE_PROOF_OF_FULFILLMENT)  |
| `/v1/customer/disputes/ERRDIS046/provide-evidence` | `VALIDATION_ERROR`<br />(issue: ITEM_ID_IS_MANDATORY_FOR_MULTIPLE_EVIDENCES) |
| `/v1/customer/disputes/ERRDIS047/provide-evidence` | `VALIDATION_ERROR`<br />(issue: MISSING_EVIDENCE_INFO)                       |
| `/v1/customer/disputes/ERRDIS048/provide-evidence` | `VALIDATION_ERROR`<br />(issue: MISSING_EVIDENCE_TYPE)                       |
| `/v1/customer/disputes/ERRDIS049/provide-evidence` | `VALIDATION_ERROR`<br />(issue: MISSING_REFUND_ID)                           |
| `/v1/customer/disputes/ERRDIS050/provide-evidence` | `VALIDATION_ERROR`<br />(issue: MISSING_TRACKING_INFO)                       |

## Escalate dispute to claim

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/escalate`

| Path parameter                             | Simulated error response |
| ------------------------------------------ | ------------------------ |
| `/v1/customer/disputes/ERRDIS082/escalate` | `FORBIDDEN`              |
| `/v1/customer/disputes/ERRDIS083/escalate` | `INVALID_RESOURCE_ID`    |
| `/v1/customer/disputes/ERRDIS084/escalate` | `NOT_ACCEPTABLE`         |
| `/v1/customer/disputes/ERRDIS085/escalate` | `UNSUPPORTED_MEDIA_TYPE` |
| `/v1/customer/disputes/ERRDIS086/escalate` | `RATE_LIMIT_REACHED`     |
| `/v1/customer/disputes/ERRDIS087/escalate` | `SERVICE_UNAVAILABLE`    |
| `/v1/customer/disputes/ERRDIS088/escalate` | `INTERNAL_SERVICE_ERROR` |
| `/v1/customer/disputes/ERRDIS089/escalate` | `AUTHORIZATION_ERROR`    |
| `/v1/customer/disputes/ERRDIS090/escalate` | `UNPROCESSABLE_ENTITY`   |

## Appeal dispute

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/appeal`

| Path parameter                           | Simulated error response                                                     |
| ---------------------------------------- | ---------------------------------------------------------------------------- |
| `/v1/customer/disputes/ERRDIS066/appeal` | `FORBIDDEN`                                                                  |
| `/v1/customer/disputes/ERRDIS067/appeal` | `INVALID_RESOURCE_ID`                                                        |
| `/v1/customer/disputes/ERRDIS068/appeal` | `NOT_ACCEPTABLE`                                                             |
| `/v1/customer/disputes/ERRDIS069/appeal` | `UNSUPPORTED_MEDIA_TYPE`                                                     |
| `/v1/customer/disputes/ERRDIS070/appeal` | `RATE_LIMIT_REACHED`                                                         |
| `/v1/customer/disputes/ERRDIS071/appeal` | `SERVICE_UNAVAILABLE`                                                        |
| `/v1/customer/disputes/ERRDIS072/appeal` | `INTERNAL_SERVICE_ERROR`                                                     |
| `/v1/customer/disputes/ERRDIS073/appeal` | `AUTHORIZATION_ERROR`                                                        |
| `/v1/customer/disputes/ERRDIS074/appeal` | `UNPROCESSABLE_ENTITY`                                                       |
| `/v1/customer/disputes/ERRDIS075/appeal` | `VALIDATION_ERROR`<br />(issue: INVALID_EVIDENCE_FILE)                       |
| `/v1/customer/disputes/ERRDIS076/appeal` | `VALIDATION_ERROR`<br />(issue: INVALID_EVIDENCE_TYPE_PROOF_OF_FULFILLMENT)  |
| `/v1/customer/disputes/ERRDIS077/appeal` | `VALIDATION_ERROR`<br />(issue: ITEM_ID_IS_MANDATORY_FOR_MULTIPLE_EVIDENCES) |
| `/v1/customer/disputes/ERRDIS078/appeal` | `VALIDATION_ERROR`<br />(issue: MISSING_EVIDENCE_INFO)                       |
| `/v1/customer/disputes/ERRDIS079/appeal` | `VALIDATION_ERROR`<br />(issue: MISSING_EVIDENCE_TYPE)                       |
| `/v1/customer/disputes/ERRDIS080/appeal` | `VALIDATION_ERROR`<br />(issue: MISSING_REFUND_ID)                           |
| `/v1/customer/disputes/ERRDIS081/appeal` | `VALIDATION_ERROR`<br />(issue: MISSING_TRACKING_INFO)                       |

## Acknowledge returned item

Use the test values as path parameters to simulate the negative responses.

**Endpoint**: `POST /v1/customer/disputes/{ID}/acknowledge-return-item`

| Path parameter                                            | Simulated error response |
| --------------------------------------------------------- | ------------------------ |
| `/v1/customer/disputes/ERRDIS109/acknowledge-return-item` | `FORBIDDEN`              |
| `/v1/customer/disputes/ERRDIS110/acknowledge-return-item` | `INVALID_RESOURCE_ID`    |
| `/v1/customer/disputes/ERRDIS111/acknowledge-return-item` | `NOT_ACCEPTABLE`         |
| `/v1/customer/disputes/ERRDIS112/acknowledge-return-item` | `UNSUPPORTED_MEDIA_TYPE` |
| `/v1/customer/disputes/ERRDIS113/acknowledge-return-item` | `RATE_LIMIT_REACHED`     |
| `/v1/customer/disputes/ERRDIS114/acknowledge-return-item` | `SERVICE_UNAVAILABLE`    |
| `/v1/customer/disputes/ERRDIS115/acknowledge-return-item` | `INTERNAL_SERVICE_ERROR` |
| `/v1/customer/disputes/ERRDIS116/acknowledge-return-item` | `AUTHORIZATION_ERROR`    |
| `/v1/customer/disputes/ERRDIS117/acknowledge-return-item` | `UNPROCESSABLE_ENTITY`   |

Additional information

- Use these test values in automated tests to regularly validate error handling.
- For full request and response formats, see the [Disputes API integration guide](/business/payments/disputes/handle-disputes/use-disputes-api).
- For happy‑path flows and additional examples, see the [Disputes API reference](/reference/api/rest/disputes/list-disputes).
