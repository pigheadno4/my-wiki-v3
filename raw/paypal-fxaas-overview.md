<!-- Source URL: https://developer.paypal.com/docs/checkout/fx-as-a-service/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Foreign Exchange as a Service
slug: /docs/checkout/fx-as-a-service/
createTime: '2025-05-14T22:40:32.971Z'
updateTime: '2025-10-27T22:52:33.035Z'
---


# Foreign Exchange as a Service


## Overview 
PayPal's Foreign Exchange as a Service (FXaaS) is a currency conversion service that helps businesses display prices and accept payments in a buyer's local currency.



## Key features 
FXaaS equips businesses to:

- **Enhance customer conversion rates** by displaying prices in over 100 local currencies.
- **Drive revenue growth** through seamless acceptance of local currency payments.
- **Minimize operational friction** by holding funds in 25 different currencies.
- **Streamline cash flow management** by converting local currency payments into a preferred currency.
- **Mitigate Foreign Exchange (FX) risks** with protection against FX volatility.



## How it works 
![FXaaS overview workflow diagram](assets/fxaas-overview.png)

- **Merchant | Partner**: Requests the exchange rate between a base and quote currency.
- **PayPal (FXaaS)**:
  - Sends the exchange rate for the requested currency pair, including the PayPal FX fee and any additional FX markup (if merchant or partner has requested for this).
  - Locks the exchange rate.
- **Merchant | Partner**: Caches exchange rate.
- **Buyer**: Visits the purchase website.
- **Merchant | Partner**: Displays the product's price to the buyer in their local currency.
- **Buyer**: Selects the product, proceeds to checkout, and submits the payment in their local currency.
- **Merchant | Partner**: Sends the transaction details to PayPal for processing.
- **PayPal (FXaaS)**:
  - Verifies if the locked rate is still valid, applies the locked FX rate, and converts the payment from the buyer's local currency to the merchant's or partner's base currency.
  - Deducts applicable fees.
  - Settles the converted amount into the merchant's or partner's account.



## Eligibility 
**Account type - Business account**: To integrate FXaaS and go live, your PayPal business account must be approved to use FXaaS.

- **New merchants or partners:** Contact PayPal to create a business account and request FXaaS.
- **Existing merchants or partners:** Contact your Account Manager to verify country and currency eligibility and enable FXaaS for your account.

**FXaaS contract:** PayPal activates FXaaS for your account based on a contract, which defines key parameters such as the rate expiration interval, PayPal's rate refresh time, FX fees, and other relevant terms. You can consult your PayPal Account Manager to understand and finalize the contract.



## Plan your integration 
**Integration pattern:** APIs only.

This integration section enables you to integrate FXaaS into your website to accept payments in your buyer's local currency. Before you integrate FXaaS, decide on the following:

- The payment methods you want to integrate FXaaS with. You can integrate FXaaS with the payment methods that use the Orders v2 API for order capture, such as:
  - PayPal wallet.
  - (Advanced) credit and debit cards.
  - (Alternative payment methods) Apple Pay and Google Pay.

- **Partners:** The payout model you want to implement. FXaaS supports immediate and delayed disbursement.
