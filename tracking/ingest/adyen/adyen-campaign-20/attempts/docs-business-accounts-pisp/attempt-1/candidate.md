---
title: "Adyen Business Accounts: PISP payment initiation"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/pisp"
raw_files:
  - "adyen/docs/business-accounts/pisp/2026-09-15.md"
tags: [adyen, business-accounts, open-banking, pisp, payment-initiation, sca]
---

## Overview

This 2026-09-15-captured open-banking guide is for a **third-party Payment Initiation Service Provider (PISP)** initiating a payment on behalf of a consenting Adyen Business Account holder. It separates creation of a payment resource, lookup of the payment's `transactionStatus`, and lookup of a specific authorization's `scaStatus`. A submitted payment, accepted technical/customer stage, or finalized SCA authorization does not by itself show completed settlement or creditor-bank receipt. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- The page identifies the actor as a third-party PISP and requires Adyen open-banking onboarding plus an access token for the Business Account (raw lines 19–33). Holder consent is the basis for the service, but this page does not itself document a new consent grant or show a particular holder's approved consent; see the separate OAuth/consent route.
- To initiate a **single payment**, POST `/payments/target-2-payments` with `instructedAmount`, `creditorAccount`, `debtorAccount`, `creditorName`, and `creditorAddress`. The sample uses a bearer access token, request ID and IP-address header (raw lines 35–79). The creditor is the payee; the debtor is the account to be charged. The sample EUR 0.50 and IBANs are TEST examples, not live payment instructions.
- The creation response carries `paymentId` and a `transactionStatus`, plus links for resource status and SCA status. Its example is `PDNG` (pending). The status catalog distinguishes received `RCVD`, rejected `RJCT`, cancellation `CANC`, several acceptance stages, and creditor/debtor settlement-completed statuses `ACCC`/`ACSC`; the catalog defines possible status meanings, not a guaranteed progression for the example (raw lines 81–119).
- GET `/payments/target-2-payments/{paymentId}` queries payment state; the guide recommends polling at five-second intervals. GET `/payments/target-2-payments/{paymentId}/authorisations/{authorizationId}` queries the **authorization resource** instead. Its `scaStatus` can be selected/started, `finalised` (SCA routine completed), or `failed` (raw lines 121–179). Do not equate `scaStatus: finalised` with `transactionStatus: ACCC` or actual bank receipt.
- The payment-status example returns `RCVD` and `instructedAmount.amount: "-0.50"`, while the initiation request uses `"0.50"` and its immediate response shows `PDNG` (raw lines 49–79, 101–119, 135–148). Treat these as separate illustrative payloads; they do not prove a PDNG-to-RCVD transition or explain the amount sign. The authorization-status curl sample uses `Authorization: Basic {access_token}` although the payment calls use bearer tokens (raw lines 53–58, 129–132, 158–162). Verify the current endpoint authentication contract rather than copying that inconsistent header.

## Detail locators

- Third-party PISP scope, setup and access-token prerequisite: raw lines 19–33.
- Payment creation fields, TEST example and status catalog: raw lines 35–119.
- Payment status polling and example: raw lines 121–148.
- Separate authorization ID, SCA status values and inconsistent authentication-header example: raw lines 150–179.

## Related

- [[adyen-business-accounts]] — Business Accounts context.
- [[source-adyen-docs-business-accounts-oauth-flow]] — separate account-holder OAuth and consent-ID flow.
- [[adyen-partner-oauth]] — distinct merchant-account partner OAuth scope.

## Raw Sources

- [[raw/adyen/docs/business-accounts/pisp/2026-09-15|Captured PISP endpoint guide]]
