---
title: "Stripe Docs — Strong Customer Authentication (SCA) exemptions"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions"
raw_files:
  - "stripe-payments-3d-secure-strong-customer-authentication-exemptions-2026-11-07.md"
  - "stripe-sca-exemptions-2025.md"
tags: [stripe, sca, 3d-secure, exemptions, tra, low-value, mit, data-only, eea, uk, liability-shift]
---

## Summary

The 2026-05-08 and 2026-11-07 captures describe SCA exemptions and Data Only for EEA, Switzerland, and UK card payments. Stripe **requests applicable exemptions** on the merchant's behalf; the customer bank decides whether to approve. A nominal low-value amount or risk classification does not guarantee a frictionless payment or remove the issuer's ability to require SCA (new raw lines 9–21). The captures give dated thresholds and access descriptions, not a live account-eligibility or legal-compliance determination.

## Bank-approved exemptions and liability

When the customer's bank approves an exemption request, fraudulent-transaction liability does **not** shift to the issuer (new raw line 13). That statement is about a bank-approved exemption. Merchant-initiated transactions and Data Only have their own scope and liability statements below; neither is evidence that the bank approved a different exemption.

| Route | Captured conditions |
| --- | --- |
| **Low Value** | Transaction amount below 30 EUR or 25 GBP. Even then, the issuer might require SCA when cardholder-initiated transactions since the last SCA cumulatively exceed 100 EUR or 85 GBP, or after five such transactions (new raw lines 19–21). |
| **TRA / Low Risk** | The provider's overall relevant card-fraud rate must stay below 0.13% for up to 100 EUR/85 GBP, below 0.06% for up to 250 EUR/220 GBP, or below 0.01% for up to 500 EUR/440 GBP; local equivalents can apply (new raw lines 22–28). These are qualifying ceilings, not guarantees of an issuer-approved exemption. |
| **Merchant-initiated transaction (MIT)** | A saved-card, off-session later charge may qualify as MIT and is technically outside SCA scope. Authenticate the card when saved and secure the customer's agreement or mandate for later charges. The guide analogizes its treatment to an exemption, saying the MIT path has no customer challenge or liability shift; this description does not establish that every future charge is correctly classified or cannot require action (new raw line 29). |

## Dated TRA access limits

The capture says the TRA ceiling available to a Stripe user depends on Stripe's overall fraud rates and access to authentication offerings **including** Adaptive Acceptance. It reports qualifying low-risk amounts up to 250 EUR for EEA merchants and 220 GBP for UK and Swiss merchants (new raw lines 31–36). “Including” does not make Adaptive Acceptance a universal prerequisite, and the captured “currently” wording does not prove any particular account's access today.

## Data Only

Data Only is supported by some card schemes and uses 3DS data. The **authentication request goes to the card network**, which includes risk data in an authorization message sent onward to the issuer. Thus the issuer does receive an authorization message, though it does **not** receive an issuer authentication request in this flow. The guide says **successful** Data Only requests can offer a frictionless experience and improve approval rates for payments **not subject to SCA**; this is a qualified product claim, not an observed outcome for an account (new raw lines 38–40). Data Only does **not** shift fraudulent-transaction liability to the issuer (new raw line 42).

The **standard Data Only flow** requires 3DS 2.2 or later. Mastercard Identity Check Insights is separately named; the capture says Stripe offered it to Adaptive Acceptance **and Authorisation Boost** users in the EEA and UK at capture time. It does not state the standard-flow 3DS-version prerequisite for every Mastercard product or establish eligibility for every user of either program (new raw line 44). The November capture adds a link to a separate Data Only guide that mentions Data Share Only and DCAP (new raw line 46); that guide's detailed behavior was not captured in this unit.

## Related pages

- [[stripe-3d-secure]] — 3DS concept and SCA exemption route
- [[stripe-authorization-boost]] — authentication and authorization optimization context
- [[stripe]] — provider

## Raw Sources

- [[raw/stripe-payments-3d-secure-strong-customer-authentication-exemptions-2026-11-07|2026-11-07 SCA exemptions capture]]
- [[raw/stripe-sca-exemptions-2025|2026-05-08 earlier SCA exemptions capture]]
