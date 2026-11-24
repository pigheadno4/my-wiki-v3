---
title: "Stripe — Radar Supported Attributes"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/rules/supported-attributes"
raw_files:
  - "stripe-radar-rules-supported-attributes-2026-11-07.md"
  - "stripe-radar-rules-supported-attributes-2026.md"
tags: [stripe, radar, rules, attributes, reference, velocity, fingerprint, ip, email, distance, platform]
---

## Summary

Stripe’s May 10 and November 7, 2026 captures catalog the signals merchants can use in Radar rules. Stripe evaluates each rule with the inputs available for the payment method, transaction or connected account. Consult the dated raw tables for attribute names, windows and applicability.

## Attribute Categories

| Category | Applies to |
| --- | --- |
| Transaction rule attributes | All Radar-screened payment methods, with constraints on individual attributes |
| Cross-payment-method attributes | Shared by multiple methods, with applicability varying by attribute |
| Payment method–specific attributes | Single payment method only. Non-Boolean attributes are missing for other methods. |
| Payment outcome counters | Authorization, block, decline and total. Charge counters use card charges, and transaction counters cover supported methods with setup-attempt scope specified by row. |
| Platform attributes | Connect platforms, with separate transaction, account and November Treasury scopes |

## Notable Transaction Attributes

**Risk.** November recommends three 0–99 rule scores. `fraudulent_dispute_score` applies to cards, ACH Direct Debit and SEPA Direct Debit. `fraudulent_payment_score` and `early_fraud_warning_score` apply to cards only. Classic `risk_level` (normal, elevated, highest, not_assessed) and `risk_score` remain supported. Both captures give adjustable classic thresholds of 65 for elevated and 75 for highest.

> **Classic risk range and rule retirement (2026-11-07).** Both Supported Attributes captures list the classic `risk_score` rule attribute as 0–100. The separate November Risk Settings capture describes the classic model as 0–99, says selecting a risk setting disables the default high-risk block rule, and still documents custom `:risk_score:` rules. Whether the model emits 100 remains unresolved. See [[source-stripe-radar-risk-settings]] and its November raw lines 141–156.

**Amount.** `amount_in_xyz` auto-converts using the explicit currency list (May raw line 60, November line 66). Decimal currencies use base units, such as dollars.

**IP and client.** See `ip_address`, `ip_country`, `ip_state`, `ip_address_connection_type`, `is_anonymous_ip` and `is_my_login_ip`, plus `browser`, `isp`, `operating_system` and `user_agent`. November says iCloud Private Relay users can share the same IP counters. It suggests using `isp` to identify the traffic and considering exclusion from rules.

**Email, distance and time.** `email`, `email_domain`, `is_disposable_email` and `email_commonality` (common, uncommon, rare, early access). Distance predicates measure billing, shipping and IP distances in km. `dispute_count_on_ip_hourly/daily/weekly/all_time` is bounded at 25. See `seconds/minutes/hours_since_email_first_seen` and the Stripe-wide and transaction variants.

**Payment details.** See `payment_method_type`, `currency`, `charge_description`, `is_checkout`, `is_off_session`, `is_recurring`, `is_setup_intent` and `destination`. November adds `is_free_trial_transaction` for transactions Stripe identifies as coming from a free trial, primarily through Checkout or Billing. Both captures deprecate the payment `transaction_type` predicate, recommend `is_setup_intent` where possible, and reserve the `payment_intent` value for Request Credentials rules.

> **Bacs rule example and enum (2026-05-10 and 2026-11-07).** The May and November Supported Attributes enum rows list `card`, `sepa_debit` and `us_bank_account`. The dated examples in [[source-stripe-radar-supported-payment-methods]] use `bacs_debit` in `:payment_method_type:`. The documentation leaves parser acceptance and entitlement for Bacs unresolved. See the May and November Attributes raw lines 166 and 170 and the paired Supported Payment Methods raw lines 46–48 and 43–45.

**Customers.** See `customer`, `hours_since_customer_was_created`, `total_customers_for_email_weekly/yearly` and `total_customers_with_prior_fraud_activity_for_email_*`. Both captures describe Accounts v2 as generally available for Connect users and in public preview for other Stripe users. Preview users must specify a preview version. November gives the Dashboard enrollment route through **Account previews and features** → **Reusable payment methods for Global Payouts**. The dated captures recommend customer-configured Account objects for most use cases.

May includes 12 yearly transaction counters for customers, emails, cards and names. November omits those rows while retaining shorter transaction windows and separately scoped yearly counters. Whether the omitted predicates still evaluate remains unresolved. See the May **Customers**, **Email usage**, **Card usage** and **Name** tables.

## Cross-Payment-Method Fingerprint Attributes

Applies to cards, ACH and SEPA. See `authorized/blocked/declined_transactions_per_payment_instrument_fingerprint_hourly/daily/weekly`, `average_usd_amount_attempted_on_payment_instrument_fingerprint_all_time` and `hours_since_per_payment_instrument_fingerprint_first_seen`.

## Card and Radar Pro Attributes

- Card issuer address and CVC checks run after authorization. The `card_description`, `card_issuer` and `card_3d_secure_result` inputs remain public preview in both captures.
- `has_liability_shift` is approximate. May starts from a non-wallet card payment’s preauthorization liability shift and allows false negatives for certain digital wallets. November describes preauthorization card liability shift, possible later downgrade under network rules and false negatives for some Google Pay payments.
- November adds `network_token` to `digital_wallet`. In both captures the listed values require a registered-device cryptogram, with `android_pay` valid with or without one. November also adds `is_agent_initiated` for card payments Stripe identifies as initiated by an AI agent.
- November’s Radar Pro table lists 0–99 `bot_score` and the `free_trial_abuse_risk_level` and `refund_abuse_risk_level` predicates for cards only. `name_verification` compares the supplied cardholder name with names inferred by Stripe, with separate match, unavailable and not-provided outcomes. The November Bot Abuse guide names Stripe Checkout, Custom Checkout, Radar Sessions and Web Elements for bot scoring. See [[source-stripe-radar-bot-abuse]] and its November raw lines 11–17.

## Crypto Attributes (Early Access)

`crypto_fingerprint`, `crypto_payins_network`, `crypto_payins_token_currency`

## Connect and Treasury Rules

- **Transaction rules** can review, block or allow connected-account transactions. May names destination charges and separate charges and transfers, and requires Radar for Platforms access for direct charges. November lists all three charge types under charge-type and Radar-tier conditions. The November Risk Settings guide describes merchant-of-record scope and the platform controls that determine whose Radar rules apply to connected-account direct charges. See [[source-stripe-radar-risk-settings]] and its November raw lines 158–186.
- **Account rules** can submit the connected account itself for review. May restricts them to Radar for Platforms and lists `account_risk_level`. November makes availability tier-dependent and lists `account_fraud_risk_level` and `account_fraud_risk_score`. Coexistence of these names, automatic migration and exact entitlement changes remain unresolved.
- **Treasury transaction rules** are a November private preview for certain Radar plans. They can review or block connected-account Treasury transactions and list `account_risk_level` in this scope. The Treasury `transaction_type` values are `INBOUND_TRANSFER` and `RECEIVED_CREDIT`, with separate inbound and return aggregates in the raw.

> **Counter descriptions (2026-05-10 and 2026-11-07).** In both captures `refund_count_on_card_all_time` refers to a billing address while companion windows refer to a card. In both platform rule tables, the daily disputed-dollar row describes the past week, and the monthly and weekly refunded-dollar rows both describe the past day. The actual counting entity and windows remain unresolved. See May raw lines 399–402, 696, 716–718, 780 and 806–808, and November raw lines 408–411, 706, 726–728, 791 and 817–819.

## Related Pages

- [[stripe]] — company page
- [[stripe-radar]] — concept page
- [[source-stripe-radar-rules-reference]] — attribute types and operators
- [[source-stripe-radar-rules]] — how to build rules using these attributes

## Raw Sources

- [[raw/stripe-radar-rules-supported-attributes-2026-11-07|November 7, 2026 Supported Attributes reference]]
- [[stripe-radar-rules-supported-attributes-2026]] — May 10, 2026 verbatim supported attributes reference (827 lines)
