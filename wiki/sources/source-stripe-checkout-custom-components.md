---
title: "Stripe Checkout: Extend Checkout with Custom Components"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-custom-components-2025.md"
tags: [stripe, checkout, custom-fields, custom-text, consent, terms-of-service, localization, policies, checkout-sessions]
---

## Summary

Reference for extending Stripe Checkout with custom fields, custom text, consent collection, localization, and policy display. Covers both hosted and embedded modes. Checkout Elements users don't need custom components — they compose freely.

## Key Takeaways

- **Custom fields**: up to 3 per session; not in `setup` mode; `text` (255 chars), `numeric` (255 digits), `dropdown` (200 options)
- **Custom text**: up to 1200 chars; Markdown (bold + links); 4 placements; may affect conversion rate
- **ToS consent**: `consent_collection.terms_of_service: 'required'` → checkbox; verified via `consent.terms_of_service = 'accepted'` in webhook
- **Payment method reuse agreement**: shown in setup/subscription/payment+setup_future_usage; hideable + replaceable with custom text
- **Localization**: auto-detects browser locale; override with `locale` param; affects number/currency formatting
- **Policies**: configured in Dashboard Checkout Settings (not per-session API)

## Custom Fields (`custom_fields`)

| Property | Required | Notes |
| --- | --- | --- |
| `key` | Yes | Unique identifier used to reconcile the field |
| `label.type` | Yes | `'custom'` for merchant-defined label |
| `label.custom` | Yes | Label text (not auto-translated) |
| `type` | Yes | `'text'`, `'numeric'`, or `'dropdown'` |
| `optional` | No | Default `false` — required by default |
| `text.minimum_length` / `maximum_length` | No | For `text` and `numeric` types |
| `text.default_value` / `dropdown.default_value` | No | Pre-filled value |
| `dropdown.options` | Yes (dropdown) | Array of `{label, value}` — up to 200 options |

**Limits**: max 3 fields; not available in `setup` mode; up to 255 chars (text), 255 digits (numeric).

**Retrieval**: `checkout.session.completed` webhook → `custom_fields` array; also Dashboard-editable via Transactions tab.

**Subscription lookup**: `stripe.checkout.sessions.list({ subscription: '...' })` to find the session and its custom fields.

## Custom Text (`custom_text`)

4 placements, all support Markdown (bold + links), max 1200 chars total:

| Placement | When shown |
| --- | --- |
| `shipping_address.message` | Below shipping address fields |
| `submit.message` | Above Pay button |
| `after_submit.message` | Below Pay button |
| `terms_of_service_acceptance.message` | Next to ToS checkbox |

> Adding extra text may reduce conversion rate — use sparingly.

## Submit Button (`submit_type`)

Override the default "Pay" button label for one-time payments. Options: `'auto'`, `'pay'`, `'book'`, `'donate'`. Example: `submit_type: 'donate'` → "Donate $5.00 USD".

## Consent Collection

### Terms of Service
- `consent_collection.terms_of_service: 'required'` → dynamic checkbox
- Customize text with `custom_text.terms_of_service_acceptance.message` (Markdown link to your ToS)
- Verified via `checkout.session.completed`: `consent.terms_of_service = 'accepted'`
- Set ToS URL in Dashboard public details first

### Promotional Emails
- `consent_collection.promotions: 'auto'` (see [[source-stripe-how-checkout-works]])

### Payment Method Reuse Agreement
- Shown automatically in `setup`/`subscription`/`payment` + `setup_future_usage` modes
- Hide: `consent_collection.payment_method_reuse_agreement.position: 'hidden'`
- Replace with custom text via `custom_text.after_submit.message`, `custom_text.submit`, or `custom_text.terms_of_service_acceptance`

## Localization

- Default: auto-detects browser locale; override with `locale` param on session create
- Affects: UI language (if Stripe supports it), number formatting, currency display
- Custom field labels are NOT auto-translated — match `locale` to your label language

## Policies (Dashboard-configured)

Set in [Checkout Settings](https://dashboard.stripe.com/settings/checkout) — not per-session API:
- **Contact information**: support phone, email, website
- **Legal policies**: ToS + privacy policy links; optional "Display agreement to legal terms" checkbox
- **Return/refund policies**: accept returns/refunds/exchanges, fee structure, time limit, shipping/in-store return options, custom message
- Free return/refund/exchange policies are highlighted to customers

## Checkout Elements Note

Checkout Elements users don't need custom components — compose Elements freely in your own interface and insert custom UI between them.

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-how-checkout-works]] — Promotional email consent (`consent_collection.promotions`)

## Raw Sources

- [[stripe-checkout-custom-components-2025]] — Custom fields (3 types, limits, validation, defaults), custom text (4 placements), submit_type, ToS consent, payment method reuse agreement, localization, Dashboard-configured policies (12 CDN images, 1 video)
