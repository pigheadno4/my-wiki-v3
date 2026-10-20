---
title: "Adyen Classic Platforms verification process and account-holder deadlines"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/2026-09-15.md"
tags: [adyen, classic-platforms, verification, account-holders, payouts]
---

## Overview

This 2023-modified page captured 2026-09-15 describes verification of **Classic Adyen for Platforms** account holders before payouts. It explicitly sends new implementations to a newer integration guide. It covers required information, notification-driven deadlines, inactive/suspended/closed status effects, extensions and a restricted unsuspension path; its dates and entity-person rules are captured guidance, not a determination of current legal requirements or an individual holder's eligibility. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The page says account holders must pass verification checks before payouts. Additional information is generally required after a first payment or progression to the next verification tier. Adyen checks data supplied at signup, communicates requirements/deadlines through notification webhooks, and allows revised details/documents after failed verification; successful verification may enable payouts, whereas failure does not (raw lines 19–34).
- Required information depends on legal-entity type, operating country, current tier and applicable legal arrangements. Its organization table defines owner, controller and signatory categories and minimums, including a 25% owner threshold and at least one controller/signatory; treat this dated table as Classic-specific source content, with exact conditions at raw lines 36–55, rather than current-law advice.
- If required information is missing, the captured schedule changes the holder to `Inactive` at 30 days, temporarily disabling payouts while data updates remain possible. After another 42 days in `Inactive`, it changes to `Suspended`: the page says unpaid payments are refunded. A deadline extension of one week is allowed once in each deadline period, and extending inactivation shifts the suspension clock (raw lines 57–68, 87–102).
- The page says a suspended holder may be unsuspended only if no verification check has `FAILED` status. For deadline-based suspension, unsuspension resets a 42-day clock and returns status to `Inactive`, where information can be updated; Customer Area requires Merchant Extended Marketplace role, or POST `/unSuspendAccountHolder` is shown. A successful API request yields a `pspReference` and status-change notification, not proof of completed verification or payout (raw lines 104–134).
- The status table allows payments but no payouts for `Inactive`, and neither activity for `Suspended` or final `Closed`. Its `Active` payouts cell visibly contains both a check and an X, and the description says payouts can be disabled pending required verification data; do not equate `Active` status alone with payout eligibility (raw lines 136–145).

## Detail locators

- Classic-only scope, verification triggers and successful/failed payout boundary: raw lines 19–34. Entity/tier and organization-person criteria: raw lines 36–55.
- Inactivation/suspension deadlines, refund effect, upcoming-deadline notification and timeline example: raw lines 57–85. One-time extensions and required Customer Area role: raw lines 87–102.
- Unsuspension condition, reset, Customer Area/API routes and webhook: raw lines 104–134. Full account-holder status matrix and final closure: raw lines 136–145.

## Related

- [[adyen-classic-platforms]] — Classic platform context and reciprocal route.
- [[adyen-platforms]] — separate current Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/2026-09-15|Classic verification process, captured 2026-09-15]]
