---
title: "Stripe — Dispute Withdrawals"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/withdrawing"
raw_files:
  - "stripe-disputes-withdrawing-2026-11-07.md"
  - "stripe-disputes-withdrawals-2026.md"
tags: [stripe, disputes, chargebacks, withdrawal, friendly-fraud]
---

## Summary

Stripe's guide to cardholder withdrawals of financial chargebacks, evidence after a withdrawal request, refund limits, fees, and late issuer adjustments. The 2026-11-07 and 2026-05-10 captures retain the same withdrawal rules; the later diff changes presentation and adds related links. Withdrawal is a cardholder request to the issuer, not an immediate win, closure, return of funds, or change in dispute status.

## Key Rules

- **Withdrawal is not a win.** The cardholder asks the issuer to cancel the dispute, but the merchant can still lose without evidence. A withdrawn dispute does not resolve faster, display differently in the Dashboard or API, or stop counting against the card-network dispute rate (new lines 13–21; old lines 12–20).
- **Only financial chargebacks can be fully withdrawn.** An EFW or inquiry has no financial impact and cannot be undone through this withdrawal route, though the cardholder may decline to escalate it (new line 23; old line 22).
- **Refunds remain blocked.** Even after the customer agrees to withdraw, the merchant cannot refund the disputed charge until the issuer decides in the merchant's favor. The issuer's normal dispute timeline can take weeks or months; customer agreement does not accelerate it (new lines 33–37; old lines 32–36).

## Pursuing Withdrawal

Stripe suggests weighing effort against the dispute's value and likely win rate. Its examples say a high-likelihood case can be fought with evidence without customer outreach, while a low-value case can be accepted if the merchant does not wish to invest resources. For customer resolution, ask the cardholder to contact their issuer; the process varies by issuer (new lines 25–33; old lines 24–32). The previous source's “mid-range / relationship matters” row was an editorial inference, not a Stripe-defined category.

The merchant may ask for withdrawal confirmation, such as a bank email or mobile-banking screenshot, and provide it if available, but the guide says this confirmation is **not required** for the issuer response (new line 35; old line 34).

## Submit Evidence

To seek a favorable outcome, submit appropriate evidence even when the customer says they withdrew. Many issuers may treat no response as acceptance of liability. Evidence can be submitted only once and cannot be submitted after the deadline; allow time for the customer conversation without missing that deadline. If withdrawal is not secured in time, still submit evidence against the dispute reason (new lines 39–47; old lines 38–46). The issuer, not Stripe or the customer's assurance, decides the case.

Countering incurs a dispute-countered fee in addition to the dispute-received fee. Stripe says it returns the countered fee on a win, but generally does not return the received fee unless the Stripe contract says otherwise. The countered fee does not apply to businesses in Mexico or Japan. The bank's review can take up to three months (new lines 49–53; old lines 48–52). The linked pricing page and any particular account's fee amount are outside this capture.

## Late Withdrawals

All card networks allow cardholders to **request** a withdrawal after the response deadline, including after a loss. An individual issuer may not support late withdrawal in every case; the cardholder must contact that issuer to learn if it is permitted. A withdrawn dispute generally follows the normal resolution timeline after evidence submission (new lines 55–61; old lines 54–60).

Late adjustments often occur outside network dispute systems. The guide says an issuer **might** take weeks or months to process one, but it is difficult to set a realistic date for when the adjustment will appear in the Stripe account. Neither issuer processing time nor Stripe reflection is guaranteed from the date of cardholder contact (new line 63; old line 62).

## Related Pages

- [[disputes]] — concept page with withdrawal versus win distinction
- [[source-stripe-disputes-how-disputes-work]] — dispute lifecycle and timing
- [[source-stripe-disputes-responding]] — evidence submission

## Raw Sources

- [[raw/stripe-disputes-withdrawing-2026-11-07|Dispute withdrawals guide, fetched 2026-11-07]]
- [[raw/stripe-disputes-withdrawals-2026|Dispute withdrawals guide, fetched 2026-05-10]]
