---
title: "GitHub: paypal/paypal-messaging-components"
type: source
date_ingested: 2026-08-29
date_updated: 2026-10-04
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/manifest.json"
  - "github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/manifest.json"
  - "github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/manifest.json"
  - "github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/manifest.json"
  - "github/paypal/paypal-messaging-components/snapshots/2026-08-28-2bdaf94/manifest.json"
tags: [paypal, pay-later, paypal-credit, messaging, javascript, github-repository]
---

## Overview

`paypal/paypal-messaging-components` implements PayPal Credit and Pay Later promotional messaging for merchant websites. This cumulative page begins with package-qualified baseline `@paypal/messaging-components@1.95.1` at exact SHA `2bdaf940cdb0dcd29a8a3bc992eea975798d6d00`.

The latest ingested release here is `@paypal/messaging-components@1.98.0`, released September 28, 2026, at `a639ec71494d3278684f5896017a426ed1fbfcd1`. Its additive ingest records Canadian bilingual long-term presentment, FR/AT/DE credit warnings and layouts, currency formatting and a modal Tab guard. The `1.95.1` baseline, `1.96.0` accessibility/content delta and `1.97.0` page-type/disclosure history below remain preserved.

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

## `1.96.0` Accessibility And Content Delta

Compared with `1.95.1`, the retained capsule adds 41 files and modifies 25, with no removals and 642 unchanged files. Ingest used the user's one-time focused-reading exception: changed implementation/content and affected prior versions read completely; unchanged changelog history and manifest inventories checked mechanically. This is not a new full-repository baseline.

### Calculator And Financing Plans

- `Calculator.jsx` distinguishes input errors from the generic request error. For a non-generic error after an initial amount or input use, it sets `aria-invalid="true"`, gives the error `id="purchase-amount-error"`, and links the input with `aria-describedby`. The visual warning uses the separate entered-amount condition; a generic request error no longer activates that input warning treatment.
- An empty US input receives the formatted placeholder as its accessible name. The existing required attribute and polite error region remain.
- A `role="status"` region reports `loadingLabel` while loading, defaulting to `Loading financing options`; the results region adds `aria-busy`. Sixteen existing modal JSONs add localized `loadingLabel` values without changing their other content.
- Both accordion and card loading shimmers add `aria-hidden="true"`. `OfferCard.jsx` changes the financing-plan title from `<strong>` to `<h4>`.

Exact new calculator attributes, shown as an excerpt rather than a standalone merchant component:

```jsx
aria-label={country === 'US' && displayValue === '' ? formattedInputPlaceholder : undefined}
aria-invalid={hasInputError ? 'true' : undefined}
aria-describedby={hasInputError ? 'purchase-amount-error' : undefined}
```

The legacy message renderer now pairs its logo with `<span className="sr-only">{brandName}</span>`. It chooses `PayPal Credit` for `PAYPAL_CREDIT_NO_INTEREST`, otherwise `PayPal`. The visual logo wrapper itself remains hidden from assistive technology. This describes that renderer branch, not every custom layout or the separate v2 renderer.

These changes establish authored semantics, not verified screen-reader or visual behavior. Upstream modal SCSS and tests are excluded from the capsule; no reduced-motion or visual-parity conclusion is made.

### Apple Wallet-Named Modal Content

Two new US PL2GO JSONs supply long- and short-term content:

- `apple_wallet_long_term.json`: Pay Monthly copy describing application, a single-use virtual card and monthly installments. It is byte-identical to this release's existing `pl2go_long_term.json`.
- `apple_wallet_short_term.json`: Pay in 4 copy describing application, a single-use virtual card and payments today and at two-, four- and six-week intervals.

These are promotional/modal content records. They do not show merchant Apple Pay integration methods, wallet provisioning, transaction execution, enrollment or current availability. Country, rate and eligibility wording in raw content must not be promoted to current commercial guidance without the relevant official authority.

### V2 Development Evidence And Layout

The new `content/messages/v2/` directory contains 38 JSON fixtures plus a README for AU, DE, ES, FR, GB, IT and US message cases. The README calls them `representative CPS v2 message content fixtures`; the content covers text, images, variable placeholders and links. This does not prove production support for every fixture's product or legal copy.

Demo documentation adds `features=useRenderV2Message` to exercise the v2 renderer on the standalone page. Package scripts add `dev:v2-comparison` and v2-specific test commands, but their supporting demo/script/test files are outside this capsule, so this ingest does not claim a runnable or tested local demo. V2 flex styling changes `.pp-message.pp-flex` height from `100%` to `100vh`, referencing the rendering document's viewport rather than guaranteeing merchant-page sizing.

No merchant public-API migration is identified in the retained delta. Runtime dependencies are unchanged. The development dependency `jest-image-snapshot` is pinned from `^6.5.2` to `6.5.2`; an empty generated dependency-change list must not be read as proof that every dependency field is unchanged.

## `1.97.0` Page Type, Disclosures And Layout

Compared with `1.96.0`, the retained snapshot has 2 added and 55 modified files, no removals and 653 unchanged files. The user approved **full additive ingest** because of the incompatible page-type enum change below, overriding the generated delta recommendation. The separate, one-time focused-reading approval covers complete changed implementation/content and affected prior versions, with unchanged history and inventories checked mechanically. Two approved exact-SHA supplemental files complete the disclosure component evidence; neither the original snapshot nor future collection policy was changed.

### Page-Type Migration

The message validator replaces `view-edit-fi` with `view-edit-funding-instrument`. At `1.97.0`, the old value logs `invalid_option_value` and returns `undefined`; there is no old-to-new alias and no throw in this validation branch. The message component uses that validator for its `page_type` query parameter.

```js
// Version-qualified options excerpt, not a complete checkout integration.
const previousOptions = { pageType: "view-edit-fi" }; // 1.96.0
const updatedOptions = { pageType: "view-edit-funding-instrument" }; // 1.97.0
```

Only consumers using that old enum value need this rename. This does not imply that all message rendering or checkout fails. The packet's empty public-API-change list missed this runtime enum change; the manual finding takes precedence for the approved ingest mode.

### Inline Disclosure And Native Callback

Both US Apple Wallet-named PL2GO JSONs now set `meta.useInlineDisclosure` to the **string** `"true"`. The short-term JSON also changes the New Mexico disclosure link from `/us/webapps/mpp/campaigns/newmexicodisclosure` to `/us/digital-wallet/new-mexico-disclosure` on `www.paypal.com`.

For array-based link content, `InlineLinks.jsx` checks whether **any supplied view** has that string flag, not only the active view. If so, it prevents navigation and opens the disclosure state; otherwise it retains the normal browser link action. Its non-array HTML-content branch is unchanged. Every array-link callback now includes the original URL alongside the link name and source.

```jsx
// Exact excerpts from the retained implementation and approved supplement.
if (shouldUseInlineDisclosure(views)) {
    event.preventDefault();
    openDisclosure(linkUrl);
}
// BodyContent renders this when disclosureUrl is set:
<Disclosure url={disclosureUrl} onBack={closeDisclosure} />
// Disclosure renders the external document:
<iframe className="disclosure-view__frame" src={url} title={backButtonLabel} />
```

`DisclosureViewProvider` stores the URL; Back clears it. Its formatter replaces the origin of HTTPS URLs whose hostname is exactly `paypal.com` or `www.paypal.com` with `getPayPalDomain()`, preserving path, query and fragment. Other URLs and parsing failures are returned unchanged. This formatter is **not a URL-rejection allowlist**. The domain helper is environment-aware and can delegate to the SDK.

The supplemental `Disclosure.jsx` renders a dialog wrapper, Back button and iframe; `_disclosure.scss` defines a fixed, inset-zero overlay with z-index 1002 and a flex-filling frame. The default button label and iframe title are `Back`. The component itself contains no explicit iframe sandbox, load-error handling or focus-management code. The existing link aria-label fallback still says `opens new tab`, even when the click is intercepted for inline display. These are source-level limitations to verify, not a browser or assistive-technology test result. The stylesheet aggregation file remains uncollected, so this evidence does not prove build wiring or deployed styling.

In the non-embedded native-webview setup, `onClick` now forwards `url` to the existing iOS/Android callback handler. A native host can consume it, but this repository change does not implement or prove that host's half-sheet presentation. None of these changes establishes merchant Apple Pay checkout, wallet provisioning or eligibility.

### Spain And Italy Warning Layouts

Seven ES and seven IT message JSONs add a `large` disclaimer. The respective wording is:

- ES: “Atención, un crédito puede tener un coste y debe ser devuelto.”
- IT: “Attenzione! Prendere in prestito denaro comporta dei costi.”

Locale mutations include that disclaimer in text/flex presentation and change wrapping and logo breakpoints. The new `disclaimerWrap()` helper sets normal wrapping and an inline-block minimum width for the large disclaimer below a configured breakpoint. Text CSS renders it with normal weight, no underline and normal whitespace.

Flex changes are substantial, not copy-only: for example, the base `1x1` headline rules change from 10vw to 5vw in ES and from 10vw to 6vw in IT, with further width-dependent rules. The IT `20x1` rule at widths up to 350px uses 5px for headline and warning text; ES `6x1` includes a `margin-right: none` declaration. Small-size readability and layout therefore remain explicit visual-QA questions, not assumed improvements. The release labels this work CCDII/CCD2, but this ingest makes no legal-compliance conclusion or qualification-rule claim.

### V2 Default And Other Changes

V2 `styles.js` changes its default font size from 14 to 12, and `validOptions.js` makes 12 the first/default text size. `validateStyle.js` uses that first value for missing or invalid input. Explicit valid sizes 10 through 16 remain accepted, including 14; this is not a forced change to every customized message or the legacy renderer.

The package manifest changes only the version. Demo account edits format commented examples; they do not enable new accounts. No upstream build, browser, native-host, visual or production test was run for this ingest.

## `1.98.0` Canadian Presentment, Credit Warnings And Modal Navigation

Compared with `1.97.0`, the capsule adds 16 files and modifies 133, with no removals and 577 unchanged files. Full additive mode follows the reviewed capsule-budget change from 720 to 760 files; that does not itself indicate a breaking payment API. Under the item-specific focused-reading exception, all changed current implementation/content and affected prior files were read completely, along with the new changelog section and full comparison; unchanged inventories/history were checked mechanically. The snapshot retains 726 files, not the entire upstream repository.

### Canadian Bilingual Long-Term Presentment

The CA dispatcher adds `PLLT_MQ_GZ` and `PLLT_NQ_GZ`, selecting new qualified/non-qualified long-term mutation modules instead of the prior generic fallback. Four new English/French message JSONs supply long-term headlines, while the modules handle text/flex layouts, bilingual breaks, logo variants and ratio-specific punctuation. This chooses the supplied message's presentation; it does not decide buyer qualification.

New English/French long-term modal and product-list JSONs expand the content. The product list describes Pay in 4 and monthly financing with merchant/consumer eligibility qualifications. Long-term checkout (`xo`) offer JSONs are also new. Existing Canadian short-term and French checkout content is revised, so this is not the first Canadian localization or first French Canadian support.

Calculator formatting changes English `$<value>` to `$<value> CAD` and French `<value> $ CAD` to `<value> $ CA`. Language now passes through `TermsTable` to `OfferCard`; for CA interest/total amounts, English appends `CAD` and French replaces a trailing `$` with `$ CA`. Other countries and falsey values keep the prior branch. This is scoped display formatting, not a general currency parser.

Ordinary long-term threshold errors now give a purchase-range instruction for both below/above-range cases; checkout variants retain separate lower/upper instructions. French Canadian labels change to `Payer par mois` and `TAP`. Revised nonzero-rate disclaimer copy adds Quebec/Newfoundland-specific wording. These are authored `1.98.0` content findings, not verified current financing terms, legal guidance or product availability. Qualifying-offer filtering and term sorting remain unchanged.

### FR, AT And DE Credit Warnings

Five FR message JSONs and sixteen each for AT and DE add a `large` credit-warning disclaimer. FR warns about repayment/borrowing cost; AT/DE use borrowing-cost warnings for generic/interest-bearing content and late-payment-cost warnings for zero-interest/Pay in 30 content. Mutations put `large` before the default link and, for cross-border variants, the existing extra account disclaimer. That account disclaimer remains.

New AT/DE text CSS applies normal weight, no underline and normal wrapping; it explicitly styles `extra` because inserting `large` moves it out of the first-of-type position. FR uses the new `disclaimerSpanWrap()` to allow the first multi-span warning to wrap separately from the following link. The existing `disclaimerWrap()` changes from fixed-minimum-width warning treatment to restoring inline messaging and span wrapping below the breakpoint. Its older behavior remains recorded in `1.97.0` above.

Flex changes affect headlines, logos, warning sizes and placement across square, tall and wide banners. For example, AT/DE GPL square warnings use a base 5.5vw rule, narrow 150px rules use a 6.5px disclaimer, and 20x1 rules up to 650px use 1vw warning text. Internal `6x1` CSS is a mobile base, not a new public ratio. Narrow-container readability needs runtime QA; release CCD2 wording does not establish legal compliance.

FR long-term, short-term and product-list views conditionally render supplied `creditWarning`; short-term English/French content supplies it. FR modal disclosures remove explicit French-account-required wording and revise links/provider text while retaining resident/approval qualifications. Product-list copy adds creditworthiness and market-dependent cross-border wording. Copy changes alone establish neither relaxed account requirements nor cross-border entitlement.

### Modal Navigation And Country Class

The forward-Tab wrap branch now requires `!e.shiftKey`; previously it could run when Shift+Tab was pressed from the last tabbable element. This is a source-level correction, not complete keyboard/screen-reader accessibility proof. `BodyContent` appends a lowercased country class to its content container. The excluded modal stylesheet aggregation prevents a claim about a specific resulting modal color, especially because release history includes a removal and revert.

Version-qualified implementation excerpts, not merchant integration code:

```jsx
// 1.98.0 forward-wrap condition; Shift+Tab no longer enters this branch.
} else if (!e.shiftKey && document.activeElement === tabArray[tabArray.length - 1]) {
```

```js
// 1.98.0 CA dispatch; the prior version used the generic fallback for these IDs.
case 'PLLT_MQ_GZ':
    return longTermQ[type];
case 'PLLT_NQ_GZ':
    return longTermNQ[type];
```

### Grounding And Scope

Five exact excerpts from the `2026-10-04-a639ec7/files/` snapshot:

- `src/components/modal/v2/lib/utils.js:101`: `} else if (!e.shiftKey && document.activeElement === tabArray[tabArray.length - 1]) {`
- `src/components/modal/v2/parts/BodyContent.jsx:93`: `const countryClassName = country?.toLowerCase();`
- `content/modals/FR/short_term_en.json:49`: `"creditWarning": "Caution! A credit costs money and must be repaid.",`
- `src/server/locale/CA/mutations/index.js:11-12`: `case 'PLLT_MQ_GZ':` followed by `return longTermQ[type];`
- `src/server/message/mediaQueries.js:222`: ``return `.message__disclaimer > span.multi:first-of-type { white-space: normal; }`;``

No detected public API or dependency change: `package.json` changes only its version; Puppeteer is already `^25.3.0` in the prior snapshot. Commented demo accounts do not enable production accounts. This is not `paypal-js`, its React wrapper or checkout orchestration, and the release does not establish a new saved-payment/token contract. No build, browser, visual, screen-reader or payment test was run.

## Version-Qualified Use

Use this source and [[changelog-github-paypal-messaging-components]] for the `1.95.1` baseline and exact `1.96.0`, `1.97.0` and `1.98.0` changes. Earlier behavior remains version-qualified rather than overwritten by the newer release. Use official Pay Later documentation for current eligibility and product availability, [[source-github-paypal-js]] for loader and React contracts, and [[source-github-paypal-sdk-release]] for the version assembled into a particular combined SDK release.

## Related

- Company: [[paypal]]
- Concept: [[paypal-pay-later]]
- Release history: [[changelog-github-paypal-messaging-components]]
- JS loader and React wrappers: [[source-github-paypal-js]]
- Combined SDK bill of materials: [[source-github-paypal-sdk-release]]

## Raw Sources

- `1.98.0` snapshot: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/manifest.json`
- Release record: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.98.0/2026-10-04/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.98.0/2026-10-04/release-notes.md`
- Comparison: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.97.0--1.98.0/comparison.json`
- Comparison detail and patch: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.97.0--1.98.0/comparison.md`, `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.97.0--1.98.0/diff.patch`
- Tab guard: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/components/modal/v2/lib/utils.js`
- Country class: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/components/modal/v2/parts/BodyContent.jsx`
- Calculator: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/components/modal/v2/parts/Calculator.jsx`
- Currency selection: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/components/modal/v2/lib/locale.js`
- Result formatting: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/components/modal/v2/parts/OfferCard.jsx`
- CA dispatcher: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/server/locale/CA/mutations/index.js`
- CA long-term content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/content/modals/CA/long_term.json`
- CA product-list content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/content/modals/CA/product_list_fr.json`
- FR warning/disclosure content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/content/modals/FR/short_term_en.json`
- AT message warning: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/content/messages/AT/generic.json`
- DE text disclaimer: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/server/locale/DE/GPL/styles/text/disclaimer.css`
- FR layout: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/server/locale/FR/styles/flex/ratio--20x1.css`
- Shared wrapping: `raw/github/paypal/paypal-messaging-components/snapshots/2026-10-04-a639ec7/files/src/server/message/mediaQueries.js`
- Review: `tracking/github/repos/paypal/paypal-messaging-components/ingest-review-93c29d33.md`
- `1.97.0` snapshot: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/manifest.json`
- Release record: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.97.0/2026-09-20/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.97.0/2026-09-20/release-notes.md`
- Comparison: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.96.0--1.97.0/comparison.json`
- Validation: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/library/zoid/message/validation.js`
- Message component: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/library/zoid/message/component.js`
- Inline links: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/components/modal/v2/parts/InlineLinks.jsx`
- Disclosure state: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/components/modal/v2/lib/providers/disclosureView.js`
- Modal body: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/components/modal/v2/parts/BodyContent.jsx`
- Native bridge: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/components/modal/v2/lib/zoid-polyfill.js`
- Supplement manifest: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/manifest.json`
- Disclosure component: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/files/src/components/modal/v2/parts/Disclosure.jsx`
- Disclosure stylesheet: `raw/github/paypal/paypal-messaging-components/supplements/2026-09-20-39769bc-70608700/files/src/components/modal/v2/styles/components/_disclosure.scss`
- Apple short-term content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/content/modals/US/PL2GO/apple_wallet_short_term.json`
- ES wording: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/content/messages/ES/short_term_q.json`
- IT wording: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/content/messages/IT/short_term_q.json`
- ES wrapping: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/server/message/mediaQueries.js`
- IT narrow layout: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/server/locale/IT/styles/flex/ratio--20x1.css`
- ES narrow layout: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/server/locale/ES/styles/flex/ratio--6x1.css`
- V2 style defaults: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/server/v2/validOptions.js`
- V2 validation: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-39769bc/files/src/server/v2/validateStyle.js`
- `1.96.0` snapshot: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/manifest.json`
- Release record: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.96.0/2026-09-20/manifest.json`
- Release notes: `raw/github/paypal/paypal-messaging-components/releases/messaging-components/1.96.0/2026-09-20/release-notes.md`
- Comparison: `tracking/github/repos/paypal/paypal-messaging-components/comparisons/messaging-components/1.95.1--1.96.0/comparison.md`
- Calculator: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/components/modal/v2/parts/Calculator.jsx`
- Shimmer: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/components/modal/v2/parts/LoadingShimmer.jsx`
- Offer card: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/components/modal/v2/parts/OfferCard.jsx`
- Message renderer: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/server/message/index.jsx`
- Logo: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/server/message/parts/Logo.jsx`
- Apple long-term content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/content/modals/US/PL2GO/apple_wallet_long_term.json`
- Apple short-term content: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/content/modals/US/PL2GO/apple_wallet_short_term.json`
- Fixture boundary: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/content/messages/v2/README.md`
- V2 styles: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/src/server/v2/flexStyles.js`
- Demo guidance: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/docs/message-demo-pages.md`
- Package: `raw/github/paypal/paypal-messaging-components/snapshots/2026-09-20-a682a8d/files/package.json`
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
