---
title: "Modify payments | Adyen Classic integrations"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/2026-09-15.md"
tags: [adyen, online-payments, classic-integrations, payment-modifications]
---

## Overview

This Adyen Classic integrations landing page routes existing online-payment integrations to capture, cancel, refund, cancel-or-refund, and authorization-adjustment documentation. It describes modifications as actions that change a payment's state.

## Key takeaways

- The page marks this endpoint inactive and unsupported for new integrations. It directs new integrations to Checkout API and existing endpoint integrations to contact Adyen about migrating to Checkout API.
- Capture applies to an approved authorization when needed to complete payment; cancellation applies before capture; refund returns funds to the shopper after capture.
- The cancel-or-refund route is for uncertainty about whether capture has occurred. Authorization adjustment changes the authorized amount after initial authorization.
- In-person cancellation and refund use separate point-of-sale documentation linked by this page.

## Detail locators

- Lines 19–24 — endpoint lifecycle, new-integration guidance, existing-integration migration, and Checkout API route.
- Lines 26–32 — Classic modification categories and their stated capture-state conditions.
- Line 34 — separate in-person cancellation and refund routes.

## Related

- Company: [[adyen]]
- Concept: [[adyen-online-payments]]
- Related concepts: [[adyen-payment-capture]], [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/2026-09-15|2026-09-15 snapshot — Classic modify payments]]
