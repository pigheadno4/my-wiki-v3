# POST /payments/{paymentPspReference}/reversals - Refund or cancel a payment

[Refunds](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/%7BpaymentPspReference%7D/refunds) a payment if it has already been captured, and [cancels](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/%7BpaymentPspReference%7D/cancels) a payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCEL_OR_REFUND** webhook](https://docs.adyen.com/online-payments/reversal/#cancel-or-refund-webhook).

The reversed amount is always the full payment amount.

Do not use this request for payments that involve multiple partial captures.

For more information, refer to [Reversal](https://docs.adyen.com/online-payments/reversal).

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to reverse. |


### Header parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| Idempotency-Key | string | No | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
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
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| reference | string | No | Your reference for the reversal request. Maximum length: 80 characters. |

## Request examples

### reversal
```json
{
  "reference": "YOUR_UNIQUE_REFERENCE",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
}
```
## Responses

### 201 Success
The request has been fulfilled and has resulted in one or more new resources being created.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to reverse. |
| pspReference | string | Yes | Adyen's 16-character reference associated with the reversal request. |
| reference | string | No | Your reference for the reversal request. |
| status | string | Yes | The status of your request. This will always have the value **received**. |


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

**reversal**
```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received"
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