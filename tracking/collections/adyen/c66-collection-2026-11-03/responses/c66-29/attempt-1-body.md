# POST /merchants/{merchantId}/users - Create a new user

Creates a user for the `merchantId` specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—Users read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantId | string | Yes | Unique identifier of the merchant. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountGroups | array of string | No | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| email | string | Yes | The email address of the user. |
| loginMethod | string | No | The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before creating the user.  Possible values: **Email** or **SSO** |
| name | object | Yes | The user's full name.  Allowed length: 1—80 characters. |
|   - firstName | string | Yes | The first name. |
|   - lastName | string | Yes | The last name. |
| roles | array of string | No | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| timeZoneCode | string | No | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| username | string | Yes | The user's email address that will be their username. Must be the same as the one in the `email` field. |

## Request examples

### create-email-user
```json
{
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "username": "johnsmith",
  "email": "john.smith@example.com",
  "loginMethod": "Email",
  "timeZoneCode": "Europe/Amsterdam",
  "roles": [
    "Merchant standard role"
  ]
}
```

### create-sso-user
```json
{
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "username": "johnsmith",
  "email": "john.smith@example.com",
  "loginMethod": "SSO",
  "timeZoneCode": "Europe/Amsterdam",
  "roles": [
    "Merchant standard role"
  ]
}
```

### create-user
```json
{
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "username": "johnsmith",
  "email": "john.smith@example.com",
  "timeZoneCode": "Europe/Amsterdam",
  "roles": [
    "Merchant standard role"
  ]
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| _links | object | No | References to resources connected with this user. |
|   - self | object | Yes | Link to the resource itself. |
|     - href | string | No |  |
| accountGroups | array of string | No | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |
| active | boolean | No | Indicates whether this user is active. |
| apps | array of string | No | Set of apps available to this user |
| email | string | Yes | The email address of the user. |
| id | string | Yes | The unique identifier of the user. |
| name | object | No | The user's full name. |
|   - firstName | string | Yes | The first name. |
|   - lastName | string | Yes | The last name. |
| roles | array of string | Yes | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |
| timeZoneCode | string | Yes | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |
| username | string | Yes | The username for this user. |


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

**create-user**
```json
{
  "id": "S2-3B3C3C3B22",
  "name": {
    "firstName": "John",
    "lastName": "Smith"
  },
  "email": "john.smith@example.com",
  "timeZoneCode": "Europe/Amsterdam",
  "username": "johnsmith",
  "roles": [
    "Merchant standard role"
  ],
  "active": true,
  "_links": {
    "self": {
      "href": "https://management-test.adyen.com/v1/merchants/YOUR_MERCHANT_ACCOUNT/users/S2-3B3C3C3B22"
    }
  }
}
```