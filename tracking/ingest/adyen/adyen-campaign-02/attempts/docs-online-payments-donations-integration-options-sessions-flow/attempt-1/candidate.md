---
title: "Adyen Docs: Donations with Sessions flow"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/donations/integration-options/sessions-flow"
raw_files:
  - "adyen/docs/online-payments/donations/integration-options/sessions-flow/2026-09-15.md"
tags: [adyen, giving, donations, sessions-flow, web-drop-in, web-components]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] Giving guide describes donations in a Web Sessions integration using either Drop-in or Components. After a successful original payment, the UI can offer an eligible shopper an active campaign; a donation uses the same payment method as the original purchase and is a separate transaction. The two routes use Sessions and have their own UI configuration, while the Adyen Giving merchant `DONATION` webhook reports the donation outcome. See [[adyen-giving]].

## Key takeaways

- Both routes specify Web v6.36.0 or later with Sessions and Checkout API v72 or later, the Donation campaigns manager Customer Area role, Standard and Adyen Giving merchant webhooks, a supported payment-method integration, and an active campaign. The guide also points to separate general Giving requirements. It does not prove a particular merchant is configured, that the shopper is eligible, or that a donation succeeds.
- Neither route requires donation-specific parameters in the merchant's `/sessions` request. Drop-in or the Component handles campaign presentation and donation processing after a successful original payment when the shopper is eligible and an active campaign is present. The offer can be a fixed amount or a round-up.
- The checkout `donation` configuration is optional. If included to customize behavior and receive client results, both `onDonationSuccess` and `onDonationFailure` handlers are required in the documented configuration. `onDonationSuccess` covers both a completed donation and a shopper decline; its `didDonate` value distinguishes them. The separate `DONATION` webhook carries the donation outcome and `originalReference` for association with the original payment.
- Drop-in mounts the donation form in its own container by default and handles the full donation flow without separately creating a Donation Component. The Web Component also mounts the form in the original Component container by default; its route additionally shows `donation.autoMount: false` and creation of a new Donation Component in `onPaymentCompleted` to use a separate container when `result.askDonation` is true.
- The earlier Advanced-flow guide's Web Components section points into Sessions setup despite its Advanced-flow heading. This Sessions guide confirms a distinct Sessions route; do not combine the Advanced-flow request steps with this guide's automatic Sessions handling as one implementation recipe.

## Detail locators

- **Drop-in scope and requirements** — `## Web Drop-in`, raw lines 19-46; includes version, role, webhook, payment-method, and campaign conditions.
- **Drop-in sequence and configuration** — `## How it works` through `## Add Giving configuration`, raw lines 48-148; covers `/sessions`, eligible campaign presentation, optional `donation` object, callbacks, and default mounting.
- **Drop-in webhook outcome** — `## Get the donation outcome`, raw lines 150-191; `DONATION`, `success`, and `originalReference`.
- **Web Component scope and sequence** — `## Web Components`, raw lines 205-277; its own versions, conditions, and automatic donation flow.
- **Web Component configuration and alternate container** — `## Add Giving configuration` through `### Show the donation form in a separate container`, raw lines 279-364; optional configuration, handlers, `autoMount`, and `onPaymentCompleted`.
- **Web Component webhook and testing route** — raw lines 366-419.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-giving]]
- Related source: [[source-adyen-docs-online-payments-donations-integration-options-advanced-flow]]

## Raw Sources

- [[raw/adyen/docs/online-payments/donations/integration-options/sessions-flow/2026-09-15|Adyen Docs — Donations with Sessions flow (2026-09-15)]]
