---
title: "Adyen Salesforce OMS manual package setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup/2026-09-15.md"
tags: [adyen, salesforce-oms, package-setup, webhooks, capture]
---

## Overview

This Adyen page explains **manual** configuration of the Salesforce Order Management System (OMS) package for orders from a Salesforce Commerce Cloud storefront using Adyen's payments cartridge. From **Salesforce OMS v3.3.0**, guided configuration is the stated default; this page is the manual alternative. It is separate from the SFCC storefront integration and does not prove a merchant's OMS installation, payment result, capture, refund or bank receipt. See [[adyen]] and the proposed [[adyen-salesforce-order-management-system]] concept.

## Key takeaways

- Before manual setup, the page calls for an OMS Org connected to the SFCC storefront, Standard webhooks, Customer Area manual capture and the dependent **API Library Apex Adyen** package. It then installs the Adyen Payments for SOM app and enables multiple currencies. The page later describes **automatic-capture configuration** as a separate branch; do not infer every deployment remains on manual capture.
- The main Salesforce **Payment Gateway** record uses Adyen OMS Provider, merchant credential `AdyenCheckout` and an External Reference that must match the SFCC B2C Payment Processor ID. A second `AdyenPos` gateway is only for in-person endless-aisle payments. Fields on Sales Channel, Payment and Payment Authorization objects and optional sales-channel-to-merchant-account mapping are setup choices, not merchant-of-record or legal-entity assignments.
- The webhook path exposes Salesforce site endpoints for default status updates and Customer Area payment modifications. It enables **Guest Access to the Payments API**, site custom-metadata/Apex/principal access and a Named Credential site URL. Customer Area Standard webhooks require JSON, selected TLS, an HMAC key and capture/refund event subscriptions; CANCELLATION and AUTHORISATION are conditional on Authorization Reversal and Order on Behalf Of. A configuration-test HTTP 200 checks endpoint response, not downstream payment or OMS state.
- **A REFUND or CAPTURE webhook with `success: true` can still precede a later failure**, while a processed Salesforce payment status cannot be changed. The page directs monitoring `PaymentGatewayLog.GatewayResultCode` for `CAPTURE_FAILED` or `REFUND_FAILED`; keep this exception distinct from a final success conclusion.
- Named Credentials are installed by the app, but a **Principal Credential** with API key and permission-set access must be configured for the Automated Process user, or the replacement automation user if process settings differ. Salesforce legacy Named Credentials are deprecated for this package version. The Adyen Adapter metadata carries a **case-sensitive merchant account**, HMAC key and webhook ID; optional sales channels can override its default merchant account subject to API permissions and their own metadata.
- Capture behavior depends on the Customer Area setting. With automatic capture, configure OMS to avoid duplicate requests, while listed method variants can still require manual capture; payment methods captured immediately after authorization must be listed in SFCC Business Manager as **without separate capture**. The supplied variant list is an example, not a universal merchant setting. For live operation the page calls for a live account, refreshed HMAC/merchant account if applicable, live Checkout Named Credential URL and live API key. These are configuration steps, not evidence of successful live execution.

## Detail locators

- Scope, v3.3.0 guided default and prerequisites: pinned raw lines 15–50.
- App install and conditional Payment Gateway records: pinned raw lines 51–100.
- Site endpoint, guest permissions, webhook JSON/TLS/HMAC/events and later-failure warning: pinned raw lines 102–214.
- Layout, Principal Credential, permission set, automated user and Adyen Adapter metadata: pinned raw lines 216–338.
- Alternative-method object access and capture-setting branches: pinned raw lines 340–405.
- Live-account, HMAC, URL and API-key transition: pinned raw lines 407–431.

## Related

- [[adyen-salesforce-order-management-system]] — proposed OMS concept route owned by the campaign overview worker.
- [[adyen-salesforce-commerce-cloud]] — distinct storefront integration.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/install-and-set-up-the-package/manual-setup/2026-09-15|Adyen Salesforce OMS manual setup, captured 2026-09-15]]
