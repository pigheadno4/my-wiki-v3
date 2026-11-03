# POST /calculateTax - Calculate the tax for a transaction.

Calculates the applicable tax, for example the India Liberalised Remittance Scheme Tax Collected at Source, based on the taxable amount and the tax calculation context. The response returns the canonical calculation and an opaque token that you submit in /payments. Use taxCalculation.totalAmount as the amount in /payments.

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantAccount | string | Yes | The merchant account identifier requesting the tax calculation. |
| taxCalculationContext | object | Yes | The context used to calculate the tax. |
|   - calculationType | string | Yes | The type of calculation requested. Initially only LRS_TCS is supported. |
|   - lrs | object | Yes | India-specific LRS declarations. |
|     - remittancePurpose | string | Yes | The remittance category, for example TOUR_PROGRAMME or EDUCATION. |
|     - sublimitStatus | string | Yes | The status of the INR 1 million LRS sublimit, for example EXCEEDED. |
|   - taxCountryCode | string | Yes | The country governing tax processing. Initially only IN is supported. |
| taxableAmount | object | Yes | The amount on which Adyen calculates the tax. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|   - value | integer | Yes | The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| taxCalculation | object | No | The canonical calculation accepted and produced by Adyen. Informational in the initial release. |
|   - merchantAccount | string | No | The merchant account for which the calculation was made. |
|   - taxCalculationContext | object | No | The tax country, calculation type, and LRS declarations accepted by Adyen. |
|     - calculationType | string | Yes | The type of calculation requested. Initially only LRS_TCS is supported. |
|     - lrs | object | Yes | India-specific LRS declarations. |
|     - taxCountryCode | string | Yes | The country governing tax processing. Initially only IN is supported. |
|   - taxCalculations | array of object | No | The individual tax components calculated by Adyen. |
|     - taxAmount | object | No | The calculated tax amount of this component. |
|     - type | string | No | The type of the calculated tax component, for example LRS_TCS. |
|   - taxableAmount | object | No | The taxable amount accepted by Adyen. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|     - value | integer | Yes | The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - totalAmount | object | No | The taxable amount plus the calculated tax. Use this amount in /payments.amount. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|     - value | integer | Yes | The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - totalTaxAmount | object | No | The total tax amount calculated by Adyen. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|     - value | integer | Yes | The amount in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| taxCalculationReference | string | No | The unique reference for this calculation attempt. |
| taxCalculationToken | string | No | The opaque, encrypted, and signed token that represents the complete canonical calculation. Required in /payments. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | Yes |  |
| errorType | string | Yes |  |
| message | string | Yes |  |
| pspReference | string | No |  |
| status | integer | No |  |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | Yes |  |
| errorType | string | Yes |  |
| message | string | Yes |  |
| pspReference | string | No |  |
| status | integer | No |  |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | Yes |  |
| errorType | string | Yes |  |
| message | string | Yes |  |
| pspReference | string | No |  |
| status | integer | No |  |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | Yes |  |
| errorType | string | Yes |  |
| message | string | Yes |  |
| pspReference | string | No |  |
| status | integer | No |  |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| errorCode | string | Yes |  |
| errorType | string | Yes |  |
| message | string | Yes |  |
| pspReference | string | No |  |
| status | integer | No |  |
