---
title: "Braintree Wells Flat Pre-dispute Programs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/pre-dispute-programs"
raw_files:
  - "braintree/articles/wells-flat/pre-dispute-programs-2026-09-16.md"
tags: [braintree, disputes, chargebacks, visa, rdr, wells-flat]
---

## Overview

This captured [[braintree]] article under the Wells Flat route describes Visa Rapid Dispute Resolution (RDR) as a US-supported pre-dispute program intended to resolve qualifying cases before formal chargeback escalation and the representment process. It is snapshot evidence of Braintree's documented handling, not independent proof of current Visa policy or eligibility for every Braintree merchant account.

## Key takeaways

- The article says merchants enroll in RDR directly with Visa; Braintree support is stated for the US.
- RDR evaluates a pre-dispute against merchant-defined rules. A match sends a credit to the cardholder and accepts dispute liability; a non-match continues through the standard chargeback flow.
- For an item satisfying RDR rules, Braintree says the dispute is automatically accepted and surfaced as Auto-accepted in the Control Panel, dispute webhooks and Dispute reports.
- The captured note says qualifying RDR-resolved disputes do not count against the merchant's dispute ratio monitored by Visa. This is a qualified statement from the captured Braintree article, not a general or independently current network-policy guarantee.

## Detail locators

- **Program purpose and scope:** `# Pre-dispute programs` and `## Visa Rapid Dispute Resolution`
- **Enrollment, merchant-defined rules, credit outcome, fallback and liability:** `## Visa Rapid Dispute Resolution`
- **Braintree status and reporting behavior:** `### How does Braintree handle pre-disputes resolved with RDR?`
- **Webhook field and Control Panel identifier:** `### How does Braintree handle pre-disputes resolved with RDR?` (`pre_dispute_program: "visa_rdr"`)
- **Dispute Search filter and qualified ratio note:** final paragraphs and `NOTE`

## Related

- [[braintree]]
- [[disputes]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/pre-dispute-programs-2026-09-16|Braintree Wells Flat pre-dispute programs (fetched 2026-09-16)]]
