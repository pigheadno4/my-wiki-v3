---
title: "PayPal Disputes Overview"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-disputes-overview-2025.md"
  - "paypal-disputes-choose-integration-2025.md"
  - "paypal-disputes-setup-2025.md"
  - "paypal-disputes-resolution-center-2025.md"
tags: [paypal, disputes, chargebacks, ach-return, resolution-center, disputes-api]
---

## Summary

Overview of PayPal's dispute management system for direct merchants and connected integrations. Covers internal and external disputes, the 3-stage lifecycle, and workflow diagrams for both dispute types.

## Key Takeaways

- **Two integration options**: Resolution Center (no-code web UI) or Disputes API (programmatic automation)
- **Internal vs external**: Internal = buyer files via PayPal Resolution Center; external = buyer files with bank/card issuer
- **180-day window**: Buyer has 180 days from payment date to dispute a transaction
- **Amicable resolution**: 20 days for buyer/merchant to resolve directly; if escalated, PayPal adjudicates within 10 days
- **Pre-chargeback alert**: Merchant has 20 hours to issue a refund and avoid the chargeback + fees
- **ACH return**: Bank requests PayPal to reverse a payment (distinct from card chargeback)
- Both merchants and buyers can **appeal** unfavorable decisions

## Parties Involved

| Party | Role |
| --- | --- |
| Buyer | Initiates the dispute |
| Merchant | Monitors and responds to disputes |
| PayPal | Facilitates resolution; adjudicates internal claims |
| Bank / card issuer | Manages and adjudicates external chargebacks and ACH returns |
| Card network | Sets rules and timelines (Visa, Mastercard, Amex, etc.) |
| Partner | Platform in connected integration; merchants assume financial liability |

## Dispute Types

### Internal disputes

- Filed via PayPal Resolution Center (or chatbot, IVR, customer support)
- PayPal holds disputed payment until resolution
- Lifecycle: inquiry (20 days amicable) → claim (PayPal adjudicates in 10 days) → resolution
- INR and SNAD start at inquiry stage; billing errors and unauthorized transactions go directly to claim

### External disputes

- Filed with buyer's bank or card issuer
- **Chargeback**: card issuer reverses payment; pre-chargeback alert gives merchant 20 hours to refund
- **ACH return**: bank requests PayPal to reverse a payment
- PayPal acts as intermediary — bank/card issuer adjudicates

## Dispute Lifecycle (3 Stages)

1. **Inquiry**: Buyer files dispute; 20 days for direct resolution
2. **Claim**: Escalated case; PayPal (internal) or bank (external) requests evidence and adjudicates
3. **Resolution**: Decision communicated; either party may appeal

## Common Buyer Issues (6 Types)

| Issue | Description |
| --- | --- |
| INR (Item not received) | Ordered and paid but not received |
| SNAD (Significantly not as described) | Item received but doesn't match description or damaged in shipping |
| Billing/subscription errors | Duplicate charges, multiple transactions, incorrect amounts |
| Unauthorized transactions | No consent; card fraud or identity theft |
| Request for additional details | Buyer needs transaction copy or receipt |
| Misdirected transactions | Payment sent to wrong recipient or account |

## Workflow Diagrams

Internal dispute flow:
![Internal disputes workflow](../raw/assets/paypal-disputes-internal-flow.png)

External dispute flow:
![External disputes workflow](../raw/assets/paypal-disputes-external-flow.png)

## Related Pages

- [[paypal]] — company page
- [[disputes]] — disputes & chargebacks concept page
- [[source-paypal-disputes-api]] — Disputes API guide (endpoints, lifecycle stages, evidence, webhooks)

## Raw Sources

- [[paypal-disputes-overview-2025]] — verbatim disputes overview page from docs.paypal.ai
- [[paypal-disputes-choose-integration-2025]] — Resolution Center vs Disputes API decision table: low-volume/no-code vs high-volume/automated
- [[paypal-disputes-resolution-center-2025]] — Resolution Center guide: 9 actions (view, message buyer, offer: partial/replacement/full-with-return, escalate, accept claim, provide evidence, provide supporting info, appeal); escalation = no more buyer messaging + prior offers on hold; partners cannot access RC
- [[paypal-disputes-setup-2025]] — Setup guide: sandbox (personal=buyer, business=handler); API: enable Customer disputes feature; buyer-side credentials for test simulation (DISPUTE_CREATE + UPDATE_BUYER scopes, Log in with PayPal consent, PayPal-Auth-Assertion JWT header); live API: DOCUMENTS_DISPUTES_DOWNLOAD scope for evidence download; partners: contact PayPal for connected integration
