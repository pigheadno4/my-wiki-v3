---
title: "Stripe — How Disputes Work"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/how-disputes-work"
raw_files:
  - "stripe-disputes-how-disputes-work-2026-11-07.md"
  - "stripe-disputes-how-disputes-work-2026.md"
tags: [stripe, disputes, chargebacks, early-fraud-warnings, inquiries, dispute-fees, chargeback-lifecycle]
---

## Summary

Stripe's guide to the card dispute lifecycle: early fraud warnings (EFWs) and inquiries before a chargeback, formal dispute timing and fees, issuer decisions, and local payment method differences. The 2026-11-07 capture revises the EFW escalation estimate; the 2026-05-09 capture remains historical evidence.

## Pre-Dispute Phase

### Early Fraud Warnings (EFWs)

- Issuer fraud reports from Visa, Mastercard, and JCB include Visa TC40 and Mastercard SAFE. An EFW is a fraud signal, not itself a formal dispute, and requires no response.
- In the 2026-11-07 capture, Stripe says that **about 40% of Visa and Mastercard EFWs become fraud disputes when the charge is not refunded**; the rate varies by network and payment amount. This is an approximate observation, not an account-level prediction or a rate for all networks. The 2026-05-09 capture instead said 80% of EFWs converted if no action was taken without liability shift; retain that as the older dated statement, not the November estimate (new line 32; old line 31).
- Liability shift does not rule out a dispute; in that case Stripe says it automatically provides some evidence, such as 3D Secure data. Automatic refunds of every EFW can refund payments that would never have been disputed.
- Stripe's analysis suggests considering refunds for charges roughly no more than the dispute fee, with charges more than 35% above that fee likely not worth refunding, all else equal. More aggressive refunds can make sense when the dispute's account or business effect matters (new lines 34–46; old lines 33–45).
- A proactive refund does not remove the warning. Only a refund processed as a reversal, usually within two hours of capture, can prevent the fraud *report* itself; this is not a guarantee against a later dispute (new line 38; old line 37).
- EFWs can even arrive after a fraud dispute because reporting and dispute systems differ. The guide links [Early Fraud Warnings API](https://docs.stripe.com/api/radar/early_fraud_warnings) for webhook listening (new line 40; old line 39).

### Inquiries

- An inquiry is a preliminary issuer request, not yet a formal chargeback. American Express and Discover most often use it; the guide says Visa and Mastercard no longer do, while Mexico Domestic disputed charges across brands use inquiries (new lines 48–50; old lines 47–49).
- The guide says satisfactory evidence or a full refund can resolve an inquiry without a dispute fee. A partially refunded charge can still escalate. Failure to answer can lead to a formal, likely unwinnable chargeback; escalation is possible, not automatic (new lines 52–61; old lines 51–60).
- The Dashboard calls these inquiries; API terminology includes `warning`. `warning_needs_response` means evidence has not been provided, `warning_under_review` means evidence awaits issuer review, and `warning_closed` means the inquiry remained open for 120 days without chargeback escalation. At that point the network will not escalate it, but inquiry closure is not a card-network win message (new lines 63–80; old lines 62–79).

## Formal Dispute (Chargeback)

When a formal dispute is filed, Stripe notifies the merchant through the Dashboard, email, webhooks and API, and debits the disputed amount plus a dispute fee from the Stripe balance. Funds remain held while the dispute is open; a refund outside the dispute process is unavailable, and the card-network dispute rate increases. The disputed amount can differ from the original payment (new lines 9–19, 82–99; old lines 8–18, 81–98). The issuer decides the outcome; Stripe facilitates the case but does not control that decision.

### Timing

| Stage | Guide's qualified timeframe |
| --- | --- |
| Cardholder filing | Typically within 120 days of payment; rules allow longer in some cases, and future services can start the window on the event date |
| Merchant response after chargeback | Usually 7–21 days, depending on card network |
| Issuer evidence review | Usually 60–75 days, depending on card network |
| Full lifecycle | Can take 2–3 months; accepting the dispute can shorten it |

See the 2026-11-07 guide lines 101–109 and 2026-05-09 guide lines 100–108. These are typical or possible windows, not guaranteed deadlines for a particular case.

### Dispute Fees

- The dispute-received fee is charged when the cardholder initiates a formal dispute. Outside Mexico it is nonrefundable unless the Stripe contract states otherwise. In Mexico it **might** be returned if the merchant wins or the cardholder withdraws. SEPA businesses incur no dispute-received fee for a card payment processed on the Cartes Bancaires network (new lines 124–130; old lines 121–127).
- Countering a dispute incurs a separate dispute-countered fee in addition to any received fee. It is returned on a win. The guide says it does not apply to businesses in Mexico or Japan; the issuer can take up to three months to decide (new lines 132–136; old lines 129–133).
- The guide directs readers to [Stripe's pricing details](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes#fee-details) for amounts by country; it does not establish a particular account's fee.

### Response, Withdrawals, and Unchallengeable Cases

For an active challengeable dispute, submit evidence by the deadline to seek reversal. A customer saying they withdrew the dispute does not itself close the chargeback in the merchant's favor; Stripe says a response with evidence is still needed (new lines 138–149; old lines 135–146).

Some disputes cannot be challenged under network rules or local regulation and are generally closed as lost immediately without an evidence opportunity. The guide names unanswered Discover inquiries, Cartes Bancaires card payments processed by SEPA businesses (not merely cards issued by Cartes Bancaires elsewhere), and Nigerian payment methods (new lines 151–167; old lines 148–164).

Rarely, one payment can have multiple disputes, each requiring separate acceptance or response. A disputed amount can differ due to currency conversion, bundled recurring charges, partial disputes, or full disputes after a partial refund. The guide's amounts are examples rather than a promise of the amount in a real case (new lines 169–184; old lines 166–181).

### Decision and Late Wins

The issuer's decision changes the formal dispute to `won` or `lost`. On a win, the chargeback amount returns to Stripe and then the merchant; on a loss, no new merchant-side movement is needed because Stripe already credited the issuer. An ordinary lost dispute cannot be overturned by the merchant or customer, and Stripe does not support arbitration escalation. A customer can withdraw even after loss, but withdrawal is not itself a win. Rare issuer-driven credits or corrections can later change `lost` to `won` as a **late win**; Stripe says it cannot predict when or why (new lines 111–122, 186–196; old lines 110–119, 183–193).

## Local Payment Method Disputes

The lifecycle above primarily describes cards. Local payment methods such as Klarna and PayPal have their own decision-makers, windows, fees, evidence deadlines and sometimes inquiries. The guide says LPMs typically allow up to 180 days to file versus the common 120-day card window, but the exact process depends on the method (new lines 198–212; old lines 195–209).

## Related Pages

- [[disputes]] — cross-provider dispute concept and Stripe lifecycle route
- [[stripe-declines]] — decline types and Radar blocking
- [[stripe-3d-secure]] — 3D Secure and liability shift
- [[source-stripe-declines-overview]] — declines overview

## Raw Sources

- [[raw/stripe-disputes-how-disputes-work-2026-11-07|Stripe card dispute lifecycle guide, fetched 2026-11-07]]
- [[raw/stripe-disputes-how-disputes-work-2026|Stripe card dispute lifecycle guide, fetched 2026-05-09]]
