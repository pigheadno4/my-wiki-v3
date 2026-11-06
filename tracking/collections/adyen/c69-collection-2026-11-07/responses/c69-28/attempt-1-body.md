# GET /transactions/{id} - Get a transaction

Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.

Returns a transaction.

## Servers
- https://balanceplatform-api-test.adyen.com/btl/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the transaction. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolder | object | Yes | Contains information about the account holder associated with the `balanceAccount`. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
| amount | object | Yes | Contains information about the amount of the transaction. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| balanceAccount | object | Yes | Contains information about the balance account involved in the transaction. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
| balancePlatform | string | Yes | The unique identifier of the balance platform. |
| bookingDate | string | Yes | The date the transaction was booked into the balance account. |
| creationDate | string | No | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2025-03-19T10:15:30+01:00**. |
| description | string | No | The `description` from the `/transfers` request. |
| id | string | Yes | The unique identifier of the transaction. |
| paymentInstrument | object | No | Contains information about the payment instrument that was used for the transaction. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
|   - tokenType | string | No | The type of wallet that the network token is associated with. |
| referenceForBeneficiary | string | No | The reference sent to or received from the counterparty.  For outgoing funds, this is the [`referenceForBeneficiary`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__resParam_referenceForBeneficiary) from the  [`/transfers`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_referenceForBeneficiary) request.  For incoming funds, this is the reference from the sender. |
| status | string | Yes | The status of the transaction.  Possible values:  **pending**: The transaction is still pending.  **booked**: The transaction has been booked to the balance account. |
| transfer | object | No | Contains information about the transfer related to the transaction. |
|   - categoryData |  | No | The relevant data according to the transfer category. |
|   - id | string | No | The ID of the resource. |
|   - reference | string | Yes | The [`reference`](https://docs.adyen.com/api-explorer/#/transfers/latest/post/transfers__reqParam_reference) from the `/transfers` request. If you haven't provided any, Adyen generates a unique reference. |
| valueDate | string | Yes | The date the transfer amount becomes available in the balance account. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |

## Response examples

### 200 Success

**success**
```json
{
  "id": "EVJN4227C224222B5JBDHPTD672M52EUR",
  "amount": {
    "value": -10000,
    "currency": "EUR"
  },
  "status": "booked",
  "transfer": {
    "id": "48TYZO5ZVURJ2FCW",
    "reference": "Your internal reference for the transfer"
  },
  "valueDate": "2023-08-11T16:19:35+02:00",
  "bookingDate": "2023-08-11T16:19:39+02:00",
  "creationDate": "2023-08-11T16:19:35+02:00",
  "accountHolder": {
    "id": "AH00000000000000000000001",
    "description": "Your description of the account holder"
  },
  "balanceAccount": {
    "id": "BA00000000000000000000001",
    "description": "Your description of the balance account"
  },
  "balancePlatform": "YOUR_BALANCE_PLATFORM"
}
```