---
title: "Braintree 3D Secure"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/3d-secure"
raw_files:
  - "braintree/articles/guides/fraud-tools/3d-secure-2026-09-16.md"
tags: [braintree, 3d-secure, card-authentication, sca, liability-shift]
---

## Overview

This collected Braintree guide describes 3D Secure (3DS) as an additional customer-authentication step for online credit- and debit-card purchases. It explains the checkout lookup and possible issuer challenge, identifies compatibility and enrollment boundaries, and routes implementation to dedicated developer documentation.

## Key takeaways

- During checkout, Braintree performs a 3D Secure Lookup. For an enrolled cardholder, the issuing bank decides whether supplied cardholder and device data is sufficient or whether additional authentication is necessary; when it is, the Braintree SDK presents the issuer-provided dialog or iframe. The authentication mechanism varies by cardholder and issuer.
- This page limits 3DS compatibility to credit-card, debit-card and Secure Remote Commerce transactions. It says support covers most merchants in named regions, but production accounts outside the EEA are not enrolled automatically and only certain configurations are compatible. These statements do not establish eligibility for an individual merchant.
- Transaction Detail in the Control Panel exposes 3DS details and status. The linked status-code authority owns the complete status semantics; this page says the status indicates the authentication outcome and whether the authenticated transaction received a liability shift.
- Fraud-chargeback liability can shift only in certain cases. Not every 3DS transaction receives a shift, and a shift does not always trigger automatic chargeback representation; merchants still need to monitor chargebacks and complete required actions.
- To start supporting 3DS, the page directs merchants to the developer docs and then to contact Braintree to enroll. This setup route is not proof of current eligibility or enrollment.

> [!warning] Authentication is not authorization or gateway fraud decisioning
> This guide documents cardholder authentication and conditional liability-shift evidence. It does not say that a completed 3DS flow authorizes a payment, causes processor approval, replaces Braintree fraud-tool decisions, or guarantees protection from fraud chargebacks.

## Detail locators

- Authentication purpose: `# 3D Secure`, line 16.
- Lookup, issuer decision and SDK-presented challenge: `## Processing`, line 28.
- Transaction Detail visibility and status-code scope: `## Processing`, line 30.
- Payment-method, region, enrollment and configuration compatibility: `## Compatibility`, lines 35-39.
- Card-brand services and American Express SafeKey setup note: `## Compatibility > ### Card brands`, lines 44-54.
- Possible additional per-transaction fee: `## Compatibility > ### Fees`, line 61.
- Conditional liability shift and continuing merchant chargeback duties: `## Compatibility > ### Chargebacks`, lines 66-74.
- Developer-documentation and enrollment route: `## Setup`, line 81.
- Control Panel enrollment check: `## Setup > ### Confirm setup`, lines 86-95.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]
- Related concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/guides/3d-secure/overview-2026-09-16|Braintree 3D Secure developer overview]] - unread navigation-only implementation route linked by this guide
- [[raw/braintree/articles/guides/fraud-tools/overview-2026-09-16|Braintree fraud tools overview]] - unread navigation-only route; not evidence that 3DS performs gateway fraud decisioning

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/3d-secure-2026-09-16|Braintree 3D Secure article]] - complete collected guide covering authentication purpose and flow, compatibility, conditional liability shift, setup and enrollment routes
