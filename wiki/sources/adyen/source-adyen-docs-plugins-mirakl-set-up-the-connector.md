---
title: "Set up the Adyen Mirakl connector"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/set-up-the-connector"
raw_files:
  - "adyen/docs/plugins/mirakl/set-up-the-connector/2026-09-15.md"
tags: [adyen, mirakl, marketplace, connector, onboarding]
---

## Overview

Adyen's Mirakl connector setup page (last modified and captured 2026-09-15) describes Mirakl Operator API access, seller custom fields, feature/email settings, connector and Adyen credentials, and synchronization scheduling. It prepares a Mirakl Marketplace for Adyen for Platforms seller onboarding/KYC and split-payment-related data; it does not prove seller verification, live eligibility, payment splitting, payout completion, bank receipt or which party is merchant of record. See [[adyen-mirakl]] for the connector/pay-in boundary.

## Key takeaways

- In Mirakl back office, create an API integration with **Operator API** scope and an **Access token**, then store that token securely. This Mirakl token is distinct from the Adyen Balance Platform and Legal Entity Management API credentials later supplied for connector onboarding; this page does not describe an OAuth app or client secret (raw lines 19–29, 110–124).
- To initiate KYC checks and split-payment processing, create marketplace-model shop-profile custom fields that the connector maps to Adyen fields on seller-shop sync. The page says these connector fields must **not** be marked required; other required custom fields can prevent connector operation and should be raised with the Adyen contact. The table distinguishes seller balance-account, legal-entity, account-holder and transfer-instrument IDs, a read-only Hosted Onboarding Page URL, and conditional VAT/original-channel fields. The VAT field applies only to the stated cross-region invoice-VAT payout case; original channel only to multiple channels (raw lines 31–58).
- Mirakl Support must enable **KYC status** and **Payment confirmation**. KYC status lets the connector update Mirakl about check results/actions; Payment confirmation lets it mark invoices **Paid**, distinct from **Pending payment**. The connector's failure emails and recommended KYC-failure template are notification setup, not evidence that KYC or settlement occurred (raw lines 60–79).
- Supply the Adyen contact with connector settings (HOP return/name, operator emails, HOP questions, maximum invoice payout retry count, locale) plus Mirakl service URL/access token and Adyen balance-platform details. Optional defaults include **Manage Payment Block** enabled (skip seller in billing cycle on balance/KYC/sync issue), **Use Subscription** disabled (one combined commission/subscription payout when disabled), and **Unsuspend New Shops** enabled after KYC success; Adyen seller status is determined separately. These settings alter eligibility/scheduling behavior but do not prove a seller's funds moved (raw lines 81–115).
- Adyen settings call for the liable balance-account ID, which should retain sufficient funds for negative commissions or transfers can fail; a Balance Platform Configuration/Transfers web-service user with **Balance Platform BCL** role; and a separate Scope/LEM API web-service user. The page supplies account/credential identity and role guidance, not authority to expose keys or evidence of a completed transfer (raw lines 117–124).
- Schedule **Partial Sync** for changed shops, **Full Sync** for all shops, and **Start Invoice Sync** for payout scheduling. Give Adyen the invoice-sync start date to avoid importing older invoices and confirm that date with Support in both test and live environments; the June 1/May 31 example illustrates inclusion, not a universal date or payout guarantee (raw lines 126–136). Seller onboarding and payment-flow pages are next-step navigation (raw lines 138–150).

## Detail locators

- Mirakl Operator API token and secure storage: raw lines 19–29.
- Seller custom-field requirements, IDs, permissions and conditional VAT/channel: raw lines 31–58.
- Mirakl feature enablement and notifications: raw lines 60–79.
- Connector optional defaults and Mirakl settings: raw lines 81–115.
- Liable balance account and Adyen API credentials/role: raw lines 117–124.
- Sync types and test/live invoice start date: raw lines 126–150.

## Related

- [[adyen-mirakl]] — connector concept and separate pay-in boundary.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/set-up-the-connector/2026-09-15|Mirakl connector setup, captured 2026-09-15]]
