---
title: "Adyen Cash App Pay iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/ios-drop-in/2026-09-15.md"
tags: [adyen, cash-app-pay, ios, drop-in, tokenization]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Cash App Pay** to iOS Drop-in for Sessions or Advanced flow. Drop-in renders the method and redirects the shopper to Cash App Pay to authorize; the Advanced return callback supplies data for a server request, not proof of authorization. It also details tokenization, $cashtag retrieval, asynchronous payment results and stored-token disabling. This method is distinct from Cash App Afterpay. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-cash-app-pay]].

## Key takeaways

- Both Sessions and Advanced requirement tables specify iOS Drop-in **minimum 5.2.0**, enabling **Recurring tokens life cycle events** webhooks, adding Cash App Pay in Customer Area with a Cash App client ID, and enabling **Payment > Recurring details** additional data. The Swift Package Manager installation section separately specifies Adyen iOS package **at least v5.42.0** and inclusion of `AdyenCashAppPay`; CocoaPods uses `Adyen/CashAppPay`. Keep these version contexts distinct. See raw lines 18–57.
- The page says no additional Cash App Pay fields are needed for `/sessions` or `/payments`. Set `dropInConfiguration.cashAppPay` with `CashAppPayConfiguration(redirectURL: ...)`. Sessions delegates to `AdyenSession`. In Advanced, after the shopper returns, `didSubmit` supplies `data.paymentMethod` to pass to the server; `didFail` and `didCancel` are separate app callbacks. Returning to the app or receiving `didSubmit` does not by itself establish payment success. See raw lines 59–118.
- Use the `/payments/details` `resultCode` to show the result and the asynchronous webhook for outcome updates. `Received` means shopper completion with final result **not yet known**, pending an **AUTHORISATION** webhook; `Authorised` is successful, and manual capture still needs capture. `Cancelled`, `Error`, and `Refused` have separate actions. See raw lines 129–141.
- For future recurring/card-on-file payments, the page supports tokenization and **strongly recommends explicit shopper permission**. Sessions `storedPaymentMethodMode` defaults to `disabled`; `askForConsent` and `enabled` depend on `shopperReference`, and storing details creates a token when the shopper pays. Advanced token creation passes client `data.storePaymentMethod` and `shopperReference` to `/payments`; stored payments use the `didSubmit` payment method. These are distinct flow recipes, not a blanket unattended-charge permission. See raw lines 143–165 and 177–192, 236–249.
- The page recommends including the shopper's **$cashtag** in recurring payments to help recognition. It says to obtain the $cashtag from `/payments/details` after enabling **Token information for digital wallets**; the `recurring.token.created` webhook includes shopper/token references but **not** $cashtag. Sessions users wanting it must switch to Advanced and implement both `/payments/details` and `/payments`. A `recurring.token.disabled` webhook signals shopper deletion of stored Cash App Pay details; remove the stored token and ask for another method to avoid future failed payments. See raw lines 167–175 and 194–254.
- **Configuration naming caveat:** the optional configuration table uses `showsStorePaymentField`, while later prose uses `showsStorePaymentMethodField`; the Sessions prose also says `storedPaymentMethod` where the table names `storePaymentMethod`. Check the actual SDK/API version before implementing consent controls. The `/payments/details` example has `merchantRreference`, apparently a typo. See raw lines 120–127, 161–164, 181–185 and 213–234.
- Test in the test environment using Cash App Pay magic values and check test Customer Area payment status. Going live requires adding Cash App Pay in live Customer Area. These are instructions, not proof of current enablement or a completed transaction. See raw lines 273–277.

## Detail locators

- Requirements, webhook/additional-data setup and package installation: raw lines 18–57.
- No extra API fields, Drop-in configuration and app callbacks: raw lines 59–118.
- Result codes and asynchronous outcome: raw lines 129–141.
- Sessions/Advanced token and consent flows: raw lines 143–192.
- $cashtag, token response and disabled-token notification: raw lines 194–271.
- Test and live steps: raw lines 273–277.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/ios-drop-in/2026-09-15|Fully read Cash App Pay iOS Drop-in raw]]
