<!-- Source URL: https://docs.stripe.com/crypto/onramp/embedded -->
<!-- Fetched: 2026-05-11 -->

# Embedded onramp

Let your users securely purchase crypto directly from your website.

Embed the Stripe fiat-to-crypto onramp directly on your website or mobile webview. Your customers complete their purchase without leaving your platform. Stripe acts as the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) and handles all fraud liability, regulatory requirements, _know your customer_ (Know your customer (KYC) regulations require that professionals and businesses make an effort to verify the identity, suitability, and risks involved with maintaining a business relationship. The procedures fall under the broader scope of anti-money laundering (AML) policy) (KYC) verifications, and sanctions screening.

[Get started](https://docs.stripe.com/crypto/onramp/embedded-quickstart.md)

## Features

| |
| |
| **Merchant of record** | When you use the onramp, Stripe acts as your merchant of record. A merchant of record is the legal entity responsible for facilitating the sale of products to a user. |
| **Stripe’s checkout infrastructure** | - Pre-populate transaction parameters (wallets, source and destination currencies, source and destination amounts, and supported networks)

- Every session status change generates a webhook
- Returning users can check out faster with [Link](https://docs.stripe.com/payments/link.md), the Stripe consumer account infrastructure |
  | **Customization** | - Add real-time quotes, automated KYC, and multi-chain support with minimal coding
- Implement using an embeddable widget, customizable to your brand |
  | **Disputes management** | No platform fraud liability, Stripe handles all disputes. |
  | **Payment methods** | Credit, debit, Apple Pay, and ACH (US only). All of these payment methods are eligible for instant crypto delivery after KYC completion. |
  | **Currencies** | Available currencies are subject to change for integration options in private preview.

- ETH (Ethereum)
- ETH (Base)1
- SOL
- POL
- MATIC
- BTC
- AVAX
- XLM1
- USDC (Ethereum)
- USDC (Solana)1
- USDC (Polygon)1
- USDC (Avalanche)1
- USDC (Base)1
- USDC (Stellar)1 |
  | **Geographic availability** | US, and EU countries |

1XLM, USDC (Stellar), USDC (Avalanche), and USDC (Polygon) aren’t available in New York. ETH (Base), MATIC, AVAX, USDC (Solana), USDC (Polygon), USDC (Avalanche), and USDC (Base) aren’t supported in the EU.

### Next steps

- [Embedded onramp quickstart](https://docs.stripe.com/crypto/onramp/embedded-quickstart.md)
- [Set up an Embedded onramp integration](https://docs.stripe.com/crypto/onramp/embedded.md)
