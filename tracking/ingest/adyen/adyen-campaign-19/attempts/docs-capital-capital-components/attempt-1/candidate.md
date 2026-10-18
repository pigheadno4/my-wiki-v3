---
title: "Integrate UI components | Adyen Capital"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/capital-components"
raw_files:
  - "adyen/docs/capital/capital-components/2026-09-15.md"
tags: [adyen, capital, components, financing, grants]
---

## Overview

This 2026-09-15 Adyen Capital guide describes the Capital Overview and Capital Offer Platform Experience components, their standard financing UI flow, grant/status labels, variable-term options and term-sheet fields. It is a product/component description, not evidence that a particular user qualified, accepted terms, received a funded grant, repaid a debt or received bank funds. See [[adyen]], [[adyen-capital]] and [[adyen-platform-components]].

## Key takeaways

- The source instructs integrators not to alter or hide component text identifying Adyen or its local branch as loan provider, or country-specific legal notices such as US ECOA. It describes disclosures as built into the components and says features vary by library version (raw lines 19–24, 34–46). This is dated provider guidance, not a present legal-compliance certification.
- Capital Overview displays eligibility messages, grant/repayment details, active-grant unscheduled-repayment bank instructions and Terms of Service action; it embeds Capital Offer by default. Capital Offer displays a maximum qualifying amount and preliminary terms and lets users select an amount and a 3/6/12-month repayment option within qualifying limits before applying (raw lines 54–103, 190–205). A shown offer or term sheet is not final grant approval.
- The standard component screens proceed from unqualified/pre-qualified through offer selection, preliminary term sheet, required actions, active and fully repaid views. For requests over EUR 25,000, additional information is prompted; another sentence says grant credit follows approval and signed Terms. The page's “once information is submitted” sentence at raw line 145 does not establish that information alone bypasses approval/Terms at line 146. The flow is for supported regions, with a separate unsupported-region screen (raw lines 101–166).
- For active grants, the UI displays bank details for an unscheduled repayment transfer; the page says the user may send it only from an Adyen-verified bank account/transfer instrument. Displaying or copying details does not prove a repayment transfer, booking, outstanding balance or debt completion (raw lines 151–160).
- The status table distinguishes Pending (request/Terms signed but not yet paid to balance account), Action needed, Active (described as approved and paid out), Failed, Fully repaid, Revoked and Written off; these are status meanings in the dated component guide, not a live grant record (raw lines 168–188). The general EUR 500–50,000 range is conditioned on individual risk assessment/supported currency, and variable rates/fees depend on risk and processing history (raw lines 190–205).
- The preliminary offer sheet has limited detail; the full active-grant sheet can distinguish remaining principal from remaining fees, total repayment including fees, daily net-capture withholding, 30-day minimum and other fields (raw lines 224–244). A rendered figure is not independently reconciled funds or debt proof.

## Detail locators

- Provider disclosure and version qualification: raw lines 19–46.
- Overview/Offer capabilities, 3/6/12-month choices and standard screens: raw lines 54–166.
- Grant status definitions and qualifying/rate conditions: raw lines 168–205.
- Term-sheet field definitions: raw lines 224–244.

## Related

- [[adyen-capital]]
- [[source-adyen-docs-capital-integration-steps-components]]
- [[source-adyen-docs-capital-grant-lifecycle-and-status]]

## Raw Sources

- [[raw/adyen/docs/capital/capital-components/2026-09-15|Pinned Adyen Capital components guide]]
