<!-- Source URL: https://docs.stripe.com/crypto/onramp -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Stripe fiat-to-crypto onramp

Let your users securely purchase crypto directly from your platform.

The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform at checkout. You can customize and integrate the onramp into your product or service.

Stripe acts as the *merchant of record* (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) for these onramp transactions and assumes full liability for all fraud and disputes. We also handle all regulatory requirements, *know your customer* (Know your customer (KYC) regulations require that professionals and businesses make an effort to verify the identity, suitability, and risks involved with maintaining a business relationship. The procedures fall under the broader scope of anti-money laundering (AML) policy) (KYC) verifications, and sanctions screening. Customers can save payment methods, KYC data, and wallet information with Stripe, which reduces the number of steps required when customers return to onramp.

There are three ways to integrate with Stripe’s fiat-to-crypto onramp. To access any of the onramps, you must first [submit an onramp application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
![Stripe-hosted onramp](https://b.stripecdn.com/docs-statics-srv/assets/stripe-hosted.2b0acc9c3b13969d506d926e832d6199.png)

Use the [Stripe-hosted onramp](https://docs.stripe.com/crypto/onramp/stripe-hosted.md) to redirect your customer to check out in the standalone page.
![Embedded onramp](https://b.stripecdn.com/docs-statics-srv/assets/embedded.db26b003a0f8634c234fe29c9fc0b562.png)

Use the [Embedded onramp](https://docs.stripe.com/crypto/onramp/embedded.md) to let your customers check out directly in your website.
![The Embedded components onramp](https://b.stripecdn.com/docs-statics-srv/assets/embedded-components.d9c4061bf19169d3e5edcefcd5c87f49.png)

Use the [Embedded components onramp](https://docs.stripe.com/crypto/onramp/embedded-components.md) (mobile SDK) to let your customers check out directly in your application.

## Submit your application

To access the Stripe onramp, including in [sandboxes](https://docs.stripe.com/sandboxes.md), you must follow these steps to submit your application:

1. [Create or sign in to your Stripe account](https://dashboard.stripe.com/register).
2. If you haven’t already, [set up your Stripe account](https://dashboard.stripe.com/account/onboarding).
3. [Submit your onramp application](https://dashboard.stripe.com/crypto-onramp/get-started). We review most onramp applications within 48 hours, and notify you when you’ve been approved or if we need more information. You can check your application status anytime in the [Dashboard](https://dashboard.stripe.com/crypto-onramp/onboarding).
4. After we approve your application, [choose an integration](https://docs.stripe.com/crypto/onramp.md#integration-options) and start development using a [sandbox](https://docs.stripe.com/sandboxes.md).

## Integration options

Choose how to integrate with Stripe’s fiat-to-crypto onramp:

|  | [Stripe-hosted](https://docs.stripe.com/crypto/onramp/stripe-hosted.md) | [Embedded](https://docs.stripe.com/crypto/onramp/embedded-quickstart.md) | [Embedded components](https://docs.stripe.com/crypto/onramp/embedded-components.md) |
| --- | --- | --- | --- |
| Availability | Public preview. For access, [submit an onramp application](https://docs.stripe.com/crypto/onramp.md#submit-your-application). |
| Use case | If you want to use the onramp without writing code. Send customers to a standalone onramp at [crypto.link.com](https://crypto.link.com) | If you want to embed the onramp directly into your website or a mobile webview using the Onramp API. | If you want a native Android or iOS mobile integration with more UI customization options. Requires integration with mobile SDK and Stripe APIs. |
| Customization | Some customization, including the suggested source or destination amount, destination currency, and network | Brand customization and full parameter customization with the [Onramp API](https://docs.stripe.com/crypto/onramp/embedded.md#customize-onramp) | Full UI and parameter customization with the Onramp SDK and API |
| Hosting | Stripe-hosted | Embed in your website | Embed in your app |

1 The [Stripe-hosted onramp](https://docs.stripe.com/crypto/onramp/stripe-hosted.md) provides two different integration options with different levels of customization available.
