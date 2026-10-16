---
title: "Troubleshooting the Adyen Mirakl Marketplace connector"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/troubleshooting"
raw_files:
  - "adyen/docs/plugins/mirakl/troubleshooting/2026-09-15.md"
tags: [adyen, mirakl, troubleshooting, support, payouts]
---

## Overview

This 2023-last-modified Adyen Docs page, captured 2026-09-15, gives a short troubleshooting and Support-escalation path for a Mirakl Marketplace connector integration. It does not itself diagnose a particular installation or establish that a configuration change or payout retry has succeeded. [[adyen-mirakl]]

## Key takeaways

- First check the connector setup guide. The release-note step says **Coming soon**, but also directs readers to plugin release notes to check whether an error is a known bundle issue fixed in a later version. That is a diagnostic route, not an instruction to upgrade blindly or proof of a specific fix.
- If the issue persists, contact Adyen Support and include **Mirakl** in the request body. Provide test-versus-live environment, reproduction and already-tried steps, screenshots and error/unexpected-behavior details, and connector logs. The page says the connector keeps logs for **up to two weeks**.
- The stated Support areas are account setup (operator emails and schedules for payouts, full account sync and partial account sync) and payouts (restarting **failed payouts that have reached the retry limit**). This is a Support-assisted boundary; the page gives no merchant-run retry command, idempotency rule, or authorization to repeat a pending transfer. A restart request is not proof of a completed payout, seller bank credit, or repaired account state.
- This page contains no credential-error taxonomy, seller KYC remediation steps, invoice-state repair procedure, or detailed payout status schema; consult the relevant dedicated connector guides and actual Support investigation for those questions.

## Detail locators

- **Setup and release-note checks:** raw lines 19–29.
- **Support request contents and two-week log retention:** raw lines 31–38.
- **Support scope for account schedules and exhausted-retry failed payouts:** raw lines 40–48.

## Related

- [[adyen-mirakl]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/troubleshooting/2026-09-15|Adyen Mirakl connector troubleshooting — collected 2026-09-15]]
