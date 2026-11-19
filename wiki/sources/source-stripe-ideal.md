---
title: "Stripe: iDEAL | Wero Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ideal"
raw_files:
  - "stripe-payments-ideal-2026-11-07.md"
  - "stripe-ideal-2025.md"
tags: [stripe, ideal, wero, netherlands, eur, bank-redirect, authenticated, sepa-debit, kvk]
---

## Overview

The May 3 and November 7, 2026 full captures describe iDEAL | Wero (formerly iDEAL) as a Netherlands-based, customer-initiated online bank payment method. A Dutch customer pays in **EUR**, redirects to their bank to authenticate with a second factor, and Stripe describes immediate notification of payment success or failure. The bank experience varies. The captured merchant-location list includes 40 Stripe account countries; this differs from the Netherlands customer location. Listing an account country or product does not establish a particular merchant's enablement, buyer authentication, payment execution, settlement, or a specific SDK flow.

## Migration notice, dated to the captures

Both captures repeat Stripe's notice that Wero acquired iDEAL, integrations should be rebranded to **iDEAL | Wero in Q1 2026**, and merchants should **switch to Wero during 2026 and 2027** to continue accepting bank redirects from Dutch customers. The Q1 instruction was already in the May 3 capture and is past relative to the November 7 capture. The repeated notice does not establish a later exact cutoff, completion for any merchant, or replacement of a particular API or SDK. See the separately linked Wero migration guide for implementation details.

## Method properties and setup

- **Customer and currency**: customers in the Netherlands; presentment in EUR. The captured page lists 40 eligible Stripe account locations separately from payer location.
- **Bank flow**: customer-initiated authenticated bank transfer with redirect, second-factor authentication, and immediate payment outcome notification. Manual capture support is **No**.
- **Recurring**: the overview points to **SEPA Direct Debit** for recurring payments; it does not itself specify a saved mandate, later off-session charge, or subscription implementation.
- **Products**: Connect, Checkout, Payment Links, Subscriptions, Invoicing, and Elements are listed. Standard payout timing is stated; no specific payout date is guaranteed.
- **Front-end display**: for Stripe front-end products, enable iDEAL in the Stripe Dashboard payment-method settings. Stripe then determines relevant methods to display. The page routes to hosted Checkout and Elements quickstarts, with Invoicing and Payment Links also configurable from Dashboard. This setup/display step does not authenticate the buyer or prove payment success. The November Elements quickstart link differs from May's link, without evidence here of SDK or endpoint removal.
- **Manual or future-use paths**: the overview links separate accept-a-payment and save-details guides and a GitHub sample. Their links are navigation; this overview alone does not define their client/server or version conditions.

## Disputes, refunds, and registration

The captures say customers cannot dispute iDEAL | Wero payments with their bank and should contact the merchant with concerns. Full and partial refunds are supported. A payment can be refunded up to **180 days after the original payment**; a refund can remain `pending` for **up to seven days**, and is considered successful after seven days only **if no failure signal is received**. Immediate payment outcome notification is distinct from refund finality and from settlement.

For website registration, a Netherlands-based business must clearly show its **KVK Chamber of Commerce company registration number**; a business based elsewhere must display its equivalent local official registration number. For Connect, the connected account's name must map to its **actual business**, not the platform, because customers see that name during the payment flow.

## November 7, 2026 eligibility category addition

The November capture adds a list **in addition to** Stripe's general prohibited and restricted business categories. It says the following are **prohibited or restricted** from using iDEAL | Wero: adult content, entertainment and sex-related products or services; cannabis businesses except cannabidiol (CBD); NFTs; payment facilitators processing for sub-merchants; peer-to-peer money transfers; contracts for difference; weapons and firearms; donation-based crowdfunding; creator economy and live-streaming businesses; open-loop gaming; traders in precious metals or minerals; and businesses whose activities are prohibited by applicable law or regulation, with examples including terrorist financing, human trafficking, illegal narcotics dealing, and shell banks (new raw lines 165-180). The page groups these under one combined label; it does **not** classify each listed category individually as prohibited versus restricted or establish any particular merchant's eligibility. The older full capture ends after its Connect section and has no such list (old raw lines 153-159).

## Related

- [[stripe]] — company context.
- [[stripe-ideal]] — iDEAL | Wero concept and connected source routes.
- [[stripe-sepa-debit]] — SEPA Direct Debit used for recurring payments.

## Raw Sources

- [[raw/stripe-payments-ideal-2026-11-07|November 7, 2026 iDEAL | Wero overview]] — full 180-line page, including the new eligibility category section.
- [[raw/stripe-ideal-2025|May 3, 2026 iDEAL | Wero overview]] — prior 159-line page; MP4 payment-flow demonstration remains an external URL.
