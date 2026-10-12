---
title: "Adyen Docs: PayPal chargeback process for marketplaces"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-guidelines/paypal-chargebacks"
raw_files:
  - "adyen/docs/risk-management/chargeback-guidelines/paypal-chargebacks/2026-09-15.md"
tags: [adyen, paypal, marketplaces, disputes, chargebacks]
---

## Overview

This [[adyen]] guide describes PayPal dispute handling for a marketplace's sellers through Adyen's Disputes API or Customer Area. A buyer can dispute a PayPal payment through a bank/card issuer or with the seller or PayPal Resolution Center. When PayPal informs Adyen, Adyen says it cannot identify the relevant marketplace seller, so the marketplace must implement seller-level dispute handling and respond on the seller's behalf. PayPal decides the defense outcome; the Adyen webhooks, journals, and reports reflect that process. This is a 2026-09-15 documentation snapshot, not proof of current case eligibility, fee terms, or a specific outcome.

## Key takeaways

- A PayPal dispute can begin at inquiry/Request for Information (RFI) or claim/Notification of Chargeback (NoC), depending on reason code. At inquiry, the seller and shopper can discuss resolution; the marketplace can fully refund, fully accept, offer a PayPal-approved partial acceptance, or wait for claim. A full refund creates an Adyen refund, while full acceptance creates an Adyen chargeback. The guide says an RFI has a 20-day response period before claim escalation, which the shopper may also initiate. Defense is unavailable until claim. See **How PayPal disputes work → Inquiry stage**.
- At NoC/claim, the marketplace can accept the chargeback and lose defense rights, or submit evidence. The guide says there are 10 days to respond before escalation and only one attempt to submit all defense information after NoC; documents then cannot be changed. The response should address the particular reason code, not merely recap the order. See **Claim stage**, **Notification of Chargeback**, and **Defend a dispute**.
- Once Adyen forwards the submitted documents to PayPal, PayPal either accepts the defense (`PREARBITRATION_WON`) or rejects it, leading to a final `CHARGEBACK` that debits the account and cannot be defended again. See **Information supplied** and **Chargeback**.
- The page's **Defend a dispute** subsection also says an API response to an RFI needs a defense reason code, while its inquiry and NoC sections say defense documents cannot be submitted until NoC. Preserve this internal wording conflict; it does not establish an RFI defense submission path. The evidence and reason-code tables are raw snapshot locators, not a universal PayPal dispute taxonomy.
- Operational edge cases matter: PayPal can send multiple disputes for one payment, for which the guide says to respond to the most recent; a partial offer can leave Adyen showing "Dispute Defense Period Ended" while PayPal remains open; and Adyen freezes its expiration at case creation even if PayPal's period later changes. An active dispute can block a refund, so the guide directs merchants to follow the dispute process. See **Common dispute scenarios**.
- Dispute fees are recorded as `PaymentCost`: the page describes an administration fee and an extra lost-dispute fee, with no dispute fee when Seller Protection covers the case. It says PayPal may occasionally hold funds for a prospective chargeback, subject to account confirmation. See **Dispute fees**; these statements are source and account qualified.

## Detail locators

- **Opening, lines 19–28** — buyer, seller, marketplace, PayPal, and Adyen roles; response urgency.
- **How PayPal disputes work, lines 30–55** — inquiry versus claim, RFI versus NoC, refund/accept/offer effects, and response periods.
- **Request for Information / Notification of Chargeback, lines 75–107** — webhooks, Customer Area routes, reason codes, one-time defense, and loss on acceptance.
- **Defend a dispute / Information supplied / Chargeback, lines 107–152** — evidence examples, RFI-wording conflict, final document submission, PayPal decision, and final debit.
- **Dispute fees, lines 154–159** — `PaymentCost`, Seller Protection qualification, and possible account-specific hold.
- **Common dispute scenarios, lines 161–191** — multiple cases, partial offers, differing expiration periods, blocked refunds, and offer rejection.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[disputes]]
- [[source-adyen-docs-risk-management-disputes-api]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-guidelines/paypal-chargebacks/2026-09-15|Adyen Docs — PayPal chargeback process for marketplaces (2026-09-15)]]
