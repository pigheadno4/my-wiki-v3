# GET /themes/{id} - Get an onboarding link theme

Returns the details of the theme identified in the path.

Requests to this endpoint are subject to rate limits:

Live environments: 700 requests per 5 seconds.

Test environments: 200 requests per 5 seconds.

Failed requests are subject to a limit of 5 failures per 10 seconds.

## Servers
- https://kyc-test.adyen.com/lem/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the theme |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| createdAt | string | Yes | The creation date of the theme. |
| description | string | No | The description of the theme. |
| id | string | Yes | The unique identifier of the theme. |
| properties | object (string) | Yes | The properties of the theme. |
| updatedAt | string | No | The date when the theme was last updated. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |

## Response examples

### 200 Success

**success**
```json
{
  "description": "Light colors theme",
  "properties": {
    "privacyStatementPage": "https://www.adyen.com/legal/terms-and-conditions",
    "supportPage": "https://www.adyen.com/contact",
    "logo": "ONBA422JV223222D5FWC4TK25S3DQW",
    "pageTitle": "Example onboarding light colors",
    "backgroundColor": "#FFFFFF",
    "faqPage": "https://docs.adyen.com/hosted-onboarding-faqs",
    "backgroundImage": "ONBA422JV223222D5G82M96F6P2VTV",
    "pageLayout": "withBackground"
  },
  "createdAt": "2022-06-22T00:00:00+02:00",
  "id": "ONBT422KH223222D5G82M968PB46HR",
  "updatedAt": "2022-08-25T00:00:00+02:00"
}
```