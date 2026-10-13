---
title: "Shopper DNA | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/shopper-dna"
raw_files:
  - "adyen/docs/risk-management/shopper-dna/2026-09-15.md"
tags: [adyen, risk-management, shopper-dna, identity-analysis, pii]
---

## Overview

This Adyen page describes Shopper DNA, a Customer Area visualization that groups transactions by shopper identifiers to investigate connections among payments and shopper details. It requires an online-payments integration, enabled risk management and Protect premium features. The 2026-09-15 snapshot says an infrastructure and linking-logic rollout is in progress; it does not establish which version a particular merchant sees, cross-merchant-account matching, or that any cluster is a verified real-world identity.

## Key takeaways

- Shopper DNA groups transactions in dynamic profiles when they share identical identifiers. A matching transaction joins an existing profile; otherwise a new profile is generated. The rollout comparison says the prior engine used strong and weak identifiers, while the new engine uses only strong identifiers. Treat that as a phased change rather than a uniform already-completed migration.
- Access is role-gated. The requirements table lists **View Payments**, **Merchant View PII**, and **Merchant View Oil Splash** to view the Shopper DNA page, and **Risk admin** or **Merchant Manual Review** to review transactions in case management. A separate limitations row says name, email and IP address are masked by default and **Merchant view PII** is needed for unmasked details. The snapshot does not reconcile why the page-access role list and masking condition both mention that PII role.
- The live Customer Area routes are a selected transaction's Payment details page or a Case details page. The graph and sidebars support node inspection, connection isolation, payment-status filtering and attribute review; the raw contains the exact UI actions and a collapse rule for large non-linking groups. These are investigation tools, not automatic proof of fraud or an instruction to block every linked transaction.
- If a link is wrong and causes over- or under-blocking, the page says a merchant can add shopper details to the relevant risk list in its risk profile to allow or block the **next transaction containing that detail**. This is a prospective risk-list action, not a retrospective correction of prior payment outcomes.

## Detail locators

- `## Requirements` — integration, risk and premium prerequisites; page and case-management roles; PII masking condition.
- `## How shopper DNA works` — matching identical identifiers, dynamic profiles, new profile creation and risk-list correction for a later transaction.
- `## View shopper DNA` — payment-details and case-management entry points in live Customer Area.
- `## Analyze shopper DNA` — force graph, Payments and Attributes sidebars, filters, node actions and collapse rule.
- `## Shopper DNA comparison` — rollout status, prior mixed-strength versus new strong-only linking logic, redesigned graph and direct attribute risk-list controls.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/shopper-dna/2026-09-15|2026-09-15 snapshot — Shopper DNA visualization and rollout]]
