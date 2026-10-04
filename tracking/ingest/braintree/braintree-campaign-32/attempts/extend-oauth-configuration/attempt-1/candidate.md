---
title: "Braintree Extend OAuth Configuration"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/oauth/configuration"
raw_files:
  - "braintree/docs/guides/extend/oauth/configuration-2026-09-16.md"
tags: [braintree, braintree-extend, oauth, control-panel, connected-merchants]
---

## Overview

This collected [[braintree]] configuration guide documents a platform setting up an OAuth application in the environment-specific Braintree Control Panel for the [[braintree-extend-oauth]] merchant-connection route. It covers merchant-facing application identity and support information, registered redirect destinations, and internal or partner tracking fields. The snapshot labels OAuth closed beta in production and open beta in sandbox; it does not establish current access, production-beta admission, merchant authorization, issued credentials, API access, or payment acceptance. This is an Extend OAuth source, not the separate [[braintree-auth]] product.

## Key takeaways

- The platform selects the Production or Sandbox Control Panel according to the environment being configured, then creates an application under **OAuth Apps**. Sandbox exposes that page by default; the guide says Braintree must enable access in production.
- The configuration includes required merchant-facing display name, website and logo fields, plus at least one support channel. The exact support options, image recommendation and optional internal or partner-tracking fields remain at the raw locators below.
- Redirect URIs are an allowlist for the destination used after a merchant authorizes the application. The redirect URI supplied during Connect URL generation must already appear in that list or Braintree will not authorize the redirect. The page requires a full URI including its protocol and requires HTTPS in production.
- This configuration page does not expose a client ID or client secret, show SDK initialization, or prescribe server-side secret storage. Those client/server and credential-security responsibilities must not be inferred from the merchant-facing configuration fields here; the separate Connect URL route owns subsequent integration details.

## Evidence boundaries

> [!warning] Snapshot availability and environment qualification
> The 2026-09-16 snapshot says OAuth is closed beta in production and open beta in sandbox. Control Panel visibility and documented setup steps do not prove current availability, account eligibility, production enablement, or a completed OAuth connection.

> [!warning] Redirect and secret-security boundary
> Redirect allowlisting is documented here, but this page does not document client credentials or a secret-storage design. Do not place or infer a client secret in merchant-facing application metadata, and do not treat configuration as proof that a merchant authorized the platform or that credentials were issued.

> [!warning] Extend and Auth remain distinct
> The production-interest link points to a Braintree Auth contact URL, but the collected page is under the `extend/oauth` route. That link does not transfer Braintree Auth product ownership, availability, credential, scope, or lifecycle claims to this Extend OAuth source.

## Detail locators

- Production closed-beta and sandbox open-beta wording: `# Configuration > AVAILABILITY`, lines 16-17.
- Environment-specific Control Panel selection and OAuth Apps creation steps: `## Creating an OAuth application`, lines 20-27.
- Sandbox-default versus production-enabled OAuth Apps access: `## Creating an OAuth application > NOTE`, lines 29-30.
- Merchant-facing identity, website, logo and support-field requirements: `## Creating an OAuth application`, lines 32-42.
- Redirect allowlisting, full-URI form and production HTTPS requirement: `## Creating an OAuth application`, line 45.
- Internal configuration name and optional PayPal BN Code fields: `## Creating an OAuth application`, lines 46-47.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-extend-oauth]]
- Control Panel context: [[braintree-control-panel]]
- Separate product route: [[braintree-auth]]

## Related raw API references

- [[raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16|Braintree Extend OAuth Connect URLs (Node.js)]] - unread navigation-only route for subsequent Connect URL integration details; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16|Braintree Extend OAuth configuration]] - complete collected guide for environment-specific OAuth application setup, merchant-facing metadata, redirect allowlisting and snapshot availability qualifications
