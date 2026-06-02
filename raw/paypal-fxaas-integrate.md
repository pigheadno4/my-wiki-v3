<!-- Source URL: https://developer.paypal.com/docs/checkout/fx-as-a-service/integrate/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Integrate
slug: /docs/checkout/fx-as-a-service/integrate/
createTime: '2025-05-15T06:34:35.217Z'
updateTime: '2025-10-28T07:27:14.209Z'
---

# Integrate

Integration steps:
1. Get exchange rate quote (`/v2/pricing/quote-exchange-rates`)
2. Create order with `fx_id` (`/v2/checkout/orders`)
3. Capture payment (`/v2/checkout/orders/{id}/capture`)
4. Handle market moving events (`FX_RATE_CHANGE_DUE_TO_MARKET_EVENT`)
5. Test the FXaaS setup

## End-to-end workflow

![FXaaS integrate flow diagram](assets/fxaas-integrate-flow.png)

## Get exchange rate quote

API: `POST /v2/pricing/quote-exchange-rates`

Two modes:
- **Product-specific quote**: include `base_amount` → response includes `quote_amount` (product price in local currency)
- **Exchange rate only**: omit `base_amount` → response includes `exchange_rate` only; calculate prices locally

### Request parameters

| Parameter | Required | Description |
| --------- | -------- | ----------- |
| `base_currency` | Yes | Merchant's holding/settlement currency |
| `quote_currency` | Yes | Buyer's local currency |
| `base_amount` | No | Product price in base currency; omit for rate-only |
| `markup_percent` | No | Additional markup % added to the base exchange rate |

### Response parameters

| Parameter | Description |
| --------- | ----------- |
| `fx_id` | Unique ID linking the locked FX rate to an order — pass as `payee_receivable_fx_rate_id` |
| `quote_amount.value` | Product price in buyer's local currency (only if `base_amount` sent) |
| `exchange_rate` | Conversion rate between base and quote currencies |
| `expiry_time` | UTC timestamp: locked rate valid until this time (includes grace period) |
| `rate_refresh_time` | UTC timestamp: when PayPal refreshes its exchange rates (hard cutoff) |

### Rate validity rules

- Rate is valid for settlement until `rate_refresh_time` (hard cutoff)
- `expiry_time` adds a grace period after `rate_refresh_time` — standard cut-off period is **3 hours** (negotiable in contract)
- If order is created **without** `payee_receivable_fx_rate_id`: PayPal ignores `expiry_time` and uses only `rate_refresh_time` to validate

### Product-specific quote example

Request:
```bash
curl -X POST 'https://api-m.sandbox.paypal.com/v2/pricing/quote-exchange-rates' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -d '{
    "quote_items": [{
      "base_currency": "USD",
      "quote_currency": "GBP",
      "base_amount": 16.80,
      "markup_percent": 1
    }]
  }'
```

Response:
```json
{
  "exchange_rate_quotes": [{
    "base_amount": { "currency_code": "USD", "value": "16.80" },
    "quote_amount": { "currency_code": "GBP", "value": "13.80" },
    "exchange_rate": "0.80956391984",
    "fx_id": "MTFFQy05RjkzLTQ4ODkwMjE5LUEzRTAtREQ4OTc1NEQ1NUUw",
    "expiry_time": "2022-03-10T21:30Z",
    "rate_refresh_time": "2022-03-10T18:30Z"
  }]
}
```

### After getting the quote

- Save `exchange_rate_quotes[].fx_id` and `exchange_rate_quotes[].quote_amount{}`
- If rate-only: use `exchange_rate_quotes[].quote_amount.value` to calculate product prices locally
- Show prices in buyer's local currency
- At checkout: call Orders v2 API with stored `fx_id` as `payment_instruction.payee_receivable_fx_rate_id`

## Create order with fx_id

API: `POST /v2/checkout/orders`

Pass `fx_id` as `payment_instruction.payee_receivable_fx_rate_id`. The order `amount.currency_code` should be in the **quote currency** (buyer's local currency).

Request:
```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [{
    "amount": {
      "currency_code": "GBP",
      "value": "13.60"
    },
    "payment_instruction": {
      "payee_receivable_fx_rate_id": "MTFFQy05RjBFLTEyOTlDQTgwLTg3MzMtMzk0ODIwRUEwMTc4"
    }
  }]
}'
```

Response includes:
- `payment_instruction.payee_receivable_fx_rate_id`: echoed back
- `id`: order ID for capture
- `links[rel=approve]`: buyer approval URL

## Capture payment

API: `POST /v2/checkout/orders/{order_id}/capture`

Empty payload — PayPal identifies `fx_id` from the order and applies the locked rate if still valid.

```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: 7b92603e-77ed-4896-8e78-5dea2050476a"
```

Key response fields in `payments.captures[].seller_receivable_breakdown`:

| Field | Description |
| ----- | ----------- |
| `receivable_amount` | Final merchant settlement amount in **base currency** |
| `exchange_rate` | Applied exchange rate (source=quote currency → target=base currency) |
| `paypal_fee` | PayPal's transaction fee in **quote currency** (buyer's currency) |
| `gross_amount` | Payment amount in quote currency |
| `net_amount` | Gross minus PayPal fee (still in quote currency) |

Note: **PayPal transaction fee is charged in the buyer (payment) currency**, not the merchant's base currency.

## Special case: Handle market-moving events (force majeure)

If a market-moving event (natural disaster, political unrest) occurs after rate retrieval but before order creation, the Create order call returns:

```
HTTP 422 UNPROCESSABLE_ENTITY
issue: FX_RATE_CHANGE_DUE_TO_MARKET_EVENT
```

Response includes a HATEOAS link with `rel: new_fx_id` pointing to the updated exchange rate quote URL.

```json
{
  "details": [{
    "issue": "FX_RATE_CHANGE_DUE_TO_MARKET_EVENT",
    "links": [{
      "href": "https://api-m.sandbox.paypal.com/v2/pricing/quote-exchange-rates/NEW_FX_ID",
      "method": "GET",
      "rel": "new_fx_id"
    }]
  }]
}
```

Recovery flow:
1. `GET links[rel=new_fx_id].href` → retrieve updated quote
2. Display new product prices to buyer
3. Call Create order with new `fx_id`

**Important edge case**: After the 422 response, any subsequent Create order with the **old** `fx_id` returns 200 OK but silently uses the **new** `fx_id` — the `payee_receivable_fx_rate_id` in the response will show the new value.

## Test FXaaS setup

Test in sandbox: exchange rate retrieval, order creation with `fx_id`, payment capture, error handling (including market-moving event scenarios).
