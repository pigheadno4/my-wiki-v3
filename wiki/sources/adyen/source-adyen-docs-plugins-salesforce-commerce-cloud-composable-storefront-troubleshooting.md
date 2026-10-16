---
title: "Adyen Composable Storefront troubleshooting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/troubleshooting"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/troubleshooting/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, troubleshooting]
---

## Overview

This Adyen page gives a diagnostic sequence for a **Salesforce Commerce Cloud Composable Storefront** integration: check package setup, inspect logs, compare package version with release notes, review open GitHub issues, then contact Support or file a bug if the problem persists. It was last modified in 2024 and captured in 2026. These are conditional investigation routes, not proof of an identified cause, applied fix, successful order or payment. See [[adyen]] and [[adyen-salesforce-commerce-cloud]].

## Key takeaways

- The page defines **Info** for business events such as status changes, **Warn** for unexpected situations, **Error** for operations being prevented, and **Debug** for sent parameters. Logs can be read in the console or Salesforce Log Center; ensure access before testing, and inspect browser console logs if the integration logs show no error. A log category alone does not identify root cause or payment outcome.
- To compare with known issues or later fixes, the guide locates the package version on a payment's Customer Area **Payment Details → Application Info → Payment Device Version**. It then routes to release notes and open GitHub issues. A later-version fix description is a lead to investigate, not evidence that the installed integration has been upgraded.
- If the issue persists, the guide suggests a GitHub issue for a bug or Support contact with package version and relevant screenshots/logs. **Debug logs contain sent parameters** according to the page; it gives no redaction or request-ID procedure. Handle any diagnostic material under the merchant's normal security controls.
- This Composable guide gives **no cache-clearing or third-party/custom cartridge isolation procedure**. Those steps are documented by the separate [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting|SFRA cartridge troubleshooting]] route and should not be applied to this package solely because both use Salesforce Commerce Cloud.

## Detail locators

- Composable scope and setup check: pinned raw lines 15–22.
- Log categories, locations and browser-console fallback: pinned raw lines 24–37.
- Release notes, package-version location and open issues: pinned raw lines 39–53.
- Escalation routes and evidence requested by Support: pinned raw lines 55–60.

## Related

- [[adyen-salesforce-commerce-cloud]] — storefront-family distinction.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting]] — separate SFRA cartridge diagnostics, with a different cache/customization path.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/troubleshooting/2026-09-15|Adyen Composable Storefront troubleshooting, captured 2026-09-15]]
