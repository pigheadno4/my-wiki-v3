---
title: "Online card surcharges | Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/surcharge"
raw_files:
  - "adyen/docs/platforms/online-payments/surcharge/2026-09-15.md"
tags: [adyen, platforms, online-payments, surcharge, split-payments, pilot]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms guide, captured 2026-09-15, describes a **pilot** for a platform's user to pass payment-acceptance costs to a customer as an online card-payment surcharge. The customer-paid surcharge, platform **commission**, and underlying **transaction/payment fees** are distinct amounts. By default the surcharge books to the platform's liable balance account; an explicit `Surcharge` split can book it to a user's balance account. The guide is not proof of pilot enrollment, legal compliance, card acceptance, payment authorization or final fund movement. [[adyen-platforms]]

## Prerequisites, compliance and amount boundaries

- The documented route requires Adyen for Platforms with **API-only online card payments** using raw or encrypted card data, an API key with the **Checkout webservice role**, a server able to receive and accept Standard webhooks, and optional Transfer/Transaction webhook subscriptions to track balance movements. Raw card data collection requires full PCI compliance in this guide; encrypted-card collection uses the Custom Card Component path. These channel and credential conditions do not establish an account's actual pilot or payment eligibility.
- The pilot may have restrictions, and the page says to contact Adyen to join. Surcharges cannot be added to **authorization adjustments or overcaptures**, and the amount cannot exceed what was shown to the customer at purchase. Compliance with legal, regional and card-scheme rules remains the platform's responsibility; the feature has **no automated global compliance enforcement**. As dated examples, the page says an EEA-issued consumer card cannot be surcharged for a payment in the EEA and a US debit-card payment cannot be surcharged in the US. These examples are not a current exhaustive legal analysis; the guide points to its surcharge-compliance source and legal advice.
- The platform's server calls `/cardDetails` using raw or encrypted card-number input and merchant account, then uses returned brand, funding source, commercial/consumer flag and issuing country to make its own surcharge decision and calculation. The raw-card `cardNumber` route specifies at least the first eight digits and recommends a full number for best result, subject to full PCI compliance; `encryptedCardNumber` is the alternative route. Card details inform the decision but do not themselves approve or collect a surcharge.

## Payment, booking and evidence

- Before payment, display the surcharge to the customer. The `/payments` request includes a `surcharge.value`, with `amount.value` equal to the original transaction amount **plus** surcharge. A split item with `type: Surcharge` can direct that surcharge to the user's balance-account ID; the field table marks `account`, `amount.currency`, `amount.value` and `type` required, recommends a reconciliation `reference`, and leaves `description` optional. The illustrated EUR 400 request separates EUR 394 sale value to user, EUR 2 surcharge to user, EUR 4 platform commission, and separate user-booked transaction fees. These example amounts and test API responses are not a universal pricing formula or completed payment. **Source discrepancy:** the table marks `amount.currency` required for the surcharge split but the illustrated JSON omits currency inside its split amounts; confirm the actual Checkout API contract before using the example.
- The page routes fund tracking through `balancePlatform.transfer.created`/`.updated` and `balancePlatform.transaction.created` webhooks. The illustrated surcharge transfer progresses `received` → `authorised` → `captured` with a `transactionId`, followed by a booked transaction; `platformPaymentType: Surcharge` distinguishes the surcharge from other split items. A received or authorised transfer is not a captured credit; a sample captured/booked balance-account event is still not seller bank receipt. Example payloads use a test environment, and their dates, balances and IDs are illustrative.
- For reconciliation, the guide strongly recommends a **Surcharge Amount** column in the Payment Accounting and Settlement Detail reports. When a `Surcharge` split type is specified in a request or split configuration, it says a separate incoming transfer is generated, with extra lines in the Balance Platform Accounting and Balance Platform Statement reports. Report lines support matching, not proof of bank payout.

## Detail locators

- **Surcharge purpose/default destination, pilot, card-channel/role/webhook gates and legal examples:** raw lines 15–53.
- **`/cardDetails` raw/encrypted conditions and response factors:** raw lines 55–322; test `/cardDetails` example starts at line 77.
- **`/payments` amount, surcharge/split fields, table/example discrepancy and EUR booking example:** raw lines 324–420; versioned test snippets continue through line 1122.
- **Transfer/transaction webhook status sequence and sample identifiers:** raw lines 1123–1451.
- **PAR/SDR recommendation and BPAR/BPSR surcharge lines:** raw lines 1453–1463.

## Related

- [[adyen-platforms]]
- [[adyen-online-payments]] — separate online card-payment context
- [[adyen-pci-dss-compliance]] — separate PCI context

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/surcharge/2026-09-15|Adyen Platforms online surcharge — collected 2026-09-15]]
