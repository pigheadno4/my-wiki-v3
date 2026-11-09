---
title: "Stripe — Industry Metadata"
type: source
date_ingested: 2026-11-09
canonical_url: https://docs.stripe.com/industry-metadata
original_format: webpage
raw_files:
  - "stripe-industry-metadata-2026-11-07.md"
  - "stripe-industry-metadata-2026.md"
tags: [stripe, industry-metadata, car-rental, lodging, flight, travel, klarna, payment-intents, mcc, preview]
---

## Summary

Industry metadata is structured travel and entertainment transaction data passed through the Payment Intents API. For supported merchant category codes, supplying relevant data is required for card-network compliance. On Klarna transactions it **might** improve authorization rates and risk assessment; neither benefit nor card-network qualification follows automatically from supplying data.

The 2026-11-07 guide documents API preview header `2026-07-29.preview` or a later preview version. The retained 2026-05-11 guide documented `2025-11-17.preview` or later. This is a documentation change, with no captured runtime test showing whether the older header is rejected. Cards remain **private preview** and Klarna **public preview**; the public-preview header does not open card access. Flight data for cards needs feature enablement from an account team or Stripe support, and cruise data is unsupported for cards.

> [!warning] Contradiction
> The 2026-05-11 capture specifies `2025-11-17.preview` and `total.tax.taxes[]`; the 2026-11-07 capture specifies `2026-07-29.preview` and `total.tax.tax_items[]`. Use the new documented fields for this capture, retain the older spelling for historical integrations, and verify actual account/API behavior before a migration decision.

## Eligible MCCs and payment methods

| Vertical | MCCs |
| --- | --- |
| Car rental | 3351–3441, 7512, 7513, 7519 |
| Lodging | 3501–3999, 7011 |
| Travel agency | 4722 |
| Flight | 4511 |

The guide names Visa, Mastercard, Amex, Discover, and Klarna. Klarna also supports events, standalone insurance, train/bus/ferry transport, organized trips and tours, vouchers, and marketplace sellers; those additional verticals are not card-payment support.

## PaymentIntent structure and timing

`payment_details` contains arrays of car rental, lodging, and flight records: `car_rental_data[]`, `lodging_data[]`, and `flight_data[]`. The guide documents it on PaymentIntent create, update, confirm, and capture. Each update **replaces the entire `payment_details` hash** and must remain valid for the payment method. Metadata cannot be changed after capture. The manual confirmation/capture examples illustrate possible points of update; the guide also allows automatic confirmation or capture use cases.

For cards, only the **first entry of each vertical's array** reaches the card networks; use separate PaymentIntents for multiple card bookings when each needs network data. Klarna processes **all entries** in each array for its risk and authorization decisions. Card-only fields are not sent to Klarna, Klarna-only fields are not seen by card networks, and unsupported payment-method-specific properties are ignored. Some property lengths may be truncated to fit a payment method.

## Required fields by vertical

| Vertical | Minimum for all supported payment methods | Additional card fields |
| --- | --- | --- |
| Car rental | Pickup and drop-off address line1, city, postal code, country and time; `total.amount` | State where applicable for each address; booking number, days rented, customer-service phone, renter name, vehicle type/make/model |
| Lodging | `checkin_at`, `checkout_at`, `total.amount` excluding taxes and fees | Booking number, fire-safety indicator, customer-service phone, accommodation nights and daily rate |
| Flight | At least one segment with service class, carrier code, departure airport/time, arrival airport; `total.amount` excluding taxes and fees | Each segment's carrier name, flight number, ticket number, and arrival time |

State codes must be valid for their country where required. Flight card data requires separate feature enablement. Optional arrays can create conditional requirements: each supplied passenger needs a name; supplied car-rental distance needs amount and unit; each supplied Klarna driver or guest needs a name; supplied driver date of birth, lodging host address, or insurance entry requires its specified component fields. Consult the full field tables for validation limits and per-method fields.

## Tax path and phone format in the 2026-11-07 capture

For car rental, lodging, and flight, the new field tables and create/confirm/capture examples use `payment_details[<vertical>][0][total][tax][tax_items][0]` (`total.tax.tax_items[]`) for rate, amount, and type. The 2026-05-11 tables and examples used `total.tax.taxes[]`. The captures do not establish whether `taxes[]` is rejected, aliased, or still accepted by an older preview version.

Card car-rental and lodging `customer_service_phone_number` fields are required. Lodging `host.property_phone_number` is an additional field. The new guide says live-mode values for these fields must be valid E.164 phone numbers: non-US numbers begin with `+` and country code; if a US number begins with `+`, it uses country code `1` followed by ten digits. All zeros (`0000000000`) remain a sandbox allowance. The old guide's 'numbers only' wording is dated, not a rule to apply to the new live format.

## Examples and evidence limits

The November create examples use `automatic_payment_methods[enabled]=true` instead of the older explicit `payment_method_types[0]=card`; confirm examples add `return_url`. Sample car daily rate and lodging total/tax amounts also change. These examples do not make automatic payment methods or those amounts required for industry metadata.

Sandbox tests can check API acceptance, method-specific required fields, and PaymentIntent processing. They do **not** simulate card-network interchange qualification or Klarna authorization/risk outcomes. Neither capture tests account-specific enablement, older-header rejection, or tax-field aliasing.

The two industry-metadata captures do not discuss payment line items. A separate 2026-05-11 [[source-stripe-payment-line-items]] guide explicitly says card line items cannot be sent alongside car-rental, lodging, or airline industry metadata, and gives PayPal the same restriction ([[raw/stripe-payment-line-items-2026|dated payment-line-items raw]], line 26). Its Klarna column separately refers to Extra Merchant Data in private preview; that does not establish a universal rule for Klarna or current availability. Treat this as a dated, payment-method-scoped restriction and verify current account/version behavior before implementation.

## Related Pages

- [[stripe-industry-metadata]] — industry metadata concept
- [[stripe-payment-intents]] — PaymentIntent lifecycle
- [[stripe-payment-line-items]] — separate line-item feature; the dated card/PayPal incompatibility is documented in [[source-stripe-payment-line-items]]
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-industry-metadata-2026-11-07|2026-11-07 industry metadata guide]] — current captured preview wording, tax item path, field tables, examples, and testing limits
- [[raw/stripe-industry-metadata-2026|2026-05-11 industry metadata guide]] — earlier preview wording, `taxes[]` path, and dated examples
