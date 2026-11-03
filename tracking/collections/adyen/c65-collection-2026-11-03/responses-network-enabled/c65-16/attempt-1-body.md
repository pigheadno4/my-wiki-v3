# POST /balanceAccounts/{id}/transferLimits - Create a transfer limit

Create a transfer limit for your balance account using the unique `id` of your balance account.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the balance account. |


### Header parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| WWW-Authenticate | string | No | Header for authenticating through SCA |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on the `scope` of the limit. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| endsAt | string | No | The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| reference | string | No | Your reference for the transfer limit. |
| scaInformation | object | No | Information for the Strong Customer Authentication (SCA) |
|   - exemption | string | No | The type of exemption for Strong Customer Authentication (SCA). Possible values:  - **lowerLimit**: the newly created limit is lower than the existing limit.  - **notRegulated**: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.  - **setByPlatform**: you set a limit for one of your user's balance accounts, or for your balance platform.  - **initialLimit**: there are no existing transfer limits set on the balance account or balance platform.  - **alreadyPerformed**: you are confident about your user's identity and do not need to verify this using SCA. |
|   - scaOnApproval | boolean | No | Indicates whether to initiate Strong Customer Authentication (SCA) later, during approval, or immediately after you submit this request. Possible values:  - **true**: you can initiate SCA later, during approval, for all pending transfer limits.  - **false** (default): you initiate SCA immediately after submitting the transfer limit request. |
| scope | string | Yes | The scope to which the transfer limit applies. Possible values:  - **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.  - **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| startsAt | string | No | The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| transferType | string | Yes | The type of transfer to which the limit applies. Possible values:  - **instant**: the limit applies to transfers with an **instant** priority.  - **all**: the limit applies to all transfers, regardless of priority. |

## Request examples

### Create a transfer limit request
```json
{
  "amount": {
    "currency": "EUR",
    "value": 10000
  },
  "reference": "Your reference for the transfer limit",
  "scaInformation": {
    "scaOnApproval": true
  },
  "scope": "perTransaction",
  "startsAt": "2025-08-15T06:36:20+01:00",
  "endsAt": "2026-08-14T00:00:00+01:00",
  "transferType": "all"
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | The amount for the transfer limit. This is the maximum amount allowed per transfer or per day based on the `scope` of the limit. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| endsAt | string | No | The date and time when the transfer limit becomes inactive. If you do not specify an end date, the limit stays active until you override it with a new limit.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| id | string | Yes | The unique identifier of the transfer limit. |
| limitStatus | string | Yes | The status of the transfer limit. Possible values:  - **active**: the limit is currently active.  - **inactive**: the limit is currently inactive.  - **pendingSCA**: the limit is pending until your user performs SCA.  - **scheduled**: the limit is scheduled to become active at a future date. |
| reference | string | No | Your reference for the transfer limit. |
| scaInformation | object | No | Information for the Strong Customer Authentication (SCA) |
|   - exemption | string | No | The type of exemption for Strong Customer Authentication (SCA). Possible values:  - **lowerLimit**: the newly created limit is lower than the existing limit.  - **notRegulated**: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.  - **setByPlatform**: you set a limit for one of your user's balance accounts, or for your balance platform.  - **initialLimit**: there are no existing transfer limits set on the balance account or balance platform.  - **alreadyPerformed**: you are confident about your user's identity and do not need to verify this using SCA. |
|   - status | string | Yes | The status of Strong Customer Authentication (SCA). Possible values:  - **notPerformed**: the requester was unable to successfully authenticate the request using SCA, or has an SCA exemption.  - **pending**: the request is pending SCA authentication.  - **performed**: the request is successfully authenticated using SCA. |
| scope | string | Yes | The scope to which the transfer limit applies. Possible values:  - **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.  - **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| startsAt | string | Yes | The date and time when the transfer limit becomes active. If you specify a date in the future, we will schedule a transfer limit.  Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): **YYYY-MM-DDThh:mm:ss.sssTZD** |
| transferType | string | Yes | The type of transfer to which the limit applies. Possible values:  - **instant**: the limit applies to transfers with an **instant** priority.  - **all**: the limit applies to all transfers, regardless of priority. |


### 400 Client Error
The input is invalid, or no registered device for SCA was found.

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
Authentication required via Strong Customer Authentication (SCA). The client must resolve the provided challenge.

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

## Response examples

### 200 Success

**Create a transfer limit response**
```json
{
  "amount": {
    "currency": "EUR",
    "value": 10000
  },
  "endsAt": "2026-08-13T23:00:00+01:00",
  "id": "TRLI00000000000000000000000001",
  "limitStatus": "pendingSCA",
  "reference": "Your reference for the transfer limit",
  "scaInformation": {
    "status": "pending"
  },
  "scope": "perTransaction",
  "startsAt": "2025-08-15T06:36:20+01:00",
  "transferType": "all"
}
```