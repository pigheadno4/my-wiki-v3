# POST /transfers/{transferId}/returns - Return a transfer

Initiates the return of previously transferred funds without creating a new `transferId`.

## Servers
- https://balanceplatform-api-test.adyen.com/btl/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| transferId | string | Yes | The unique identifier of the transfer to be returned. |


### Header parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| Idempotency-Key | string | No | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | Contains information about the amount to be returned. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| reference | string | No | Your internal reference for the return. If you don't provide this in the request, Adyen generates a unique reference. This reference is used in all communication with you about the instruction status.  We recommend using a unique value per instruction. If you need to provide multiple references for a transaction, separate them with hyphens ("-"). |

## Request examples

### transfers-return
```json
{
  "amount": {
    "value": 189,
    "currency": "EUR"
  },
  "reference": "Your internal reference for the return"
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | No | The unique identifier of the return. |
| reference | string | No | Your internal reference for the return. |
| status | string | No | The resulting status of the return.  Possible values: **Authorised**, **Declined**. |
| transferId | string | No | The unique identifier of the original transfer. |


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
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
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
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
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
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
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
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |

## Response examples

### 200 Success

**transfers-return**
```json
{
  "id": "1W1UG35QQEBJLHZ8",
  "reference": "Your internal reference for the return",
  "status": "Authorised",
  "transferId": "1W1UG35U8A9J5ZLG"
}
```