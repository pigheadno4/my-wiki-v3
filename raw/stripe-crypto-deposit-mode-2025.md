<!-- Source URL: https://docs.stripe.com/payments/crypto-deposit-mode -->
<!-- Fetched: 2026-05-01 -->

# Deposit mode stablecoin payments

Accept stablecoin payments with API-only deposit addresses.

Deposit mode is an API-only crypto payment flow where we return deposit addresses for each requested network. When your customer sends funds to a deposit address, we automatically _capture_ (Another way to say that you receive payment for a charge is to say that you "capture" the charge. Capturing the charge is often asynchronous and takes place after authorization. The capture is what transfers the money from the customer to you) the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) after the funds settle on-chain.

## Before you begin

Access to deposit mode is required. Contact [machine-payments@stripe.com](mailto:machine-payments@stripe.com).

> Your customers can use stablecoins as payment globally, but only US businesses can accept stablecoin payments.

To start accepting stablecoin payments:

1. Make sure you’ve [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md).
1. Go to your [Payment methods](https://dashboard.stripe.com/settings/payment_methods) settings in the Dashboard and request the **Stablecoins and Crypto** payment method. If you only want to accept stablecoin or crypto payments for [machine payments](https://docs.stripe.com/payments/machine.md), we recommend creating a separate [payment method configuration](https://docs.stripe.com/payments/payment-method-configurations.md) dedicated to machine payments.
1. Stripe reviews your access request and contact you for more details if necessary. The payment method appears as **Pending** while we review your request.
1. After we approve your request, **Stablecoins and Crypto** becomes active in the Dashboard.

## Create a PaymentIntent

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the `crypto` payment method and `mode: "deposit"`. Specify the networks that you want deposit addresses for by using `deposit_options.networks`.

> #### API version
>
> This feature requires the `2026-03-04.preview` API version. Set the `Stripe-Version` header to `2026-03-04.preview` when initializing your Stripe client.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: 'usd',
  payment_method_types: ['crypto'],
  payment_method_data: {
    type: 'crypto',
  },
  payment_method_options: {
    crypto: {
      mode: 'deposit',
      deposit_options: {
        networks: ['base', 'tempo', 'solana'],
      },
    },
  },
  confirm: true,
});
```

## PaymentIntent response

The confirmed `PaymentIntent` includes `crypto_display_details` in `next_action`, which contains deposit addresses and `supported_tokens` for each network:

```json
{
  "id": "pi_123",
  "amount": 5000,
  "currency": "usd",
  "status": "requires_action",
  "next_action": {
    "type": "crypto_display_details",
    "crypto_display_details": {
      "deposit_addresses": {
        "base": {
          "address": "0xbase_address",
          "supported_tokens": [
            {
              "token_currency": "usdc",
              "token_contract_address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
            }
          ]
        },
        "tempo": {
          "address": "0xtempo_address",
          "supported_tokens": [
            {
              "token_currency": "usdc",
              "token_contract_address": "0x20c000000000000000000000b9537d11c60e8b50"
            }
          ]
        },
        "solana": {
          "address": "So1ana_deposit_address",
          "supported_tokens": [
            {
              "token_currency": "usdc",
              "token_contract_address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
            }
          ]
        }
      }
    }
  }
}
```

Present the deposit address to your customer along with the expected amount and supported tokens. Your customer sends the correct token to the deposit address on the specified network.

## Payment lifecycle

Use the following steps to understand how a deposit-mode `PaymentIntent` moves from confirmation to completion.

1. After you confirm the `PaymentIntent`, it enters the `requires_action` status with deposit address details. The [Stripe Dashboard](https://dashboard.stripe.com/payments) displays these PaymentIntents as **Incomplete** while it waits for your customer to send funds.
1. Your customer sends funds to the deposit address on-chain.
1. Stripe detects the on-chain transaction and move the `PaymentIntent` to `processing` while we validate the transaction details.
1. After validations complete, the `PaymentIntent` moves to `succeeded`.

> #### Transfer detection delay
>
> It can take a few minutes for us to detect the transfer after the network confirms it.

If the transaction fails validation or we can’t match the deposit, the `PaymentIntent` returns to `requires_payment_method`. Otherwise, the `PaymentIntent` remains in `requires_action`.

## Transaction details

After the `PaymentIntent` succeeds, retrieve on-chain transaction details by expanding `latest_charge` on the `PaymentIntent`. The [payment_method_details.crypto](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-crypto) hash on the charge includes fields such as the transaction hash, buyer wallet address, network, and token currency.

## Failure modes

Use the following scenarios to understand when we can’t match a deposit to a `PaymentIntent`.

- **Wrong network or asset**: If your customer sends tokens on a network or with a token contract that doesn’t match the deposit address, we can’t automatically match or return the funds.
- **Funds after expiration**: If your customer sends funds after the `PaymentIntent` expires, we can’t automatically match or return the funds.
- **Overpayment or underpayment**: The token amount that your customer transfers must exactly match the amount on the `PaymentIntent`. If your customer sends more or less than the specified amount, we can’t automatically match or return the funds.
  - The transferred token amount must exactly match the `PaymentIntent` amount. Because fiat currencies and stablecoins use different decimal precisions, account for this difference when you calculate the transfer. For example, USD uses two decimal places, while USDC uses six. To fulfill a `PaymentIntent` for 1.01 USD (101 minor units), your customer must transfer exactly 1.010000 USDC (1,010,000 minor units).

## Refunds

When you refund a deposit mode payment, we return funds to the sending wallet address from the detected on-chain transaction.

> Make sure that you verify the destination address before you initiate the refund. If your customer paid from an exchange or omnibus wallet, they might not be able to recover refunded funds.

## Token and network support

`PaymentIntents` with the `crypto` payment method in `mode: deposit` support USDC on the following networks:

| Network | Token | Token contract address                         |
| ------- | ----- | ---------------------------------------------- |
| Tempo   | USDC  | `0x20c000000000000000000000b9537d11c60e8b50`   |
| Base    | USDC  | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`   |
| Solana  | USDC  | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |

## Test your integration

[Sandboxes](https://docs.stripe.com/sandboxes.md) don’t monitor crypto testnets, so we can’t automatically detect testnet transactions that you send. Instead, use the [test helper endpoint](https://docs.stripe.com/api/payment_intents/simulate_crypto_deposit.md?api-version=2026-03-04.preview) to simulate crypto deposits for sandbox PaymentIntents. This lets you verify your integration immediately without relying on on-chain transactions.

```curl
curl https://api.stripe.com/v1/test_helpers/payment_intents/{{PAYMENT_INTENT_ID}}/simulate_crypto_deposit \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-03-04.preview" \
  -d transaction_hash=0x00000000000000000000000000000000000000000000000000000testsuccess \
  -d network=base \
  -d token_currency=usdc \
  -d buyer_wallet=0x0000000000000000000000000000000000000000
```

To simulate different outcomes, set `transaction_hash` to one of the following:

| Transaction hash                                                     | Outcome                                                                                          |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `0x00000000000000000000000000000000000000000000000000000testsuccess` | `PaymentIntent` succeeds within 15 seconds                                                       |
| `0x000000000000000000000000000000000000000000000000000000testfailed` | The charge fails, and the `PaymentIntent` returns to `requires_payment_method` within 15 seconds |
