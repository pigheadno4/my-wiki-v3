---
title: "Braintree Data Shared with PayPal"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/shared-data"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/shared-data-2026-09-16.md"
tags: [braintree, paypal, data-sharing, merchant-account, account-linking, consent]
---

## Overview

This collected Braintree article enumerates information that Braintree says it shares with PayPal to create and/or link a merchant's PayPal account. It records TLS/SSL transport encryption and identifies contact, business-entity, account-credential, consent and approved-volume categories; it does not establish current operational behavior, merchant eligibility, data retention, PayPal's downstream use or the legal mechanism for consent.

## Key takeaways

- The article limits its stated purpose to creating and/or linking a merchant's PayPal account and says the shared data is encrypted and sent to PayPal using TLS/SSL. It does not describe storage, retention, access controls or downstream processing.
- Primary business contact information includes name and title plus sensitive identity data: date of birth, SSN and residential address.
- Business entity information includes address, business description, phone number, business type, tax ID number, website URL and average monthly PayPal payment volume.
- The article lists PayPal account credentials as username and password. It does not state how those credentials are collected, stored or subsequently used.
- The final listed items are "Legal Agreement Consent on Merchant's Behalf" and "Annual Approved Volume." The article does not identify the agreement, define the consent scope, explain who supplied or captured consent, or state that Braintree has general authority to consent for merchants.

## Evidence boundaries

> [!warning] Data inventory is not consent authority
> Treat the page as a snapshot of categories Braintree says it shares for merchant PayPal-account creation or linking. Its "Legal Agreement Consent on Merchant's Behalf" label does not by itself establish which agreement applies, a merchant's present consent, Braintree's authority, or any use outside that stated account purpose.

> [!warning] Transport encryption is not a complete data-protection claim
> The article states that data is encrypted and sent using TLS/SSL. It does not document encryption at rest, credential-handling design, retention, deletion, access, PayPal's downstream processing or compliance status.

## Detail locators

- Sharing purpose and TLS/SSL transport statement: `# Braintree Data Shared with PayPal`, line 16.
- Primary business contact and sensitive identity-data categories: lines 19-22.
- Business entity and stated volume categories: lines 25-32.
- PayPal account credentials, legal-agreement-consent label and annual approved volume: lines 35-41.

## Related

- Company: [[braintree]]
- Main integration boundary: [[paypal-braintree-integration]]
- Payment-method context: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/shared-data-2026-09-16|Braintree Data Shared with PayPal article]] - complete collected page covering the stated account-linking purpose, TLS/SSL transport and listed data categories
