# POST /legalEntities/{id}/termsOfService - Get Terms of Service document

Returns the Terms of Service document for a legal entity.

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
| id | string | Yes | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. For organizations, this is the ID of the organization. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| language | string | Yes | The language to be used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible values: **en** for English or **fr** for French. |
| termsOfServiceDocumentFormat | string | No | The requested format for the Terms of Service document. Default value: JSON. Possible values: **JSON**, **PDF**, or **TXT**. |
| type | string | Yes | The type of Terms of Service.  Possible values:  - **adyenForPlatformsManage**  - **adyenIssuing**  - **adyenForPlatformsAdvanced**  - **adyenCapital**  - **adyenCapitalCashAdvance**  - **adyenAccount**  - **adyenCard**  - **adyenFranchisee**  - **adyenPccr**  - **adyenChargeCard**  - **kycOnInvite**  - **directDebit** |

## Request examples

### createTermsofService
```json
{
  "type": "adyenIssuing",
  "language": "en"
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| document | string | No | The Terms of Service document in Base64-encoded format. |
| id | string | No | The unique identifier of the legal entity. |
| language | string | No | The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English or **fr** for French.  Note that French is only available for some integration types in certain countries/regions. Reach out to your Adyen contact for more information. |
| termsOfServiceDocumentFormat | string | No | The format of the Terms of Service document. |
| termsOfServiceDocumentId | string | No | The unique identifier of the Terms of Service document. |
| type | string | No | The type of Terms of Service.  Possible values:  - **adyenForPlatformsManage**  - **adyenIssuing**  - **adyenForPlatformsAdvanced**  - **adyenCapital**  - **adyenCapitalCashAdvance**  - **adyenAccount**  - **adyenCard**  - **adyenFranchisee**  - **adyenPccr**  - **adyenChargeCard**  - **kycOnInvite**  - **directDebit** |


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

**createTermsofService**
```json
{
  "id": "LE00000000000000000000001",
  "type": "adyenIssuing",
  "language": "en",
  "document": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC==",
  "termsOfServiceDocumentId": "abc123",
  "termsOfServiceDocumentFormat": "JSON"
}
```