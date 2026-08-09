---
title: "GitHub: paypal/paypal-sdk-logos"
type: source
date_ingested: 2026-04-16
date_updated: 2026-08-09
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/manifest.json"
  - "github-paypal-sdk-logos.md"
tags: [paypal, logos, svg, payment-methods, branding, javascript, github-repository]
---

## Overview

`paypal/paypal-sdk-logos` publishes `@paypal/sdk-logos`, a JSX/SVG rendering library for PayPal, Venmo, card, wallet, and local-payment-method artwork used by PayPal SDKs. The current retained source baseline is package `2.3.7` at exact commit `4c39c1ec50b15dde3af99b524fb24ec8aa9fa11b`.

This cumulative page preserves the earlier `2.3.3` collection, including its 117 generated CDN SVGs, and adds the complete policy-selected public source for `2.3.7`. Repository: <https://github.com/paypal/paypal-sdk-logos>

## Evidence boundary

- A logo or renderer in this package proves that an SDK asset exists. It does not prove merchant eligibility, regional availability, payment-method enablement, buyer presentation, or transaction support.
- The Apache-2.0 license does not grant permission to use PayPal's or another owner's trade names, trademarks, service marks, or product names. Branding requirements remain separate from source-code licensing.
- The `2.3.7` capsule retains source definitions and release documentation but excludes generated `cdn/` history. Exact generated `2.3.7` SVG questions require a future supplement or an upstream clone pinned to the retained SHA.
- The legacy `2.3.3` raw evidence retains the exact generated CDN directory, so it remains authoritative for those 117 historical files.

## Grounding excerpts

> "Logos for PayPal SDKs."
>
> `raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/README.md:16`

> "return `${CDN_BASE_URL}/${svgFilename}`;"
>
> `raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/src/lib/util.js:62`

> "if (logoColorMap && (!logoColor || !logoColorMap[logoColor])) { logoColor = LOGO_COLOR.DEFAULT; }"
>
> `raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/src/lib/util.js:56-58`

> "When changes are merged into the `main` branch, the GitHub Action will automatically create a new patch version and publish it to npm under the `latest` dist-tag."
>
> `raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/CONTRIBUTING.md:120-121`

> "This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor"
>
> `raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/files/LICENSE:138-140`

## Rendering API

The root package exports constants, utility functions, and every logo family. Each family generally provides an inline SVG component, an external-image component, and a default alias to the inline component. The README demonstrates JSX-Pragmatic rendering to HTML, React rendering, and vanilla JavaScript rendering.

The shared `SVG` component has two output paths:

- With `cdnUrl`, it returns an `<img>` whose `src` is that URL.
- Without `cdnUrl`, it renders the JSX SVG to an HTML string, converts the string to a base64 data URI, and returns an `<img>`.

Generic logo images receive an empty `alt` value and CSS classes derived from the logo name and color. Card-brand images receive a capitalized brand name as `alt`. Individual PayPal, PayPal Credit, Pay Later, and Apple Pay implementations also define explicit accessible labels where required.

## CDN and color behavior

Package `2.3.7` hard-codes:

```text
https://www.paypalobjects.com/js-sdk-logos/2.3.7
```

`getSVGFilename()` constructs either `<name>.svg` or `<name>-<color>.svg`. `getLogoCDNUrl()` appends that filename to the versioned CDN base. When a requested color is absent from a family's color map, both color selection and CDN URL generation fall back to `default`; an unavailable default raises an error.

The public color constants are `BLUE`, `BLACK`, `WHITE`, `MONOCHROME`, and `DEFAULT`. Actual support varies by family, so callers must not assume every logo has every color.

## Current logo surface

The `2.3.7` source index exports 30 top-level families:

- PayPal, Venmo, Apple Pay, PayPal Credit, card, and bank assets;
- Bancontact, BLIK, Boleto, EPS, Giropay, iDEAL, Itau, Mercado Pago, Multibanco, MyBank, OXXO, P24, Paidy, PayU, Satispay, SEPA, Sofort, Trustly, and WeChat Pay; and
- rebrand families for PayPal, Venmo, PayPal Credit, Pay Later, Bancontact, and the generic card glyph.

The card family exports Amex, CB Nationale, CUP, Diners, Discover, Elo, Hiper, JCB, Maestro, Mastercard, Visa, and generic original/rebrand card glyphs.

Rebrand-specific badge constants in `2.3.7` cover the PayPal rebrand badge, Credit rebrand badge, and Credit rebrand PP badge. The source also adds `PAYPAL_CREDIT_REBRAND` to the logo constants.

PayPal Credit selects a German-specific logo/CDN identity when the locale language is German. This is asset-selection behavior, not evidence of country eligibility. The old Venmo default artwork uses `#3D93CE`; the rebrand artwork uses `#008CFF` and has no black color mapping, so a black request follows the default fallback.

## Version-qualified history

### `2.3.3` retained baseline

The original collection at commit `bb24f9b` retained the README, constants, package and logo indexes, plus 117 generated SVGs under `raw/github-paypal-sdk-logos/cdn/2.3.3/`. Its CDN base is `https://www.paypalobjects.com/js-sdk-logos/2.3.3/`.

The source already contained the principal PayPal, Venmo, Credit, Pay Later, Bancontact, and card rebrand families. Therefore, later 2.3.x releases must not be described as initially adding those payment methods or rebrand families.

### `2.3.4` through `2.3.7`

The upstream changelog describes `2.3.4` as generated-CDN output. Releases `2.3.5`, `2.3.6`, and `2.3.7` refine whitespace or geometry and regenerate CDN packages: general logo whitespace in `2.3.5`, Venmo whitespace in `2.3.6`, and the PP monogram in `2.3.7`.

The current source also exposes badge constants/components absent from the retained `2.3.3` constants file. These are rendering-surface changes, not checkout eligibility changes.

## Implementation notes

- `@paypal/sdk-constants` supplies card identifiers; JSX-Pragmatic and Belter supply rendering and SVG-to-base64 utilities.
- The npm package publishes `dist/` and `src/`; generated `cdn/` files are not listed in the npm `files` array.
- `VenmoRebrandLogoInlineSVG` passes the original `LOGO.VENMO` identity to `getLogoColors`, while its external form uses `LOGO.VENMO_REBRAND`. The helper uses that identity only in an error message, so the retained code does not show a rendering difference, but the inconsistency is relevant during source-level debugging.
- Publishing uses `standard-version`; merging to `main` triggers a patch npm release. CDN generation and deployment are separate steps, including internal staging, SDK-team approval, deployment, and verification.

## Related

- Company: [[paypal]]
- Payment-method context: [[paypal-apm]]
- Checkout runtime and eligibility: [[paypal-checkout]]
- Repository history: [[changelog-github-paypal-sdk-logos]]

## Raw Sources

- [2.3.7 exact-SHA snapshot](../../../../raw/github/paypal/paypal-sdk-logos/snapshots/2026-08-09-4c39c1e/manifest.json) - 105 policy-selected source and documentation files at `4c39c1e`.
- [Legacy 2.3.3 collection](../../../../raw/github-paypal-sdk-logos.md) - retained source indexes and 117 generated CDN SVG files.
