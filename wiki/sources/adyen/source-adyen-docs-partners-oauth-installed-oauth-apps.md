---
title: "Manage installed Adyen OAuth apps"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/oauth/installed-oauth-apps"
raw_files:
  - "adyen/docs/partners/oauth/installed-oauth-apps/2026-09-15.md"
tags: [adyen, partners, oauth, consent, app-management]
---

## Overview

Adyen's installed OAuth apps page (metadata last modified 2023-05-04; captured 2026-09-15) describes the customer-side authorization, viewing, revocation and audit route in Customer Area. It says only partners can create OAuth apps. This is a procedure and access model, not evidence that a particular customer installed, approved, revoked or used an app. [[adyen-partner-oauth]] owns the wider delegated-token lifecycle.

## Key takeaways

- To install a partner app, the partner redirects the customer to Adyen for authentication. After authenticating, the customer selects one or more merchant accounts and is shown the app's access scope. The customer cannot modify that scope on this page; the selected accounts and scope bound the intended grant rather than providing universal merchant access (raw lines 19–25).
- The **Installed OAuth apps** page shows which apps are installed for which merchant accounts. Viewing it requires **company account access** and the **Merchant admin** user role, using the company account in Customer Area at **Developers → OAuth authorizations** (raw lines 27–40).
- Revocation has the same company-account and Merchant-admin prerequisites. In the app's **Edit** view, select **Uninstall**. The page says revocation immediately removes the app's account access and invalidates all active access. It does not distinguish access from refresh tokens or specify a revocation API; do not infer token-type mechanics or claim an operation occurred (raw lines 42–59).
- The audit-trail performing-user identifier is formatted `oauth_[Authorization_ID]@Company.[YourCompanyAccount]`, with the authorization ID looked up via installed apps. That is attribution format, not proof that a particular action or payment was authorized (raw lines 61–65).

## Detail locators

- Partner creation and customer account/scope selection: raw lines 19–25.
- View prerequisites and Customer Area navigation: raw lines 27–40.
- Revocation role, action and immediate stated effect: raw lines 42–59.
- Audit-trail actor format: raw lines 61–65.

## Related

- [[adyen-partner-oauth]] — partner delegation and token-lifecycle concept.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/partners/oauth/installed-oauth-apps/2026-09-15|Installed OAuth apps, captured 2026-09-15]]
