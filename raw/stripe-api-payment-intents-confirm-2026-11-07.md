<!-- Source URL: https://docs.stripe.com/api/payment_intents/confirm -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Confirm a PaymentIntent

Confirm that your customer intends to pay with current or provided payment method. Upon confirmation, the PaymentIntent will attempt to initiate a payment.

If the selected payment method requires additional authentication steps, the PaymentIntent will transition to the `requires_action` status and suggest additional actions via `next_action`. If payment fails, the PaymentIntent transitions to the `requires_payment_method` status or the `canceled` status if the confirmation limit is reached. If payment succeeds, the PaymentIntent will transition to the `succeeded` status (or `requires_capture`, if `capture_method` is set to `manual`).

If the `confirmation_method` is `automatic`, payment may be attempted using our [client SDKs](https://docs.stripe.com/stripe-js/reference.md#stripe-handle-card-payment) and the PaymentIntent’s [client_secret](https://docs.stripe.com/api/payment_intents/confirm.md#payment_intent_object-client_secret). After `next_action`s are handled by the client, no additional confirmation is required to complete the payment.

If the `confirmation_method` is `manual`, all payment attempts must be initiated using a secret key.

If any actions are required for the payment, the PaymentIntent will return to the `requires_confirmation` state after those actions are completed. Your server needs to then explicitly re-confirm the PaymentIntent to initiate the next payment attempt.

There is a variable upper limit on how many times a PaymentIntent can be confirmed. After this limit is reached, any further calls to this endpoint will transition the PaymentIntent to the `canceled` state.

## Prerequisites

Before you can run the following code snippet, you need to call these APIs with the provided parameters to set up the prerequisite API object(s).

1. createPaymentIntent
POST /v1/payment_intents {"amount":2000,"currency":"usd","automatic_payment_methods":{"enabled":true}}

## Request

```curl
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive" \
  -d payment_method=pm_card_visa \
  --data-urlencode "return_url=https://www.example.com"
```

### Response

```json
{
  "id": "pi_3MtweELkdIwHu7ix0Dt0gF2H",
  "object": "payment_intent",
  "amount": 2000,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 2000,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": {
    "enabled": true
  },
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "automatic",
  "client_secret": "pi_3MtweELkdIwHu7ix0Dt0gF2H_secret_ALlpPMIZse0ac8YzPxkMkFgGC",
  "confirmation_method": "automatic",
  "created": 1680802258,
  "currency": "usd",
  "customer": null,
  "description": null,
  "last_payment_error": null,
  "latest_charge": "ch_3MtweELkdIwHu7ix05lnLAFd",
  "livemode": false,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1MtweELkdIwHu7ixxrsejPtG",
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    },
    "link": {
      "persistent_token": null
    }
  },
  "payment_method_types": [
    "card",
    "link"
  ],
  "processing": null,
  "receipt_email": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "source": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "transfer_group": null
}
```

## Parameters

- `id` (string, required)
  Unique identifier for the object.

- `allowed_payment_method_types` (array of enums, optional)
  The list of payment method types allowed for use with this payment. Stripe automatically returns compatible payment methods from this list in the `payment_method_types` field of the response, based on the other PaymentIntent parameters, such as `currency`, `amount`, and `customer`.
Possible enum values:
  - `acss_debit`
    [Pre-authorized debit payments](https://docs.stripe.com/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  - `affirm`
    [Affirm](https://docs.stripe.com/payments/affirm.md) is a buy now, pay later payment method in the US.

  - `afterpay_clearpay`
    [Afterpay / Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  - `alipay`
    [Alipay](https://docs.stripe.com/payments/alipay.md) is a digital wallet payment method used in China.

  - `alma`
    [Alma](https://docs.stripe.com/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  - `amazon_pay`
    [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  - `au_becs_debit`
    [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  - `bacs_debit`
    [Bacs Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  - `bancontact`
    [Bancontact](https://docs.stripe.com/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  - `billie`
    [Billie](https://docs.stripe.com/payments/billie.md) is a payment method.

  - `bizum`
    [Bizum](https://docs.stripe.com/payments/bizum.md) is a payment method.

  - `blik`
    [BLIK](https://docs.stripe.com/payments/blik.md) is a single-use payment method common in Poland.

  - `boku_promptpay`
    PromptPay is a payment method.

  - `boleto`
    [Boleto](https://docs.stripe.com/payments/boleto.md) is a voucher-based payment method used in Brazil.

  - `capchase_pay`
    CapchasePay is a payment method.

  - `card`
    [Card payments](https://docs.stripe.com/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources (Link is also known as Onelink in the UK).

  - `card_present`
    [Stripe Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment.md) is used to collect in-person card payments.

  - `cashapp`
    [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  - `check_scan`
    CheckScan is a payment method.

  - `click_to_pay`
    ClickToPay is a payment method.

  - `crypto`
    [Stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `customer_balance`
    Uses a customer’s [cash balance](https://docs.stripe.com/payments/customer-balance.md) for the payment.

  - `demo_pay`
    DemoPay is a payment method.

  - `duitnow`
    Duitnow is a payment method.

  - `dummy_auth_push`
    Dummy auth push payment method for internal testing.

  - `dummy_passthrough_card`
    Dummy auth push payment method for internal testing.

  - `edenred`
    [Edenred](https://docs.stripe.com/payments/edenred.md) is a payment method.

  - `eps`
    [EPS](https://docs.stripe.com/payments/eps.md) is an Austria-based bank redirect payment method.

  - `fpx`
    [FPX](https://docs.stripe.com/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  - `gcash`
    GCash is a payment method.

  - `getbalance`
    [Getbalance](https://docs.stripe.com/payments/getbalance.md) is a payment method.

  - `gift_card`
    Gift card is a payment method for redeeming third-party gift cards.

  - `giropay`
    [giropay](https://docs.stripe.com/payments/giropay.md) is a German bank redirect payment method.

  - `gopay`
    Gopay is a payment method.

  - `grabpay`
    [GrabPay](https://docs.stripe.com/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  - `id_bank_transfer`
    [Indonesia bank transfer](https://docs.stripe.com/payments/id-bank-transfer.md) payments are used to accept bank transfers from customers in Indonesia.

  - `ideal`
    [iDEAL](https://docs.stripe.com/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  - `interac_present`
    [Stripe Terminal](https://docs.stripe.com/terminal/payments/collect-card-payment.md) accepts [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) debit cards for in-person payments in Canada.

  - `kakao_pay`
    [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `klarna`
    [Klarna](https://docs.stripe.com/payments/klarna.md) is a global buy now, pay later payment method.

  - `knet`
    KNET is a bank redirect payment method used in Kuwait.

  - `konbini`
    [Konbini](https://docs.stripe.com/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  - `kr_card`
    [Korean cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  - `kr_market`
    KrMarket is a payment method.

  - `kriya`
    Kriya is a payment method.

  - `link`
    [Link (also known as Onelink in the UK)](https://docs.stripe.com/payments/link.md) allows customers to pay with their saved payment details.

  - `mb_way`
    MB WAY is a payment method.

  - `mobilepay`
    [MobilePay](https://docs.stripe.com/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  - `momo`
    [MoMo](https://docs.stripe.com/payments/momo.md) is a Vietnamese mobile wallet payment method.

  - `mondu`
    [Mondu](https://docs.stripe.com/payments/mondu.md) is a payment method.

  - `multibanco`
    [Multibanco](https://docs.stripe.com/payments/multibanco.md) is a voucher payment method

  - `naver_pay`
    [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `netbanking`
    [NetBanking](https://docs.stripe.com/payments/netbanking.md) is a bank redirect payment method used in India.

  - `ng_bank`
    Naira wallet is a payment method.

  - `ng_bank_transfer`
    Naira bank transfer is a payment method.

  - `ng_card`
    Naira card is a payment method.

  - `ng_market`
    NgMarket is a payment method.

  - `ng_ussd`
    Naira USSD is a payment method used in Nigeria to power USSD payments.

  - `ng_wallet`
    NgWallet is a payment method.

  - `nz_bank_account`
    [New Zealand BECS Direct Debit](https://docs.stripe.com/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  - `octopus`
    [Octopus](https://docs.stripe.com/payments/octopus.md) is a payment method.

  - `oxxo`
    [OXXO](https://docs.stripe.com/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  - `p24`
    [Przelewy24](https://docs.stripe.com/payments/p24.md) is a bank redirect payment method used in Poland.

  - `paper_check`
    PaperCheck is a payment method.

  - `pay_by_bank`
    [Pay By Bank](https://docs.stripe.com/payments/pay-by-bank.md) is an open banking payment method in the UK.

  - `payco`
    [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `paynow`
    [PayNow](https://docs.stripe.com/payments/paynow.md) is a QR code payment method used in Singapore.

  - `paypal`
    [PayPal](https://docs.stripe.com/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  - `paypay`
    [PayPay](https://docs.stripe.com/payments/paypay.md) is a payment method.

  - `payto`
    [PayTo](https://docs.stripe.com/payments/payto.md) is a real time payment method

  - `pix`
    [Pix](https://docs.stripe.com/payments/pix.md) is an instant bank transfer payment method in Brazil.

  - `promptpay`
    [PromptPay](https://docs.stripe.com/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  - `qris`
    [QRIS](https://docs.stripe.com/payments/qris.md) is a QR Code payment method in Indonesia.

  - `rechnung`
    [Rechnung](https://docs.stripe.com/payments/rechnung.md) is a buy now, pay later payment option in Germany using white-label invoicing.

  - `revolut_pay`
    [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  - `samsung_pay`
    [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `satispay`
    [Satispay](https://docs.stripe.com/payments/satispay.md) is a payment method.

  - `scalapay`
    Scalapay is a payment method.

  - `sepa_debit`
    [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  - `sequra`
    SeQura is a payment method.

  - `shop_pay`
    [Shop Pay](https://docs.stripe.com/payments/shop-pay.md) is a Wallet payment method that lets hundreds of millions of Shopify customers pay their way, every day.

  - `shopeepay`
    Shopeepay is a payment method.

  - `sofort`
    [Sofort](https://docs.stripe.com/payments/sofort.md) is a bank redirect payment method used in Europe.

  - `south_korea_market`
    SouthKoreaMarket is a payment method.

  - `stripe_balance`
    [Pay with Stripe balance](https://docs.stripe.com/payments/balance-pay.md) is a payment method linked directly to a Stripe account’s available balance.

  - `sunbit`
    [Sunbit](https://docs.stripe.com/payments/sunbit.md) is a payment method.

  - `swish`
    [Swish](https://docs.stripe.com/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  - `tamara`
    [Tamara](https://docs.stripe.com/payments/tamara.md) is a payment method.

  - `test_pay`
    TestPay is a payment method.

  - `touch_n_go`
    Touch 'n Go is a Malaysian mobile wallet payment method.

  - `truemoney`
    TrueMoney is a payment method.

  - `twint`
    [TWINT](https://docs.stripe.com/payments/twint.md) is a single-use payment method used in Switzerland.

  - `upi`
    [UPI](https://docs.stripe.com/payments/upi.md) is an instant real-time payment system in India.

  - `us_bank_account`
    [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  - `us_cash_voucher`
    UsCashVoucher enables Treasury customers to add cash to their account using a voucher at select major US retailers.

  - `vipps`
    [Vipps](https://docs.stripe.com/payments/vipps.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the Vipps application.

  - `wechat_pay`
    [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) is a digital wallet payment method based in China.

  - `wero`
    Wero is a payment method.

  - `zip`
    [Zip](https://docs.stripe.com/payments/zip.md) is a Buy now, pay later Payment Method

- [`amount_details`](https://docs.stripe.com/api/payment_intents/confirm.md?query=amount_details) (object, optional)
  Provides industry-specific information about the amount.

- `amount_to_confirm` (integer, optional)
  Amount to confirm on the PaymentIntent. Defaults to `amount` if not provided.

- `capture_method` (enum, optional)
  Controls when the funds will be captured from the customer’s account.
Possible enum values:
  - `automatic`
    Stripe automatically captures funds when the customer authorizes the payment.

  - `automatic_async`
    (Default) Stripe asynchronously captures funds when the customer authorizes the payment. Recommended over `capture_method=automatic` due to improved latency. Read the [integration guide](https://docs.stripe.com/payments/payment-intents/asynchronous-capture.md) for more information.

  - `manual`
    Place a hold on the funds when the customer authorizes the payment, but [don’t capture the funds until later](https://docs.stripe.com/payments/capture-later.md). (Not all payment methods support this.)

- `client_secret` (string, Required if using a publishable key.)
  The client secret of the PaymentIntent.

- `confirmation_token` (string, optional)
  ID of the ConfirmationToken used to confirm this PaymentIntent.

  If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.

- `error_on_requires_action` (boolean, optional)
  Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://docs.stripe.com/payments/save-card-without-authentication.md).

- `excluded_payment_method_types` (array of enums, optional)
  The list of payment method types to exclude from use with this payment.
Possible enum values:
  - `acss_debit`
    [Pre-authorized debit payments](https://docs.stripe.com/payments/acss-debit.md) are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

  - `affirm`
    [Affirm](https://docs.stripe.com/payments/affirm.md) is a buy now, pay later payment method in the US.

  - `afterpay_clearpay`
    [Afterpay / Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md) is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

  - `alipay`
    [Alipay](https://docs.stripe.com/payments/alipay.md) is a digital wallet payment method used in China.

  - `alma`
    [Alma](https://docs.stripe.com/payments/alma.md) is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

  - `amazon_pay`
    [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

  - `au_becs_debit`
    [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

  - `bacs_debit`
    [Bacs Direct Debit](https://docs.stripe.com/payments/payment-methods/bacs-debit.md) is used to debit UK bank accounts.

  - `bancontact`
    [Bancontact](https://docs.stripe.com/payments/bancontact.md) is a bank redirect payment method used in Belgium.

  - `billie`
    [Billie](https://docs.stripe.com/payments/billie.md) is a payment method.

  - `bizum`
    [Bizum](https://docs.stripe.com/payments/bizum.md) is a payment method.

  - `blik`
    [BLIK](https://docs.stripe.com/payments/blik.md) is a single-use payment method common in Poland.

  - `boleto`
    [Boleto](https://docs.stripe.com/payments/boleto.md) is a voucher-based payment method used in Brazil.

  - `card`
    [Card payments](https://docs.stripe.com/payments/payment-methods/overview.md#cards) are supported through many networks, card brands, and select Link funding sources (Link is also known as Onelink in the UK).

  - `cashapp`
    [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) enables customers to frictionlessly authenticate payments in the Cash App using their stored balance or linked card.

  - `crypto`
    [Stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) enable customers to pay in stablecoins like USDC from 100s of wallets including Phantom and Metamask.

  - `customer_balance`
    Uses a customer’s [cash balance](https://docs.stripe.com/payments/customer-balance.md) for the payment.

  - `eps`
    [EPS](https://docs.stripe.com/payments/eps.md) is an Austria-based bank redirect payment method.

  - `fpx`
    [FPX](https://docs.stripe.com/payments/fpx.md) is a Malaysia-based bank redirect payment method.

  - `giropay`
    [giropay](https://docs.stripe.com/payments/giropay.md) is a German bank redirect payment method.

  - `grabpay`
    [GrabPay](https://docs.stripe.com/payments/grabpay.md) is a digital wallet payment method used in Southeast Asia.

  - `ideal`
    [iDEAL](https://docs.stripe.com/payments/ideal.md) is a Netherlands-based bank redirect payment method.

  - `kakao_pay`
    [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `klarna`
    [Klarna](https://docs.stripe.com/payments/klarna.md) is a global buy now, pay later payment method.

  - `konbini`
    [Konbini](https://docs.stripe.com/payments/konbini.md) is a cash-based voucher payment method used in Japan.

  - `kr_card`
    [Korean cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md) enables customers to accept local credit and debit cards in South Korea.

  - `mb_way`
    MB WAY is a payment method.

  - `mobilepay`
    [MobilePay](https://docs.stripe.com/payments/mobilepay.md) is a Nordic card-passthrough wallet payment method where customers authorize the payment in the MobilePay application.

  - `multibanco`
    [Multibanco](https://docs.stripe.com/payments/multibanco.md) is a voucher payment method

  - `naver_pay`
    [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `nz_bank_account`
    [New Zealand BECS Direct Debit](https://docs.stripe.com/payments/nz-bank-account.md) is used to debit New Zealand bank accounts through the Bulk Electronic Clearing System (BECS).

  - `oxxo`
    [OXXO](https://docs.stripe.com/payments/oxxo.md) is a cash-based voucher payment method used in Mexico.

  - `p24`
    [Przelewy24](https://docs.stripe.com/payments/p24.md) is a bank redirect payment method used in Poland.

  - `pay_by_bank`
    [Pay By Bank](https://docs.stripe.com/payments/pay-by-bank.md) is an open banking payment method in the UK.

  - `payco`
    [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `paynow`
    [PayNow](https://docs.stripe.com/payments/paynow.md) is a QR code payment method used in Singapore.

  - `paypal`
    [PayPal](https://docs.stripe.com/payments/paypal.md) is an online wallet and redirect payment method commonly used in Europe.

  - `paypay`
    [PayPay](https://docs.stripe.com/payments/paypay.md) is a payment method.

  - `payto`
    [PayTo](https://docs.stripe.com/payments/payto.md) is a real time payment method

  - `pix`
    [Pix](https://docs.stripe.com/payments/pix.md) is an instant bank transfer payment method in Brazil.

  - `promptpay`
    [PromptPay](https://docs.stripe.com/payments/promptpay.md) is an instant funds transfer service popular in Thailand.

  - `revolut_pay`
    [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md) is a digital wallet payment method used in the United Kingdom.

  - `samsung_pay`
    [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md) is a digital wallet payment method used in South Korea.

  - `satispay`
    [Satispay](https://docs.stripe.com/payments/satispay.md) is a payment method.

  - `scalapay`
    Scalapay is a payment method.

  - `sepa_debit`
    [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) is used to debit bank accounts within the Single Euro Payments Area (SEPA) region.

  - `sequra`
    SeQura is a payment method.

  - `sofort`
    [Sofort](https://docs.stripe.com/payments/sofort.md) is a bank redirect payment method used in Europe.

  - `sunbit`
    [Sunbit](https://docs.stripe.com/payments/sunbit.md) is a payment method.

  - `swish`
    [Swish](https://docs.stripe.com/payments/swish.md) is a Swedish wallet payment method where customers authorize the payment in the Swish application.

  - `twint`
    [TWINT](https://docs.stripe.com/payments/twint.md) is a single-use payment method used in Switzerland.

  - `upi`
    [UPI](https://docs.stripe.com/payments/upi.md) is an instant real-time payment system in India.

  - `us_bank_account`
    [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md) is used to debit US bank accounts through the Automated Clearing House (ACH) payments system.

  - `wechat_pay`
    [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) is a digital wallet payment method based in China.

  - `wero`
    Wero is a payment method.

  - `zip`
    [Zip](https://docs.stripe.com/payments/zip.md) is a Buy now, pay later Payment Method

- [`hooks`](https://docs.stripe.com/api/payment_intents/confirm.md?query=hooks) (object, optional)
  Automations to be run during the PaymentIntent lifecycle

- `mandate` (string, optional)
  ID of the mandate that’s used for this payment.

- [`mandate_data`](https://docs.stripe.com/api/payment_intents/confirm.md?query=mandate_data) (object, optional)
  This hash contains details about the mandate to create.

- `off_session` (boolean | enum, optional)
  Set to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt and can’t authenticate. Use this parameter in scenarios where you collect payment method details and [charge them later](https://docs.stripe.com/payments/save-during-payment.md).
Possible enum values:
  - `one_off`
  - `recurring`

- [`payment_details`](https://docs.stripe.com/api/payment_intents/confirm.md?query=payment_details) (object, optional)
  Provides industry-specific information about the charge.

- `payment_method` (string, optional)
  The ID of a PaymentMethod to attach to this PaymentIntent. If the payment method is attached to a Customer, it must match the [customer](https://docs.stripe.com/api/payment_intents/confirm.md#create_payment_intent-customer) that is set on this PaymentIntent.

- [`payment_method_data`](https://docs.stripe.com/api/payment_intents/confirm.md?query=payment_method_data) (object, optional)
  If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear in the [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) property on the PaymentIntent.

- [`payment_method_options`](https://docs.stripe.com/api/payment_intents/confirm.md?query=payment_method_options) (object, optional)
  Payment method-specific configuration for this PaymentIntent.

- [`radar_options`](https://docs.stripe.com/api/payment_intents/confirm.md?query=radar_options) (object, optional)
  Options to configure Radar. Learn more about [Radar Sessions](https://docs.stripe.com/radar/radar-session.md).

- `receipt_email` (string, optional)
  Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).

- `return_url` (string, optional)
  The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you’d prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter is only used for cards and other redirect-based payment methods.

- `setup_future_usage` (enum, optional)
  Indicates that you intend to make future payments with this PaymentIntent’s payment method.

  If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment.md) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach.md) the payment method to a Customer after the transaction completes.

  If the payment method is `card_present` and isn’t a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

  When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication.md).

  If you’ve already set `setup_future_usage` and you’re performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be present in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when your customer is present in your checkout flow.

- [`shipping`](https://docs.stripe.com/api/payment_intents/confirm.md?query=shipping) (object, optional)
  Shipping information for this PaymentIntent.

- `use_stripe_sdk` (boolean, optional)
  Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.

## Returns

Returns the resulting PaymentIntent after all possible transitions are applied.
