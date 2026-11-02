# POST /payments/{paymentPspReference}/amountUpdates - Update an authorised amount

Increases or decreases the authorised payment amount and returns a unique reference for this request. You get the outcome of the request asynchronously, in an [**AUTHORISATION_ADJUSTMENT** webhook](https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes).

You can only update authorised amounts that have not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/%7BpaymentPspReference%7D/captures).

The amount you specify in the request is the updated amount, which is larger or smaller than the initial authorised amount.

For more information, refer to [Authorisation adjustment](https://docs.adyen.com/online-payments/adjust-authorisation#use-cases).

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment. |


### Header parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| Idempotency-Key | string | No | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| adjustAuthType | string | No | The type of adjustment. Possible values:  **cardholderInitiatedTransaction**  **merchantInitiatedTransaction** |
| adjustAuthorisationData | string | No | The required data to make a [synchronous authorization adjustment](https://docs.adyen.com/online-payments/adjust-authorisation). Pass the corresponding value from the `/payments` response or webhook message. |
| amount | object | Yes | The updated amount. The `currency` must match the currency used in authorisation. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| applicationInfo | object | No | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
|   - adyenLibrary | object | No | Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - adyenPaymentSource | object | No | Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - externalPlatform | object | No | Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc. |
|     - integrator | string | No | External platform integrator. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - merchantApplication | object | No | Merchant developed software, such as cashier application, used to interact with the Adyen API. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - merchantDevice | object | No | Merchant device information. |
|     - os | string | No | Operating system running on the merchant device. |
|     - osVersion | string | No | Version of the operating system on the merchant device. |
|     - reference | string | No | Merchant device reference. |
|   - shopperInteractionDevice | object | No | Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests. |
|     - locale | string | No | Locale on the shopper interaction device. |
|     - os | string | No | Operating system running on the shopper interaction device. |
|     - osVersion | string | No | Version of the operating system on the shopper interaction device. |
| industryUsage | string | No | The reason for the amount update. Possible values:  - **delayedCharge**  - **noShow**  - **installment** |
| lineItems | array of object | No | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).  This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
|   - amountExcludingTax | integer | No | Item amount excluding the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - amountIncludingTax | integer | No | Item amount including the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - brand | string | No | Brand of the item. |
|   - color | string | No | Color of the item. |
|   - description | string | No | Description of the line item. |
|   - id | string | No | ID of the line item. |
|   - imageUrl | string | No | Link to the picture of the purchased item. |
|   - itemCategory | string | No | Item category, used by the payment methods PayPal and Ratepay. |
|   - manufacturer | string | No | Manufacturer of the item. |
|   - marketplaceSellerId | string | No | Marketplace seller id. |
|   - productUrl | string | No | Link to the purchased item. |
|   - quantity | integer | No | Number of items. |
|   - receiverEmail | string | No | Email associated with the given product in the basket (usually in electronic gift cards). |
|   - returnShippingCompany | string | No | Shipping company handling the return of the item. |
|   - returnTrackingNumber | string | No | Tracking number for the return of the item. |
|   - returnTrackingUri | string | No | Tracking URI for the return of the item. |
|   - riskCategory | string | No | An optional, free-text category for the item to be used in the risk evaluation. When provided, Protect uses this value to evaluate custom risk rules. |
|   - shippingCompany | string | No | Shipping company handling the delivery of the item. |
|   - shippingMethod | string | No | Shipping method used to deliver the item. |
|   - size | string | No | Size of the item. |
|   - sku | string | No | Stock keeping unit. |
|   - taxAmount | integer | No | Tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - taxPercentage | integer | No | Tax percentage, represented as a [basis point](https://en.wikipedia.org/wiki/Basis_point) integer. For example:  - **530** for 5.3% (five point three percent)  - **2100** for 21% (twenty-one percent) |
|   - trackingNumber | string | No | Tracking number for the delivery of the item. |
|   - trackingUri | string | No | Tracking URI for the delivery of the item. |
|   - upc | string | No | Universal Product Code. |
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| mpiData | object | No | Authentication data from a [merchant plug-in (MPI)](https://en.wikipedia.org/wiki/Merchant_plug-in) like Mastercard SecureCode, Visa Secure, or Cartes Bancaires. Required for cardholder-initiated transaction (CIT) adjustments. |
|   - authenticationResponse | string | No | In 3D Secure 2, this is the `transStatus` from the challenge result. If the transaction was frictionless, omit this parameter. |
|   - cavv | string | No | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). |
|   - cavvAlgorithm | string | No | The CAVV algorithm used. Include this only for 3D Secure 1. |
|   - challengeCancel | string | No | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). |
|   - directoryResponse | string | No | In 3D Secure 2, this is the `transStatus` from the `ARes`. |
|   - dsTransID | string | No | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. |
|   - eci | string | No | The electronic commerce indicator. |
|   - riskScore | string | No | Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations. |
|   - threeDSVersion | string | No | The version of the 3D Secure protocol. |
|   - tokenAuthenticationVerificationValue | string | No | Network token authentication verification value (TAVV). The network token cryptogram. |
|   - transStatusReason | string | No | Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |
|   - xid | string | No | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). |
| reference | string | No | Your reference for the amount update request. Maximum length: 80 characters. |
| splits | array of object | No | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |
|   - account | string | No | The unique identifier of the account to which the split amount is booked. Required if `type` is **MarketPlace** or **BalanceAccount**.  - [Classic Platforms integration](https://docs.adyen.com/classic-platforms): The [`accountCode`](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked.  - [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model): The [`balanceAccountId`](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. |
|   - amount | object | No | The amount of the split item.  - Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).  - Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration. |
|     - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency. |
|     - value | integer | Yes | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - description | string | No | Your description for the split item. |
|   - reference | string | No | Your unique reference for the part of the payment booked to the specified `account`.  This is required if `type` is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/classic-platforms)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/adyen-for-platforms-model)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. |
|   - type | string | Yes | The part of the payment you want to book to the specified `account`.  Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):  - **BalanceAccount**: Books part of the payment (specified in `amount`) to the specified `account`.  Transaction fees types that you can book to the specified `account`:  - **AcquiringFees**: The aggregated amount of the interchange and scheme fees.  - **PaymentFee**: The aggregated amount of all transaction fees.  - **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.  - **AdyenCommission**: The transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **AdyenMarkup**: The transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **Interchange**: The fees paid to the issuer for each payment made with the card network.  - **SchemeFee**: The fees paid to the card scheme for using their network.  - **Commission**: Your platform's commission on the payment (specified in `amount`), booked to your liable balance account.  - **Remainder**: The amount left over after a currency conversion, booked to the specified `account`.  - **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.  - **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.  - **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.  - **Default**: In very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.  Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**. |

## Request examples

### amount-update
```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "amount": {
    "currency": "EUR",
    "value": 2500
  },
  "reference": "YOUR_UNIQUE_REFERENCE"
}
```
## Responses

### 201 Success
The request has been fulfilled and has resulted in one or more new resources being created.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| adjustAuthorisationData | string | No | The data blob for subsequent synchronous adjust authorisation calls. Returned when the synchronous flow is used. |
| amount | object | Yes | The updated amount. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| industryUsage | string | No | The reason for the amount update. Possible values:  - **delayedCharge**  - **noShow**  - **installment** |
| lineItems | array of object | No | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).  This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
|   - amountExcludingTax | integer | No | Item amount excluding the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - amountIncludingTax | integer | No | Item amount including the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - brand | string | No | Brand of the item. |
|   - color | string | No | Color of the item. |
|   - description | string | No | Description of the line item. |
|   - id | string | No | ID of the line item. |
|   - imageUrl | string | No | Link to the picture of the purchased item. |
|   - itemCategory | string | No | Item category, used by the payment methods PayPal and Ratepay. |
|   - manufacturer | string | No | Manufacturer of the item. |
|   - marketplaceSellerId | string | No | Marketplace seller id. |
|   - productUrl | string | No | Link to the purchased item. |
|   - quantity | integer | No | Number of items. |
|   - receiverEmail | string | No | Email associated with the given product in the basket (usually in electronic gift cards). |
|   - returnShippingCompany | string | No | Shipping company handling the return of the item. |
|   - returnTrackingNumber | string | No | Tracking number for the return of the item. |
|   - returnTrackingUri | string | No | Tracking URI for the return of the item. |
|   - riskCategory | string | No | An optional, free-text category for the item to be used in the risk evaluation. When provided, Protect uses this value to evaluate custom risk rules. |
|   - shippingCompany | string | No | Shipping company handling the delivery of the item. |
|   - shippingMethod | string | No | Shipping method used to deliver the item. |
|   - size | string | No | Size of the item. |
|   - sku | string | No | Stock keeping unit. |
|   - taxAmount | integer | No | Tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - taxPercentage | integer | No | Tax percentage, represented as a [basis point](https://en.wikipedia.org/wiki/Basis_point) integer. For example:  - **530** for 5.3% (five point three percent)  - **2100** for 21% (twenty-one percent) |
|   - trackingNumber | string | No | Tracking number for the delivery of the item. |
|   - trackingUri | string | No | Tracking URI for the delivery of the item. |
|   - upc | string | No | Universal Product Code. |
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to update. |
| pspReference | string | Yes | Adyen's 16-character reference associated with the amount update request. |
| reference | string | Yes | Your reference for the amount update request. Maximum length: 80 characters. |
| splits | array of object | No | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |
|   - account | string | No | The unique identifier of the account to which the split amount is booked. Required if `type` is **MarketPlace** or **BalanceAccount**.  - [Classic Platforms integration](https://docs.adyen.com/classic-platforms): The [`accountCode`](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked.  - [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model): The [`balanceAccountId`](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. |
|   - amount | object | No | The amount of the split item.  - Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).  - Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration. |
|     - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency. |
|     - value | integer | Yes | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - description | string | No | Your description for the split item. |
|   - reference | string | No | Your unique reference for the part of the payment booked to the specified `account`.  This is required if `type` is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/classic-platforms)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/adyen-for-platforms-model)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. |
|   - type | string | Yes | The part of the payment you want to book to the specified `account`.  Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):  - **BalanceAccount**: Books part of the payment (specified in `amount`) to the specified `account`.  Transaction fees types that you can book to the specified `account`:  - **AcquiringFees**: The aggregated amount of the interchange and scheme fees.  - **PaymentFee**: The aggregated amount of all transaction fees.  - **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.  - **AdyenCommission**: The transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **AdyenMarkup**: The transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **Interchange**: The fees paid to the issuer for each payment made with the card network.  - **SchemeFee**: The fees paid to the card scheme for using their network.  - **Commission**: Your platform's commission on the payment (specified in `amount`), booked to your liable balance account.  - **Remainder**: The amount left over after a currency conversion, booked to the specified `account`.  - **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.  - **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.  - **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.  - **Default**: In very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.  Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**. |
| status | string | Yes | The status of your request.  If you included `adjustAuthorisationData` in your request, possible values are the following:  **authorised**  **refused**  Otherwise, the value is **received**. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
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
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
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
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
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
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
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
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |

## Response examples

### 201 Success

**amount-update**
```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received",
  "amount": {
    "currency": "EUR",
    "value": 2500
  }
}
```

### 400 Client Error

**generic**
```json
{
  "status": 400,
  "errorCode": "702",
  "message": "Unexpected input: \", expected: }",
  "errorType": "validation"
}
```

### 401 Client Error

**generic**
```json
{
  "status": 401,
  "errorCode": "000",
  "message": "HTTP Status Response - Unauthorized",
  "errorType": "security"
}
```

### 403 Client Error

**generic**
```json
{
  "status": 403,
  "errorCode": "901",
  "message": "Invalid Merchant Account",
  "errorType": "security",
  "pspReference": "881611827877203B"
}
```

### 422 Client Error

**generic**
```json
{
  "status": 422,
  "errorCode": "14_030",
  "message": "Return URL is missing.",
  "errorType": "validation",
  "pspReference": "8816118280275544"
}
```

### 500 Server Error

**generic**
```json
{
  "status": 500,
  "errorCode": "905",
  "message": "Payment details are not supported",
  "errorType": "configuration",
  "pspReference": "8516091485743033"
}
```