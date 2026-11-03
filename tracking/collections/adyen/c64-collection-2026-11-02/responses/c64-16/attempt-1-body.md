# POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings - Create a balance webhook setting

Configures the criteria for triggering [balance webhooks](https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated).

Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered when the balance reaches, exceeds, or drops below a specific value in a specific currency.

You can get notified about balance changes in your entire balance platform, in the balance accounts of a specific user, or a specific balance account. The hierarchy between the webhook settings are based on the following business logic:

Settings on a higher level apply to all lower level resources (balance platform > account holder > balance acocunt).

The most granular setting overrides higher level settings (balance account > account holder > balance platform).

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| webhookId | string | Yes | The unique identifier of the balance webhook. |
| balancePlatformId | string | Yes | The unique identifier of the balance platform. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| conditions | array of object | No | The array of conditions a balance change must meet for Adyen to send the webhook. |
|   - balanceType | string | Yes | Define the type of balance about which you want to get notified. Possible values:  **available**: the balance available for use.  **balance**: the sum of transactions that have already been settled.  **pending**: the sum of transactions that will be settled in the future.  **reserved**: the balance currently held in reserve. |
|   - conditionType | string | Yes | Define when you want to get notified about a balance change. Possible values:  **greaterThan**: the balance in the account(s) exceeds the specified `value`.  **greaterThanOrEqual**: the balance in the account(s) reaches or exceeds the specified `value`.  **lessThan**: the balance in the account(s) drops below the specified `value`.  **lessThanOrEqual**: the balance in the account(s) reaches to drops below the specified `value`. |
|   - value | integer | Yes | The value limit in the specified balance type and currency, in minor units. |
| currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance. |
| status | string | Yes | The status of the webhook setting. Possible values:  - **active**: You receive a balance webhook if any of the conditions in this setting are met.  - **inactive**: You do not receive a balance webhook even if the conditions in this settings are met. |
| target | object | Yes | The type and ID of the resource about whose balance changes you want to be notified. |
|   - id | string | Yes | The unique identifier of the `target.type`. This can be the ID of your:  - balance platform  - account holder  - account holder's balance account |
|   - type | string | Yes | The resource for which you want to receive notifications. Possible values:  **balancePlatform**: receive notifications about balance changes in your entire balance platform.  **accountHolder**: receive notifications about balance changes of a specific user.  **balanceAccount**: receive notifications about balance changes in a specific balance account. |
| type | string | Yes | The type of the webhook you are configuring. Set to **balance**. |

## Request examples

### create-webhook-setting
```json
{
  "type": "balance",
  "target": {
    "type": "balanceAccount",
    "id": "BA00000000000000000LIABLE"
  },
  "currency": "USD",
  "status": "active",
  "conditions": [
    {
      "balanceType": "available",
      "conditionType": "lessThan",
      "value": 500000
    }
  ]
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance. |
| id | string | Yes | The unique identifier of the webhook setting. |
| status | string | Yes | The status of the webhook setting. Possible values:  - **active**: You receive a balance webhook if any of the conditions in this setting are met.  - **inactive**: You do not receive a balance webhook even if the conditions in this settings are met. |
| target | object | Yes | The resource about whose balance change you want to get notified. |
|   - id | string | Yes | The unique identifier of the `target.type`. This can be the ID of your:  - balance platform  - account holder  - account holder's balance account |
|   - type | string | Yes | The resource for which you want to receive notifications. Possible values:  **balancePlatform**: receive notifications about balance changes in your entire balance platform.  **accountHolder**: receive notifications about balance changes of a specific user.  **balanceAccount**: receive notifications about balance changes in a specific balance account. |
| type | string | Yes | The type of the webhook setting. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 404 Client Error
The payment was not found

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |

## Response examples

### 200 Success

**create-webhook-setting**
```json
{
  "id": "BWHS00000000000000000000000001",
  "type": "balance",
  "target": {
    "type": "balanceAccount",
    "id": "BA00000000000000000LIABLE"
  },
  "currency": "USD",
  "status": "active",
  "conditions": [
    {
      "balanceType": "available",
      "conditionType": "lessThan",
      "value": 500000
    }
  ]
}
```