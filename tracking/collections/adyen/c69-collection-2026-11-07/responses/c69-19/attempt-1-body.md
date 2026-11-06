# DELETE /merchants/{merchantId}/terminalThemes/{id} - Delete a terminal theme

Deletes the terminal theme identified in the path. If the theme is currently in use, you must first deactivate it using a call to the `/merchants/{merchantId}/terminalThemes/unapply` endpoint before you can delete the theme.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#manage-api-permissions):

- Management API - Terminal themes read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the terminal theme. |
| merchantId | string | Yes | The unique identifier of the merchant account. |

## Responses

### 204 Success
Theme deleted


### 401 Client Error
Unauthorized


### 403 Client Error
Forbidden


### 404 Client Error
Not Found


### 409 Client Error
Conflict


### 500 Server Error
Internal Server Error

## Response examples

### 401 Client Error

**delete-terminal-theme-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**delete-terminal-theme-403**
```json
{
  "type": "https://docs.adyen.com/errors/forbidden",
  "title": "Forbidden",
  "detail": "You do not have access to the specified account",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 403,
  "errorCode": "00_403"
}
```

### 404 Client Error

**delete-terminal-theme-404**
```json
{
  "type": "https://docs.adyen.com/errors/not-found",
  "title": "Not Found",
  "detail": "Account not found or not accessible",
  "requestId": "f7a3b2c1d4e5f6a7b8c9d0e1f2a3b4c5",
  "status": 404,
  "errorCode": "00_404"
}
```

### 409 Client Error

**delete-terminal-theme-409**
```json
{
  "type": "https://docs.adyen.com/errors/conflict",
  "title": "Conflict",
  "status": 409,
  "errorCode": "00_409"
}
```

### 500 Server Error

**delete-terminal-theme-500**
```json
{
  "type": "https://docs.adyen.com/errors/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "errorCode": "00_500"
}
```