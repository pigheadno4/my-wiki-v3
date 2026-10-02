---
title: "Braintree Auth Configuration"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/configuration"
raw_files:
  - "braintree/docs/guides/braintree-auth/configuration-2026-09-16.md"
tags: [braintree, braintree-auth, oauth, control-panel, connected-merchants]
---

## Overview

This collected Braintree Auth configuration guide is a retrieval entry for a platform setting up its OAuth application in the Braintree Control Panel. It covers the platform's merchant-facing application identity and support information, registered redirect destinations, and environment-specific server credentials. The snapshot labels Braintree Auth closed beta; it does not establish current availability, acceptance into the beta, merchant connection, or live payment acceptance.

## Key takeaways

- The guide says Braintree Auth follows OAuth 2.0. After acceptance into the closed beta, the platform can create an OAuth application in the Control Panel; that application authenticates the platform and identifies it to merchants who connect.
- OAuth application setup is environment-specific: the platform uses either the Production or Sandbox Control Panel for the environment it is configuring. The configured categories include merchant-facing display, website, logo and support information, plus redirect destinations and internal or partner tracking information; exact field requirements remain at the raw locator below.
- Redirect URIs must be registered before they are passed while generating a Connect URL, or the redirect will not be authorized. The guide requires a full URI and says production redirects require HTTPS.
- After creation, the OAuth application has a `client_id` and `client_secret` for Sandbox testing and Production. The platform must store them securely on its server; the guide routes their use to Braintree server SDK configuration and the separate Connect flow.

> [!warning] Closed beta and setup ownership
> This 2026-09-16 snapshot says Braintree Auth is in closed beta and directs interested platforms to contact Braintree. It documents configuration that the accepted platform performs; it does not show that a platform has been accepted, that a merchant has authorized the platform, or that either environment is ready for payments.

## Detail locators

- Closed-beta availability and interest route: `# Configuration > AVAILABILITY`, lines 16-17.
- OAuth 2.0 basis, beta-acceptance prerequisite, platform identity and application purpose: `# Configuration`, line 19.
- Production-versus-Sandbox Control Panel selection and the OAuth Apps setup route: `# Configuration`, lines 22-26.
- Merchant-facing identity and support configuration categories and exact field requirements: `# Configuration`, lines 28-38.
- Redirect allowlisting, full-URI form and production HTTPS requirement: `# Configuration`, line 41.
- Environment-specific client credentials, server-storage ownership, SDK configuration and Connect-flow route: `# Configuration`, line 45.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Supporting concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/server-side/node-2026-09-16|Braintree Auth Server-side Connect Flow (Node.js)]] - navigation-only route for generating a Connect URL and passing a registered redirect URI; not used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Connect guide]] - navigation-only route for the merchant connection flow; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/configuration-2026-09-16|Braintree Auth configuration guide]] - complete collected guide for closed-beta access, platform OAuth application setup, redirect registration and server-held credentials
