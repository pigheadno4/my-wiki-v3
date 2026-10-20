---
title: "Adyen Issuing network tokens for digital wallets"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/tokens-digital-wallet"
raw_files:
  - "adyen/docs/issuing/tokens-digital-wallet/2026-09-15.md"
tags: [adyen, issuing, network-tokens, digital-wallets]
---

## Overview

Adyen's 2026-09-15-captured Issuing guide explains the issuer-side provisioning of network tokens when a cardholder adds an Adyen-issued card to a digital wallet such as Apple Pay or Google Pay. The wallet asks the card scheme, the scheme passes the request to Adyen, and a created token initially has `inactive` status while Adyen analyzes risk. The token substitutes for sensitive card details in the wallet; this guide addresses cardholder wallet provisioning rather than acquiring-side checkout tokenization. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The stated prerequisites are an Issuing-supporting integration, a Configuration API credential with the account-scoped NetworkTokens read/patch role, Network token webhook subscription, and Adyen-contact confirmation of a card manufacturing profile. Phone-call authentication is optional setup through the Adyen contact (raw lines 25–35).
- Adyen may activate a token automatically after low-risk analysis; require 2FA if it has the cardholder's email or phone; require cardholder phone verification through the issuer's call center when that option is enabled; or close the token and end provisioning. For successful call-center verification, the issuer PATCHes `/networkTokens/{networkTokenId}` to `active` (raw lines 70–89, 93–161).
- High risk without enabled call-center authentication, or incorrect/incomplete token-request information, leads to automatic closure in this guide. The page suggests linking cardholder email/phone for 2FA or using a different device after high device risk, but does not describe reopening a closed token (raw lines 167–190).
- Provisioning and decision webhooks are described for creation and subsequent activation/closure (raw lines 99–108, 120–130, 150–161, 181–188). A created `inactive` token, webhook, or wallet add attempt does not demonstrate activation or a successful payment.
- The page's abbreviated payment example says the scheme approves if the token is valid (raw lines 56–64). Treat that as a simplified token-flow illustration, not a complete authorization rule or assurance of approval; the separate [[source-adyen-docs-issuing-authorisation]] describes other issuer checks and decision stages.

## Detail locators

- Wallet request and card scheme/Adyen token handoff: raw lines 19–23 and 37–54. Illustrated wallet payment handoff: raw lines 56–68.
- Inactive creation and four risk-decision branches: raw lines 70–95. Automatic activation: raw lines 93–112; 2FA and contact-data prerequisite: raw lines 114–134.
- Call-center verification, optional enablement and PATCH: raw lines 136–165. Closure conditions and suggested mitigations: raw lines 167–192.

## Related

- [[adyen-issuing]] — Issuing program and reciprocal source route.
- [[source-adyen-docs-issuing-authorisation]] — separate issued-card payment authorization checks.

## Raw Sources

- [[raw/adyen/docs/issuing/tokens-digital-wallet/2026-09-15|Network tokens for digital wallets, captured 2026-09-15]]
