---
title: "Adyen Issuing Transfer Instrument components"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/components-overview/before-payment/transfer-instrument-component"
raw_files:
  - "adyen/docs/issuing/components-overview/before-payment/transfer-instrument-component/2026-09-15.md"
tags: [adyen, issuing, platforms, onboarding, transfer-instruments, ui-components]
---

## Overview

This 2026-09-15 Issuing-path guide covers Adyen's prebuilt Transfer Instrument Configuration and Management UI components for adding, verifying, and managing users' bank-account information in a platform onboarding flow. A transfer instrument is the bank-account resource here, distinct from an Issuing card payment instrument. This page overlaps the [[source-adyen-docs-issuing-onboard-users-components]] and [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] entries but has its own canonical URL and pinned raw snapshot. See [[adyen-issuing]].

## Key takeaways

- The Onboarding components are compatible only with legal entities created using Legal Entity Management API v3 or v4. This guide requires an Adyen for Platforms integration, a Legal Entity Management API key for Session Authentication API access, preceding API-only onboarding steps, and applicable language/browser support. Feature guidance may vary with the component-library version; other onboarding steps still require API calls (raw lines 23–53).
- Configuration lets users provide bank-account information and either permit instant verification or upload documents for Adyen validation. Management lists added accounts with their verification statuses and applicable errors, and supports add, edit, and delete actions (raw lines 57–75, 562–572).
- The platform server creates the authentication session with `POST /sessions` using its LEM API key, an allowed origin (HTTPS only on live), `product=onboarding`, a `legalEntity` resource for the legal entity that owns the bank account and has the platform contract (the individual owner for a sole proprietorship), and `transferInstrumentConfiguration` and/or `transferInstrumentManagement` roles. The front end uses the session response through a token-fetch/refresh callback (raw lines 98–113, 141, 180–204).
- The Configuration `complete` event means the transfer instrument was successfully submitted and the component finished its task. Management `add`, `edit`, and `remove` events notify the host application of user actions. The guide's immediate-change/payout-direction language and its example completion payload do not establish that verification succeeded, a payout was eligible, or funds reached a bank (raw lines 73–75, 186, 562–601).

## Detail locators

- Configuration and Management component properties, including test/live environment, root legal entity, token callback, US/CA `openBankingPartnerConfigId` requirement, optional payout-account settings, and event callbacks: raw lines 174–203.
- Library install and HTML/React/Vue examples: raw lines 152–170 and 204–389. Example entities, URLs, and callback data are illustrative.
- Optional CSS variables and supported locale table: raw lines 391–558 and 603–631.

## Related

- [[adyen]] — provider context.

- [[adyen-issuing]] — main Issuing concept and neighboring evidence.
- [[source-adyen-docs-issuing-onboard-users-components]] — overlapping Issuing onboarding route.
- [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] — overlapping Platforms component route.

## Raw Sources

- [[raw/adyen/docs/issuing/components-overview/before-payment/transfer-instrument-component/2026-09-15|Issuing Transfer Instrument components guide, captured 2026-09-15]]
