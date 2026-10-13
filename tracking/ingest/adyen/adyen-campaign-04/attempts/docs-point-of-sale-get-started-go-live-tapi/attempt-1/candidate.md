---
title: "Terminal API go-live checklist | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/get-started/go-live-tapi"
raw_files:
  - "adyen/docs/point-of-sale/get-started/go-live-tapi/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, go-live, live-environment]
---

## Overview

This Adyen Docs checklist describes taking a merchant Terminal API integration with **Adyen-provided payment terminals** from test to live: obtain a live account, create its merchant/store and finance setup, order and configure live terminals, change local or cloud integration settings, board terminals, and test through reconciliation. It is a 2026-09-15 website snapshot, not evidence that any account was approved, live terminal enabled, or payment executed. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- Before beginning, the checklist points to applying for a live account, signing the contract, and reading live-application requirements. The **test account structure is not copied** to live: request live merchant accounts, then stores if needed, through the live Customer Area. The stated four-business-day and two-business-day processing times are examples from this dated page, not a delivery commitment.
- The finance review asks for payout bank account information, notes that changing the payout schedule is optional, and calls for reports and settlement-detail reconciliation. It says to **consider** a Reserve and auto-funding to cover refunds and other expenses; that phrasing does not make them universal go-live prerequisites. This page does not prescribe a per-payment capture configuration.
- **Test terminals cannot process live payments.** Order live terminals from the live Customer Area. Test-environment terminal settings are not copied either: configure the live terminals and payment features in the live Customer Area, enable Terminal API, and assign terminals to a store. Some feature configuration may need Adyen Support. The page names company, merchant, store, and terminal setting levels.
- Update live API credentials and POS code separately by architecture. For a **local** integration, use live terminal IP addresses or hostnames, install and verify Adyen's live terminal certificate (or use a library), and implement message encryption if skipped in test; the page says a live terminal will not accept unencrypted API requests. For **cloud**, generate a new API key for the credential in use and switch to the live endpoints and key. Adding extra credentials and Customer Area users is recommended or optional as described, not a claim that the test key or test endpoints work live.
- On receipt, the checklist says to inspect, power on, network-connect, board, and check the terminal's Adyen connection, with model-specific manual steps. It then **recommends** end-to-end live testing from a low-value real-card payment through Customer Area verification, reconciliation, and a refund. Its example journal sequence is Received → Authorised → Settled; it should not be read as proof that a merchant completed authorization, capture, settlement, refund, or reconciliation.

## Detail locators

- `Terminal API go-live checklist` / `Requirements`, lines 15–35: Adyen-provided Terminal API scope, live-account application, contract, and application-requirement routes.
- `1. Set up your Adyen live account`, lines 37–51: test/live account-structure separation, merchant account and store requests, historical processing estimates.
- `2. Review your finance settings`, lines 53–96: payout bank data, optional schedule change, reporting/reconciliation steps, optional Reserve and auto-funding consideration.
- `3. Order live payment terminals`, lines 98–108: test-terminal limitation, live ordering and historical arrival estimate.
- `4. Prepare your terminals`, lines 110–130: live feature/settings reset, Terminal API enablement, support and store assignment.
- `5. Update your integration`, lines 132–173: live credentials/users, local certificate and encryption, cloud key/endpoints, terminal inspection/boarding/connectivity.
- `6. Test your integration`, lines 175–199: recommended real-card payment, Customer Area journal example, reconciliation scope, and refund test.
- `See also`, lines 201–204: terminal diagnostics and troubleshooting links are navigation only.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — in-person Terminal API concept and related source routes.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/get-started/go-live-tapi/2026-09-15|Terminal API go-live checklist (2026-09-15 snapshot)]]
