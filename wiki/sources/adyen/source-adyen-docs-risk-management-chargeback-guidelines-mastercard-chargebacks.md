---
title: "Adyen Docs: Mastercard chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/mastercard-chargebacks/2026-09-15.md"
tags: [adyen, mastercard, chargebacks, disputes]
---

## Overview

This [[adyen]] webpage snapshot describes Mastercard chargeback stages, merchant defense, conditional pre-arbitration, and scheme arbitration. Its 2026-09-15 capture carries 2019-10-08 `last_modified` metadata. The stated windows and fee are dated documentation evidence, not proof of current scheme policy, an account's eligibility, or a case outcome. See [[adyen-risk-management]].

## Key takeaways

- Notification of Chargeback (NoC) can arrive after a payment becomes Settled or Refunded; it signals a forthcoming debit, usually a few days later. At the first chargeback Adyen assigns the issuer-initiated dispute for merchant review, books *NotificationOfChargeback* and *Chargeback*, sends a `CHARGEBACK` webhook, and debits the disputed amount. The merchant may accept through Customer Area or the Disputes API, closing defense, or defend through either route with reason-specific documents. See raw **Notification of Chargeback** and **Chargeback**.
- The guide says defense documents are due within **40 days**. They must address the reason code; an order overview alone is insufficient. Submission is described as irreversible and documents are automatically sent to the issuing bank. Once Adyen receives and forwards the material, it says the documents cannot be changed and *InformationSupplied* is booked. The page also says later information is possible if it was not available before, in tension with its broader no-later-information and no-change wording. It does not explain a route or conditions for that exception; do not assume submitted files can be replaced. See raw **Chargeback** and **Information Supplied**.
- *Chargeback reversed* returns the disputed amount while the issuer is still reviewing the defense. The page calls this final **if the issuer accepts**. If the issuer does not accept, reason codes **4808, 4870, and 4871** bypass pre-arbitration and go directly to Scheme Arbitration if escalated. Other reason codes can reach pre-arbitration; the issuer has **45 days from the Information Supplied date** to file it under this guide. See raw **Chargeback Reversed** and **Pre-Arbitration**.
- Pre-arbitration is accepted if its response time expires. A merchant can ask Adyen Support to decline on their behalf; self-acceptance or self-decline requires eligibility plus Adyen configuration and approval. Acceptance loses the dispute and produces a second chargeback. Decline can lead to Scheme Arbitration and significant additional costs. A second chargeback after merchant or Adyen acceptance is final and permits no new defense documents. See raw **Pre-Arbitration** and **Second Chargeback**.
- If the issuer accepts a declined pre-arbitration, the guide calls the case won; otherwise the issuer may file Scheme Arbitration. Mastercard then rules on liability. If Mastercard rules for the issuer, the merchant can incur a fee of **up to USD 600**, added to the second chargeback, and the process can take months. See raw **Scheme Arbitration**.

## Detail locators

- Raw opening stage list and **Mastercard flow** outline the path; reason codes 4808, 4870, and 4871 have the direct-arbitration exception.
- Raw **Reason codes and guidelines** links to Mastercard chargeback and Notification of Fraud reason-code references.

## Related

- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — general dispute-stage context.
- [[source-adyen-docs-risk-management-disputes-api]] — API handling route.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/mastercard-chargebacks/2026-09-15|Mastercard chargebacks (2026-09-15 snapshot)]]
