<!-- Source: Stripe Terminal — Design a custom POS integration -->
<!-- Fetched: 2026-04-24 -->

# Design a custom POS integration

Choose your country, reader, and integration type to learn how to build your custom point of sale.

> #### Reader details
>
> For more information about the differences between readers, see [Select your reader](https://docs.stripe.com/terminal/payments/setup-reader.md).

#### Item 1

#### Item 1

![Stripe Reader M2](assets/stripe-terminal-m2-reader.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)

[Product sheet](https://stripe.com/m2/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## M2 reader features

- Miniature reader
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using Bluetooth or USB
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader M2 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a [Location](https://docs.stripe.com/api/terminal/locations.md) to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

![Stripe Reader M2](assets/stripe-terminal-m2-reader.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)

[Product sheet](https://stripe.com/m2/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## M2 reader features

- Miniature reader
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using Bluetooth or USB
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader M2 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a [Location](https://docs.stripe.com/api/terminal/locations.md) to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

![Stripe Reader M2](assets/stripe-terminal-m2-reader.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)

[Product sheet](https://stripe.com/m2/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## M2 reader features

- Miniature reader
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using Bluetooth
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader M2 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a [Location](https://docs.stripe.com/api/terminal/locations.md) to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

![Stripe Reader M2](assets/stripe-terminal-m2-reader.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)

[Product sheet](https://stripe.com/m2/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## M2 reader features

- Miniature reader
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader M2 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a [Location](https://docs.stripe.com/api/terminal/locations.md) to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 5

![Stripe Reader M2](assets/stripe-terminal-m2-reader.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md)

[Product sheet](https://stripe.com/m2/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## M2 reader features

- Miniature reader
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader M2 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a [Location](https://docs.stripe.com/api/terminal/locations.md) to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

#### Item 1

![](assets/stripe-terminal-wisepad3-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)

[Product sheet](https://docs.stripecdn.com/wp3-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePad 3 reader features

- Reader with keypad and LCD display
- Built for handheld or countertop use
- Contactless and chip payments

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using Bluetooth or USB
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePad 3 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

![](assets/stripe-terminal-wisepad3-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)

[Product sheet](https://docs.stripecdn.com/wp3-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePad 3 reader features

- Reader with keypad and LCD display
- Built for handheld or countertop use
- Contactless and chip payments

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using Bluetooth or USB
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePad 3 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

![](assets/stripe-terminal-wisepad3-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)

[Product sheet](https://docs.stripecdn.com/wp3-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePad 3 reader features

- Reader with keypad and LCD display
- Built for handheld or countertop use
- Contactless and chip payments

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using Bluetooth
- Use an internet connection or [operate offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md)

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePad 3 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

![](assets/stripe-terminal-wisepad3-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)

[Product sheet](https://docs.stripecdn.com/wp3-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePad 3 reader features

- Reader with keypad and LCD display
- Built for handheld or countertop use
- Contactless and chip payments

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePad 3 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 5

![](assets/stripe-terminal-wisepad3-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md)

[Product sheet](https://docs.stripecdn.com/wp3-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePad 3 reader features

- Reader with keypad and LCD display
- Built for handheld or countertop use
- Contactless and chip payments

Not a coder? [Find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:
![Integration architecture for mobile readers](assets/stripe-terminal-bluetooth-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePad 3 reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. Connect to the reader [using Bluetooth](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=usb)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

#### Item 1

![](assets/stripe-terminal-wisepose-e-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)

[Product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePOS E reader

- Smart reader with touchscreen
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using WiFi or Ethernet

Not a coder? [Find a Stripe partner who supports Terminal](https://support.stripe.com/questions/recommended-resources-and-partners-for-stripe-terminal#point-of-sale).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.
![WisePOS E Integration Architecture](assets/stripe-terminal-wisepose-integration-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePOS E reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

![](assets/stripe-terminal-wisepose-e-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)

[Product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePOS E reader

- Smart reader with touchscreen
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using WiFi or Ethernet

Not a coder? [Find a Stripe partner who supports Terminal](https://support.stripe.com/questions/recommended-resources-and-partners-for-stripe-terminal#point-of-sale).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.
![WisePOS E Integration Architecture](assets/stripe-terminal-wisepose-integration-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePOS E reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

![](assets/stripe-terminal-wisepose-e-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)

[Product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePOS E reader

- Smart reader with touchscreen
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using WiFi or Ethernet

Not a coder? [Find a Stripe partner who supports Terminal](https://support.stripe.com/questions/recommended-resources-and-partners-for-stripe-terminal#point-of-sale).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.
![WisePOS E Integration Architecture](assets/stripe-terminal-wisepose-integration-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePOS E reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

![](assets/stripe-terminal-wisepose-e-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)

[Product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePOS E reader

- Smart reader with touchscreen
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the JavaScript SDK

- Write a browser-based point-of-sale app
- Access Stripe features with the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md)
- Connect your app to the reader using WiFi or Ethernet

### Terminal JavaScript SDK requirements

When you integrate with [smart readers](https://docs.stripe.com/terminal/smart-readers.md) using the JavaScript SDK, make sure your network meets [our network requirements](https://docs.stripe.com/terminal/network-requirements.md).

Not a coder? [Find a Stripe partner who supports Terminal](https://support.stripe.com/questions/recommended-resources-and-partners-for-stripe-terminal#point-of-sale).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.
![WisePOS E Integration Architecture](assets/stripe-terminal-wisepose-integration-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePOS E reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 5

![](assets/stripe-terminal-wisepose-e-floating.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md)

[Product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## WisePOS E reader

- Smart reader with touchscreen
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it in a server-driven integration

- Write your point-of-sale app for any device
- Access Stripe features using the Stripe API
- Communicate with the reader using Stripe and your server

### Limitations

Server-driven integration doesn’t support:

- [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md)
- [Collect payments while offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet)

Not a coder? [Find a Stripe partner who supports Terminal](https://support.stripe.com/questions/recommended-resources-and-partners-for-stripe-terminal#point-of-sale).

## Architecture

In a server-driven integration, your POS device connects to your server. Then, your server makes [Stripe API](https://docs.stripe.com/api.md) calls, and Stripe updates the reader and returns the result.

The structure of the integration looks like this:
![Server-driven integration architecture](assets/stripe-terminal-server-driven-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a BBPOS WisePOS E reader and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). Then, when you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations might use addresses that represent a primary place of business.

## Next steps

- See [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

#### Item 1

> #### Verifone reader support
>
> Verifone reader support is in public preview for the United States and Canada. Some verifone readers are in private preview for Ireland and the United Kingdom (V660p, UX700, P630) and for Singapore (V660p, P630). To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

## Verifone readers

#### Item 1

Stripe supports two Verifone readers: V660p and P630. These are the basic features:

#### Item 2

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 3

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 4

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

#### Item 5

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

- Smart reader with touchscreen
- For handheld or countertop use
- Optional dock available for mounted or countertop use cases for the V660p
- Contactless, chip, and swipe payments

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your Android application using the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code

#### Item 2

> #### Verifone reader support
>
> Verifone reader support is in public preview for the United States and Canada. Some verifone readers are in private preview for Ireland and the United Kingdom (V660p, UX700, P630) and for Singapore (V660p, P630). To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

## Verifone readers

#### Item 1

Stripe supports two Verifone readers: V660p and P630. These are the basic features:

#### Item 2

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 3

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 4

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

#### Item 5

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

- Smart reader with touchscreen
- For handheld or countertop use
- Optional dock available for mounted or countertop use cases for the V660p
- Contactless, chip, and swipe payments

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using WiFi or Ethernet

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code

#### Item 3

> #### Verifone reader support
>
> Verifone reader support is in public preview for the United States and Canada. Some verifone readers are in private preview for Ireland and the United Kingdom (V660p, UX700, P630) and for Singapore (V660p, P630). To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

## Verifone readers

#### Item 1

Stripe supports two Verifone readers: V660p and P630. These are the basic features:

#### Item 2

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 3

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 4

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

#### Item 5

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

- Smart reader with touchscreen
- For handheld or countertop use
- Optional dock available for mounted or countertop use cases for the V660p
- Contactless, chip, and swipe payments

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your iOS application using the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code

#### Item 4

> #### Verifone reader support
>
> Verifone reader support is in public preview for the United States and Canada. Some verifone readers are in private preview for Ireland and the United Kingdom (V660p, UX700, P630) and for Singapore (V660p, P630). To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

## Verifone readers

#### Item 1

Stripe supports two Verifone readers: V660p and P630. These are the basic features:

#### Item 2

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 3

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 4

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

#### Item 5

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

- Smart reader with touchscreen
- For handheld or countertop use
- Optional dock available for mounted or countertop use cases for the V660p
- Contactless, chip, and swipe payments

## Use it with the JavaScript SDK

- Write a browser-based point-of-sale app
- Access Stripe features with the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

### Terminal JavaScript SDK requirements

When you integrate with [smart readers](https://docs.stripe.com/terminal/smart-readers.md) using the JavaScript SDK, make sure your network meets [our network requirements](https://docs.stripe.com/terminal/network-requirements.md).

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your web application using the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md). The application runs in the mobile browser on the POS device, and uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code

#### Item 5

> #### Verifone reader support
>
> Verifone reader support is in public preview for the United States and Canada. Some verifone readers are in private preview for Ireland and the United Kingdom (V660p, UX700, P630) and for Singapore (V660p, P630). To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

## Verifone readers

#### Item 1

Stripe supports two Verifone readers: V660p and P630. These are the basic features:

#### Item 2

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 3

Stripe supports four Verifone readers: V660p, UX700, M425, and P630. These are the basic features:

#### Item 4

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

#### Item 5

Stripe supports three Verifone readers: V660p, UX700, and P630. These are the basic features:

- Smart reader with touchscreen
- For handheld or countertop use
- Optional dock available for mounted or countertop use cases for the V660p
- Contactless, chip, and swipe payments

## Use it in a server-driven integration

- Write your point-of-sale app for any device
- Access Stripe features using the Stripe API
- Communicate with the reader using Stripe and your server

### Limitations

Server-driven integration doesn’t support:

- [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md)
- [Collect payments while offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

In a server-driven integration, your POS device connects to your server. Your server then makes [Stripe API](https://docs.stripe.com/api.md) calls, and Stripe updates the reader and returns the result.

The structure of the integration looks like this:
![Server-driven integration architecture](assets/stripe-terminal-server-driven-smart-reader.png)

## Prototyping

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code

#### Item 5

#### Item 1

![two views of the S700 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s700/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S700 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your Android application using the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S700 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

![two views of the S700 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s700/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S700 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using WiFi or Ethernet

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S700 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

![two views of the S700 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s700/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S700 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your iOS application using the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S700 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

![two views of the S700 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s700/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S700 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it with the JavaScript SDK

- Write a browser-based point-of-sale app
- Access Stripe features with the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

### Terminal JavaScript SDK requirements

When you integrate with [smart readers](https://docs.stripe.com/terminal/smart-readers.md) using the JavaScript SDK, make sure your network meets [our network requirements](https://docs.stripe.com/terminal/network-requirements.md).

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your web application using the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md). The application runs in the mobile browser on the POS device, and uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S700 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 5

![two views of the S700 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s700/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S700 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments

## Use it in a server-driven integration

- Write your point-of-sale app for any device
- Access Stripe features using the Stripe API
- Communicate with the reader using Stripe and your server

### Limitations

Server-driven integration doesn’t support:

- [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md)
- [Collect payments while offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

In a server-driven integration, your POS device connects to your server. Your server then makes [Stripe API](https://docs.stripe.com/api.md) calls, and Stripe updates the reader and returns the result.

The structure of the integration looks like this:
![Server-driven integration architecture](assets/stripe-terminal-server-driven-smart-reader.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S700 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 6

#### Item 1

![two views of the S710 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s710/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S710 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments
- Cellular enabled

## Use it with the Android SDK

- Write an Android point-of-sale app
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your Android application using the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S710 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

![two views of the S710 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s710/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S710 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments
- Cellular enabled

## Use it with the React Native SDK

- Write a React Native point-of-sale app
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/)
- Connect your app to the reader using WiFi or Ethernet

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S710 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

![two views of the S710 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s710/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S710 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments
- Cellular enabled

## Use it with the iOS SDK

- Write an iOS point-of-sale app
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your iOS application using the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html). The application uses the SDK to communicate with the reader, your backend, and the Stripe API.
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S710 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 4

![two views of the S710 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s710/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S710 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments
- Cellular enabled

## Use it with the JavaScript SDK

- Write a browser-based point-of-sale app
- Access Stripe features with the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md)
- Connect your app to the reader using WiFi or Ethernet (with the dock accessory)

### Terminal JavaScript SDK requirements

When you integrate with [smart readers](https://docs.stripe.com/terminal/smart-readers.md) using the JavaScript SDK, make sure your network meets [our network requirements](https://docs.stripe.com/terminal/network-requirements.md).

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

Write your web application using the [Terminal JavaScript SDK](https://docs.stripe.com/terminal/references/api/js-sdk.md). The application runs in the mobile browser on the POS device, and uses the SDK to communicate with the reader, your backend, and the Stripe API.

The structure of the integration looks like this:
![Smart reader integration architecture](assets/stripe-terminal-smart-reader-architecture.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S710 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 5

![two views of the S710 reader](assets/stripe-terminal-s700-3d-view.png)

[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers.md#pricing)

[Reader instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)

[Product sheet](https://stripe.com/s710/manual)

[Set up your integration](https://docs.stripe.com/terminal/quickstart.md)

## S710 reader

- All-in-one, Android-based smart reader that can run your [custom application](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)
- For handheld or countertop use; optional dock available for mounted or countertop use cases
- Contactless, chip, and swipe payments
- Cellular enabled

## Use it in a server-driven integration

- Write your point-of-sale app for any device
- Access Stripe features using the Stripe API
- Communicate with the reader using Stripe and your server

### Limitations

Server-driven integration doesn’t support:

- [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md)
- [Collect payments while offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet)

If you don’t write code, you can [find a Stripe partner who supports Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

In a server-driven integration, your POS device connects to your server. Your server then makes [Stripe API](https://docs.stripe.com/api.md) calls, and Stripe updates the reader and returns the result.

The structure of the integration looks like this:
![Server-driven integration architecture](assets/stripe-terminal-server-driven-smart-reader.png)

## Prototyping

You can use simulated and physical readers as you’re building your integration.

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md) demonstrates an app at this stage of development.

### Using a physical reader

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Order a Stripe Reader S710 and physical test cards](https://dashboard.stripe.com/terminal/shop)
1. [Connect to the reader over the internet](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including a simulated reader. Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- [See the Terminal quickstart](https://docs.stripe.com/terminal/quickstart.md) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md) to start writing your own code
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 7

#### Item 1

## Tap to Pay reader features

- Use compatible Android devices as payment terminals.
- Android devices support a range of use cases, including mobile, countertop, and handheld.
- Supports contactless payments only.

## Use it with the Android SDK

- Write an Android point-of-sale mobile application.
- Access Stripe features with the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/).
- Supports WiFi and Cellular connectivity.

Not a coder? [Accept payments from the Stripe Dashboard mobile app](https://docs.stripe.com/no-code/in-person.md).

## Architecture

Write your application using the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/). The application uses the SDK to communicate with your back end and the Stripe API.

The structure of the integration looks like this:
![Tap to pay integration architecture](assets/stripe-terminal-tap-to-pay-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with simulated payments and test cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=android) demonstrates an app at this stage of development.

### Using a physical device

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. [Verify that your Android device meets the requirements](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices)
1. Build and release your mobile application
1. [Connect to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=tap-to-pay)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards)

## Next steps

- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=android) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android) to start writing your own code
- [Order physical test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 2

## Tap to Pay reader features

- Use compatible iPhones as payment terminals.
- Apple devices support mobile and handheld use cases.
- Supports contactless payments only.

## Use it with the iOS SDK

- Write an iOS point-of-sale mobile application.
- Access Stripe features with the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/).
- Supports WiFi and Cellular connectivity.

Not a coder? [Accept payments from the Stripe Dashboard mobile app](https://docs.stripe.com/no-code/in-person.md).

## Architecture

Write your application using the [Terminal iOS SDK](https://stripe.dev/stripe-terminal-ios/docs/index.html). The application uses the SDK to communicate with your back end and the Stripe API.

The structure of the integration looks like this:
![Tap to pay integration architecture](assets/stripe-terminal-tap-to-pay-architecture.png)

## Prototyping

### Using the simulated reader

When you begin writing your application, you can test it with a simulated reader and simulated cards—no reader hardware required. This lets you build and verify your complete integration without needing physical hardware. The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=ios) demonstrates an app at this stage of development.

You need to request a [development Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file) before you can test your application. After you get the Entitlement, you can test it using simulated payments and test cards.

### Using a physical device

When you’re ready to work with actual hardware, you can extend your integration to a physical device. Follow these steps:

1. Build a mobile application that meets [Apple’s requirements](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#best-practices).
1. [Connect to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay) and [accept Apple’s Terms and Conditions](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#account-linking-and-apple-terms-and-conditions).
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards).
1. [Request a Publishing Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file), which requires Apple to review your application.
1. After receiving approval, publish your mobile application.
1. Market your app using the [Tap to Pay on iPhone Marketing Guide and Toolkit](https://partners.marketingtools.apple.com/vip/a53dfe31d8a1f925ac51a7d7f531f4a037b06eb3663adb6272d2668ba0c48653).

## Organize readers and locations

Stripe requires a Location to be associated with every Terminal reader, including the simulated reader.

Before you connect a reader to a Terminal integration, you must create one or more [Locations](https://docs.stripe.com/api/terminal/locations.md), either [in the Dashboard](https://dashboard.stripe.com/terminal/locations/manage) or [using the API](https://docs.stripe.com/terminal/fleet/locations-and-zones.md#create-locations-and-zones). When you [connect to your reader](https://docs.stripe.com/terminal/payments/connect-reader.md), specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations can use addresses that represent a primary place of business.

## Next steps

- Request [an Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file)
- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=ios) for a full code example using the simulated reader
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios) to start writing your own code
- [Order physical test cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work with physical hardware

#### Item 3

## Tap to Pay reader features

- Use compatible iPhones and Android devices as payment terminals.
- Apple devices support mobile and handheld use cases. Android devices support a range of use cases, including mobile, countertop, and handheld.
- Supports contactless payments only.

## Use it with the React Native SDK

- Write a point-of-sale mobile application.
- Access Stripe features with the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/).
- Supports WiFi and Cellular connectivity.

Not a coder? [Accept payments from the Stripe Dashboard mobile app](https://docs.stripe.com/no-code/in-person.md).

## Architecture

Write your application using the [Terminal React Native SDK](https://stripe.dev/stripe-terminal-react-native/). The application uses the SDK to communicate with your back end and the Stripe API.

The structure of the integration looks like this:
![Tap to pay integration architecture](assets/stripe-terminal-tap-to-pay-architecture.png)

## Prototyping

While building your application, you can test it with simulated payments and test cards—no reader hardware required. However, if using iOS, you first need to request and receive a [development Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file). The [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=react-native) demonstrates an app at this stage of development.

When you’re ready to accept live payments, follow these steps:

1. Build a mobile application. If using iOS, make sure the app meets [Apple’s requirements](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#best-practices).
1. [Connect to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay). If using iOS, [accept Apple’s Terms and Conditions](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=tap-to-pay#account-linking-and-apple-terms-and-conditions)
1. [Test your logic with physical test cards](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards).
1. If using iOS, [Request a Publishing Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file), which requires Apple to review your application.
1. Publish your mobile application.
1. If using iOS, Market your app using the [Tap to Pay on iPhone Marketing Guide and Toolkit](https://partners.marketingtools.apple.com/vip/a53dfe31d8a1f925ac51a7d7f531f4a037b06eb3663adb6272d2668ba0c48653).

## Next steps

- Request [an Entitlement from Apple](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#entitlements-build-file).
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native) to start writing code.
- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart.md?reader=ttp&platform=react-native) for a full code example.
- [Order physical test cards](https://dashboard.stripe.com/terminal/shop).
