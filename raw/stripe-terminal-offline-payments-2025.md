<!-- Source: Stripe Terminal — Accept offline payments -->
<!-- Fetched: 2026-04-24 -->

# Accept offline payments

Accept payments when you have internet connectivity issues.

If you have internet connectivity issues, Stripe Terminal allows you to store payments locally on your POS device or smart reader. When a network connection is restored, the SDK or smart reader automatically forwards any stored payments to Stripe.

From your application’s perspective, the payment collection process is similar to operating online. While offline, the smart reader or SDK securely stores the payment information and automatically forwards the stored payments when connectivity is restored. The SDK allows you to handle offline-related events using callbacks to your application.

## Availability

### Payment methods

| Payment Method    | Supported        |
| ----------------- | ---------------- |
| Visa              | ✓ Supported1,2   |
| Mastercard        | ✓ Supported1,2   |
| Discover          | ✓ Supported1,2   |
| American Express  | ✓ Supported1,2   |
| China UnionPay    | ✓ Supported1,2   |
| JCB               | ✓ Supported1,2   |
| Maestro           | ✓ Supported1,2   |
| eftpos            | ✓ Supported1,2,3 |
| Cartes Bancaires  | ✓ Supported1,2,3 |
| NYCE, PULSE, STAR | - Unsupported    |
| girocard          | - Unsupported    |
| Interac           | - Unsupported    |
| QR code payments  | - Unsupported    |

1 Physical cards and NFC-based [mobile wallets](https://docs.stripe.com/payments/wallets.md) are supported. Swiping isn’t allowed. 2 If you’re collecting payments in the European Economic Area, customers are required to insert their card and enter a PIN. 3 Co-branded cards are routed through the international scheme. For more information, see [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires.md) or [eftpos Australia](https://docs.stripe.com/payments/eftpos-australia.md)

### Readers

| Device category | Readers                                                                                                                                                                                                                                        | Connection type               | Integration type                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------- |
| Bluetooth       | [BBPOS Chipper 2X BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt.md), [Stripe Reader M2](https://docs.stripe.com/terminal/readers/stripe-m2.md), [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) | Bluetooth, USB (Android only) | iOS SDK, Android SDK, React Native SDK |
| Internet        | [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md)                                                                 | Internet                      | iOS SDK, Android SDK, React Native SDK |

### Features

| Feature                                                                                                    | Bluetooth readers | Internet readers |
| ---------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-reader.md)**                      | - Unsupported     | ✓ Supported      |
| **[Ability to run custom POS app](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md)** | - Unsupported     | ✓ Supported      |
| **[Extended authorizations](https://docs.stripe.com/terminal/features/extended-authorizations.md)**        | ✓ Supported       | ✓ Supported      |
| **[Incremental authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations.md)**  | - Unsupported     | - Unsupported    |
| **[Ability to collect input on-screen](https://docs.stripe.com/terminal/features/collect-inputs.md)**      | - Unsupported     | ✓ Supported      |

# Bluetooth readers

> This is a Bluetooth readers for when reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/features/operate-offline/overview?reader-type=bluetooth.

## Collect a payment while offline

The following diagram describes the payment collection process when the Terminal SDK is offline. When storing payments, the SDK stores the payments to disk. You can safely reboot the POS device even if it has stored offline payments. When you re-initialize the SDK and it has reestablished a connection to the internet, and the SDK resumes forwarding any remaining stored payments.
A high-level diagram that shows how offline payments are stored. (See full diagram at https://docs.stripe.com/terminal/features/operate-offline/overview)

### Forward stored payments when online

The following diagram describes how stored payments are forwarded after connectivity is restored.
A high-level diagram that shows how offline payments are forwarded to the Stripe backend. (See full diagram at https://docs.stripe.com/terminal/features/operate-offline/overview)

## See also

- [Collect card payments while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md)

# Internet readers

> This is a Internet readers for when reader-type is internet. View the full page at https://docs.stripe.com/terminal/features/operate-offline/overview?reader-type=internet.

## Collect a payment while offline

The following diagram shows how a smart reader processes payment collection while offline and stores payments to disk. You can safely reboot the reader, even with stored offline payments. After you reboot the reader and it reconnects to the internet, you can connect your POS application to the reader. The reader then resumes forwarding any remaining stored payments.
A high-level diagram that shows how offline payments are stored. (See full diagram at https://docs.stripe.com/terminal/features/operate-offline/overview)

### Forward stored payments when online

The following diagram describes how stored payments are forwarded after connectivity is restored.
A high-level diagram that shows how offline payments are forwarded to the Stripe backend. (See full diagram at https://docs.stripe.com/terminal/features/operate-offline/overview)

## See also

- [Collect card payments while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md)
