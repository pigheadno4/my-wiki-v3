---
title: "Braintree Account Updater Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/account-updater"
raw_files:
  - "braintree/articles/guides/account-updater-2026-09-16.md"
tags: [braintree, account-updater, vault, cards, recurring-billing, reporting]
---

## Overview

This collected Braintree guide documents Account Updater, an optional Braintree Direct feature that requests updated account numbers and/or expiration dates from participating issuers for supported vaulted cards. The captured eligibility is limited to merchants based in the US or transacting primarily with US customers; pricing varies by pricing model, and the feature is not enabled by default.

## Key takeaways

- A compatible card is not guaranteed to be updateable: issuer participation controls eligibility. The guide lists Visa, Mastercard and Discover, while excluding prepaid cards and cards processed through Apple Pay or Google Pay.
- On initial enablement, Braintree requests issuer updates for vaulted supported credit cards in batches of 600,000. If the Vault contains more than 2 million payment methods, the initial request is limited to cards that expired within the prior 13 months.
- After the initial batch, requests run on documented rolling criteria involving expiration, near-term recurring billing, transaction activity and Next Day Card Refresh. The transaction-activity section explains why one decline may be insufficient for a recently successful monthly subscription, and Next Day Card Refresh works only when failed-transaction retry logic is configured.
- Account Updater activity can be inspected in an individual payment method's history, a Control Panel report, or a daily-report webhook. The Control Panel report is limited to 40,000 rows; the webhook route links a CSV for vaulted payment methods updated within 24 hours and uses a different event-description column name.
- Certain returned event descriptions stop further update submissions for that card until a user manually updates the payment method in the Control Panel or through the API.

## Detail locators

- Feature purpose: `# Account Updater`, lines 14-16.
- Pricing-model qualification: `## Fees`, lines 19-21.
- Braintree Direct, US, issuer-participation, supported-card and excluded-card scope: `## Compatibility`, lines 24-40.
- Not-enabled-by-default setup boundary: `## Setup`, lines 45-47.
- Initial batching and the more-than-2-million-Vault limit: `## How it works`, lines 50-56.
- Rolling triggers and transaction-activity criteria, including the one-decline recurring-billing example: `## How it works`, lines 60-78.
- Next Day Card Refresh retry dependency and decline-code table: `### Next Day Card Refresh`, lines 81-99.
- Reporting routes, payment-method history, the 40,000-row report limit and daily webhook details: `## Reporting`, lines 102-154.
- Event descriptions and no-resend-until-manual-update behavior: `### Event descriptions`, lines 159-173.

## Evidence boundary

> [!warning] Update requests are not guaranteed card updates
> Account Updater requests updates from participating issuers; card-brand compatibility alone does not establish issuer participation or a successful update. Next Day Card Refresh additionally depends on merchant retry logic, and the reporting outcomes include unsuccessful or action-required states. This collected snapshot does not prove current availability, merchant enablement or a successful payment retry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-account-updater]]
- Supporting concepts: [[braintree-control-panel]], [[braintree-webhooks]], [[recurring-payments]]
- [[source-braintree-control-panel-reporting-expiring-cards]] - navigation to the separate report that identifies expired or soon-to-expire Vault cards
- [[source-braintree-webhooks-account-updater-node]] - navigation to the feature-specific daily-report webhook reference

## Raw Sources

- [[raw/braintree/articles/guides/account-updater-2026-09-16|Braintree Account Updater guide]] - complete collected guide covering feature identity, pricing and eligibility, request criteria, retry dependency, reporting and terminal no-resend outcomes
