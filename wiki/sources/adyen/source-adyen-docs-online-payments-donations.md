---
title: "Adyen Docs: Donations using Giving"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/donations"
raw_files:
  - "adyen/docs/online-payments/donations/2026-09-15.md"
tags: [adyen, online-payments, giving, donations]
---

## Overview

This Adyen Giving documentation page explains how a merchant can offer a nonprofit donation within an online payment flow. A shopper's donation is a separate charge to the payment method used for the original transaction; Adyen says it settles the donation directly to the nonprofit's bank account and covers the fees. The page covers campaign setup, donation options, eligibility, and integration routes. It is a 2026-09-15 documentation snapshot, not evidence of a live merchant's eligibility or a completed donation.

## Key takeaways

- A merchant chooses an onboarded or pre-approved nonprofit and configures a Giving campaign in the Customer Area for participating merchant accounts, sales channel, donation type, and currency. A newly created campaign is inactive until started. The shopper sees separate payment and donation charges; the merchant makes a donation API request if the shopper opts in, and Giving webhooks report donation outcomes. See **Requirements**, **How it works**, and **Donation campaigns**.
- The documented online integration requires Checkout API v67 or later and one of the listed integration paths: Advanced-flow Web Components v5.0.0 or later, Sessions-flow Web Drop-in or Components v6.36.0 or later, or API only. Pre-checkout donation presentation is limited to API-only integration; post-checkout presentation is also described. See **Requirements → Integration type** and **Donation options → Interaction flow**.
- Giving supports fixed donation amounts or round-up, subject to region, currency, nonprofit, and payment-method limits. The supported tables are snapshot-specific; Singapore fundraising is limited to local nonprofits in this raw. See **Donation options**, **Supported countries/regions and currencies**, and **Supported payment methods**.
- Ending a campaign is consequential: an ended campaign cannot be restarted. Campaign edits and state changes take effect right away. See **Donation campaigns → Campaign lifecycle management**.
- The merchant must show the nonprofit's terms and conditions when offering Giving. See **How it works** and **Integration resources → Terms and conditions**.

## Detail locators

- **Requirements** — integration versions, Customer Area campaign roles, supported-method/currency checks, and nonprofit onboarding. The campaign roles do not grant payment-information access.
- **How it works** — nonprofit choice, campaign activation, shopper opt-in, donation API request, settlement, two statement charges, and Giving webhooks.
- **Donation campaigns → Set up a campaign / Campaign lifecycle management** — account and campaign choices, inactive creation state, activation, editing, ending, and immediate changes.
- **Donation options → Donation type / Interaction flow** — up to three fixed amounts or round-up; pre-checkout API-only and post-checkout timing.
- **Supported countries/regions and currencies / Supported payment methods** — snapshot tables and nonprofit-dependent currency availability.
- **Integrate with Giving / Integration resources** — online and point-of-sale routes, plugin version pointers, testing, terms, and reporting navigation.

## Related

- [[adyen-giving]]

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/donations/2026-09-15|Adyen Docs — Donations using Giving (2026-09-15)]]
