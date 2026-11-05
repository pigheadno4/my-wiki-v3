# GET /companies/{companyId}/webhooks - List all webhooks

Lists all webhook configurations for the company account.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API—Webhooks read

- Management API—Webhooks read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| companyId | string | Yes | Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account). |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| pageSize | integer | No | The number of items to have on a page, maximum 100. The default is 10 items on a page. |
| pageNumber | integer | No | The number of the page to fetch. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| _links | object | No | Pagination references. |
|   - first | object | Yes | The first page. |
|     - href | string | No |  |
|   - last | object | Yes | The last page. |
|     - href | string | No |  |
|   - next | object | No | The next page. Only present if there is a next page. |
|     - href | string | No |  |
|   - prev | object | No | The previous page. Only present if there is a previous page. |
|     - href | string | No |  |
|   - self | object | Yes | The current page. |
|     - href | string | No |  |
| accountReference | string | No | Reference to the account. |
| data | array of object | No | The list of webhooks configured for this account. |
|   - _links | object | No | References to resources connected with this webhook. |
|     - company | object | No | The company account that the webhook is configured for. Only present for company-level webhooks. |
|     - generateHmac | object | Yes | Generate an HMAC key. |
|     - merchant | object | No | The merchant account that the webhook is configured for. Only present for merchant-level webhooks. |
|     - self | object | Yes | Link to the resource itself. |
|     - testWebhook | object | Yes | Test the webhook setup. |
|   - acceptsExpiredCertificate | boolean | No | Indicates if expired SSL certificates are accepted. Default value: **false**. |
|   - acceptsSelfSignedCertificate | boolean | No | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |
|   - acceptsUntrustedRootCertificate | boolean | No | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |
|   - accountReference | string | No | Reference to the account the webook is set on. |
|   - active | boolean | Yes | Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account. |
|   - additionalSettings | object | No | Additional shopper and transaction information to be included in your [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings). |
|     - excludeEventCodes | array of string | No | Object containing list of event codes for which the notification will not be sent. |
|     - includeEventCodes | array of string | No | Object containing list of event codes for which the notification will be sent. |
|     - properties | object (boolean) | No | Object containing boolean key-value pairs. The key can be any [standard webhook additional setting](https://docs.adyen.com/development-resources/webhooks/additional-settings), and the value indicates if the setting is enabled. For example, `includeCaptureDelayHours`: **true** means the standard notifications you get will contain the number of hours remaining until the payment will be captured. |
|   - certificateAlias | string | No | The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias. |
|   - communicationFormat | string | Yes | Format or protocol for receiving webhooks. Possible values:  - **soap**  - **http**  - **json** |
|   - description | string | No | Your description for this webhook configuration. |
|   - encryptionProtocol | string | No | SSL version to access the public webhook URL specified in the `url` field. Possible values:  - **TLSv1.3**  - **TLSv1.2**  - **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use `sslVersion`: **TLSv1.2**. |
|   - filterMerchantAccountType | string | No | Shows how merchant accounts are included in company-level webhooks. Possible values:  - **includeAccounts**  - **excludeAccounts**  - **allAccounts**: Includes all merchant accounts, and does not require specifying `filterMerchantAccounts`. |
|   - filterMerchantAccounts | array of string | No | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for `filterMerchantAccountType`.  Required if `filterMerchantAccountType` is either:  - **includeAccounts**  - **excludeAccounts**  Not needed for `filterMerchantAccountType`: **allAccounts**. |
|   - hasError | boolean | No | Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/%7BcompanyId%7D/webhooks/%7Bwebhookid%7D/test). |
|   - hasPassword | boolean | No | Indicates if the webhook is password protected. |
|   - hmacKeyCheckValue | string | No | The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook. |
|   - id | string | No | Unique identifier for this webhook. |
|   - networkType | string | No | Network type for Terminal API details webhooks. |
|   - populateSoapActionHeader | boolean | No | Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if `communicationFormat`: **soap**. |
|   - type | string | Yes | The type of webhook. Possible values are:  - **standard**  - **account-settings-notification**  - **banktransfer-notification**  - **boletobancario-notification**  - **directdebit-notification**  - **ach-notification-of-change-notification**  - **direct-debit-notice-of-change-notification**  - **pending-notification**  - **ideal-notification**  - **ideal-pending-notification**  - **report-notification**  - **terminal-api-notification**  - **terminal-settings**  - **terminal-boarding**  Find out more about [standard webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes) and [other types of webhooks](https://docs.adyen.com/development-resources/webhooks/webhook-types/#other-webhooks). |
|   - url | string | Yes | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |
|   - username | string | No | Username to access the webhook URL. |
| itemsTotal | integer | Yes | Total number of items. |
| pagesTotal | integer | Yes | Total number of pages. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |

## Response examples

### 200 Success

**get-company-webhooks**
```json
{
  "_links": {
    "first": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks?pageNumber=1&pageSize=10"
    },
    "last": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks?pageNumber=1&pageSize=10"
    },
    "self": {
      "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks?pageNumber=1&pageSize=10"
    }
  },
  "itemsTotal": 1,
  "pagesTotal": 1,
  "data": [
    {
      "id": "S2-4A3B33202A46",
      "type": "standard",
      "url": "YOUR_WEBHOOK_URL",
      "description": "Webhook for YOUR_COMPANY_ACCOUNT - YOUR_COMPANY_CODE",
      "filterMerchantAccountType": "allAccounts",
      "username": "adyen",
      "hasPassword": true,
      "active": true,
      "hasError": false,
      "communicationFormat": "json",
      "acceptsExpiredCertificate": false,
      "acceptsSelfSignedCertificate": false,
      "acceptsUntrustedRootCertificate": false,
      "populateSoapActionHeader": false,
      "additionalSettings": {
        "properties": {
          "includePosTerminalInfo": false,
          "includeARN": false,
          "includePosDetails": false,
          "includeCardInfoForRecurringContractNotification": false,
          "includeRiskData": false,
          "includeRiskExperimentReference": false,
          "includeSoapSecurityHeader": false,
          "includeContactlessWalletTokenInformation": false,
          "includeAcquirerReference": false,
          "includeRiskProfileReference": false,
          "includeOriginalMerchantReferenceCancelOrRefundNotification": false,
          "includeNfcTokenInformation": false,
          "includeSubvariant": false,
          "includeThreeDSVersion": false,
          "includeInstallmentsInfo": false,
          "includeAliasInfo": false,
          "includeShopperCountry": false,
          "includeRawThreeDSecureResult": false,
          "includeAirlineData": false,
          "includeGrossCurrencyChargebackDetails": false,
          "includeThreeDSecureResult": false,
          "includeMetadataIn3DSecurePaymentNotification": false,
          "includeOriginalReferenceForChargebackReversed": false,
          "addAcquirerResult": false,
          "includeDeliveryAddress": false,
          "includeRetryAttempts": false,
          "includeExtraCosts": false,
          "includeCardHolderName": false,
          "includeShopperDetail": false,
          "includeBankAccountDetails": false,
          "includeMandateDetails": false,
          "includeAuthAmountForDynamicZeroAuth": false,
          "includeIssuerCountry": false,
          "includeAcquirerErrorDetails": false,
          "includeCoBrandedWith": false,
          "includeShopperInteraction": false,
          "includeDeviceAndBrowserInfo": false,
          "addRawAcquirerResult": false,
          "includeCardBin": false,
          "includeFundingSource": false,
          "includeThreeDS2ChallengeInformation": false,
          "includeRiskProfile": false,
          "includeRealtimeAccountUpdaterStatus": false,
          "includeDunningProjectData": false,
          "includePaymentResultInOrderClosedNotification": false,
          "includeCardBinDetails": false,
          "includeNotesInManualReviewNotifications": false,
          "includeZeroAuthFlag": false,
          "addCaptureReferenceToDisputeNotification": false,
          "includePayPalDetails": false,
          "includeRawThreeDSecureDetailsResult": false,
          "includeBankVerificationResults": false,
          "includeCaptureDelayHours": false,
          "addPaymentAccountReference": false,
          "includePayULatamDetails": false,
          "includeStore": false,
          "returnAvsData": false,
          "includeWeChatPayOpenid": false,
          "includeUpiVpa": false,
          "includeUpiMetadata": false,
          "includeCustomRoutingFlagging": false,
          "includeTokenisedPaymentMetaData": false
        }
      },
      "_links": {
        "self": {
          "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks/S2-4A3B33202A46"
        },
        "company": {
          "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT"
        },
        "generateHmac": {
          "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks/S2-4A3B33202A46/generateHmac"
        },
        "testWebhook": {
          "href": "https://management-test.adyen.com/v1/companies/YOUR_COMPANY_ACCOUNT/webhooks/S2-4A3B33202A46/test"
        }
      }
    }
  ]
}
```