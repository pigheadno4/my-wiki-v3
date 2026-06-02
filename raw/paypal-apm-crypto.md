---
title: Accept crypto payments
slug: /docs/checkout/apm/crypto/
createTime: "2026-01-13T21:14:01.904Z"
updateTime: "2026-01-29T20:20:38.549Z"
---

# Accept crypto payments

PayPal's Pay with crypto is a payment solution that allows you to accept cryptocurrency (crypto) payments from global buyers and receive automatic settlement in local currency. With this payment method, you can:

- Offer flexible payment options to buyers at checkout.
- Attract new customers and expand reach to pro-crypto audiences.

| Countries | Payment type | Payment flow | Settlement currency | Minimum amount | Refunds |
| US merchants

Global buyers | cryptocurrency | redirect | Local currency | 0.01 USD | Yes, in PYUSD (Stablecoin) |

## Key features

- **Expanded customer reach:** Reach over 650 million pro-crypto consumers worldwide.
- **Higher payment success rates:** Improve transaction completion compared to traditional cross-border card transactions.
- **Competitive transaction fees:** Control costs with lower processing fees for crypto payments.
  **Note**: PayPal USD (PYUSD) is a stablecoin that maintains full backing with US dollar deposits, US treasuries, and similar cash equivalents. You can buy and sell 1 PYUSD for 1 USD.- **Seamless integration:** Streamline operations by adding crypto to your current PayPal setup without major changes.
- **Broad cryptocurrency support:** Accept approximately 100 cryptocurrencies, including Bitcoin, Ethereum, and PayPal USD. For a complete list, see [supported cryptocurrencies](#supported-cryptocurrencies) .
- **Flexible payment sources:** Help buyers pay using cryptocurrency from popular exchanges such as Coinbase or self-hosted wallets such as Metamask.
- **Local currency settlement:** Receive settlements in your preferred local currency based on your PayPal Business account's primary currency setting.

## How it works

- **Merchant:** Presents **Pay with crypto** as a payment option on the checkout page.
- **Buyer:** Selects **Pay with crypto** at checkout.
- **Merchant:** Creates an order with PayPal using crypto as the payment method.
- **PayPal:** Creates the order and returns a link for buyer approval.
- **Merchant:** Redirects the buyer to PayPal to complete payment approval.
- **Buyer:** - Selects a preferred wallet or exchange account.
- Authenticates with the selected wallet or exchange.
- Reviews and approves the payment.

- **PayPal:** - Manages the crypto payment flow.
- Automatically captures the payment and converts the cryptocurrency to the merchant's local currency.
- Notifies the merchant of payment completion.
- Settles the funds to the merchant's PayPal account in their local currency.

- **Merchant:** Confirms the payment and proceeds with order fulfillment.

## Buyer flows

Select a tab to view either the self-custody wallet flow or the exchange account flow.

### Self-custody wallet flow

![image](assets/paypal-crypto-wallet-1.png)

![image](assets/paypal-crypto-wallet-2.png)

![image](assets/paypal-crypto-wallet-3.png)

![image](assets/paypal-crypto-wallet-4.png)

,### Exchange account flow
![image](assets/paypal-crypto-exchange-1.png)

![image](assets/paypal-crypto-exchange-2.png)

![image](assets/paypal-crypto-exchange-3.png)

## Eligibility

- **Account type:** Verified US PayPal Business required.
- **Geographic availability:** Available only to US merchants.
- **Buyer coverage:** Global buyers can pay with about 100 supported cryptocurrencies (for example, BTC, ETH, PYUSD) using their preferred third-party walletwithout needing to create a PayPal account.
- **Platform availability:** Available for current PayPal for Business or Platforms integration using the Orders V2 API.
- **Minimum transaction:** Accept payments starting from 0.01 USD.
- **Refunds** : Issuerefunds in PYUSD (PayPal's stable digital dollar) without holding any cryptocurrency. You transact in your preferred currency.
- **Settlement** : Processed in local currency based on your PayPal Business account's primary currency setting.

## Limitations

- **Payment features:** Billing agreements, recurring payments, chargebacks, and multi-seller configurations are not supported.
- **Geographic restrictions:** Only available to US merchants.
- **Payment authorization:** Authorization and Capture payment flows are not supported.
- **Vaulting:** Vaulted payments are not supported.

## Supported cryptocurrencies

The following cryptocurrencies are supported for Pay with crypto and are listed in the [PayPal Payments allow list](https://www.paypal.com/in/webapps/mpp/country-worldwide) . Each currency must be identified by its standard currency code (for example, BTC , ETH , PYUSD ).

| **Currency** | **Code** |
| Bitcoin | BTC |
| Ethereum | ETH |
| XRP | XRP |
| Tether USDt | USDT |
| Solana | SOL |
| BNB | BNB |
| USD Coin | USDC |
| Dogecoin | DOGE |
| Cardano | ADA |
| TRON | TRX |
| Sui | SUI |
| Chainlink | LINK |
| Avalanche | AVAX |
| Stellar Lumens | XLM |
| Shiba Inu | SHIB |
| Hedera | HBAR |
| Toncoin | TON |
| Polkadot | DOT |
| Bitcoin Cash | BCH |
| UNUS SED LEO | LEO |
| Litecoin | LTC |
| Pepe | PEPE |
| Dai | DAI |
| Uniswap | UNI |
| NEAR Protocol | NEAR |
| Aptos | APT |
| Aave | AAVE |
| Ondo | ONDO |
| OKB | OKB |
| Internet Computer | ICP |
| Ethereum Classic | ETC |
| Render | RENDER |
| Cronos | CRO |
| VeChain | VET |
| Polygon | POL |
| Mantle | MNT |
| Arbitrum | ARB |
| Filecoin | FIL |
| Algorand | ALGO |
| Artificial Superintelligence Alliance | FET |
| Celestia | TIA |
| Cosmos | ATOM |
| Bonk | BONK |
| Worldcoin | WLD |
| Solidus AI Tech | S |
| Jupiter | JUP |
| Maker | MKR |
| Stacks | STX |
| Optimism | OP |
| KuCoin Token | KCS |
| Injective | INJ |
| EOS | EOS |
| Immutable X | IMX |
| Sei | SEI |
| The Graph | GRT |
| Quant | QNT |
| XDC Network | XDC |
| FLOKI | FLOKI |
| Theta Network | THETA |
| JasmyCoin | JASMY |
| Curve DAO Token | CRV |
| Lido DAO | LDO |
| Gala | GALA |
| Raydium | RAY |
| IOTA | IOTA |
| The Sandbox | SAND |
| Ethereum Name Service | ENS |
| PayPal USD | PYUSD |
| Nexo | NEXO |
| BitTorrent (New) | BTT |
| Bitcoin SV | BSV |
| PAX Gold | PAXG |
| Decentraland | MANA |
| Flow | FLOW |
| Pi Network | PI |
| Hyperliquid | HYPE |
| Bitget Token | BGB |
| Ethena USDe | USDe |
| Bittensor | TAO |
| Kaspa | KAS |
| GateToken | GT |
| MAGA | TRUMP |
| Ethena | ENA |
| USD1 | USD1 |
| First Digital USD | FDUSD |
| Fartcoin | FARTCOIN |
| Internet Protocol | IP |
| VIRTUAL | VIRTUAL |
| dogwifhat | WIF |
| DeXe | DEXE |
| Formation Fi | FORM |
| Wallet | WAL |
| Pudgy Penguins | PENGU |
| Core | CORE |
| Brett | BRETT |
| Tether Gold | XAUt |
| PancakeSwap | CAKE |
| Kaia | KAIA |
| SPX6900 | SPX |

## Integration method

### Orders REST API

Integrate directly using the Orders API for a fully customised checkout experience.
