---
title: "Riverty chargebacks | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/riverty-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/riverty-chargebacks/2026-09-15.md"
tags: [adyen, riverty, bnpl, disputes, chargebacks]
---

## Overview

This Adyen webpage explains Riverty's dispute and chargeback flow for invoice payments: a shopper dispute in Riverty, a first Request for Information (RFI) sent by Adyen, optional second RFI for appealing Riverty's decision, and a possible final chargeback. It separately describes a Notification of Fraud for suspected fraudulent orders. This 2026-09-15 snapshot is Riverty-specific guidance, not proof of a merchant's current eligibility, live case state, fee agreement or independently current scheme rule.

## Key takeaways

- Riverty invoice payments are described as immediately settled in full, yet a shopper can still dispute them through the Riverty app. When Riverty notifies Adyen of the dispute, Adyen sends the merchant an RFI. The first RFI is stage 2 (S2) with **14 days** to upload supporting documents; if it expires without response, the dispute is lost in the shopper's favor and becomes a chargeback. Once information is supplied, the merchant cannot edit or add to it at that stage.
- Riverty assesses the first response within **7 days** in the guide. Its decision arrives as an optional second RFI described as stage 4 (S4). A merchant that disagrees can appeal with more documents within **5 days**; ignoring the second RFI accepts the decision by expiry. After that appeal, the guide says there is no further arbitration. The embedded stage-four RFI example still shows `riverty.stageId` as `S2`, so that example does not consistently demonstrate the narrative's S4 marker.
- A suspected-fraud Notification of Fraud normally arrives by webhook within **8 hours** of authorization. The page recommends canceling the transaction or refunding it if already captured. If the notice is sent within Riverty's cutoff time, it says a chargeback is guaranteed if the merchant does neither; a notice after cutoff does not guarantee a chargeback. The page recommends withholding fulfillment until the cutoff passes and not fulfilling after an out-of-cutoff fraud notice.
- If Riverty accepts the supplied information after the second submission, the guide says no further journals are booked and that status is final. If Riverty rejects the defense, it initiates a Chargeback journal and webhook, debits the merchant account, and the chargeback cannot be defended. A dispute fee applies to **certain** chargebacks and appears as `FEE` in the settlement detail report; the page gives no universal fee amount.

## Detail locators

- Introductory flow list — Riverty invoice-payment scope, first and optional second RFI, Information Supplied stages and Chargeback route.
- `## Notification of Fraud` — webhook timing, cutoff fields, cancel/refund and shipping guidance, and in-cutoff versus late-notice consequence.
- `## Request for Information` — dispute webhook and the guide's live India Customer Area route; S2 RFI, 14-day response and expiration result, plus sample additional data.
- `## Information Supplied` — document forwarding, immutable evidence, journal and `INFORMATION_SUPPLIED` webhook.
- `## (Optional) Second Request for Information (RFI)` and `## (Optional) Second Information Supplied` — S4 narrative, five-day appeal, `riverty.decision`, no further arbitration and final decision; compare the sample `riverty.stageId` to the narrative.
- `## Chargeback` and `## Dispute Fees` — final debit and webhook, no defense at chargeback, and fee limited to certain cases.

## Related

- Company: [[adyen]]
- Provider concept: [[adyen-risk-management]]
- Generic background: [[disputes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/riverty-chargebacks/2026-09-15|2026-09-15 snapshot — Riverty dispute and chargeback guide]]
