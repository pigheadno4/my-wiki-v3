---
title: "Stripe Industry Metadata"
type: concept
category: technology
tags: [stripe, industry-metadata, car-rental, lodging, flight, travel, klarna, payment-intents, mcc, preview]
---

## Overview

Industry metadata is a PaymentIntents API feature (public preview, API version `2025-11-17.preview`) for passing structured travel and entertainment transaction data. It serves two purposes: compliance with card network requirements for specific MCCs, and improved authorization rates/risk assessment for Klarna.

**Mutually exclusive with [[stripe-payment-line-items]]** — cannot send both on the same PaymentIntent.

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

Can be passed at create, update, confirm, or capture. **Immutable after capture.** Each update is a full hash replacement.

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
