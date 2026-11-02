# GET /sessions/{sessionId} - Get the result of a payment session

Returns the status of the payment session with the `sessionId` and `sessionResult` specified in the path.

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| sessionId | string | Yes | A unique identifier of the session. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| sessionResult | string | Yes | The `sessionResult` value from the Drop-in or Component. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some fields are included only if you enable them. To enable these fields in your Customer Area, go to **Developers** > **Additional data**. |
| id | string | No | A unique identifier of the session. |
| payments | array of object | No | A list of all authorised payments done for this session. |
|   - amount | object | No | Authorised amount in the transaction. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|     - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
|   - paymentMethod | object | No | Only returned for `resultCode`: **Authorised**. Details about the payment method used in the transaction. |
|     - brand | string | No | The card brand that the shopper used to pay. Only returned if `paymentMethod.type` is **scheme**. |
|     - type | string | No | The `paymentMethod.type` value used in the request. |
|   - pspReference | string | No | Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request. |
|   - resultCode | string | No | The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes).  Possible values:  - **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.  - **Received** – Indicates the payment request was successfully received by Adyen, and will be processed. This is the initial state for all payments.  - **Pending** – The payment order was successfully received but the final status of the payment is not available yet. This is common for payment methods with an asynchronous flow. |
| reference | string | No | The unique reference that you provided in the original `/sessions` request. This identifies the payment and is used in all communication with you about the payment status. |
| status | string | No | The status of the session. The status included in the response doesn't get updated. Don't make the request again to check for payment status updates.  Possible values:  - **completed**: the shopper completed the payment, and the payment was authorized.  - **paymentPending**: the shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.  - **refused**: the session has been refused, because of too many refused payment attempts. The shopper can no longer complete the payment with this session.  - **canceled**: the shopper canceled the payment.  - **expired**: the session expired. The shopper can no longer complete the payment with this session. By default, the session expires one hour after it is created. |

## Response examples

### 200 Success

**success**
```json
{
  "id": "CS12345678",
  "status": "completed"
}
```