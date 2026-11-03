# GET /accountHolders/{id}/balanceAccounts - Get all balance accounts of an account holder

Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages, use the query parameters.

For example, to limit the page to 5 balance accounts and skip the first 10, use `/accountHolders/{id}/balanceAccounts?limit=5&offset=10`.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the account holder. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| limit | integer | No | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |
| offset | integer | No | The number of items that you want to skip. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| balanceAccounts | array of object | Yes | List of balance accounts. |
|   - accountHolderId | string | Yes | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders#responses-200-id) associated with the balance account. |
|   - defaultCurrencyCode | string | No | The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. This is the currency displayed on the Balance Account overview page in your Customer Area. The default value is **EUR**.  After a balance account is created, you cannot change its default currency. |
|   - description | string | No | A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder. |
|   - id | string | Yes | The unique identifier of the balance account. |
|   - metadata | object (string) | No | A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired.  Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |
|   - migratedAccountCode | string | No | The unique identifier of the account of the migrated account holder in the classic integration. |
|   - platformPaymentConfiguration | object | No | Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account. |
|     - salesDayClosingTime | string | No | Specifies at what time a sales day ends for this account.  Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.  Default value: **"00:00"**. |
|     - settlementDelayDays | integer | No | Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.  Possible values: **1** to **20**, or **null**.  Default value: **null**. |
|   - reference | string | No | Your reference for the balance account, maximum 150 characters. |
|   - status | string | No | The status of the balance account, set to **active** by default. |
|   - timeZone | string | No | The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). |
| hasNext | boolean | Yes | Indicates whether there are more items on the next page. |
| hasPrevious | boolean | Yes | Indicates whether there are more items on the previous page. |


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

**success**
```json
{
  "balanceAccounts": [
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CTDNB66W2Z",
      "status": "active"
    },
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CTDQPM6W2H",
      "status": "active"
    },
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CVF5J63LMW",
      "status": "active"
    }
  ],
  "hasNext": true,
  "hasPrevious": false
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