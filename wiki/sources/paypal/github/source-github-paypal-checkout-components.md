---
title: "GitHub: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-09-01
date_updated: 2026-09-20
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, github-repository, venmo, pay-later]
---

## Overview

`paypal/paypal-checkout-components` contains the browser runtime that renders PayPal funding buttons and launches PayPal checkout experiences. This cumulative page preserves the package-qualified `@paypal/checkout-components@4.1.47` baseline and extends ingested history through `@paypal/checkout-components@5.0.434` at exact SHA `79fa938be54dd364bb251e5b5caa49c7c809030a`. This release adds checkout-child window-name monitoring. The iframe aria-label addition in `5.0.432` and revert in `5.0.433` remain documented.

Repository: <https://github.com/paypal/paypal-checkout-components>

## Evidence boundary

- The v4 snapshot proves the implementation shipped in `@paypal/checkout-components@4.1.47`, released on 2019-02-07. The v5 snapshot proves the source retained at `5.0.425`, released on 2026-07-22. Neither is a substitute for current integration guidance.
- The repository owns checkout presentation and funding-button behavior. The separately collected `paypal/paypal-js` repository owns loader, wrapper, and TypeScript package evidence.
- Historical funding eligibility does not prove current product availability, merchant enablement, geographic eligibility, or account configuration.
- The exact `5.0.425` patch forwards browser back-forward-cache events via post-robot. Broader capability statements below describe the accumulated v5 source, not features introduced by that one patch.
- The exact `5.0.426` release is a maintenance boundary: it upgrades formatting and repository tooling, raises the declared Node/npm development baseline, and moves the Zoid runtime dependency. Its retained package manifest reports no public export change, and the release does not establish new merchant payment behavior.
- The exact `5.0.427` release adds Austria to existing Germany-specific Pay Later label and label-sizing branches. This proves browser presentation behavior for an eligible `AT` variant, not Austrian product availability, buyer eligibility, or merchant enablement.
- The exact `5.0.428` release changes only the no-funding-source iframe title to address a duplicate PayPal screen-reader announcement. It does not change merchant callbacks, eligibility, or payment execution.
- The exact `5.0.429` release reverts the `5.0.428` title fix completely. Preserve `5.0.428` for version-specific history, but do not describe `PayPal Payment Buttons` as the current title in `5.0.429` or later without new evidence.
- The exact `5.0.430` release changes the package version, cumulative changelog, and generated bundles only. It carries forward `5.0.429` behavior and establishes no new source-level implementation fact.
- The exact `5.0.431` release has the same release-only shape as `5.0.430` and likewise carries forward `5.0.429` behavior.

## Grounding excerpts

> "A set of components allowing easy integration of PayPal Buttons and PayPal Checkout into your site"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md:6-7`

> "Expected a promise for a string order id to be passed to createOrder"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx:150-169`

> "Do not pass both createOrder and createBillingAgreement"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx:193-205`

> "eligibleFunding = eligibleFunding.slice(0, 2)"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js:38-50`

> "Pass bfcache events via post-robot"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/CHANGELOG.md:1-3`

> "flows: [BUTTON_FLOW.PURCHASE, BUTTON_FLOW.VAULT_WITHOUT_PURCHASE]"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/funding/venmo/config.jsx:27`

> "export const SavedPaymentMethods"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/interface/saved-payment-methods.js:9-11`

> "upgrade prettier to v3"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/CHANGELOG.md:1-3`

> `"node": "^22"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/package.json:43-46`

> `"@krakenjs/zoid": "^10.6.0"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/package.json:113-126`

> "Feature/austria geo expansion paylater button"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/CHANGELOG.md:1-3`

> `["DE", "AT"].includes(paylater?.products?.paylater?.variant)`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/funding/paylater/config.jsx:32-36`

> `paylater?.products?.paylater?.variant === "AT"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/ui/buttons/styles/styleUtils.js:228-236`

> `font-family: PayPalOpen-Regular`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/ui/buttons/styles/page.js:5-8`

> "Fix duplicate PayPal screen reader announcement"
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/CHANGELOG.md:1-3`

> `// avoid title colliding when no fundingSource is set`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/src/zoid/buttons/component.jsx:233-237`

> `` `${FUNDING_BRAND_LABEL.PAYPAL} Payment Buttons` ``
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/src/zoid/buttons/component.jsx:234-243`

> `role: "presentation"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/src/zoid/buttons/component.jsx:239-245`

> `Revert "Fix duplicate PayPal screen reader announcement  (#2655)"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/CHANGELOG.md:1-3`

> `` title: `${FUNDING_BRAND_LABEL.PAYPAL}${fundingSource}` ``
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/src/zoid/buttons/component.jsx:233-243`

> `chore(release): 5.0.429`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/CHANGELOG.md:1-3`

> `"version": "5.0.430"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/package.json:1-4`

> `"sha":"1e6da3424d7bb5654bf4a2479702b521dc69aa01"`
>
> `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.430/2026-09-01/manifest.json`

> `chore(release): 5.0.430`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/CHANGELOG.md:1-3`

> `"version": "5.0.431"`
>
> `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/package.json:1-4`

> `"sha":"9bb1162373b4dd96d5a3196dbfab41990f606bb7"`
>
> `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.431/2026-09-01/manifest.json`

## Repository responsibility and architecture

The README identifies this repository as the implementation of PayPal Buttons and PayPal Checkout, powered by Zoid. The v4 runtime defines separate `paypal-buttons` and `paypal-checkout` components. Buttons collect merchant callbacks and funding configuration; Checkout manages the buyer-facing PayPal window.

Checkout prefers a pop-up when the browser supports one and falls back to an iframe. The public interface always exports `Buttons`, but it exposes the lower-level `Checkout`, `PopupOpenError`, and `allowIframe` members only when executing on a PayPal domain.

## Merchant callback contract

The decorated `createOrder` callback receives an `actions.order.create()` helper and must resolve to a nonempty string order ID. The component rejects a missing or non-string result before checkout continues.

`createOrder` and `createBillingAgreement` are mutually exclusive. The billing-agreement path also requires the SDK to be loaded with `vault=true`. These are historical client-runtime guards; merchants still need matching server-side order or billing-agreement handling.

The v4 source contains a USD 0.01 fallback order when no merchant callback is supplied. That fallback is implementation behavior, not a production integration recommendation. Merchant integrations should create and validate their own order on the server.

For approval handling, the historical default captures automatically only when the intent is `CAPTURE` and `commit` is true. Other flows require the merchant's `onApprove` implementation.

## Funding eligibility and presentation

Funding sources pass through several gates before rendering:

1. The server-provided funding record must exist, be eligible, and not set `branded` to false.
2. The source must support the selected button layout and detected platform.
3. A remembered-only source must appear in the buyer's remembered funding list.
4. Eligible sources are ordered by the repository's funding priority.

Horizontal layouts retain at most two eligible funding sources. The historical priority starts with PayPal, Venmo, and Credit, followed by local methods and cards. Most alternative payment methods are constrained to vertical layouts and cannot be the primary button.

## Historical Venmo behavior

In `4.1.47`, the Venmo funding configuration:

- supports only the mobile platform;
- uses the shared PayPal Checkout URL;
- supports blue and silver button colors; and
- sets `allowPrimary: false`, making Venmo a secondary funding choice.

This is a version-qualified implementation fact. It must not be used to deny current desktop Venmo QR support, which was added in later product/runtime generations.

## Version 5 accumulated architecture

The `5.0.425` source retains the public `Buttons` interface and adds distinct interfaces for Marks, Card Fields, Payment Fields, Hosted Buttons, Wallet, and Saved Payment Methods. Lower-level Checkout, Venmo, QR Code, and other Zoid components remain protected exports in the button interface. This demonstrates a broader runtime architecture than v4, but each integration still depends on the matching JS SDK loader and product eligibility.

The v5 Venmo funding configuration allows purchase and vault-without-purchase flows. Vault-without-purchase is gated by the `venmoVaultWithoutPurchase` experiment, and shipping callbacks are rejected when the display-only state is vaultable because native app-switch and QR flows do not support that combination. Mobile Venmo requires both native and popup capabilities; the accumulated changelog records later desktop handling and QR component work that superseded v4's mobile-only presentation.

The separate Venmo Zoid component accepts order creation or vault setup-token creation and distinguishes desktop-web from mobile-web channels. The Saved Payment Methods component carries order callbacks, app-switch preferences, shipping callbacks, funding eligibility, customer identity, and style validation. These are implementation contracts, not proof that a merchant account is enabled for every flow.

The exact `5.0.425` release entry is narrowly about forwarding bfcache events through post-robot. The major-version comparison is used as a full historical baseline because the change from `4.1.47` to `5.0.425` spans the accumulated v5 component system.

## Version 5.0.426 maintenance boundary

The `5.0.426` changelog records a Prettier 3 upgrade. The package moves its declared development engines from Node `^18` and npm `8` to Node `^22` and npm `10`; the retained `.nvmrc` pins `22.22.3`, and the repository's version-check script rejects a runtime that does not satisfy that pin. Prettier moves from `^2.5.1` to `^3.9.6`, with `prettier-plugin-sh` moving from `^0.10.0` to `^0.19.0`.

The runtime dependency on `@krakenjs/zoid` moves from `^10.5.3` to `^10.6.0`. The package comparison reports no public API export change, and the broad source diff is dominated by formatting plus removal of legacy repository tooling and Flow declaration files. Treat the Node/npm declarations as contributor and build-environment compatibility evidence, not as a browser requirement imposed on merchants integrating the hosted JavaScript SDK.

## Version 5.0.427 Austria Pay Later presentation

For an eligible Pay Later product whose backend-provided variant is `AT`, the browser runtime now uses the same German-language `Später Bezahlen` label as the existing `DE` branch. Both responsive-style paths also classify `AT` as a label that needs the smaller sizing treatment, covering normal responsive buttons and the disable-max-height path.

The release also replaces the `PayPal Plain` CSS family with `PayPalOpen-Regular` in the rebranded button label, powered-by treatment, page root, PayPal app-switch overlay, and 3DS overlay. This is a presentation change rather than a public JavaScript API change. The package pins `@percy/playwright` from `^1.0.4` to `1.1.1`, which affects visual-test tooling only.

The added generic Pay Later demo selects buyer country and currency, loads the local SDK, checks Pay Later eligibility, and renders country-specific buttons. It is development evidence for the new `AT` branch; it does not make buyer-country override, funding eligibility, or an Austrian offer merchant-configurable in production.

## Version 5.0.428 screen-reader title fix

The Buttons Zoid iframe keeps a funding-qualified title such as `PayPal-paypal` when `fundingSource` is present. When no funding source is set, `5.0.428` replaces the prior plain `PayPal` title with `PayPal Payment Buttons`. The inline comment says this avoids a title collision, and the changelog identifies the user-facing result as fixing a duplicate PayPal screen-reader announcement.

The iframe's `role="presentation"` remains unchanged. No public API export or dependency range changes are reported, so this is an internal accessibility and presentation fix rather than a merchant integration migration.

## Version 5.0.429 accessibility fix revert

The next release reverts the `5.0.428` title branch in full. `5.0.429` again builds an optional `-<fundingSource>` suffix and assigns `PayPal${fundingSource}` as the iframe title, which means a no-funding-source Buttons iframe returns to plain `PayPal`. The `role="presentation"` attribute remains.

The changelog names the reverted duplicate-announcement fix but gives no reason for the rollback and no replacement mitigation. Therefore, `5.0.428` is a short-lived accessibility behavior, not a safe description of `5.0.429`; affected assistive-technology conditions and the reason for reverting remain unknown.

## Version 5.0.430 release-only boundary

The retained comparison contains only `CHANGELOG.md`, `package.json`, and generated `dist` bundles. The package version advances to `5.0.430`, while the changelog entry is only `chore(release): 5.0.429`. No retained authored source file changed, and no public API export or dependency range change is reported, so `5.0.430` carries forward the `5.0.429` iframe-title behavior without establishing a new merchant or runtime capability.

## Version 5.0.431 release-only boundary

The `5.0.430` to `5.0.431` comparison again contains only `CHANGELOG.md`, `package.json`, and generated `dist` bundles. The changelog records `chore(release): 5.0.430`; no retained authored source file changed, and no public API export or dependency range change is reported. Consequently, `5.0.431` still carries the `5.0.429` iframe-title revert and establishes no new merchant or runtime capability.

## Version 5.0.432 iframe accessibility label

Released September 1, 2026; collected and delta-ingested September 20. The only changed authored implementation adds `"aria-label": "Payment Button"` to the Buttons Zoid iframe attributes:

```js
title: `${FUNDING_BRAND_LABEL.PAYPAL}${fundingSource}`,
"aria-label": "Payment Button",
role: "presentation",
```

The existing optional `-<fundingSource>` suffix remains. Unlike `5.0.428`, this does not change the generic title to `PayPal Payment Buttons`; it supplies a separate, unconditional accessible-label attribute. The changelog describes a fix for duplicate PayPal screen-reader announcements. No browser/screen-reader validation was run, so that outcome is upstream intent rather than independently reproduced proof.

Package JSON changes only its version. There are no detected dependency, public-export, merchant-callback or payment-flow changes. No merchant API migration is documented; this release does not establish additional payment-method availability.

The comparison contains four retained changes: changelog, package manifest, authored component and generated `dist/button.js`; the generated test bundle is policy-excluded. All 210 unchanged retained files were verified byte-equal. The generated bundle changes but contains neither `Payment Button` nor `allowpaymentrequest` in either snapshot; it does not independently substantiate this source-level iframe change. No bundle semantic-equivalence or hosted deployment claim is made.

User-approved focused-reading exception: complete authored component and package reads, new changelog entry review, unchanged-history and bundle mechanical checks. The full upstream changelog, generated bundle and large diff were not all semantically reread. Raw evidence and the 13-path packet remain immutable. Review record: `tracking/github/repos/paypal/paypal-checkout-components/ingest-review-ac14a515.md`.

Grounding under `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/files/`: `CHANGELOG.md:3` says "Fix duplicate PayPal announcement for screen readers via distinct iframe aria-label"; `src/zoid/buttons/component.jsx:244` adds `"aria-label": "Payment Button"`; line 245 retains `role: "presentation"`; `package.json:3` declares `"version": "5.0.432"`. Upstream release notes are unavailable; the retained changelog supplies release intent.

## Version 5.0.433 iframe label revert

Released September 4, 2026; delta-ingested September 20. The only authored implementation change removes `"aria-label": "Payment Button"` from the Buttons iframe. The complete component is byte-identical to `5.0.431`, including the existing funding-qualified title and `role="presentation"`. This is the reversal of the second accessibility attempt, not the older `5.0.428` title fix (already reverted in `5.0.429`).

```diff
 title: `${FUNDING_BRAND_LABEL.PAYPAL}${fundingSource}`,
-"aria-label": "Payment Button",
 role: "presentation",
```

The changelog explicitly records the revert but does not explain the reason or provide a replacement mitigation. Keep `5.0.432` as version-specific history; do not promise its label in `5.0.433`. No merchant API migration, dependency-range change or payment-flow change is established. No browser or screen-reader behavior was independently tested.

Four retained files change: component, package version, new changelog prefix and generated bundle; 210 other retained files are byte-equal. The generated bundle differs but contains no `Payment Button` literal in either version, so the authored component is the authority for this change. The approved item-specific focused-reading exception covered full authored component/package reads and mechanical bundle/history checks; it did not authorize semantic claims about unread generated code. Review: `tracking/github/repos/paypal/paypal-checkout-components/ingest-review-645ba7c9.md`.

Grounding under `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/files/`: `CHANGELOG.md:3` names the revert; `src/zoid/buttons/component.jsx:243-244` retains the title immediately followed by `role: "presentation"`; `package.json:3` declares `5.0.433`. Separate release notes remain unavailable.

## Version 5.0.434 checkout window-name monitoring

Released September 9, 2026; collected and delta-ingested September 20. The checkout component calls `spyOnWindowNameAssignment()` only when `component.isChild()`. The helper captures the existing name and installs a configurable getter/setter on that child window's `name` property. It does not install this hook on arbitrary merchant parent windows or the Buttons iframe.

Names matching `/^__zoid__.+__$/` update the stored value silently. Other assignments log `checkout_window_name_overwritten`, then update the stored value on the normal logging path. Matching the name shape is not authentication of the writer or origin. This helper observes assignments; it does not reject, restore or sanitize unexpected names.

Both the new value embedded in the error message and the original value are truncated to 50 characters. Truncation is not redaction. Installation failures log `checkout_window_name_spy_error`. The surrounding try/catch executes during installation, not future setter invocations: if logging throws inside a later setter call, the following value update may not execute. No cleanup/restoration is implemented in this helper, and no browser/navigation lifecycle testing was performed here.

The package differs only in version; no dependency-range, public export or merchant-callback change is established. The Buttons component is unchanged, retaining the `5.0.433` aria-label revert. No merchant API migration is documented, and source evidence does not prove hosted SDK deployment.

The upstream comparison changes only `CHANGELOG.md`, `package.json` and `src/zoid/checkout/component.jsx`. The packet also reports `dist/button.js` removed from retained evidence; that capsule difference is not an upstream file deletion. All 210 common unchanged retained files are byte-equal. The approved focused-reading exception covered complete authored component/package reads, new changelog entry and mechanical history/generated-evidence verification; no semantic full-read claim for the prior generated bundle. Review: `tracking/github/repos/paypal/paypal-checkout-components/ingest-review-c58f0a0c.md`.

Grounding under `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/files/`: `CHANGELOG.md` records "observe window name"; the checkout component defines `WINDOW_NAME_LOG_TRUNCATION_LENGTH = 50`, the Zoid-name regex, `Object.defineProperty(window, "name", ...)`, and both named log events. Separate upstream release notes are unavailable; motivation beyond the named observation change is undocumented.

## Public and security boundary

The browser-facing `Buttons` component is public on merchant pages. Lower-level checkout controls remain PayPal-domain-only. The iframe helper is therefore not a merchant escape hatch for forcing an unsupported presentation mode.

The exact snapshot also shows that layout, platform, remembered funding, and server eligibility jointly determine button visibility. A configured funding source is not proof that its button will render for a particular buyer.

## Related

- [[changelog-github-paypal-checkout-components]] — package-qualified release ledger
- [[source-github-paypal-js]] — independent loader, wrapper, and TypeScript package history
- [[paypal-checkout]] — cumulative PayPal Checkout concept
- [[paypal-vault]] — setup-token and stored-payment-method concepts
- [[paypal-expanded-checkout]] — Card Fields and 3DS concepts
- [[source-paypal-pay-with-venmo]] — current product documentation for mobile app switch and desktop QR

## Raw sources

- Snapshot (`5.0.434`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/manifest.json`
- Release (`5.0.434`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.434/2026-09-20/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.433--5.0.434/comparison.json`
- Checkout component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/files/src/zoid/checkout/component.jsx`
- Package: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/files/package.json`
- Changelog (new entry reviewed; prior history verified unchanged): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-79fa938/files/CHANGELOG.md`

- Snapshot (`5.0.433`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/manifest.json`
- Release (`5.0.433`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.433/2026-09-20/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.432--5.0.433/comparison.json`
- Authored component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/files/src/zoid/buttons/component.jsx`
- Package: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/files/package.json`
- Changelog (new entry reviewed; prior history verified unchanged): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e5f517b/files/CHANGELOG.md`

- Snapshot (`5.0.432`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/manifest.json`
- Release (`5.0.432`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.432/2026-09-20/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.431--5.0.432/comparison.json`
- Authored iframe attributes: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/files/src/zoid/buttons/component.jsx`
- Package: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/files/package.json`
- Changelog (new release entry reviewed; prior body verified unchanged): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-20-e4c6f20/files/CHANGELOG.md`

- Snapshot manifest (`5.0.431`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/manifest.json`
- Release manifest (`5.0.431`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.431/2026-09-01/manifest.json`
- Patch comparison (`5.0.430` to `5.0.431`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.430--5.0.431/comparison.json`
- `5.0.431` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/package.json`
- `5.0.431` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/CHANGELOG.md`
- Snapshot manifest (`5.0.430`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/manifest.json`
- Release manifest (`5.0.430`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.430/2026-09-01/manifest.json`
- Patch comparison (`5.0.429` to `5.0.430`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.429--5.0.430/comparison.json`
- `5.0.430` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/package.json`
- `5.0.430` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/CHANGELOG.md`
- Snapshot manifest (`5.0.429`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/manifest.json`
- Release manifest (`5.0.429`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.429/2026-09-01/manifest.json`
- Patch comparison (`5.0.428` to `5.0.429`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.428--5.0.429/comparison.json`
- `5.0.429` Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/src/zoid/buttons/component.jsx`
- `5.0.429` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/package.json`
- `5.0.429` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/CHANGELOG.md`
- Snapshot manifest (`5.0.428`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/manifest.json`
- Release manifest (`5.0.428`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.428/2026-09-01/manifest.json`
- Patch comparison (`5.0.427` to `5.0.428`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.427--5.0.428/comparison.json`
- `5.0.428` Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/src/zoid/buttons/component.jsx`
- `5.0.428` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/package.json`
- `5.0.428` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/CHANGELOG.md`
- Snapshot manifest (`5.0.427`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/manifest.json`
- Release manifest (`5.0.427`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.427/2026-09-01/manifest.json`
- Patch comparison (`5.0.426` to `5.0.427`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.426--5.0.427/comparison.json`
- `5.0.427` Pay Later label logic: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/funding/paylater/config.jsx`
- `5.0.427` responsive label sizing: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/ui/buttons/styles/styleUtils.js`
- `5.0.427` generic Pay Later demo: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/demo/dev/button-paylater-generic.htm`
- `5.0.427` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/package.json`
- `5.0.427` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/CHANGELOG.md`
- Snapshot manifest (`5.0.426`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/manifest.json`
- Release manifest (`5.0.426`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.426/2026-09-01/manifest.json`
- Patch comparison (`5.0.425` to `5.0.426`): `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.425--5.0.426/comparison.json`
- `5.0.426` package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/package.json`
- `5.0.426` changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/CHANGELOG.md`
- Snapshot manifest (`5.0.425`): `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json`
- Release manifest (`5.0.425`): `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.425/2026-07-23/manifest.json`
- Major comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/4.1.47--5.0.425/comparison.json`
- Release history: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/CHANGELOG.md`
- v5 public interfaces: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/interface/`
- v5 Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/funding/venmo/config.jsx`
- v5 Venmo component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/zoid/venmo/component.jsx`
- v5 Saved Payment Methods component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/zoid/saved-payment-methods/component.jsx`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json`
- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/4.1.47/2026-07-23/manifest.json`
- README: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx`
- Funding eligibility: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js`
- Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/venmo/config.jsx`
- Public button interface: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/interface/button.js`
