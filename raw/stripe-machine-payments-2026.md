<!-- Source URL: https://docs.stripe.com/payments/agentic-commerce/machine-payments -->
<!-- Fetched: 2026-05-12 -->
<!-- Note: Content formatted from structured UI text (not raw markdown paste) -->

# Machine payments

Enable machine-to-machine payments with Stripe.

> **Frontier** feature

Use machine payments to let your agents pay for resources programmatically (for example, for API calls or services). As a business, you can use Stripe to accept machine payments in crypto directly into your Stripe balance.

| | Description |
| --- | --- |
| **For sellers** | If you have growing traffic and interest from agents, you can enable pay-per-use business models as low as 0.01 USDC. If your product is primarily an API, you can sell individual requests to agents. You can also restrict access to data or content with a paywall. |
| **For agents** | As an alternative to setting up an account and getting an API key, your agent can interact with services on demand and pay per invocation. Your agents only need access to a crypto wallet. |

## Features

Machine payments integrate with your existing Stripe integration.

| Feature | Description |
| --- | --- |
| **Stripe payments** | Payments land directly in your Stripe balance and settle in fiat. Metrics, reporting, and multi-currency payouts work the same as any other payment in Stripe. |
| **Refunds** | Refunds are available through the API and in the Stripe Dashboard. For stablecoin transactions, we return funds to the "From" wallet address of the token transfer. |
| **Microtransactions** | Individual charges can be as low as 0.01 USDC. |
| **Private** | Stripe uses a unique deposit address for each payment, which reduces on-chain visibility of your processing volume. |
| **US availability** | Card and wallet payments through SPTs are available nationwide to developers with a US legal entity. Stablecoin payments are available in all states except New York and Texas. |

## Availability

Stripe supports machine payments across these networks.

| Network | Protocols | Currency |
| --- | --- | --- |
| Base | x402 | USDC |
| Solana | MPP | USDC |
| Tempo | MPP | USDC |
| Stripe card networks | MPP | Stripe currencies |

## Integration guides

Learn how to apply payment middleware to your HTTP endpoints using common payment protocols to accept machine payments.

- **Machine payments protocol (MPP)**: Learn about using MPP for machine-to-machine payments.
- **x402**: Learn about the x402 payment protocol for machine-to-machine payments.
