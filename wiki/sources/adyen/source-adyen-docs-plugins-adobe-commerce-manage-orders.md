---
title: "Adyen Adobe Commerce order management"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/manage-orders"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/manage-orders/2026-09-15.md"
tags: [adyen, adobe-commerce, orders, capture, refund, webhooks]
---

## Overview

This 2023-last-modified, 2026-09-15-captured guide explains how Adobe Commerce and Adyen Customer Area expose **order capture, cancellation and refund** actions, and how plugin webhooks affect Commerce order, invoice and credit-memo statuses. An Adobe Commerce order, invoice or credit memo is a distinct object from its Adyen payment and from a bank settlement. This is procedural documentation without an exact plugin package version; the versioned implementation route is [[adyen-magento2]] and [[source-github-adyen-magento2]]. See [[adyen]].

## Key takeaways

- **Two admin surfaces and webhook dependency:** The guide permits order management through Commerce admin or Adyen Customer Area and describes webhooks keeping the platforms in sync. Commerce status names can be customized. A configured action or displayed status alone is not proof that a payment modification succeeded, funds returned, or settlement arrived.
- **Manual capture and invoicing:** With manual capture configured, each order needs an explicit capture request. In Commerce the described action is **Invoice**, optionally reduce product quantity for a partial capture, then **Submit Invoice**. The guide says a `CAPTURE` webhook follows capture and the Commerce invoice moves to **Paid** after successful capture. The invoice status is not bank-payment evidence, and this page does not define a general multiple-capture entitlement or amount limit.
- **Multiple-method order grain:** Where one order uses payment methods with differing capture modes, the plugin generates an invoice only after the **full order amount** has been authorized or captured, regardless of the order in which individual `AUTHORISATION` and `CAPTURE` webhooks arrive. That is an order/invoice creation rule; it does not mean every underlying payment has the same financial state or that all funds were settled.
- **Cancel versus refund:** The page allows cancellation only for an authorized, **not yet captured** order with manual capture delay; after capture it directs the merchant to refund. Commerce cancellation changes the order to **Closed** or a configured status following the described webhook. For refund, the Commerce path selects an invoice, creates a **Credit Memo**, chooses item quantities and selects **Refund**. It says a `REFUND` notification and credit memo follow; partial refund leaves order **Processing**, full refund moves it to **Closed**, and a successful refund changes credit memo to **Refunded**. These are Commerce/plugin lifecycle observations, not independent proof of shopper bank receipt. This page calls the cancellation webhook `CANCELLATION`; the separate [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce]] order-status table calls it `CANCEL_OR_REFUND`. Verify the actual installed plugin and webhook event before relying on either label.
- **Expiry and risk-review conditions:** The snapshot gives default expiration of 12 hours for card payments and up to 28 days for other methods, with Support contact for merchant/scheme/timeframe changes. For expired **SVS gift-card payments**, Adyen does not send `OFFER_CLOSED`. The guide says an offer closes automatically only if the shopper leaves the SVS page using **Previous**; other abandonment (such as closing the browser) requires manual closure in Adobe Commerce admin, or the alternative configured pending-payment order lifetime and scheduled cron route. Case management is optional and requires RevenueProtect premium plus role, trigger, action and webhook setup. Recommended accept/reject behavior requests Capture/Cancel and notification; optional Commerce manual-review statuses do not themselves establish a fraud or payment outcome.

## Detail locators

- Lines 15–23: scope, Commerce versus Customer Area and webhook/status route.
- `## Capture an order`, lines 25–41: manual capture, Commerce Invoice action, quantity-based partial capture, `CAPTURE` webhook and mixed-method full-order invoice condition.
- `## Cancel an order`, lines 43–55: authorized-uncaptured manual-only cancellation and `CANCELLATION` label; compare separate setup guide's `CANCEL_OR_REFUND` label.
- `## Refund an order`, lines 57–72: invoice/Credit Memo path, partial/full order statuses and `REFUND` notification.
- `## Expired payments`, lines 74–91: dated expiry defaults, `OFFER_CLOSED` and SVS exception.
- `## Case management`, lines 93–124: premium, roles/triggers/actions/webhooks and optional review-status settings.

## Related

- [[adyen-magento2]] — reciprocal plugin and exact-version implementation route.
- [[source-github-adyen-magento2]] — exact `adyen/module-payment@11.0.0` lifecycle evidence.
- [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce]] — configuration and conflicting cancellation-event label.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/manage-orders/2026-09-15|Adobe Commerce Manage orders, captured 2026-09-15]]
