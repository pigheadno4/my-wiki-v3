<!-- Source URL: https://developer.paypal.com/docs/checkout/fx-as-a-service/get-started/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Get started
slug: /docs/checkout/fx-as-a-service/get-started/
createTime: '2025-05-15T01:21:12.684Z'
updateTime: '2025-05-23T00:13:14.138Z'
---

# Get started

Prerequisites (standard): developer account, sandbox accounts, sandbox app credentials (Client ID + Client Secret), sandbox personal and business account credentials.

## Reference - Key terms

### Core currency types

**Primary currency**: The key currency in which you prefer to hold the balance in your PayPal business account. PayPal converts buyer payments into your primary currency and settles the money. Configurable via Account Settings → Money, Banks, and Card → Currency Management → Primary.

**Holding currencies**: The currencies in which you can hold the balance in your PayPal business account and present prices to buyers. Set by PayPal based on country eligibility; can be modified. Configurable via Account Settings → Money, Banks, and Card → Currency Management.

**Presentment currencies**: The currencies in which you can present prices to buyers but **cannot hold balances**. Set by PayPal based on account currency eligibility (not modifiable by merchant).

### FXaaS-specific terms

**Quote currency | Buyer currency | Payment currency | Transaction currency**: The buyer's local currency — the currency into which your base currency is converted when requesting an exchange rate. Can use both holding AND presentment currencies as quote currency.

**Base currency | Settlement currency**: The currency in which PayPal settles money into your business account — the currency that is converted INTO the buyer's currency. Can only use holding currencies as base currency (not presentment currencies).

Key distinction: **base currency = holding currencies only**; **quote currency = holding + presentment currencies**.

## Set up production business account

### View and modify primary currency
Account Settings → Money, Banks, and Card → Currency Management → currency marked "Primary"

### Manage holding currencies
Account Settings → Money, Banks, and Card → Currency Management → add or remove holding currencies

### Set payment receiving preferences
For PayPal to settle payments in a currency that is not a holding currency, set payment receiving preferences:

Account Settings → Payment Preferences → Block Payments → unblock payments sent in a non-holding currency.

Options:
- Convert any payment into primary currency automatically (auto-settlement)
- Or: payment status remains **pending** until manually approved in PayPal account

Additional blocking options:
- Payments from U.S. customers without confirmed address
- Payments for duplicate invoice IDs
- Payments from customers with non-U.S. PayPal accounts
