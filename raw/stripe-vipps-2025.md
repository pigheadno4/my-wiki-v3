<!-- Source URL: https://docs.stripe.com/payments/vipps -->
<!-- Fetched: 2026-05-08 -->

# Vipps payments

Learn about Vipps, a common payment method in Norway.

Vipps is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) card wallet payment method used in Norway. It allows your customer to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using the Vipps app.

When your customer pays with Vipps, Stripe performs a card transaction using the card data we receive from Vipps. The processing of the card transaction is invisible to your integration, and Stripe [immediately notifies you](https://docs.stripe.com/payments/payment-methods.md#payment-notification) whether the payment succeeded or failed.

> Vipps is in private preview. While in private preview, you must include the `vipps_preview=v1` header in all API requests that include Vipps. See the [integration docs](https://docs.stripe.com/payments/vipps/accept-a-payment.md) for examples that include this header.

#### Payment method properties

- **Customer locations**

  Norway

- **Presentment currency**

  NOK

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/vipps.md#connect)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/vipps.md#disputed-payments)

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/vipps.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Vipps payments:

- AT
- BE
- BG
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
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

#### Product support

- Connect
- Checkout1
- Payment Links2
- Elements3

1Not supported when using Checkout in subscription mode or setup mode.2Only supports payment links created through the API.3Express Checkout Element doesn’t support Vipps.

## Payment flow

Customers enter their phone number linked with Vipps and receive a push notification on their Vipps app to authorize the payment.
![](assets/stripe-vipps-flow.mp4)

## Get started

Learn how to [manually configure Vipps as a payment method](https://docs.stripe.com/payments/vipps/accept-a-payment.md).

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Vipps to process payments. Connect users can use Vipps with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable Vipps for connected accounts

Connected accounts with access to the full Stripe Dashboard can enable Vipps in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). To check which accounts have enabled Vipps, use the `capabilities` hash in the [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-vipps_payments) to see if the `vipps_payments` capability is set to `active`.

For connected accounts that don’t have access to the full Stripe Dashboard, see [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). The name of the connected account is the name that customers see during checkout and in the Vipps app.

## Disputes

Vipps allows transaction disputes. Customers can open disputes directly with their cards issuer for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

You can submit evidence to contest a dispute directly. The dispute process is the same as for card payments. Learn how to [manage disputes](https://docs.stripe.com/disputes/responding.md).

## Refunds

Vipps supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Restricted business categories

In addition to the categories of [businesses restricted from using Stripe](https://stripe.com/restricted-businesses), the following categories are specifically prohibited from using Vipps:

- Cryptocurrencies (Restricted)
- Stock trade
- Gambling
- Betting
- Bonds
- Money transfers
- Debt collection
- Multi-level marketing and pyramid schemes

For more information about Vipps eligibility for your account, review your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.

## Current limitations

### BankAxept support

Stripe doesn’t support the BankAxept card network. If a customer pays with a BankAxept-branded card, Stripe processes the payment on the Visa and Mastercard networks instead.

## Fees

Stripe receives card data from Vipps to process card transactions using Stripe’s Visa and Mastercard integrations. Because Vipps payments are card transactions, you incur the following fees for each successful transaction:

- Stripe processing fees associated with the card transaction
- Applicable taxes
- Vipps transaction processing fee

The Vipps transaction fee isn’t subtracted immediately from the transaction. Instead, Stripe bills them once a day.

### Stripe processing fees and taxes

After a successful transaction, Stripe automatically deducts the Stripe transaction fees and applicable taxes from the original transaction amount and provides the remaining amount on your Stripe balance. These fees are identical to a standard card transaction.

Vipps is subject to the [standard payout schedule](https://docs.stripe.com/payouts.md) applicable to your country.

### Vipps processing fee

The Vipps processing fee isn’t presented within the net amount of a successful transaction. Instead, Stripe bills the Vipps processing fee once a day, at which point we automatically deduct the sum that you owe from your [Stripe balance](https://dashboard.stripe.com/balance).
