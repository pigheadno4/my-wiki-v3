---
title: "PayPal Checkout: Customize the Checkout Experience"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-customize-overview.md"
tags: [paypal, checkout, customization, reference, app-switch, authorize-capture, shipping, recurring-payments, spa, pay-now]
---

## PayPal Checkout: Customize the Checkout Experience

Official PayPal index of all checkout customization features — a reference catalog of 20 extension points for the standard PayPal Checkout integration.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/>

Last updated: 2025-05-08

## Feature Catalog

PayPal recommends starting with **Show cancellation page** and **Validate user input** as the first two customizations to add after a basic integration.

| Feature | What it does |
| ------- | ------------ |
| App Switch | Redirect mobile buyers to the PayPal app for faster auth and checkout |
| Authorize and capture | Two-step flow: authorize now, capture later (e.g. after verifying inventory) |
| Contact module | Let buyers view/edit email and phone during checkout |
| Display funding source | Show buyer the payment method used after purchase |
| Display PayPal buttons with other payment methods | Clean UI when presenting PayPal alongside other options |
| Handle errors | Surface errors in the buyer experience |
| Handle funding failures | Restart payment flow when buyer's funding source fails (`INSTRUMENT_DECLINED`) |
| Messaging with buttons | Render Pay Later / promotional messaging alongside buttons |
| Overcharge handling | Re-authorize when final amount exceeds original agreement |
| Pass buyer identifier | Pre-fill PayPal login with buyer's email |
| Pass line-item details | Send SKU/item details for transparency during checkout |
| Pay another account | Route payment to a different receiver at order creation |
| Pay now or continue | Control whether checkout completes in PayPal or returns to merchant site |
| PayPal Checkout with SPAs | React, Vue, Angular integration guidance |
| Recurring payments module | Display billing plan to buyer before committing to recurring charge |
| Shipping module | Offer shipping options during checkout |
| Show cancellation page | Confirm cancellation to buyer (**recommended starting point**) |
| Standalone payment buttons | Render individual buttons per payment method |
| Update order details | Modify order/transaction details mid-checkout |
| Validate user input | Validate forms before buyer submits (**recommended starting point**) |

## Grouping by theme

**Buyer UX / trust:**
Show cancellation page, Display funding source, Pass line-item details, Contact module, Messaging with buttons

**Payment flow control:**
Authorize and capture, Pay now or continue, Overcharge handling, Handle funding failures, Handle errors

**Checkout optimisation:**
App Switch, Pass buyer identifier, Standalone payment buttons, Display PayPal buttons with other payment methods

**Order / shipping:**
Shipping module, Update order details, Pass line-item details, Pay another account

**Recurring / vault:**
Recurring payments module

**Technical / integration:**
PayPal Checkout with SPAs, Validate user input

## Raw Sources

- [[paypal-checkout-customize-overview]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration (customizations extend this)
