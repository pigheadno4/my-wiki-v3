---
title: "PayPal Checkout: Contact Module"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-contact-module.md"
tags: [paypal, checkout, contact-module, orders-api, experience-context, gift-orders, us-only]
---

## PayPal Checkout: Contact Module

Official PayPal guide for the Contact Module — controls whether buyers can view and edit the email and phone number shared with the merchant during checkout.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/contact-module/>

Last updated: 2025-04-07

## Key Takeaways

### Availability

US only.

### Three contact preference modes

Set via `payment_source.paypal.experience_context.contact_preference` in the Create Order call:

| Value | Buyer can see? | Buyer can edit? | Notes |
| ----- | -------------- | --------------- | ----- |
| `NO_CONTACT_INFO` | No | No | **Default** — omitting the field also triggers this |
| `UPDATE_CONTACT_INFO` | Yes | Yes | Merchant-provided data pre-fills; buyer can change both email and phone (not individually) |
| `RETAIN_CONTACT_INFO` | Yes | No | Merchant must pass data; if no data passed, falls back to `NO_CONTACT_INFO` |

### Where contact data lives in the API

Contact info is stored in `purchase_units[].shipping`:
- `email_address` — string
- `phone_number` — object with `country_code` and `national_number`

### UPDATE_CONTACT_INFO: UX detail

Collapsed view shows buyer's primary PayPal profile email and phone. When expanded:
- Dropdown of up to 5 previously used contact entries (most recent first)
- Option to add new email or phone
- Inline validation

After buyer edits and approves, call `GET /v2/checkout/orders/{order_id}` to retrieve the **latest** contact info — the updated values appear in `purchase_units[].shipping`.

### RETAIN_CONTACT_INFO: edge cases

- Pass only email → PayPal shows only email (assumes phone not needed)
- Pass only phone → PayPal shows only phone
- Pass neither → falls back silently to `NO_CONTACT_INFO`

### Primary use case

Gift orders — buyer wants to provide a recipient's contact details rather than their own account details.

### Granular edit control

Individual field editing (e.g. email-only editable, phone read-only) is **not supported** — `UPDATE_CONTACT_INFO` makes both email and phone editable.

## Images

- `raw/assets/paypal-contact-module-add-email.png` — buyer flow for adding a new email during checkout
- `raw/assets/paypal-contact-module-select-phone.png` — buyer flow for selecting a phone number during checkout

## Raw Sources

- [[paypal-checkout-contact-module]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration (contact_preference is set in Create Order)
