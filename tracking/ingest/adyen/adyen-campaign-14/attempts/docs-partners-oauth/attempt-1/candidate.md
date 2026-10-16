---
title: "Adyen partner OAuth overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/oauth"
raw_files:
  - "adyen/docs/partners/oauth/2026-09-15.md"
tags: [adyen, partners, oauth, delegated-access, consent]
---

## Overview

This Adyen OAuth hub describes partner-only delegated API access: a partner application requests access to a customer account, the customer authorizes a requested scope at Adyen, and the application uses issued tokens for API calls on that customer's behalf. It is a conceptual flow and navigation page, not evidence that an app was installed, a customer consented, any scope or account was granted, or an online payment succeeded. [[adyen]] [[adyen-partner-oauth]]

## Key takeaways

- The resource owner is the partner's customer, who grants access to their account resources; the client is the partner application; Adyen APIs are the resource server; and Adyen's OAuth server authenticates the customer and issues access tokens. This customer-resource identity should not be replaced by the partner's own account or by an ordinary merchant API credential.
- The partner requests a scope and the customer confirms it. The hub says this limits resource access to what the partner needs, but it does not enumerate scopes, account identifiers, role prerequisites, test/live endpoints, or the exact returned grant. Those details belong to the linked integration and scopes references.
- The outlined sequence is **Connect with Adyen** → redirect to Adyen for customer authentication and authorization → return with an authorization code → exchange for access and refresh tokens → use the access token for customer-account API calls → refresh after expiry. A button click, redirect, or authorization code is not a completed grant or successful API action; token use remains bounded by the actual granted scope and resources.
- The page states OAuth lets partners process online payments on a customer's behalf on an ecommerce platform. That describes a potential integration capability, not payment-method eligibility, live merchant authorization, a payment or order outcome, or funds movement.

## Detail locators

- Opening, lines 19–23: partner-only scope, delegated customer authorization, requested/confirmed scope and online-payment use case.
- `## How it works`, lines 25–43: four party identities and six high-level code/token flow steps.
- `## Next steps`, lines 45–52: detailed OAuth integration navigation.

## Related

- [[adyen-partner-oauth]] — provider concept and authorization boundary.
- [[source-adyen-docs-partners-oauth-integration]] — detailed app registration, roles, environment URLs, consent, token and refresh conditions.
- [[source-adyen-docs-partners-oauth-scopes]] — scope-to-API-action reference; this hub does not enumerate permissions.

## Raw Sources

- [[raw/adyen/docs/partners/oauth/2026-09-15|Adyen partner OAuth overview, fetched 2026-09-15]]
