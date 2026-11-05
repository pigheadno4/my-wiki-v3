# POST /companies/{companyId}/shippingLocations - Create a shipping location

Creates a shipping location for the company identified in the path. A shipping location defines an address where orders can be delivered.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| companyId | string | Yes | The unique identifier of the company account. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| address | object | No | The address details of the shipping location. |
|   - city | string | No | The name of the city. |
|   - companyName | string | No | The name of the company. |
|   - country | string | No | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
|   - postalCode | string | No | The postal code. |
|   - stateOrProvince | string | No | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Applicable for the following countries:  - Australia  - Brazil  - Canada  - India  - Mexico  - New Zealand  - United States |
|   - streetAddress | string | No | The name of the street, and the house or building number. |
|   - streetAddress2 | string | No | Additional address details, if any. |
| contact | object | No | The contact details for the shipping location. |
|   - email | string | No | The individual's email address. |
|   - firstName | string | No | The individual's first name. |
|   - infix | string | No | The infix in the individual's name, if any. |
|   - lastName | string | No | The individual's last name. |
|   - phoneNumber | string | No | The individual's phone number, specified as 10-14 digits with an optional `+` prefix. |
| id | string | No | The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order. |
| name | string | No | The unique name of the shipping location. |

## Request examples

### create-shipping-location
```json
{
  "name": "YOUR_COMPANY Rokin depot",
  "address": {
    "companyName": "YOUR_COMPANY",
    "streetAddress": "Rokin 21",
    "postalCode": "1012 KS",
    "city": "Amsterdam",
    "stateOrProvince": "",
    "country": "NL"
  },
  "contact": {
    "firstName": "Paul",
    "lastName": "Green",
    "phoneNumber": "+31 020 1234567",
    "email": "Paul.Green@company.com"
  }
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| address | object | No | The address details of the shipping location. |
|   - city | string | No | The name of the city. |
|   - companyName | string | No | The name of the company. |
|   - country | string | No | The two-letter country code, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
|   - postalCode | string | No | The postal code. |
|   - stateOrProvince | string | No | The state or province as defined in [ISO 3166-2](https://www.iso.org/standard/72483.html). For example, **ON** for Ontario, Canada.  Applicable for the following countries:  - Australia  - Brazil  - Canada  - India  - Mexico  - New Zealand  - United States |
|   - streetAddress | string | No | The name of the street, and the house or building number. |
|   - streetAddress2 | string | No | Additional address details, if any. |
| contact | object | No | The contact details for the shipping location. |
|   - email | string | No | The individual's email address. |
|   - firstName | string | No | The individual's first name. |
|   - infix | string | No | The infix in the individual's name, if any. |
|   - lastName | string | No | The individual's last name. |
|   - phoneNumber | string | No | The individual's phone number, specified as 10-14 digits with an optional `+` prefix. |
| id | string | No | The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order. |
| name | string | No | The unique name of the shipping location. |


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

**create-shipping-location**
```json
{
  "id": "S2-7973536B20662642215526704F302044452F714622375D476169",
  "name": "YOUR_COMPANY Rokin depot",
  "contact": {
    "firstName": "Paul",
    "lastName": "Green",
    "phoneNumber": "+31 020 1234567",
    "email": "Paul.Green@company.com"
  },
  "address": {
    "companyName": "YOUR_COMPANY",
    "streetAddress": "Rokin 21",
    "postalCode": "1012 KS",
    "city": "Amsterdam",
    "stateOrProvince": ""
  }
}
```