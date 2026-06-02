<!-- Source URL: https://docs.stripe.com/payments/customer-balance/refunding -->
<!-- Fetched: 2026-05-05 -->

# Refund bank transfer payments

Refund payments made with bank transfers, or refund a customer’s available cash balance.

You can refund customer balance payments through the [Dashboard](https://dashboard.stripe.com/payments) or [API](https://docs.stripe.com/api.md#create_refund).

## Refund a payment to the customer

Stripe requires customer bank account details to process the refund. In some cases, Stripe receives the customer’s bank account details when performing the transfer. Stripe emails the customer to let them know that the refund is in process.

When we can’t determine the destination bank account automatically due to unavailable or ambiguous customer bank account information, Stripe requests it by contacting the customer at the email address in the customer object you created. If you didn’t include an email address when you created the customer object, creating a refund results in an error. Update the customer object with a valid email address for the customer, and try creating the refund again. You can specify a new email address when you create a refund.

In some cases, Stripe performs additional checks before processing a refund or asking your customers for bank account information. Stripe contacts you if we require more information before finalizing the refund.

Customers have 45 days from receipt of the request to submit bank account details. After 45 days without a valid response, Stripe cancels the refund and returns the funds to the customer’s account cash balance. We recommend you then contact your customer to discuss alternative ways of returning the funds.

You can refund a payment up to 180 days after it was created.

### Creating a payment refund using the Dashboard

1. To refund a payment made with a bank transfer, go to the payment page and click **Refund**.
   ![Payment page header with Refund button](assets/stripe-bank-transfer-payment-page-header.png)

1. In the following dialog, enter the amount you want to refund, if different than the full payment amount, and any other details about the refund. Then click **Refund**.

### Creating a payment refund using the API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const refund = await stripe.refunds.create({
  payment_intent: "{{PAYMENTINTENT_ID}}",
  instructions_email: "customeremail@example.com",
});
```

Refunds are sent to the customer’s bank account, and the customer receives a notification at their default email address. If you want to override the default email address used to contact the customer, specify the new email address using the [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) parameter.

The refund’s status transitions as follows:

| Event                                                                          | Refund status     |
| ------------------------------------------------------------------------------ | ----------------- |
| Refund is created                                                              | `requires_action` |
| Customer submits bank account details, and Stripe begins processing the refund | `pending`         |
| Refund is expected to arrive in customer’s bank                                | `succeeded`       |
| Customer’s bank returns the funds back to Stripe                               | `requires_action` |
| Refund is in `requires_action` 45 days after creation                          | `failed`          |
| Refund is canceled from a `requires_action` state                              | `canceled`        |

If the customer’s bank can’t successfully complete the transfer, the funds are returned to Stripe and the refund transitions to `requires_action`. This can happen if the account holder’s name doesn’t match what the recipient bank has on file or if the provided bank account number has a typo. In these cases, Stripe emails the customer to inform them of the failure and to request that they resubmit their bank account details.

If your customer doesn’t provide their bank account details within 45 days, the refund’s status transitions to `failed` and we send the [refund.failed](https://docs.stripe.com/api/events/types.md#event_types-refund.failed) event. This means that Stripe can’t process the refund, and you must [return the funds to your customer outside of Stripe](https://docs.stripe.com/refunds.md#failed-refunds).

The [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) field on the refund is the email that the refund was sent to. While a refund is waiting for a response from the customer, details of the email sent to the customer can also be found under the [next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object.md#refund_object-next_action-display_details-email_sent) field on the refund.

Each individual refund (including each partial refund) might incur a fee. Contact your point of contact at Stripe to learn more about this.

## Cancel a payment refund sent to the customer

If a bank transfer payment refund has been sent to the customer, and the customer hasn’t submitted their bank details, you can still cancel the refund.

### Canceling a payment refund using the Dashboard

1. To cancel a refund for a bank transfer payment, go to the payment page and click **Cancel refund**.
   ![Cancel payment refund button on payment page](assets/stripe-bank-transfer-cancel-payment-refund.png)

1. If the payment has multiple partial refunds in the `requires_action` state, select the correct refund from the **Refund** dropdown in the following dialog.
1. Confirm the cancellation by selecting **Cancel refund** in the dialog.

### Canceling a payment refund using the API

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const refund = await stripe.refunds.cancel({
  refund: "{{REFUND_ID}}",
});
```

After the payment refund has been canceled, the refund transitions from `requires_action` to `canceled`. If there are no other refunds, the payment transitions back to its original pre-refund state.

## Refund a payment to the customer’s cash balance

A refund to the customer cash balance succeeds immediately. Refunds to the customer cash balance are free of charge.

### Creating a payment refund using the Dashboard

1. To refund a payment made with a bank transfer, go to the payment page and click **Refund**.
   ![Payment page header with Refund button](assets/stripe-bank-transfer-payment-page-header.png)

1. In the following dialog, select **Customer cash balance** in the **Destination** dropdown. Selecting this option deposits the refund into the customer’s cash balance on Stripe, which allows them to use the funds for future payments on your site.

## Refund the cash balance to the customer

You can return a customer’s cash balance directly to them. For example, you might need to do this when a customer transfers more funds than expected for a payment.

### Refund a customer’s cash balance using the Dashboard

1. Navigate to the [Customer list](https://dashboard.stripe.com/customers) page.
1. Click the customer in the list of customers.
1. Expand the **Cash Balance** row in the **Payment methods** section.
1. Click **Initiate Refund** button at the end of the row.
   ![Cash Balance row on Customer page with Initiate Refund button](assets/stripe-customer-balance-row.png)

1. In the next dialog, enter the amount to refund.
1. Click **Initiate Refund**.

View the status of the refund on the customer balance transactions list page.

### Refund a customer’s cash balance using the API

To refund a customer’s cash balance with the API, set the [origin](https://docs.stripe.com/api/refunds/object.md#refund_object-origin) parameter to `customer_balance` and specify the [customer](https://docs.stripe.com/api/refunds/object.md#refund_object-customer). The customer’s default email address is used to contact them. To override it, specify the new email address using the [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const refund = await stripe.refunds.create({
  amount: 1099,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  instructions_email: "jenny.rosen@example.com",
  origin: "customer_balance",
});
```

## Cancel a cash balance refund sent to the customer

You can only cancel un-processed refunds. After the customer submits their bank account details, you can’t cancel a refund. Currently, you must use the Stripe Dashboard to cancel a refund:

1. Navigate to the [Customer list](https://dashboard.stripe.com/customers) page.
1. Click the customer in the list of customers.
1. Expand the **Cash Balance** row in the **Payment methods** section.
1. Click the **View balance details** link.
   ![Cash balance View balance details link](assets/stripe-cash-balance-transactions-link.png)

1. Click the overflow menu (**•••**) next to the refund you want to cancel and click the **Cancel** link
   ![Cancel customer return overflow menu](assets/stripe-cancel-customer-return.png)

The refund amount is credited back to the available cash balance.

## Track state of a refund

You can track the state of a refund through the [Dashboard](https://dashboard.stripe.com/payments) or [API](https://docs.stripe.com/api/refunds.md).

### When and where refund email is sent

Stripe sends an email to the email address provided in the [instructions_email](https://docs.stripe.com/api/refunds/object.md#refund_object-instructions_email) field on the refund. While a refund is waiting for a response from the customer, you can also check the refund’s [next_action.display_details.email_sent](https://docs.stripe.com/api/refunds/object.md#refund_object-next_action-display_details-email_sent) field for details such as the sent time and the address. The sent time is also the time when the refund transitioned to the `requires_action` state.

### Pending refunds

If the customer has submitted their bank account details, the refund transitions to `pending`.

### Successful refunds

The refund transitions to `succeeded` when the refund is successfully paid out to the customer.

## Refund international payments

Stripe doesn’t support refunds for international (SWIFT) payments and doesn’t send any automated refund emails for international wire payments.

1. **Move funds from the customer balance to your Stripe account balance**: If the funds are sitting unreconciled in the customer’s cash balance, reconcile them through the Dashboard or API, or wait for Stripe to automatically sweep them to your account balance after 75 days.
1. **Pay out the funds to your bank account**: After the funds are in your Stripe account balance, initiate a [payout](https://dashboard.stripe.com/payouts) to transfer them to your external bank account.
1. **Collect your customer’s bank account details**: Reach out to your customer directly to obtain the account information needed to send the funds back to them.
1. **Send the funds and notify your customer**: Use your preferred method to transfer the funds back to your customer, and let them know the refund timeline and method.

## Test refunds

You can test refund behavior in a sandbox using the following test bank accounts on the bank account details collection page linked in the email sent to the customer. Bank account details outside of these test bank accounts won’t be accepted.

> In a sandbox, refund instruction emails are only sent to email addresses linked to the Stripe account.

#### IBAN

Specify the appropriate [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) (for example, GB, IL, CR, and so on) to test IBANs for any IBAN country and any valid currency for that country. For instance, the following IBANs specify Germany with the `DE` prefix.

| Number                   | Type             |
| ------------------------ | ---------------- |
| `DE89370400440532013000` | Refund succeeds. |

| `DE62370400440532013001`

`DE89370400440532013002`

`DE89370400440532013003`

`DE89370400440532013004`

`DE89370400440532013005` | Refund fails. |

#### Japan

| Routing   | Account   | Type             |
| --------- | --------- | ---------------- |
| `1100000` | `0001234` | Refund succeeds. |
| `1100000` | `1111113` |

`1111116`

`1111113`

`3333335`

`4444440` | Refund fails. |

#### Mexico

| Account              | Type             |
| -------------------- | ---------------- |
| `000000001234567897` | Refund succeeds. |

| `000000111111111117`

`000000111111111133`

`000000222222222224`

`000000333333333331`

`000000444444444448` | Refund fails. |

#### United Kingdom

| Sort     | Account    | Type             |
| -------- | ---------- | ---------------- |
| `108800` | `00012345` | Refund succeeds. |
| `108800` | `11111113` |

`11111116`

`22222227`

`33333335`

`44444440` | Refund fails. |

#### United States

| Routing     | Account        | Type             |
| ----------- | -------------- | ---------------- |
| `110000000` | `000123456789` | Refund succeeds. |
| `110000000` | `000111111113` |

`000111111116`

`000222222227`

`000333333335`

`000444444440` | Refund fails. |

#### Testing Refunds Expiry

You can make an API call to simulate the expiry of a testmode refund.

```bash
curl https://api.stripe.com/v1/test_helpers/refunds/{{REFUND_ID}}/expire \
  -X POST \
  -u <<YOUR_SECRET_KEY>>:
```
