---
title: "Stripe Industry Metadata"
type: concept
category: technology
tags: [stripe, industry-metadata, car-rental, lodging, flight, travel, klarna, payment-intents, mcc, preview]
---

## Overview

Industry metadata is a PaymentIntents API feature for structured travel and entertainment transaction data. The 2026-11-07 guide documents `2026-07-29.preview` or a later preview header; the 2026-05-11 capture documented `2025-11-17.preview`. Relevant data is required for card-network compliance at supported MCCs and **might** improve Klarna authorization rates or risk assessment. Cards remain private preview; Klarna is public preview.

> [!warning] Contradiction
> The two dated captures give different preview headers and tax item paths (`total.tax.taxes[]` in May, `total.tax.tax_items[]` in November). Neither capture tests whether the older version or field spelling is rejected or aliased.

[[stripe-payment-line-items]] is a separate PaymentIntent feature. Its 2026-05-11 [[source-stripe-payment-line-items]] restriction table states that card line items cannot be sent alongside car-rental, lodging, or airline industry metadata, and gives PayPal the same restriction ([[raw/stripe-payment-line-items-2026|dated line-item raw]], line 26). Its Klarna column refers to Extra Merchant Data in private preview; do not generalize the card/PayPal rule to Klarna or infer current preview access.

## Status

- **Cards**: private preview (requires account enablement via Stripe support)
- **Klarna**: public preview
- Cruise data not supported for cards

## Eligible MCCs

| Vertical | MCCs |
| --- | --- |
| Car Rental | 3351–3441, 7512, 7513, 7519 |
| Lodging | 3501–3999, 7011 |
| Travel Agency | 4722 |
| Flight | 4511 |

Card brands: Visa, Mastercard, Amex, Discover.

## API Structure

Data is sent under `payment_details` (alongside `payment_method`, etc.) using vertical-specific arrays:

- `payment_details.car_rental_data[]`
- `payment_details.lodging_data[]`
- `payment_details.flight_data[]`

Can be passed at create, update, confirm, or capture. **Immutable after capture.** Each update is a full hash replacement. In the 2026-11-07 field tables and examples, each vertical's tax entries use `total.tax.tax_items[]` (the 2026-05-11 capture used `total.tax.taxes[]`). Live card car-rental and lodging customer-service phones, and the optional lodging property phone, follow the new guide's E.164 wording; non-US numbers include `+` and country code, while all-zero values are a sandbox allowance only.

**Critical array behavior**:

- **Cards**: only the first entry (`[0]`) in each array reaches card networks — create separate PaymentIntents per booking
- **Klarna**: all array entries are processed

## Required Fields Summary

| | Car Rental | Lodging | Flight |
| --- | --- | --- | --- |
| All | pickup+dropoff address (line1/city/postal_code/country), timestamps, total.amount | checkin_at, checkout_at, total.amount | segments[].service_class, carrier_code (2-char IATA), departure+arrival airports (3-char IATA), departs_at, total.amount |
| Cards add | state, booking_number, days_rented, phone, renter_name, vehicle.type/make/model | booking_number, fire_safety_act_compliance_indicator, phone, accommodation.nights + daily_rate_amount | carrier_name, flight_number, ticket_number, arrival.arrives_at |

## Card vs Klarna Field Split

Each vertical has three field layers:
1. **General** — base fields used by all payment methods
2. **Cards-only** — compliance fields (booking numbers, vehicle/property details, GDS codes)
3. **Klarna-only** — risk assessment fields (driver/guest names, dates of birth, host details, insurance coverage)

Fields for one payment method are ignored by the other.

## Klarna-Exclusive Verticals

Klarna also supports verticals unavailable for cards:
- Events (concerts, festivals, sports, conferences)
- Insurance (standalone policies)
- Train, bus, and ferry transportation
- Organized trips and tours
- Vouchers
- Marketplace sellers

## Sources

- [[source-stripe-industry-metadata]] — full field reference, required fields per vertical, code examples for car rental/lodging/flight, multi-vertical PaymentIntent
