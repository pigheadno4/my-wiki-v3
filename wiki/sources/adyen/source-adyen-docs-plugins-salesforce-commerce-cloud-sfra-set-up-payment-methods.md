---
title: "Adyen SFRA payment-method setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/set-up-payment-methods"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/set-up-payment-methods/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, payment-methods, wallets]
---

## Overview

This 2023-last-modified, 2026-09-15-captured guide describes **payment-method configuration for the Adyen Salesforce Commerce Cloud SFRA cartridge** in Salesforce Business Manager and Adyen Customer Area. It is not the Composable Storefront package guide and names no exact installed cartridge version. Configuration settings, test routes and storefront buttons do not prove that a merchant is eligible, that a shopper was charged, or that an order, capture, refund or settlement completed. See [[adyen]] and [[adyen-salesforce-commerce-cloud]].

## Key takeaways

- **Base SFRA setup and display:** After metadata import, Adyen is described as payment processor for credit cards and merchant-account-enabled local methods. The guide directs checking enabled `AdyenComponent` and `CREDIT_CARD` payment methods and assigning `Adyen_Component` as processor in Business Manager. Displayed methods depend on shopper order amount, currency and shipping country; their country-specific order can be changed in Customer Area. The cartridge's description text is editable in its SFRA config file. These are configuration conditions, not method-availability guarantees.
- **Apple Pay branches:** With **Adyen's certificate**, the guide describes checkout and express use, requires adding Apple Pay and Shop website URLs in test Customer Area, disallows `http://localhost` testing, offers optional Express toggles, and gives a live domain-association/alias procedure. With the merchant's **own certificate**, the Salesforce-provided integration is **express-only** and Adyen says Salesforce handles troubleshooting. That route calls for the Salesforce `plugin-applepay` cartridge, Apple merchant identifier and processing certificate, Salesforce domain registration, and Business Manager payment-provider configuration with environment-specific Adyen URL and Basic-auth API credential. These are distinct paths; neither setup instruction proves a live Apple Pay transaction.
- **Other express and local methods:** Amazon Pay Express requires merchant-method addition plus Amazon Pay registration, sandbox buyer and PublicKeyId steps before a cart/mini-cart toggle. Klarna's inline widget is optional after adding Klarna. Credit-card installments are optional in some countries and have per-card-type minimum amount, count and allowed-type rules. Gift cards require Support confirmation of setup. Google Pay standard flow needs test Customer Area enablement; Express has separate site toggles and live use requires a Google Merchant ID. Keep these method-specific prerequisites separate.
- **PayPal qualifications:** Live PayPal setup points to a PayPal Merchant ID and Adyen Customer Area enablement. The page says Venmo appears when merchant and shopper are both in the US, with a hide option. PayPal tokenization requires additional Adyen-side configuration even if shopper-detail storage was enabled for the cartridge. Existing users of the old PayPal Express integration are directed to Support for the new flow. Its prose names cart and mini-cart display, while the toggle step lists product detail, cart, mini-cart and shipping pages; verify storefront behavior for the installed cartridge rather than merging those into a guaranteed placement.
- **Lifecycle boundary:** The page ends with a live-account checklist route. It does not define universal API credential roles, capture mode, webhook/order-status semantics, or financial finality. Follow the SFRA cartridge/setup and payment-method authorities for those matters.

## Detail locators

- `## Requirements` and `## Arrange payment methods`, lines 25–40: metadata import, merchant-account method setup, Business Manager processor IDs and amount/currency/country display.
- `## Adjust payment method descriptions`, lines 44–51: SFRA description file.
- `## Apple Pay`, lines 53–183: certificate branches, test/live domains, Express and own-certificate plugin/credential configuration; the JSON alias and field table are routine setup detail at lines 94–183.
- `## Amazon Pay Express`, lines 185–200; `## Klarna payment widget`, lines 202–212; `## Credit card installments`, lines 214–235; `## Gift cards`, lines 237–241.
- `## Google Pay`, lines 243–260; `## PayPal`, lines 262–281: environment, express, Venmo, tokenization and old-flow conditions.

## Related

- [[adyen-salesforce-commerce-cloud]] — pending provider concept proposed by the SFCC overview worker; reciprocal source route.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud]] — SFRA versus Composable overview, not SFRA method configuration.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — separate cartridge setup evidence.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/set-up-payment-methods/2026-09-15|SFRA payment-method setup, captured 2026-09-15]]
