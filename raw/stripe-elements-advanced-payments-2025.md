<!-- Source: Stripe — Build an advanced payments integration -->
<!-- Fetched: 2026-04-21 -->
<!-- URL: https://docs.stripe.com/payments/advanced -->

# Build an advanced payments integration

Learn how to create a custom payments integration using Stripe Elements and the Checkout Sessions API or the Payment Intents API.

Use the Stripe Elements user interface with the Checkout Sessions API to create a customized payments integration. Checkout Sessions is the recommended API for most integrations, and it covers similar use cases as Payment Intents. The Payment Intents API is also available for building your own checkout flow. To understand which API is right for your business, compare the Checkout Sessions and Payment Intents APIs.

## ELEMENTS

Build a custom integration with full UI control

Use Stripe Elements to start building your own custom integration to accept payments.

## Features and availability

|  | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| UI | Elements | Elements |
| API | Checkout Sessions | PaymentIntents |
| Integration effort | Low coding | The most coding—you build checkout features yourself |
| Hosting | Embed on your site | Embed on your site |
| UI customization | Extensive customization with Appearance API | Extensive customization with Appearance API |

### PAYMENT METHODS

*For detailed support for each payment method, see learn more about payment methods.*

|  | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Dynamically display 40+ payment methods | ✓ | ✓ |
| Manage payment methods in the Stripe Dashboard without coding | ✓ | ✓ |
| Faster checkout with Link | ✓ | ✓ |
| Custom payment methods | ✓ | ✓ |

## Compare payment scenario support

See how Stripe supports different payment scenarios by each integration path.

|  | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Set up future payments | ✓ | ✓ |
| Save payment details during payment | ✓ | ✓ |
| Place a hold on a payment method | ✓ | ✓ |
| Finalize payments on your server | ✓ | ✓ |
| Multi-step payment flow | ✓ | ✓ |

### FLEXIBLE PAYMENT SCENARIOS

*Only available on IC+ pricing.*

|  | Checkout Sessions API | Payment Intents API |
| --- | --- | --- |
| Multicapture | ✓ | ✓ |
| Overcapture | ✓ | ✓ |
| Extended authorization | ✓ | ✓ |
| Incremental authorization | ✓ | ✓ |

## Customize checkout

### Customize look and feel

Customize the appearance and behavior of your checkout page.

### Manage payment methods

Present the most applicable payment methods for each customer and each location.

### One-click checkout options

Show multiple one-click payment buttons with a single component.

### Send email receipts

Send payment or refund receipts automatically.

## Collect different payment details

### Collect additional information

Collect shipping and other customer info during checkout.

### Collect taxes

Use Stripe Tax APIs to implement tax calculations in your custom integration.

### Flexible payment scenarios

Support complex payment flows through flexible and customizable acquiring features.

## Choose when you collect payment

### Subscriptions

Create and manage subscriptions to accept recurring payments.

### Set up future payments

Save payment details and charge your customers later.

### Save payment details during payment

Save payment details during a payment.
