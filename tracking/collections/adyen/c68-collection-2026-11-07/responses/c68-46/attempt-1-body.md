# PATCH /companies/{companyId}/terminalThemes/{id} - Update the metadata of a terminal theme

Changes the metadata, consisting of the name and dark or light mode, of the terminal theme specified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#manage-api-permissions):

- Management API - Terminal themes read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the terminal theme. |
| companyId | string | Yes | The unique identifier of the company account. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| mode | string | No | The terminal display mode. Possible values: **dark**, **light**. |
| name | string,null | No | The name of the theme. Must be unique per account within the same company context. |

## Request examples

### update-terminal-theme-request
```json
{
  "name": "ThemeLive",
  "mode": "light"
}
```
## Responses

### 200 Success
OK

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the theme. |
| mode | string | Yes | The terminal display mode. Possible values: **dark**, **light**. |
| name | string | Yes | The name of the theme. |


### 400 Client Error
Bad Request


### 401 Client Error
Unauthorized


### 403 Client Error
Forbidden


### 404 Client Error
Not Found


### 422 Client Error
Unprocessable Entity


### 500 Server Error
Internal Server Error

## Response examples

### 200 Success

**update-terminal-theme-200**
```json
{
  "id": "THEM_001ABC",
  "name": "ThemeLive",
  "mode": "light"
}
```

### 400 Client Error

**update-terminal-theme-400**
```json
{
  "type": "https://docs.adyen.com/errors/invalid-request",
  "title": "Bad Request",
  "status": 400,
  "errorCode": "00_400"
}
```

### 401 Client Error

**update-terminal-theme-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**update-terminal-theme-403**
```json
{
  "type": "https://docs.adyen.com/errors/forbidden",
  "title": "Forbidden",
  "detail": "You do not have access to the requested account",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 403,
  "errorCode": "00_403"
}
```

### 404 Client Error

**update-terminal-theme-404**
```json
{
  "type": "https://docs.adyen.com/errors/not-found",
  "title": "Not Found",
  "detail": "Cannot find a theme with the given ID for the specified owner and company context",
  "requestId": "f7a1c89db4f2ca31e82734bc10da9f21",
  "status": 404,
  "errorCode": "00_404"
}
```

### 422 Client Error

**update-terminal-theme-422**
```json
{
  "type": "https://docs.adyen.com/errors/validation",
  "title": "The request is missing required fields or contains invalid data.",
  "requestId": "22ccfa81a92dcba49c7fc13992412b4a",
  "status": 422,
  "errorCode": "29_001",
  "invalidFields": [
    {
      "name": "name",
      "value": "ThemeLive",
      "message": "A theme with this name already exists for the same owner and company context."
    }
  ]
}
```

### 500 Server Error

**update-terminal-theme-500**
```json
{
  "type": "https://docs.adyen.com/errors/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "errorCode": "00_500"
}
```