# GET /balanceAccounts/{id}/paymentInstruments - Get payment instruments linked to a balance account

Returns a paginated list of the payment instruments associated with a balance account.

To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments which are in active status and to skip the first 6, use `/balanceAccounts/{id}/paymentInstruments?limit=3&offset=6&status=active`.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the balance account. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| status | string | No | The status of the payment instruments that you want to get. By default, the response includes payment instruments with any status. |
| limit | integer | No | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |
| offset | integer | No | The number of items that you want to skip. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| hasNext | boolean | Yes | Indicates whether there are more items on the next page. |
| hasPrevious | boolean | Yes | Indicates whether there are more items on the previous page. |
| paymentInstruments | array of object | Yes | List of payment instruments associated with the balance account. |
|   - additionalBankAccountIdentifications | array | No | Contains optional, additional business account details. Returned when you create a payment instrument with `type` **bankAccount**. |
|   - balanceAccountId | string | Yes | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument. |
|   - bankAccount | object | No | Contains the business account details. Returned when you create a payment instrument with `type` **bankAccount**. |
|     - accountNumber | string | No | The bank account number, without separators or whitespace. |
|     - accountType | string | No | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. |
|     - branchNumber | string | No | The bank account branch number, without separators or whitespace |
|     - formFactor | string | No | Business accounts with a `formFactor` value of **physical** are business accounts issued under the central bank of that country. The default value is **physical** for NL, US, and UK business accounts.  Adyen creates a local IBAN for business accounts when the `formFactor` value is set to **virtual**. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL. |
|     - iban | string | No | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |
|     - routingNumber | string | No | The [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. |
|     - sortCode | string | No | The [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace. |
|     - type | string | Yes | **iban** or **usLocal** or **ukLocal** |
|   - card | object | No | Contains information about the card payment instrument. Returned when you create a payment instrument with `type` **card**. |
|     - authentication | object | No | Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to [3D Secure and digital wallets](https://docs.adyen.com/issuing/3d-secure-and-wallets) for more information. |
|     - bin | string | No | The bank identification number (BIN) of the card number. |
|     - brand | string | Yes | The brand of the physical or the virtual card. Possible values: **visa**, **mc**. |
|     - brandVariant | string | Yes | The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**.  Reach out to your Adyen contact to get the values relevant for your integration. |
|     - cardholderName | string | Yes | The name of the cardholder. Maximum length: 26 characters. |
|     - configuration | object | No | Contains information about the configuration profile for your cards. The configuration profile consists of settings required when creating a physical or a virtual card. You identify a configuration profile with its `configurationProfileId`.  When you provide this field in a request, you can override the settings of an existing configuration profile.  Reach out to your Adyen contact to get the values that you can send in this object. |
|     - cvc | string | No | The CVC2 value of the card.  The CVC2 is not sent by default. This is only returned in the `POST` response for single-use virtual cards. |
|     - deliveryContact | object | No | The delivery contact (name and address) for physical card delivery. |
|     - expiration | object | No | The expiration date of the card. |
|     - formFactor | string | Yes | The form factor of the card. Possible values: **virtual**, **physical**. |
|     - lastFour | string | No | Last last four digits of the card number. |
|     - number | string | No | The primary account number (PAN) of the card.  The PAN is masked by default and returned only for single-use virtual cards. |
|     - threeDSecure | string | No | The 3DS configuration of the physical or the virtual card. Possible values: **fullySupported**, **secureCorporate**.  Reach out to your Adyen contact to get the values relevant for your integration. |
|     - usage | string | No | Specifies how many times the card can be used. Possible values: **singleUse**, **multiUse**.  Reach out to your Adyen contact to determine the value relevant for your integration. |
|   - description | string | No | Your description for the payment instrument, maximum 300 characters. |
|   - id | string | Yes | The unique identifier of the payment instrument. |
|   - issuingCountryCode | string | Yes | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |
|   - paymentInstrumentGroupId | string | No | The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs. |
|   - reference | string | No | Your reference for the payment instrument, maximum 150 characters. |
|   - replacedById | string | No | The unique identifier of the payment instrument that replaced this payment instrument. |
|   - replacementOfId | string | No | The unique identifier of the payment instrument that is replaced by this payment instrument. |
|   - status | string | No | The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card.formFactor` and the `issuingCountryCode`. For example, when issuing physical cards in the US, the default status is **inactive**.  Possible values:  **active**:  The payment instrument is active and can be used to make payments.  **inactive**: The payment instrument is inactive and cannot be used to make payments.  **suspended**: The payment instrument is suspended, either because it was stolen or lost.  **closed**: The payment instrument is permanently closed. This action cannot be undone. |
|   - statusComment | string | No | The status comment provides additional information for the statusReason of the payment instrument. |
|   - statusReason | string | No | The reason for the status of the payment instrument.  Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**, **suspectedFraud**, **transactionRule**, **other**. If the reason is **other**, you must also send the `statusComment` parameter describing the status change. |
|   - type | string | Yes | The type of payment instrument.  Possible values: **card**, **bankAccount**. |


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
  "hasNext": true,
  "hasPrevious": false,
  "paymentInstruments": [
    {
      "balanceAccountId": "BA32272223222B59CZ3T52DKZ",
      "issuingCountryCode": "GB",
      "status": "active",
      "type": "card",
      "card": {
        "brand": "mc",
        "brandVariant": "mc",
        "cardholderName": "name",
        "formFactor": "virtual",
        "bin": "555544",
        "expiration": {
          "month": "12",
          "year": "2022"
        },
        "lastFour": "2357",
        "number": "************2357"
      },
      "id": "PI32272223222B59M5TM658DT"
    },
    {
      "balanceAccountId": "BA32272223222B59CZ3T52DKZ",
      "issuingCountryCode": "GB",
      "status": "active",
      "type": "card",
      "card": {
        "brand": "mc",
        "brandVariant": "mc",
        "cardholderName": "name",
        "formFactor": "virtual",
        "bin": "555544",
        "expiration": {
          "month": "01",
          "year": "2023"
        },
        "lastFour": "8331",
        "number": "************8331"
      },
      "id": "PI32272223222B59PXDGQDLSF"
    }
  ]
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