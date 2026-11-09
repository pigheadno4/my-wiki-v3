---
title: "Stripe — Protect Yourself From Card Testing"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/prevention/card-testing"
raw_files:
  - "stripe-disputes-prevention-card-testing-2026-11-07.md"
  - "stripe-disputes-card-testing-2026.md"
tags: [stripe, card-testing, fraud, carding, captcha, rate-limiting, radar, disputes]
---

## Overview

Stripe's card-testing prevention guide describes how stolen or enumerated card details can be tested through card setup or small payments, how to recognize possible attacks, and mitigations for integrations that save cards or make payments. The 2026-11-07 capture retains the older guide's core advice and changes the condition for Radar custom velocity rules to plan feature support. See [[stripe]] and [[disputes]]. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#How card testing works|Attack methods]]

Card testing is also called carding, account testing, enumeration, or card checking. The November capture additionally notes the Japanese term “credit master (クレジットマスター)” or クレマス. Card setup validations often do not appear on cardholder statements; small payment attempts may be less noticeable. The guide describes possible early fraud warnings/disputes, higher decline rates, fees that depend on pricing and disputes, infrastructure strain, monitoring-program exposure, and distorted business data—not inevitable results for every attack. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Card testing consequences|Consequences]]

## Recognition and response

Stripe lists spikes in failed or blocked payments, HTTP 402 errors or `generic_decline` outcomes, and suspicious low-value payments with odd names or emails as symptoms to investigate. These signals are diagnostic clues, not proof that any individual failure or decline is card testing. For an integration being exploited, the guide recommends identifying activity, refunding fraudulent payments to avoid disputes, using a recommended integration or adding controls, and monitoring whether the controls work. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Identify card testing|Identification]] [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Active card testing checklist|Checklist]]

## Mitigations and conditions

- **Recommended integrations:** The guide says the latest Payment Element or Checkout has automated and manual card-testing controls, including rate limiters, AI models and CAPTCHA triggers; payments blocked by Stripe can carry `Blocked by Stripe`. Their effectiveness depends on integration and supplied risk factors. Advanced fraud detection has the highest impact in its list, followed by IP address, customer email, customer name and billing address. Direct integrations might need to pass data explicitly. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Use a Stripe-recommended integration|Integration and factors]]
- **Implementation controls:** For endpoints that save a card or make a payment, consider server-validated CAPTCHA, login or session checks, network and checkout-flow rate limits, and monitoring of cards per account, customers per IP, purchases or other anomalous patterns. The guide's one-IP-per-day limit and CAPTCHA-after-first-attempt flow are examples, not fixed universal thresholds. A single IP heuristic or firewall rule is generally insufficient. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Control implementation|Control sections]]
- **Radar velocity rules:** The 2026-05-10 capture names Radar for Fraud Teams for custom rules. The 2026-11-07 capture says custom Radar rules can be used **if the merchant's plan supports the feature**, at both its anomaly-control and risk-appetite sections. It does not identify all qualifying plans or prove any plan changed eligibility. Check feature support before relying on custom rules; this is distinct from the guide's general card-testing controls. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Detect and prevent unusual behavior|Conditional custom rules]] [[raw/stripe-disputes-card-testing-2026#Detect and prevent unusual behavior|Older wording]]
- **Keys, retries, and monitoring:** Keep secret keys private; leaked credentials can let card testers create payments or set up cards. Extreme spikes of low-success payment retries can resemble card testing; avoid retrying cards set up on fraudulent customers after an attack. The guide says Stripe Smart Retries takes this into consideration, not that it makes all retries safe. Combine controls while watching for impact on legitimate traffic. [[raw/stripe-disputes-prevention-card-testing-2026-11-07#Retry carefully|Retry guidance]]

These are mitigation recommendations from dated documentation. They do not establish a compliance requirement, current account entitlement, guaranteed attack prevention, or successful payment outcomes.

## Related

- [[disputes]] — card-testing context and dispute effects
- [[stripe-radar]] — Radar context; consult its own sources for plan and rule details
- [[source-stripe-disputes-fraud-types]] — fraud-type overview

## Raw Sources

- [[raw/stripe-disputes-prevention-card-testing-2026-11-07|Stripe card-testing prevention guide, captured 2026-11-07]]
- [[raw/stripe-disputes-card-testing-2026|Stripe card-testing prevention guide, captured 2026-05-10]]
