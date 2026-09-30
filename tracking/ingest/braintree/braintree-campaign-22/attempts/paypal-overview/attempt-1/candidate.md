---
title: "Braintree PayPal Overview"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/overview"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/overview-2026-09-16.md"
tags: [braintree, paypal, payment-methods, checkout, vaulting, recurring-payments]
---

## Overview

This collected Braintree article is the provider-specific orientation for accepting PayPal alongside cards through a Braintree integration. It routes merchants among One-Time Payments, Vaulted Payments and Recurring Payments, then states merchant and customer availability boundaries, pricing ownership, dispute-management routes and sandbox-testing options; linked implementation pages remain separate authorities.

## Key takeaways

- The article describes a Braintree checkout in which customers select a Braintree-specific PayPal button and enter PayPal credentials in a new window or lightbox without leaving the merchant's checkout page. It routes most purchases to One-Time Payments, low-value future transactions to Vaulted Payments, and subscriptions or automated billing to Recurring Payments.
- The article states that the next generation of all three named PayPal flows is currently available only in the United States. Separately, it says PayPal acceptance requires Braintree Direct, that gateway-only accounts are ineligible, and that the latest client SDKs can integrate PayPal in countries where Braintree is available. These statements have different scope and must not be collapsed into universal merchant eligibility.
- For eligible Braintree merchants, the article says customers may transact from any country. The transaction uses the currency of the merchant account selected at creation, or the default merchant account when none is specified.
- Braintree says it adds no processing fee for PayPal transactions; the applicable rates come from the merchant's PayPal merchant account, and service fees are stated as incompatible. PayPal disputes can be managed through the Braintree Control Panel or PayPal Resolution Center, but Control Panel handling requires a full PayPal integration and selection of that feature.
- The sandbox section offers either Braintree's default PayPal testing mock or a linked PayPal sandbox for end-to-end testing. This is a testing route, not proof of production enablement or transaction acceptance.

## Evidence boundaries

> [!warning] Availability is qualified
> Preserve the article's separate subjects: next-generation One-Time, Vaulted and Recurring Payments are stated as US-only; client-SDK integration is stated for countries where Braintree is available; and customer-country reach applies only to eligible Braintree merchants. The collected snapshot does not establish current enablement for a particular merchant.

> [!warning] Provider and implementation scope
> This is a Braintree PayPal payment-method overview. Its navigation links do not establish the implementation behavior of any particular SDK, version or linked guide, and its statements should not be generalized to direct PayPal Orders API integrations.

## Detail locators

- Checkout presentation and selection among One-Time, Vaulted and Recurring Payments: `# Overview`, lines 16-18.
- Next-generation US-only note, Braintree Direct prerequisite, gateway-only ineligibility and client-SDK country scope: `# Overview`, lines 21-28.
- Eligible-merchant customer-country reach and merchant-account currency selection: `## Customer availability`, line 33.
- PayPal pricing ownership, service-fee incompatibility and dispute-management qualifications: `### Fees` through `### Disputes`, lines 39-46.
- Mock versus linked-sandbox testing routes: `## Testing in the sandbox`, lines 49-51.

## Related

- Company: [[braintree]]
- Main payment-method route: [[braintree-payment-methods]]
- Braintree-to-PayPal integration boundary: [[paypal-braintree-integration]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal Overview article]] - complete collected overview covering PayPal flow selection, availability, pricing, disputes and sandbox routes
