---
title: "Braintree ACH Direct Debit Server-side Implementation (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/server-side/node"
raw_files:
  - "braintree/docs/guides/ach/server-side/node-2026-09-16.md"
tags: [braintree, ach, direct-debit, nodejs, server-side, vaulting, verification]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide describes the Node.js server-side flow for ACH Direct Debit after a custom JavaScript v3 client supplies a payment-method nonce. The page limits availability to eligible merchants that can build that custom client integration and states that ACH Direct Debit is not available in Drop-in UI; the snapshot does not establish current eligibility or enablement. It routes three verification choices—network check, micro-transfers and independent check—through Vault storage before a vaulted token is used for a transaction. See [[braintree-payment-methods]] for the provider-wide method route.

## Key takeaways

- Vaulting is required to begin verification and transacting: the server calls Payment Method Create with the client nonce, customer ID and the selected US bank-account verification method. The callback and Promise examples are under **Vaulting the payment method** (lines 68–95).
- Network check requires a separate verification decision after vaulting. A successful vaulting result does not prove the bank account was verified; the page directs the integration to inspect the payment method's verification status and optionally its most recent processor response code. The customer-verification add-on is optional and applies only to network check. See **Verification Add Ons** (lines 97–125) and **Checking for successful verification** (lines 128–144).
- Micro-transfers require the merchant to collect the two micro-deposit amounts in its own UI, confirm them in a separate call, wait for settlement, and then look up the verification until it is verified, pending or failed. Before confirmation, the vaulted bank account is neither verified nor transactable. See **Confirming micro-deposit amounts** (lines 145–167) and **Looking up individual verification status** (lines 170–204).
- Once the relevant verification path permits transacting, the all-method transaction example passes the vaulted payment-method token and client-collected device data to Transaction Sale and requests settlement submission. This is an example request, not proof of a successful debit, settlement or funding. See **Creating transactions / From payment method tokens** (lines 205–250).
- Retrying verification applies to network check and micro-transfers. The page permits repeated attempts with the same or a different verification method, but Payment Method Update cannot replace the bank-account details on a vaulted US bank account; new bank information requires creation of a new payment method. See **Retrying verifications** (lines 255–289).
- Webhooks apply to all three verification methods and can notify the merchant of ACH transaction-status changes. General setup and transaction-notification detail remain in the linked webhook documents. See **Setting up webhooks** (lines 294–302).

## Material boundaries

- This source is a captured, unversioned website guide for the Node.js server-side route. It is not package-qualified SDK implementation evidence, current service availability, merchant or buyer eligibility, account enablement, bank-account ownership proof, or successful transaction, settlement or funding evidence.
- The client-side prerequisite is specifically a custom JavaScript v3 integration, and the captured page says the method is unavailable in Drop-in UI. Do not generalize this page to other client SDKs or interfaces.
- At line 144, the captured sentence reads, "If the payment method has been markedon any attempt, it will be transactable"; the status word or formatting after "marked" is missing. This damaged rendering is not sufficient to reconstruct which mark makes the method transactable.
- The retry examples and backup-method discussion are guidance and examples. They do not guarantee that a particular verification attempt or transaction will succeed.

## Detail locators

- Availability and client/UI qualification: lines 21–22
- Verification-method flow map: lines 25–65
- Vault creation and verification-method selection examples: lines 68–95
- Network-check-only verification add-on: lines 97–125
- Network-check success inspection and damaged transactable sentence: lines 128–144
- Micro-transfer amount confirmation and settlement wait: lines 145–167
- Micro-transfer verification-status polling: lines 170–204
- Vaulted-token transaction examples: lines 205–250
- Retry choices and vaulted-bank-detail immutability: lines 255–289
- ACH transaction-status webhooks: lines 294–302

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/ach/server-side/node-2026-09-16|Braintree ACH server-side Node.js guide (captured 2026-09-16)]]
