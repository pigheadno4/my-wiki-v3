# GET /merchants/{merchantId}/terminalThemes - List terminal themes

Returns a paginated list of terminal themes for the merchant account specified in the path. The response provides only the metadata of the themes. Assets (images and videos) are not included. To get the URLs for the assets of a specific theme, make a GET request to the `/merchants/{merchantId}/terminalThemes/{id}` endpoint

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#manage-api-permissions):

- Management API - Terminal themes read and write

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
| search | string | No | A search term to filter themes by name. The match is case-insensitive and returns any theme with a name that contains the search term. |
| page | integer | No | The number of the page to fetch. If not specified, the list starts from page 1. |
| pageSize | integer | No | The number of themes to return per page. If not specified, the list has 10 themes per page. |

## Responses

### 200 Success
OK

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | array of object | Yes | The list of themes for the requested page. |
|   - id | string | Yes | The unique identifier of the theme. |
|   - mode | string | Yes | The terminal display mode. Possible values: **dark**, **light**. |
|   - name | string | Yes | The name of the theme. |
| hasNextPage | boolean | Yes | Indicates whether there are more themes after the current page. |


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

**list-terminal-themes-200**
```json
{
  "data": [
    {
      "id": "THEM_001ABC",
      "name": "BrandDark",
      "mode": "dark"
    },
    {
      "id": "THEM_002DEF",
      "name": "BrandLight",
      "mode": "light"
    }
  ],
  "hasNextPage": false
}
```

### 400 Client Error

**list-terminal-themes-400**
```json
{
  "type": "https://docs.adyen.com/errors/invalid-request",
  "title": "Bad Request",
  "status": 400,
  "errorCode": "00_400"
}
```

### 401 Client Error

**list-terminal-themes-401**
```json
{
  "type": "https://docs.adyen.com/errors/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "errorCode": "00_401"
}
```

### 403 Client Error

**list-terminal-themes-403**
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

**list-terminal-themes-404**
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

**list-terminal-themes-422**
```json
{
  "type": "https://docs.adyen.com/errors/validation",
  "title": "The request is missing required fields or contains invalid data.",
  "requestId": "22ccfa81a92dcba49c7fc13992412b4a",
  "status": 422,
  "errorCode": "29_001",
  "invalidFields": [
    {
      "name": "pageSize",
      "value": "200",
      "message": "pageSize must be between 1 and 100"
    }
  ]
}
```

### 500 Server Error

**list-terminal-themes-500**
```json
{
  "type": "https://docs.adyen.com/errors/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "errorCode": "00_500"
}
```