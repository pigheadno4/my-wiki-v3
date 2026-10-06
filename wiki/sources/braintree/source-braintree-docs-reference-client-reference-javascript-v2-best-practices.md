---
title: "Braintree JavaScript v2 Best Practices and Troubleshooting"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/best-practices"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/best-practices-2026-09-16.md"
tags: [braintree, javascript, client-sdk, troubleshooting, content-security-policy]
---

## Overview

This collected [[braintree]] website snapshot is a JavaScript v2 client-reference page for Braintree.js setup, readiness and teardown, custom PayPal UI initiation, Content Security Policy configuration, and form-submit handling. It is historical website guidance for [[braintree-web-sdk]], not proof of current SDK or browser support, current hosted behavior, merchant eligibility, successful payment execution, or the behavior of any separately retained GitHub version.

## Key takeaways

- The page recommends putting the Braintree.js script near the end of the HTML body. Separately, it says `braintree.setup()` must run only after the form container exists; running it earlier may prevent the UI from appearing. The first statement is advice, while the setup ordering is stated as a requirement.
- The v2 `onReady` callback signals that the chosen client integration is fully loaded and interactive. Hiding Braintree-specific DOM until that callback is presented only as an option dependent on the checkout experience.
- In single-page, modal, and other state-sensitive flows, the integration object returned through `onReady` exposes `teardown`. The page says teardown removes integration-created DOM nodes, handlers, popups, and/or iframes, and its callback signals when it is safe to continue. It can be invoked only once for each `braintree.setup()` call; concurrent and later repeated calls produce distinct errors.
- To open the PayPal authorization flow from a merchant-supplied button, the page requires a headless PayPal integration together with `paypal.initAuthFlow()` from `onReady`. Its example passes `CLIENT_TOKEN_FROM_SERVER` to the client-side `braintree.setup()` call and leaves cross-browser click-handler compatibility to the merchant; the example does not establish server behavior or payment completion.
- The CSP section recommends considering a Content Security Policy rather than declaring CSP universally mandatory. It provides separate Sandbox and Production directive tables for AJAX with CORS (`enableCORS: true`) and for non-CORS use. A further JavaScript-v2 snapshot instruction says 3D Secure users need `frame-src` and `form-action` set to `*`; preserve that broad wildcard statement as historical page-specific guidance, not a current general security recommendation or guarantee.
- Braintree.js attaches form-submit handlers by default. The page shows native `HTMLFormElement.prototype.submit.call(form)` as a bypass and dispatching a custom `submit` event for a form without a button; these are client-side action examples, not evidence that tokenization, authorization, or settlement succeeded.

## Detail locators

- **Script tag placement and initialization** — advisory script placement and the required container-before-`braintree.setup()` ordering.
- **Optimizing for tablets and phones** — advisory viewport metadata for injected Drop-in or PayPal interfaces and a device-review recommendation.
- **Leverage onReady** — readiness semantics and optional DOM-hiding guidance.
- **Teardown** — integration-object acquisition, cleanup effects, callback sequencing, one-call-per-setup constraint, and the two repeated-call error cases.
- **Custom UI** — headless PayPal prerequisite, `paypal.initAuthFlow()` action, client-token placeholder, one-time-use amount/currency example settings, shipping-address example, and merchant-owned click compatibility.
- **Using Braintree.js with a Content Security Policy** — advisory CSP framing; conditional CORS and non-CORS tables split by Sandbox and Production; exact resource origins; and the page's broad 3D Secure `frame-src`/`form-action` wildcard instruction. Treat the origin lists and wildcard as captured configuration, not current allowlist or security-policy evidence.
- **Bypass submit handlers** — default submit interception, native-submit bypass, and custom-event example.

## Related

- [[braintree-web-sdk]] — provider concept for the browser SDK and separately qualified current/exact-version evidence.
- [[source-braintree-client-sdk-migration-javascript-v3]] — historical v2-to-v3 migration route; consult it rather than treating this v2 practices page as current support evidence.
- [[source-braintree-client-sdk-deprecation-policy-javascript-v3]] — separately collected JavaScript v3 lifecycle policy snapshot, which does not assign current status to this v2 page.

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/best-practices-2026-09-16|Braintree JavaScript v2 Best Practices and Troubleshooting snapshot]]
