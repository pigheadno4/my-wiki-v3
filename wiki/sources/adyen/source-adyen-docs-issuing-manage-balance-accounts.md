---
title: "Adyen Issuing manage balance accounts"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-balance-accounts"
raw_files:
  - "adyen/docs/issuing/manage-balance-accounts/2026-09-15.md"
tags: [adyen, issuing, balance-accounts, configuration-api, lifecycle]
---

## Overview

This 2026-09-15 Adyen Issuing guide explains Configuration API and Customer Area operations for a user's balance account: creation under an account holder, viewing balances and linked cards, updating, and permanent closure. These operations are part of broader onboarding and verification, as the page states. See [[adyen-issuing]] and [[adyen]].

## Key takeaways

- A balance account is an API resource containing information about funds held by a user. The guide says to use the Configuration API to manage it, within a broader onboarding and verification process (raw lines 19–21).
- To create one manually, send `POST /balanceAccounts` with the **account holder ID** to attach it to. Retain the returned balance-account `id` for viewing, updating and closing. The response shown is a **test example**, including zero balances and `active` status; it does not establish an actual funded account (raw lines 23–27, 227–254).
- To view an account holder's balance accounts and available balances, use Customer Area **Balances > Balance accounts** or the documented GET endpoints. Account-holder listing is paginated; account detail includes balances, and a separate GET lists payment instruments associated with a balance account (raw lines 256–278).
- `PATCH /balanceAccounts/{id}` updates a balance account; the page's example changes its description (raw lines 280–295). For **permanent closure**, first check that the account has **zero balance**. Only empty balance accounts can be closed; transfer any remaining funds through the separately linked funds guide, then update `status` to `Closed` (raw lines 473–480). This page does not itself demonstrate a successful transfer or closure.
- The page separately points to permanent account-holder deactivation if the holder discontinues its contractual relationship with the platform (raw line 482); balance-account closure and account-holder deactivation are distinct actions.

## Detail locators

- Create request and illustrative test-environment response: raw lines 23–254. The language examples are versioned separately (Java 33.0.0, PHP 24.0.0, .NET 28.0.0, Node 23.3.0, Go 17.0.0, Python 13.3.0, Ruby 10.1.1); use the captured snippet only in its stated version context.
- Customer Area selection and GET endpoint details: raw lines 256–278.
- PATCH description examples and language versions: raw lines 280–470.
- Closure zero-balance precondition, `Closed` status, and linked account-holder deactivation: raw lines 473–482. The transfer and deactivation links are navigation to separate guidance, not evidence of their outcome here.

## Related

- [[adyen-issuing]] — Issuing concept.
- [[adyen-index]] — provider source index.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-balance-accounts/2026-09-15|Adyen manage balance accounts, captured 2026-09-15]]
