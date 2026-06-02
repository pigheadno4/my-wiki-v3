<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/lifecycle -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Invoice lifecycle and status flow

PayPal Invoicing defines a set of statuses that represent an invoice's lifecycle. Most invoices follow a simple flow: **Draft** → **Due** → **Paid** (or **Cancelled**). An invoice starts as a draft, is sent to request payment, and finishes as paid or canceled, depending on the result.

## Invoice statuses

The invoice status determines how the invoice should be interpreted and what actions are allowed at any given point.

| UI status          | API status                         | Description and possible actions                                                                                                                                                                                | Next possible status                                                                         |
| ------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Draft              | `DRAFT`                            | All invoices start in draft status. The invoice is created but not sent. It is fully editable and invisible to the payer.                                                                                       | **Due**, **Scheduled**, **Overdue** (after the due date), **Marked as Paid**, or **Deleted** |
| Due                | `SENT` or `UNPAID`                 | The invoice is payable. <br />- `SENT`: The invoice is sent to the customer’s registered email address through the invoicing UI. <br />- `UNPAID`: The invoice is shared through a link or QR code.             | **Overdue** (after the due date), **Paid**, **Partially Paid**, or **Canceled**              |
| Overdue            | `SENT` or `UNPAID`                 | The invoice is payable and past due.<br />- `SENT`: The invoice is sent to the customer’s registered email address through the invoicing UI. <br />- `UNPAID`: The invoice is shared through a link or QR code. | **Paid**, **Partially Paid**, or **Canceled**                                                |
| Scheduled          | `SCHEDULED`                        | The invoice is scheduled for a future send date. The invoice is fully editable and invisible to the payer.                                                                                                      | **Due** (on the scheduled date), **Overdue** (after the due date), or **Deleted**            |
| Partially Paid     | `PARTIALLY_PAID`                   | Partially paid with an outstanding balance.                                                                                                                                                                     | **Paid** when the remaining balance is collected                                             |
| Paid               | `PAID` or `MARKED_AS_PAID`         | - `PAID`: The invoice is fully paid and settled, and is no longer payable. <br />-`MARKED_AS_PAID`: The invoice is manually marked as paid to reflect an external payment for reconciliation.                   | **Partially Refunded**, **Marked as Refunded** or **Refunded**, if you issue a refund        |
| Payment Pending    | `PAYMENT_PENDING`                  | Payment is in progress but not yet completed.                                                                                                                                                                   | **Paid**, **Partially Paid**                                                                 |
| Canceled           | `CANCELLED` or `AUTO_CANCELLED`    | - `CANCELLED`: The invoice is canceled, no longer payable, and retained for audit and reference. <br />- `AUTO_CANCELLED`: The invoice is automatically cancelled.                                              | No further transitions allowed                                                               |
| Partially Refunded | `PARTIALLY_REFUNDED`               | The invoice has been partially refunded, so some but not all of the original payment has been returned.                                                                                                         | No further transitions allowed                                                               |
| Refunded           | `REFUNDED` or `MARKED_AS_REFUNDED` | - `REFUNDED`: The invoice is fully refunded. <br />- `MARKED_AS_REFUNDED`: The invoice is manually marked as refunded to show that the refund was handled outside PayPal and is used for manual reconciliation. | No further transitions allowed                                                               |
