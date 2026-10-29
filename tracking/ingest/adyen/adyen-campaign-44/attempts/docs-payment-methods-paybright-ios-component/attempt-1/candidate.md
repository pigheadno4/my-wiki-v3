---
title: "PayBright iOS Redirect Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paybright/ios-component/2026-09-15.md"
tags: [adyen, paybright, ios, components, redirect, capture, refund]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, adds the PayBright Redirect Component to an existing iOS Components integration with Sessions or Advanced server flow. It explicitly says PayBright was acquired by Affirm and Adyen will not accept new PayBright integrations. See [[source-adyen-docs-payment-methods-paybright|PayBright overview]], [[source-adyen-docs-payment-methods-affirm|Affirm]] and [[adyen-online-payments]]. The snapshot does not establish current merchant eligibility, operational payment success or settlement.

## Key takeaways

- The guide assumes an existing iOS Components integration for the chosen server flow and PayBright added in Customer Area. It calls `/sessions` the default with Components v5.0.0 or later and shows `/payments` for an additional use case. Both request tables mark shopper first/last name, date of birth, email, phone, country, billing address and a unique shopper reference of at least three characters as required. Delivery address defaults to billing when blank or missing; `shopperLocale` and `lineItems` are optional, with line items recommended for approval rates. These are method-specific table markings, separate from the general Checkout schema.
- For iOS Components v5.0.0+, the page checks for `paybright` as an `other` payment method, creates `InstantPaymentComponent`, assigns the Session or merchant delegate according to flow and initiates payment. The v4.x.x example instead uses `PayBrightPaymentMethod` and `PayBrightComponent`. The page says no additional PayBright-specific component configuration is required.
- The capture section says PayBright payments are automatically captured after authorization by default; capture delay or manual capture is needed to capture after shipment or partially. Capturing charges the shopper's first installment. Partial capture is unavailable while automatic capture is enabled in Customer Area. Its `/capture` example uses `modificationAmount` and optional `additionalData.openinvoicedata`; after a partial capture, the unclaimed amount is automatically cancelled unless the account is enabled for multiple partial captures. That option requires Support and creates a new invoice per capture.
- Before capture, cancel a payment; after capture, refund it. The partial-refund prose names `/payments/{paymentPspReference}/refunds` with `modificationAmount` and optional `additionalData.openinvoicedata`, while the example is labeled `/refund request` and uses an `originalReference` legacy-looking shape. The page does not reconcile those endpoint/payload forms; follow the applicable API reference before reuse.
- The page calls for test details and a live Customer Area request. Its own opening warning says Adyen accepts no new PayBright integrations, so that older live-request instruction must not be read as current onboarding availability.

> [!warning] Incomplete and inconsistent request examples
> The Sessions and Advanced examples contain empty strings for required shopper values and `amount.currency`. The Advanced Java/PHP snippets use USD for CA, while the [[source-adyen-docs-payment-methods-paybright|PayBright overview]] lists CA/CAD. The examples also include render hints as JSON keys and some Web-channel snippets on this iOS page. They are illustrative, not ready-to-send requests; verify currency, values and channel against the applicable method/API documentation. The partial-capture example's amount is 4500 while its listed shoes plus one pair of socks total 5500 before any discount, and no discount line appears in that invoice example.

## Detail locators

- Acquisition/new-integration warning and Sessions/Advanced prerequisites: pinned raw lines 15–39. Request tables: lines 45–60 and 789–804.
- Test `/v69/sessions` samples: lines 62–787; `/v72/payments` samples: lines 806–1310. Blank currency/required values are present in both; Advanced Java/PHP USD appears at lines 887 and 975.
- Versioned iOS component creation: lines 1312–1367. Capture default, first-installment timing, partial-capture gate and unclaimed-balance effects: lines 1369–1428.
- Cancel/refund boundary and endpoint/example mismatch: lines 1430–1474. Test and live instructions: lines 1476–1482.

## Related

- [[adyen-online-payments]] — provider online integration concept
- [[source-adyen-docs-payment-methods-paybright]] — CA/CAD overview and no-new-integration warning
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm method

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/ios-component/2026-09-15|PayBright iOS Redirect Component guide, fetched 2026-09-15]]
