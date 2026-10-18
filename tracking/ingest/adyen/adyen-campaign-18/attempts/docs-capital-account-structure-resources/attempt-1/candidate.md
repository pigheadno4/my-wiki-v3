---
title: "Adyen Capital account structure and resources"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/account-structure-resources"
raw_files:
  - "adyen/docs/capital/account-structure-resources/2026-09-15.md"
tags: [adyen, capital, platforms, account-structure, grants]
---

## Overview

This Adyen Capital account-structure page was last modified 2026-01-02 and captured 2026-09-15. It maps ordinary Adyen for Platforms user resources to Capital-specific grant-account and grant-reference resources. The page describes accounting and resource roles for offering financing; the existence of a resource or example balance does not prove a user's eligibility, grant payout, legal ownership beyond the stated relationships, or completed repayment.

## Key takeaways

- The page says Capital is currently available only to merchant accounts with an Adyen for Platforms integration connected to a balance platform. Its foundational user resources are a legal entity containing organization details for verification, a verified-bank-account transfer instrument for grant payouts, supporting documents for legal-entity or instrument checks, an account holder linked to the user's main legal entity and balance account to specify capabilities, and the user's balance account where funds are held and financial activities pass. These roles are different from the platform's liable balance account and from a Capital grant account.
- Adyen creates a **grant account** in the balance platform to track its total outstanding grant receivables. The page explicitly says this account **does not hold funds**. Each grant account has one currency; multiple grant currencies require multiple grant accounts. Its `CG...` identifier and EUR 55,000 illustration for five EUR 10,000 grants with EUR 1,000 fees each describe a sample receivable total, not cash held or a live outstanding amount.
- Adyen creates a **grant reference** with a one-to-one relationship to a grant when that grant is paid out. The reference tracks total, principal and fee balances for that grant, has `Active` status until fully repaid, and then `Repaid`. Its `GR...` identifier and the example negative EUR 11,000 balance for EUR 10,000 principal plus EUR 1,000 fee, decreasing toward zero, illustrate this reference's sign convention. Do not equate its signed balance with the non-funds grant-account example or infer actual debt settlement from the illustration.
- Resource creation and verification are prerequisites to an integration, not proof of eligibility or grant execution. This page describes a verified transfer instrument as a grant payout destination; the broader Capital overview also describes possible balance-account funding. Do not treat this source alone as an exclusive destination rule. Follow the offer, capability, terms, grant-request and payout evidence for a particular user and environment.
- The grant-reference lifecycle is a resource description. It does not specify the timing or evidence needed to confirm a live disbursement, bank receipt, repayment booking, or final contractual discharge; those require transaction and grant-lifecycle records.

## Detail locators

- `## Adyen for Platforms structure`: balance platform prerequisite and legal entity, transfer instrument, supporting document, account holder, balance account roles.
- `## Capital structure` / `### Grant account`: non-funds receivable account, per-currency rule, CG identifier and illustrative total.
- `### Grant reference`: one-to-one per paid-out grant, outstanding total/principal/fee, Active-to-Repaid states, GR identifier and negative-balance example.

## Related

- [[adyen-capital]] — main Capital product concept.
- [[adyen-platforms]] — parent platform context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/account-structure-resources/2026-09-15|Adyen Capital account structure (last modified 2026-01-02; captured 2026-09-15)]]
