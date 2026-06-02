---
title: "CIT and MIT: Customer-Initiated vs Merchant-Initiated Transactions"
type: concept
category: standard
tags: [cards, cit, mit, subscriptions, recurring-payments, card-network-rules, compliance]
---

## Definition

Card networks divide card payments into two types based on who initiates them:

- **CIT (Customer-Initiated Transaction)**: the customer is present and participating in the payment flow (e.g. placing an order on a website)
- **MIT (Merchant-Initiated Transaction)**: the merchant initiates without the customer present, based on a prior agreement (e.g. monthly subscription renewal)

The distinction affects authorization validity periods, compliance requirements, and what actions the merchant can take.

## MIT Requirements

**Prior agreement required**: Must obtain explicit customer consent before initiating any MIT. Agreement must cover:

- Which transactions you're authorized to initiate
- Timing and frequency (scheduled installments, subscription, unscheduled top-ups)
- How payment amounts are determined
- Cancellation policy

Keep a record of each customer's consent.

**Use restriction**: A saved payment method may only be used for the specific purposes the customer consented to. Expanding use requires new consent.

## Card Brand Changes (MIT-specific)

Stripe's Card Account Updater automatically updates saved cards (expired, reissued). Brand changes (e.g. Visa → Mastercard) can occur. When the brand changes:

1. You **must prompt the cardholder to update** their payment method
2. You **cannot charge MIT** until a **new cardholder agreement** is obtained
3. Detect via `payment_method.automatically_updated` event — compare `brand` in `previous_attributes` vs current `card` object

## Authorization Window

The authorization validity period differs between CIT and MIT. Use `payment_method_details.card.capture_before` on the Charge object for the most accurate window.

## Mastercard TLID (2026)

Mastercard is introducing a Transaction Link ID (TLID) requirement:

- **June 2, 2026**: retain TLIDs from CITs that store card credentials + ASI requests
- **October 23, 2026**: send retained TLID with all subsequent MITs ("economically related TLID")

TLID: 22-char alphanumeric case-sensitive identifier; runs in parallel with NTID. Stripe stores and propagates TLIDs automatically. See [[source-stripe-mastercard-tlid]].

## Sources

- [[source-stripe-cit-mit]] — primary source: CIT/MIT definitions, MIT compliance, card brand change rules
- [[source-stripe-mastercard-tlid]] — Mastercard TLID: 2026 requirement timeline, Stripe auto-handling
