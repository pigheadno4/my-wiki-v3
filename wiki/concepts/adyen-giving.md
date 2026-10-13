---
title: "Adyen Giving"
type: concept
category: technology
tags: [adyen, giving, donations, checkout]
---

## Overview

Adyen Giving lets a shopper make a separate donation transaction using the payment method used for an original purchase. The captured Advanced-flow guide covers fixed-amount and round-up donations through either Web Components or a merchant-built API-only form.

## Advanced-flow routes

The Web Components route presents the Giving Component after the original payment. The API-only route lets the merchant present a donation option before or after checkout, then sends the donation request after the original payment is authorized; a post-checkout request follows shopper confirmation. Both routes depend on supported payment methods, an active campaign, the documented Customer Area role and webhooks, and their stated minimum integration versions. The Adyen Giving merchant `DONATION` webhook provides the donation outcome; iDEAL delivery may take a day or more. The 2026-09-15 guide's Web Components sequence also points to Sessions-flow setup despite its Advanced-flow heading, so exact implementation steps require route-specific verification.

## Sessions-flow routes

The 2026-09-15 Sessions guide covers Web Drop-in and Components on Web v6.36.0 or later with Checkout API v72 or later. After a successful original payment, an eligible shopper can be shown an active donation campaign; the UI handles the separate donation flow without donation-specific `/sessions` parameters. Optional `donation` configuration carries client callbacks, while the Adyen Giving merchant `DONATION` webhook provides the donation outcome. Components can place the donation form in a separate container by disabling `autoMount`; Drop-in manages its form in the Drop-in container. The separate Advanced-flow guide's Component sequence points into Sessions setup, so its explicit API steps should not be read as this Sessions route.

## Web version boundary

The captured Advanced-flow guide lists Web Components v5.0.0 or later and describes a Giving Component. The separate Web v6 upgrade guide says that from v6 onward an Adyen Giving integration must use the Giving Campaign Manager Component. These statements overlap for v6, and the snapshots do not explain how the two Components relate. Treat the Advanced-flow Component steps as guide-scoped and verify the version-specific route before implementation. [[source-adyen-docs-online-payments-donations-integration-options-advanced-flow]] [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]]

## Sources

- [[source-adyen-docs-online-payments-donations-terms-and-conditions]] — Giving page requiring display of the partner nonprofit's Privacy Policy and Terms and Conditions, with flexible presentation and an illustrative fill-in template (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-donations-testing]] — Adyen Giving test-and-live verification guide (webpage snapshot, 2026-09-15) for campaign activation, donation fixtures or live donation, and outcome checks.


- [[source-adyen-docs-online-payments-donations]] — Giving overview for nonprofit and campaign setup, eligibility, donation options, campaign lifecycle, and terms (webpage snapshot, 2026-09-15).

- [[source-adyen-docs-online-payments-donations-integration-options-sessions-flow]] — 2026-09-15 Adyen webpage guide to Web Drop-in and Components donations using Sessions, optional UI callbacks and the merchant `DONATION` webhook.

- [[source-adyen-docs-online-payments-donations-integration-options-advanced-flow]] — Adyen Advanced-flow donations guide for Web Components and API-only presentation, prerequisites, campaign/request flow, and webhook outcome (webpage snapshot, 2026-09-15).
- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]] — Web v5-to-v6 migration guide; Step 8 requires the Giving Campaign Manager Component from v6 onward (webpage snapshot, 2026-09-15).
