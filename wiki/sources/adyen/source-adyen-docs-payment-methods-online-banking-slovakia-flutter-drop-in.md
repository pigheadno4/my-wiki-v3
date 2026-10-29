---
title: "Online banking Slovakia Flutter Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/flutter-drop-in/2026-09-15.md"
tags: [adyen, online-banking-slovakia, flutter, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Slovakia to an existing Flutter Drop-in** integration, separating Sessions and Advanced server-side flows. It covers redirect handling, Customer Area setup, the Advanced issuer field, examples and test/live notes. It is a method-specific add-on, not a complete base integration or evidence of current merchant enablement or successful bank payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** requires an existing Flutter Drop-in Sessions integration, Checkout API **v68 or later**, `action.type: redirect` handling, and Online banking Slovakia added in Customer Area. The guide says there are **no additional method-specific `/sessions` or configuration parameters**. Its Sessions integration-type link points to an **Advanced-flow URL**, while the redirect and create-session links point to Sessions; use the heading and matching Sessions base guide. “No additional” does not remove base request requirements (raw lines 25–48).
- **Advanced:** requires an existing Flutter Drop-in Advanced integration, `action.type: redirect` handling and Customer Area setup. No additional method configuration is stated. The `/payments` table marks **`paymentMethod.issuer` required**, identifying the shopper-selected issuing bank. The v72 test example includes `type: onlineBanking_SK`, `issuer: cs`, EUR amount and HTTPS returnUrl; those are sample values, not a separately stated minimum Checkout API version for Advanced or a guaranteed bank choice (raw lines 58–107).
- The guide includes server-side examples in Java, PHP, C#, Node.js, Go, Python and Ruby, with library version labels and test-environment credentials; those versions are **examples**, not declared minimum SDK requirements. The Go snippet labels API Library **v10.4.0** but imports `/v9/` paths, so do not copy it as a verified v10.4.0 build recipe without checking the library version/imports (raw lines 109–396, particularly 263–272).
- For testing, the page advises **real payment details and small amounts**, then checking the **test Customer Area > Payments > Payment list**. This is a test instruction, not a claim of a simulated free transaction. Live acceptance requires adding the method in Customer Area; the source does not prove that any particular merchant has done so (raw lines 50–56, 398–404).
- The separate [[source-adyen-docs-payment-methods-online-banking-slovakia|method overview]] describes the shopper selecting an issuing bank and being redirected to its website or mobile app, and records the **SK/EUR** matrix and refund/capture/recurring indicators. Those are method-level snapshot facts; this Flutter child guide does not define final payment confirmation or merchant-specific availability (overview pinned raw lines 23–31).

## Detail locators

- Scope, Sessions prerequisites, redirect and no-extra statements: raw lines 15–48; mismatched integration-type link at line 33.
- Sessions test/live notes: raw lines 50–56.
- Advanced prerequisites, required issuer and v72 sample: raw lines 58–107.
- Server-side examples and example-only library versions: raw lines 109–396; Go version/import mismatch lines 263–272.
- Advanced test/live notes: raw lines 398–404.
- Method-level bank journey and SK/EUR capability matrix: [[source-adyen-docs-payment-methods-online-banking-slovakia]] and its pinned raw lines 23–31; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/flutter-drop-in/2026-09-15|Online banking Slovakia Flutter Drop-in guide, captured 2026-09-15]]
