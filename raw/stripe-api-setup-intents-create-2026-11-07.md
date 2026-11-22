<!-- Source URL: https://docs.stripe.com/api/setup_intents/create -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Create a SetupIntent

Creates a SetupIntent object.

After you create the SetupIntent, attach a payment method and [confirm](https://docs.stripe.com/api/setup_intents/confirm.md) it to collect any required permissions to charge the payment method later.

## Request

```curl
curl https://api.stripe.com/v1/setup_intents \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive" \
  -d "automatic_payment_methods[enabled]=true"
```

### Response

```json
{
  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",
  "object": "setup_intent",
  "application": null,
  "automatic_payment_methods": {
    "enabled": true
  },
  "cancellation_reason": null,
  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",
  "created": 1678942624,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": null,
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_options": {
    "card": {
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "single_use_mandate": null,
  "status": "requires_payment_method",
  "usage": "off_session"
}
```

## Parameters

- `allowed_payment_method_types` (array of enums, optional)
  The list of payment method types to allow for this SetupIntent. Stripe will only use methods in this list when determining the payment methods to offer. A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type).
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

- `attach_to_self` (boolean, optional)
  If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

  It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

- [`automatic_payment_methods`](https://docs.stripe.com/api/setup_intents/create.md?query=automatic_payment_methods) (object, optional)
  When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.

- `confirm` (boolean, optional)
  Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary.

- `confirmation_token` (string, optional)
  ID of the ConfirmationToken used to confirm this SetupIntent.

  If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.

- `customer` (string, optional)
  ID of the Customer this SetupIntent belongs to, if one exists.

  If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

- `customer_account` (string, optional)
  ID of the Account this SetupIntent belongs to, if one exists.

  If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `excluded_payment_method_types` (array of enums, optional)
  The list of payment method types to exclude from use with this SetupIntent.
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

- `flow_directions` (array of enums, optional)
  Indicates the directions of money movement for which this payment method is intended to be used.

  Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
Possible enum values:
  - `inbound`
    Set up an inbound flow

  - `outbound`
    Set up an outbound flow

- [`mandate_data`](https://docs.stripe.com/api/setup_intents/create.md?query=mandate_data) (object, optional)
  This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-confirm).

- `metadata` (map, optional)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `on_behalf_of` (string, optional)
  The Stripe account ID created for this SetupIntent.

- `payment_method` (string, optional)
  The ID of a PaymentMethod to attach to this SetupIntent.

- `payment_method_configuration` (string, optional)
  The ID of the [payment method configuration](https://docs.stripe.com/api/payment_method_configurations.md) to use with this SetupIntent.

  The maximum length is 100 characters.

- [`payment_method_data`](https://docs.stripe.com/api/setup_intents/create.md?query=payment_method_data) (object, optional)
  When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-payment_method) value in the SetupIntent.

- [`payment_method_options`](https://docs.stripe.com/api/setup_intents/create.md?query=payment_method_options) (object, optional)
  Payment method-specific configuration for this SetupIntent.

- `return_url` (string, optional)
  The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-confirm).

- [`single_use`](https://docs.stripe.com/api/setup_intents/create.md?query=single_use) (object, optional)
  If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.

  Single-use mandates are only valid for the following payment methods: `acss_debit`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `ideal`, `link`, `sepa_debit`, and `us_bank_account`.

- `usage` (enum, optional)
  Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`.
Possible enum values:
  - `off_session`
    Use `off_session` if your customer may or may not be in your checkout flow.

  - `on_session`
    Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow.

- `use_stripe_sdk` (boolean, optional)
  Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.

## Returns

Returns a SetupIntent object.
