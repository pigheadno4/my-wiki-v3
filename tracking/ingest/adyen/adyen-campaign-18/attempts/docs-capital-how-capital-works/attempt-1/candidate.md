---
title: "Adyen Capital eligibility and financing lifecycle"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/how-capital-works"
raw_files:
  - "adyen/docs/capital/how-capital-works/2026-09-15.md"
tags: [adyen, capital, business-financing, grants, repayment]
---

## Overview

This 2026-09-15 Adyen Capital guide describes minimum eligibility, a risk-assessed financing offer, Terms acceptance, grant disbursement and repayment for platform users. It also describes a pilot path to additional financing and the offer's principal, fixed fee, daily repayment rate, threshold and maximum period. This is a product/lifecycle description, not a current offer, approval, funded grant, debt balance or bank receipt. See [[adyen]], [[adyen-capital]] and [[adyen-financial-products]].

## Key takeaways

- **Minimum screen, not approval:** The captured minimum requirements include a supported location and legal-entity type, at least 90 consecutive days of Adyen payment processing, volume of at least 1,000 EUR/GBP/USD/AUD for each of three consecutive months, and exclusion of high-risk industries as categorized by payment risk. The page explicitly says these minima do not guarantee an offer. Its country/legal-entity matrix distinguishes Australia, Canada with Saskatchewan and Quebec qualifications, Finland, France, Sweden, UK including Channel Islands/Isle of Man, and US including Puerto Rico; it is a dated eligibility table, not live access proof.
- **Offer to grant:** Adyen configures or requests Capital capabilities in the described integration, underwrites with user payment data, and generates fixed or range offers depending on API-only versus UI-components presentation. An offer includes grant amount, fixed fee and repayment terms. The user must accept Capital Terms of Service for each new grant, even after prior acceptance, before disbursement. API-only integrations present a generated Terms document; UI components include acceptance in their flow. A displayed offer or acceptance step does not itself prove a disbursement.
- **Funding destination:** The grant is initially disbursed to the balance account linked to the user's account holder. The guide says that after this initial disbursement settles, the same grant-configuration API request can instruct a transfer to the user's Adyen-verified bank-account transfer instrument. Treat the balance-account grant and later bank transfer as distinct steps; neither an example nor a request proves beneficiary bank credit.
- **Repayment and renewal:** The default scheduled repayment is described as Adyen reserving/deducting a fixed percentage from processed sales; the offer structure expresses the rate against daily net captured volume. Unscheduled repayment allows early or missed-payment action and requires platform action. Principal plus fixed fee forms total repayment; a 30-day minimum threshold and maximum repayment period qualify the plan, and Adyen may take additional action if the threshold is missed. Subsequent grants are stated to be in pilot: full repayment permits a new-grant path, while partial repayment requires separate eligibility and reserves the prior outstanding principal from the new full grant. A renewal requires fresh underwriting and Terms acceptance; the page does not establish final debt outcome for any user.

## Detail locators

- Eligibility minima, no-guarantee warning and country/legal-entity matrix: pinned raw lines 21-48.
- Lifecycle phases, capabilities, underwriting and API/UI offer variants: pinned raw lines 50-82.
- Per-grant Terms acceptance, disbursement ID and conditional bank transfer: pinned raw lines 84-110.
- Scheduled/unscheduled repayment and pilot subsequent grants: pinned raw lines 112-135.
- Offer principal, fee, daily rate, 30-day threshold and maximum period; integration options: pinned raw lines 137-154.

## Related

- [[adyen-capital]] — main Capital concept and reciprocal source route.
- [[adyen-financial-products]] — financial-products umbrella.

## Raw Sources

- [[raw/adyen/docs/capital/how-capital-works/2026-09-15|Adyen How Capital works, captured 2026-09-15]]
