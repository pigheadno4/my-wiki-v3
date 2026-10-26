---
title: "Trustly Web Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/web-component"
raw_files:
  - "adyen/docs/payment-methods/trustly/web-component/2026-09-15.md"
tags: [adyen, trustly, web, components, online-banking, redirect]
---

## Overview

This Trustly Web Component page (last modified 2019-09-06; captured 2026-09-15) adds Trustly to an **existing** Web Components integration. It covers Sessions/Advanced prerequisites, v6 versus v5.x.x-or-earlier mounting, ordinary request fields, and TEST/LIVE setup. It does not describe the shopper redirect, `/payments/details`, authorization webhook, or actual receipt of bank funds. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For **Sessions** or **Advanced**, the corresponding Web Components integration must already be built, and Trustly must be added in Customer Area before beginning. The page states no additional Trustly fields for the ordinary `/sessions` or `/payments` endpoint path; it points to general optional fields without defining a method-specific request payload. See raw lines 21–37 and 47–52.
- On **Web Components v6**, import `AdyenCheckout` and `Trustly` from `@adyen/adyen-web`, then mount `new Trustly(checkout)` to the checkout DOM element. For **v5.x.x or earlier**, use `checkout.create('trustly').mount(...)`. The v6 import-guide hyperlink is labeled as a Component guide but contains `integration=Drop-in`; follow the page's explicit Component snippets while treating that link as a navigation mismatch. A stray standalone `**` appears between v6 and v5 headings. See raw lines 39–45 and 54–84.
- TEST directs readers to a Trustly test environment, gives a `YYMMDD-XXXX`-format example for Login ID/Personal number, and says to check test-payment status in Customer Area. These are test-entry instructions, not evidence of a successful payment. Live acceptance requires submitting a Trustly request in **live** Customer Area; this snapshot does not establish approval or current eligibility. See raw lines 86–92.
- **Funding warning from the separately approved Trustly overview:** even a successful `AUTHORISATION` webhook means verification passed and transfer was initiated, not that Adyen received funds; cancellation or later bank processing can prevent funds, with a nondefensible chargeback path. This Component page gives no contrary funding guarantee. See [[source-adyen-docs-payment-methods-trustly]] (its raw lines 38–53); this page's raw lines 86–92 only describe test-status lookup and the live request gate. Do not infer settled funds from mounting, redirect completion, or an authorization result.

## Detail locators

- Existing Sessions/Advanced integration and Customer Area prerequisites: raw lines 21–37.
- v6 import and versioned mounting; Drop-in-link mismatch: raw lines 39–45 and 54–84.
- No additional Trustly request fields and endpoint references: raw lines 47–52.
- TEST and live Customer Area routes: raw lines 86–92.
- Cross-page funding/outcome qualification: [[source-adyen-docs-payment-methods-trustly]], overview raw lines 38–53.

## Related

- [[adyen-online-payments]] — main Web Components route.
- [[source-adyen-docs-payment-methods-trustly]] — bank-redirect overview and authorized-but-unfunded warning.
- [[source-adyen-docs-payment-methods-trustly-api-only]] — separate API-only flow.

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/web-component/2026-09-15|Trustly Web Component, captured 2026-09-15]]
