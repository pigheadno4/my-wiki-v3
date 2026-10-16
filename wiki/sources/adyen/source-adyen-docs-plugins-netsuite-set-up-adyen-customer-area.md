---
title: "Set up Adyen Customer Area for NetSuite | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/set-up-adyen-customer-area"
raw_files:
  - "adyen/docs/plugins/netsuite/set-up-adyen-customer-area/2026-09-15.md"
tags: [adyen, netsuite, customer-area, api-credentials, webhooks]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot gives Customer Area preparation for ecommerce payments through the NetSuite integration: API credential roles and account scope, record-type-dependent capture delay, and a Standard webhook to NetSuite's payment-processing profile. It documents configuration steps, not completed credential assignment, webhook delivery or payment outcome. [[adyen-netsuite]]

## Key takeaways

- After Adyen's get-started steps, the guide tells the merchant to create a Basic authentication password in the test Customer Area, copy and store that password securely, ask Support to enable **API PCI Payments** for the API credential, and ensure **Checkout webservice** and **Merchant PAL Webservice** roles. The web service user must also have the correct merchant accounts enabled under Roles and Associated Accounts. These are API-credential permissions and scope, not proof that a particular user or live merchant account is already enabled.
- Capture delay depends on the NetSuite transaction path in this guide: retain the stated immediate-after-authorization default for **Cash Sales**, while **Sales Orders** require selecting `manual` at merchant-account account settings. Choosing a capture setting is not itself a capture result, and an authorization should not be treated as an order charge or settlement.
- Adyen webhooks are called **notifications** in NetSuite and are described as HTTP callbacks for events such as payment-status changes and chargebacks. The page recommends configuring a company-account Standard webhook to avoid duplicate configurations, with all, selected or excluded merchant accounts. Its postback URL comes from the NetSuite payment-processing profile; it specifies JSON and TLS 1.2 for delivery. A configured URL and saved webhook do not prove receipt, validation or downstream order-state processing.
- The Basic authentication password here belongs to the API credential; this page does not specify webhook HMAC or webhook Basic-auth setup. Consult the linked NetSuite Customer Center/payment-flow guides for their distinct steps. No particular bundle version or live production setup is established by this snapshot.

## Detail locators

- **Prerequisite, API password/roles and merchant-account association:** raw lines 19–40.
- **Cash Sales versus Sales Orders capture delay:** raw lines 42–51.
- **Webhook/notification purpose, account scope, NetSuite postback URL and transport:** raw lines 53–84.
- **Linked NetSuite Customer Center and payment-flow next steps:** raw lines 86–94.

## Related

- [[adyen]]
- [[adyen-netsuite]]
- [[adyen-api-access]] — credential access context
- [[adyen-webhooks]] — separate webhook verification and lifecycle context

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/set-up-adyen-customer-area/2026-09-15|Adyen NetSuite Customer Area setup — collected 2026-09-15]]
