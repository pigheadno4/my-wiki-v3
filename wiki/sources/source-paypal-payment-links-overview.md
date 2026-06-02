---
title: "PayPal Payment Links and Buttons Overview"
type: source
date_ingested: 2026-04-16
original_format: webpage
raw_files:
  - "paypal-payment-links-overview.md"
  - "paypal-payment-links-choose-integration.md"
  - "paypal-payment-links-create.md"
  - "paypal-payment-links-share.md"
  - "paypal-payment-links-buy-button.md"
  - "paypal-payment-links-shopping-cart.md"
  - "paypal-payment-links-customize-checkout.md"
  - "paypal-payment-links-inventory-variants.md"
  - "paypal-payment-links-api.md"
  - "paypal-payment-links-api-use-cases.md"
  - "paypal-payment-links-troubleshooting.md"
  - "paypal-payment-links-faq.md"
tags: [paypal, payment-links, buy-button, qr-code, no-code, invoicing]
---

## Summary

Overview of PayPal's no-code payment options: Payment Links, Buy Button, Shopping Cart Button, and QR Codes. Also compares Payment Links vs Invoicing. From `docs.paypal.ai` (newer PayPal docs domain).

## FAQ Highlights

- **Venmo cannot be tested in sandbox** — live environment required
- **Payment links do not expire** — no single-use or expiration support
- **One-time payments only** — subscriptions not supported
- **Account shipping settings override does not apply** to payment links/buttons
- **PDT supported**: sends transaction details to return URL when Auto Return is enabled
- **IPN supported**: account settings → Notifications → IPN settings
- **Webhooks**: Developer Dashboard → Apps and Credentials → Manage webhooks
- **CSS selector pattern** for hiding button labels: `#paypal-form-fields-container-{ID}` with child selectors; warning: hiding required input fields breaks transactions
- `locale.x` + `country.x` work on both payment link URLs **and** button script tags

## Troubleshooting

- **Business account required** — Payment Links and Buttons unavailable on personal accounts
- **Button doesn't render**: check CSP; verify button ID in PayPal account matches code on page
- **Same button ID on one page** → only first renders; **mixed currencies on one page** → only first renders
- **PayPal SDK script must be included once** per page
- **CSP required domains**: `*.paypal.com` + `*.paypalobjects.com` for script-src, img-src; `*.paypal.com` for style-src, connect-src, frame-src; needs `'unsafe-inline'` for script-src and style-src
- **Billing address defaults to US** for card payments (browser locale issue):
  - Payment Links fix: append `?locale.x=en_CA&country.x=CA` to URL (affects all buyers including US buyers)
  - Buy Buttons / Shopping Cart Buttons: not supported
- **Locale/language wrong**: `LANG` cookie from previous PayPal visit overrides browser locale — same fix as billing address
- **Continue Shopping link**: appears when Homepage URL is set in Payment Link settings — remove URL to hide link

## Four No-Code Payment Options

| Option | Best for | Setup |
| --- | --- | --- |
| Payment Link | Sharing via social/email/messages | No-code |
| Buy Button | Single product on a website | No-code + basic HTML |
| Shopping Cart Button | Multiple products in one transaction | No-code + basic HTML |
| QR Code | In-person / contactless payments | No-code |

## Payment Methods Supported

PayPal, Pay Later, Venmo, Apple Pay, major debit and credit cards.
200+ countries, 23+ currencies, multiple languages. PayPal handles PCI compliance.

## Payment Links vs Invoicing

| Dimension | Payment Links | Invoicing |
| --- | --- | --- |
| Customer | Anyone with the link | Specific individual/business |
| Reusability | Reusable multiple times | One per transaction |
| Recurring | One-time only | One-time invoices |
| Partial payments | ✕ | ✓ |
| Customer sets amount | ✓ | ✕ |
| Collection tools | ✕ | Reminders + status tracking |
| Pay by Bank (ACH) | ✕ | ✓ |
| Discounts / Taxes | ✓ | ✓ |
| Hosted payment page | ✓ | ✓ |

## Payment Links API

Base path: `/v1/checkout/payment-resources`

| Method | Endpoint | Response | Notes |
| --- | --- | --- | --- |
| POST | `/v1/checkout/payment-resources` | 201 Created | Requires `PayPal-Request-Id` header; `integration_mode: "LINK"` + `type: "BUY_NOW"` required |
| GET | `/v1/checkout/payment-resources` | 200 OK | Paginated via `page_size` + `page_token`; supports `status` filter |
| GET | `/v1/checkout/payment-resources/{id}` | 200 OK | ID format: `PLB-{id}` |
| PUT | `/v1/checkout/payment-resources/{id}` | 204 (sometimes 200) | **Full replace** — send complete object, not just changed fields |
| DELETE | `/v1/checkout/payment-resources/{id}` | 204 No Content | Permanent; QR codes pointing to deleted link → expiration page |

**Payment link URL**: found in `links[]` with `rel: "payment_link"` — format: `https://www.paypal.com/ncp/payment/{PLB-id}`

**Must enable**: "Payment Links & Buttons" in app credentials (Apps and Credentials → app settings).

Minimum required fields: `integration_mode`, `type`, `reusable`, `return_url`, `line_items[].name`, `line_items[].unit_amount`.

Supported line item fields: `name`, `description`, `product_id`, `unit_amount`, `taxes`, `shipping`, `collect_shipping_address`, `customer_notes`, `variants` (dimensions/options), `adjustable_quantity.maximum`.

### Key API patterns (from use cases)

- **Variant-level pricing**: omit `unit_amount` at line item level; set `unit_amount` per option in primary dimension instead
- **PROFILE tax/shipping**: `"type": "PREFERENCE", "value": "PROFILE"` — applies merchant's pre-configured PayPal account settings; merchant must set up tax/shipping in PayPal account first
- **customer_notes**: array of custom checkout fields (label + required flag); use for gift messages, invoice IDs
- **adjustable_quantity.maximum**: caps units per transaction
- Secondary variant dimensions (no `unit_amount`) = selection-only, no price impact

Error codes: 400 INVALID_REQUEST, 403 NOT_AUTHORIZED, 404 RESOURCE_NOT_FOUND, 422 UNPROCESSABLE_ENTITY, 500 INTERNAL_SERVER_ERROR.

## Inventory, Variants & Fees

**Inventory** (One set price only):

- Per-transaction quantity limit
- Item ID, stock quantity, alert quantity for low-stock email notifications
- Configurable: allow/block out-of-stock purchases

**Variants**: up to 3 variations per item, up to 10 options per variant; per-variant pricing with "Add price per variant"

**Checkout tab fees**:

| Type | Notes |
| --- | --- |
| Taxes | Percentage, flat, or not applicable; or use account settings; tax-inclusive pricing: include tax in item price |
| Discounts | Amount off (fixed) or percentage; applied per item and variant |
| Handling fee | Single flat fee per transaction regardless of quantity |
| Shipping fee | Configurable; supports free shipping |

## Customization Settings

- **Payment methods**: PayPal, Pay Later, Venmo, Apple Pay (opt-in); credit/debit **enabled by default**
- **Stacked buttons**: settings apply to **all existing** sitewide; **no custom colors** (standard PayPal only); second button is region-dependent (can set to None); label options: Checkout / Proceed / Pay / Custom
- **Single button**: changes apply to **new buttons only** (existing unchanged); **custom colors supported**
- **Cart buttons**: apply to **all existing** cart buttons; custom colors supported
- **Shopping cart buttons auto-generate a payment link + QR code** reusable across channels
- **Auto-return URL scope**: Shopping Cart = sitewide (Settings → Cart Buttons tab); Payment Links/Buy Buttons = per-link (Confirmation tab)

## Shopping Cart Button Integration

Two buttons required together:

- **View Cart**: Part 1 in `<head>` (once per page) + Part 2 in sitewide visible location (e.g. nav); Part 2 can appear in multiple locations
- **Add to Cart**: single snippet per product, placed near the product in `<body>`; repeat for each product

⚠️ Opening Settings while building a button replaces the editor — unsaved changes are lost.

`<head>` fallback: paste Part 1 at top of `<body>`, above Part 2.

## Buy Button Integration

Two display modes:

- **Stacked button** (PayPal + Pay Later + cards together): HTML = 2 parts (Part 1 in `<head>`, Part 2 in `<body>`); React = 3 parts. Fallback if no `<head>` access: paste Part 1 at top of `<body>`
- **Single button**: 1 snippet, paste in `<body>` only

**Button config is server-side**: product detail changes take effect without updating HTML code. **Exception: changing currency code requires replacing the button code.**

## Share & QR Code

- **Share path**: Sales → Payment Links and Buttons → Open → View → Payment Link → copy
- **QR code**: same path → QR code → Download QR code; **does not expire**
- **QR + deleted link**: if the payment link is deleted, QR scans redirect to an expiration page (QR is tied to the link)
- **Payment method availability**: country and eligibility-dependent — not all methods show for every buyer

## Create Payment Link (Dashboard Flow)

11-step flow: Pay & Get Paid → Create Payment Links and Buttons → Product tab → Price → Checkout tab → Confirmation tab → Build it.

- **One set price**: fixed amount; for products/services
- **Customer-set price**: buyer enters amount; for donations/tips/pay-what-you-want; enables "Label for Invoice ID" to match payments to orders
- **Auto-return**: optional redirect URL after successful payment (Confirmation tab); must be publicly accessible
- Testing: use sandbox buyer account; verify auto-return redirect and transaction in dashboard

## Integration Options

> [!info] API scope limitation
> The Payment Links and Buttons API supports **payment links only**. Buy buttons and shopping cart buttons can only be created via the dashboard UI.

| | UI Editor | API |
| --- | --- | --- |
| Who | No-code merchants | Developers with REST/backend experience |
| Volume | Low-to-medium | High-volume or dynamic |
| How | Create in dashboard, copy link/code | Call API, store returned URLs in your flows |
| Buy/Cart buttons | ✓ | ✗ |

## Related Pages

- [[paypal]] — company page
- [[paypal-payment-links]] — Payment Links concept page
- [[source-paypal-invoicing-overview]] — Invoicing docs

## Raw Sources

- [[paypal-payment-links-overview]] — verbatim docs.paypal.ai overview page
- [[paypal-payment-links-choose-integration]] — Integration options: API supports links only (not buttons); UI Editor for low-medium volume; API for high-volume/dynamic
- [[paypal-payment-links-create]] — Create payment link: 11-step dashboard flow, fixed vs customer-set price, auto-return, Label for Invoice ID
- [[paypal-payment-links-share]] — Share: Sales nav path, QR code download, QR never expires but link deletion → expiration page, payment methods are country-dependent
- [[paypal-payment-links-buy-button]] — Buy button: stacked (2-part HTML / 3-part React) vs single (1 snippet); button config is server-side; exception: currency change requires new code
- [[paypal-payment-links-shopping-cart]] — Shopping cart: View Cart (Part 1 in head + Part 2 sitewide) + Add to Cart (per product); Settings mid-build loses unsaved changes
- [[paypal-payment-links-customize-checkout]] — Customize: stacked (all existing, no custom color) vs single (new only, custom color); auto-return scope differs by button type; cart buttons auto-generate payment link + QR
- [[paypal-payment-links-inventory-variants]] — Inventory (quantity limit = One set price only, out-of-stock toggle), variants (3 max, 10 options each), taxes/discounts/handling/shipping
- [[paypal-payment-links-api]] — Payment Links API: POST/GET/PUT/DELETE /v1/checkout/payment-resources; PLB-* ID format; payment_link in links[]; PUT is full replace; 690 lines with full examples
- [[paypal-payment-links-api-use-cases]] — API use cases: 4 POST patterns (return URL, variants, variant-level pricing, PROFILE tax/shipping); customer_notes; adjustable_quantity; 705 lines
- [[paypal-payment-links-troubleshooting]] — Troubleshooting: CSP config, same-ID/same-currency single-render rule, billing address locale fix (Payment Links only), Continue Shopping removal
- [[paypal-payment-links-faq]] — FAQ: Venmo sandbox not supported, no link expiration, one-time only (no subscriptions), account shipping ignored, CSS selectors for hiding labels, PDT/IPN/webhook support
