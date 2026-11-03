# PATCH /balanceAccounts/{id} - Update a balance account

Updates a balance account.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the balance account. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolderId | string | No | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
| description | string | No | A human-readable description of the balance account. You can use this parameter to distinguish between multiple balance accounts under an account holder. |
| metadata | object (string) | No | A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired.  Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| platformPaymentConfiguration | object | No | Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account. |
|   - salesDayClosingTime | string | No | Specifies at what time a sales day ends for this account.  Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.  Default value: **"00:00"**. |
|   - settlementDelayDays | integer | No | Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.  Possible values: **1** to **20**, or **null**.  Default value: **null**. |
| reference | string | No | Your reference to the balance account. |
| status | string | No | The status of the balance account. Payment instruments linked to the balance account can only be used if the balance account status is **active**.  Possible values: **active**, **closed**, **suspended**. |
| timeZone | string | No | The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |

## Request examples

### updateBalanceAccount
```json
{
  "timeZone": "Europe/Amsterdam"
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolderId | string | Yes | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
| balances | array of object | No | List of balances with the amount and currency. |
|   - available | integer | Yes | The balance available for use. |
|   - balance | integer | Yes | The sum of the transactions that have already been settled. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance. |
|   - pending | integer | No | The sum of the transactions that will be settled in the future. |
|   - pendingAvailable | integer | No | The balance that will become the available balance after the pending balance is settled.  The pending available balance is equal to the lower of the following:  - The `pending` balance  - The `pending` balance plus the `available` balance. |
|   - reserved | integer | Yes | The balance currently held in reserve. |
| defaultCurrencyCode | string | No | The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area. The default value is **EUR**.  After a balance account is created, you cannot change its default currency. |
| description | string | No | A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder. |
| id | string | Yes | The unique identifier of the balance account. |
| metadata | object (string) | No | A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired.  Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
| migratedAccountCode | string | No | The unique identifier of the account of the migrated account holder in the classic integration. |
| platformPaymentConfiguration | object | No | Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account. |
|   - salesDayClosingTime | string | No | Specifies at what time a sales day ends for this account.  Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.  Default value: **"00:00"**. |
|   - settlementDelayDays | integer | No | Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.  Possible values: **1** to **20**, or **null**.  Default value: **null**. |
| reference | string | No | Your reference for the balance account, maximum 150 characters. |
| status | string | No | The status of the balance account, set to **active** by default. |
| timeZone | string | No | The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |


### 400 Client Error
A problem reading or understanding the request.

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

**updateBalanceAccount**
```json
{
  "accountHolderId": "AH32272223222B5GFSNVGFFM7",
  "defaultCurrencyCode": "EUR",
  "timeZone": "Europe/Amsterdam",
  "balances": [
    {
      "available": 0,
      "balance": 0,
      "currency": "EUR",
      "reserved": 0
    }
  ],
  "id": "BA32272223222B59K6ZXHBFN6",
  "status": "active"
}
```

### 400 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/bad-request",
  "title": "Bad request",
  "status": 400,
  "detail": "Empty input which would have resulted in a null result.",
  "errorCode": "00_400"
}
```

### 401 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/security/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Not authorized to access this service.",
  "errorCode": "00_401"
}
```

### 403 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/security/unauthorized",
  "title": "Forbidden",
  "status": 403,
  "detail": "Not the right permission to access this service.",
  "errorCode": "00_403"
}
```

### 422 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/invalid-field-value",
  "title": "Invalid Payment Instrument information provided",
  "status": 422,
  "detail": "The balanceAccountId can only be changed when the status is Inactive or Requested",
  "requestId": "1W1UI15PLVGC9V8O",
  "errorCode": "30_031"
}
```

### 500 Server Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/internal",
  "title": "An internal error happened",
  "status": 500,
  "detail": "Unrecoverable error while trying to create payment instrument",
  "requestId": "1WAF555PLWNTLYOQ",
  "errorCode": "00_500"
}
```