---
title: "GitHub: paypal/paypal-messaging-components"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json"
tags: [paypal, pay-later, paypal-credit, messaging, javascript, github-repository]
---

## Overview

`paypal/paypal-messaging-components` implements PayPal Credit and Pay Later promotional messaging for merchant websites. This cumulative page begins with package-qualified baseline `@paypal/messaging-components@1.95.1` at exact SHA `2bdaf940cdb0dcd29a8a3bc992eea975798d6d00`.

Repository: <https://github.com/paypal/paypal-messaging-components>

## Evidence Boundary

- This repository establishes browser message rendering, modal behavior, merchant-facing options, server rendering, and package changes. It does not establish live merchant enablement, buyer qualification, regional rollout, or transaction eligibility.
- Messages promote financing products and open PayPal-hosted explanatory or application content. Checkout payment execution remains owned by separate checkout integrations.
- The initial capsule retains all 667 policy-selected source files. It excludes tests, so implementation branches are source evidence rather than proof of runtime test results.
- `@paypal/sdk-release@5.0.569` independently pins Messaging Components `1.94.0`. The direct `1.95.1` release here is newer; the two records describe different package/version boundaries and are not contradictory.
- Venmo logo support in the v2 renderer means that PayPal-supplied message content can render the brand asset. It does not establish Venmo checkout, Venmo Pay Later, or merchant eligibility.

## Grounding Excerpts

> "A messaging component allowing easy integration of PayPal Credit Messages onto your site."
>
> `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/README.md:7`

> "PayPal messaging library for integrating PayPal Credit messaging on merchant websites"
>
> `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/package.json:4`

> `render: (selector = '[data-pp-message]') => {`
>
> `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/library/controllers/message/interface.js:42-44`

> `offers.filter(offer => offer.meta.qualifying === 'true')`
>
> `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/components/modal/v2/parts/TermsTable.jsx:58-68`

> "guard against null target window in modal sendEvent"
>
> `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/CHANGELOG.md:9`

## Merchant Integration Surface

The package publishes `dist/messaging.js` as its main entry and retains `src/library`, `src/utils`, the distribution bundle, `__sdk__.js`, and `globals.js` as package files. It supports SDK, standalone, standalone-modal, and server-rendering build targets.

The public browser entry is `Messages(options).render(selector)`. The selector defaults to `[data-pp-message]`; a selector can also be an element or element array. Configuration is merged in this order:

1. global SDK or standalone configuration;
2. JavaScript options passed to `Messages()`; and
3. inline `data-pp-*` attributes on the message container.

Inline placement is normalized to `pageType`. Material options include account/client identity, merchant and customer IDs, amount, currency, page type, style, preferred offer, buyer country, language/locale, channel, contextual components, CSP nonce, feature flags, and render/click/apply callbacks.

The library auto-renders new `[data-pp-message]` elements inserted into the DOM. It also observes later `data-pp-*` changes and updates existing Zoid component props rather than always creating another iframe. Multiple containers are rendered serially enough to prioritize the first, with idle-callback or timed scheduling for later placements.

## Message And Modal Lifecycle

Each message is a Zoid component restricted to a PayPal domain and rendered in an iframe. The component fetches PayPal message markup, applies responsive text or flex presentation, reports render and visibility telemetry, and hides content that cannot meet the returned minimum dimensions.

When an account is available, the message receives a modal controller. A click can open PayPal-hosted offer detail, calculator, prequalification, or product-list content. The modal overlays the top-level merchant page, manages focus and viewport scrolling, supports Escape and close actions, and uses a popup when the component is already inside another iframe. Native-webview callback handlers and a controlled PayPal-domain popup path are also present.

The modal supports short-term installments, long-term monthly offers, Pay in 1, no-interest PayPal Credit, and product-list views. Content and country determine which view appears; source-level view presence is not proof that a given buyer or merchant receives the offer.

## Rendering And Style Contracts

Message presentation supports text, flex, and legacy custom layouts. Text options include logo type/position, color, size, alignment, and custom fonts. Flex options include color themes and `1x1`, `1x4`, `8x1`, and `20x1` ratios with responsive parent sizing.

The newer v2 server renderer maps legacy logo inputs to wordmark, monogram, inline, or text presentation and renders PayPal, PayPal Credit, and Venmo assets locally. Unknown image blocks fall back to the PayPal-supplied source URL. It supports both text and flex content blocks but explicitly defers several v6-parity behaviors, including text-variable placeholders and some card-offer logo overrides.

## `1.95.1` Offer Processing

The `1.95.1` release is a focused modal-correctness update:

- filter offers to `meta.qualifying === 'true'` before display and sorting;
- convert `total_payments` to a number and avoid ordering malformed values;
- use explicit ascending term order for US, ES, IT, and CA;
- use explicit descending term order for AT, DE, and FR;
- fall back to the default APR disclaimer when a term-specific disclaimer is absent; and
- guard modal event delivery when the target window is null.

These fixes affect how already-returned financing offers are presented. They do not change the upstream qualification decision or prove new product availability.

## Version-Qualified Use

Use this source when a question concerns `@paypal/messaging-components@1.95.1` implementation behavior, message rendering, modal lifecycle, or the exact offer-processing fixes. Use official Pay Later documentation for current eligibility and product availability, [[source-github-paypal-js]] for loader and React contracts, and [[source-github-paypal-sdk-release]] for the version assembled into a particular combined SDK release.

## Related

- Company: [[paypal]]
- Concept: [[paypal-pay-later]]
- Release history: [[changelog-github-paypal-messaging-components]]
- JS loader and React wrappers: [[source-github-paypal-js]]
- Combined SDK bill of materials: [[source-github-paypal-sdk-release]]

## Raw Sources

- Snapshot manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json`
- Release manifest: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.95.1/2026-08-28/release-notes.md`
- README: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/README.md`
- Package manifest: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/package.json`
- Changelog: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/CHANGELOG.md`
- Message interface: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/library/controllers/message/interface.js`
- Modal component: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/library/zoid/modal/component.js`
- Offer terms table: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/components/modal/v2/parts/TermsTable.jsx`
- V2 message renderer: `raw/github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/files/src/server/v2/message.jsx`
