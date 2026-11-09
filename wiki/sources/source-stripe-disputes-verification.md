---
title: "Stripe — Card Verification Checks (CVC and AVS)"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/prevention/verification
raw_files:
  - "stripe-disputes-prevention-verification-2026-11-07.md"
  - "stripe-disputes-verification-2026.md"
tags: [stripe, cvc, avs, verification, fraud, disputes, card-checks, radar]
---

## Summary

The May and November 2026 captures give substantively the same guidance on CVC and address verification. Collected CVC, postal code, and billing street address can be passed for issuer checks on card payments. Failed checks can indicate fraud and merit review before fulfillment; a pass or unavailable check is not a guarantee of authorization, safety, compliance, or dispute outcome.

## CVC Check

A CVC or CVV is the three- or four-digit number printed on the card. Stripe says a cardholder physically possessing the card **should** have access to it; that is a security rationale, not proof that only the legitimate holder can know it. If a business requires the CVC with a card payment method during payment or when attaching that method to a customer profile, the issuer verifies it during transaction authorization.

A business can enable a Dashboard Radar rule to block payments that **fail** issuer CVC verification in specified situations. That failed-check rule does not affect payments where the CVC check cannot be performed or is unavailable. Stripe gives wallets such as Apple Pay and off-session payments as examples that **do not require CVC**; this does not mean all such payments universally lack a verification result or bypass every fraud check. Rule behavior depends on configuration and whether the check ran.

Businesses cannot store the CVC. Stripe says fraudsters are therefore unlikely to obtain it through a computer breach, making it useful against that route of fraud. CVC verification does **not** protect against physical card theft or computers and websites with poor security. A failed CVC result is a risk signal, not a verdict on whether the transaction is fraudulent.

## Address Verification (AVS)

When postal code and billing street address are required with a card payment method during payment or attachment, the issuer checks them against the cardholder's address on file. A configured Radar rule can block payments that fail postal code (AVS) verification in specified situations.

AVS can fail for a legitimate customer because of entry errors or a move not yet reported to the issuer. Support varies by country and issuer: some countries do not use postal codes and some issuers do not support street address verification. Stripe says most cards issued in the United States, Canada, and the United Kingdom support street address verification. A match alone does not establish that the cardholder authorized the payment.

## Collection and Results

Stripe recommends collecting CVC, postal code, and billing address so the issuer can run applicable checks; if the required information is absent, the associated check cannot run. Read that general recommendation with the wallet and off-session qualification: those example flows do not require CVC. This guide does not impose a universal CVC collection requirement for every payment flow.

The capture says verification responses appear in the `Charge` object's `source` attribute and on the payment in the Dashboard. It does not establish the exact response shape for every wallet, off-session payment, integration, or API version. Review failed CVC or postal code checks before fulfillment rather than interpreting them as automatic proof of fraud.

## Related Pages

- [[disputes]] — dispute prevention context
- [[stripe-radar]] — Radar rule context
- [[stripe-declines]] — decline and outcome context
- [[stripe]] — provider overview

## Raw Sources

- [[raw/stripe-disputes-prevention-verification-2026-11-07|Stripe card verification checks, 2026-11-07 capture]] — current captured guidance
- [[raw/stripe-disputes-verification-2026|Stripe card verification checks, 2026-05 capture]] — substantively matching earlier guidance
