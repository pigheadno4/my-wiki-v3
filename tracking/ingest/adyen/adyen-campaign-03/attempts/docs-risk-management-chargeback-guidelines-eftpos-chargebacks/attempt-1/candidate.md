---
title: "Adyen Docs: eftpos chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/eftpos-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/eftpos-chargebacks/2026-09-15.md"
tags: [adyen, eftpos, chargebacks, disputes, australia]
---

## Overview

This [[adyen]] guide describes the eftpos dispute sequence for Australia's local debit-card scheme: initial Request for Information (RFI), optional second RFI, and a possible first chargeback. It says eftpos supports in-person and online payments and that most eftpos cards are co-badged. The 2026-09-15 capture has 2023-01-20 `last_modified` metadata; its deadlines and outcomes are snapshot evidence, not current scheme-rule or case-outcome proof. See [[adyen-risk-management]].

## Key takeaways

- At the first RFI, funds have not yet been deducted. The merchant has **14 days** to provide information that helps the cardholder recognize the charge or supports transaction validity. Response is mandatory in the guide: missing the deadline leads to a chargeback that cannot be defended and is final. Customer Area email notification is conditional on subscribing; the RFI list is also available in Customer Area. See raw **Request for Information (RFI)**.
- When Adyen receives and forwards RFI documents to eftpos, it says they cannot be changed, books *InformationSupplied*, and sends `INFORMATION_SUPPLIED`. The issuer has **10 days** to review. If it accepts the defense, the dispute is final at this stage. See raw **Information Supplied**.
- If the issuer rejects the first RFI response, it may request more information through an optional second RFI. The merchant then has **5 days** to respond; missing that mandatory response produces an undefendable final chargeback. After second information is supplied, the issuer has **7 days** to review, and acceptance makes the dispute final. See raw **Optional: 2nd Request for Information (RFI)** and **Optional: 2nd Information Supplied**.
- If the issuer rejects defense or the merchant misses the document deadline, the first chargeback books *Chargeback* and debits the account for the disputed amount. The guide says this chargeback **cannot be defended** and is the final dispute status; defense belongs at the RFI stages, unlike some other scheme flows. The merchant can manage this eftpos flow through Customer Area or, if integrated, the Disputes API and its dispute webhooks. See raw **1st Chargeback** and management sections.

## Detail locators

- Raw opening and **eftpos flow** — local-debit and co-badging context plus the five-stage sequence with optional second RFI.
- Raw **Reason codes and guidelines** — eftpos RFI reason-code navigation.
- Raw **Manage chargebacks using the Disputes API** / **Manage chargebacks in the Customer Area** — route-specific management surfaces.

## Related

- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — general scheme-dependent dispute stages.
- [[source-adyen-docs-risk-management-disputes-api]] — API route.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/eftpos-chargebacks/2026-09-15|eftpos chargebacks (2026-09-15 snapshot)]]
