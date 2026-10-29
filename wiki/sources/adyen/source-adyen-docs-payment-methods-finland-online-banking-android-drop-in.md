---
title: "Adyen Online banking Finland Android Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/android-drop-in/2026-09-15.md"
tags: [adyen, finland-online-banking, android, drop-in, paytrail, redirect, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Finland to an existing Android Drop-in integration. It separates Sessions and Advanced server-side flows, their method-specific email/type/issuer fields, a redirect action example, and Paytrail test guidance. It is a supplement to [[adyen-online-payments]], not a complete base integration or evidence of an enabled account or successful payment. [[adyen]]

## Key takeaways

- **Sessions flow:** Start with an existing Android Sessions-flow Drop-in integration using Checkout API **v68 or later** and add Online banking Finland in Customer Area. The method-specific `/sessions` table requires `shopperEmail`. Its FI/EUR amount, app-scheme `returnUrl`, and `s.hopper@@example.com` address are sample values; the double-`@` address is malformed and should not be copied as a real shopper email. The page says no extra method-specific Drop-in configuration is needed. [Raw: lines 25–65, 338–343]
- **Advanced flow:** Start with an existing Android Advanced-flow Drop-in integration that handles `action.type: redirect` and has the method added in Customer Area. The `/payments` table requires `paymentMethod.type: ebanking_FI` and `shopperEmail`. `paymentMethod.issuer` is required only for the **Issuer redirect flow**, not every redirect flow; the optional-row description says it is the selected bank ID. `returnUrl` is unmarked in this method-specific table, with a 1024-character maximum stated. No Advanced API minimum is given here. [Raw: lines 355–381]
- **Incomplete Advanced examples:** Every shown Advanced `/payments` sample omits the `paymentMethod` object despite the table's required `paymentMethod.type`, and carries the malformed double-`@` email placeholder. The curl examples also put `-X POST` on a line without continuation before `-d`; Node snippets refer to `Config`/`EnvironmentEnum` without imports. Use the required-field table and base integration contract rather than copying these examples as complete runnable requests. [Raw: lines 50–66, 386–666]
- **Redirect versus final result:** The Advanced example returns `resultCode: RedirectShopper` with a GET `action.type: redirect` URL. This is an intermediate action. This child guide does not give the Android return/details/webhook outcome sequence, so do not treat the example response as authorized payment. The approved [[source-adyen-docs-payment-methods-finland-online-banking]] overview separately describes the bank-authentication journey and contains a bank-selection-location tension; that overview should be cited for those method-level claims. [Raw: lines 668–682]
- **Test scope and refund distinction:** Before accepting live payments, the page instructs testing with Paytrail-provided test environment and sample data and says **testing multiple partial refunds is currently not available**. The separately approved overview's capability matrix checks multiple partial refunds but has an unresolved “See note” pointer; the child test limitation is not itself proof that live multiple partial refunds are impossible or available for a particular merchant. The page contains no actual test result. [Child raw: lines 346–352, 684–688; overview raw: lines 34–36]

> [!WARNING] Required type absent from every Advanced request sample
> The method-specific table requires `paymentMethod.type: ebanking_FI` (raw line 378), but the curl and language requests omit `paymentMethod` (raw lines 386–666). The sample email has two `@` signs. Do not use these snippets as complete payment requests or infer that Drop-in removes the required method type.

## Detail locators

- Sessions prerequisites, required email, examples and no-extra-config: pinned raw lines 25–343.
- Paytrail testing instruction and multiple-partial-refund test limitation: pinned raw lines 345–352 and 684–688.
- Advanced prerequisites and field requiredness: pinned raw lines 355–381.
- Incomplete request examples and redirect response: pinned raw lines 383–682.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-finland-online-banking]] — approved Paytrail/FI/EUR overview and its separate bank-selection/refund-note qualifications.

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/android-drop-in/2026-09-15|Online banking Finland Android Drop-in guide, captured 2026-09-15]]
