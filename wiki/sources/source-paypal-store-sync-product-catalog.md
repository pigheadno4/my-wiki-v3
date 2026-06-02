---
title: "PayPal Store Sync — Product Catalog Integration"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-store-sync-overview-2025.md"
  - "paypal-store-sync-product-catalog-2025.md"
  - "paypal-store-sync-connect-feed-2025.md"
  - "paypal-store-sync-api-overview-2025.md"
  - "paypal-store-sync-setup-api-2025.md"
  - "paypal-store-sync-braintree-2025.md"
  - "paypal-store-sync-response-handling-2025.md"
  - "paypal-store-sync-use-cases-2025.md"
  - "paypal-store-sync-advanced-2025.md"
tags: [paypal, agentic-commerce, store-sync, product-catalog, product-feed, ai]
---

## Summary

Technical reference for integrating a product catalog (feed) into PayPal Store Sync. Covers file format requirements, 3 feed specifications, variant handling, validation rules, and troubleshooting.

## Key Takeaways

- **File constraints**: max 4 GB; UTF-8; header row required; compressed archives (GZ/ZIP) must contain only 1 CSV/TSV file
- **3 feed formats**: CSV, TSV, PSV
- **3 feed specifications**: Google Product Feed (reuse existing), OpenAI ACP (richer, agent-optimized), PayPal Enhanced Shopping Feed (Google + 2 extra fields — easiest upgrade path)
- **Critical dependency**: `is_eligible_checkout: true` only works if `is_eligible_search: true`
- **Variants**: one row per variant; share `item_group_id`/`group_id`; invalid rows skipped silently — not feed-fatal
- **Images**: JPG/PNG only; min 300×300px; must return HTTP 200
- **Price format**: `"XX.XX USD"` — currency must match merchant profile

## File Requirements

| Constraint | Value |
| --- | --- |
| Max file size | 4 GB |
| Encoding | UTF-8 |
| Header row | Required |
| Compressed archive | Max 1 CSV/TSV file inside GZ or ZIP |

## Feed Specifications Comparison

| Spec | Best for | Required fields | Key extras |
| --- | --- | --- | --- |
| Google Product Feed | Already have Google Shopping feed | 7 | Standard variant/image/price fields |
| OpenAI ACP | Agent-optimized, conversational checkout | 17 | `seller_name`, `seller_url`, `seller_tos`, `return_policy`, `target_countries`, `is_eligible_search`, `is_eligible_checkout` |
| PayPal Enhanced Shopping Feed | Minimal upgrade from Google feed | 7 + 2 | `is_eligible_search` + `is_eligible_checkout` added to Google feed |

## Google Product Feed — Required Fields (7)

`id`, `title`, `link`, `image_link`, `description` (min 25 chars), `price` (`"19.99 USD"`), `availability`

## OpenAI ACP — Required Fields (17)

`item_id`, `group_id`, `title`, `url`, `image_url`, `description`, `price`, `availability`, `brand`, `listing_has_variations`, `seller_name`, `seller_url`, `seller_privacy_policy`, `seller_tos`, `return_policy`, `target_countries`, `store_country`

## PayPal Enhanced Shopping Feed — Additional Required Fields (2)

`is_eligible_search` + `is_eligible_checkout` (on top of all Google Product Feed required fields)

## Agentic Eligibility Fields

| Field | Effect |
| --- | --- |
| `is_eligible_search: true` | Product surfaces in AI search results |
| `is_eligible_checkout: true` | Product can be purchased via agentic surfaces (requires `is_eligible_search: true`) |

## Availability Values

`in_stock` / `out_of_stock` / `preorder` / `backorder`

## Variant Handling

- One row per variant
- All variants share same `item_group_id` (Google) or `group_id` (ACP/Enhanced)
- Each variant has unique `id` or `item_id`
- Include `color`, `size`, `size_system`, `gender` per variant
- Invalid rows skipped silently during ingestion — validate before upload

## Common Troubleshooting

| Issue | Fix |
| --- | --- |
| Feed rejected on upload | File exceeds 4 GB — split into smaller files |
| Products missing after ingestion | Missing required fields — rows skipped silently |
| Encoding errors | Re-export as UTF-8 |
| Image not displayed | URL not accessible or not returning HTTP 200; must be JPG/PNG |
| Product not in search results | Set `is_eligible_search: "true"` |
| Agentic checkout unavailable | `is_eligible_search` must be `"true"` before `is_eligible_checkout` takes effect |
| Variants not grouped | Inconsistent `item_group_id`/`group_id` across rows |
| Compressed archive rejected | Archive contains more than 1 data file |

## Cart API Implementation

**3 endpoints** your merchant server must implement:

| Endpoint | Purpose | Critical notes |
| --- | --- | --- |
| `POST /merchant-cart` | Create cart | Also call `POST /v2/orders` to create PayPal payment context |
| `PUT /merchant-cart/{id}` | Update cart | **Full replacement — not merge**; include all fields or they reset; call `PATCH /v2/orders/{id}` |
| `POST /merchant-cart/{id}/checkout` | Complete purchase | Call `POST /v2/checkout/orders/{id}/capture`; `payment_method.token` = PayPal Order ID |

**JWT auth**: PayPal supplies JWT in `Authorization: Bearer` header. Verify against public key at `https://www.paypal.ai/.well-known/jwks.json`. Token contains merchant ID + permissions + expiry.

**Orders API v2 mapping**:

| Cart action | Orders API call |
| --- | --- |
| Create cart | `POST /v2/orders` |
| Add/remove items, change qty, apply coupon, update shipping | `PATCH /v2/orders/{id}` |
| Token expired, new cart after checkout | `POST /v2/orders` (fresh context) |
| Checkout | `POST /v2/checkout/orders/{id}/capture` |

**Response fields**: `status` (CREATED/INCOMPLETE/COMPLETED), `validation_status` (VALID/INVALID/REQUIRES_ADDITIONAL_INFORMATION), `validation_issues[]`, `payment_method.token` (= PayPal Order ID), `payment_confirmation.order_review_page` (after checkout).

**Response handling key rules**:

- Business logic errors → `200 OK` + `validation_issues[]` (not HTTP error codes)
- `422` only when you cannot create the cart at all due to validation failure
- `400` for malformed requests; `404` for valid ID not found; `500` for server errors
- `validation_issues[].code`: INVENTORY_ISSUE / PRICING_ERROR / SHIPPING_ERROR / PAYMENT_ERROR / DATA_ERROR / BUSINESS_RULE_ERROR
- `validation_issues[].type`: MISSING_FIELD / INVALID_DATA / BUSINESS_RULE
- 8 resolution actions (with `auto_applicable` flag): ACCEPT_NEW_PRICE, ACCEPT_BACK_ORDER, SUGGEST_ALTERNATIVE, UPDATE_ADDRESS, REMOVE_ITEM, SPLIT_ORDER, CONTACT_SUPPORT, RETRY_LATER

Postman collection available for download from docs.

## Agentic Shopping Flow

**PayPal calls your merchant API** — your store implements a server that PayPal calls, not the reverse.

3-step sequence:

1. **Search**: Agent → `GET /search?query=...` → PayPal returns results
2. **Create cart**: Agent → `POST /commerce/carts {product_id, access_token}` → PayPal calls `POST /merchant-cart {items, shippingAddress, paymentSource}` → merchant returns `{cartId, items, shippingOptions, totals}`
3. **Complete payment**: Agent → `POST /commerce/carts/{id}/complete_payment` → PayPal calls `POST /merchant-cart/{cartId}/checkout {paymentSource}` → merchant returns `{status: 'completed', orderId, transactionId}`

**2 integration paths**: Orders API v2 or Braintree.

**Braintree path differences** (vs Orders v2):

- Share `merchant_id` + `tokenization_key` with PayPal upfront
- Cart creation: do NOT return a token — PayPal creates the Braintree token automatically
- Checkout: `payment_method.token` = Braintree nonce (UUID); merchant uses it to create a Braintree transaction
- Cart API schema: `github.com/paypal/agent-commerce/blob/main/v1/api-spec.yaml`

## Feed Ingestion (Connect)

| Method | Setup | Notes |
| --- | --- | --- |
| Public URL (recommended) | Provide URL to account manager | Basic auth supported (`user:pass`); IP allowlist may be needed |
| FTP/SFTP | Provide host/port/user/pass to account manager | Supports multi-storefront via manifest.csv |
| S3/GCS | Grant PayPal service account read access | Supports multi-storefront via manifest.csv |

**Default cadence**: once daily. Custom schedules via account manager.

**Multi-storefront** (FTP/S3/GCS only): provide `manifest.csv` with 7 fields per row — `storeName`, `storeUrl`, `paypalMerchantId`, `country`, `currency`, `favIcon`, `pathToFileInThisBucket`. All setup is account-manager-driven — no self-serve API.

## Related Pages

- [[paypal]] — company page
- [[agentic-commerce]] — agentic commerce concept
- [[source-paypal-agentic-commerce]] — Store Sync + Agent Ready overview

## Raw Sources

- [[paypal-store-sync-overview-2025]] — Store Sync eligibility: US/USD/physical goods/Orders v2; two integration steps
- [[paypal-store-sync-product-catalog-2025]] — full 293-line product catalog guide: 3 specs, field tables, variant handling, validation, troubleshooting
- [[paypal-store-sync-connect-feed-2025]] — Connect feed: 3 ingestion methods (Public URL recommended / FTP/SFTP / S3/GCS); default daily cadence; Public URL auth = user:pass; IP allowlist may be needed; multi-storefront via manifest.csv (7 fields, FTP/S3/GCS only); all setup via account manager
- [[paypal-store-sync-api-overview-2025]] — Agentic shopping API overview: PayPal calls merchant API (not reverse); 3-step flow (search/create cart/complete payment); 2 integration paths (Orders API v2 or Braintree); buyer wallet used for payment
- [[paypal-store-sync-setup-api-2025]] — Cart API implementation: 3 endpoints (POST/PUT/POST checkout); JWT auth via PayPal public key; PUT = full replacement not merge; Orders API v2 mapping table; payment_method.token = PayPal Order ID; validation_status/issues in response; Postman collection available
- [[paypal-store-sync-braintree-2025]] — Braintree integration variant: share merchant_id+tokenization_key with PayPal; cart creation = no token returned (PayPal creates it); checkout token = Braintree nonce (UUID); cart schema at github.com/paypal/agent-commerce
- [[paypal-store-sync-response-handling-2025]] — Response handling: 3 status fields; business errors → 200+validation_issues (not HTTP codes); 422 only when cart cannot be created; 6 error codes; 8 resolution actions with auto_applicable flag; SUGGEST_ALTERNATIVE and RETRY_LATER are auto-applicable
- [[paypal-store-sync-use-cases-2025]] — Integration use cases: 6 concrete validation_issues JSON examples (out-of-stock + alternatives, back-order, discontinued, price change, invalid address + auto-correction, PO box restriction, geographic restriction, maintenance mode)
- [[paypal-store-sync-advanced-2025]] — Advanced use cases: gift cards (items[].gift_options with recipient/delivery_date/message); geo_coordinates (WGS84 decimal, separate from shipping_address, enables local inventory/delivery radius/distance pricing, optional/graceful degradation)
