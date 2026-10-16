---
title: "Adyen Adobe Commerce in-person payment setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-in-person-payments"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-in-person-payments/2026-09-15.md"
tags: [adyen, adobe-commerce, in-person-payments, terminal-api, pos]
---

## Overview

This 2024-last-modified, 2026-09-15-captured guide configures the Adyen Adobe Commerce plugin for **in-person payments through Terminal API**. It covers a separate POS merchant account, API key and roles, card capture delay, Terminal API/WebSockets settings, Commerce POS method fields, and optional tokenization. It does not identify an exact installed plugin or terminal software version, prove device/network readiness, or establish a successful terminal payment, order, capture or bank settlement. See [[adyen]], [[adyen-magento2]] and the separate [[adyen-terminal-api]] protocol concept.

## Key takeaways

- **Account and API setup:** The page requires a **separate merchant account** for in-person processing. A company-account Customer Area user selects a Payments or Platforms API credential, generates and securely stores an API key (the page says it cannot be copied after leaving), and saves it for Commerce configuration. Before live use, the credential needs **Merchant PAL webservice role**, with Support contact to enable it. Keep test and live keys in their respective Commerce fields; key generation and role configuration alone do not establish successful live API authentication.
- **Card capture model and irreversible remainder:** The guide describes card authorization as verification/reservation and capture as a later funds-transfer step; a configurable delay applies where a method supports separate authorization/capture. It says the delay does **not** affect Alipay, WeChatPay and some other one-step wallets. POS capture-delay choices are immediate, a specified time, or manual; two hours is a **recommendation**, not a rule. Manual capture requires creating a Commerce invoice per payment. **If only part of the authorized amount is captured, the remaining authorization is automatically cancelled** per this guide. Do not assume later capture of that remainder.
- **Terminal settings and access:** Account configuration requires **Merchant POS Terminal Management Admin role**. In test Customer Area at company scope, the guide enables Terminal API and WebSockets in terminal account configuration. It points to a separate terminal-selection guide but gives no model compatibility, local-network design, webhook setup or connector-version requirement here. Those must be checked in their own sources.
- **Commerce POS fields and order timing:** Commerce's **In-person payments** settings include the POS merchant account, optional **Terminal Store ID** limiting terminal selection to a store, separate test/live API keys, matching capture delay, optional card-installment rules and **Order Creation Time**. The default is **After payment**; **Before payment** creates the order before a payment request is initiated. This is order-object timing, not evidence payment was authorized, captured or completed. An enabled POS method or selected terminal does not prove a terminal result.
- **Optional recurring setup:** The page offers in-person tokenization with `CardOnFile`, `UnscheduledCardOnFile` or `Subscription` processing model. Enabling the field is configuration only; the page does not supply merchant consent, a created token, or a successful later charge.

## Detail locators

- Lines 15–25: Adobe Commerce/Terminal API scope and separate POS merchant account.
- `## Step 1: Generate an API key`, lines 27–53: company-scope credential, key storage and live Merchant PAL role.
- `## Step 2: Set up capture delay`, lines 55–86: two-step card model, wallet exception, immediate/timed/manual choices and partial-capture remainder cancellation.
- `## Step 3: Set up the terminal configuration`, lines 88–99: terminal-management role, Terminal API and WebSockets toggles.
- `## Step 4: Set up in-person payments in Adobe Commerce`, lines 101–122: merchant/store, environment keys, capture, installments and before/after order creation.
- `## Step 5 (optional): Set up recurring payments`, lines 124–139: POS tokenization toggle and recurring model selection.

## Related

- [[adyen-magento2]] — reciprocal Adobe Commerce plugin concept and versioned implementation route.
- [[adyen-terminal-api]] — separate terminal protocol and result handling.
- [[source-github-adyen-magento2]] — exact `adyen/module-payment@11.0.0` implementation evidence.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-in-person-payments/2026-09-15|Adobe Commerce in-person setup, captured 2026-09-15]]
