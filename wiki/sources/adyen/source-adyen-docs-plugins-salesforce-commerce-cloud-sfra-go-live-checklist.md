---
title: "Adyen SFRA go-live checklist"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/go-live-checklist"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/go-live-checklist/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, go-live, webhooks, credentials]
---

## Overview

This Adyen SFRA cartridge checklist (2024-01-19 last-modified metadata; captured 2026-09-15) lists live-account, finance, risk/compliance, API, webhook, end-to-end test, and Salesforce Business Manager tasks before accepting live payments. Test setup is not copied to live. The guide is a preparation checklist, not evidence that a merchant has switched environments, passed compliance review, processed a live payment/refund, migrated tokens, or received settlement. See [[adyen-salesforce-commerce-cloud]] and [[adyen]].

## Key takeaways

- Live setup requires account structure and individual live Customer Area users with task-appropriate roles/access; payment methods are rendered from enabled Customer Area methods. Finance tasks include payout-bank details, payout settings and settlement-report reconciliation, with reserve an optional funding consideration. [Raw lines 19–66]
- Risk/compliance guidance includes reviewing risk rules and strongly recommending CAPTCHA against card testing; Visa/Mastercard 3DS enrollment may take up to seven days. Only cartridge v22.1.1 and earlier has the specified Business Manager 3DS2 enablement step. The page calls for PCI DSS assessment against SAQ A, recommends default card component for eligibility, and warns customization may require other assessment such as SAQ D; accessibility compliance remains the merchant's responsibility. These are qualifications, not compliance certification. [Raw lines 68–102]
- Live API communication requires a live Customer Area API key copied to Business Manager and live credentials with `Merchant Recurring`, `Checkout webservice`, and `Checkout encrypted cardholder data` permissions. Live webhooks must be configured in both systems; the cartridge's scheduled job handles events. A **200** from Test Configuration shows an HTTP response for that test, not proof that all event types, orders, or financial outcomes were processed. [Raw lines 104–130]
- Adyen asks for real-detail end-to-end tests covering successful, refused and fraud-risk payments, API refunds including partial refunds, and successful/failed 3DS challenge cases. Real payments incur fees. This testing instruction is not a record that any test was performed or passed, and the checklist provides no capture-mode or stored-token migration procedure. [Raw lines 132–147]
- Business Manager steps are **version-specific**: v25.3.0+, v25.2.0–25.2.1 and v24.1.0–25.1.0 use environment Live, new live API/client keys, live URL prefix, matching front-end region and live service credentials. v23.3.1 or earlier instead edits live endpoint prefixes and `adyen_mode`, and warns a Salesforce sandbox shares a single live URL prefix across connected live sites, preventing different prefixes for different go-live regions. Conditional wallet merchant IDs/certificates and India region setting are listed. Replacing credentials or shared prefixes affects the selected Business Manager configuration and requires merchant-specific review; this page does not document rollback. [Raw lines 149–268]
- The page says to test real payments after configuring live Customer Area/Business Manager (line 27), while its Business Manager section says to configure those settings after tests (line 151). Treat this as a sequence ambiguity in the dated checklist; verify the intended test/live transition for the installed version before using it as a runbook. The closing “ready to accept” sentence is guidance, not live approval or payment proof. [Raw lines 27, 149–151, 270–272]

## Detail locators

- Account, method and finance checklist: raw lines 19–66. Risk, 3DS, PCI and accessibility scope: raw lines 68–102. Credential roles and webhook/scheduled-job checks: raw lines 104–130.
- Real-payment test cases and fee warning: raw lines 132–147. Versioned Business Manager branches, region matching and shared-prefix limitation: raw lines 149–268. Closing readiness statement: raw lines 270–280.
- This source does not specify token migration, actual capture configuration, webhook-to-order transition proof, live account eligibility, or payment/payout finality.

## Related

- [[adyen-salesforce-commerce-cloud]]
- [[adyen]]
- [[source-adyen-docs-plugins-salesforce-commerce-cloud]]

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/go-live-checklist/2026-09-15|Adyen SFRA go-live checklist, 2026-09-15 snapshot]]
