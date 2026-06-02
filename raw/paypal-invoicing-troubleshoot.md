<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/troubleshooting -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Invoicing API

The PayPal Invoicing API returns specific error codes and messages to help you troubleshoot integration issues.

## Error response format

All Invoicing API errors follow this structure:

```json theme={null}
{
  "name": "INVALID_REQUEST",
  "message": "Request is not well-formed, syntactically incorrect, or violates schema.",
  "details": [
    {
      "description": "Payment method is missing.",
      "field": "/method",
      "issue": "MISSING_REQUIRED_PARAMETER",
      "location": "body"
    }
  ],
  "links": [
    {
      "href": "https://developer.paypal.com/docs/limited-release/invoicing/#errors",
      "rel": "information_link"
    }
  ],
  "debug_id": "04228dda78114"
}
```

## API errors

PayPal returns HTTP `4XX` status codes if something passes in the request has an error. `5XX` status codes appear when something is wrong on our end with a server or service. For more information, see [Handling API responses when integrating with PayPal APIs](https://paypal.mintlify.app/developer/how-to/api/handling-api-responses#common-paypal-api-error-codes).

| HTTP code | Error name               | Message                                                    | Details                                                                        |
| :-------- | :----------------------- | :--------------------------------------------------------- | :----------------------------------------------------------------------------- |
| `400`     | `INVALID_REQUEST`        | Invalid request                                            | One or more validation errors have occurred.                                   |
| `401`     | `AUTHENTICATION_FAILURE` | Authorization error occurred                               | Authorization error occurred. Check your credentials.                          |
| `404`     | `RESOURCE_NOT_FOUND`     | Resource not found                                         | The resource requested is not found in the system.                             |
| `422`     | `UNPROCESSABLE_ENTITY`   | Invoicing business error                                   | A detailed error message is passed in the message field.                       |
| `429`     | `RATE_LIMIT_REACHED`     | Too many requests and user is blocked due to rate limiting | The rate limit for the user, application, or token exceeds a predefined value. |
| `500`     | `INTERNAL_SERVER_ERROR`  | Internal service error                                     | Resend the request at another time.                                            |

## Authorization errors

<table>
  <thead>
    <tr>
      <th>HTTP code</th>
      <th>Issue</th>
      <th>Message</th>
      <th>Common cause</th>
      <th>Affected fields</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>403</code></td>
      <td><code>NOT\_AUTHORIZED</code></td>
      <td>Authorization failed due to insufficient permissions</td>
      <td>Invalid access token or account permissions</td>

      <td>
        <ul>
          <li><code>invoiceId</code></li>
          <li><code>templateId</code></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><code>403</code></td>
      <td><code>PERMISSION\_DENIED</code></td>
      <td>The requested invoice and template are not associated with the requested user</td>
      <td>Accessing resources that don't belong to your account</td>

      <td>
        <ul>
          <li><code>invoiceId</code></li>
          <li><code>templateId</code></li>
        </ul>
      </td>
    </tr>

  </tbody>
</table>

## Request validation errors

<table>
  <thead>
    <tr>
      <th>Issue</th>
      <th>Description</th>
      <th>Affected fields</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>INVALID\_STRING\_LENGTH</code></td>
      <td>Currency code must be 3 characters</td>

      <td>
        <ul>
          <li><code>/detail/currency\_code</code></li>
          <li><code>/amount/currency\_code</code></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><code>INVALID\_STRING\_MAX\_LENGTH</code></td>
      <td>Field exceeds maximum character limit</td>

      <td>
        <ul>
          <li><code>/detail/note</code></li>
          <li><code>/items/0/name</code></li>
          <li><code>/detail/invoice\_number</code></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><code>INVALID\_PARAMETER\_SYNTAX</code></td>
      <td>Invalid format of the dates, phone numbers, or country codes</td>

      <td>
        <ul>
          <li><code>/detail/invoice\_date</code></li>
          <li><code>/detail/payment\_term/due\_date</code></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td><code>MISSING\_REQUIRED\_PARAMETER</code></td>
      <td>Required field is missing</td>

      <td>
        <ul>
          <li><code>/method</code></li>
          <li><code>/amount/value</code></li>
        </ul>
      </td>
    </tr>

  </tbody>
</table>

## Business logic errors

| Issue                                    | Description                                                             |
| :--------------------------------------- | :---------------------------------------------------------------------- |
| `INVOICE_ALREADY_SENT`                   | The system blocks sending any invoice that has already been sent.       |
| `CANT_SEND_INVOICE_WITHOUT_EMAIL`        | A recipient email address is required before an invoice can be sent.    |
| `CANT_CANCEL_INVOICE_IN_DRAFT_STATE`     | Cannot cancel an invoice that is in draft state.                        |
| `CANT_PAY_AN_PAID_OR_CANCELED_INVOICE`   | Cannot record a payment on an invoice that is already paid or canceled. |
| `PAYMENT_AMOUNT_GREATER_THAN_AMOUNT_DUE` | Payment amount cannot exceed the total amount due on the invoice.       |
| `CANT_REFUND_MORE_THAN_PAYMENT_AMOUNT`   | Cannot refund more than the amount of recorded payments.                |
| `INVOICE_CANNOT_BE_DELETED`              | Only draft, scheduled, or canceled invoices can be deleted.             |
| `INVOICE_NOT_FOUND`                      | Invoice with specified id does not exists.                              |

## Field validation limits

| Field                | Character limit |
| :------------------- | :-------------- |
| Invoice number       | 25              |
| Currency code        | 3               |
| Country code         | 2               |
| Email address        | 3–254           |
| Phone number         | 1–14 digits     |
| Item name            | 200             |
| Item description     | 1000            |
| Invoice note         | 4000            |
| Terms and conditions | 4000            |
| Reference field      | 120             |
| Logo URL             | 2000            |
| Website URL          | 2048            |
