---
title: "Braintree Auth Merchant Connect Flow"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/connect"
raw_files:
  - "braintree/docs/guides/braintree-auth/connect-2026-09-16.md"
tags: [braintree, braintree-auth, merchant-connect, oauth, connected-merchants]
---

## Overview

This collected Braintree Auth guide describes the merchant-facing Connect flow that begins from a platform's **Connect with Braintree** button. It covers the Braintree-hosted login or signup experience, OAuth authorization and return redirect, while the snapshot marks Braintree Auth as closed beta.

## Key takeaways

- A platform places the **Connect with Braintree** button in its dashboard so merchants can begin connecting a Braintree account to the platform. Clicking it redirects the merchant to a Braintree-hosted, cobranded page.
- On that hosted page, a merchant can log into an existing Braintree account with PayPal or Braintree credentials. By default the page also offers new-account signup, but the platform can choose a login-only flow.
- An existing-account merchant reaches an Authorize step and grants the platform the permissions defined by its OAuth scope. **Agree and Return** redirects the merchant to a URI allowlisted in the platform's OAuth configuration.
- A merchant signing up for a new account supplies personal and business information before authorization. The flow can pre-populate documented fields and supports **Finish Later**, which lets the merchant stop and resume later while redirecting them to a platform-defined URI.

> [!warning] Closed-beta and flow boundary
> This 2026-09-16 snapshot labels Braintree Auth closed beta. The page describes the merchant-facing navigation and authorization flow; it does not establish current access, platform or merchant eligibility, completed account connection, token exchange, or permission beyond the OAuth scope the merchant grants.

## Detail locators

- Closed-beta availability and interest route: `# Merchant Connect Flow > AVAILABILITY`, lines 16-17.
- Platform button purpose: `# Merchant Connect Flow`, line 19.
- Hosted-page branding, existing-account credentials, default signup option and login-only control: `## User experience`, line 24.
- Existing-account Authorize step, OAuth-scope permissions and allowlisted return URI: `### Login flow`, line 29.
- New-account information, pre-population reference and Finish Later behavior: `### Signup flow`, line 34.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/configuration-2026-09-16|Braintree Auth configuration guide]] - navigation-only authority for OAuth configuration; not read or used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth server-side Connect flow (Node.js)]] - navigation-only authority for server-side connection handling; not read or used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/reference/node-2026-09-16|Braintree Auth Node.js guide reference]] - navigation-only authority for signup fields and broader reference details; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Merchant Connect Flow]] - complete collected guide covering the closed-beta merchant-facing login, signup, authorization and return flow
