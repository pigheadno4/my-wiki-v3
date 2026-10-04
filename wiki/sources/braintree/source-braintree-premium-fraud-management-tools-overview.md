---
title: "Braintree Premium Fraud Management Tools Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/overview"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/overview-2026-09-16.md"
tags: [braintree, premium-fraud-management-tools, risk-data, chargeback-protection, disputes]
---

## Overview

This collected Braintree developer-guide overview describes Premium Fraud Management Tools as pre-processing fraud-prevention and detection checks, identifies transaction data that the page labels mandatory or recommended for particular risk tools, and gives an automated evidence-submission sequence for eligible Chargeback Protection disputes. It is an umbrella integration and routing page, not evidence that every named fraud product has the same decisions, eligibility, payment-method coverage, protection, or bypass behavior.

This is a 2026-09-16 website snapshot. It does not establish current product availability, merchant eligibility, account enablement, successful risk evaluation, processor authorization, settlement, funding, or a favorable chargeback outcome.

## Key takeaways

- The page positions Premium Fraud Management Tools as checks performed before a request is processed, intended to catch suspected fraud before an authorization request reaches the customer's bank. That stated purpose does not mean a risk check is bank authorization or payment execution.
- Its transaction-data table is product-sensitive: it labels email, customer IP, and device ID for Chargeback Protection Tools while marking several fields only as recommended for Fraud Protection Advanced or for all risk tools. Exact field formats, limits, Vault/non-Vault request routes, and per-tool labels remain in the raw table rather than being generalized into a single requirement set.
- Customer IP and device ID are described for customer-initiated transactions under the page's stated `transactionSource` conditions. The linked JavaScript v3 device-data procedure is a separate implementation route; this overview does not establish that collection or server receipt occurred.
- For Chargeback Protection Tools, the page describes automating evidence submission after chargeback-status webhooks: act only on an `Open` chargeback, look up the dispute, confirm that `chargeback_protection_level` references a Chargeback Protection tool and that the dispute remains `Open`, add eligible text or file evidence, then finalize before the reply-by date.
- The page states umbrella compatibility with credit and debit cards, Apple Pay, Google Pay, and Secure Remote Commerce. Treat this as page-scoped compatibility routing, not proof that every named Premium Fraud Management Tool supports every listed method for a particular merchant, region, processor, transaction, or current account configuration.

> [!warning] Named products are not interchangeable
> **Fraud Protection**, **Fraud Protection Advanced**, **Kount Custom**, **Chargeback Protection**, and **Effortless Chargeback Protection** have separate eligibility, decision, evidence, fee, and protection boundaries in their dedicated sources. The table's mandatory/recommended labels and the automated evidence workflow must be applied only to the named tool and conditions shown; they do not transfer behavior among sibling products.

> [!warning] Eligibility and deadline remain consequential
> The evidence sequence applies only when the dispute is `Open` and its `chargeback_protection_level` references a Chargeback Protection tool. Evidence still has to be eligible and finalized before the reply-by date. The sequence does not establish coverage, waive every evidence requirement, or guarantee protection or a dispute result.

> [!warning] Bypass behavior remains unresolved elsewhere
> This developer overview does not state whether fraud checks can be bypassed. The existing [[braintree-chargeback-protection]] concept records conflicting collected guidance about bypass support for Chargeback Protection tools. Do not infer bypass availability or prohibition from this page's silence; obtain current Braintree/PayPal clarification before operational use.

## Detail locators

- Premium-tool purpose and additional-data statement: `# Overview`, raw line 16.
- Risk-data field formats, Vault/non-Vault routes, transaction-source conditions, and tool-specific mandatory/recommended labels: table under `# Overview`, raw lines 18-31.
- Chargeback evidence automation purpose and webhook-to-finalization sequence: `#### Chargeback Protection Tools - submitting required evidence for eligible chargebacks`, raw lines 34-43.
- Fraud-option comparison route: raw line 45.
- Umbrella payment-method compatibility list: `## Compatibility`, raw lines 48-55.
- Configuration next-page route: raw line 59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Chargeback workflow and conflict route: [[braintree-chargeback-protection]]
- Advanced product boundary: [[braintree-fraud-protection-advanced]]
- Named Fraud Protection boundary: [[braintree-fraud-protection]]
- Kount Custom boundary: [[braintree-kount-custom]]
- Effortless product boundary: [[braintree-effortless-chargeback-protection]]
- Generic dispute context: [[disputes]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/basic/overview-2026-09-16|Braintree Basic Fraud Tools overview]] - linked navigation for the basic-tools comparison; not read as factual evidence for this source
- [[raw/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v3-2026-09-16|Braintree Premium Fraud Management Tools client-side JavaScript v3 guide]] - linked device-data implementation route; not used as raw factual evidence for this source
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks guide]] - linked chargeback-notification setup route; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/add-text-evidence/node-2026-09-16|Braintree Node.js Dispute Add Text Evidence reference]] - linked evidence-operation family route; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/document-upload/create/node-2026-09-16|Braintree Node.js Document Upload Create reference]] - linked file-upload family route; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/dispute/finalize/node-2026-09-16|Braintree Node.js Dispute Finalize reference]] - linked finalization-operation family route; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/overview-2026-09-16|Braintree Premium Fraud Management Tools overview]] - complete collected snapshot covering umbrella purpose, tool-sensitive risk-data applicability, qualified chargeback evidence automation, and payment-method compatibility routing
