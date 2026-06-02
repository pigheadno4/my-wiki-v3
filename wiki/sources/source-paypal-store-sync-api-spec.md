---
title: "PayPal Store Sync — Cart API OpenAPI Specification"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-store-sync-api-reference-2025.md"
  - "paypal-store-sync-api-get-cart-2025.md"
  - "paypal-store-sync-api-put-cart-2025.md"
  - "paypal-store-sync-api-checkout-2025.md"
tags: [paypal, agentic-commerce, store-sync, cart-api, openapi, api-reference]
---

## Summary

Full OpenAPI 3.0.3 specification (v1.2.0) for the PayPal Cart API used in Store Sync agentic commerce integration. 2757 lines covering the complete schema, all endpoints, request/response examples, and error structures.

## Key Takeaways

- **API version**: PayPal Cart API v1 (v1.2.0), OpenAPI 3.0.3
- **Base URL**: `https://your-domain.com/api/paypal/v1` — merchant's own server
- **Architecture**: Customer ↔ AI Agent ↔ PayPal Commerce Platform ↔ Your Merchant API
- **Auth**: PayPalJWT security scheme — PayPal-supplied JWT in Authorization header
- **Note**: Only `POST /merchant-cart` is in this spec; GET and PUT are separate reference pages

## Endpoints in Spec

| Method | Path | Returns |
| --- | --- | --- |
| POST | `/merchant-cart` | 201/200+issues/400/401/422/500 |
| GET | `/merchant-cart/{cartId}` | 200/400/401/404/500 |
| PUT | `/merchant-cart/{cartId}` | 200/400/401/404/422/500 — **full replacement, not merge** |
| POST | `/merchant-cart/{cartId}/checkout` | 200/400/401/404/422/500 — requires `token` (starts with `EC-`, 17 chars) + `payer_id` |

## Core Schema: PayPalCart

Unified object used for create, update, and response. Key fields:

| Field | R/W | Type | Notes |
| --- | --- | --- | --- |
| `id` | readOnly | string | Server-generated, e.g. `CART-123` |
| `status` | readOnly | enum | CREATED / INCOMPLETE / COMPLETED (READY deprecated) |
| `validation_status` | readOnly | enum | VALID / INVALID / REQUIRES_ADDITIONAL_INFORMATION |
| `validation_issues` | readOnly | array | Empty = ready for checkout |
| `totals` | readOnly | CartTotals | Server-calculated breakdown |
| `applied_coupons` | readOnly | array | Server-calculated |
| `available_shipping_options` | read/write | array | With `is_selected` flag |
| `items` | write | array | Min 1 item required |
| `customer` | write | Customer | name/phone/email |
| `shipping_address` | write | Address | |
| `billing_address` | write | Address | For tax calculation and compliance |
| `payment_method` | write | PaymentMethod | Only `type: paypal` supported |
| `checkout_fields` | write | array | AGE_VERIFICATION, GIFT_*, TERMS_ACCEPTANCE, etc. |
| `coupons` | write | array | Discount coupons to apply |
| `geo_coordinates` | write | GeoCoordinates | Optional WGS84 for location-aware services |

## Key Schemas

### CartItem

Required: `quantity`. Key optional: `variant_id` (preferred), `item_id` (deprecated), `parent_id` (group), `gift_options`.

### Customer

- `name.given_name` / `name.surname`: max 140 chars
- `email_address`: max 254 chars, RFC 5321 validated
- `phone.country_code`: 1–3 digits; `phone.national_number`: 1–14 digits

### CartTotals

Formula: `subtotal - discount + shipping + tax + handling + insurance - shipping_discount + custom_charges = total`

- `custom_charges` does NOT map directly to PayPal Orders API — roll into `handling` or add as line items
- `total` must match PayPal order total for successful capture

### ValidationIssue

| Field | Values |
| --- | --- |
| `code` | INVENTORY_ISSUE / PRICING_ERROR / SHIPPING_ERROR / PAYMENT_ERROR / DATA_ERROR / BUSINESS_RULE_ERROR |
| `type` | MISSING_FIELD / INVALID_DATA / BUSINESS_RULE |
| `context` | Typed per code: InventoryIssueContext / PricingErrorContext / ShippingErrorContext / PaymentErrorContext / DataErrorContext / BusinessRuleErrorContext |

Key context fields: `specific_issue`, `suggested_alternatives[]`, `resolution_options[].action`, `resolution_options[].metadata.auto_applicable`

### CheckoutField types (12)

AGE_VERIFICATION_18_PLUS, AGE_VERIFICATION_21_PLUS, GIFT_RECIPIENT_EMAIL, GIFT_RECIPIENT_NAME, GIFT_MESSAGE, DELIVERY_INSTRUCTIONS, DELIVERY_DATE_PREFERENCE, ALLERGY_INFORMATION, CUSTOM_ENGRAVING_TEXT, CUSTOM_SIZING_INFO, TERMS_ACCEPTANCE, PRIVACY_CONSENT

### AuthenticationIssueCode (401 details)

TOKEN_EXPIRED / TOKEN_INVALID / TOKEN_MISSING / SIGNATURE_VERIFICATION_FAILED / INSUFFICIENT_PERMISSIONS

### BusinessError (422)

Includes optional `business_context` field (same structure as ValidationIssue) — provides rich resolution context for 422 responses.

## Related Pages

- [[paypal]] — company page
- [[agentic-commerce]] — agentic commerce concept
- [[source-paypal-store-sync-product-catalog]] — integration guides (setup, response handling, use cases)

## Raw Sources

- [[paypal-store-sync-api-reference-2025]] — full 2757-line OpenAPI 3.0.3 spec: PayPalCart schema, ValidationIssue with 6 codes + typed context schemas, CartTotals formula, CheckoutField types, auth codes, BusinessError structure
- [[paypal-store-sync-api-get-cart-2025]] — GET /merchant-cart/{cartId}: path param cartId, returns PayPalCart on 200; 400 for malformed ID, 404 for well-formed but missing; schemas identical to POST spec
- [[paypal-store-sync-api-put-cart-2025]] — PUT /merchant-cart/{cartId}: FULL REPLACEMENT not merge; 3 request examples (update qty, add shipping address, change shipping selection); 200/400/401/404/422/500; schemas identical to POST spec
- [[paypal-store-sync-api-checkout-2025]] — POST /merchant-cart/{cartId}/checkout: requires payment_method.token (must start with 'EC-', 17 chars) + payer_id; 3 checkout-specific 400 errors; 5 distinct 500 error names (PAYMENT_CAPTURE_FAILED, INVENTORY_SYSTEM_ERROR, ORDER_SYSTEM_ERROR, etc.); response adds payment_confirmation.order_review_page
