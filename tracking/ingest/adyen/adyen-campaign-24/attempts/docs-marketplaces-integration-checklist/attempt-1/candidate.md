---
title: "Integration and go-live checklist | Adyen Marketplaces"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/integration-checklist"
raw_files:
  - "adyen/docs/marketplaces/integration-checklist/2026-09-15.md"
tags: [adyen, marketplaces, platforms, integration, go-live]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplace-path checklist routes a marketplace through designing an Adyen for Platforms integration, preparing account structure and credentials, onboarding users, processing and splitting payments, paying out, reconciling, and a separate go-live transition. Its balance-platform, legal-entity, account-holder and transfer-instrument model belongs with [[adyen-platforms]], not the older Classic Platforms account structure or Account API. The page says to design the implementation with an Adyen implementation manager before building (raw lines 23–25).

## Key takeaways

- The checklist identifies company and merchant accounts, a balance platform, account holders and balance accounts, legal entities, transfer instruments and business lines as the core resource types (raw **Review your account structure**, lines 29–44). It distinguishes Balance Platform credentials for Configuration/Transfers/FX/session work, company-scope LEM credentials for legal entities and onboarding sessions, and company credentials for Checkout/Management payment work (raw **Generate and test your API keys**, lines 60–72). Test calls and samples at lines 74–1034 check those integrations; example HTTP 200 or `Authorised` results do not establish a particular live marketplace's verification, split, capture, payout or bank receipt.
- Set up server webhook endpoints and acknowledgments, Customer Area webhook configuration and HMAC protection (raw **Set up webhooks**, lines 1036–1042). For onboarding, Adyen describes hosted and API-only routes and says it needs to verify user information before processing payments for users and paying them out (raw **Onboard and verify users**, lines 1068–1075). The hosted route creates legal entities, an account holder, a hosted link and balance accounts, then receives verification updates; the API-only route also lists a transfer instrument representing a payout bank account that Adyen must verify before payout, Terms of Service acceptance, capability/verification updates and possibly additional documents (raw lines 1095–1135). The guide qualifies business-line creation by route and offering; see those steps rather than assuming it is universal.
- The payment section requires an online payments integration and checkout UI, then directs incoming funds and fees to user balance accounts and the platform liable balance account through split instructions, including authorization/capture, refund and chargeback routes (raw **Process payments**, lines 1137–1156). Payout, internal-transfer, webhook and report routes are separate (lines 1158–1191); a balance-account movement or report is not proof of external bank receipt.
- Going live requires applying for a live account; test-account setup is not automatically replicated. The guide then calls for live credentials and endpoints plus end-to-end checks of legal entities, account holders/balance accounts, payments including declines, payouts, verification errors, webhooks and reports (raw **Go live**, lines 1193–1228). This checklist is a test plan, not evidence those checks passed.

## Detail locators

- Test-only Configuration API, LEM v3 and Checkout v72 calls, SDK-language/version examples and responses: raw lines 74–1034. The curl Checkout payload contains a rendered `{hint:...}` token in its `amount.value` (lines 713–718), so that displayed snippet should not be copied as literal JSON.
- Component session, package, initialization and customization steps: raw **Integrate components**, lines 1044–1066.
- Managed versus custom payout, internal transfer and report-download routes: raw lines 1158–1191.

## Related

- [[adyen-platforms]] — balance-platform model and related source routes.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/integration-checklist/2026-09-15|Integration and go-live checklist, captured 2026-09-15]]
