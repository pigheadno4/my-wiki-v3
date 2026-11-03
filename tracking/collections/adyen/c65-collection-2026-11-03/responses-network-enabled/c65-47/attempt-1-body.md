# GET /legalEntities/{id}/termsOfServiceAcceptanceInfos - Get Terms of Service information for a legal entity

Returns Terms of Service information for a legal entity.

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

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | array of object | No | The Terms of Service acceptance information. |
|   - acceptedBy | string | No | The unique identifier of the user that accepted the Terms of Service. |
|   - acceptedFor | string | No | The unique identifier of the legal entity for which the Terms of Service are accepted. |
|   - createdAt | string | No | The date when the Terms of Service were accepted, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00. |
|   - id | string | No | An Adyen-generated reference for the accepted Terms of Service. |
|   - type | string | No | The type of Terms of Service.  Possible values:  - **adyenForPlatformsManage**  - **adyenIssuing**  - **adyenForPlatformsAdvanced**  - **adyenCapital**  - **adyenCapitalCashAdvance**  - **adyenAccount**  - **adyenCard**  - **adyenFranchisee**  - **adyenPccr**  - **adyenChargeCard**  - **kycOnInvite**  - **directDebit** |
|   - validTo | string | No | The expiration date for the Terms of Service acceptance, in ISO 8601 extended format. For example, 2022-12-18T00:00:00+01:00. |


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
  "data": [
    {
      "acceptedBy": "LE00000000000000000000002",
      "acceptedFor": "LE00000000000000000000001",
      "createdAt": "2022-12-05T13:36:58.212253Z",
      "id": "TOSA000AB00000000B2AAAB2BA0AA0",
      "type": "adyenIssuing"
    }
  ]
}
```