<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/webhooks -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoicing webhooks

When a merchant creates, updates, pays, or cancels an invoice, PayPal sends a webhook event to your server. Your server can then process the events automatically.
To set up webhooks, see our [Webhooks guide](https://developer.paypal.com/api/rest/webhooks/).

PayPal sends these webhook events for invoice activities.

| Event                         | PayPal sends this webhook when                                     | API reference                                                                                         |
| :---------------------------- | :----------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| `INVOICING.INVOICE.CANCELLED` | A merchant or customer cancels an invoice                          | [Cancel sent invoice](https://developer.paypal.com/docs/api/invoicing/v1/#invoice_cancel)             |
| `INVOICING.INVOICE.CREATED`   | A merchant creates an invoice                                      | [Create draft invoice](https://developer.paypal.com/docs/api/invoicing/v1/#invoices_create)           |
| `INVOICING.INVOICE.PAID`      | A customer makes a full, partial, or pending payment on an invoice | [Mark invoice as paid](https://developer.paypal.com/docs/api/invoicing/v1/#invoice_record-payment)    |
| `INVOICING.INVOICE.REFUNDED`  | A merchant issues a full or partial refund for an invoice          | [Mark invoice as refunded](https://developer.paypal.com/docs/api/invoicing/v1/#invoice_record-refund) |
| `INVOICING.INVOICE.SCHEDULED` | A merchant schedules an invoice                                    | [Schedule invoice](https://developer.paypal.com/docs/api/invoicing/v1/#invoice_schedule)              |
| `INVOICING.INVOICE.UPDATED`   | A merchant updates an invoice                                      | [Update invoice](https://developer.paypal.com/docs/api/invoicing/v1/#invoice_update)                  |
