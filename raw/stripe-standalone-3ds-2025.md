<!-- Source URL: https://docs.stripe.com/payments/3d-secure/standalone-3d-secure -->
<!-- Fetched: 2026-05-08 -->

# Standalone 3DS

Use the standalone 3DS API to run EMV 3D Secure (3DS) authentication and authorize the payment with any payment service provider (PSP).

By decoupling authentication and authorization, standalone 3DS allows you to use multiple payment processors or those that require specialized payment workflows.

In addition, enterprise businesses use standalone 3DS to improve payments performance through:

- API-level control over 3DS requests and the checkout flow

- Observability into 3DS responses from issuers

- Customized flows for each transaction based on business goals (fraud prevention, conversion, or cost)

The successful completion of a standalone 3DS authentication results in a 3DS cryptogram, which you might submit as part of a payment authorization request using any of the following methods:

- [Import 3D Secure results with Stripe](https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md)

- Any payment services provider (PSP) of your choice

Standalone 3DS supports Visa, Mastercard, American Express, Discover, and Cartes Bancaires card payments. It’s available to businesses on Interchange Plus pricing and in all countries where Stripe supports card payments, with the exception of Malaysia and Thailand.
