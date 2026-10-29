---
title: "Adyen Online banking Poland API-only integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/api-only"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/api-only/2026-09-15.md"
tags: [adyen, online-banking-poland, api-only, redirect, pln, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Poland to an existing Web Advanced-flow API-only integration. It covers bank discovery and checkout consent, method-specific payment fields, redirect return through `/payments/details`, result presentation and live setup. It is a supplement to [[adyen-online-payments]], not a complete base integration or proof that a merchant processed a payment. [[adyen]]

## Key takeaways

- **Prerequisites and form:** The existing API-only integration must handle `action.type: redirect`, and Online banking Poland must be added in Customer Area. The merchant builds the payment form, asks the shopper to accept the linked Online banking Poland regulations and information obligation, and discovers the method with `/paymentMethods` using `countryCode: PL` and `amount.currency: PLN`. The response example has `type: onlineBanking_PL` and an issuer list; sample issuer `141` is illustrative, not a complete bank list or current availability proof. [Raw: lines 23–59, 275–293]
- **Payment field requiredness:** The method-specific `/payments` table marks `shopperEmail` required with a **50-character maximum**, while the `paymentMethod.issuer` row has no required mark and describes the shopper-selected bank ID. Payment examples include `type: onlineBanking_PL`, `issuer: 141`, PLN amount 1000 minor units, a merchant reference, and `returnUrl`; the sample issuer does not turn the unmarked field into an unconditional requirement. The how-it-works prose asks for intended-item information, but the method-specific table and sample requests do not show item fields. Consult the base API contract for a complete request rather than deriving fields from that prose. [Raw: lines 31–35, 297–327]
- **Example completeness:** The `/paymentMethods` curl sample puts `-X POST` on a line without continuation before `-d`, as does the `/payments` curl sample. Several discovery SDK examples call `paymentMethodsRequest` without constructing it; the Node examples use `Config` and `EnvironmentEnum` without showing imports. These are incomplete documentation illustrations, not shell-ready or guaranteed runnable recipes. The displayed versions are for example API libraries, not a stated minimum Checkout API version. [Raw: lines 64–176, 270–276, 306–327, 455–491]
- **Redirect and return:** A `/payments` example returns `resultCode: RedirectShopper` with `action.type: redirect`, GET method and `action.url`. Send the shopper to that returned URL. After website return, URL-decode `redirectResult` and send it inside `details` to `/payments/details`; use its `resultCode` to present the result and `pspReference` as the transaction ID. The mobile-default-browser/SFSafariViewController/Chrome Custom Tabs advice on this Web page is explicitly for mobile integrations, not a Web-only requirement. [Raw: lines 635–706]
- **Finality and live gate:** `Authorised` is described as a successful payment, with funds stated to arrive in **2–3 days**. `Pending` or `Received` means the final result is unknown and may take minutes or hours; wait for an `AUTHORISATION` webhook. `Refused` means bank refusal, with advice to try a different method. A webhook also carries outcome if the shopper does not return to the website/app. Before live acceptance, submit a request for Online banking Poland in live Customer Area. These are captured provider statements, not a guarantee of a particular transfer or merchant enablement. [Raw: lines 708–727]

> [!WARNING] Do not turn examples into required fields or final status
> The table requires `shopperEmail` but leaves `paymentMethod.issuer` unmarked (raw lines 297–302), despite issuer values in samples. `RedirectShopper` is an intermediate action; `Pending`/`Received` are not final results (raw lines 635–720). The how-it-works item statement has no matching method-specific field in this page.

## Detail locators

- Requirements, checkout form, PL/PLN discovery and consent: pinned raw lines 23–59.
- Discovery examples and issuer-list response: pinned raw lines 61–293.
- Payment requiredness and language request examples: pinned raw lines 295–633.
- Redirect, details, result statuses and live setup: pinned raw lines 635–731.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-poland]] — approved overview for P24 partner, PL/PLN bank redirect and method capability context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/api-only/2026-09-15|Online banking Poland API-only guide, captured 2026-09-15]]
