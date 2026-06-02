---
title: Test and go live with invoicing
slug: /docs/invoicing/test-and-go-live/
createTime: "2024-05-15T20:30:27.889Z"
updateTime: "2025-02-27T07:56:47.726Z"
---

# Test and go live with invoicing

You can run negative tests on your integration to manage the responses you give to your customers.

## Know before you code

### Get your credentials

- Before you trigger a simulation, you'll need to [get an access token](https://developer.paypal.com/api/rest/authentication/) .
- Use Postman to explore and test PayPal APIs.

To trigger a simulation for the Invoicing API, you can use a [JSON pointer in the request payload](/docs/invoicing/test-and-go-live/#use-a-json-pointer-in-the-request-payload) or a [path parameter in the request URI](/docs/invoicing/test-and-go-live/#use-a-path-parameter-in-the-request-uri) .

Test values are case sensitive.

### Use a JSON pointer in the request payload

| Trigger          | Test value | Simulated error response |
| ---------------- | ---------- | ------------------------ |
| detail/reference | ERRINV002  | PERMISSION_DENIED        |

#### **`Request`**

```curl
curl -X POST \
  https://api-m.sandbox.paypal.com/v2/invoicing/invoices \
  -H 'Authorization: Bearer <Access Token>' \
  -H 'Content-Type: application/json' \
  -d '{
          "detail":
          {
                    "reference": "ERRINV002"
          }
}'
```

#### **`Response`**

```curl
{
    "localizedMessage": "No permission for the requested operation. ",
    "name": "PERMISSION_DENIED",
    "message": "No permission for the requested operation. ",
    "details": [
        {
            "issue": "No permission for the requested operation. "
        }
    ],
    "information_link": "https://developer.paypal.com/docs/archive/permissions-service/",
    "debug_id": "6e07326c281c4"
}
```

### Use a path parameter in the request URI

| Trigger or test value                           | Simulated error response |
| ----------------------------------------------- | ------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010 | INVOICE_NOT_FOUND        |

#### **`Request`**

```curl
curl -X GET \
  https://api-m.sandbox.paypal.com/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010 \
  -H 'Authorization: Bearer <Access Token>' \
  -H 'Content-Type: application/json'
```

#### **`Response`**

```curl
{
    "name": "RESOURCE_NOT_FOUND",
    "message": "The specified resource does not exist.",
    "debug_id": "98b2b9d2d89cb",
    "links": [
        {
            "href": "https://developer.paypal.com/docs/api/invoicing/#errors",
            "rel": "information_link"
        }
    ]
}
```

## Test values

Test values are case sensitive.

- [Generate invoice number](/docs/invoicing/test-and-go-live/#generate-invoice-number)
- [Create invoices](/docs/invoicing/test-and-go-live/#create-invoices)
- [Get invoice](/docs/invoicing/test-and-go-live/#get-invoice)
- [Delete invoice](/docs/invoicing/test-and-go-live/#delete-invoice)
- [Fully update invoice details](/docs/invoicing/test-and-go-live/#fully-update-invoice-details)
- [Cancel sent invoice](/docs/invoicing/test-and-go-live/#cancel-sent-invoice)
- [Record payment for invoice](/docs/invoicing/test-and-go-live/#record-payment-for-invoice)
- [Delete payment](/docs/invoicing/test-and-go-live/#delete-payment)
- [Record refund for invoice](/docs/invoicing/test-and-go-live/#record-refund-for-invoice)
- [Delete refund](/docs/invoicing/test-and-go-live/#delete-refund)
- [Send invoice reminder](/docs/invoicing/test-and-go-live/#send-invoice-reminder)
- [Send invoice](/docs/invoicing/test-and-go-live/#send-invoice)
- [Search invoices](/docs/invoicing/test-and-go-live/#search-invoices)

### Generate invoice number

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/generate-next-invoice-number .

| Trigger   | Test value | Simulated error response |
| --------- | ---------- | ------------------------ |
| reference | ERRINV066  | INTERNAL_SERVER_ERROR    |
| reference | ERRINV067  | PERMISSION_DENIED        |

### Create invoices

Use the JSON pointer method to simulate the following error responses at POST v2/invoicing/invoices/ .

| Trigger          | Test value | Simulated positive response      |
| ---------------- | ---------- | -------------------------------- |
| detail.reference | ERRINV001  | INTERNAL_SERVER_ERROR            |
| detail.reference | ERRINV002  | PERMISSION_DENIED                |
| detail.reference | ERRINV003  | UNSUPPORTED_MEDIA_TYPE           |
| detail.reference | ERRINV004  | VALIDATION_ERROR_EMPTY_BODY      |
| detail.reference | ERRINV005  | INVALID_REQUEST_GENERIC          |
| detail.reference | ERRINV006  | INVALID_REQUEST_SCHEMA_VIOLATION |

### Get invoice

Use the path parameter in the request URI method to simulate the following error responses at GET /v2/invoicing/invoices/{invoice_id} .

| Trigger or test value                           | Simulated error response |
| ----------------------------------------------- | ------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0007 | INTERNAL_SERVER_ERROR    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0008 | PERMISSION_DENIED        |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0009 | UNAUTHORIZED_ACCESS      |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010 | INVOICE_NOT_FOUND        |

### Delete invoice

Use the path parameter in the request URI method to simulate the following response at DELETE /v2/invoicing/invoices/{invoice_id} .

| Trigger or test value                           | Simulated positive response    |
| ----------------------------------------------- | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0059 | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at DELETE /v2/invoicing/invoices/{invoice_id} .

| Trigger or test value                           | Simulated error response |
| ----------------------------------------------- | ------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0055 | INTERNAL_SERVER_ERROR    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0056 | PERMISSION_DENIED        |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0057 | UNAUTHORIZED_ACCESS      |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0058 | INVOICE_NOT_FOUND        |

### Fully update invoice details

Use the path parameter in the request URI method to simulate the following error responses at PUT /v2/invoicing/invoices/{invoice_id} .

| Trigger or test value                           | Simulated error response         |
| ----------------------------------------------- | -------------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0060 | INTERNAL_SERVER_ERROR            |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0061 | PERMISSION_DENIED                |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0062 | UNSUPPORTED_MEDIA_TYPE           |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0063 | VALIDATION_ERROR_EMPTY_BODY      |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0064 | INVALID_REQUEST_GENERIC          |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0065 | INVALID_REQUEST_SCHEMA_VIOLATION |

### Cancel sent invoice

Use the path parameter in the request URI method to simulate the following response at POST /v2/invoicing/invoices/{invoice_id}/cancel .

| Trigger or test value                                  | Simulated positive response    |
| ------------------------------------------------------ | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0029/cancel | PAYLOAD WITH 204 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/{invoice_id}/cancel .

| Trigger or test value                                  | Simulated error response           |
| ------------------------------------------------------ | ---------------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0024/cancel | INTERNAL_SERVER_ERROR              |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0025/cancel | PERMISSION_DENIED                  |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0026/cancel | UNAUTHORIZED_ACCESS                |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0027/cancel | INVOICE_NOT_FOUND                  |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0028/cancel | CANT_CANCEL_INVOICE_IN_DRAFT_STATE |

### Record payment for invoice

Use the path parameter in the request URI method to simulate the following response at POST /v2/invoicing/invoices/{invoice_id}/payments .

| Trigger or test value                                    | Simulated positive response    |
| -------------------------------------------------------- | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0037/payments | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/{invoice_id}/payments .

| Trigger or test value                                    | Simulated error response             |
| -------------------------------------------------------- | ------------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0031/payments | INTERNAL_SERVER_ERROR                |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0032/payments | PERMISSION_DENIED                    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0033/payments | UNAUTHORIZED_ACCESS                  |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0034/payments | INVOICE_NOT_FOUND                    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0035/payments | CANT_PAY_AN_PAID_OR_CANCELED_INVOICE |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0036/payments | CANT_PAY_MORE_THAN_INVOICE_AMOUNT    |

### Delete payment

Use the path parameter in the request URI method to simulate the following response at DELETE /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/{transaction_id} .

| Trigger or test value                                                          | Simulated positive response    |
| ------------------------------------------------------------------------------ | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV042 | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at DELETE /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/{transaction_id} .

| Trigger or test value                                                          | Simulated error response     |
| ------------------------------------------------------------------------------ | ---------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV038 | INTERNAL_SERVER_ERROR        |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV039 | PERMISSION_DENIED            |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV040 | UNAUTHORIZED_ACCESS          |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV041 | PAYMENT_OR_INVOICE_NOT_FOUND |

### Record refund for invoice

Use the path parameter in the request URI method to simulate the following response at POST /v2/invoicing/invoices/{invoice_id}/refunds .

| Trigger or test value                                   | Simulated positive response    |
| ------------------------------------------------------- | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0049/refunds | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/{invoice_id}/refunds .

| Trigger or test value                                   | Simulated error response             |
| ------------------------------------------------------- | ------------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0043/refunds | INTERNAL_SERVER_ERROR                |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0044/refunds | PERMISSION_DENIED                    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0045/refunds | UNAUTHORIZED_ACCESS                  |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0046/refunds | INVOICE_NOT_FOUND                    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0047/refunds | CANT_REFUND_A_CANCELED_INVOICE       |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0048/refunds | CANT_REFUND_MORE_THAN_PAYMENT_AMOUNT |

### Delete refund

Use the path parameter in the request URI method to simulate the following response at DELETE /v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id} .

| Trigger or test value                                                         | Simulated positive response    |
| ----------------------------------------------------------------------------- | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV054 | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at DELETE /v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id}/delete .

| Trigger or test value                                                         | Simulated error response    |
| ----------------------------------------------------------------------------- | --------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV050 | INTERNAL_SERVER_ERROR       |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV051 | PERMISSION_DENIED           |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV052 | UNAUTHORIZED_ACCESS         |
| /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV053 | REFUND_OR_INVOICE_NOT_FOUND |

### Send invoice reminder

Use the path parameter in the request URI method to simulate the following response at POST /v2/invoicing/invoices/{invoice_id}/remind .

| Trigger or test value                                  | Simulated positive response    |
| ------------------------------------------------------ | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0023/remind | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/{invoice_id}/remind .

| Trigger or test value                                  | Simulated error response                 |
| ------------------------------------------------------ | ---------------------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0017/remind | INTERNAL_SERVER_ERROR                    |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0018/remind | PERMISSION_DENIED                        |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0019/remind | UNAUTHORIZED_ACCESS                      |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0020/remind | INVOICE_NOT_FOUND                        |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0021/remind | CANT_REMIND_INVOICE_IN_DRAFT_STATE       |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0022/remind | CANT_REMIND_INVOICE_WITHOUT_BILLING_INFO |

### Send invoice

Use the path parameter in the request URI method to simulate the following response at POST /v2/invoicing/invoices/{invoice_id}/send .

| Trigger or test value                                | Simulated positive response    |
| ---------------------------------------------------- | ------------------------------ |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0016/send | PAYLOAD WITH 200 RESPONSE CODE |

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/invoices/{invoice_id}/send .

| Trigger or test value                                | Simulated error response        |
| ---------------------------------------------------- | ------------------------------- |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0011/send | INTERNAL_SERVER_ERROR           |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0012/send | PERMISSION_DENIED               |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0013/send | UNAUTHORIZED_ACCESS             |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0014/send | INVOICE_NOT_FOUND               |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0015/send | CANT_SEND_INVOICE_WITHOUT_EMAIL |
| /v2/invoicing/invoices/INV2-ABCD-1234-EINV-0030/send | CANT_SEND_ALREADY_SENT_INVOICE  |

### Search invoices

Use the path parameter in the request URI method to simulate the following error responses at POST /v2/invoicing/search-invoices .

| Trigger or test value | Simulated error response |
| --------------------- | ------------------------ |
| ERRINV068             | INTERNAL_SERVER_ERROR    |
| ERRINV069             | PERMISSION_DENIED        |
| ERRINV070             | INVALID_REQUEST          |
