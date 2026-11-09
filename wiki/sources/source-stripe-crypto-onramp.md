---
title: "Stripe — Fiat-to-Crypto Onramp"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp"
raw_files:
  - "stripe-crypto-onramp-2026-11-07.md"
  - "stripe-crypto-onramp-2026.md"
tags: [stripe, crypto, onramp, fiat-to-crypto, kyc, dapp, apple-pay, google-pay]
---

## Summary

The May 11 and November 7, 2026 captures describe [[stripe]]'s fiat-to-crypto onramp, where customers can purchase and exchange crypto through Stripe-hosted, embedded web, or embedded mobile components paths. Stripe says it is merchant of record for these onramp transactions, assumes fraud and dispute liability, and handles regulatory requirements, KYC verification, and sanctions screening. Customers can save payment methods, KYC data, and wallet information with Stripe for return visits. The May overview expressly mentions platform or decentralized application (Dapp); the November short description omits Dapp without stating that Dapp integrations are unsupported. See [[stripe-crypto-onramp]].

## Three Integration Modes

| Mode | Use case and hosting | May 11, 2026 availability wording |
| --- | --- | --- |
| Stripe-hosted | No-code redirect to `crypto.link.com`; Stripe hosts the page; some amount, currency, and network customization | Public preview; apply for access |
| Embedded | Onramp API in a website or mobile webview; brand and parameter customization | Public preview; apply for access |
| Embedded components (mobile SDK) | Native iOS or Android app; SDK and Stripe API integration with more UI customization | Private preview; separate signup linked |

> [!warning] Contradiction
> The May 11 capture assigns preview status to each mode, while the November 7 overview still lists all three but renders a single `Public preview` availability cell without separate embedded or embedded-components status cells. It also omits the earlier mobile private-preview signup. The November row does not establish general availability, public-preview access for mobile components, or whether the May private-preview label still applies to a particular account. Check the relevant integration's current access requirements before planning a rollout.

## Access Requirements

Both captures require submitting an onramp application for any integration, including sandbox or testing access. The captured sequence is to create or sign in to a Stripe account, finish account setup if needed, submit the application, and start sandbox development after approval. Stripe says it reviews **most** applications within **48 hours** and notifies applicants of approval or a need for more information; no specific account's approval or timing is established here.

## Images

![Stripe-hosted onramp](assets/stripe-onramp-stripe-hosted.png)
![Embedded onramp](assets/stripe-onramp-embedded.png)
![Embedded components onramp](assets/stripe-onramp-embedded-components.png)

## Related Pages

- [[stripe-crypto-onramp]] — concept page with dated overview and implementation routes
- [[stripe-stablecoin-payments]] — accepting stablecoin payments is a different product

## Raw Sources

- [[raw/stripe-crypto-onramp-2026-11-07|November 7, 2026 onramp overview]] — later same-URL capture with all three modes, required application, and ambiguous collapsed availability row.
- [[raw/stripe-crypto-onramp-2026|May 11, 2026 onramp overview]] — historical per-mode preview labels, Dapp mention, mobile private-preview signup, and three captured images.
