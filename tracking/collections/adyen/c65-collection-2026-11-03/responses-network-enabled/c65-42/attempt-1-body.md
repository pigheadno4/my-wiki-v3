# GET /documents/{id} - Get a document

Returns a document.

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
| id | string | Yes | The unique identifier of the document. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| skipContent | boolean | No | Do not load document content while fetching the document. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| attachment | object | No | Object that contains the document. |
|   - content | string | Yes | The document in Base64-encoded string format. |
|   - contentType | string | No | The file format.  Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**. |
|   - filename | string | No | The name of the file including the file extension. |
|   - pageName | string | No | The name of the file including the file extension. |
|   - pageType | string | No | Specifies which side of the ID card is uploaded.  If the `type` is **driversLicense** or **identityCard**, you must set this to **front** or **back** and include both sides in the same API request.  For any other types, when this is omitted, we infer the page number based on the order of attachments. |
| attachments | array of object | No | Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document. |
|   - content | string | Yes | The document in Base64-encoded string format. |
|   - contentType | string | No | The file format.  Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**. |
|   - filename | string | No | The name of the file including the file extension. |
|   - pageName | string | No | The name of the file including the file extension. |
|   - pageType | string | No | Specifies which side of the ID card is uploaded.  If the `type` is **driversLicense** or **identityCard**, you must set this to **front** or **back** and include both sides in the same API request.  For any other types, when this is omitted, we infer the page number based on the order of attachments. |
| creationDate | string | No | The creation date of the document. |
| description | string | Yes | Your description for the document. |
| expiryDate | string | No | The expiry date of the document, in YYYY-MM-DD format. |
| fileName | string | No | The filename of the document. |
| id | string | No | The unique identifier of the document. |
| issuerCountry | string | No | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |
| issuerState | string | No | The state or province where the document was issued (AU only). |
| modificationDate | string | No | The modification date of the document. |
| number | string | No | The number in the document. |
| owner | object | No | Contains information about the resource that owns the document. |
|   - id | string | Yes | Unique identifier of the resource that owns the document. For `type` **legalEntity**, this value is the unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). For `type` **bankAccount**, this value is the unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id). |
|   - type | string | Yes | Type of resource that owns the document.  Possible values: **legalEntity**, **bankAccount**. |
| type | string | Yes | Type of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type.  For **organization**, the `type` values can be **proofOfAddress**, **registrationDocument**, **vatDocument**, **proofOfOrganizationTaxInfo**, **proofOfOwnership**, **proofOfIndustry**, **proofOfSignatory**, **proofOfDirector**, or **proofOfFundingOrWealthSource**.  For **individual**, the `type` values can be **identityCard**, **driversLicense**, **passport**, **liveSelfie**, **proofOfNationalIdNumber**, **proofOfResidency**, **proofOfIndustry**, **proofOfIndividualTaxId**, **proofOfFundingOrWealthSource** or **proofOfRelationship**.  For **soleProprietorship**, the `type` values can be **constitutionalDocument**, **proofOfAddress**, or **proofOfIndustry**.  For **trust**, the `type` value is **constitutionalDocument**.  For **unincorporatedPartnership**, the `type` value is **constitutionalDocument**.  Use **bankStatement** to upload documents for a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). |


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
  "type": "registrationDocument",
  "attachments": [
    {
      "content": "JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC=="
    }
  ],
  "description": "Registration doc for Example Company",
  "fileName": "Registration doc for Example Company",
  "owner": {
    "id": "LE00000000000000000000001",
    "type": "legalEntity"
  },
  "id": "SE322JV223222F5GV2N9L8GDK"
}
```