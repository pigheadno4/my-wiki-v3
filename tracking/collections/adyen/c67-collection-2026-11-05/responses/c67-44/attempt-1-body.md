# GET /merchants/{merchantId}/terminalOrders/{orderId} - Get an order

Returns the details of the terminal products order identified in the path.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—Terminal ordering read

- Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| orderId | string | Yes | The unique identifier of the order. |
| merchantId | string | Yes | The unique identifier of the merchant account. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| billingEntity | object | No | The details of the entity that the order is billed to. |
|   - address | object | No | The address details of the billing entity. |
|     - city | string | No | The name of the city. |
|     - companyName | string | No | The name of the company. |
|     - country | string | No | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
|     - postalCode | string | No | The postal code. |
|     - stateOrProvince | string | No | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Applicable for the following countries:  - Australia  - Brazil  - Canada  - India  - Mexico  - New Zealand  - United States |
|     - streetAddress | string | No | The name of the street, and the house or building number. |
|     - streetAddress2 | string | No | Additional address details, if any. |
|   - email | string | No | The email address of the billing entity. |
|   - id | string | No | The unique identifier of the billing entity, for use as `billingEntityId` when creating an order. |
|   - name | string | No | The unique name of the billing entity. |
|   - taxId | string | No | The tax number of the billing entity. |
| customerOrderReference | string | No | The merchant-defined purchase order number. This will be printed on the packing list. |
| id | string | No | The unique identifier of the order. |
| items | array of object | No | The products included in the order. |
|   - id | string | No | The unique identifier of the product. |
|   - installments | integer | No | The number of installments for the specified product `id`. |
|   - name | string | No | The name of the product. |
|   - quantity | integer | No | The number of items with the specified product `id` included in the order. |
| orderDate | string | No | The date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z". |
| shippingLocation | object | No | The details of the location where the order is shipped to. |
|   - address | object | No | The address details of the shipping location. |
|     - city | string | No | The name of the city. |
|     - companyName | string | No | The name of the company. |
|     - country | string | No | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
|     - postalCode | string | No | The postal code. |
|     - stateOrProvince | string | No | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Applicable for the following countries:  - Australia  - Brazil  - Canada  - India  - Mexico  - New Zealand  - United States |
|     - streetAddress | string | No | The name of the street, and the house or building number. |
|     - streetAddress2 | string | No | Additional address details, if any. |
|   - contact | object | No | The contact details for the shipping location. |
|     - email | string | No | The individual's email address. |
|     - firstName | string | No | The individual's first name. |
|     - infix | string | No | The infix in the individual's name, if any. |
|     - lastName | string | No | The individual's last name. |
|     - phoneNumber | string | No | The individual's phone number, specified as 10-14 digits with an optional `+` prefix. |
|   - id | string | No | The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order. |
|   - name | string | No | The unique name of the shipping location. |
| status | string | No | The processing status of the order. |
| trackingUrl | string | No | The URL, provided by the carrier company, where the shipment can be tracked. |


### 204 Success
The request has been successfully processed, but there is no additional content.


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
  "id": "4154567890100682",
  "customerOrderReference": "YOUR_REFERENCE",
  "status": "Placed",
  "shippingLocation": {
    "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
    "name": "YOUR_COMPANY Spain",
    "contact": {
      "firstName": "Pablo",
      "lastName": "Mengano",
      "phoneNumber": "+34911234567",
      "email": "Pablo.Mengano@company.com"
    },
    "address": {
      "streetAddress": "Paseo de la Castellana 43",
      "streetAddress2": "7 piso",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "billingEntity": {
    "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
    "name": "YOUR_MERCHANT_ACCOUNT",
    "taxId": "ES1234567890",
    "email": "Pablo.Mengano@company.com",
    "address": {
      "streetAddress": "Paseo de la Castellana 43, 7",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "orderDate": "2022-01-21T16:12:33Z",
  "items": [
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "quantity": 2
    },
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "quantity": 20
    }
  ]
}
```