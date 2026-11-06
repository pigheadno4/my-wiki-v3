# POST /terminals/{terminalId}/terminalThemes/unapply - Unapply a terminal theme

Resets the theme assignment for the Android terminal specified in the path. The terminal will switch to the theme from the next higher level where a custom theme is applied (store, merchant account, or company) or the default Adyen theme. The terminal must be [deployed or boarded](https://docs.adyen.com/api-explorer/Management/3/get/terminals#responses-200-data-assignment-status).

The theme itself remains unchanged and is not deleted.

If no custom theme is currently applied to the terminal, this request returns a **200 OK** response without error.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#manage-api-permissions):

- Management API - Terminal themes read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| terminalId | string | Yes | The unique identifier of the terminal. |

## Responses

### 200 Success
OK


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

**unapply-terminal-theme-200**
```json
{
  "status": "success"
}
```

### 401 Client Error

**unapply-terminal-theme-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**unapply-terminal-theme-403**
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

**unapply-terminal-theme-404**
```json
{
  "type": "https://docs.adyen.com/errors/not-found",
  "title": "Not Found",
  "detail": "Cannot find or cannot access the account",
  "requestId": "f7a3b2c1d4e5f6a7b8c9d0e1f2a3b4c5",
  "status": 404,
  "errorCode": "00_404"
}
```

### 422 Client Error

**unapply-terminal-theme-terminal-422**
```json
{
  "type": "https://docs.adyen.com/errors/validation",
  "title": "Unprocessable Entity",
  "detail": "To apply or unapply a theme the terminal must be deployed or boarded",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 422,
  "errorCode": "00_422"
}
```

### 500 Server Error

**unapply-terminal-theme-500**
```json
{
  "type": "https://docs.adyen.com/errors/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "errorCode": "00_500"
}
```