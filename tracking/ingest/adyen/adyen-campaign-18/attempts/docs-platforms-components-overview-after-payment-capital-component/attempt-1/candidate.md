---
title: "Adyen for Platforms Capital components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/capital-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/capital-component/2026-09-15.md"
tags: [adyen, platforms, capital, components, business-financing]
---

## Overview

This 2026-09-15 guide describes Platform Experience **Capital Overview** and **Capital Offer** components for presenting Adyen Capital financing to eligible platform users. The Overview shows a grant term sheet, status, repayment progress and required actions; the Offer lets a qualifying user choose an amount and repayment term and submit a request. The guide says the components handle offer retrieval, Terms of Service and grant payouts, but a rendered screen, preliminary offer, submitted request, signature or displayed status is not independent proof of approved financing, booked grant funds, completed repayment or bank receipt. Exact integration/version and session requirements belong to the linked integration guide; this page says features vary by library version but does not state an API credential role or a minimum supported version.

## Key takeaways

- Adyen says the Capital components include required disclosures and must not hide or alter text identifying Adyen or its local branches as the loan provider, or country-specific legal notices such as the US ECOA notice. Preserve that wording even though the page also uses **grant** and **business financing**; the snapshot is not legal advice or a current jurisdiction-specific compliance determination.
- **Capital Overview** can show eligibility messages, Terms signing, active-grant terms and repayment progress, bank details for unscheduled repayments, and eligible renewal routes. **Capital Offer** shows a preliminary term sheet and a user-specific qualifying maximum, with a slider for amount and 3-, 6- or 12-month repayment terms and corresponding daily rate/fees. The guide says a user may have only one active grant, while eligible users can request a subsequent grant before full repayment; those are distinct eligibility and active-state claims, not an unconditional renewal promise.
- The illustrated flow includes not-qualified, pre-qualified, offer selection, preliminary term sheet, required actions, active and fully repaid screens. For requested loans over EUR 25,000, extra information is described; Terms signing is another required action. One extra-information bullet says the amount is credited after submission, but the adjacent Terms bullet says approval and signature precede credit, and the status table defines **Pending** as signed but not yet paid out. Do not infer that submitting information or signing alone causes an immediate balance-account credit.
- The status table distinguishes Pending, Action needed, Active, Failed, Fully repaid, Revoked and Written off. In that table, Active means approved and paid out to a balance account; Failed includes technical or documentation failure; Revoked says user cancellation and funds returned; Written off says Adyen closed an unpaid grant. These are documented component labels, not verification of any live user's debt balance, repayment finality or accounting result. The active screen supplies bank details for optional unscheduled repayment, and the page says the user may send such repayment only from an Adyen-verified transfer instrument; viewing those details does not execute or confirm a bank transfer.
- The page gives a general EUR 500–50,000 (or supported-currency equivalent) component application range, explicitly subject to individual risk-based qualifying limits. The term sheet distinguishes **remaining amount** excluding fees, **remaining fees**, and **total repayment amount** including grant and fees; a 30-day repayment minimum can lead to further Adyen action if missed. Supported country/region and renewal criteria are linked elsewhere; this page does not establish current user, country, offer or grant eligibility.

## Detail locators

- Opening — nonalterable lender/country notices, UI-managed financing steps, version qualification (raw lines 15–46).
- `Capital Overview component` and `Capital Offer component` — term-sheet/status/repayment views, verified-bank unscheduled repayment route, preliminary offer, amount and term choices (lines 54–99).
- `Standard user flow` — seven screens, >EUR 25,000 extra-information step, Terms/approval wording conflict, active/repaid display and supported-region qualification (lines 101–166).
- `Statuses of a grant` — pending/action/active/failure/repaid/revoked/written-off meanings (lines 168–188).
- `Qualifying limit`, `Variable terms`, `Offer and renewal states`, and `Term sheet` — risk-based range, 3/6/12-month choices, renewal routes and fee-inclusive versus fee-exclusive balances (lines 190–244).
- `Next steps` — Capital component integration and library navigation; this page itself has no session/role setup specification (lines 246–256).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platform-components]]
- Product concept: [[adyen-capital]]

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/capital-component/2026-09-15|2026-09-15 Platforms Capital components guide]]
