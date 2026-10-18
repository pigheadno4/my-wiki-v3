---
title: "Adyen Business Accounts: Open banking account-holder consent OAuth flow"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/oauth-flow"
raw_files:
  - "adyen/docs/business-accounts/oauth-flow/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, oauth, consent]
---

## Overview

This 2026-09-15-captured guide addresses a **third-party provider** seeking an Adyen Business Account holder's explicit consent to access open-banking account data and, depending on scope, initiate payments. It describes authorization-code OAuth with PKCE, access and rotating refresh tokens, then a separate `POST /consents` step to obtain a consent ID. It is distinct from Adyen Partner OAuth for merchant-account resources and from the separate open-banking route for verifying an unregistered external individual's bank account. The procedure does not prove that a holder approved consent, an account is open, or a payment occurred. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- The page says this integration-type entry is **not applicable** because it is intended for third-party providers, and requires prior Adyen open-banking onboarding (raw lines 21–26). The holder is redirected to Adyen's authentication/consent interface; the client receives an authorization code at its `redirect_uri`, and the **server** exchanges it for tokens (raw lines 28–45, 79–85).
- The unauthenticated GET `/bankoauth/authorize` request carries `client_id`, `response_type=code`, `redirect_uri`, requested `scope`, PKCE `code_challenge_method=S256` and `code_challenge`, and anti-CSRF `state`. The page lists `bank.aisp:read`, `bank.pisp:write` and `bank.cof:read` as possible scopes and says the returned authorization code expires in **five minutes** (raw lines 51–85). The TEST URL and HTML-embedding example are captured integration guidance, not a successful redirect or grant.
- Server-side POST `/token` uses `grant_type=authorization_code`, the code, `code_verifier`, the matching redirect URI and HTTP Basic `client_id:client_secret`. The returned bearer access token defaults to a 24-hour lifetime; the refresh token is one-time-use and a replacement must be saved. If it is lost, the guide says the holder must authenticate again (raw lines 96–148). Refresh uses `grant_type=refresh_token` and the current refresh token (raw lines 207–246).
- Access token alone is not the consent ID. The guide then calls `POST /consents` with bearer access and a Base64 eIDAS QSEAL certificate in `TPP-Signature-Certificate`. It requests account access, recurrence, validity, frequency and combined-service settings; the table states maximum **90 days** and **10 uses/day**. Its response includes `consentStatus`, `consentId` and SCA-status links, and the text says holder approval is still needed. The illustrated `consentStatus: received` is not approval (raw lines 150–205).
- The refresh-token descriptions differ: the first says it expires as soon as used; the refresh section says it expires with a short grace period, while both call it one-time-use (raw lines 125–131, 230–237). Preserve that discrepancy rather than assuming a retry window. The page describes possible account-detail, balance or payment initiation access **depending on actual consent and scope**; neither requested scope nor token issuance alone proves payment permission (raw lines 32–45, 63–67).

## Detail locators

- Third-party-provider identity, onboarding and actor/data-access sequence: raw lines 19–45.
- Authorization redirect, PKCE/state fields and five-minute code: raw lines 47–94.
- Server token exchange, token lifetimes, refresh-token rotation and loss boundary: raw lines 96–148, 207–246.
- Separate consent request, QSEAL header, validity/frequency fields, received-status example and authorization tracking: raw lines 150–205.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[adyen-partner-oauth]] — distinct partner application OAuth for merchant-account resources.
- [[source-adyen-docs-business-accounts-verify-account-holder]] — distinct external-individual bank-account verification route.

## Raw Sources

- [[raw/adyen/docs/business-accounts/oauth-flow/2026-09-15|Captured account-holder consent OAuth guide]]
