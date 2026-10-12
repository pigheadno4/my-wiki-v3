---
title: "Adyen Docs: Donations with Advanced flow"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/donations/integration-options/advanced-flow"
raw_files:
  - "adyen/docs/online-payments/donations/integration-options/advanced-flow/2026-09-15.md"
tags: [adyen, donations, giving, advanced-flow, web-components]
---

## Overview

This Adyen Giving guide covers donations with Web Components or an API-only Advanced-flow integration. A donation is a separate transaction using the shopper's original payment method. The guide distinguishes the Giving Component, which shows a donation form after the original payment, from a merchant-built API-only form that can offer fixed-amount or round-up donations before or after checkout. See [[adyen-giving]] and the two separately headed routes in the raw snapshot.

## Key takeaways

- The Web Components route specifies Web Components v5.0.0 or later and Checkout API v67 or later; the API-only route specifies Checkout API v67 or later. Both routes also list the Donation campaigns manager Customer Area role, Standard and Adyen Giving merchant webhooks, supported payment-method integration, and an active donation campaign. General Giving requirements remain in a separately linked guide.
- In the API-only route, the merchant server retrieves active campaigns with POST `/donationCampaigns`, presents the form, and sends POST `/donations` only after the original payment is authorized. For a post-checkout offer, the shopper confirms the donation first. Campaign lookup after payment is conditioned on a `donationToken` in `/payments` or, for iDEAL, `/payments/details`.
- The donation request uses the original payment reference and donation token. The Apple Pay subsection specifies a different `paymentMethod.type` based on the returned brand variant; use its own field table rather than the general card/iDEAL example.
- The donation outcome is delivered through the Adyen Giving merchant `DONATION` webhook. A synchronous `/donations` response may be `completed`, `pending`, or `refused`; the guide says to wait for the webhook before showing card success, and says an iDEAL webhook can arrive a day or more later.
- **Documentation inconsistency:** Under the Advanced-flow Web Components heading, the “How it works” sequence creates a payment session and links to Sessions-flow setup, while later sections describe explicit campaign lookup and `/donations` requests. Do not combine those descriptions into one assured implementation recipe. The two general `/donations` curl examples also omit a comma before `merchantAccount` (raw lines 314–315 and 718–719), so they are not copy-ready JSON.

## Detail locators

- **Web Components → Requirements and How it works, raw lines 19–90** — component version, role/webhooks/setup, post-payment presentation, and the Sessions-flow inconsistency.
- **Web Components → Get details / Show Giving / Make a donation, raw lines 91–371** — authorized-payment and `donationToken` condition, campaign lookup, Component configuration, callbacks, request fields, and Apple Pay variant.
- **Web API only → Intro / Requirements / How it works, raw lines 429–498** — merchant-owned form, version/setup, and separate pre-checkout and post-checkout sequences.
- **Web API only → Get details / Present the option, raw lines 499–679** — campaign response shapes, form requirements, round-up calculation, decline route, and iDEAL bank-statement notice.
- **Web API only → Make a donation / Get the donation outcome, raw lines 680–820** — authorization and confirmation timing, field tables, Apple Pay variation, response status, webhook outcome, and iDEAL delay.
- **Test and go live, raw lines 821–823** — Adyen's test-card route before live integration.

> [!warning] Contradiction
> The Advanced-flow guide lists a Giving Component for Web v5.0.0 or later, while the Web v6 migration guide requires a Giving Campaign Manager Component from v6 onward. The snapshots do not explain the overlap. See [[adyen-giving]] and the version-specific guide before implementation.

## Related

- [[adyen]]
- [[adyen-giving]]
- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/donations/integration-options/advanced-flow/2026-09-15|Adyen Docs — Donations with Advanced flow (2026-09-15)]]
