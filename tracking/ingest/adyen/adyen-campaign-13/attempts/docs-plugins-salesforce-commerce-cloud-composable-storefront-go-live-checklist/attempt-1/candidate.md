---
title: "Adyen Composable Storefront go-live checklist"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/go-live-checklist"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/go-live-checklist/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, go-live]
---

## Overview

This 2023-modified Adyen checklist addresses **Salesforce Commerce Cloud Composable Storefront/PWA** preparation before accepting live payments. It says test-environment configuration is not copied into live, so account, finance, risk/compliance, API, webhook and live-region settings require separate attention; wallet methods have extra conditions. This checklist is not the SFRA cartridge guide, a package-version audit, deployment proof or evidence that a live payment succeeded. See [[adyen]] and [[adyen-salesforce-commerce-cloud]].

## Key takeaways

- In the live Customer Area, review merchant-account structure, give individual team members task-appropriate roles/account access, enable desired methods and check their checkout ordering and shopper statement. Add payout bank details if needed, review payout settings, set up reconciliation reports, and consider a Reserve and risk notifications/profile changes as the page specifies.
- For 3D Secure, the guide warns **Visa and Mastercard enrollment can take up to seven days** after live activation. A Composable Retail React App must authorize relevant scripts in its **CSP `script-src`** to render the live 3DS2 Component. The page directs merchants using this package to assess PCI DSS against SAQ A; it does not itself certify compliance.
- Live API credentials need the listed Merchant Recurring, Checkout webservice and Checkout encrypted cardholder data permissions. The **MRT** environment must use the live API key, appropriate endpoint-region `environment` value and live URL prefix; different sites can have separate region variables. This is site- and region-specific configuration, not a universal live endpoint.
- Configure live webhooks separately, check needed event types, accept all webhook events to avoid queuing, and set the MRT webhook user, password and HMAC key. The package has a scheduled job for webhook events. A Customer Area test can return HTTP 200 for a selected event, but that response alone does not prove the scheduled job processed an order or that payment settled. The checklist's webhook-setup link includes a `version=3.0.0` qualifier while MRT links use `version=latest`; apply the setup instructions for the actual deployed package version.
- Wallet steps apply **if used**: live PayPal account/Merchant ID, Google Pay go-live and Apple Pay go-live routes are separate. The checklist calls for real-detail end-to-end tests across offered methods, refused/FRAUD cases, full and partial refunds, and successful and incomplete 3DS challenges. Real-detail payments incur fees; an optional Reserve is suggested for refund funds. These are prescribed tests, not a claim that any merchant has run or passed them.

## Detail locators

- Live/test separation and account, finance, risk setup: pinned raw lines 15–85.
- CSP, SAQ A, live API roles and MRT API key: pinned raw lines 83–105.
- Live region, URL prefix and optional per-site variables: pinned raw lines 107–124.
- Live webhook setup, test response, scheduled job and credentials: pinned raw lines 126–148.
- Conditional wallets and charged end-to-end test scenarios: pinned raw lines 150–174.

## Related

- [[adyen-salesforce-commerce-cloud]] — Composable versus SFRA product boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-install-and-set-up-the-package]] — package setup details; follow its applicable version.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/go-live-checklist/2026-09-15|Adyen Composable Storefront go-live checklist, captured 2026-09-15]]
