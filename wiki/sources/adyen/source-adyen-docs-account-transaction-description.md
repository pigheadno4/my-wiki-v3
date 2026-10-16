---
title: "Transaction description | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/transaction-description"
raw_files:
  - "adyen/docs/account/transaction-description/2026-09-15.md"
tags: [adyen, transaction-description, shopper-statement, payment-methods, customer-area]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot explains the transaction description (statement/billing descriptor) used to help a shopper recognize a charge, and how a merchant configures it in the **live** Customer Area or Management API. It covers merchant-account/store settings and payment-method-specific overrides, plus payment-request shopper statements for dynamic descriptions. [[adyen-transaction-descriptions]]

## Key takeaways

- Without customization, the description uses the Name in the live Customer Area plus the merchant-account address city and country/region. City and country/region remain appended after customization. The page recommends a cardholder-recognizable brand or merchant name and warns that unrecognized charges can increase chargeback risk and potentially scheme fines. See raw lines 19–24, 40–44.
- Options are a static DBA name, a dynamic shopper statement from the individual payment request, or DBA followed by that statement. Dynamic values must be enabled **and** sent as `shopperStatement` in each relevant request; otherwise the request value does not appear, and a configured DBA is the fallback when the request omits the statement. Ecommerce uses Checkout `/sessions` or `/payments`; POS carries it in Terminal API `SaleToAcquirerData`. See raw lines 46–77, 243–248.
- Live Customer Area configuration can apply one description to selected merchant accounts/stores or use a CSV for different descriptions (10 MB maximum). It applies across listed supported methods already added to the account/store. Live Management API configuration is per payment method and overrides the general Customer Area setting. The page distinguishes viewing roles from change roles: Customer Area needs Merchant admin or Change payment methods; Management API read can use Payment methods read or read and write, while changes require Payment methods read and write. See raw lines 26–38, 79–92, 94–143, 154–167, 191–241.
- The configured DBA, dynamic value, or combination has a **22-character** maximum including spaces; excess text is truncated before city and country/region are added. The page lists allowed characters. A single Customer Area change and a Management API method change are described as immediate for their selected transaction scope; a CSV change is applied within one calendar day. A Customer Area change affects current methods only, so newly added methods default to the DBA name. See raw lines 144–162, 169–189, 191–216, 218–241.
- Customization is supported only for the methods listed in the raw page. Wallet use is conditional on an underlying listed card brand. For eligible local-market ecommerce `/payments`, `localizedShopperStatement` accompanies `shopperStatement`; missing/empty localized content or a cross-border transaction uses `shopperStatement`. Japan has additional in-person store and online Kanji/Katakana routes, with brand-dependent character widths; the online request value overrides account values. See raw lines 250–335.

## Detail locators

- **Default, options, precedence and inspection:** raw lines 40–143.
- **Configuration paths, roles, format and propagation:** raw lines 144–241.
- **Request parameters and locale-specific behavior:** raw lines 243–302.
- **Supported methods and wallets:** raw lines 304–335.

## Related

- [[adyen]]
- [[adyen-transaction-descriptions]]
- [[source-adyen-docs-point-of-sale-add-data]] — separate Terminal API additional-data route

## Raw Sources

- [[raw/adyen/docs/account/transaction-description/2026-09-15|Adyen transaction description — collected 2026-09-15]]
