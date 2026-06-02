---
title: "Stripe Checkout: Customize Appearance"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-appearance-2025.md"
tags: [stripe, checkout, branding, appearance, fonts, connect, customization]
---

## Summary

Detailed guide for customizing Stripe Checkout branding — colors, fonts, shapes, logo/icon handling, Connect brand overrides, and font compatibility by locale.

## Key Takeaways

- **`branding_settings` API param**: overrides Dashboard defaults per Checkout Session
- **Invoices always use Dashboard branding** — not per-session `branding_settings`
- **Hosted vs Embedded differences**: hosted supports `logo` + `icon`; embedded supports `display_name`, `font_family`, `border_style`, `background_color`, `button_color` only (no logo)
- **Font fallback**: unsupported locale → system font; Serif font unsupported → Serif-based system font

## `branding_settings` Fields

| Field | Hosted | Embedded | Notes |
| --- | --- | --- | --- |
| `icon` | ✓ | — | Used as favicon; if only icon passed → also displayed |
| `logo` | ✓ | — | Displayed on page; if only logo → Dashboard icon used as favicon |
| `display_name` | ✓ | ✓ | Brand name shown on checkout page |
| `font_family` | ✓ | ✓ | 24 options; locale-dependent fallback |
| `border_style` | ✓ | ✓ | e.g. `rectangular` |
| `background_color` | ✓ | ✓ | Hex color |
| `button_color` | ✓ | ✓ | Hex color |

## Logo vs Icon Logic (Hosted only)

| Passed | Displayed | Favicon |
| --- | --- | --- |
| Both `logo` + `icon` | Logo | Icon |
| `logo` only | Logo | Dashboard icon |
| `icon` only | Icon | Icon |

## Connect Branding

- Default: uses brand settings of the connected account (destination charges with `on_behalf_of` or direct charges)
- Override: set `branding_settings` when creating the Checkout Session
- Connected accounts without full Dashboard access (Express/Custom): platforms configure via the Accounts API

## Font Compatibility (24 fonts)

Each font has locale restrictions — unsupported locales fall back to system font. Most broadly supported: **Noto Serif** (only `th` unsupported), **Noto Sans** (`ja`, `ko`, `th`), **Roboto** (`ja`, `ko`, `zh`, `zh-HK`, `zh-TW`).

Most restricted: **Lato** (unsupported in 18 locales including CJK, Eastern European languages).

Full locale table in raw file.

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-how-checkout-works]] — How Checkout works: full feature list
- [[source-stripe-checkout-quickstart]] — Quickstart with branding params

## Raw Sources

- [[stripe-checkout-appearance-2025]] — Customize appearance: branding_settings API, logo/icon logic, Connect override, 24-font compatibility table with unsupported locales
