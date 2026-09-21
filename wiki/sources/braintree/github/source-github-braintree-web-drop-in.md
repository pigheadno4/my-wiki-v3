---
title: "GitHub: braintree/braintree-web-drop-in"
type: source
date_ingested: 2026-07-28
date_updated: 2026-09-20
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/manifest.json"
  - "github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json"
tags: [braintree, drop-in, checkout, javascript-sdk, hosted-fields, paypal, venmo, 3d-secure, github-repository]
---

## Overview

`braintree/braintree-web-drop-in` contains Braintree's prebuilt browser checkout UI. The first retained baseline is package-qualified release `braintree-web-drop-in@1.47.0` at exact SHA `ec1c7c533c2e878545f2b25505c56b7e22dc1c17`.

Repository: <https://github.com/braintree/braintree-web-drop-in>

Latest ingested release: `braintree-web-drop-in@1.48.0` (2026-09-10) at `5e6de786a463598b4583a657acbd5cafee72dbf9`. This additive delta retains the `1.47.0` baseline below and changes card-label output handling, not the checkout API or runtime dependency versions.

## Evidence Boundary

- This snapshot proves implementation present in `braintree-web-drop-in@1.47.0`, released on 2026-06-17. It does not prove merchant, buyer, region, browser, or payment-method eligibility.
- Drop-in is an independent package and repository. At this release it depends on `braintree-web@3.123.2`; later findings from the separately collected `braintree-web@3.144.0` source cannot be attributed to this Drop-in baseline.
- The repository announces future deprecation on 2026-09-01 and unsupported status on 2027-09-01. It says processing will be supported for one year after deprecation, while processing on unsupported SDKs may be suspended at any time. At this snapshot date, those milestones are scheduled rather than already effective.
- The capsule contains production source and translations but no tests. Test-only behavior and upstream Braintree Web implementation outside the pinned dependency boundary are not retained here.

> [!warning] Contradiction: lifecycle evidence
> The September milestones above describe the `1.47.0` baseline and remain unchanged in the `1.48.0` README. However, `1.48.0` was released September 10, after the stated September 1 no-updates date. Separately, [[source-braintree-get-started]] gives October 1, 2026 and October 1, 2027 milestones. Preserve these source-specific statements; neither this release nor the conflicting dates establish a revised support commitment.

## Grounding Excerpts

> "Starting September 1, 2026 the Drop-in SDK will move to a [deprecated status](https://developer.paypal.com/braintree/docs/guides/client-sdk/deprecation-policy/javascript/v3/#status-categories) and we will no longer make any updates to this SDK."
>
> `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/README.md:7-8`

> "Please migrate to the Braintree SDK to continue processing and receiving updates."
>
> `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/README.md:12`

> "A pre-made payments UI for accepting cards and alternative payments in the browser built using version 3 of the Braintree JS client SDK."
>
> `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/README.md:14`

> "Requests a payment method object which includes the payment method nonce used by by the Braintree Server SDKs."
>
> `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/dropin.js:789-790`

> "Payment options omitted from this array will not be offered to the customer."
>
> `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/index.js:238`

## Integration Architecture

Drop-in renders into an empty merchant container and creates an opinionated payment UI outside an iframe. Card inputs themselves use Braintree Hosted Fields. Merchants can integrate through `dropin.create()` or a script-tag/form mode that intercepts submission, tokenizes the selected method, writes `payment_method_nonce` to a hidden input, optionally writes fraud `device_data`, and resumes form submission.

The main public operation is `requestPaymentMethod()`, which returns a payment-method payload containing a nonce for a Braintree server SDK. The instance also exposes payment-method requestability events, active-view and card-field events, `getAvailablePaymentOptions()`, `clearSelectedPaymentMethod()`, selected configuration updates, and `teardown()` for single-page applications.

## Payment Methods and Presentation

The default payment-option order is card, PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay. Cards are enabled by default; other methods require merchant configuration and pass their underlying SDK/browser enablement checks. `paymentOptionPriority` both orders methods and removes omitted methods from the UI.

- Card entry is built with Hosted Fields and supports cardholder name, field/style overrides, supported-brand filtering, tokenization, and optional vaulting.
- PayPal and PayPal Credit use Braintree Web's non-v6 PayPal Checkout component for checkout or vault flows.
- Venmo uses the Braintree Web Venmo component and app-switch tokenization.
- Apple Pay and Google Pay adapt their browser wallet sheets into Braintree payment-method nonces.

`getAvailablePaymentOptions()` reports what Drop-in actually presented after configuration and browser checks. Source presence alone must not be used as eligibility evidence.

## Vaulted Methods

A client token generated with a customer ID lets Drop-in fetch and display supported vaulted methods and vault newly added methods according to configuration. Cards and PayPal can be shown from the vault; Apple Pay, Google Pay, and Venmo vaulted records are always hidden from new authorization selection. The UI includes edit and deletion handling through Braintree Vault Manager for non-guest checkout.

Clearing a selected method removes unvaulted selections and returns the buyer to the payment options without deleting vaulted records. Updating PayPal configuration after authorization also removes unvaulted PayPal selections so stale authorization data is not reused.

## 3D Secure and Fraud Data

When configured, `requestPaymentMethod()` can run 3D Secure after card or eligible Google Pay tokenization, replace the nonce with the verified nonce, and return liability-shift fields and 3DS information. The merchant still decides whether to proceed when liability does not shift.

Data Collector can append device data to the returned payload. Its presence does not itself establish that advanced fraud tooling or Kount is enabled for the merchant.

## Localization and Customization

The public create API lists locale modules from Arabic through Chinese variants and supports partial custom translations. Merchant strings pass through HTML escaping before being inserted into localized templates. Drop-in supports Hosted Fields overrides and stylesheet replacement, but its design is intentionally opinionated; the README directs fully customized integrations to the modular Braintree Web SDK.

## `1.47.0` Release Findings

The release adds conventional-commit tooling, expands `sanitizeHtml()` to escape ampersands and both quote types in addition to angle brackets, replaces an error-message `innerHTML` assignment with `textContent`, and adds the deprecation schedule.

The sanitization changes reduce unsafe interpolation paths but are not described as a security advisory. No payment method, public checkout API, or pinned `braintree-web@3.123.2` dependency change is documented for this release.

## `1.48.0` Delta from `1.47.0`

Four of 86 retained files changed: `CHANGELOG.md`, `README.md`, `package.json`, and `src/views/payment-method-view.js`; 82 are hash-identical. The upstream comparison also includes lockfile and unit-test changes excluded from the retained capsule. Their changed hunks were reviewed, not executed.

### Card Label Output

The card branch previously inserted `details.lastFour` directly into the localized `endingIn` string. It now uses:

```javascript
Number(this.paymentMethod.details.lastFour)
  .toString()
  .slice(0, 4)
  .padStart(4, '0')
```

This is first-four-character truncation after number conversion, not extraction of the final four digits from a card number. Examples of the expression's behavior:

| Input | Display substitution |
| --- | --- |
| `"0012"` | `"0012"` |
| `"0000"` | `"0000"` |
| `"123456"` | `"1234"` |
| `"abc"` or `"<alert>test!</alert>"` | `"0NaN"` |
| `"12.3"` | `"12.3"` |

The expression does not reject invalid input or guarantee four decimal digits. The view still writes `this.element.innerHTML = html`; PayPal email and Venmo username continue through the existing HTML-escaping helper, while Apple Pay and Google Pay label branches are unchanged. Treat this as a bounded card-display hardening change, not a complete `textContent` migration, payment-data validator, or demonstrated security advisory.

### Release and Integration Boundary

- Release notes say "sanitize `lastFour` card digits"; the changelog describes tightening its `innerHtml` usage. The same changelog retrospectively qualifies the `1.47.0` textContent entry with "(where possible)". The original `1.47.0` raw snapshot remains preserved.
- README CDN examples move from `1.47.0` to `1.48.0`; the lifecycle notice does not change. See the contradiction above.
- `package.json` changes only the package version. Runtime pins remain `braintree-web@3.123.2` and `@braintree/uuid@1.0.1`, among the unchanged dependencies. Independently ingested newer SDK behavior must not be projected onto Drop-in.
- No public integration API, tokenization, nonce, wallet, or eligibility change is identified in this comparison. Existing integrations updating to `1.48.0` should check selected-card labels, including leading-zero values; malformed-value examples above are diagnostic behavior, not supported payment inputs.
- Changed upstream test hunks cover overlong strings, markup-like input, and zero padding. No upstream test suite, browser checkout, or payment transaction was run during this ingest.

## Related

- [[changelog-github-braintree-web-drop-in]] - package-qualified release ledger
- [[braintree]] - company and knowledge-status page
- [[braintree-web-drop-in]] - product concept and migration boundary
- [[braintree-web-sdk]] - modular SDK used underneath Drop-in

## Raw Sources

- Current snapshot: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/manifest.json`
- `1.48.0` release: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.48.0/2026-09-20/manifest.json`
- `1.48.0` notes: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.48.0/2026-09-20/release-notes.md`
- Comparison: `tracking/github/repos/braintree/braintree-web-drop-in/comparisons/braintree-web-drop-in/1.47.0--1.48.0/comparison.json`
- Comparison overview: `tracking/github/repos/braintree/braintree-web-drop-in/comparisons/braintree-web-drop-in/1.47.0--1.48.0/comparison.md`
- Upstream diff: `tracking/github/repos/braintree/braintree-web-drop-in/comparisons/braintree-web-drop-in/1.47.0--1.48.0/diff.patch`
- Current payment-method view: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/src/views/payment-method-view.js`
- Prior payment-method view: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/views/payment-method-view.js`
- Current HTML template: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/src/html/payment-method.html`
- Current sanitizer: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/src/lib/sanitize-html.js`
- Current README: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/README.md`
- Current package: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/package.json`
- Current changelog: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-09-20-5e6de78/files/CHANGELOG.md`

- Snapshot manifest: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/manifest.json`
- Release manifest: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.47.0/2026-07-28/manifest.json`
- Release notes: `raw/github/braintree/braintree-web-drop-in/releases/braintree-web-drop-in/1.47.0/2026-07-28/release-notes.md`
- README: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/README.md`
- Package manifest: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/package.json`
- Public create API: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/index.js`
- Drop-in instance: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/dropin.js`
- State and vault model: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/dropin-model.js`
- Payment sheet views: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/views/payment-sheet-views/`
- Sanitizer: `raw/github/braintree/braintree-web-drop-in/snapshots/2026-07-28-ec1c7c5/files/src/lib/sanitize-html.js`
