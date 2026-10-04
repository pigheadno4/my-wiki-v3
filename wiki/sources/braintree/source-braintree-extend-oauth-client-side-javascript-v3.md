---
title: "Braintree Extend OAuth Client-side Connect Flow for JavaScript v3"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/extend/oauth/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, javascript-v3, connect, client-side]
---

## Overview

This collected [[braintree]] page is a JavaScript v3 client-side Connect guide under the site's `extend/oauth` route. It has a platform page give `BraintreeOAuthConnect` a Connect URL generated on the platform server so the page can display **Connect with Braintree** and send a merchant to Braintree's consent UI for the requested OAuth scopes. The snapshot labels OAuth closed beta in production and open beta in sandbox. [[braintree-extend-oauth]] owns this Extend OAuth route; it remains distinct from the separate [[braintree-auth]] product despite overlapping connected-merchant OAuth terminology and the page's Braintree Auth contact link.

## Key takeaways

- The browser-side library can display the provided **Connect with Braintree** button, while generation of the Connect URL remains a server responsibility. The page describes that URL as pointing to a Braintree website with a consent UI appropriate for the requested OAuth scopes.
- The page says not to initialize `braintree-oauth-connect.js` or display the Connect button again when the merchant returns to the page after authorizing the application. This is a return-page presentation rule, not proof that consent completed, credentials were issued, an API call succeeded or a payment was accepted.
- `connectUrl` and `container` are required parameters. The optional `onError` callback receives an error object with a `message` property, and the optional `environment` accepts `production` (the documented default) or `sandbox`. These are fields in the collected JavaScript v3 snapshot, not evidence of current production access, environment isolation or parity with other client variants.
- The page supplies both a hosted library inclusion and a manual button-image example. Those examples establish presentation options only; they do not move server-owned URL generation or OAuth credential work into the browser.

> [!warning] Flow and product boundary
> This raw page does not document Finish Later handling, authorization-code exchange, access-token creation, state validation or callback security. Do not import those behaviors from the separate Braintree Auth JavaScript guide or infer them from the button example. Follow the dedicated Extend OAuth server-side sources for those stages and preserve the merchant-approved scope boundary.

> [!warning] Snapshot-qualified availability
> Production closed beta and sandbox open beta are statements from the page collected on 2026-09-16. They do not prove current availability, platform or merchant eligibility, successful OAuth authorization, usable credentials or payment execution.

## Detail locators

- Production closed-beta and sandbox open-beta availability: `# Client-side Connect Flow > AVAILABILITY`, raw lines 17-18.
- Merchant authorization transition and Connect-button task: introduction below availability, raw lines 20-28.
- Hosted library inclusion and manual button-image alternatives: `## Display the button`, raw lines 33-48.
- Return-page rule not to initialize the library or show the button again after authorization: note below `## Display the button`, raw lines 50-51.
- Browser use of a server-generated Connect URL and `BraintreeOAuthConnect` example: `## Specify parameters`, raw lines 54-68.
- Required `connectUrl` and `container`, optional `onError`, and optional `environment` with documented values/default: parameter table, raw lines 69-74.
- Consent-UI and requested-scope purpose of the server-generated Connect URL: parameter table, raw line 71.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Product boundary: [[braintree-auth]] - separate connected-merchant OAuth route whose JavaScript Finish Later behavior is not documented by this Extend page.

## Related raw API references

The following are unread navigation targets named by this page; they are not evidence for claims above.

- [[raw/braintree/docs/guides/extend/oauth/overview-2026-09-16|Braintree Extend OAuth overview (collected 2026-09-16)]]
- [[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16|Braintree Extend OAuth Connect URLs for Node.js (collected 2026-09-16)]]

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/client-side/javascript/v3-2026-09-16|Braintree Extend OAuth client-side Connect flow for JavaScript v3 (collected 2026-09-16)]]
