<!-- Source URL: https://docs.stripe.com/payments/stripe-balance -->
<!-- Fetched: 2026-05-01 -->

# Pay with Stripe balance

Collect subscription fees directly from the Stripe balances of your connected accounts.

Review the [Connect pricing page](https://stripe.com/connect/pricing) for details on transaction fees.

As a Connect platform, you can create a payment method linked to a connected account’s available Stripe balance. This allows you to collect subscription payments directly from a connected account’s available balance, instead of through external payment methods such as cards.

> You can only use Stripe balance payments to charge subscription payments to your connected accounts.

## Integrate payments from Stripe balances

This payment method is only available as part of a preview release with [Accounts V2](https://docs.stripe.com/connect/accounts-v2.md).

## Eligibility

Stripe balance payments are subject to the following conditions:

- You can only configure this payment method for an active connected account that’s controlled by your platform and that has the `card_payments` capability active.
- You can only use this payment method for debiting subscription payments from connected accounts where your platform provides payments functionality through Connect, not for any other goods or services.
- Paying from a Stripe balance isn’t available when using [Dynamic Payment Methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You must explicitly specify paying from a Stripe balance as a payment method when creating a subscription payment.

#### Payment method properties

- **Customer locations**

  Connected accounts in the following countries can pay their platforms using Balance Pay:

  AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, NO, CA, CH, GB, US

- **Presentment currency**

  USD, CAD, GBP, EUR, CHF, NOK, CZK, DKK, HUF, PLN, RON, SEK

- **Payment confirmation**

  Business-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  Requires Billing

- **Payout timing**
  - Domestic payments: instant
  - International payments: T+1

- **Connect support**

  Requires Connect

- **Dispute support**

  No

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  Yes / Yes

#### Business locations

Connect platforms in the following countries can accept Stripe balance payments with local currency settlement:

- AT
- BE
- BG
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GR
- HR
- HU
- IE
- IT
- LI
- LT
- LU
- LV
- MT
- NL
- NO
- PL
- PT
- RO
- SE
- SI
- SK
- US

#### Product support

- Connect
- Subscriptions
- Invoicing

### Required approval from your connected accounts

You must obtain approvals from your connected accounts before collecting payments from their Stripe balances. We recommend using the following language to inform your connected accounts, and that you provide an option to opt out of paying from their Stripe balance:

By clicking **Confirm**, you authorize to debit your Stripe account balance for any amount owed for recurring charges arising from your use of 's services, pursuant to 's website and terms.

## Timing and availability of funds

Payments made from a Stripe balance are confirmed immediately. Stripe balance payments from connected accounts in the same country as your platform become available in your Stripe balance with same-day settlement (T+0). Cross-border payments from connected accounts in a different country become available in your Stripe balance with next-day settlement (T+1).

## Cross-border payments

You can create Stripe balance payments in a currency other than your platform’s default currency, as long as the connected account’s Stripe account includes that currency. Stripe automatically converts the funds to your platform account’s default currency.

> If you accept balance payments in multiple currencies, [create a separate price](https://docs.stripe.com/products-prices/manage-prices.md#create-price) in each currency for each product. For example, if you create a product with a USD price, and want to charge a connected account for it in EUR, add a price for that product in EUR.

### Supported currencies by country

When you collect a payment from a connected account’s Stripe balance, that account’s country determines which currencies are available. The following table shows the supported currencies for Stripe balance payments from accounts in each country.

| Country        | Default Currency | Supported Currencies |
| -------------- | ---------------- | -------------------- |
| United States  | USD              | USD                  |
| Canada         | CAD              | CAD, USD             |
| Switzerland    | CHF              | CHF                  |
| United Kingdom | GBP              | GBP, EUR             |
| Austria        | EUR              | EUR                  |
| Belgium        | EUR              | EUR                  |
| Bulgaria       | EUR              | EUR                  |
| Cyprus         | EUR              | EUR                  |
| Czech Republic | CZK              | CZK, EUR             |
| Germany        | EUR              | EUR                  |
| Denmark        | DKK              | DKK, EUR             |
| Estonia        | EUR              | EUR                  |
| Spain          | EUR              | EUR                  |
| Finland        | EUR              | EUR                  |
| France         | EUR              | EUR                  |
| Greece         | EUR              | EUR                  |
| Croatia        | EUR              | EUR                  |
| Hungary        | HUF              | HUF, EUR             |
| Ireland        | EUR              | EUR                  |
| Italy          | EUR              | EUR                  |
| Lithuania      | EUR              | EUR                  |
| Luxembourg     | EUR              | EUR                  |
| Latvia         | EUR              | EUR                  |
| Malta          | EUR              | EUR                  |
| Netherlands    | EUR              | EUR                  |
| Poland         | PLN              | PLN, EUR             |
| Portugal       | EUR              | EUR                  |
| Romania        | RON              | RON, EUR             |
| Sweden         | SEK              | SEK, EUR             |
| Slovenia       | EUR              | EUR                  |
| Slovakia       | EUR              | EUR                  |
| Norway         | NOK              | NOK, EUR             |

## Refunds

You can partially or fully [refund](https://docs.stripe.com/refunds.md) any successful Stripe balance payment in the same way you refund card payments.

## Transaction failures

Payment from a connected account’s Stripe balance requires sufficient available funds in the specified presentment currency. Otherwise, the PaymentIntent fails with an `insufficient_funds` decline code. The payment fails even if the account has sufficient funds in a different currency.

We recommend configuring your integration to manage balance-related payment failures.

### Avoid balance payment failures

Because payments from a connected account’s Stripe balance rely on its available funds, you can avoid payment failures by taking steps to maximize your connected accounts’ balances.

#### Tailor connected account payout schedules

Coordinate your payout schedules with your subscription billing cycles. For example, if you charge subscription fees on the first day of each month, and schedule weekly payouts on Mondays, then months with more Mondays have more payouts. Those months have lower available balances than months with fewer payouts, making payment failures more likely.

Another way to avoid payment failures due to payouts is to change to manual payouts before a subscription payment. At a set time before each subscription payment, if a connected account has sufficient available funds, switch it to [manual payouts](https://docs.stripe.com/connect/manage-payout-schedule.md) so the subscription payment gets paid before the automatic payout clears the account. After the subscription payment, resume automatic payouts.

#### Set a minimum balance on connected accounts

You can prevent automatic payouts from reducing a connected account’s available balance below a certain amount by defining a minimum balance for that account.

You can programmatically configure minimum balances per connected account using the [Balance Settings API](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md#minimum-balances-platforms). Alternatively, you can manually set the minimum balance for each connected account in the Dashboard:

1. Find the account in your Dashboard.
1. From the account’s overflow menu (⋯), select [View Dashboard as…](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md#view-the-dashboard-as-a-connected-account).
1. Click the gear icon and select **Settings**.
1. Under Account Settings, click **Business**.
1. Select the **External payout accounts and scheduling** tab.
1. Turn on **Keep a minimum amount in your payments balance** and enter an amount.

### Handle balance payment failures

Set up [webhooks](https://docs.stripe.com/webhooks.md) and [event destinations](https://docs.stripe.com/billing/subscriptions/webhooks.md#events) to receive notifications about subscription payments. Identify payment failures by listening for the `invoice.payment_failed` event. When a payment fails:

- The PaymentIntent status changes to `requires_action`.
- The Subscription status remains `incomplete` for the current invoice.
- The Subscription continues to generate invoices, which remain in `draft` status.

#### Automatic retries

[Enable retries](https://dashboard.stripe.com/revenue_recovery/retries) for failed balance payments due to insufficient available funds on recurring subscription invoices. Automatic retries schedules 2 payment attempts following an insufficient funds failure:

- The first retry happens at least 24 hours after the failed payment.
- If needed, the second retry happens on the next Sunday following the first retry.

This retry schedule aims to give your connected account time to accumulate more funds in their Stripe balance and to avoid conflicts with scheduled payouts.

You can enable retries for any amount for no additional fee.

#### Manually retrying

If a payment from a Stripe balance fails due to insufficient available funds, you can manually retry it by following these steps:

1. Set the connected account’s payout schedule interval to `manual`.
1. Listen for the next payment that comes into the connected account, then [check the account’s available balance](https://docs.stripe.com/api/balance/balance_retrieve.md).
1. If the available balance is equal to or greater than the subscription fee, set the unpaid invoice’s payment method to `stripe_balance` and retry it. Otherwise, continue listening for payments until the available balance is enough to pay the invoice.
1. If the payment succeeds, restore the connected account’s normal payout schedule.

Instead of retrying a failed payment from a Stripe balance, you can try using a different payment method by [specifying it directly on the invoice](https://docs.stripe.com/billing/collection-method.md#set-collection-method-invoice). You can also implement a flow that allows connected accounts to [update their own subscription payment methods](https://docs.stripe.com/billing/subscriptions/payment-methods-setting.md#update-payment-method).

## Reporting and payment tracking

Payments made using a connected account’s Stripe balance generate transaction data reflecting the payment details on both the platform and the connected account.

On the platform, the payment creates a Charge and a BalanceTransaction with positive amounts. The BalanceTransaction has the following values:

- `reporting_category`: `charge`
- `source`: Charge object ID
- `type`: `payment`

On the connected account, the payment creates only a BalanceTransaction, with a negative amount and the following values:

- `description`: "Stripe balance payment - " + description from the PaymentIntent
- `reporting_category`: `stripe_balance_payment_debit`
- `source`: null
- `type`:
  - For payments: `stripe_balance_payment_debit`
  - For refunds: `stripe_balance_payment_debit_reversal`
