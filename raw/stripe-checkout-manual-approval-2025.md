<!-- Source URL: https://docs.stripe.com/payments/advanced/manual-approval -->
<!-- Fetched: 2026-04-22 -->

# Manually approve payments on your server

Run custom logic on your server before finalizing a payment.

Before finalizing payment, you can run custom logic on your server based on information collected from the customer.

Use manual approval to:

- Run your own custom or third-party fraud prevention logic
- Perform inventory checks to make sure you have sufficient inventory to fulfill an order before confirming payment
- Make sure that you can support a customer’s chosen payment information before confirming payment

### Feature compatibility

You can use manual approval with the [dynamic line items](https://docs.stripe.com/payments/checkout/dynamically-update-line-items.md) feature.

> #### Payment Intents API
>
> Manual approval isn’t available for the Payment Intents API. However, you can run custom logic by [finalizing payments on your server](https://docs.stripe.com/payments/finalize-payments-on-the-server.md) with the Payment Intents API.
