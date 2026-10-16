---
title: "Set up Adyen NetSuite Customer Center"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/set-up-netsuite-customer-center"
raw_files:
  - "adyen/docs/plugins/netsuite/set-up-netsuite-customer-center/2026-09-15.md"
tags: [adyen, netsuite, suitepayments, plugin, configuration]
---

## Overview

This Adyen guide configures the NetSuite Customer Center side of the Adyen payment plugin: install the chargeback and SuitePayments bundles, create payment-method instances, and set up a payment-processing profile. Optional alerts surface exceptions needing review. It documents configuration, not proof that a NetSuite order, payment, refund, capture or bank payout succeeded. See [[adyen]] and [[adyen-netsuite]] for provider and plugin context. The captured page does not identify a plugin package version or a named NetSuite administrator role.

## Key takeaways

- Install the NetSuite Chargeback Workflow Bundle (ID 127355) before the Adyen Payments Bundle for NetSuite (ID 125171), then activate ADYEN SUITEPAYMENTS IMPLEMENTATION. The first bundle supports chargeback/notification handling; the SuitePayments bundle supports processing between NetSuite clients and Adyen for cards and local payment methods. Menu paths and setup checkboxes are in the raw.
- Create a separate payment-method instance for each accepted method. PAYMENT INSTRUMENTS must be enabled before creating instances, except the guide says it must be disabled for debit cards. Cards and ACH have distinct instance types; BACS, Hosted Checkout local methods, Klarna, WeChat Pay and Pay by Link use their indicated External Checkout setup. Pay by Reference is for Pay by Link invoice payments and requires PAYMENT INSTRUMENTS. Card-token and general-token instances are additional configuration if using tokenization in NetSuite; creating an instance does not show a stored token or a charge. Klarna Pay later and Pay over time are distinct methods and require line-level setup.
- One processing profile can accept multiple charge currencies but settles in only one currency to one bank account, so create a separate profile for each settlement currency. Separate profiles for cards versus local methods and each NetSuite subsidiary are recommendations, not universal requirements. The profile selects website, subsidiary, settlement currency/account, charge currencies, 3D Secure option, test mode and inactivity; TEST MODE uses Adyen test endpoints and overrides the production endpoint prefix. The merchant-account ID and basic-auth credentials/API key bind the profile to the intended Adyen account and environment.
- Credential handling has a persistence trap: NetSuite does not send nulls, so blanking a previously filled credential field still passes the previous value. Hosted Checkout requires the CHECKOUT ENDPOINT DOMAIN PREFIX. The guide says the plugin migrated HPP methods to Hosted Checkout from 2023-02-13; prior HPP users must add that prefix to their NetSuite processing profile. Endpoint examples are configuration instructions, not proof of a live call.
- The SuiteCommerce Advanced table includes online payment with sales-order creation, optional purchase-order field, zero-order page hiding, payment-method display restrictions and card-info display settings. These website switches do not establish the submitted order amount or a payment result. Gateway request types selected are AUTHORIZATIONS, CAPTURES, SALES and REFUNDS. SuiteCommerce 3D Secure has a separate website checkout setting.
- Optional saved-search emails cover notification exceptions and rejected/payment-hold events. Adyen says that, in rare cases such as a later capture failure, payment status may not be reflected in NetSuite and the order needs a manual update to synchronize the two back ends. An order record or queued alert therefore needs reconciliation with the payment event before claiming an outcome.

## Detail locators

- Setup sequence and optional alerts: raw lines 15–21. Bundle prerequisites, IDs, activation and NetSuite chargeback review path: `## Install the Adyen payments bundles`, lines 23–75.
- Per-method instance types, PAYMENT INSTRUMENTS exception, token variants and Klarna line-level requirement: `## Create a payment method instance`, lines 77–211.
- Profile currency/bank-account grain, recommendations, fields, environment and credentials: `## Create a payment processing profile`, lines 213–246. Merchant account and endpoint fields: lines 248–265. Hosted Checkout migration, payment information and gateway request types: lines 267–282.
- SuiteCommerce Advanced website fields, including zero-order and card-info settings: lines 284–309. Separate 3D Secure checkout setting: lines 311–319. Notification and payment-event exception searches, with manual order-update warning: `## Set up email alerts`, lines 321–385.

## Related

- [[adyen]] — provider context.
- [[adyen-netsuite]] — plugin overview and NetSuite route.
- [[adyen-account-structure]] — Adyen merchant-account and company-account hierarchy; this page configures a NetSuite profile for a merchant-account ID.

## Related raw API references

- The raw page links to NetSuite tokenization, Adyen account structure, API credentials, 3D Secure, Pay by Link themes, capture failure and the NetSuite glossary. Those linked pages own their detailed behavior until read separately.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/set-up-netsuite-customer-center/2026-09-15|Adyen Docs: Set up NetSuite Customer Center (2026-09-15 snapshot; page last modified 2024-12-30)]]
