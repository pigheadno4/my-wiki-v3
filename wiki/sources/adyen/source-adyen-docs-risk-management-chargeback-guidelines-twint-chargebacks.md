---
title: "Adyen TWINT chargebacks"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/twint-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/twint-chargebacks/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, twint]
---

## Overview

This [[adyen]] guide describes the TWINT chargeback flow within [[adyen-risk-management]], including the shopper initiation window, merchant defense window, document submission, journal and webhook events, and resulting debit. The periods and fee statement are from a 2026-09-15 snapshot; an individual dispute's current deadline and fees require case-specific verification.

## Key takeaways

- A shopper can initiate a TWINT chargeback directly with TWINT up to 100 days after the payment, refund, or expected receipt of goods or services. When TWINT opens the dispute, the merchant has 10 calendar days to defend and the disputed funds have not yet been charged back.
- If the merchant does not respond within that 10-day window, the dispute is lost and the funds are charged back. If the merchant defends in time and wins, the guide says there is no account debit. The page states that there are “currently no chargeback fees for TWINT” in this captured version; it is not a guarantee of later fee policy.
- At Notification of Chargeback (NoC), the dispute is assigned in Customer Area and a `NOTIFICATION_OF_CHARGEBACK` webhook is sent, while the `Chargeback` journal and account debit have not yet occurred. Accepting loses the dispute, ends defense, and debits the payment amount. To defend, upload the complete package through Customer Area or the Disputes API; the guide says there is no later opportunity to add information.
- After Adyen receives the defense, `InformationSupplied` is booked and the documents can no longer be changed. Adyen then forwards them to TWINT and books `AcquirerPreArbitrationUploaded`, usually soon after. If TWINT has not notified Adyen of a loss 45 calendar days after that journal's booking, the dispute can be considered won and a `PREARBITRATION_WON` webhook is sent. A loss produces both `PREARBITRATION_LOST` and `CHARGEBACK` webhooks.
- A chargeback is the final status when the merchant accepts it or TWINT refuses the defense: the amount is debited, the `Chargeback` journal is booked, and a `CHARGEBACK` webhook is sent. This TWINT sequence and its clocks should not be generalized to other schemes.

## Detail locators

- `# TWINT chargebacks`, raw lines 15–30 — initiation window and its three possible starting events, 10-day defense, no-debit win, dated fee statement, 45-day conditional won path, and flow list.
- `## Notification of Chargeback`, raw lines 34–45 — NoC and webhook, no initial debit, acceptance/defense choices, and complete defense package.
- `## Information Supplied`, raw lines 47–49 — document lock, journal, and webhook.
- `## Acquirer Pre-arbitration uploaded`, raw lines 51–53 — forwarding to TWINT and `AcquirerPreArbitrationUploaded` journal.
- `## Chargeback`, raw lines 55–57 — accepted or refused-defense finality, debit, journal, and webhook.
- `## Reason codes and guidelines`, raw lines 59–61 — route to TWINT reason-code requirements.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk and dispute source routes.

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/twint-chargebacks/2026-09-15|TWINT chargebacks (2026-09-15 snapshot)]]
