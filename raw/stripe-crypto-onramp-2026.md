<!-- Source URL: https://docs.stripe.com/crypto/onramp -->
<!-- Fetched: 2026-05-11 -->

# Stripe fiat-to-crypto onramp

Let your users securely purchase crypto directly from your platform or Dapp.

The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application (Dapp) at checkout. You can customize and integrate the onramp into your product or service.

Stripe acts as the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) for these onramp transactions and assumes full liability for all fraud and disputes. We also handle all regulatory requirements, _know your customer_ (Know your customer (KYC) regulations require that professionals and businesses make an effort to verify the identity, suitability, and risks involved with maintaining a business relationship. The procedures fall under the broader scope of anti-money laundering (AML) policy) (KYC) verifications, and sanctions screening. Customers can save payment methods, KYC data, and wallet information with Stripe, which reduces the number of steps required when customers return to onramp.

There are three ways to integrate with Stripe’s fiat-to-crypto onramp. To access any of the onramps, you must first [submit an onramp application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
![Stripe-hosted onramp](assets/stripe-onramp-stripe-hosted.png)

Use the [Stripe-hosted onramp](https://docs.stripe.com/crypto/onramp/stripe-hosted.md) to redirect your customer to check out in the standalone page.
![Embedded onramp](assets/stripe-onramp-embedded.png)

Use the [Embedded onramp](https://docs.stripe.com/crypto/onramp/embedded.md) to let your customers check out directly in your website.
![The Embedded components onramp](assets/stripe-onramp-embedded-components.png)

Use the [Embedded components onramp](https://docs.stripe.com/crypto/onramp/embedded-components.md) (mobile SDK) to let your customers check out directly in your application. [Sign up to join the private preview](https://docs.stripe.com/crypto/onramp.md#sign-up).

## Submit your application

To access the Stripe onramp, including testing environments, you must follow these steps to submit your application:

1. [Create or sign in to your Stripe account](https://dashboard.stripe.com/register).
1. If you haven’t already, [set up your Stripe account](https://dashboard.stripe.com/account/onboarding).
1. [Submit your onramp application](https://dashboard.stripe.com/crypto-onramp/get-started). We review most onramp applications within 48 hours, and notify you when you’ve been approved or if we need more information. You can check your application status anytime in the [Dashboard](https://dashboard.stripe.com/crypto-onramp/onboarding).
1. After we approve your application, [choose an integration](https://docs.stripe.com/crypto/onramp.md#integration-options) and start development using a [sandbox](https://docs.stripe.com/sandboxes.md).

## Integration options

Choose how to integrate with Stripe’s fiat-to-crypto onramp:

|               | [Stripe-hosted](https://docs.stripe.com/crypto/onramp/stripe-hosted.md)                                                                 | [Embedded](https://docs.stripe.com/crypto/onramp/embedded-quickstart.md)                                                                       | [Embedded components](https://docs.stripe.com/crypto/onramp/embedded-components.md)                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Availability  | Public preview. For access, [submit an onramp application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).           | Public preview. For access, [submit an onramp application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).                  | Private preview. For access, [sign up](https://docs.stripe.com/crypto/onramp.md#sign-up).                                                        |
| Use case      | If you want to use the onramp without writing code. Send customers to a standalone onramp at [crypto.link.com](https://crypto.link.com) | If you want to embed the onramp directly into your website or a mobile webview using the Onramp API.                                           | If you want a native Android or iOS mobile integration with more UI customization options. Requires integration with mobile SDK and Stripe APIs. |
| Customization | Some customization, including the suggested source or destination amount, destination currency, and network                             | Brand customization and full parameter customization with the [Onramp API](https://docs.stripe.com/crypto/onramp/embedded.md#customize-onramp) | Full UI and parameter customization with the Onramp SDK and API                                                                                  |
| Hosting       | Stripe-hosted                                                                                                                           | Embed in your website                                                                                                                          | Embed in your app                                                                                                                                |

1 The [Stripe-hosted onramp](https://docs.stripe.com/crypto/onramp/stripe-hosted.md) provides two different integration options with different levels of customization available.

## Sign up
