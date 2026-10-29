---
title: "Alma Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/web-component"
raw_files:
  - "adyen/docs/payment-methods/alma/web-component/2026-09-15.md"
tags: [adyen, alma, web, components, redirect, installments]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Alma to an existing Web Components integration through Sessions or Advanced flow. It covers request additions, Redirect Component setup, optional installment count and test/live routes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma overview]] for captured FR/EUR method scope. The TEST samples do not prove account eligibility or a completed payment.

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later and Alma added in Customer Area. Advanced requires its Web Components base integration, `action.type: redirect` handling and Customer Area setup. TEST curl samples use Checkout API v71 for `/sessions` and v72 for `/payments`, both with FR/EUR.
- The Alma-specific `/sessions` and `/payments` tables list telephone number, shopper email, billing and delivery addresses with blank Required cells. Advanced also lists optional `additionalData.alma.installments_count`: `3` or `4` chooses the installment count, while omission lets the shopper choose. The examples include optional fields but do not make them mandatory.
- Import Adyen Web with `Redirect` and initialize that class for Alma; the Sessions flow says no extra method configuration is needed. The JavaScript example writes `{ type:alma }` without quoting or defining `alma`, so treat it as illustrative rather than verified runnable code.
- The Web Sessions TEST sample uses an Android-style app-scheme `returnUrl` placeholder `adyencheckout://your.package.name` (line 64), while the Advanced Web sample uses HTTPS (line 184). The guide does not reconcile this cross-platform example difference or show a completed return. The Advanced example shows `RedirectShopper`/`action.type: redirect`, which is a handoff action, not final authorization.
- TEST payment status is checked in Customer Area; live acceptance requires requesting Alma in live Customer Area. This add-on does not describe capture, refund or final asynchronous outcomes.

## Detail locators

- Sessions prerequisites, optional fields and FR/EUR v71 example: pinned raw lines 25–84. Redirect import/init and no-extra-config: lines 86–114.
- Advanced prerequisites, redirect setup and optional installments count: lines 122–169. FR/EUR v72 example and redirect response: lines 170–224. Test/live route: lines 226–230.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-alma]] — method overview and feature matrix

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/web-component/2026-09-15|Alma Web Component guide, captured 2026-09-15]]
