# PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers - Update the authorized users for a card.

Updates the list of authorized users for a card.

This request replaces all existing authorized users for the card.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| paymentInstrumentId | string | Yes |  |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| legalEntityIds | array of string | No | The legal entity IDs of the authorized card users linked to the specified payment instrument. |

## Request examples

### authorisedCardUsers
```json
{
  "legalEntityIds": [
    "LE328V522322685LV3KTNF35M",
    "LE328SW223226B5LWVWNQ8THN"
  ]
}
```
## Responses

### 204 Success
Successful operation


### 400 Client Error
Bad request

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
Unauthorized

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
Forbidden

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

### 400 Client Error

**authorisedCardUsers-patch-400**
```json
{
  "type": "https://docs.adyen.com/errors/bad-request",
  "errorCode": "999_400_000",
  "title": "Bad request",
  "detail": "Payment instrument hasn't linked with any legal entity reference Please use post method.",
  "requestId": "a852d1b1c0fcbb7177b3bd16a0a2f6d7",
  "status": 400
}
```

### 401 Client Error

**authorisedCardUsers-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**authorisedCardUsers-403**
```json
{
  "type": "https://docs.adyen.com/errors/forbidden",
  "errorCode": "00_403",
  "title": "Forbidden",
  "detail": "Not allowed for card partner yet.",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 403
}
```

### 422 Client Error

**authorisedCardUsers-patch-422**
```json
{
  "type": "https://docs.adyen.com/errors/unprocessable-entity",
  "errorCode": "999_422_002",
  "title": "Business constraint violation",
  "detail": "Request must have maximum 10 legal entity reference.",
  "requestId": "aeadb5646efe065f5e027d2fb6b137ec",
  "status": 422
}
```