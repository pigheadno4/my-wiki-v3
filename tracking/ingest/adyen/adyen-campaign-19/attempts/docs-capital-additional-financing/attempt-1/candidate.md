---
title: "Adyen Capital additional financing and grant renewal"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/additional-financing"
raw_files:
  - "adyen/docs/capital/additional-financing/2026-09-15.md"
tags: [adyen, capital, platforms, additional-financing, grant-renewal]
---

## Overview

This 2026-09-15 Adyen Capital guide distinguishes a **new grant after full repayment** from a **subsequent grant after partial repayment** (renewal). The latter is described as a limited-availability pilot, subject to prior-grant eligibility, a renewal offer and new Terms of Service. It states how principal reservation, prior-fee waiver and new-fee application are intended to work; the page is a product/flow description, not proof of an individual's eligibility, accepted terms, settled prior balance or funded subsequent grant.

## Key takeaways

- After the prior grant is **100% repaid**, the user may receive a new grant through the first-time grant process. A **partially repaid** prior grant can instead be renewed only if it meets specific conditions; the guide says Adyen disburses the full subsequent grant amount and reserves prior outstanding principal for repayment. Renewal is a **pilot** requiring contact with Adyen for access. The page does not itself specify platform API roles or country availability; those must be checked in the relevant Capital integration and product guides.
- Renewal eligibility requires a risk-assessed, balance-platform-varying minimum repayment percentage, no outstanding missed repayments, prior-grant age of at least **90 days**, same currency for prior grant and renewal offer, and a renewal offer of at least **150%** of prior outstanding balance. Eligibility is separate from an offer selected by the user and from actual funding.
- Current underwriting determines the renewal's repayment percentage, fee and maximum amount, which may differ from the prior grant. Offers are recalculated weekly and expire after **seven days**. For each subsequent grant the user must accept new ToS; after selecting the renewal offer, `receiveGrants` is disallowed until that acceptance. A stale displayed offer or prior ToS acceptance does not establish permission to fund the renewal.
- The guide describes full subsequent-grant disbursement and reservation of prior outstanding principal for repayment as a **single atomic action**. At renewal, any unpaid fee from the prior grant is fully waived, while the new fee percentage applies to the entire subsequent principal. It defines effectively available funds as new principal minus prior outstanding principal. These stated mechanics do not supply a transaction record proving a real reservation, fee waiver, repayment or receipt of funds.
- The UI-component route shows a renewal notification, updated minimum, new ToS and automatic subsequent-grant creation after offer acceptance/signature. The API-only route obtains eligibility and minimum from a webhook or GET `/grants`, gets and presents qualifying offers, obtains new ToS acceptance, and configures the subsequent grant with prior ID `renewsGrantId`. The UI description says its minimum loan amount updates to outstanding balance plus **EUR 500** (or equivalent), while the eligibility table separately requires **150%** of outstanding balance; the page does not reconcile these thresholds. Preserve both statements and do not infer one universal minimum formula. UI creation/configuration is not disbursement proof.

## Detail locators

- Opening and `## Eligibility`: fully repaid new grant versus partially repaid renewal, pilot and five prior-grant/offer eligibility conditions.
- `## Renewal conditions`: weekly/seven-day offer validity, new ToS/capability gate, atomic disbursement/reservation, prior fee waiver, new fee and effectively available-funds formula.
- `## How renewal works` / `### Tab: UI components`: UI notification, outstanding-plus-EUR-500 statement, new ToS and automatic configuration path.
- `### Tab: API-only`: eligibility webhook/GET, offer presentation, ToS and `renewsGrantId` handoff.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-renew-grant]] — separate step-by-step pilot API renewal flow.
- [[source-adyen-docs-capital-grant-lifecycle-and-status]] — separate status evidence.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/additional-financing/2026-09-15|Adyen Capital additional-financing guide (fetched 2026-09-15)]]
