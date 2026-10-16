---
title: "Adyen Salesforce OMS authorization reversal"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/authorization-reversal"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/authorization-reversal/2026-09-15.md"
tags: [adyen, salesforce-oms, authorization-reversal, cancellation, webhooks]
---

## Overview

This 2023-last-modified Salesforce Order Management System (OMS) guide explains enabling and requesting **Salesforce Authorization Reversal** through its Payment Authorization Reversal Service API and the Adyen OMS package. In Adyen's integration, the reversal maps to **cancelling an uncaptured payment authorization**, such as when an order cannot be fulfilled. It is distinct from a refund of captured funds or cancelling the Salesforce order itself. The page gives setup and outcome checks; it does not prove a live reversal or a shopper's issuer hold release.

## Key takeaways

- Requirements are a functioning Salesforce OMS Org connected to an SFCC storefront, the Adyen OMS package **v3.1.0 or later**, and Salesforce's reversal API guidance. The Salesforce site must expose the Adyen non-payment webhook handler Apex class. The page does not specify an operator role or universally supported order state.
- For **OMS 3.3.0 or later**, an additional Authorization Reversal webhook configuration is not required. For the described manual setup, use the merchant account handling captures/refunds, configure a standard JSON webhook to the Salesforce site non-payment endpoint, use the existing HMAC key, and select `CANCELLATION`. The package cancels the payment for the Salesforce order; cancelling the **order** requires the implementer's own logic.
- The Salesforce reversal request's `amount` must match **Available to Capture** on the Order Payment Summary object. This is an authorization/cancellation condition, not a request to refund or capture money.
- Salesforce `PaymentGatewayLog` records `InteractionType: AuthorizationReversal` and a `GatewayResultCode`; the page says the **final outcome comes asynchronously from Adyen's CANCELLATION webhook**. Its `originalReference` is the original authorization PSP reference. `success=true` means the cancel request succeeded; `success=false` includes a reason. Example payloads are illustrative test examples, not actual merchant events.
- Failure handling is not a blind retry: the webhook section says to review the reason, fix the issue if possible, and resubmit; the final paragraph instead directs a failed reversal to manual reversal in Adyen Customer Area. Preserve that difference and verify the specific original authorization and current state before another action, to avoid duplicate or conflicting cancellation attempts. Neither a log state nor this guide confirms issuer-side hold release or settlement effects.

## Detail locators

- Raw lines 15–27: Salesforce reversal purpose, Adyen cancel mapping and OMS/package prerequisites.
- Raw lines 29–82: Salesforce site Apex access, version-specific webhook setup, HMAC and payment-versus-order cancellation boundary.
- Raw lines 84–92: request through Salesforce API, Available to Capture amount and asynchronous outcome.
- Raw lines 94–114: Salesforce gateway logs versus Adyen `CANCELLATION` webhook fields and failure reason.
- Raw lines 116–170: illustrative success/failure payloads and differing final failure guidance.

## Related

- [[adyen]] — provider context.
- [[adyen-salesforce-order-management-system]] — OMS package and order-management payment operations.
- [[adyen-salesforce-commerce-cloud]] — separate connected storefront integration.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/authorization-reversal/2026-09-15|Salesforce OMS authorization reversal, fetched 2026-09-15]]
