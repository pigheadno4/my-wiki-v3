---
title: "Pay upon Invoice with Ratepay"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-pay-upon-invoice.md"
  - "paypal-apm-pay-upon-invoice-integrate.md"
  - "paypal-apm-pay-upon-invoice-fraudnet.md"
tags: [paypal, apm, pay-upon-invoice, ratepay, germany, bnpl, deferred-payment, invoice, vat, dispute]
---

## Overview

Pay upon Invoice (Rechnungskauf mit Ratepay) is Germany's BNPL deferred payment method. PayPal partners with Ratepay: merchant is funded immediately, buyer pays Ratepay within 30 days via bank transfer.

Source URL: <https://developer.paypal.com/docs/checkout/apm/pay-upon-invoice/>

Last updated: 2025-05-12

## Key Details

| Field | Value |
| --- | --- |
| Buyer countries | Germany (DE) only |
| Merchant countries | Germany (DE) only |
| Payment type | Deferred payment (BNPL) |
| Minimum | **5 EUR** |
| Maximum | **2,500 EUR** |
| Refunds | Within 180 days |
| German name | Rechnungskauf mit Ratepay |

## Eligibility Requirements (most restrictive of all APMs)

- **B2C only** — no B2B transactions
- **Germany only** — both buyer and merchant must be in Germany
- **Terms acceptance required** — merchant must acknowledge [Ratepay T&C](https://www.paypal.com/de/webapps/mpp/ua/rechnungskauf-mit-ratepay?locale.x=eng_DE) (part of PayPal User Agreement)
- **VAT ID required** — EU regulation; without it PayPal collects additional VAT on PayPal fees
- **Ship within 7 days** of transaction
- **Digital/virtual goods prohibited** — no vouchers, gift cards, cash codes
- Approved merchants only; self-serve approval via sandbox/live links

## How It Works

1. Buyer selects Pay upon Invoice at checkout
2. PayPal sends buyer info to Ratepay for risk assessment
3. Ratepay approves → emails payment instructions to buyer (30-day bank transfer deadline)
4. **Merchant funded immediately** (not after buyer pays)
5. Buyer pays Ratepay directly (not merchant)
6. If buyer doesn't pay: Ratepay handles dunning (no action needed from merchant)

## Buyer Information Collected

Most extensive of all APMs: **full name, email, delivery address, billing address, date of birth, phone number**

## Merchant Obligations

### Shipment tracking

Must send tracking via Add Tracking API with **`notify_buyer: false`** for all Ratepay transactions. Also acceptable: PayPal account Transaction details page.

### Dispute handling

- **10 business days** to respond with evidence (carrier name + tracking number, invoice copy)
- Retain proof of shipment/delivery for **at least 180 days**
- Carrier tracking data deleted after 90 days — save PDF/image copy
- Non-response = automatic reversal of disputed funds
- PayPal may contact merchant if buyer disputes with Ratepay

### VAT statements

Monthly VAT Statements available in PayPal account — summary of VAT collected on PayPal fees; use for tax credits/self-assessment.

## Buyer Experience Flow

1. Select Pay upon Invoice (show benefits + due date)
2. Fill form: name, email, addresses, **date of birth**, phone
3. Legal text displayed near "Buy Now" button (required)
4. Success: Ratepay emails payment instructions to buyer
5. Failure (Ratepay risk decline): must display specific error message
6. Invoice sent with `payment_reference` and `payment_entity` from API response

> [!warning] Error handling requirement
> If Ratepay declines due to buyer risk, merchant must display the specific error message from the Error handling section of the integration guide — not a generic error.

## FraudNet Integration

Source URL: <https://developer.paypal.com/docs/checkout/apm/pay-upon-invoice/fraudnet/>

Last updated: 2025-12-09

### Required parameters

| Param | Name | Max length | Value |
| --- | --- | --- | --- |
| `f` | FraudNet Session Identifier | 32 | Unique random ID per transaction |
| `s` | Source Website Identifier | 32 | `<merchant_id>_<page_id>` |

`fncls` attribute key (hardcoded): `fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99`

`sandbox: true` required in sandbox environment.

### Critical: `PAYPAL-CLIENT-METADATA-ID` header

The `f` parameter value must be sent as `PAYPAL-CLIENT-METADATA-ID` HTTP header on the Create Order API call.

### `page_id` allowed values

`home-page`, `search-result-page`, `category-page`, `product-detail-page`, `cart-page`, `inline-cart-page`, `checkout-page`

### CSP allowlist

| Tag | URLs |
| --- | --- |
| img-src | `https://c.paypal.com`, `https://b.stats.paypal.com` |
| frame-src | `https://c.paypal.com` |
| script-src | `https://c.paypal.com` |

Nonce support available; static nonce discouraged.

## Integration Guide

Source URL: <https://developer.paypal.com/docs/checkout/apm/pay-upon-invoice/integrate-pui-merchant/>

Last updated: 2025-05-14

### Required checkout page elements

1. **FraudNet JS library** — Ratepay buyer credit/risk check (separate from SDK)
2. **PUI Legal Component** (`components=legal`, `fundingSource: paypal.Legal.FUNDING.PAY_UPON_INVOICE`) OR copy-pasted legal text (English and German both provided)

### Create Order payload

```json
{
  "intent": "CAPTURE",
  "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
  "payment_source": {
    "pay_upon_invoice": {
      "name": { "given_name": "John", "surname": "Doe" },
      "email": "buyer@example.com",
      "birth_date": "1990-01-01",
      "phone": { "national_number": "6912345678", "country_code": "49" },
      "billing_address": { ... },
      "experience_context": {
        "locale": "en-DE",
        "brand_name": "EXAMPLE INC",
        "logo_url": "https://example.com/logoUrl.svg",
        "customer_service_instructions": ["..."]
      }
    }
  },
  "purchase_units": [{
    "amount": { "breakdown": { "item_total": ..., "tax_total": ... } },
    "items": [{ "category": "PHYSICAL_GOODS", "tax_rate": "19.00", ... }],
    "invoice_id": "MERCHANT_INVOICE_ID"
  }]
}
```

> [!info] `experience_context.locale` contradiction
> Sample shows `en-DE` but docs note only `de-DE` is currently supported as the preferred language.

Key constraints:

- `intent: CAPTURE` only (not AUTHORIZE)
- **`PHYSICAL_GOODS` category only** in items — wrong category = transaction reversal
- **`invoice_id` strongly recommended** — appears in Ratepay payment instruction email; if absent, PayPal order `id` used
- Tax breakdown required in amount
- **Duplicate order protection**: `PUI_DUPLICATE_ORDER` error if same payload resubmitted within seconds

### Response

Initial status: **`PENDING_APPROVAL`** (unique — other APMs return `PAYER_ACTION_REQUIRED`).

After `PAYMENT.CAPTURE.COMPLETED`, GET order details to obtain:

- `payment_source.pay_upon_invoice.payment_reference` — buyer enters as `Verwendungszweck` (reason for transfer)
- `payment_source.pay_upon_invoice.deposit_bank_details` — BIC, IBAN, bank name, account holder name

### Webhooks (unique to PUI)

| Webhook | Meaning |
| --- | --- |
| `PAYMENT.CAPTURE.COMPLETED` | Success — ship goods |
| `PAYMENT.CAPTURE.DENIED` | Ratepay declined |
| `CHECKOUT.PAYMENT-APPROVAL.REVERSED` | **Unique to PUI** — approved order cancelled/refunded (e.g. capture window missed) |

### Mandated error messages (legal requirement)

| Error code | Must display to buyer |
| --- | --- |
| `PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED` | Name/address validation failed (EN + DE text provided) |
| `PAYMENT_SOURCE_DECLINED_BY_PROCESSOR` | Ratepay risk decline (EN + DE text provided) |

### Sandbox test emails (5 failure scenarios)

| Error | Test email |
| --- | --- |
| `PAYMENT_SOURCE_INFO_CANNOT_BE_VERIFIED` | `payment_source_info_cannot_be_verified@example.com` |
| `PAYMENT_SOURCE_DECLINED_BY_PROCESSOR` | `payment_source_declined_by_processor@example.com` |
| `PAYMENT_SOURCE_CANNOT_BE_USED` | `payment_source_cannot_be_used@example.com` |
| `BILLING_ADDRESS_INVALID` | `billing_address_invalid@example.com` |
| `SHIPPING_ADDRESS_INVALID` | `shipping_address_invalid@example.com` |

Any other email = successful scenario.

## Raw Sources

- [[paypal-apm-pay-upon-invoice]] — verbatim overview page with buyer experience flow and 6 UX images
- [[paypal-apm-pay-upon-invoice-integrate]] — integration guide: FraudNet, legal component, Create Order payload, PENDING_APPROVAL status, deposit_bank_details, mandated error messages, 5 test emails
- [[paypal-apm-pay-upon-invoice-fraudnet]] — FraudNet JS library: `f`+`s` params, `fncls` key, `PAYPAL-CLIENT-METADATA-ID` header, page_id values, CSP allowlist

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
