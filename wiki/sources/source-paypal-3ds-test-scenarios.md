---
title: "PayPal 3D Secure: Test Scenarios"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-3ds-test-scenarios.md"
tags: [paypal, 3d-secure, sandbox, test-cards, testing, purchase-flow, save-payment-methods, visa, mastercard, amex]
---

## PayPal 3D Secure: Test Scenarios

Complete sandbox test card reference for 3D Secure testing — purchase flows across 10 countries and Save payment methods flows (Payment Method Tokens v3 API).

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/test/>

Last updated: 2025-10-29

## Key Takeaways

### Two separate test card sets — do not mix

| Use case | Cards to use | API |
| -------- | ------------ | --- |
| Purchase flows | Country-specific cards (US, GB, CN, AU, FR, DE, IT, JP, MX, ES) | Orders v2 API |
| Save payment methods | `4000000000002701`-style cards | Payment Method Tokens v3 API |

### Purchase flow — 9 standard test scenarios

All 10 countries have the same 9 scenarios:

| # | Scenario | enrollment | auth | liability_shift |
| - | -------- | ---------- | ---- | --------------- |
| 1 | Successful Frictionless | Y | Y | POSSIBLE |
| 2 | Failed Frictionless | Y | N | NO |
| 3 | Attempts Stand-In Frictionless | Y | A | POSSIBLE |
| 4 | Unavailable Frictionless | Y | U | NO |
| 5 | Rejected Frictionless | Y | R | NO |
| 6 | Auth Not Available on Lookup | U | — | NO |
| 7 | Successful Step-up | Y | Y | POSSIBLE |
| 8 | Failed Step-Up | Y | N | NO |
| 9 | Step-Up Unavailable | Y | U | NO |

### Purchase flow — quick Visa card lookup by scenario

| Test # | US Visa | GB Visa | FR Visa | DE Visa |
| ------ | ------- | ------- | ------- | ------- |
| 1 (success) | 4868719196829038 | 4462603042343024 | 4147044347484424 | 4779131010696190 |
| 2 (fail) | 4868719158130060 | 4462603045503384 | 4147044332973480 | 4779131029887282 |
| 7 (step-up success) | 4868719166101368 | 4462603040971339 | 4147044387320066 | 4779131109317713 |

### Save payment methods — 15 test scenarios

Expiration: month = 01, year = current year + 3.

| # | Scenario | API response |
| - | -------- | ------------ |
| 1 | Successful No-Challenge | authenticate_successful |
| 2 | Failed No-Challenge | authenticate_frictionless_failed |
| 3 | Attempt No-Challenge | authenticate_attempt_successful |
| 4 | Unavailable from Issuer | authenticate_unable_to_authenticate |
| 5 | Rejected by Issuer | authenticate_rejected |
| 6 | Not Available on Lookup | authentication_unavailable |
| 7 | Error on Lookup | lookup_error |
| 8 | Timeout on Lookup | lookup_failed_acs_error |
| 9 | Bypassed | lookup_bypassed |
| 10 | Successful Challenge | authenticate_successful |
| 11 | Failed Challenge | challenge_required |
| 12 | Challenge Unavailable | challenge_required |
| 13 | Error on Authentication | authenticate_error |
| 14 | Data Only (MC only) | data_only_successful |
| 15 | Authentication Unsuccessful | authenticate_rejected |

Quick save-flow Visa: `4000000000002701` (success), `4000000000002925` (fail)

### Card brands by country (purchase flows)

- **US**: Visa, Mastercard, Discover, JCB, Diners, CUP
- **GB**: Visa, Mastercard, Amex
- **CN**: CUP only
- **AU**: EFTPOS Mastercard, EFTPOS Visa (only 2 scenarios)
- **FR**: Visa, Mastercard, Carte Bancaire Visa, Carte Bancaire Mastercard, Amex
- **DE**: Visa, Mastercard
- **IT**: Visa, Mastercard, Amex
- **JP**: JCB, Visa, Mastercard, Amex, Diners
- **MX**: Visa, Mastercard
- **ES**: Visa, Mastercard, Amex

## Raw Sources

- [[paypal-3ds-test-scenarios]] — verbatim webpage content with all test card numbers for all countries

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-3ds-response-parameters]] — what each response code means
- [[source-paypal-expanded-checkout-3d-secure]] — 3DS eligibility by country
- [[source-paypal-expanded-checkout-3ds-card-fields]] — CardFields integration
- [[source-paypal-expanded-checkout-3ds-orders-api]] — Orders API integration
