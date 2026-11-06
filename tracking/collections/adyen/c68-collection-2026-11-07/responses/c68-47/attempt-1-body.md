# POST /companies/{companyId}/terminalThemes/{id}/apply - Apply a terminal theme

Applies the terminal theme specified by its ID to all Android terminals under this company, unless a different theme is applied at a lower level (merchant account, store, or individual terminal).

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

## Responses

### 200 Success
OK


### 401 Client Error
Unauthorized


### 403 Client Error
Forbidden


### 404 Client Error
Not Found


### 500 Server Error
Internal Server Error

## Response examples

### 401 Client Error

**apply-terminal-theme-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**apply-terminal-theme-company-403**
```json
{
  "type": "https://docs.adyen.com/errors/forbidden",
  "title": "Forbidden",
  "detail": "Only company-owned themes can be applied at company level",
  "requestId": "d42c493b5176df89e51516c6060cc34c",
  "status": 403,
  "errorCode": "00_403"
}
```

### 404 Client Error

**apply-terminal-theme-404**
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

### 500 Server Error

**apply-terminal-theme-500**
```json
{
  "type": "https://docs.adyen.com/errors/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "errorCode": "00_500"
}
```