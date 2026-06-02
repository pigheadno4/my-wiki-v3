<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PayPal standard payments

Accept PayPal payments on your website. Customers can select the PayPal button on your site and pay with any funding source linked to their PayPal account.

Use the quickstart integration to get a localhost demo up and running. The quickstart includes sample code for:

- server-side integration using the [Orders v2 API](/reference/api/rest/orders/create-order)
- client-side integration using the [PayPal JavaScript SDK v6](/reference/sdk/js/v6/reference)

After completing the quickstart, extend your PayPal integration with additional features such as order management, authorization handling, and specialized payment flows. Choose the features that match your business needs.

Add server-side endpoints to handle refunds, voids, delayed captures, and specialized checkout flows. Each feature builds on the [quickstart integration](/payments/methods/paypal/integrate).

## Common use cases

Choose the features that match your business model. You can implement all of these programmatically.

<Tip>
  Merchants can also add tracking, mark shipments, and issue refunds directly in the PayPal business dashboard.
</Tip>

### Retail and ecommerce

- [Refund a payment](/payments/methods/paypal/refund) - Handle returns and cancellations.
- [Split shipments](/payments/methods/paypal/split-shipments) - Ship items to multiple addresses.

### Services and hospitality

- [Delay capture](/payments/methods/paypal/delayed-capture): Charge after service delivery.
- [Void an authorization](/payments/methods/paypal/void-an-authorization): Cancel holds before charging.
- [Buy online, pick up in store](/payments/methods/paypal/buy-online-pick-up-in-store): Verify pickup before capturing.

### Recurring payments and extended fulfillment

- [Recurring payments](/payments/methods/paypal/save): Save and reuse stored payment methods.
- [Reauthorize an authorization](/payments/methods/paypal/reauthorize): Extend payment holds beyond 3 days.

## Authorization vs. capture

Authorization holds funds on the buyer's payment method to confirm they can pay, but doesn't transfer money.

Capture moves the funds from the buyer to the merchant account. There are two capture flows:

- Immediate capture: Authorization and capture occur in one step.
- Authorize then capture: Authorization occurs first, then capture occurs later when the merchant is ready to fulfill the order.

| Flow                   | When to use                                      | Features available                                                  |
| :--------------------- | :----------------------------------------------- | :------------------------------------------------------------------ |
| Immediate capture      | Ship within 3 days                               | Refunds, shipping and tax, split shipments                          |
| Authorize then capture | Ship after 3+ days or require order verification | Void, delayed capture, reauthorization, buy online pick up in store |

## Next steps

Complete the quickstart PayPal integration, then add features to match your business needs.
