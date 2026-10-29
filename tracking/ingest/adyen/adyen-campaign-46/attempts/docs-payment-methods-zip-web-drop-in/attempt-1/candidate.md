---
title: "Adyen Zip Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/zip/web-drop-in/2026-09-15.md"
tags: [adyen, zip, web, drop-in, redirect, recurring-payments]
---

## Overview

This 2026-09-15 capture of Adyen's Zip Web Drop-in guide explains how to add Zip to an existing Web Drop-in integration. It requires Zip added in the test Customer Area. The guide contains endpoint examples, a Zip redirect action, recurring-token steps, and test/live setup; it does not establish current merchant eligibility, live enablement or completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The API reference labels `/sessions` as the default for Drop-in v5.0.0 or later; its parameter table lists shopper name, email, date of birth, phone, billing and delivery addresses, and line items with no required marks. It says a line-item imageURL is optional, at most 500 characters, for display on Zip's product page (pinned raw lines 28–44). The `/payments` tab is for an additional use case; its `paymentMethod.clickAndCollect=true` field indicates pickup instead of delivery (lines 681–694).
- In the `/payments` response, `resultCode=RedirectShopper` and `action.type=redirect` provide the action to redirect the shopper. The page does not itself describe final result handling; follow the main Web Drop-in flow rather than treating this redirect response as authorization (lines 1375–1389, 1636–1640). It says Zip needs no Drop-in-specific configuration steps (lines 1391–1393).
- For recurring Zip payments, the guide says to include `storePaymentMethod=true` and a unique `shopperReference` in `/payments`. After the initial payment is settled, a `recurring.token.created` webhook provides `storedPaymentMethodId`. The server must be set up to receive Recurring tokens life cycle events webhooks to obtain the token. A later `/payments` request uses `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`; the page also names `/listRecurringDetails` as a token lookup route (lines 1395–1428).
- Zip test accounts use Zip's test credentials and Adyen's test environment. The page instructs merchants to submit a Zip request in the live Customer Area before accepting live Zip payments (lines 1628–1634).

> [!warning] Example syntax
> The `/payments` curl example includes literal `{hint:...}` markup around `clickAndCollect` inside its JSON object (raw lines 697–718). It illustrates the pickup option but is not ready-to-run JSON. The endpoint and SDK samples are historical examples; select the active Drop-in flow and validate its request separately.

## Detail locators

- Scope, test setup and Sessions parameters/examples: pinned raw lines 15–680.
- Additional-use-case `/payments` table and examples: lines 681–1373.
- Redirect action and Drop-in configuration: lines 1375–1393.
- Recurring token creation, webhook prerequisite and reuse examples: lines 1395–1626.
- Test/live setup and main guide links: lines 1628–1640.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-zip]] — Zip method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/web-drop-in/2026-09-15|Zip Web Drop-in guide, captured 2026-09-15]]
