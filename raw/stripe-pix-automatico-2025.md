<!-- Source URL: https://docs.stripe.com/payments/pix/pix-automatico -->
<!-- Fetched: 2026-05-06 -->

# Pix Automático

Accept automatic recurring Pix payments through customer-authorized mandates.

Pix Automático supports recurring payments through mandates. This lets customers authorize automatic charges for subscriptions and recurring services. You can use Pix Automático to [save payment details](https://docs.stripe.com/payments/pix/save-payment-details.md) for future charges or [set up a subscription](https://docs.stripe.com/billing/subscriptions/pix.md) with automatic billing.

## How it works

When setting up a mandate, customers authorize it in their bank app during the initial payment flow. After the mandate is created, you can charge customers automatically for future payments within the mandate terms.

### Initial payments

The customer must accept an enrollment, which is the mandate. Your customer authorizes an amount and a billing cycle for recurring charges.

If you want to encourage your customers to upgrade to a higher subscription plan without coming back on session, you can pass a higher amount in `payment_method_options.pix.mandate_options.amount`. Passing higher amounts might impact conversion rates.

> If you plan to add sales tax, consider including it in the mandate amount.

For subscriptions where there’s an initial payment, your customers authorize an initial charge as part of the mandate creation flow.

For subscriptions where there’s no initial payment (free trials), the mandate is created without an initial charge.

### Subsequent payments

When you confirm a PaymentIntent for a recurring payment, Stripe automatically:

- Triggers the pre-debit notification
- Waits the required 3 days
- Charges the customer

No additional action is required from you.

### Pre-debit notifications

Your customer’s bank notifies them 3 days before issuing a charge with the exact debit amount and an option to cancel the payment.

The bank generates pre-debit notifications, with no action required from you.

This means that subsequent payments are charged on billing cycle plus 3 days. During the period after the notification is sent, the PaymentIntent is in `processing`. Confirmation for a recurring payment typically happens 3 days after the pre-debit notification is sent, but it can take up to 7 days with retries.
Example on how subsequent payments are handled on a monthly billing cycle (See full diagram at https://docs.stripe.com/payments/pix/pix-automatico)

### Handle Brazilian consumer tax (IOF)

IOF is applicable on each recurring transaction. Learn more about [handling IOF](https://docs.stripe.com/payments/pix.md#handle-brazilian-consumer-tax).

### Customer communications

In Brazil, businesses commonly send a receipt for each transaction. Learn more about [customer communications](https://docs.stripe.com/payments/pix.md#customer-communications).

### Pix Automático customization

Stripe offers multiple options for you to customize the Pix Automático mandate that you set up for your customer.

You can specify these options using the `payment_method_options[pix][mandate_options]` hash in the Stripe API:

| Field name            | Description                                                                                                                                                                                                                                               | Default value                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `reference`           | The subscription name displayed to customers in their banking app on enrollment.                                                                                                                                                                          | Defaults to the user’s displayable business name. |
| `amount`              | The maximum amount that can be charged in a billing cycle. Set this high enough to allow for price changes and any potential currency conversion fees and Stripe Tax liabilities payable by the buyer.                                                    | 400 BRL                                           |
| `amount_type`         | Set to `maximum` to authorize payments under the mandate up to the amount. Set it to `fixed` to charge that exact amount under the mandate.                                                                                                               | `maximum`                                         |
| `amount_includes_iof` | Whether the customer pays the IOF (default) or you absorb it on behalf of the customer.                                                                                                                                                                   | `never`                                           |
| `payment_schedule`    | The frequency at which you can collect payments. A billing cycle defines the possible charge frequency rather than a required cadence. Pix doesn’t allow you to pass a daily billing schedule. If you select a daily billing schedule, all payments fail. | `monthly`                                         |
| `end_date`            | The expiration date for the mandate.                                                                                                                                                                                                                      | Doesn’t expire if not provided.                   |
| `start_date`          | The start date of the mandate, in YYYY-MM-DD format. The start date should be at least 3 days in the future.                                                                                                                                              | Current date plus 3 days                          |

### Retries

After a recurring payment is scheduled, it moves to a `processing` status. After 3 days, Stripe attempts automatic capture. If the capture fails for a retryable reason (for example, insufficient funds or network failures), we retry the payment once a day for the next 3 days. During this time, the payment stays in `processing` status until it moves to a terminal state (`succeeded` or `failed`). This is enabled by default.

If you use Stripe Billing, we also support retries for cases when a payment wasn’t scheduled at all (for example, a partner error). In these cases, Stripe Billing can retry once after 1 day. Contact [Stripe support](https://support.stripe.com/) to enable this behavior.

## See also

- [Save payment details with Pix](https://docs.stripe.com/payments/pix/save-payment-details.md)
- [Set up a subscription with Pix](https://docs.stripe.com/billing/subscriptions/pix.md)
- [Accept a one-time Pix payment](https://docs.stripe.com/payments/pix/accept-a-payment.md)
