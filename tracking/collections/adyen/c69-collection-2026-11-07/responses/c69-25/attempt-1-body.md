# GET /balanceOverview/merchants/{merchantAccountCode}/balances - View all balances available for your merchant account.

Returns an overview of the different balances available for the merchant account. This includes details about the following:

**Available funds**: The funds in the merchant account that have been settled and are available for use.

**Pending balance**: The funds in the merchant account that have not been settled yet.

**Next payout amount**: The amount that will be settled to your bank account with the next payout.

**Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that cannot be covered by your in-process funds.

**Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

## Servers

**Test Environment**
- https://balance-control-test.adyen.com/balance-control/api/v2

**Live Environment**
- https://balance-control-live.adyen.com/balance-control/api/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantAccountCode | string | Yes | The unique identifier of your merchant account. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| currency | string | Yes | The currency for which you want a balances overview. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| availableFund | object | No |  |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| deposit | object | No |  |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| merchantAccount | string | No |  |
| nextPayout | object | No |  |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| pendingBalance | object | No |  |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| reserve | object | No |  |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |


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


### 403 Client Error
Insufficient permissions to process the request.

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

## Response examples

### 200 Success

**Response code 200: balances overview for merchant account**
```text
{
    "merchantBalancesOverview": [
        {
            "merchantAccount": "MERCHANT_ACCOUNT_1",
            "availableFund": {
                "value": 3191,
                "currency": "EUR"
            },
            "pendingBalance": {
                "value": -112845,
                "currency": "EUR"
            },
            "nextPayout": {
                "value": 3191,
                "currency": "EUR"
            },
            "reserve": {
                "value": 0,
                "currency": "EUR"
            }
        },
        {
            "merchantAccount": "MERCHANT_ACCOUNT_2",
            "availableFund": {
                "value": 0,
                "currency": "USD"
            },
            "reserve": {
                "value": 0,
                "currency": "USD"
            },
            "deposit": {
                "value": 50000,
                "currency": "USD"
            }
        }
    }
}

```