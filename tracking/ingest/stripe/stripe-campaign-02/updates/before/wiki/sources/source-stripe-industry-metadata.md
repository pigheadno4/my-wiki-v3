---
title: "Stripe — Industry Metadata"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-industry-metadata-2026.md"
tags: [stripe, industry-metadata, car-rental, lodging, flight, travel, klarna, payment-intents, mcc, preview]
---

## Summary

Public preview feature (API version `2025-11-17.preview`) for passing industry-specific T&E data on PaymentIntents. Required for compliance with card network requirements for certain MCCs; also improves Klarna authorization rates and risk assessment. Cards are in **private preview** (needs account enablement); Klarna is in public preview.

**Mutually exclusive with payment line items** — cannot send both on the same PaymentIntent.

## Eligible MCCs

| Vertical | MCCs |
| --- | --- |
| Car Rental | 3351–3441, 7512, 7513, 7519 |
| Lodging | 3501–3999, 7011 |
| Travel Agency | 4722 |
| Flight | 4511 |

Cards supported: Visa, Mastercard, Amex, Discover.

## API Structure

Data passes in `payment_details` on create/update/confirm/capture:

```
payment_details.car_rental_data[]   — array of car rental hashes
payment_details.lodging_data[]      — array of lodging hashes
payment_details.flight_data[]       — array of flight hashes
```

**Critical**: Cards send only `[0]` (first entry) of each array — additional entries are ignored. For multiple card bookings, create separate PaymentIntents. Klarna processes all entries.

`payment_details` is a full hash replacement on each update. Cannot be modified after capture.

## Required Fields by Vertical

### Car Rental (`car_rental_data`)

**All payment methods**: pickup address (line1, city, postal_code, country), pickup.time, drop_off address (same fields), drop_off.time, total.amount

**Cards additionally**: pickup/drop_off state (when country has states), booking_number, days_rented, customer_service_phone_number, renter_name, vehicle.type, vehicle.make, vehicle.model

### Lodging (`lodging_data`)

**All payment methods**: checkin_at, checkout_at, total.amount (excl. taxes/fees)

**Cards additionally**: booking_number, fire_safety_act_compliance_indicator, customer_service_phone_number, accommodation.nights, accommodation.daily_rate_amount

### Flight (`flight_data`)

**All payment methods**: segments[] with service_class, carrier_code (2-char IATA), departure.airport (3-char IATA), departure.departs_at, arrival.airport; total.amount (excl. taxes/fees)

**Cards additionally**: segments[].carrier_name, segments[].flight_number, segments[].ticket_number, segments[].arrival.arrives_at

## Card-Only vs Klarna-Only Fields

**Card-only** (additional compliance fields): booking_number, renter/guest details, vehicle specifics, fire_safety_act_compliance_indicator, distance, computerized_reservation_system, etc.

**Klarna-only** (risk assessment fields): drivers[].name/date_of_birth, guests[].name, host address, insurances[], booking_number (flights), departure/arrival city+country per segment

## Klarna-Exclusive Verticals

Not available for card payments:
- Events (concerts, festivals, sports, conferences)
- Insurance (standalone policies)
- Train, bus, ferry transportation
- Organized trips and tours
- Vouchers
- Marketplace sellers

See [Klarna supplementary purchase data](https://docs.stripe.com/payments/klarna/supplementary-purchase-data.md) for these additional verticals.

## Notes

- Phone numbers: numbers only; non-US must start with `+`; sandbox accepts all zeros
- Timestamps: seconds since Unix epoch; must be within ±2 years
- State fields: conditional on country (required when country uses states)
- Property lengths may be truncated to comply with payment method requirements
- Sandbox testing does not simulate card network interchange qualification or Klarna auth rate outcomes

## Related Pages

- [[stripe-industry-metadata]] — concept page
- [[stripe-payment-line-items]] — mutually exclusive feature (line items vs industry metadata)

## Raw Sources

- [[stripe-industry-metadata-2026]] — verbatim industry metadata guide (1,055 lines)
