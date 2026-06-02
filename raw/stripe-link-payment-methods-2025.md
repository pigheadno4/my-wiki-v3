<!-- Source URL: https://docs.stripe.com/payments/wallets/link -->
<!-- Fetched: 2026-05-08 -->

# Link payment methods

Increase global conversion and reduce costs with Link payment methods.
Available in: US
Link lets your customers pay with their preferred payment methods. This allows you to reach your global consumers, increasing conversion rates and lowering costs. Link presents these alternative payment methods automatically on your checkout—no integration required.

**Supported payment methods:** [Instant Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments.md), [Klarna](https://docs.stripe.com/payments/link/klarna.md), [Pix](https://docs.stripe.com/payments/link/pix.md), [UPI](https://docs.stripe.com/payments/link/upi.md), [Stablecoins](https://docs.stripe.com/payments/link/stablecoins.md).

## How it works

Link automatically evaluates and turns on the most relevant payment methods for your customers. You don’t need to make any integration changes or handle any LPM specific configurations.

Link payments appear in your dashboard either as type `link` or type `card` with `brand=link`, depending on your [Link integration](https://docs.stripe.com/payments/link/link-payment-integrations.md). Payments always appear as Link regardless of the underlying payment method your customer used.

## Eligibility

Link dynamically evaluates and displays eligible payment methods for each checkout session. Because not every business or transaction qualifies for every payment method, Link handles the routing rules for you.

During a session, Link filters available payment methods based on several criteria, including:

- **Business eligibility**: Some payment methods restrict the types of businesses or industry verticals they support.
- **Presentment currency**: Certain payment methods require businesses to present in local currency. To learn how to adapt your checkout pages to host local currencies, see [here](https://docs.stripe.com/payments/currencies/localize-prices.md).
- **Transaction limit**: The payment amount must fall within the payment method’s supported minimum and maximum limits.
- **Customer location**: The payment method must be available in your customer’s country.
- **Recurring payment and subscription support**: Some payment methods don’t support recurring payments or off-session charges.

Link removes this complexity from your integration, so your customers only see payment methods they can use successfully.

> You can still enable payment methods outside of Link in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). However, this disables the payment method’s Link interface, so your customers can’t save payment details for faster checkout.

## Buyer experience

### For new Link customers

When a customer checks out for the first time with a payment method offered by Link:

1. At checkout, the customer enters their email. Link detects their location and shows available payment methods.
1. The customer selects their preferred method, signs up for Link, and authenticates the payment. Payment confirms instantly.
1. Link saves the details for this payment method for future use across Link-enabled merchants.

### For returning Link customers

A customer can choose their preferred payment methods and check out faster with Link.

1. Link automatically detects if a customer is enrolled to Link by using their email address, phone number, or browser cookie.
1. The customer receives a one-time passcode to authenticate with Link.
1. After authentication succeeds, Link autofills their saved payment method details and shipping information.

## Disable Link

To disable payment methods, you must turn off Link entirely. Turning off Link also removes access to Link's accelerated checkout on cards and other saved payment methods, as well as conversion benefits from returning customers.

> Because BNPL payment methods have higher fees, you can configure them individually on your [Link settings](https://dashboard.stripe.com/settings/link) page.

## See also

- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link.md)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link.md)
