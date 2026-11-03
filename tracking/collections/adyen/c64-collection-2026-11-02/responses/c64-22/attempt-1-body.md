# GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id} - Get a specific managed payout schedule on your balance platform

Returns the specified managed payout schedule configured on your balance platform.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the payout configuration for your balance platform. |
| balancePlatformId | string | Yes | The unique identifier of the balance platform. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| automaticApplication | boolean | No | Specifies whether this payout schedule is automatically applied to new balance accounts. |
| balancePlatformId | string | Yes | The balance platform to which the payout schedule applies. |
| countryCode | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of the country to which the payout schedule applies. |
| createdAt | string | Yes | The date when the payout schedule was created. |
| currency | string | No | The three-character [ISO code](https://docs.adyen.com/development-resources/currency-codes) of the currency used for the payout schedule. |
| defaultDescription | string | No | The default description for payouts initiated by this payout schedule. |
| defaultFrequency | string | No | The default frequency of payouts initiated by this payout schedule. |
| defaultFrequencyValue | integer | No | The default value for date of the month or day of the week when payouts are initiated. Allowed only if `defaultFrequency` is **monthly** or **weekly**.  Possible values if `defaultFrequency` is **monthly**: **[1 - 31]**.  - If your specified date happens on a weekend, the payout is initiated on the next business day.  - If your specified date (**29**, **30**, or **31**) does not exist in a month, the payout is initiated  on the last day of that month.  Possible values if `defaultFrequency` is **weekly**: **[1 - 5]**. |
| defaultReference | string | No | Your internal default reference for the payout schedule.When the payout schedule is applied to a balance account, this reference is also used for that payout schedule. |
| defaultReferenceForBeneficiary | string | No | The default reference for beneficiary for payouts initiated by this payout schedule. |
| enabled | boolean | No | Specifies whether the payout schedule is enabled immediately after it is created. |
| id | string | No | The unique identifier of the payout schedule for your balance platform. |
| maxPayoutAmount | integer | No | The maximum amount that can be paid out from balance accounts that use this payout schedule.  Default value: **0**, which means that there is no maximum limit. |
| minPayoutAmount | integer | No | The minimum amount that can be paid out from balance accounts that use this payout schedule.  Default value: **0**. |
| payoutScheduleDescription | string | Yes | The type of payout schedule. This type indicates how fast funds are paid out to your user.  Possible values:  - **Standard**: The funds arrive in your user's transfer instrument two days after the funds are settled.  - **Accelerated**: The funds arrive to your user's transfer instrument the day after the funds are settled. |
| retainedAmount | integer | No | The amount of funds that must remain available in a balance account after an execution of the payout schedule. If the funds in the balance account are less than the retained amount, the execution is not initiated.  Default value: **0** |
| updatedAt | string | No | The date when the payout schedule was updated. |
| userSettlementDelay | integer | Yes | The default [settlement delay](https://docs.adyen.com/platforms/settle-funds/#settlement-delay) for this payout schedule. |
| userSettlementTime | string | Yes | The time when the payout funds are settled in your user's transfer instrument. For example, 11:30:00. |
| userSettlementTimeZone | string | Yes | The timezone of the `userSettlementTime`. |


### 401 Client Error
Authentication required.

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


### 404 Client Error
The resource was not found

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


### 500 Server Error
The server could not process the request.

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
