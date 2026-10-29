---
title: "Adyen PaySafeCard API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/api-only"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/api-only/2026-09-15.md"
tags: [adyen, paysafecard, api-only, redirect, online-payments]
---

## Overview

This captured Adyen guide adds PaySafeCard to an existing Web Advanced-flow API-only integration. It covers method discovery, a required shopper reference, a redirect action and return through `/payments/details`, and test/live setup. It is an add-on to [[adyen-online-payments]], not proof that a particular merchant is enabled or has processed a payment. [[adyen]]

## Key takeaways

- **Prerequisites and discovery:** The existing API-only integration must handle `action.type: redirect`, and PaySafeCard must be added in Customer Area. The payment form need not collect shopper information. The `/paymentMethods` table lists country codes and currency codes separately; the NL/EUR request and `paysafecard` response are examples, not a guarantee that every listed country/currency combination or merchant is eligible. [Raw: lines 23–51, 57–72, 329–340]
- **Captured country-code token conflict:** This API-only child lists `AE`, `GB`, `GIB` and `SRB` among `/paymentMethods` `countryCode` values (child raw line 50), whereas the separately approved [[source-adyen-docs-payment-methods-paysafecard]] overview labels the corresponding places `UAE`, `UK`, `GI` and `RS` in its country-code table (overview raw lines 51, 76, 83–84). The two captured pages disagree on the literal tokens. Neither list alone resolves which values the active Checkout API and merchant account accept; verify the current API contract and account setup before sending a country code. This qualification is separate from the child table's independently listed currencies and the NL/EUR example.
- **Payment request scope:** The method-specific `/payments` table marks `shopperReference` required as the merchant's unique shopper reference. The flow prose also says to include information about the intended items, but the method-specific table and payment examples do not show item fields. The examples omit a `paymentMethod` object even though discovery returns type `paysafecard`; several SDK snippets refer to an unconstructed `paymentRequest`. Treat them as incomplete illustrations and use the base integration/API contract for a complete payment request. The curl examples also put `-X POST` on a line without continuation before `-d`. [Raw: lines 31–36, 342–370, 387–390, 408–413, 434–468, 487–491, 562–565]
- **Redirect and return:** A sample `/payments` response has `resultCode: RedirectShopper` and `action.type: redirect`, an intermediate action rather than payment success. Send the shopper to `action.url`. After the shopper returns to the website, URL-decode `redirectResult` and post it in `details` to `/payments/details`; use that response's `resultCode` for presentation and `pspReference` as the transaction identifier. The page recommends a device default browser for mobile integrations, with SFSafariViewController or Chrome Custom Tabs rather than WebView for app-hosted GET redirects. That is mobile advice on this Web API-only page, not an additional Web requirement. [Raw: lines 568–623]
- **Test versus live:** The captured test section provides a 16-digit code for testing and says to inspect test payments in Customer Area. Before live acceptance, contact Adyen Support to add PaySafeCard to the live Customer Area. The sample `Authorised` details result is documentation, not evidence of an executed transaction or guaranteed settlement. [Raw: lines 616–633]

> [!WARNING] Incomplete payment examples
> The page's how-it-works step calls for intended-item information, while its additional-parameter table only marks `shopperReference` and its payment request examples omit item fields and `paymentMethod`. Several language examples do not construct `paymentRequest`. Do not copy the snippets as a complete API-only payment request. [Raw: lines 35, 342–370, 387–390, 408–413, 434–468, 487–491, 562–565]

> [!warning] Contradiction — overview flow and country-code labels
> The [[source-adyen-docs-payment-methods-paysafecard|method overview]] labels the flow **Direct** and lists country-code values **UAE, UK, GI, RS** (overview raw lines 25–27, 51, 76, 83–84), while this API-only guide requires a **redirect** action and lists **AE, GB, GIB, SRB** (child raw lines 25–28, 50, 570–585). Retain both captured statements; do not infer accepted request codes or remove redirect handling from the overview label. The reciprocal overview warning links here.

## Detail locators

- Requirements, method form and country/currency discovery table: pinned raw lines 15–51; discovery examples and type: lines 53–340.
- Required shopper reference and incomplete payment request examples: pinned raw lines 342–566.
- Redirect response, mobile advice, return and details result: pinned raw lines 568–623.
- Test code, test payment check and live Support gate: pinned raw lines 625–637.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-paysafecard]] — approved method overview with a separate country-code table; its captured tokens conflict with this API-only child.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/api-only/2026-09-15|PaySafeCard API-only guide, captured 2026-09-15]]
