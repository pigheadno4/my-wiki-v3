# PATCH /grants/{grantId}/disbursements/{disbursementId} - Update the repayment configuration of a disbursement

Update the percentage of your user's net income that is deducted for repaying the grant.

## Servers

**Test Environment**
- https://balanceplatform-api-test.adyen.com/capital/v1

**Live Environment**
- https://balanceplatform-api-live.adyen.com/capital/v1

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| disbursementId | string | Yes | The unique identifier of the disbursement. |
| grantId | string | Yes | The unique identifier of the grant reference. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| repayment | object | No | Contains information about the basis points configured for repaying the disbursement. |
|   - basisPoints | integer | No | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
|   - updateDescription | string | No |  |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolderId | string | Yes | The unique identifier of the account holder that received the disbursement. |
| amount | object | Yes | Contains information about the amount of the disbursement. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| balanceAccountId | string | Yes | The unique identifier of the balance account that received the disbursement. |
| balances | object | Yes | Contains information about the balances of the disbursement. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|   - fee | integer | Yes | The amount of the grant fee. |
|   - principal | integer | Yes | The grant amount that is paid out to the user for business financing. |
|   - total | integer | Yes | The total amount of the grant that the user must repay. It is the sum of the fee amount and the principal amount. |
| fee | object | Yes | Contains information about the fee that your user must pay for the disbursement. |
|   - amount | object | Yes | Contains the amount of the grant fee. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|     - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| fundsCollections | array of object | No | Contains information about the accounts that Adyen uses to collect funds related to repayments. |
|   - accountIdentification | object | No | Contains the identification information of the account to which you can transfer funds related to repayments. |
|     - type | string | No | The type of account, which depends on the country of the account and the currency of the transfer. |
|   - fundsCollectionType | string | No | The type of funds collection.  Possible values: **UnscheduledRepayment**, **Revocation**. |
| grantId | string | Yes | The unique identifier of the grant related to the disbursement. |
| id | string | Yes | The unique identifier of the disbursement. |
| repayment | object | Yes | Contains information about the basis points configured for repaying the disbursement. |
|   - basisPoints | integer | Yes | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
|   - updateDescription | string | Yes |  |


### 404 Client Error
The entity was not found.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | No | Unique business error code. |
| instance | string | No | A URI that identifies the specific occurrence of the problem if applicable. |
| invalidFields | array of object | No | Array of fields with validation errors when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | The unique reference for the request. |
| status | integer | No | The HTTP status code. |
| title | string | No | A short, human-readable summary of the problem type. |
| type | string | No | A URI that identifies the validation error type. It points to human-readable documentation for the problem type. |
