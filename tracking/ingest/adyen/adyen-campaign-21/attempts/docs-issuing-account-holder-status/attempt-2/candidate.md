---
title: "Adyen account-holder status and inheritance"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/account-holder-status"
raw_files:
  - "adyen/docs/issuing/account-holder-status/2026-09-15.md"
tags: [adyen, issuing, account-holders, status, balance-platform]
---

## Overview

This 2026-09-15-captured Adyen page defines account-holder status and describes Adyen-initiated suspensions/closures, related-resource and shared-legal-entity effects, and **split settlement** routing when account holders cannot receive funds. The payment section concerns supplied split instructions after settlement; it does not establish authorization behavior for an issued-card purchase. [[adyen]] [[adyen-issuing]]

## Key takeaways

- After onboarding and verification, an account holder is `active`. The status table says account holders and balance accounts start active; `active` can move to `suspended` or `closed`, `suspended` to `active` or `closed`, and `closed` permanently disables the resource/capabilities. It also lists `inactive` for payment instruments. See raw lines 19-36.
- **Cross-page conflict:** this page calls `inactive` the initial payment-instrument status and marks it non-editable (raw line 36). The 2026-09-15-captured [[source-adyen-docs-issuing-create-cards]] says cards default `active` and can be explicitly created `inactive` (its raw lines 53, 610), while [[source-adyen-docs-issuing-manage-cards]] describes activating inactive cards. Treat initial card status and the table's `Editable` cell as unresolved across pages; do not use this table to deny activation.
- Adyen may suspend or close an account holder for suspected risk, fraud or terms issues. Its action can be seen through a Customer Area status reason or `balancePlatform.accountHolder.updated` webhook. Only Adyen can reverse an Adyen-initiated suspension. See raw lines 40-49.
- For **Adyen-initiated** status changes, suspending an account holder also suspends related balance accounts, while closing one closes related balance accounts and payment instruments. These effects are observed through the Customer Area status reason or account-holder update webhook, not initiated there. The linked [[source-adyen-docs-issuing-manage-account-holders]] describes a distinct platform API `PATCH` suspension: payout capability is disabled while related balance accounts and payment instruments remain active (its raw line 752). Depending on the reason, capability effects can inherit at the **legal-entity** level to other account holders sharing that entity. The reason/capability/inheritance tables are general guidance, with case-by-case variation, not universal rules. See raw lines 51-85.
- The page says status does not directly stop payment processing where the integration supplies split information after settlement. A split to a suspended holder may settle in that holder's balance account **if pay-in remains available**; if pay-in is blocked, or the holder is closed, the split is directed to the liable account holder's Reserved Incorrect Splits Account. This is documented routing, not evidence of a specific settlement. See raw lines 87-93.

## Detail locators

- Status values and editable transitions: raw lines 25-38.
- Adyen-initiated action signals, resource/legal-entity inheritance and reason tables: raw lines 40-85; platform API contrast in [[source-adyen-docs-issuing-manage-account-holders]], its raw line 752.
- Split-fund routing after settlement: raw lines 87-93.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[source-adyen-docs-issuing-manage-account-holders]] — suspend/reactivate/close procedures.
- [[source-adyen-docs-issuing-create-cards]] — conflicting card initial-status description.
- [[source-adyen-docs-issuing-manage-cards]] — card activation procedure.

## Raw Sources

- [[raw/adyen/docs/issuing/account-holder-status/2026-09-15|Adyen Account holder status, captured 2026-09-15]]
