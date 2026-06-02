<!-- Source URL: https://docs.stripe.com/payments/moto -->
<!-- Fetched: 2026-05-11 -->

# Mail order telephone order (MOTO)

​​Learn how to collect mail order and telephone order (MOTO) payments, adhering to SCA rules.

In the context of _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) regulation, MOTO transactions are [out-of-scope](https://stripe.com/guides/strong-customer-authentication#phone-sales). Your integration must correctly flag transactions as MOTO. Similar to other exemptions, the cardholder’s bank makes the final decision to accept or reject the transaction. If their bank doesn’t support claiming the MOTO exemption, the customer must complete the payment on your website.

The Payment Intents and _Setup Intents APIs_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method) let you flag card payments as `moto` with a parameter.

> Before you can enable MOTO transactions, Stripe must verify that you’re PCI compliant. Contact [Stripe support](https://support.stripe.com/) for more information.
