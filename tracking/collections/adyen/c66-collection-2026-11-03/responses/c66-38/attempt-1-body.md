# GET /merchants/{merchantId}/apiCredentials - Get a list of API credentials

Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the merchant account. The list is grouped into pages as defined by the query parameters.

To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—API credentials read and write

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
| pageSize | integer | No | The number of items to have on a page, maximum 100. The default is 10 items on a page. |
| pageNumber | integer | No | The number of the page to fetch. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| _links | object | No | Pagination references. |
|   - first | object | Yes | The first page. |
|     - href | string | No |  |
|   - last | object | Yes | The last page. |
|     - href | string | No |  |
|   - next | object | No | The next page. Only present if there is a next page. |
|     - href | string | No |  |
|   - prev | object | No | The previous page. Only present if there is a previous page. |
|     - href | string | No |  |
|   - self | object | Yes | The current page. |
|     - href | string | No |  |
| data | array of object | No | The list of API credentials. |
|   - _links | object | No | References to resources linked to the API credential. |
|     - allowedOrigins | object | No | List of allowed origins. |
|     - company | object | No | Company account that the API credential is linked to. Only present for company-level webhooks. |
|     - generateApiKey | object | No | Generates a new API key. When you generate a new one, the existing key remains valid for 24 hours. |
|     - generateClientKey | object | No | Generates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours. |
|     - merchant | object | No | The merchant account that the API credential is linked to. Only present for merchant-level API credentials. |
|     - self | object | Yes | Link to the resource itself. |
|   - active | boolean | Yes | Indicates if the API credential is enabled. Must be set to **true** to use the credential in your integration. |
|   - allowedIpAddresses | array of string | Yes | List of IP addresses from which your client can make requests.  If the list is empty, we allow requests from any IP. If the list is not empty and we get a request from an IP which is not on the list, you get a security error. |
|   - allowedOrigins | array of object | No | List containing the [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) linked to the API credential. |
|     - _links | object | No | References to resources linked to the allowed origin. |
|     - domain | string | Yes | Domain of the allowed origin. |
|     - id | string | No | Unique identifier of the allowed origin. |
|   - clientKey | string | Yes | Public key used for [client-side authentication](https://docs.adyen.com/development-resources/client-side-authentication). The client key is required for Drop-in and Components integrations. |
|   - description | string | No | Description of the API credential. |
|   - id | string | Yes | Unique identifier of the API credential. |
|   - roles | array of string | Yes | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. |
|   - subjectDN | string | No | The subject DN of the certificate issued by Adyen. |
|   - username | string | Yes | The name of the [API credential](https://docs.adyen.com/development-resources/api-credentials), for example **ws@Company.TestCompany**. |
| itemsTotal | integer | Yes | Total number of items. |
| pagesTotal | integer | Yes | Total number of pages. |


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
  "_links": {
    "first": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials?pageNumber=1&pageSize=10"
    },
    "last": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials?pageNumber=2&pageSize=10"
    },
    "next": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials?pageNumber=2&pageSize=10"
    },
    "self": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials?pageNumber=1&pageSize=10"
    }
  },
  "itemsTotal": 11,
  "pagesTotal": 2,
  "data": [
    {
      "id": "YOUR_API_CREDENTIAL_1",
      "username": "YOUR_USERNAME_1",
      "clientKey": "YOUR_CLIENT_KEY_1",
      "allowedIpAddresses": [],
      "roles": [
        "Merchant Report Download role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_CREDENTIAL_1"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_CREDENTIAL_1/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_CREDENTIAL_1/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_CREDENTIAL_1/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_2",
      "username": "YOUR_USERNAME_2",
      "clientKey": "YOUR_CLIENT_KEY_2",
      "allowedIpAddresses": [],
      "roles": [
        "Merchant Rss feed role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_2"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_2/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_2/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_2/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_3",
      "username": "YOUR_USERNAME_3",
      "clientKey": "YOUR_CLIENT_KEY_3",
      "allowedIpAddresses": [],
      "roles": [
        "Merchant iDeal-API Webservice role",
        "Management API - Accounts read",
        "Management API - API credentials read and write",
        "Management API — Payment methods read",
        "Merchant PAL Donation role",
        "Merchant PAL Charity role",
        "Checkout encrypted cardholder data",
        "Checkout webservice role",
        "Store payout detail and submit payout - withdrawal",
        "Management API - Accounts read and write",
        "Management API - Webhooks read",
        "Merchant Payout role",
        "API tokenise payment details",
        "General API Payments role",
        "API Supply MPI data with Payments",
        "API Authorise Referred Payments",
        "API PCI Payments role",
        "Management API - Stores read",
        "API Payment RefundWithData",
        "API Clientside Encryption Payments role",
        "API to retrieve authentication data",
        "Management API - Stores read and write",
        "Management API - Webhooks read and write",
        "Mastercard inControl service",
        "Merchant Recurring role",
        "Management API - Payout Account Settings Read",
        "API surcharge cost estimation and regulatory information",
        "Store payout detail",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "allowedOrigins": [
        {
          "id": "YOUR_ALLOWED_ORIGIN_1",
          "domain": "YOUR_DOMAIN_1",
          "_links": {
            "self": {
              "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3/allowedOrigins/YOUR_ALLOWED_ORIGIN_1"
            }
          }
        },
        {
          "id": "YOUR_ALLOWED_ORIGIN_2",
          "domain": "YOUR_DOMAIN_2",
          "_links": {
            "self": {
              "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3/allowedOrigins/YOUR_ALLOWED_ORIGIN_2"
            }
          }
        }
      ],
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_3/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_4",
      "username": "YOUR_USERNAME_4",
      "clientKey": "YOUR_CLIENT_KEY_4",
      "allowedIpAddresses": [],
      "roles": [
        "API Clientside Encryption Payments role",
        "API tokenise payment details",
        "General API Payments role",
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "API PCI Payments role",
        "Checkout webservice role",
        "ThreeDSecure WebService Role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_4"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_4/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_4/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_4/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_5",
      "username": "YOUR_USERNAME_5",
      "clientKey": "YOUR_CLIENT_KEY_5",
      "allowedIpAddresses": [],
      "roles": [
        "Merchant iDeal-API Webservice role",
        "General API Payments role",
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_5"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_5/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_5/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_5/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_6",
      "username": "YOUR_USERNAME_6",
      "clientKey": "YOUR_CLIENT_KEY_6",
      "allowedIpAddresses": [],
      "roles": [
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "API PCI Payments role",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_6"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_6/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_6/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_6/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_7",
      "username": "YOUR_USERNAME_7",
      "clientKey": "YOUR_CLIENT_KEY_7",
      "allowedIpAddresses": [],
      "roles": [
        "Checkout encrypted cardholder data",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_7"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_7/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_7/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_7/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_8",
      "username": "YOUR_USERNAME_8",
      "clientKey": "YOUR_CLIENT_KEY_8",
      "allowedIpAddresses": [],
      "roles": [
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_8"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_8/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_8/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_8/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_9",
      "username": "YOUR_USERNAME_9",
      "clientKey": "YOUR_CLIENT_KEY_9",
      "allowedIpAddresses": [],
      "roles": [
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "API PCI Payments role",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_9"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_9/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_9/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_9/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    },
    {
      "id": "YOUR_API_CREDENTIAL_10",
      "username": "YOUR_USERNAME_10",
      "clientKey": "YOUR_CLIENT_KEY_10",
      "allowedIpAddresses": [],
      "roles": [
        "Checkout encrypted cardholder data",
        "Merchant Recurring role",
        "Checkout webservice role",
        "Merchant PAL Webservice role"
      ],
      "active": true,
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_10"
        },
        "allowedOrigins": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_10/allowedOrigins"
        },
        "generateApiKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_10/generateApiKey"
        },
        "generateClientKey": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/apiCredentials/YOUR_API_CREDENTIAL_10/generateClientKey"
        },
        "merchant": {
          "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT"
        }
      }
    }
  ]
}
```