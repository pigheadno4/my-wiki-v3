<!-- Source: Stripe Terminal — Accept in-person payments with Terminal (how Terminal works) -->
<!-- Fetched: 2026-04-23 -->

# Accept in-person payments with Terminal

Learn how Terminal works.

Stripe partners with platforms that provide [no-code POS solutions](https://stripe.partners/?f_category=point-of-sale).

With [Stripe Terminal](https://docs.stripe.com/terminal.md), you can integrate Stripe payments into your existing in-person checkout flow or build in-person payments into your native mobile or web-based application.

Terminal comes with SDKs built for modern development environments, Tap to Pay on [iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) and [Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android), [pre-certified readers](https://docs.stripe.com/terminal/payments/setup-reader.md), and tools for ordering and managing readers from the Stripe Dashboard. Build a SaaS platform or marketplace using [Connect](https://docs.stripe.com/connect.md) or initiate subscriptions in-store with [Billing](https://docs.stripe.com/billing.md).

Learn about [global availability for Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md).

## Features

Use Terminal to take the complexity out of in-person payments:

- **Online compatibility**: Unify your online and in-person payments in a single system.
- **Flexible SDKs**: Use Terminal’s JavaScript, iOS, Android, or React Native SDK to integrate your existing point of sale (POS), or build a modern POS tailored to your business. Use the [server-driven integration](https://support.stripe.com/questions/terminal-server-driven-integration) to integrate directly using the Stripe API.
- **Reader choices**: Choose from [different readers](https://docs.stripe.com/terminal/payments/setup-reader.md) depending on your business needs.
- **Connection types**: [Connect](https://docs.stripe.com/terminal/payments/connect-reader.md) to your Terminal reader with Bluetooth, USB (Android with mobile readers only), or internet, depending on your physical sales environment.
- **Ordering and fleet management from the Stripe Dashboard**: Order [pre-certified readers](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md) and [monitor your fleet of readers](https://docs.stripe.com/terminal/fleet/locations-and-zones.md) from the Stripe Dashboard.

## How Terminal works

A Stripe Terminal deployment consists of four main components:

- Your web-based, mobile, or desktop application
- Your back end
- A Stripe Terminal reader
- The Stripe Terminal SDK

The SDK facilitates communication between your point of sale application logic, the firmware running on the reader, and the Stripe API so you can accept in-person payments in the same way as you accept online payments with Stripe. The SDK is available for JavaScript, iOS, Android applications. You can develop desktop applications using a server-driven integration.
![Stripe Terminal ecosystem diagram](assets/stripe-terminal-ecosystem-diagram.png)

Stripe Terminal offers a selection of [pre-certified readers](https://docs.stripe.com/terminal/payments/setup-reader.md) that accept payment details (_EMV_ (EMV refers to the standards governing acceptance of chip-enabled cards and some contactless payment methods. Today most payment cards issued around the world support EMV), contactless, and swiped), encrypt sensitive card information, and return a token to your application (through the Stripe Terminal SDK) so you can confirm payment.

Stripe Terminal works only with our pre-certified card readers and compatible Tap to Pay [iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) and [Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android) devices. This ensures secure transactions by our end-to-end encryption, by default, and up-to-date readers through our remote management tools.

You can [order readers and accessories](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md) from the Stripe Dashboard and get them shipped to a location of your choice. As a [Connect](https://docs.stripe.com/connect.md) platform, you can even enable your connected accounts to receive readers and accessories at their business location.

## Use cases

Stripe Terminal is built with developers in mind. Its flexible design supports a wide range of use cases:

- Extend your online business to the physical world.
- Enable in-person payments for your [Connect](https://docs.stripe.com/connect.md) platform, with readers for each connected account.
- Collect payments in-person and use those card details for recurring online payments with [Billing](https://docs.stripe.com/billing.md).
- Build a new, customized point of sale application or integrate with your existing point of sale application, while taking advantage of the Stripe API for processing payments.

Choose an SDK that works best for you and combine it with a reader that works best for you. This documentation provides all the information you need to design your in-person payments solution, order readers and accessories, integrate, and deploy.

## Scope of integration

The full scope of an integration consists of four major steps.

1. Use the [sample integration](https://docs.stripe.com/terminal/quickstart.md) to get up and running with an integration quickly.
1. [Design your integration](https://docs.stripe.com/terminal/designing-integration.md) to create in-person payments.
1. [Integrate the SDK](https://docs.stripe.com/terminal/payments/setup-integration.md) in your application. Use the simulated reader to emulate reader behavior for all the Terminal flows while building your initial integration.
1. [Order](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md) a physical reader and test card.

From there, explore the docs to see all you can do with your Terminal integration. We recommend [testing your integration](https://docs.stripe.com/terminal/references/testing.md) and reviewing the [checklist](https://docs.stripe.com/terminal/references/checklist.md) before going live.

## Encryption

Businesses using Terminal for in-person payments can choose between two levels of encryption. All payments using Terminal are securely encrypted using end-to-end encryption (E2EE) by default. Businesses in certain industries, such as healthcare and education, can also use the PCI-audited point-to-point encryption (P2PE) solution from Stripe.

Stripe P2PE is an optional, paid feature. See [pricing](https://stripe.com/pricing) for more information. If you’re interested in P2PE, [contact your sales representative](https://stripe.com/contact/sales) to discuss whether P2PE is a good fit for your business.

P2PE standards, which are developed by the PCI Council, add an additional decryption step through hardware security modules (HSM) before Stripe sends payment data to card networks. Our P2PE solution simplifies PCI compliance and reduces PCI audit scope and audit costs. It’s validated by a third party, ensuring compliance with PCI P2PE standards, and doesn’t require any additional integration to get started.

If you’ve enabled P2PE, consult the [P2PE Instruction Manual (PIM)](https://docs.stripecdn.com/Stripe_PCI-P2PE-PIM_v2.3.pdf) for detailed guidance. This manual provides instructions on how to properly implement our validated P2PE solution.

## See also

- [Design an integration](https://docs.stripe.com/terminal/designing-integration.md)
- [Sample integration](https://docs.stripe.com/terminal/quickstart.md)
- [Supported card brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md)
