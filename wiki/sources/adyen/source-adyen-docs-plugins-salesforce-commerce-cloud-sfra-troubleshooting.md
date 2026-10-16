---
title: "Adyen SFRA cartridge troubleshooting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/troubleshooting"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/troubleshooting/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, troubleshooting]
---

## Overview

This 2020-modified Adyen webpage snapshot gives a **Salesforce Commerce Cloud SFRA cartridge** troubleshooting sequence: check setup, isolate third-party/custom cartridges, inspect logs, then investigate named payment-method, configuration, and order-placement symptoms. The steps are diagnostic suggestions, not proof of a particular fix, payment result, or order state. See [[adyen]] and [[adyen-salesforce-commerce-cloud]].

## Key takeaways

- Adyen says its payment cartridge does **not** use the SFCC cache, but recommends clearing caches while troubleshooting because a third-party cartridge may use them. It also advises checking cartridge-path precedence, temporarily disabling third-party cartridges, and isolating customizations by removing a separate custom cartridge or comparing against a clean Adyen installation (raw lines 25–53). Those are conditional isolation steps, not a finding that cache or custom code caused the issue.
- The guide locates error logs in Salesforce Business Manager's **Development Setup → WebDAV Log Files**, with browser console logs as another check if those logs show no errors (raw lines 55–63). For a missing payment method, inspect method-specific setup and the `service-adyen` logs for the `/paymentMethods` request's country/region and currency and for whether the method appears in its response (lines 73–79). A missing method in checkout is not by itself proof of merchant-account enablement or API failure.
- For origin-key retrieval or nonfunctioning payment calls, the page says incorrectly loaded metadata is **likely** and recommends reimporting metadata. Only **cartridge v20.1.2 or earlier** gets the additional live-endpoint setup check in live Customer Area (raw lines 81–93). This is a version- and environment-limited diagnostic, not a current-version universal requirement.
- For the exact order-placement error **“No user found for OriginKey on validation”**, check the Business Manager merchant-account name, then generate a new API key in Customer Area, copy it to Business Manager, and verify its access to the integration's merchant account (raw lines 95–102). Rotating the key changes a credential; it does not by itself prove that prior orders were fixed or safe to retry.
- The exact **PayPal** error **“Expected intent from order api call to be authorize, got capture”** is attributed here to a mismatch between code capture setting and Adyen-side setting, with a suggested code setting of `SALE` (raw lines 104–108). Do not generalize that setting to other PayPal flows or treat the advice as proof of capture/order success.
- The page routes readers to release notes, the cartridge version shown under a payment's **Application Info → Payment Device Version**, open GitHub issues, and Support if the problem persists (raw lines 110–131). It does not document webhook-job troubleshooting or authorize blindly retrying payment/order requests.

## Detail locators

- Steps 1–4, raw lines 25–63: cache, third-party/custom-cartridge isolation, and log access.
- Step 5, raw lines 65–108: symptom-specific payment-method, metadata/live-endpoint and order-placement checks.
- Steps 6–8, raw lines 110–131: version/release-note lookup and escalation routes.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable integration boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — SFRA setup route for keys, account scope, webhooks, and jobs.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/troubleshooting/2026-09-15|SFCC troubleshooting, fetched 2026-09-15]]
