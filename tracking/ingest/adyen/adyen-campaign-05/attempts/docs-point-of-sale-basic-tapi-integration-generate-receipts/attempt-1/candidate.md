---
title: "Adyen Terminal API receipt generation"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/generate-receipts"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/generate-receipts/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, receipts, payment-receipt, receipt-language, card-scheme-compliance]
---

## Overview

This Adyen Docs page explains receipt data in a Terminal API transaction response, generation of shopper and merchant receipts, and printing or alternate delivery on terminals with a built-in printer. It also covers receipt-language selection and the catalog of possible `PaymentReceipt` keys. See [[adyen]] and [[adyen-terminal-api]]. Standalone terminals are described separately as automatically printing their own compliant receipt; that statement does not make them POS-integrated Terminal API clients. A receipt or a listed `approved`, `refused`, or `void` key is transaction-result data, not evidence here of capture, settlement, or funds received.

## Key takeaways

- In a Terminal API payment result, `PaymentReceipt.CustomerReceipt` supplies data for a shopper receipt; `CashierReceipt` supplies a merchant receipt and can also support signature collection or reconciliation. A POS app can print, show, or email shopper receipt values. The generated key-value content varies with transaction type and result, cardholder verification method, issuer and store country/region, and payment method. The table lists keys that *can* appear; it is not a mandatory-field list for every receipt.
- Card-scheme receipt requirements vary by scheme and country/region and may change. Adyen says its generated receipts are certified by supported schemes and strongly recommends using the generated receipt data without alteration. A merchant that overrides that data or hard-codes accepted values is responsible for ongoing scheme compliance; a noncompliant receipt can lead to a chargeback. This snapshot is not a fresh independent compliance or legal determination for any merchant.
- If a Terminal API request contains characters from a non-Latin script, the page says those characters are URL-encoded; URL-decode the response `PaymentReceipt` before printing them. This is a receipt-rendering condition, not a general instruction to decode arbitrary payment-response fields.
- A terminal with a built-in printer, such as the cited V400m or V400c, normally prints from Terminal API receipt data. With the `ReceiptHandler` tender option in the payment request, that terminal does not print; the POS app can route the receipt data to its printer or email the shopper. A Customer Area **Ask before printing** setting lets the shopper choose printing after a transaction. Wide-screen multimedia terminals are separately linked for virtual display, without a guarantee that every terminal supports it.
- Merchant and shopper receipt-language flows differ. A Support-configured receipt language takes precedence for each. Without it, the merchant receipt uses the terminal primary language, then English if primary is absent. The shopper flow next considers card-issuer country/region language, then a shopper-selected secondary terminal language, primary language, and English fallback; excluded languages are skipped. Support is needed for a merchant or shopper receipt language different from the terminal's primary/secondary languages.
- The key table includes `cardholderName` only on the merchant receipt when Support enables it; it is absent by default. Other entries, such as preauthorization and funding source, also have enablement conditions. Do not mirror the full key table onto a shopper receipt or treat any example key as guaranteed.

## Detail locators

- POS response and standalone-terminal distinction: `# Generate receipts`, raw lines 15–21; Terminal API requirement and language setup pointer: `## Requirements`, lines 23–30.
- Scheme/region compliance warning and responsibility for overrides: `## Generating compliant receipts`, raw lines 32–40. Non-Latin request-character decoding: `## URL encoding`, lines 42–44.
- Virtual display and printer behavior, `ReceiptHandler`, shopper print prompt: raw lines 46–65.
- Merchant/shopper language configuration and fallback order: `## Changing the receipt languages`, raw lines 67–100; diagram repeats the flow at lines 102–142.
- `PaymentReceipt` roles and dynamic field conditions: `## Receipt data`, raw lines 144–160. Possible key catalog and field-specific enablement, including `cardholderName`: lines 162–230.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API payment-response and POS integration route; GitHub implementation versions remain separate.

## Related raw API references

- The raw page links to the payment-response guide, tender options, terminal feature configuration, virtual receipt display, terminal models, and mobile receipt-language guidance. Those targets are navigation until independently read; see raw lines 29–30, 46–56, 69–90, and 232–235.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/generate-receipts/2026-09-15|Adyen Docs: Generate receipts (2026-09-15 snapshot)]]
