---
title: "Adyen Business Accounts: open banking for third-party providers"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/open-banking"
raw_files:
  - "adyen/docs/business-accounts/open-banking/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, third-party-providers, consent]
---

## Overview

This 2026-09-15-modified and captured Adyen open-banking overview addresses **licensed third-party providers (TPPs)** seeking access to Adyen Business Account holders' account information, payment initiation or funds-confirmation interfaces, subject to the holder's agreed scopes, authentication and explicit consent. Adyen is the account-servicing payment service provider; the holder is the payment-service user. The opening PSD2/2018 statement is the page's historical regulatory description, not a current legal determination. This is separate from Checkout's Pay by Bank methods and from the open-banking route for verifying an unregistered external individual's bank-account ownership.

## Key takeaways

- The page describes three TPP functions: **AISP** requests Business Account information, **PISP** initiates payments from Business Accounts, and **PIISP** requests available-funds information. The holder requests a TPP service, authenticates with Adyen and consents to agreed scopes; Adyen then permits API use and sends requested information if that step succeeds. Naming a role, scope or API does not prove consent was granted, a payment was initiated or funds were available.
- To seek access under this captured guide, a TPP must be licensed by a national regulatory authority, have a Qualified Website Authentication Certificate (**QWAC**) and complete Adyen onboarding. Onboarding calls for a PEM QWAC, redirect URL, TPP website and requested AISP/PISP/PIISP scopes; the page says Adyen reviews these and returns a client ID and secret for the linked OAuth flow. Credential issuance is a setup step, not account-holder authorization.
- The page repeatedly says **this documentation is EU-only** and directs UK readers to external UK documentation. Yet it also lists a UK regulatory API, `obuk` URL region and a UK row marked available for account information, payment and funds check. Preserve this internal scope conflict: the captured UK table and URL structure are navigation/context, not an assurance of current UK integration support or eligibility.
- The captured API structure lists TEST and live open-banking PSD2 base URLs, region identifiers `obeu`/`obuk`, provider path segments and `/v1`. It lists EU Berlin Group NextGenPSD2 and UK Open Banking API specifications. These are dated documentation claims; endpoint examples do not prove live access or a successful financial operation.

## Detail locators

- **Opening; Requirements** — PSD2 historical framing, TPP audience, account information/payment/funds-check purposes, EU-only limitation and licensing/QWAC/onboarding requirements.
- **Adyen open banking APIs; Base URL and API structure** — account-holder, AISP/PISP/PIISP and Adyen roles; EU/UK API standards, base URLs, regions, paths and version.
- **How it works; Onboard with Adyen** — agreed scopes, holder authentication/consent, requested information, QWAC/redirect details, Adyen review and OAuth credentials.
- **Supported countries and regions** — EU and UK check-mark rows conflict with the page's EU-only documentation statement. Treat these as a captured table, not verified current coverage.
- **Next steps** — OAuth, consent, AISP, PISP and PIISP child guides are navigation; this overview does not document their detailed operations.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[source-adyen-docs-business-accounts-oauth-flow]] — separate detailed TPP OAuth and holder-consent flow.
- [[source-adyen-docs-business-accounts-verify-account-holder]] — different Adyen/AISP flow to verify an unregistered external individual's bank-account ownership.

## Raw Sources

- [[raw/adyen/docs/business-accounts/open-banking/2026-09-15|Open banking overview, captured 2026-09-15]]
