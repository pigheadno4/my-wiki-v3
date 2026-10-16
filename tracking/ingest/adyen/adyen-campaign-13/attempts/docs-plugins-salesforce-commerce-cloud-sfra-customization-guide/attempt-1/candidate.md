---
title: "Adyen SFRA customization guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/customization-guide"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/customization-guide/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, cartridge-customization, checkout]
---

## Overview

This Adyen guide describes checkout-flow, payment-method configuration, and pre-authorization customization for the Salesforce Commerce Cloud Storefront Reference Architecture (SFRA) cartridge. It recommends placing merchant code in a separate cartridge before the Adyen cartridge so version upgrades can preserve that code and supported-version cartridge support can continue. The page is an SFRA customization guide, not Composable Storefront/PWA Kit authority or evidence that any custom checkout has been deployed or paid successfully. [[adyen]] [[adyen-salesforce-commerce-cloud]]

## Key takeaways

- The guide says direct changes to the default Adyen `/src/cartridges` can make support unavailable and upgrades/troubleshooting harder. Its separate-cartridge approach is available by default from v23.2.1, with the custom cartridge added before Adyen cartridges in the site cartridge path. It gives an extraction route for prior edits to the default code. The stated support continuation is conditional on a supported cartridge version, not a guarantee for arbitrary customization.
- The payment-method section lists methods that accept custom configuration and examples of `showPayButton`, `environment` (`test` or `live`), `onSubmit`, `onError`, and `onAuthorised` options. These are storefront configuration/callback descriptions; the method list does not prove a merchant has each method enabled, regional eligibility, security compliance, or a successful payment. An `onAuthorised` callback describes authorization, not capture or settlement.
- A material ambiguity in this page: its preferred separate-cartridge route discourages direct default-cartridge edits (lines 23–39), while `### How to customize` instructs editing files under `/src/cartridges/app_adyen_SFRA/...` (lines 160–171). Treat that direct-edit procedure as subject to the earlier support and upgrade warning; this source does not resolve how the two instructions fit together.
- From v25.4.0, an `app.payment.pre.auth` hook can run custom checks before the cartridge's Adyen `/payments` authorization request. Returning `error: true` stops the cartridge from making that request; `error: false` lets it proceed. The third-party risk-provider call is an example, not a built-in risk decision or proof of a payment outcome.
- The guide directs unit/end-to-end testing and deployment checks around customization. Its listed `npm install` and `npm run build` commands alone do not demonstrate tests passed. Display troubleshooting points to `showPayButton` and live Customer Area enablement; API errors point to Business Manager credentials. Actual version compatibility and method behavior require the installed cartridge and environment.

## Detail locators

- Opening, lines 19–39: Salesforce customization route, support boundary, no-default-edit warning, v23.2.1 separate-cartridge condition.
- `## Add custom code in a separate cartridge`, lines 41–67: creation, cartridge path order, build and test steps. `## Extract custom code from the default cartridge`, lines 73–111: comparison and migration navigation.
- `## Customize payment methods`, lines 113–158: method list and featured configuration options; `### How to customize`, lines 160–199: direct-path instructions and illustrative card configuration.
- `## Implement pre-authorization checks`, lines 201–214: v25.4.0 hook and return-value branch.
- `## Troubleshoot common issues`, lines 216–225: displayed-method, credential and deployment checks.

## Related

- [[adyen-salesforce-commerce-cloud]] — provider SFCC concept and SFRA-versus-Composable boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — SFRA setup and credential/webhook route.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-payment-methods]] — method-specific setup prerequisites.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/customization-guide/2026-09-15|Adyen SFRA customization guide, fetched 2026-09-15]]
