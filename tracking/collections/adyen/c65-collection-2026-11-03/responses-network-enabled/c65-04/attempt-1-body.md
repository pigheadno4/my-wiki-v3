# DELETE /transactionRules/{transactionRuleId} - Delete a transaction rule

Deletes a transaction rule.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| transactionRuleId | string | Yes | The unique identifier of the transaction rule. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| aggregationLevel | string | No | The level at which data must be accumulated, used in rules with `type` **velocity** or **maxUsage**. The level must be the [same or lower in hierarchy](https://docs.adyen.com/issuing/transaction-rules#accumulate-data) than the `entityKey`.  If not provided, by default, the rule will accumulate data at the **paymentInstrument** level.  Possible values: **paymentInstrument**, **paymentInstrumentGroup**, **balanceAccount**, **accountHolder**, **balancePlatform**. |
| description | string | Yes | Your description for the transaction rule. |
| endDate | string | No | The date when the rule will stop being evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.  If not provided, the rule will be evaluated until the rule status is set to **inactive**. |
| entityKey | object | Yes | The type and unique identifier of the resource to which the rule applies. |
|   - entityReference | string | No | The unique identifier of the resource. |
|   - entityType | string | No | The type of resource.  Possible values: **balancePlatform**, **paymentInstrumentGroup**, **accountHolder**, **balanceAccount**, or **paymentInstrument**. |
| id | string | No | The unique identifier of the transaction rule. |
| interval | object | Yes | The [time interval](https://docs.adyen.com/issuing/transaction-rules#time-intervals) when the rule conditions apply. |
|   - dayOfMonth | integer | No | The day of month, used when the `duration.unit` is **months**. If not provided, by default, this is set to **1**, the first day of the month. |
|   - dayOfWeek | string | No | The day of week, used when the `duration.unit` is **weeks**. If not provided, by default, this is set to **monday**.  Possible values: **sunday**, **monday**, **tuesday**, **wednesday**, **thursday**, **friday**. |
|   - duration | object | No | The duration, which you can specify in hours, days, weeks, or months. The maximum duration is 90 days or an equivalent in other units. Required when the `type` is **rolling** or **sliding**. |
|     - unit | string | No | The unit of time. You can only use **minutes** and **hours** if the `interval.type` is **sliding**.  Possible values: **minutes**, **hours**, **days**, **weeks**, or **months** |
|     - value | integer | No | The length of time by the unit. For example, 5 days.  The maximum duration is 90 days or an equivalent in other units. For example, 3 months. |
|   - timeOfDay | string | No | The time of day, in **hh:mm:ss** format, used when the `duration.unit` is **hours**. If not provided, by default, this is set to **00:00:00**. |
|   - timeZone | string | No | The [time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For example, **Europe/Amsterdam**. By default, this is set to **UTC**. |
|   - type | string | Yes | The [type of interval](https://docs.adyen.com/issuing/transaction-rules#time-intervals) during which the rule conditions and limits apply, and how often counters are reset.  Possible values:  - **perTransaction**: conditions are evaluated and the counters are reset for every transaction.  - **daily**: the counters are reset daily at 00:00:00 CET.  - **weekly**: the counters are reset every Monday at 00:00:00 CET.  - **monthly**: the counters reset every first day of the month at 00:00:00 CET.  - **lifetime**: conditions are applied to the lifetime of the payment instrument.  - **rolling**: conditions are applied and the counters are reset based on a `duration`. If the reset date and time are not provided, Adyen applies the default reset time similar to fixed intervals. For example, if the duration is every two weeks, the counter resets every third Monday at 00:00:00 CET.  - **sliding**: conditions are applied and the counters are reset based on the current time and a `duration` that you specify. |
| outcomeType | string | No | The [outcome](https://docs.adyen.com/issuing/transaction-rules#outcome) that will be applied when a transaction meets the conditions of the rule.  Possible values:  **hardBlock** (default): the transaction is declined.  **scoreBased**: the transaction is assigned the `score` you specified. Adyen calculates the total score and if it exceeds 100, the transaction is declined. This value is not allowed when `requestType` is **bankTransfer**.  **enforceSCA**: your user is prompted to verify their identity using [3D Secure authentication](https://docs.adyen.com/issuing/3d-secure/). If the authentication fails or times out, the transaction is declined. This value is only allowed when `requestType` is **authentication**. |
| overridesRule | string | No | The `id` of the transaction rule you want to override or skip for the specified `entityKey`. |
| purpose | string | No | Specifies the reason for creating the rule.  Possible values:  - **fraud**: the rule is created to regulate fraudulent activity.  - **policy**: the rule is created to ensure that the transaction adheres to your business' policies. For example, if your business has policies about the Merchant Category Codes (MCCs) allowed on a transaction, you can create a rule to block transactions that have specific MCCs. |
| reference | string | Yes | Your reference for the transaction rule. |
| requestType | string | No | Indicates the type of request to which the rule applies. If not provided, by default, this is set to **authorization**.  Possible values: **authorization**, **authentication**, **tokenization**, **bankTransfer**. |
| ruleRestrictions | object | Yes | Contains one or more objects that define the [rule conditions](https://docs.adyen.com/issuing/transaction-rules#conditions). Each object must have a value and an operation which determines how the values must be evaluated.  For example, a `countries` object can have a list of country codes **["US", "CA"]** in the `value` field and **anyMatch** in the `operation` field. |
|   - activeNetworkTokens | object | No | The total number of tokens that a card can have across different kinds of digital wallets on the user's phones, watches, or other wearables.  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | integer | No | The number of tokens. |
|   - brandVariants | object | No | List of card brand variants and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of card brand variants.  Possible values:  **mc**, **mccredit**, **mccommercialcredit_b2b**, **mcdebit**, **mcbusinessdebit**, **mcbusinessworlddebit**, **mcprepaid**, **mcmaestro**  **visa**, **visacredit**, **visadebit**, **visaprepaid**.  You can specify a rule for a generic variant. For example, to create a rule for all Mastercard payment instruments, use **mc**. The rule is applied to all payment instruments under **mc**, such as **mcbusinessdebit** and **mcdebit**. |
|   - counterpartyBank | object | No | Contains a list of counterparty financial institutions and how they must be evaluated.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of object | No | The list of counterparty bank institutions to be evaluated. |
|   - counterpartyTypes | object | No | Contains a list of counterparty types and how they must be evaluated.  Supported operations: **anyMatch**, **noneMatch**.  Supported value inputs:  - **balanceAccount**  - **bankAccount**  - **card**  - **transferInstrument** |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | The list of counterparty types to be evaluated. |
|   - countries | object | No | List of countries and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. |
|   - dayOfWeek | object | No | List of week days and the operation. Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of days of the week.  Possible values: **monday**, **tuesday**, **wednesday**, **thursday**, **friday**, **saturday**, **sunday**. |
|   - differentCurrencies | object | No | Compares the currency of the payment against the currency of the payment instrument, and specifies the operation.  Supported operations: **equals**, **notEquals**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | boolean | No | Checks the currency of the payment against the currency of the payment instrument.  Possible values:  **true**: The currency of the payment is different from the currency of the payment instrument.  **false**: The currencies are the same. |
|   - entryModes | object | No | List of point-of-sale entry modes and the operation..  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of point-of-sale entry modes.  Possible values: **barcode**, **chip**, **cof**, **contactless**, **magstripe**, **manual**, **ocr**, **server**. |
|   - internationalTransaction | object | No | Indicates whether transaction is an international transaction and specifies the operation.  Supported operations: **equals**, **notEquals**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | boolean | No | Boolean indicating whether transaction is an international transaction.  Possible values:  **true**: The transaction is an international transaction.  **false**: The transaction is a domestic transaction. |
|   - matchingTransactions | object | No | The number of transactions and the operation.  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | integer | No | The number of transactions. |
|   - matchingValues | object | No | Checks if a user has recently made multiple transfers with the specified values.  To use this restriction, you must:  Set the rule `type` to **velocity**.  Specify a time `interval`.  Specify a number of `matchingTransactions`.  Supported operation: **allMatch**.  Supported value inputs:  - **merchantId** and **acquirerId**  - **amount** and **currency**  - **merchantName**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No |  |
|   - mccs | object | No | List of merchant category codes (MCCs) and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of merchant category codes (MCCs). |
|   - merchantNames | object | No | List of names that will be compared to the merchant name according to the matching type.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of object | No |  |
|   - merchants | object | No | List of merchant ID and acquirer ID pairs, and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of object | No | List of merchant ID and acquirer ID pairs. |
|   - processingTypes | object | No | List of processing types and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | List of processing types.  Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **recurring**, **token**. |
|   - riskScores | object | No | Risk scores provided by specific sources. The same operation applies to all scores.  Current sources available: **visa**, **mastercard**  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | object | No |  |
|   - sameAmountRestriction | object | No | Checks if a user has recently sent the same amount of funds in multiple transfers.  To use this restriction, you must:  Set the rule `type` to **velocity**.  Specify a time `interval`.  Specify a number of `matchingTransactions`.  Supported operation: **equals**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | boolean | No |  |
|   - sameCounterpartyRestriction | object | No | Checks if a user has recently made multiple transfers to the same counterparty.  To use this restriction, you must:  Set the rule `type` to **velocity**.  Specify a time `interval`.  Specify a number of `matchingTransactions`.  Supported operations: **equals**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | boolean | No |  |
|   - sourceAccountTypes | object | No | Contains a list of source account types and how they must be evaluated.  Supported operations: **anyMatch**, **noneMatch**.  Supported value inputs:  - **balanceAccount**  - **businessAccount**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No | The list of source account types to be evaluated. |
|   - timeOfDay | object | No | A start and end time in a time-only ISO-8601 extended offset format. Supported operations: **equals**, **notEquals**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | object | No |  |
|   - tokenRequestors | object | No | List of token requestor IDs and the operation.  Supported operations: **anyMatch**, **noneMatch**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No |  |
|   - totalAmount | object | No | The total amount and the operation.  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | object | No | The amount value and currency. |
|   - walletProviderAccountScore | object | No | Checks the wallet account score.  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | integer | No |  |
|   - walletProviderDeviceScore | object | No | Wallet Provider Device Score and the operation.  Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**. |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | integer | No |  |
|   - walletProviderDeviceType | object | No | Wallet Provider Device Type and the operation.  Supported operations: **anyMatch**, **noneMatch**.  Supported value inputs:  **MOBILE_PHONE**  **TABLET_OR_EREADER**  **WATCH_OR_WRISTBAND**  **WEARABLE**  **CARD**  **PC**  **OTHER**  **UNKNOWN** |
|     - operation | string | Yes | Defines how the condition must be evaluated. |
|     - value | array of string | No |  |
| score | integer | No | A positive or negative score applied to the transaction if it meets the conditions of the rule. Required when `outcomeType` is **scoreBased**.  The value must be between **-100** and **100**. |
| startDate | string | No | The date when the rule will start to be evaluated, in ISO 8601 extended offset date-time format. For example, **2025-03-19T10:15:30+01:00**.  If not provided when creating a transaction rule, the `startDate` is set to the date when the rule status is set to **active**. |
| status | string | No | The status of the transaction rule. If you provide a `startDate` in the request, the rule is automatically created with an **active** status.  Possible values: **active**, **inactive**. |
| type | string | Yes | The [type of rule](https://docs.adyen.com/issuing/transaction-rules#rule-types), which defines if a rule blocks transactions based on individual characteristics or accumulates data.  Possible values:  - **blockList**: decline a transaction when the conditions are met.  - **maxUsage**: add the amount or number of transactions for the lifetime of a payment instrument, and then decline a transaction when the specified limits are met.  - **velocity**: add the amount or number of transactions based on a specified time interval, and then decline a transaction when the specified limits are met.  - **bypass**: bypass or skip a rule for the specified `entityKey`. Transactions processed to that entity are no longer evaluated by the bypassed rule.  You must provide the `id` of the rule to bypass in `overridesRule` and leave the `ruleRestrictions` object empty. |


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

**success**
```json
{
  "aggregationLevel": "paymentInstrument",
  "description": "Up to 1000 EUR per card for the last 12 hours",
  "entityKey": {
    "entityReference": "PG3227C223222C5GXR3M5592Q",
    "entityType": "paymentInstrumentGroup"
  },
  "interval": {
    "duration": {
      "unit": "hours",
      "value": 12
    },
    "timeZone": "UTC",
    "type": "sliding"
  },
  "outcomeType": "hardBlock",
  "reference": "myRule12345",
  "requestType": "authorization",
  "ruleRestrictions": {
    "totalAmount": {
      "operation": "greaterThan",
      "value": {
        "currency": "EUR",
        "value": 100000
      }
    }
  },
  "type": "velocity",
  "id": "TR3227C223222C5GXT3DD5VCF"
}
```

### 400 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/bad-request",
  "title": "Bad request",
  "status": 400,
  "detail": "Empty input which would have resulted in a null result.",
  "errorCode": "00_400"
}
```

### 401 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/security/unauthorized",
  "title": "Unauthorized",
  "status": 401,
  "detail": "Not authorized to access this service.",
  "errorCode": "00_401"
}
```

### 403 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/security/unauthorized",
  "title": "Forbidden",
  "status": 403,
  "detail": "Not the right permission to access this service.",
  "errorCode": "00_403"
}
```

### 422 Client Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/invalid-field-value",
  "title": "Invalid Payment Instrument information provided",
  "status": 422,
  "detail": "The balanceAccountId can only be changed when the status is Inactive or Requested",
  "requestId": "1W1UI15PLVGC9V8O",
  "errorCode": "30_031"
}
```

### 500 Server Error

**generic**
```json
{
  "type": "https://docs.adyen.com/errors/general/internal",
  "title": "An internal error happened",
  "status": 500,
  "detail": "Unrecoverable error while trying to create payment instrument",
  "requestId": "1WAF555PLWNTLYOQ",
  "errorCode": "00_500"
}
```