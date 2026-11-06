# GET /grantOffers/{id} - Get the details of a static offer

Returns the details of the specified static offer.

## Servers

**Test Environment**
- https://balanceplatform-api-test.adyen.com/capital/v1

**Live Environment**
- https://balanceplatform-api-live.adyen.com/capital/v1

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the static offer. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolderId | string | Yes | The unique identifier of the account holder to which the grant is offered. |
| amount | object | No | The amount that would be paid out to the user for business financing. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| contractType | string | No | The contract type of the offer.  Possible values:  - **loan**  - **cashAdvance** |
| expiresAt | string | No | The expiration date and time of the offer validity period. |
| fee | object | No | Contains information about the fee that your user would pay for the grant. |
|   - amount | object | Yes | Contains the amount of the offer fee. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|     - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
|   - aprBasisPoints | integer | No | Annual Percentage Rate (APR) of the offer. The percentage is expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
| id | string | No | The unique identifier of the offer. |
| repayment | object | No | Contains information about the repayment configuration of the grant. |
|   - basisPoints | integer | Yes | The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp). |
|   - term | object | No | Contains information about the time period in which your user must repay the total amount of the grant. |
|     - estimatedDays | integer | Yes | The estimated duration of the repayment term, in days. |
|     - maximumDays | integer | No | The maximum duration of the repayment term, in days. Only applies when `contractType` is **loan**. |
|   - threshold | object | No | Contains the minimum threshold amount that your user must repay every 30-day period. |
|     - amount | object | Yes | The minimum threshold amount that your user must repay on every 30-day period. |
| startsAt | string | No | The starting date and time of the offer validity period. |


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
