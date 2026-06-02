---
title: "Stripe — Radar Supported Attributes"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-rules-supported-attributes-2026.md"
tags: [stripe, radar, rules, attributes, reference, velocity, fingerprint, ip, email, distance, platform]
---

## Summary

Complete reference of all Radar rule attributes across 5 categories. 827-line reference — consult raw file for full attribute list.

## Attribute Categories

| Category | Applies to |
| --- | --- |
| Transaction rule attributes | All Radar-screened payment methods |
| Cross-payment-method attributes | Multiple payment methods (cards + ACH + SEPA) |
| Payment method–specific attributes | Single payment method only |
| Payment outcome counters | Authorized/blocked/declined tracking |
| Platform attributes | Connect platforms only |

## Notable Transaction Attributes

**Risk**: `risk_level` (normal/elevated/highest/not_assessed), `risk_score` (0-100)

**Amount**: `amount_in_xyz` (auto-converts; 32 supported currencies; uses base unit not sub-units)

**IP**: `ip_address`, `ip_country`, `ip_state`, `ip_address_connection_type`, `is_anonymous_ip`, `is_my_login_ip`

**Email**: `email`, `email_domain`, `is_disposable_email`, `email_commonality` (common/uncommon/rare, early access)

**Distance** (km): `distance_between_billing_and_shipping_address`, `distance_between_ip_and_billing_address`, `distance_between_ip_and_shipping_address`

**Disputes**: `dispute_count_on_ip_hourly/daily/weekly/all_time` (bounded ≤25)

**Time**: `seconds/minutes/hours_since_email_first_seen`, `..._on_stripe` (Stripe global), `..._on_transactions` variants

**Payment details**: `payment_method_type`, `currency`, `charge_description`, `is_checkout`, `is_off_session`, `is_recurring`, `is_setup_intent`, `destination`

**Client**: `browser`, `isp`, `operating_system`, `user_agent`

**Customer**: `customer`, `hours_since_customer_was_created`, `total_customers_for_email_weekly/yearly`, `total_customers_with_prior_fraud_activity_for_email_*`

## Cross-Payment-Method Fingerprint Attributes

Applies to cards, ACH, and SEPA: `authorized/blocked/declined_transactions_per_payment_instrument_fingerprint_hourly/daily/weekly`, `average_usd_amount_attempted_on_payment_instrument_fingerprint_all_time`, `hours_since_per_payment_instrument_fingerprint_first_seen`

## Crypto Attributes (Early Access)

`crypto_fingerprint`, `crypto_payins_network`, `crypto_payins_token_currency`

## Related Pages

- [[stripe-radar]] — concept page
- [[source-stripe-radar-rules-reference]] — attribute types and operators
- [[source-stripe-radar-rules]] — how to build rules using these attributes

## Raw Sources

- [[stripe-radar-rules-supported-attributes-2026]] — verbatim supported attributes reference (827 lines)
