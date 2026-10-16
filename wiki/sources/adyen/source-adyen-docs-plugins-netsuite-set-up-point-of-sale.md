---
title: "Adyen NetSuite SuiteCommerce InStore POS setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/set-up-point-of-sale"
raw_files:
  - "adyen/docs/plugins/netsuite/set-up-point-of-sale/2026-09-15.md"
tags: [adyen, netsuite, suitecommerce-instore, pos, terminal-api]
---

## Overview

This 2023-last-modified, 2026-09-15-captured Adyen guide describes configuring **NetSuite SuiteCommerce InStore (SCIS)** for in-person payments through Adyen terminals and Terminal API. It is a NetSuite POS profile, credential, device and callback setup procedure, not evidence that it was performed or that a terminal sale, capture, refund, deposit or bank payout succeeded. See [[adyen]] and [[adyen-netsuite]]; [[adyen-terminal-api]] owns the broader terminal protocol boundary.

## Key takeaways

- **Prerequisites and scope:** The guide requires the NetSuite Chargeback Workflow Bundle and Adyen SuitePayments Bundle plus network connectivity for the POS app and terminal. It names supported terminal models in the raw, recommends a separate Adyen merchant account for in-person processing, and says multiple stores can share one merchant account with `storeID` distinguishing locations. Those are guide claims for this SCIS integration, not a current hardware/region eligibility check.
- **Adyen credential and role setup:** From a **company-account** Customer Area login, create/select a Webservice API credential, generate an API key and note the separate Basic-auth password, store both securely because the guide says they cannot be restored later. Associate the relevant merchant accounts and enable **API PCI Payments Role** (requires Support contact mentioning NetSuite), **Merchant PAL Webservice Role**, and **Checkout webservice Role**; saved configuration makes the credentials effective. This is credential configuration, not proof of a usable live connection.
- **NetSuite profile and terminals:** The guide sequences multiple shipping routes, an SCIS `EMV` payment-method instance, a separate POS payment-processing profile, and registered device IDs. The profile selects SCIS website, subsidiary, settlement currency/bank account, charge currencies, test mode, Adyen merchant account, POS shopper interaction and authorization/capture/sale/refund request types. **TEST MODE** overrides the production endpoint prefix. The production-prefix field's example is a `pos-payment-test` URL; verify the actual live URL from Customer Area rather than copying that example into production. Each terminal must be registered in NetSuite under a unique `[device model]-[serial number]` ID with Adyen EMV; registration alone proves no transaction.
- **Callbacks and security:** For payment status changes, the guide configures a Standard webhook on the POS merchant account to the NetSuite payment-profile postback URL, with JSON and TLSv1.2 and selected merchant accounts. Separately, the Adyen Terminal API integration needs its Event URL set to the postback URL, choosing Public or Local network scope. It instructs contacting Support to enable WebSockets and applying device settings per device. A saved endpoint is not proof it is reachable, authenticated, receiving events or updating a NetSuite payment.
- **Financial boundary:** The profile's settlement currency and bank-account fields are configuration targets. The guide supplies no actual amount, order reference, bank-credit record, settlement result, or assurance that every configured gateway request type succeeded.

## Detail locators

- `## Requirements`, lines 19–24: required bundles, network and named terminal models.
- `## Step 1: Set up your Adyen Customer Area`, lines 26–65: recommended merchant/store mapping, API key versus Basic-auth password, three roles, Support and merchant-account association.
- `## Step 2: Set up your NetSuite Customer Center`, lines 67–127: ordered SCIS method/profile setup, currency/account fields, Test Mode override, production-prefix example and request types.
- `### Set up device IDs`, lines 129–146: unique terminal ID format and NetSuite Adyen EMV registration.
- `## Step 3: Set up webhooks`, lines 148–167: POS merchant-account Standard webhook, postback URL, JSON/TLS and scope.
- `## Step 4: Enter the postback URL in the Terminal API settings`, lines 169–192: enable Terminal API, Event URL Public/Local scope, Support WebSockets and per-device settings.

## Related

- [[adyen-netsuite]] — reciprocal NetSuite bundle concept.
- [[adyen-terminal-api]] — protocol context, separate from this NetSuite setup.
- [[source-adyen-docs-plugins-netsuite-set-up-netsuite-customer-center]] — separate ordered NetSuite bundle and customer-center setup source.

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/set-up-point-of-sale/2026-09-15|NetSuite SCIS in-person setup, captured 2026-09-15]]
