# GET /merchants/{merchantId}/shippingLocations - Get a list of shipping locations

Returns the shipping locations for the merchant account identified in the path.
A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

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
| merchantId | string | Yes | The unique identifier of the merchant account. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| limit | integer | No | The number of locations to return. |
| offset | integer | No | The number of locations to skip. |
| name | string | No | The name of the shipping location. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | array of object | No | Physical locations where orders can be shipped to. |
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
  "data": [
    {
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
    }
  ]
}
```