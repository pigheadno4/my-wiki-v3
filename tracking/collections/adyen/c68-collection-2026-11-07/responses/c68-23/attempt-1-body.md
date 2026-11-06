# POST /merchants/{merchantId}/splitConfigurations - Create a split configuration profile

Creates a split configuration profile to [split payments automatically](https://docs.adyen.com/platforms/automatic-split-configuration/). After you [associate it with a store](https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)#request-splitConfiguration) in your merchant account, it splits the funds of all transactions processed through that store between your liable balance account and [your user's balance account](https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(storeId)#request-splitConfiguration-balanceAccountId).

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

- Management API - SplitConfiguration read and write

## Servers
- https://management-test.adyen.com/v3

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantId | string | Yes | The unique identifier of the merchant account. |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| description | string | Yes | Your description for the split configuration. |
| rules | array of object | Yes | Array of rules that define the split configuration behavior. |
|   - cardRegion | string | No | The card region condition that determines whether the [split logic](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic) applies to the transaction.  Possible values:  - **domestic**: The card issuer and the store where the transaction is processed are registered in the same country.  - **international**: The card issuer and the store where the transaction is processed are registered in different countries or regions. Includes all **interRegional** and **intraRegional** transactions.  - **interRegional**: The card issuer and the store where the transaction is processed are registered in different regions.  - **intraRegional**: The card issuer and the store where the transaction is processed are registered in different countries, but in the same region.  - **intraEEA**: The card issuer and the store where the transaction is processed are registered in different countries, but in the European Economic Area (EEA).  - **ANY**: Applies to all transactions, regardless of the processing and issuing country/region. |
|   - cardUsageType | string | No | The card usage type condition that determines whether the split logic applies to commercial cards, consumer cards, or all cards.  - **ANY** (default): The split logic applies to all cards, regardless of its usage type.  - **commercial**: The split logic applies to commercial cards only.  - **consumer**: The split logic applies to consumer cards only. |
|   - currency | string | Yes | The currency condition that defines whether the split logic applies. Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
|   - fundingSource | string | Yes | The funding source of the payment method.  Possible values:  - **credit**  - **debit**  - **prepaid**  - **deferred_debit**  - **charged**  - **ANY** |
|   - paymentMethod | string | Yes | The payment method condition that defines whether the split logic applies.  Possible values:  - [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method.  - **ANY**: Apply the split logic for all available payment methods. |
|   - shopperInteraction | string | Yes | The sales channel condition that defines whether the split logic applies.  Possible values:  - **Ecommerce**: Online transactions where the cardholder is present.  - **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).  - **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.  - **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.  - **ANY**: All sales channels. |
|   - splitLogic | object | Yes | Contains the split logic that is applied if the rule conditions are met. |
|     - acquiringFees | string | No | Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - additionalCommission | object | No | Defines whether to book an additional commission for payments to your user's balance account. The commission amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. |
|     - adyenCommission | string | No | Deducts the transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - adyenFees | string | No | Deducts the fees due to Adyen (markup or commission) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - adyenMarkup | string | No | Deducts the transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/what-is-interchange) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - chargeback | string | No | Specifies how and from which balance account(s) to deduct the chargeback amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |
|     - chargebackCostAllocation | string | No | Deducts the chargeback costs from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
|     - commission | object | Yes | Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account. |
|     - dcc | object | No | Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).  This field is in pilot phase, and not yet available for all platforms. |
|     - interchange | string | No | Deducts the interchange fee from specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - paymentFee | string | No | Deducts all transaction fees incurred by the payment from the specified balance account. The transaction fees include the acquiring fees (interchange and scheme fee), and the fees due to Adyen (markup or commission). You can book any and all these fees to different balance account by specifying other transaction fee parameters in your split configuration profile:  - [`adyenCommission`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenCommission): The transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).  - [`adyenMarkup`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenMarkup): The transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).  - [`schemeFee`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-schemeFee): The fee paid to the card scheme for using their network.  - [`interchange`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-interchange): The fee paid to the issuer for each payment transaction made with the card network.  - [`adyenFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenFees): The aggregated amount of Adyen's commission and markup.  - [`acquiringFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-acquiringFees): The aggregated amount of the interchange and scheme fees.  If you don't include at least one transaction fee type in the `splitLogic` object, Adyen updates the payment request with the `paymentFee` parameter, booking all transaction fees to your platform's liable balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - refund | string | No | Specifies how and from which balance account(s) to deduct the refund amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio** |
|     - refundCostAllocation | string | No | Deducts the refund costs from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
|     - remainder | string | No | Books the amount left over after currency conversion to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |
|     - schemeFee | string | No | Deducts the scheme fee from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - surcharge | string | No | Books the surcharge amount to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount** |
|     - tip | string | No | Books the tips (gratuity) to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |

## Request examples

### post-splitConfiguration
```json
{
  "description": "Your description for the split configuration",
  "rules": [
    {
      "paymentMethod": "ANY",
      "shopperInteraction": "ANY",
      "fundingSource": "ANY",
      "currency": "ANY",
      "splitLogic": {
        "paymentFee": "deductFromLiableAccount",
        "chargeback": "deductFromLiableAccount",
        "tip": "addToOneBalanceAccount",
        "remainder": "addToOneBalanceAccount",
        "commission": {
          "fixedAmount": 10,
          "variablePercentage": 100
        },
        "additionalCommission": {
          "fixedAmount": 10,
          "variablePercentage": 50,
          "balanceAccountId": "BA3227C223222H5HQ2XX77VVH"
        }
      }
    }
  ]
}
```
## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| description | string | Yes | Your description for the split configuration. |
| rules | array of object | Yes | Array of rules that define the split configuration behavior. |
|   - cardRegion | string | No | The card region condition that determines whether the [split logic](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic) applies to the transaction.  Possible values:  - **domestic**: The card issuer and the store where the transaction is processed are registered in the same country.  - **international**: The card issuer and the store where the transaction is processed are registered in different countries or regions. Includes all **interRegional** and **intraRegional** transactions.  - **interRegional**: The card issuer and the store where the transaction is processed are registered in different regions.  - **intraRegional**: The card issuer and the store where the transaction is processed are registered in different countries, but in the same region.  - **intraEEA**: The card issuer and the store where the transaction is processed are registered in different countries, but in the European Economic Area (EEA).  - **ANY**: Applies to all transactions, regardless of the processing and issuing country/region. |
|   - cardUsageType | string | No | The card usage type condition that determines whether the split logic applies to commercial cards, consumer cards, or all cards.  - **ANY** (default): The split logic applies to all cards, regardless of its usage type.  - **commercial**: The split logic applies to commercial cards only.  - **consumer**: The split logic applies to consumer cards only. |
|   - currency | string | Yes | The currency condition that defines whether the split logic applies. Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
|   - fundingSource | string | Yes | The funding source of the payment method.  Possible values:  - **credit**  - **debit**  - **prepaid**  - **deferred_debit**  - **charged**  - **ANY** |
|   - paymentMethod | string | Yes | The payment method condition that defines whether the split logic applies.  Possible values:  - [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method.  - **ANY**: Apply the split logic for all available payment methods. |
|   - ruleId | string | No | The unique identifier of the split configuration rule. |
|   - shopperInteraction | string | Yes | The sales channel condition that defines whether the split logic applies.  Possible values:  - **Ecommerce**: Online transactions where the cardholder is present.  - **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).  - **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.  - **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.  - **ANY**: All sales channels. |
|   - splitLogic | object | Yes | Contains the split logic that is applied if the rule conditions are met. |
|     - acquiringFees | string | No | Deducts the acquiring fees (the aggregated amount of interchange and scheme fee) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - additionalCommission | object | No | Defines whether to book an additional commission for payments to your user's balance account. The commission amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. |
|     - adyenCommission | string | No | Deducts the transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - adyenFees | string | No | Deducts the fees due to Adyen (markup or commission) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - adyenMarkup | string | No | Deducts the transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/what-is-interchange) from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - chargeback | string | No | Specifies how and from which balance account(s) to deduct the chargeback amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |
|     - chargebackCostAllocation | string | No | Deducts the chargeback costs from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
|     - commission | object | Yes | Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account. |
|     - dcc | object | No | Defines the logic for booking the markup paid by the customer for Dynamic Currency Conversion (DCC).  This field is in pilot phase, and not yet available for all platforms. |
|     - interchange | string | No | Deducts the interchange fee from specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - paymentFee | string | No | Deducts all transaction fees incurred by the payment from the specified balance account. The transaction fees include the acquiring fees (interchange and scheme fee), and the fees due to Adyen (markup or commission). You can book any and all these fees to different balance account by specifying other transaction fee parameters in your split configuration profile:  - [`adyenCommission`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenCommission): The transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).  - [`adyenMarkup`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenMarkup): The transaction fee due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained#interchange-vs-blended).  - [`schemeFee`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-schemeFee): The fee paid to the card scheme for using their network.  - [`interchange`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-interchange): The fee paid to the issuer for each payment transaction made with the card network.  - [`adyenFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-adyenFees): The aggregated amount of Adyen's commission and markup.  - [`acquiringFees`](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic-acquiringFees): The aggregated amount of the interchange and scheme fees.  If you don't include at least one transaction fee type in the `splitLogic` object, Adyen updates the payment request with the `paymentFee` parameter, booking all transaction fees to your platform's liable balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - refund | string | No | Specifies how and from which balance account(s) to deduct the refund amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio** |
|     - refundCostAllocation | string | No | Deducts the refund costs from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |
|     - remainder | string | No | Books the amount left over after currency conversion to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |
|     - schemeFee | string | No | Deducts the scheme fee from the specified balance account.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |
|     - splitLogicId | string | No | Unique identifier of the collection of split instructions that are applied when the rule conditions are met. |
|     - surcharge | string | No | Books the surcharge amount to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount** |
|     - tip | string | No | Books the tips (gratuity) to the specified balance account.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |
| splitConfigurationId | string | No | Unique identifier of the split configuration. |


### 204 Success
The request has been successfully processed, but there is no additional content.


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

**post-splitConfiguration**
```json
{
  "description": "Your description for the split configuration",
  "rules": [
    {
      "currency": "ANY",
      "fundingSource": "ANY",
      "paymentMethod": "ANY",
      "ruleId": "SCRL4224P22322585HPCX384JW65VW",
      "shopperInteraction": "ANY",
      "splitLogic": {
        "additionalCommission": {
          "fixedAmount": 10,
          "variablePercentage": 50,
          "balanceAccountId": "BA3227C223222H5HQ2XX77VVH"
        },
        "chargeback": "deductFromLiableAccount",
        "commission": {
          "fixedAmount": 10,
          "variablePercentage": 100
        },
        "splitLogicId": "SCLG4224P22322585HPCX384JX52M2",
        "paymentFee": "deductFromLiableAccount",
        "remainder": "addToOneBalanceAccount",
        "tip": "addToOneBalanceAccount"
      }
    }
  ],
  "splitConfigurationId": "SCNF4224P22322585HPCX384JV6JGX"
}
```