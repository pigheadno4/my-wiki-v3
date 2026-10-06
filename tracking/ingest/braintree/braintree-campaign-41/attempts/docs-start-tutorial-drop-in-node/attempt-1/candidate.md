---
title: "Braintree Drop-in Tutorial (Node.js)"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/tutorial-drop-in-node"
raw_files:
  - "braintree/docs/start/tutorial-drop-in-node-2026-09-16.md"
tags: [braintree, drop-in, node-js, express, javascript, sandbox, payment-method-nonce]
---

## Overview

This [[braintree]] website-tutorial snapshot, collected 2026-09-16, builds a sandbox-only example with a browser Drop-in payment form and a Node.js/Express server. In the browser, Drop-in collects payment information and returns a one-time payment-method nonce; the example posts that nonce to `/checkout`. On the server, the Braintree Node.js library creates a Sandbox gateway and uses the nonce in a `$10.00` transaction-sale request with settlement submission requested. These are tutorial responsibilities and example requests, not proof that a transaction was authorized, submitted, settled, funded or fulfilled.

## Key takeaways

- The page expects current Node.js and npm, a console and text editor, Express generator 4, and a Braintree sandbox account for its test-transaction path. It labels the tutorial for Windows and Mac and uses JavaScript, Node.js and Express.
- The browser setup includes the Drop-in script at `web/dropin/1.44.0`, initializes it with a tokenization key, calls `requestPaymentMethod()`, and posts `payload.nonce` as `paymentMethodNonce` to the merchant's `/checkout` route. The page distinguishes this static, reduced-privilege tokenization key from a server-generated client token that enables all client API capabilities.
- The nonce is a one-time-use reference to the payment information, not the payment itself. The merchant server receives it, supplies the amount, and calls `gateway.transaction.sale`; the tutorial's `submitForSettlement: true` requests funds after a successful authorization. The sample amount and settlement choice are example flow conditions, not general defaults or execution evidence.
- The server example explicitly selects `braintree.Environment.Sandbox` and requires sandbox merchant ID, public key and private key values. The page warns never to share the public or private key. It does not identify an exact Node SDK package version, despite describing the gateway-instance snippet as using the latest Node SDK.
- The test section runs the local app, uses sandbox-only test values and then directs the reader to look for the transaction in the sandbox Control Panel. Instructions and expected UI/results do not show that this collected snapshot was executed successfully.

> [!warning] Source-qualified Drop-in lifecycle notice
> This website snapshot says Drop-in deprecation begins October 1, 2026, with no new features, improvements or bug fixes after that date; it says payment processing remains supported until October 1, 2027, when the SDK becomes unsupported, support ends and processing may be suspended at any time. It directs migration to the Braintree Android, iOS or JavaScript SDK. Treat these dates as this website snapshot's statements, not current status or versioned GitHub SDK evidence, and verify current official lifecycle guidance before migration planning.

## Evidence and version boundaries

This is a website tutorial, not an exact-SHA GitHub implementation source. The `1.44.0` browser Drop-in URL and the unversioned `npm install braintree` instruction establish only what the example shows; they do not prove compatibility with other retained package versions. The Node.js route, JavaScript browser flow and named Android/iOS migration destinations are separate platform routes, so no behavior should be inferred across languages or SDKs.

## Detail locators

- Drop-in deprecation, processing-support and unsupported-status notice plus migration destinations: `# Drop-in Tutorial > **IMPORTANT**`, raw lines 17-22.
- Estimated time, Windows/Mac label, difficulty and JavaScript/Node.js/Express technologies: `# Drop-in Tutorial`, raw lines 26-38.
- Node.js/npm, console/editor, Express generator 4 and sandbox-account prerequisites: `## Before you begin`, raw lines 41-60.
- Express app generation, Handlebars setup, dependency installation and server-side Braintree library purpose/install command: `## 1. Set up a basic app`, raw lines 63-104.
- Browser Drop-in setup checklist, `1.44.0` script and jQuery-not-required note: `## 2. Add the Drop-in UI`, raw lines 106-134.
- Client-token versus tokenization-key capabilities and the tutorial's Control Panel tokenization-key route: `### Get a tokenization key`, raw lines 137-155.
- Browser markup, authorization parameter, `requestPaymentMethod()`, nonce POST, result-display example and nonce definition: `### Add the Drop-in UI markup`, raw lines 158-219.
- Server responsibility, sandbox credentials, key-sharing warning, Sandbox gateway, `$10.00` sale request, nonce input, `submitForSettlement` condition and Node-SDK-version wording: `## 3. Handle checkout`, raw lines 222-317.
- Express `/checkout` route registration: `### Connect the route to app.js`, raw lines 320-335.
- Local start command, sandbox card fixture and Control Panel lookup directions: `## 4. Create a test transaction`, raw lines 337-379.
- Further integration, error handling, payment-method, API, production-contact and fraud-management routes: `## Next steps`, raw lines 382-392.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-drop-in]]
- Broader integration flow: [[source-braintree-get-started]]
- Node transaction request route: [[source-braintree-transaction-sale-node]]

## Related raw API references

- [[raw/braintree/docs/guides/authorization/tokenization-key/javascript/v3-2026-09-16|Braintree tokenization-key guide for JavaScript v3]] - unread navigation-only authorization reference
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Transaction Sale request for Node.js]] - unread navigation-only server request reference
- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree testing reference for Node.js]] - unread navigation-only test-values reference

## Raw Sources

- [[raw/braintree/docs/start/tutorial-drop-in-node-2026-09-16|Braintree Drop-in Tutorial for Node.js]] - fully read pinned website snapshot covering prerequisites, browser Drop-in nonce collection, Node/Express sale handling and sandbox test directions
