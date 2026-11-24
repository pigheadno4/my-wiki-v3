<!-- Source URL: https://docs.stripe.com/payments/link/link-payment-methods -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Link payment methods

Increase global conversion and reduce costs with Link payment methods.
Available in: US
Link lets your customers pay with their preferred payment methods. This allows you to reach your global consumers, increasing conversion rates and lowering costs. Link presents these alternative payment methods automatically on your checkout—no integration required.

## Supported payment methods 

Link supports payment methods that are divided into four flat-rate funding source groups. When you enable Link, all payment methods in all funding source groups are automatically enabled. Groups 1-3 are included as standard components of Link and remain active while you have Link enabled.

This table reflects the supported payment methods in the Link funding source groups.

| Group code | Group name | Payment methods | Payment method documentation |
| --- | --- | --- | --- |
| `lfsg_000` | Cards | Cards | [Cards](https://docs.stripe.com/payments/cards.md) |
| `lfsg_001` | Link Group&nbsp;1 | Stablecoins | [Stablecoins](https://docs.stripe.com/payments/link/stablecoins.md) |
| `lfsg_002` | Link Group&nbsp;2 | Pix, UPI | [Pix](https://docs.stripe.com/payments/link/pix.md), [UPI](https://docs.stripe.com/payments/link/upi.md) |
| `lfsg_003` | Link Group&nbsp;3 | Instant Bank Payments | [Instant Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments.md) |
| `lfsg_004` | Link Group&nbsp;4 | Klarna | [Klarna](https://docs.stripe.com/payments/link/klarna.md) |

For terms associated with the relevant supported payment methods, see [Stripe’s Payment Terms](https://stripe.com/legal/payment-terms).

## How it works

Link automatically evaluates and turns on the most relevant payment methods for your customers. You don’t need to make any integration changes or handle any specific payment method configurations.

Link payments appear in your dashboard either as type `link` or type `card` with `brand=link`, depending on your [Link integration](https://docs.stripe.com/payments/link/link-payment-integrations.md). Payments always appear as Link regardless of the underlying payment method your customer used.

## Identify the Link funding source group

For payments made with Link, the [Charge object](https://docs.stripe.com/api/charges/object.md) includes the Link funding source group in [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details). The Link `funding_source_group` field appears in the following locations, depending on your Link integration:

- Link as a payment method: `link.funding_source_group`
- Link within a card-specific integration: `card.wallet.link.funding_source_group`

## Eligibility

Availability of payment methods within each Link Group depends on availability and business eligibility. Not all payment methods in a Link Group are available to every business. Link dynamically evaluates and displays eligible payment methods for each checkout session. Because not every business or transaction qualifies for every payment method, Link handles the routing rules for you.

During a session, Link filters available payment methods based on several criteria, including:

- **Business eligibility**: Some payment methods restrict the types of businesses or industry verticals they support.
- **Presentment currency**: Certain payment methods require businesses to present in local currency. Learn how to [adapt your checkout pages](https://docs.stripe.com/payments/currencies/localize-prices.md).
- **Transaction limit**: The payment amount must fall within the payment method’s supported minimum and maximum limits.
- **Customer location**: The payment method must be available in your customer’s country.
- **Recurring payment and subscription support**: Some payment methods don’t support recurring payments or off-session charges.

Link removes this complexity from your integration, so your customers only see payment methods they can use successfully.

Link Group fees apply as described in your Stripe Pricing Agreement regardless of your eligibility for any particular payment method. For standard pricing, see [Link pricing](https://stripe.com/link). For more information about eligibility requirements per payment method, contact your account manager.

## Customer flow 

The flow differs for new and existing Link customers.

### For new Link customers

When a customer checks out for the first time with a payment method offered by Link:

1. At checkout, the customer enters their email. Link detects their location and shows available payment methods.
2. The customer selects their preferred method, selects the option to sign up for Link, and authenticates the payment. Payment confirms instantly.
   > #### Default selection
   > 
   > You can set the default state of the opt-in checkbox in the [Link settings](https://dashboard.stripe.com/link/settings) page of the Dashboard by enabling (selected) or disabling (unselected) **Save customer information**.
3. Link saves the details for this payment method for future use across Link-enabled merchants.

### For returning Link customers

A customer can choose their preferred payment methods and check out faster with Link.

1. Link automatically detects if a customer is enrolled in Link by using their email address, phone number, or browser cookie.
2. The customer receives a one-time passcode to authenticate with Link.
3. After authentication succeeds, Link autofills their saved payment method details and shipping information.

## Disable Link

To disable payment methods in Link Groups 1–3, you must [turn off](https://dashboard.stripe.com/settings/payment_methods) Link entirely. This also removes access to Link's accelerated checkout on cards and other saved payment methods, as well as conversion benefits from returning customers.

## See also

- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link.md)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link.md)
