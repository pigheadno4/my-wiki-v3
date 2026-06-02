<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/test-and-go-live -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test and go live with invoicing

Use test values to simulate error responses with the PayPal Invoicing API and verify that your application handles different scenarios correctly.

## Prerequisites

- Get your [access token](https://developer.paypal.com/api/rest/authentication/).
- Use [Postman](https://identity.getpostman.com/login?continue=https%3A%2F%2Fgo.postman.co%2Ffork%3Fcollection%3D19024122-92a85d0e-51e7-47da-9f83-c45dcb1cdf24%26referrer%3Dhttps%253A%252F%252Fdeveloper.paypal.com%252Fapi%252Frest%252F%26token%3Da88e6154-b499-46fd-bf83-f99a6267dedb%26key%3DeyJhbGciOiJBMjU2Q1RSIiwiZXh0Ijp0cnVlLCJrIjoiT3BwM0EzTVU4b0ZBM1daTW8zZmlPczd4dEdOSUpGNkxwR3JXQXV3LWxrYyIsImtleV9vcHMiOlsiZW5jcnlwdCIsImRlY3J5cHQiXSwia3R5Ijoib2N0In0%253D%26counter%3DbbhMUbsoFAUBKcDlXqGK3Q%253D%253D%26traceId%3D60b5403d-d4d6-497c-ac61-c6fb7e6dcdf0) to test the PayPal APIs.
- Use the [sandbox environment](https://api-m.sandbox.paypal.com).

## Simulation methods

You can simulate responses in two ways: [JSON pointer method](#json-pointer-method) or the [path parameter method](#path-parameter-method).

### JSON pointer method

| Request location   | Test value  | Simulated response  |
| :----------------- | :---------- | :------------------ |
| `detail.reference` | `ERRINV001` | `PERMISSION_DENIED` |

The following sample code shows a simulated request with a test value and the Sandbox response.

#### Request

```
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

#### Response

```
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

### Path parameter method

Use test value in the request URI. This simulates a response.

| Test value                                        | Simulated response  |
| :------------------------------------------------ | :------------------ |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010` | `INVOICE_NOT_FOUND` |

The following sample code shows a simulated request with a test value and the Sandbox response.

#### Request

```
curl -X GET \
  https://api-m.sandbox.paypal.com/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010 \
  -H 'Authorization: Bearer <Access Token>' \
  -H 'Content-Type: application/json'
```

#### Response

```
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

**Note**: Test values are case sensitive.

The following test values simulate different responses for each Invoicing API operation. Each operation shows where to insert the test value and the response you can expect.

### Generate invoice number

Use the path parameter in the request URI at `POST /v2/invoicing/invoices/generate-next-invoice-number` to simulate the following error responses.

| Test value  | Simulated response      |
| :---------- | :---------------------- |
| `ERRINV066` | `INTERNAL_SERVER_ERROR` |
| `ERRINV067` | `PERMISSION_DENIED`     |

### Create invoices

Use the JSON pointer method at
`POST /v2/invoicing/invoices/` to simulate the following error responses.

| Request location   | Test value  | Simulated response                 |
| :----------------- | :---------- | :--------------------------------- |
| `detail.reference` | `ERRINV001` | `INTERNAL_SERVER_ERROR`            |
| `detail.reference` | `ERRINV002` | `PERMISSION_DENIED`                |
| `detail.reference` | `ERRINV003` | `UNSUPPORTED_MEDIA_TYPE`           |
| `detail.reference` | `ERRINV004` | `VALIDATION_ERROR_EMPTY_BODY`      |
| `detail.reference` | `ERRINV005` | `INVALID_REQUEST_GENERIC`          |
| `detail.reference` | `ERRINV006` | `INVALID_REQUEST_SCHEMA_VIOLATION` |

### Get invoice

Use the path parameter in the request URI at `GET /v2/invoicing/invoices/{invoice_id}` to simulate the following error responses.

| Test value                                        | Simulated response      |
| :------------------------------------------------ | :---------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0007` | `INTERNAL_SERVER_ERROR` |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0008` | `PERMISSION_DENIED`     |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0009` | `UNAUTHORIZED_ACCESS`   |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0010` | `INVOICE_NOT_FOUND`     |

### Delete invoice

Use the path parameter in the request URI method to simulate the following response at `DELETE /v2/invoicing/invoices/{invoice_id}`.

#### Success

| Test value                                        | Simulated response               |
| :------------------------------------------------ | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0059` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                        | Simulated response      |
| :------------------------------------------------ | :---------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0055` | `INTERNAL_SERVER_ERROR` |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0056` | `PERMISSION_DENIED`     |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0057` | `UNAUTHORIZED_ACCESS`   |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0058` | `INVOICE_NOT_FOUND`     |

### Update the invoice

Use the path parameter in the request URI method to simulate the following error response at
`PUT /v2/invoicing/invoices/{invoice_id}`.

| Test value                                        | Simulated response                 |
| :------------------------------------------------ | :--------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0060` | `INTERNAL_SERVER_ERROR`            |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0061` | `PERMISSION_DENIED`                |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0062` | `UNSUPPORTED_MEDIA_TYPE`           |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0063` | `VALIDATION_ERROR_EMPTY_BODY`      |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0064` | `INVALID_REQUEST_GENERIC`          |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0065` | `INVALID_REQUEST_SCHEMA_VIOLATION` |

### Cancel a sent invoice

Use the path parameter in the request URI method to simulate the following response at\
`POST /v2/invoicing/invoices/{invoice_id}/cancel`.

#### Success

| Test value                                               | Simulated response               |
| :------------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0029/cancel` | `PAYLOAD WITH 204 RESPONSE CODE` |

#### Error

| Test value                                               | Simulated response                   |
| :------------------------------------------------------- | :----------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0024/cancel` | `INTERNAL_SERVER_ERROR`              |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0025/cancel` | `PERMISSION_DENIED`                  |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0026/cancel` | `UNAUTHORIZED_ACCESS`                |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0027/cancel` | `INVOICE_NOT_FOUND`                  |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0028/cancel` | `CANT_CANCEL_INVOICE_IN_DRAFT_STATE` |

### Record payment for invoice

Use the path parameter in the request URI method to simulate the following response at\
`POST /v2/invoicing/invoices/{invoice_id}/payments`.

#### Success

| Test value                                                 | Simulated response               |
| :--------------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0037/payments` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                                 | Simulated response                     |
| :--------------------------------------------------------- | :------------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0031/payments` | `INTERNAL_SERVER_ERROR`                |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0032/payments` | `PERMISSION_DENIED`                    |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0033/payments` | `UNAUTHORIZED_ACCESS`                  |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0034/payments` | `INVOICE_NOT_FOUND`                    |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0035/payments` | `CANT_PAY_AN_PAID_OR_CANCELED_INVOICE` |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0036/payments` | `CANT_PAY_MORE_THAN_INVOICE_AMOUNT`    |

### Delete payment

Use the path parameter in the request URI method to simulate the following response at\
`DELETE /v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/{transaction_id}`.

#### Success

| Test value                                                                       | Simulated response               |
| :------------------------------------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV042` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                                                       | Simulated response             |
| :------------------------------------------------------------------------------- | :----------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV038` | `INTERNAL_SERVER_ERROR`        |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV039` | `PERMISSION_DENIED`            |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV040` | `UNAUTHORIZED_ACCESS`          |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/payments/EXT-ABCDEFGHERRINV041` | `PAYMENT_OR_INVOICE_NOT_FOUND` |

### Record refund for invoice

Use the path parameter in the request URI method to simulate the following response at\
`POST /v2/invoicing/invoices/{invoice_id}/refunds`:

#### Success

| Test value                                                | Simulated response               |
| :-------------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0049/refunds` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                                | Simulated response                     |
| :-------------------------------------------------------- | :------------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0043/refunds` | `INTERNAL_SERVER_ERROR`                |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0044/refunds` | `PERMISSION_DENIED`                    |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0045/refunds` | `UNAUTHORIZED_ACCESS`                  |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0046/refunds` | `INVOICE_NOT_FOUND`                    |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0047/refunds` | `CANT_REFUND_A_CANCELED_INVOICE`       |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0048/refunds` | `CANT_REFUND_MORE_THAN_PAYMENT_AMOUNT` |

### Delete refund

Use the path parameter in the request URI method to simulate the following response at\
`DELETE /v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id}`.

#### Success

| Test value                                                                      | Simulated response               |
| :------------------------------------------------------------------------------ | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV054` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                                                      | Simulated response            |
| :------------------------------------------------------------------------------ | :---------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV050` | `INTERNAL_SERVER_ERROR`       |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV051` | `PERMISSION_DENIED`           |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV052` | `UNAUTHORIZED_ACCESS`         |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EFGH-5678/refunds/EXT-ABCDEFGHERRINV053` | `REFUND_OR_INVOICE_NOT_FOUND` |

### Send invoice reminder

Use the path parameter in the request URI method to simulate the following response at\
`POST /v2/invoicing/invoices/{invoice_id}/remind`.

#### Success

| Test value                                               | Simulated response               |
| :------------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0023/remind` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                               | Simulated response                         |
| :------------------------------------------------------- | :----------------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0017/remind` | `INTERNAL_SERVER_ERROR`                    |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0018/remind` | `PERMISSION_DENIED`                        |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0019/remind` | `UNAUTHORIZED_ACCESS`                      |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0020/remind` | `INVOICE_NOT_FOUND`                        |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0021/remind` | `CANT_REMIND_INVOICE_IN_DRAFT_STATE`       |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0022/remind` | `CANT_REMIND_INVOICE_WITHOUT_BILLING_INFO` |

### Send invoice

Use the path parameter in the request URI method to simulate the following response at\
`POST /v2/invoicing/invoices/{invoice_id}/send`.

#### Success

| Test value                                             | Simulated response               |
| :----------------------------------------------------- | :------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0016/send` | `PAYLOAD WITH 200 RESPONSE CODE` |

#### Error

| Test value                                             | Simulated response                |
| :----------------------------------------------------- | :-------------------------------- |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0011/send` | `INTERNAL_SERVER_ERROR`           |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0012/send` | `PERMISSION_DENIED`               |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0013/send` | `UNAUTHORIZED_ACCESS`             |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0014/send` | `INVOICE_NOT_FOUND`               |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0015/send` | `CANT_SEND_INVOICE_WITHOUT_EMAIL` |
| `/v2/invoicing/invoices/INV2-ABCD-1234-EINV-0030/send` | `CANT_SEND_ALREADY_SENT_INVOICE`  |

### Search invoices

Use the path parameter in the request URI method to simulate the following error responses at\
`POST /v2/invoicing/search-invoices`.

| Test value  | Simulated response      |
| :---------- | :---------------------- |
| `ERRINV068` | `INTERNAL_SERVER_ERROR` |
| `ERRINV069` | `PERMISSION_DENIED`     |
| `ERRINV070` | `INVALID_REQUEST`       |
