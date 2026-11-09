---
title: "Stripe — Common Types of Online Fraud"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/prevention/fraud-types"
raw_files:
  - "stripe-disputes-prevention-fraud-types-2026-11-07.md"
  - "stripe-disputes-fraud-types-2026.md"
tags: [stripe, fraud, disputes, stolen-cards, card-testing, friendly-fraud, marketplace-fraud, overpayment]
---

## Overview

The May 10 and November 7, 2026 captures describe the same online-fraud patterns, actors, possible loss, and prevention ideas. The November change is primarily formatting, a CAPTCHA link target, and the marketplace example's “buyers” to “customers” wording; it does not establish a new fraud rule. The existing source's stolen-card loss row needed a correction that was already supported by both captures.

A payment is fraudulent in this page's sense when the cardholder did not authorize it. An issuer's early fraud warning, Stripe's post-authorization suspicion, a successful payment, a cardholder dispute, and a final cardholder-favorable dispute decision are distinct events. A suspicious signal is not proof of fraud; a successful payment does not prove cardholder authorization.

## Seven patterns and consequences

| Pattern | Description and qualified implication |
| --- | --- |
| Suspected fraud | Stripe may notify after issuer authorization, sometimes days after payment, based on later signals; the prediction is not a guarantee. A card issuer's early fraud warning is a separate notification. Review the payment; the page suggests contacting the customer, holding the order, or considering a prompt refund when concerns remain. A **partially** refunded payment can still be disputed for its **full original amount**; the page says fully refunded payments cannot be disputed. |
| Stolen card or details | A fraudulent actor may buy goods or services before the cardholder reports the theft. A processed payment need not have cardholder authorization. **If the subsequent dispute is resolved for the cardholder**, the business loses the payment amount and the value of goods or services already supplied, and is subject to a dispute fee. This is a conditional outcome, not an immediate consequence of every suspicious or disputed payment. |
| Overpayment or fake third-party service | A stolen-card buyer asks the seller to pay an extra sum to a supposed third-party provider, often with a tip. The example's shipper is fraudulent; the seller may have already paid money outside the card network when the actual cardholder disputes the payment. |
| Card testing | An actor checks one or more cards on a low-friction site before using them elsewhere. Donation and “pay what you like” sites are examples, not exclusive targets. CAPTCHA or rate-limiting charges **can help** combat it. |
| Alternative refunds | An actor overpays, claims the original card is closed, and requests a partial refund by check, wire, or another channel. The page advises refunding only through the original payment method; it says a legitimately closed card can still receive a refund and the customer should contact the issuer to retrieve funds. |
| Marketplace fraud | A fraudulent seller takes payment but does not supply the promised goods or services to customers. In the Connect-style example, **if seller funds cannot be recovered**, responsibility for the disputed amount and fee ultimately rests with the platform. That condition is separate from the stolen-card cardholder-favorable dispute outcome. |
| Friendly fraud | A legitimate cardholder later disputes their own purchase, sometimes due to a statement misunderstanding and sometimes deliberately. Verified-address shipping, signature for physical goods, and clearly agreed return policies **can help**. Visa CE 3.0 can use qualifying prior non-fraud transactions from the same cardholder; Stripe says it identifies qualifying history, pre-populates most required response evidence, and allows API self-selection of prior transactions. This may increase the likelihood of overturning a dispute; it does not guarantee evidence acceptance or a win. |

## Detail locators

- Definition, issuer and Stripe warning roles, timing, and partial refunds: November raw lines 9–23; May raw lines 8–22.
- Stolen-card lifecycle and **cardholder-favorable** loss condition, plus overpayment example: November lines 25–39; May lines 24–38.
- Card testing and alternative-refund examples and advice: November lines 41–51; May lines 40–50.
- Marketplace seller-recovery condition and friendly-fraud/CE 3.0 wording: November lines 53–65; May lines 52–64.

## Related

- [[disputes]] — dispute and chargeback concept, including the qualified stolen-card row.
- [[source-stripe-disputes-best-practices]] — prevention guidance.
- [[source-stripe-disputes-visa-ce3]] — Visa CE 3.0 API route. This comparison does not itself establish account eligibility, exact evidence acceptance, or any particular dispute outcome.

## Raw Sources

- [[raw/stripe-disputes-prevention-fraud-types-2026-11-07|November 7, 2026 fraud-types page]]
- [[raw/stripe-disputes-fraud-types-2026|May 10, 2026 fraud-types page]]
