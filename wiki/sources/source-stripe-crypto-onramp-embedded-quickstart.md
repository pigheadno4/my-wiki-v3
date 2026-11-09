---
title: "Stripe — Crypto Onramp: Embedded Quickstart"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/embedded-quickstart"
raw_files:
  - "stripe-crypto-onramp-embedded-quickstart-2026-11-07.md"
  - "stripe-crypto-onramp-embedded-quickstart-2026.md"
tags: [stripe, crypto, onramp, embedded, react, node, fiat-to-crypto, session-api]
---

## Overview

Stripe's [[stripe]] embedded fiat-to-crypto onramp quickstart describes a test-key integration that creates an `OnrampSession` on a server, returns its client secret, and mounts a client-side iframe. The May 11, 2026 capture gives a Node/Express plus React example; the November 7 capture adds alternative server-language panels and a direct browser-script path. These are examples for [[stripe-crypto-onramp]], not proof of account access, an executed purchase, payment finality, or crypto delivery.

## Key takeaways

- Add the hosting domains to the onramp domain allowlist before using the page. The guide frames the example with test keys and sandbox values. The server uses a secret key to create an `OnrampSession` and returns `clientSecret`; the browser uses a publishable key and that client secret to mount the widget. Stripe describes the session object as tracking the onramp lifecycle and order details to avoid charging twice, but the captured examples do not demonstrate a completed charge.
- In the May Node/Express example, the browser sends `transaction_details` with `destination_currency`, `destination_exchange_amount`, and `destination_network`; the server separately gets `customer_ip_address` from the request socket and passes those values in its session-creation example. The shown `usdc`, `13.37`, and `ethereum` values are sandbox example inputs. Neither dated capture supplies a complete request schema proving these sample fields universally required.
- The May Node example extends `Stripe.StripeResource` to call `crypto/onramp_sessions`. The November capture retains this example and adds Ruby, Python, PHP, Go, .NET, and Java server snippets. These panels and setup commands are alternatives, not one runnable program. The flattened November text even places two endpoint strings in single displayed fetch calls; select a coherent variant before adapting sample code.
- The React variant installs `@stripe/crypto` and `@stripe/stripe-js`, calls `loadStripeOnramp` with a publishable key outside render, and mounts `createSession({ clientSecret, appearance })` through a custom `CryptoElements`/`OnrampElement` wrapper. The example listens to `onramp_ui_loaded` and `onramp_session_updated`; a displayed `session.status` message is a UI update, not evidence of settled payment or delivered crypto. The page says the wrapper components are to be released as an ES module in the future.
- A **separate direct browser-script variant** loads Stripe.js and crypto-js scripts from `js.stripe.com` and `crypto-js.stripe.com`. The November guide says those scripts must load directly from Stripe domains and not be bundled or self-hosted. This restriction is scoped to the script variant; it does not contradict the documented React package installation.
- The page still calls the onramp API **limited beta**. Its general note says official libraries lack built-in endpoint support and demonstrates custom extensions, yet the same November capture shows a Java `client.v1().crypto().onrampSessions().create(params)` call and a .NET `OnrampSessionService` example. The capture does not establish which SDK versions implement those examples or this merchant's access.

> [!warning] Contradiction
> The November 7 guide's blanket statement that official libraries lack built-in onramp endpoint support conflicts with its Java and .NET service examples. Retain the May Node custom-extension example as dated code; do not infer a universal library-support status from this page alone.

## Detail locators

- Domain allowlist, sample server fields and client secret: [[raw/stripe-crypto-onramp-embedded-quickstart-2026-11-07|November 7 quickstart]], lines 9–36; the original Node/Express sequence is in [[raw/stripe-crypto-onramp-embedded-quickstart-2026|May 11 quickstart]], lines 4–62.
- November server alternatives and React/browser variants: November lines 37–338; per-language setup commands and package panels, lines 339–845.
- Limited-beta text, script-domain requirement, iframe, callbacks, and sandbox framing: November lines 848–902 and 916–922. May React wrappers, callbacks, and sample values: May lines 64–96, 98–233, 267–296.

## Related

- [[stripe-crypto-onramp]] — onramp integration context.
- [[source-stripe-crypto-onramp-embedded]] — embedded onramp overview.

## Raw Sources

- [[raw/stripe-crypto-onramp-embedded-quickstart-2026-11-07|Stripe embedded onramp quickstart, 2026-11-07]]
- [[raw/stripe-crypto-onramp-embedded-quickstart-2026|Stripe embedded onramp quickstart, 2026-05-11]]
