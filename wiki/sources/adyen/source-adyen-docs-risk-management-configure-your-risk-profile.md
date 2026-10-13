---
title: "Configure your risk profile | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/configure-your-risk-profile"
raw_files:
  - "adyen/docs/risk-management/configure-your-risk-profile/2026-09-15.md"
tags: [adyen, risk-management, protect, risk-profiles, risk-rules]
---

## Overview

This Adyen guide explains how a merchant configures Protect risk rules on a risk profile assigned to a merchant account, how rule timing and priority affect decisions, and where to inspect results and premium analytics. Its captured raw is dated 2026-09-15 and reports `last_modified` 2022-05-19; it documents configuration and evaluation behavior, not an observed decision on a particular payment.

## Key takeaways

- Configuring rules presupposes use of Protect and at least one created and assigned risk profile. Available rule types depend on Protect basic versus enabled premium features: premium adds fraud-risk and risk-based-authentication machine-learning rules, custom lists and rules, and Dynamic 3D Secure with custom rules. `Review` and `Check for 3DS` are premium actions, with the latter tied to a custom rule linked to Dynamic 3D Secure.
- A rule triggers when a transaction matches its conditions; Protect then applies the configured `Allow`, `Block`, `Review` or `Check for 3DS` action subject to that action's tier and setup. Pre-authorization rules evaluate before payment authorization; post-authorization rules can use later signals such as authentication, CVC/CVV or AVS results.
- Within a risk profile, a triggered `Allow` rule overrides `Block` or `Review`. A post-authorization rule can override a pre-authorization decision, except that a transaction blocked before authorization does not trigger post-authorization risk rules. This exception matters when interpreting a risk result or designing rules for a blocked payment.
- The live Customer Area's payment-level **Risk results** page shows the decision, triggered rules, timing and actions. Profile and rule performance analytics require premium features; the page routes to authorization, refusal and chargeback metrics and risk-based-authentication performance. It does not establish that a particular merchant has premium enabled, that every signal is available, or that a configured rule guarantees a fraud, 3DS or authorization outcome.

## Detail locators

- `## Risk rules` — basic/premium rule table; pre- versus post-authorization evaluation; rule actions, Allow priority, post-authorization override and blocked-before-authorization exception; payment-request fields and list dependencies.
- `## Fine-tune your risk profile` — links to risk lists, post-authorization rules, machine-learning rules and premium custom rules.
- `## View risk results` — live Customer Area route from a merchant account's payment list to payment-level risk decisions and triggered-rule detail.
- `## View risk profile analytics` — premium-only profile and rule performance routes and risk-based-authentication metrics.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/configure-your-risk-profile/2026-09-15|2026-09-15 snapshot — configure a Protect risk profile]]
