# POST /merchants/{merchantId}/apiCredentials - Create an API credential

Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify the roles and allowed origins for the new API credential.

The response includes the:

- [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication.

- [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication.

- [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.

Make sure you store the API key securely in your system. You won't be able to retrieve it later.

If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/%7BmerchantId%7D/apiCredentials/%7BapiCredentialId%7D/generateApiKey).

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—API credentials read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantId | string | Yes | The unique identifier of the merchant account. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| allowedOrigins | array of string | No | The list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential. |
| description | string | No | Description of the API credential. |
| roles | array of string | No | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials. |

## Request examples

### post-merchant-credential
```json
{
  "roles": [
    "Checkout webservice role"
  ],
  "allowedOrigins": [
    "https://www.mystore.com"
  ]
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| _links | object | No | References to resources linked to the API credential. |
|   - allowedOrigins | object | No | List of allowed origins. |
|     - href | string | No |  |
|   - company | object | No | Company account that the API credential is linked to. Only present for company-level webhooks. |
|     - href | string | No |  |
|   - generateApiKey | object | No | Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours. |
|     - href | string | No |  |
|   - generateClientKey | object | No | Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours. |
|     - href | string | No |  |
|   - merchant | object | No | The merchant account that the API credential is linked to. Only present for merchant-level API credentials. |
|     - href | string | No |  |
|   - self | object | Yes | Link to the resource itself. |
|     - href | string | No |  |
| active | boolean | Yes | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. |
| allowedIpAddresses | array of string | Yes | List of IP addresses from which your client can make requests.  If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, you get a security error. |
| allowedOrigins | array of object | No | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. |
|   - _links | object | No | References to resources linked to the allowed origin. |
|     - self | object | Yes | Link to the resource itself. |
|   - domain | string | Yes | Domain of the allowed origin. |
|   - id | string | No | Unique identifier of the allowed origin. |
| apiKey | string | Yes | The API key for the API credential that was created. |
| clientKey | string | Yes | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. |
| description | string | No | Description of the API credential. |
| id | string | Yes | Unique identifier of the API credential. |
| password | string | Yes | The password for the API credential that was created. |
| roles | array of string | Yes | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. |
| subjectDN | string | No | The subject DN of the certificate issued by Adyen. |
| username | string | Yes | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. |


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

**post-merchant-credential**
```json
{
  "id": "YOUR_API_CREDENTIAL",
  "username": "YOUR_USERNAME",
  "clientKey": "YOUR_CLIENT_KEY",
  "allowedIpAddresses": [],
  "roles": [
    "Checkout webservice role"
  ],
  "active": true,
  "allowedOrigins": [
    {
      "id": "YOUR_ALLOWED_ORIGIN",
      "domain": "https://www.mystore.com",
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins/YOUR_ALLOWED_ORIGIN"
        }
      }
    }
  ],
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL"
    },
    "allowedOrigins": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/allowedOrigins"
    },
    "generateApiKey": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/generateApiKey"
    },
    "generateClientKey": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL/generateClientKey"
    },
    "merchant": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
    }
  },
  "apiKey": "YOUR_API_KEY",
  "password": "YOUR_PASSWORD"
}
```