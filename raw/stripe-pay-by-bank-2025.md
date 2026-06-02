<!-- Source URL: https://docs.stripe.com/payments/pay-by-bank -->
<!-- Fetched: 2026-05-06 -->

# Pay by Bank payments

Offer your customers in the UK and Europe the option to pay directly from their bank account.

Pay by Bank is a single-use payment method that allows customers to pay directly from their bank account instead of using a card.

Pay by Bank runs on banking infrastructure and takes advantage of [open banking APIs](https://www.openbanking.org.uk/what-is-open-banking). When a customer chooses Pay by Bank, they first select their bank and then approve the payment on their bank’s mobile app or web portal.

Pay by Bank is available by default for payments between 0.50 GBP and 10,000 GBP. If you want to accept Pay by Bank payments over that amount, contact us using the form at [Stripe support](https://support.stripe.com).

#### Payment method properties

- **Customer locations**

  Finland, France, Germany, Ireland, United Kingdom

- **Presentment currency**

  EUR, GBP

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Real-time payments

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/pay-by-bank.md#connect)

- **Dispute support**

  [No](https://docs.stripe.com/payments/pay-by-bank.md#disputes)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/pay-by-bank.md#refunds)

## Sign up

Pay by Bank for customers in France, Germany, and Ireland is in private preview.

#### Business locations

Stripe accounts in the following countries can accept Pay by Bank payments with GBP and EUR currency settlement.

- AT
- AU
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
- SG
- SI
- SK
- US

#### Product support

- Connect
- Payment Links
- Checkout1

- Elements2

1Not supported when using Checkout in subscription mode.2Express Checkout Element and Mobile Payment Element don’t support Pay by Bank.

## Payment flow

![](assets/stripe-pay-by-bank-flow-checkout.svg)

Customer selects Pay by Bank at checkout
![](assets/stripe-pay-by-bank-flow-select-bank.svg)

Customer chooses bank and gets redirected
![](assets/stripe-pay-by-bank-flow-redirect.svg)

Customer enters account credentials
![](assets/stripe-pay-by-bank-flow-pincode-sms.svg)

Customer completes authorization process
![](assets/stripe-pay-by-bank-flow-redirect-success.svg)

Customer is notified that payment is complete
![](assets/stripe-pay-by-bank-flow-success.svg)

Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate Pay by Bank and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Pay by Bank. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

If you prefer to manually list payment methods, learn how to [manually configure Pay by Bank as a payment](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment.md).

## Refunds

You can refund Pay by Bank payments for up to 730 days (2 years) after the original payment. You can refund part of the original payment or the entire amount of the original payment. Refunds are free of charge but the processing fees for the original payment are non-refundable.

Stripe sends the refund back to the same bank account that initiated the payment. We notify you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the status of the [Refund](https://docs.stripe.com/api/refunds/object.md) object transitions to `succeeded`.

A refund can fail if the customer’s bank can’t process it correctly (for example, the bank account is closed). If a refund fails, the status of the Refund object transitions to `failed`. We’ll return the amount of the refund to your Stripe balance. You’ll then need to arrange an alternative way of providing your customer with a refund.

## Disputes

Pay by Bank payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment in their banking app. As a result, no dispute process exists that can result in a chargeback and funds being withdrawn from your Stripe account

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Pay by Bank to process payments on behalf of a connected account. Connect users can use Pay by Bank with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable Pay by Bank for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable Pay by Bank in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. To check which accounts have enabled Pay by Bank, use the `capabilities` hash in our [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-pay_by_bank_payments) to see if the `pay_by_bank_payments` capability is set to `active`.

### Enable Pay by Bank for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

To onboard connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, request the `pay_by_bank_payments` capability using the [Capabilities API](https://docs.stripe.com/api/capabilities.md) For more details, follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).
