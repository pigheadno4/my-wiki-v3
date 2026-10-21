---
title: "Adyen Marketplace Capital components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/capital-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/capital-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, capital, ui-components, business-financing]
---

## Overview

This 2026-09-15 Marketplace-path Platform Experience guide describes **Capital Overview** and **Capital Offer** UI components for presenting Adyen Capital business-financing offers and grant information to eligible users. Overview can show status, term sheet, required actions and repayment progress; Offer can show a qualifying limit, amount/term choices and a request flow. The page says components handle offer, Terms and payout API interactions, but a rendered offer, signed Terms, submitted request or displayed status alone is not independent evidence of funding or repayment. See [[adyen]], [[adyen-platform-components]] and [[adyen-capital]].

## Key takeaways

- **Required disclosures and version:** Adyen says the components include product disclosures and warns not to alter or hide text naming Adyen or its local branches as the loan provider, or country-specific legal notices such as the US ECOA notice. Preserve that wording alongside the page's “grant” and “business financing” terminology. Features may differ by library version; this page links to a separate integration guide and does not specify an API credential role or minimum version. This dated snapshot is not a present-day legal or eligibility determination (raw lines 19–47, 247–256).
- **Views and choices:** Capital Overview shows user eligibility messages, Terms signing, active grant terms, progress and bank details for unscheduled repayment. Capital Offer shows a preliminary term sheet and user-specific qualifying maximum; the amount slider and risk/processing-based 3-, 6- or 12-month term options display corresponding rates/fees. A user may request a subsequent grant before full repayment only if eligible, although the status table says there can be only one active grant. The general component application range is EUR 500–50,000 or supported-currency equivalent, constrained by each user's risk-based limit (raw lines 54–99, 190–223).
- **Actions, regions and credit ambiguity:** The illustrated flow covers ineligible, pre-qualified, offer, preliminary term sheet, required actions, active and fully repaid screens, with a separate unsupported-region screen. A requested loan over EUR 25,000 prompts extra information. Its extra-information bullet says the grant is credited after submission, while the adjacent Terms bullet says approval and signed Terms precede credit; **Pending** explicitly means signed but not yet paid out. The page therefore does not justify an immediate-credit promise from submitting information or signing alone. Unscheduled repayments require an Adyen-verified bank account/transfer instrument; showing bank details does not send or confirm a repayment (raw lines 101–166, 180–188).
- **Status and money boundary:** The component labels Pending, Action needed, Active, Failed, Fully repaid, Revoked and Written off. In this source, Active denotes approved and paid out to the user's balance account; Failed includes technical or incomplete-documentation cases; Revoked says user cancellation and funds returned; Written off denotes Adyen closure after non-repayment. These are documented display definitions, not an actual user's accounting record or bank-receipt proof. The term sheet separates outstanding principal from fees and total repayment amount, and describes a 30-day minimum that may prompt further Adyen action if missed (raw lines 168–188, 226–245).

## Detail locators

- Disclosure wording, component purpose and library-version qualifier: pinned raw lines 19–47.
- Overview/Offer functions, term choices and conditional renewal: pinned raw lines 54–99.
- Seven-screen flow, >EUR 25,000 action, credit-wording conflict, verified-bank repayment and region gate: pinned raw lines 101–166.
- Grant status table: pinned raw lines 168–188.
- Risk-based qualifying range, variable terms, renewal state and term sheet: pinned raw lines 190–245.
- Separate Capital integration guide: pinned raw lines 247–256.

## Related

- [[adyen-platform-components]] — main component-suite concept.
- [[adyen-capital]] — separate business-financing product and eligibility context.
- [[source-adyen-docs-platforms-components-overview-after-payment-capital-component]] — parallel Platforms-path snapshot.
- [[adyen-financial-products]] — umbrella product context; not a grant decision.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/capital-component/2026-09-15|Marketplace Capital components, captured 2026-09-15]]
