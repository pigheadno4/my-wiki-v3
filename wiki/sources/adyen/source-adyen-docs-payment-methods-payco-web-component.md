---
title: "Adyen PayCo Web Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/web-component"
raw_files:
  - "adyen/docs/payment-methods/payco/web-component/2026-09-15.md"
tags: [adyen, payco, web, component, redirect]
---

## Overview

This 2026-09-15 Adyen page describes PayCo-specific additions to an existing Web Components integration, with separate Sessions and Advanced paths. Both paths use the `Redirect` Component for PayCo and require redirect handling. It is an add-on guide, not a complete payment integration or evidence of a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and adding PayCo in the Customer Area. The page says no additional PayCo parameters are needed in the base `/sessions` request and no additional method configuration is needed.
- Both paths say to include `Redirect` when importing Adyen Web and initialize a `Redirect` Component. Their sample uses `type:kcp_payco` without quotes or a shown definition of `kcp_payco`; preserve this as a source sample, not verified runnable JavaScript or proof of a different method identifier.
- Advanced requires an existing Web Components Advanced integration, redirect handling, and the Customer Area method addition. It says no additional parameters are needed in the base `/payments` request. The page does not state a Checkout API minimum for the Advanced path.
- Under both “Test and go live” headings, the page says there are no specific PayCo test credentials and directs readers to Adyen Support for testing assistance. It does not document a successful test, live activation, or final payment result.

## Detail locators

- Sessions prerequisites: pinned raw lines 25–36; request, import, configuration, and initialization: lines 38–72; testing statement: lines 74–78.
- Advanced prerequisites: lines 80–88; import, sample, and request: lines 90–118; repeated testing statement: lines 120–124.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/web-component/2026-09-15|PayCo Web Component, 2026-09-15]]
