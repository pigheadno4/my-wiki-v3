# GET /merchants/{merchantAccount}/connectedDevices - Get a list of connected devices

Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified merchant account that have an active cloud connection.  The `store` query parameter limits the list of devices to those belonging to a specific store under the specified merchant account.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- **Cloud Device API role**

## Servers

**Test environment**
- https://device-api-test.adyen.com/v1

**Live environment for Australia**
- https://device-api-live-au.adyen.com/v1

**Live environment for East Asia**
- https://device-api-live-apse.adyen.com/v1

**Live environment for Europe**
- https://device-api-live.adyen.com/v1

**Live environment for United States of America**
- https://device-api-live-us.adyen.com/v1

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantAccount | string | Yes | The unique identifier of the merchant account. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| store | string | No | The store ID of the store belonging to the merchant account specified in the path. |

## Responses

### 200 Success
Successful operation

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| uniqueDeviceIds | array of string | No | A list of the unique IDs of the devices that have an active cloud connection. The IDs are payment terminal IDs in the format *[terminal model]-[serial number]* (for example, P400‑123456789), or SDK installation IDs as used in Mobile solutions. |


### 401 Client Error
Unauthorized

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
|   - message | string | Yes | Description of the validation error. |
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
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
|   - message | string | Yes | Description of the validation error. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |

## Response examples

### 200 Success

**connected-devices-for-merchant-200**
```json
{
  "uniqueDeviceIds": [
    "S1F2-000158215131748",
    "S1F2-000158215131749",
    "S1F2-000158215131750",
    "M400-401972710",
    "M400-401972715",
    "M400-401972720"
  ]
}
```

### 401 Client Error

**connected-devices-for-merchant-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**connected-devices-for-merchant-403**
```json
{
  "type": "https://docs.adyen.com/errors/forbidden",
  "errorCode": "00_403",
  "title": "Forbidden",
  "detail": "User doesn't have access to all token policy resources",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 403
}
```