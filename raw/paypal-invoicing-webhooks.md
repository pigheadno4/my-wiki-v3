---
title: Invoicing webhooks
slug: /docs/invoicing/webhooks/
createTime: "2024-08-15T07:15:47.597Z"
updateTime: "2025-05-14T12:33:30.582Z"
---

# Invoicing webhooks

A webhook is an HTTP callback that receives notification messages for events. See [configure webhooks](/docs/integration/direct/webhooks/rest-webhooks/) for more details.

PayPal APIs use webhooks for event notification. Most invoice-related actions, including invoice payments, trigger invoicing webhook events:

| Event                       | Trigger                                                                | Related method                                                             |
| --------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| INVOICING.INVOICE.CANCELLED | A merchant or customer cancels an invoice.                             | [Cancel invoice](/docs/api/invoicing/v1/#invoices_get)                     |
| INVOICING.INVOICE.CREATED   | An invoice is created.                                                 | [Create draft invoice](/docs/api/invoicing/v1/#invoices_create)            |
| INVOICING.INVOICE.PAID      | An invoice is paid, partially paid, or payment is made and is pending. | [Mark invoice as paid](/docs/api/invoicing/v1/#invoices_record-payment)    |
| INVOICING.INVOICE.REFUNDED  | An invoice is refunded or partially refunded.                          | [Mark invoice as refunded](/docs/api/invoicing/v1/#invoices_record-refund) |
| INVOICING.INVOICE.SCHEDULED | An invoice is scheduled.                                               | [Schedule invoice](/docs/api/invoicing/v1/#invoices_schedule)              |
| INVOICING.INVOICE.UPDATED   | An invoice is updated.                                                 | [Update invoice](/docs/api/invoicing/v1/#invoices_update)                  |
