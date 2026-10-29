---
title: "Adyen Online banking Finland Flutter Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/flutter-drop-in/2026-09-15.md"
tags: [adyen, finland-online-banking, flutter, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland** to an existing Flutter Drop-in integration. It distinguishes Sessions and Advanced server-side flows, lists method-specific request fields and redirect handling, and points to Paytrail test data. It supplies no Flutter Drop-in initialization code; the base integration guides remain necessary. **Navigation warning:** the Sessions integration-type row links to an Advanced-flow Flutter Drop-in guide (raw line 33), whereas the Sessions redirect and create-session links point to Sessions-flow guides (lines 35 and 42). Keep the Sessions flow identity and check the link target before using the base guide. See [[adyen]], [[adyen-online-payments]], and the separate FI/EUR method overview [[source-adyen-docs-payment-methods-finland-online-banking]].

## Key takeaways

- **Sessions:** the guide assumes an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and says to **contact Adyen Support** to add Online banking Finland in Customer Area. It marks `shopperEmail` required for `/sessions`. Its TEST v71 sample uses FI/EUR and a custom-scheme `returnUrl`, but `s.hopper@@example.com` is malformed and the curl example lacks a line continuation after `-X POST`; do not copy either as a valid request. The Sessions integration-type link points to an Advanced-flow base guide despite its Sessions label, while the redirect and create-session links point to Sessions-flow guides; use those verified Sessions routes to resolve the mismatch. See raw lines 25–69.
- The Sessions section says no additional Online banking Finland configuration parameters are needed. It does not provide a method-specific Flutter Drop-in constructor or payment-result recipe. See raw lines 342–346.
- **Advanced:** the guide assumes an existing Flutter Drop-in Advanced integration and redirect handling, but here says to **add the method in Customer Area**; it likewise says no additional method configuration parameters. The Checkout API v68 floor appears in the Sessions requirements table only. See raw lines 354–370.
- The Advanced `/payments` table marks `paymentMethod.type: ebanking_FI` and `shopperEmail` required. `paymentMethod.issuer` is relevant and required **for the Issuer redirect flow**; the `returnUrl` row describes a post-payment destination of at most 1024 characters without a required mark. The TEST v72 examples omit `paymentMethod` despite the required type row, repeat the malformed email, and use an HTTPS `returnUrl` in this Flutter guide. The curl example again lacks a continuation after `-X POST`. Treat these as incomplete illustrations, and follow the applicable base flow for redirect return handling. See raw lines 372–405 and 427–667.
- The example `/payments` response has `resultCode: RedirectShopper` and `action.type: redirect`; this is a redirect step, not final payment confirmation. Before live acceptance, the guide directs testing with Paytrail test environment and sample data, and says **testing multiple partial refunds is currently not available**. The separate method overview marks multiple partial refunds available, but its refund note is missing in that captured page; preserve the test limitation without treating the matrix as a successful test. See raw lines 670–690 and [[source-adyen-docs-payment-methods-finland-online-banking]].

## Detail locators

- Sessions prerequisites and conflicting base-guide link targets (33 versus 35 and 42), Support setup, required email and TEST examples: raw lines 25–340.
- Sessions configuration and Paytrail test limitation: raw lines 342–352.
- Advanced prerequisites, Customer Area setup, no additional configuration and request table: raw lines 354–383.
- Advanced TEST examples: raw lines 385–668.
- Redirect response and repeated Paytrail test limitation: raw lines 670–690.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/flutter-drop-in/2026-09-15|Fully read Online banking Finland Flutter Drop-in raw]]
