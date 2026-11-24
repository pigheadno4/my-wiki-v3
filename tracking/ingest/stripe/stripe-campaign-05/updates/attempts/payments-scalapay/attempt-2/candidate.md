---
title: "Stripe: Scalapay Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/scalapay"
raw_files:
  - "stripe-payments-scalapay-2026-11-07.md"
  - "stripe-scalapay-2025.md"
tags: [stripe, bnpl, scalapay, buy-now-pay-later, consumer, installments, europe, eur]
---

## Overview

The November 7, 2026 guide describes Scalapay as single-use B2C buy now, pay later in three or four installments. At checkout the customer selects Scalapay, follows the hosted redirect, chooses a plan and authorizes the payment. At the depicted payment-complete step the customer sees confirmation and returns, and Stripe immediately reports success or failure. Verify the completed payment before fulfillment. After success, expand the PaymentIntent’s `latest_charge` and read `latest_charge.payment_method_details.scalapay.transaction_id` for the customer’s Scalapay support reference. The guide separately lists the standard payout schedule. See November lines 9–14 and 240–260.

## November eligibility and limits

- **Buyers.** AT, BE, DE, ES, FI, FR, IT, NL and PT. The matrix shows EUR presentment for domestic and cross-border payments.
- **Stripe accounts.** AT, AU, BE, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK and US. Compared with May's 28-country account list, November adds CY, EE, HR, LI, LV and MT and omits HU.
- **Access and Connect.** The guide labels access “Instant provisional access” and lists merchants and Connect platforms or marketplaces. A connected account accepting Scalapay must have `scalapay_payments` enabled. The business still has to meet the category and risk requirements.
- **Amount.** The November transaction rows specify EUR 5.00–4,999.99. Country plan rows display EUR 5–5,000, while the explicit eligibility maximum is EUR 4,999.99. The method’s introductory wording refers to country currencies, and its payment support matrix specifies EUR presentment.
- **Categories.** The November method guide lists prohibited categories in addition to Stripe's restrictions. Examples include automotive dealers, financial services, telecommunications and digital goods, and gambling. An unlisted activity can still be ineligible for risk reasons.

May labeled buyer location EU and listed EUR for its 28 Stripe account locations. The separate May acceptance guide lists IT, FR, ES, DE, NL, BE, IE and FI for its Checkout compatibility. Those eight business locations belong to that integration and capture date. See November lines 18–62 and 68–127, May lines 12–18, 52–83 and 115–170, and [[source-stripe-scalapay-accept-payment]].

## Integration and capture

November recommends full-page Checkout and Checkout Sessions. It also lists Payment Links, embedded checkout, Payment Element, in-app payments, Connect and PaymentIntents. It excludes recurring, Checkout subscription and setup, Express Checkout Element, PaymentIntents with `setup_future_usage` and SetupIntents. The dedicated guide distinguishes Dashboard-managed display from manual integration. See November lines 129–143 and 206–238 and 262–266.

November lists manual and partial capture and excludes multicapture, overcapture and the extended, flexible extended, incremental, decremental and re-authorization modes shown in its table. The separate May PaymentIntents acceptance example leaves successful authorization in `requires_capture` until explicit capture and documents automatic cancellation with `payment_intent.canceled` after seven days if uncaptured. Use that dated guide for the capture window and check the payment outcome separately from browser return. See November lines 129–143 and May acceptance lines 1094–1103 and 1122–1138.

The May method overview marks Connect No, while its aggregate BNPL product matrix marks Supported. The November aggregate matrix and dedicated method both mark Connect supported, with the dedicated capability requirement above. The aggregate matrices change the Mobile Payment Element cell from May Unsupported to November Supported. The dedicated November in-app label and the versioned Android PaymentSheet 23.18.0 announcement cover separate surfaces, with SDK implementation and specific account enablement outside the scope of those labels. Scalapay has no row in either aggregate BNPL API table. See [[source-stripe-bnpl-overview]] and [[stripe-bnpl#Android SDK `23.18.0` Evidence|Android SDK evidence]].

## Refunds and disputes

Full and partial refunds can be requested through Dashboard or API within 90 days of the original payment. The guides describe asynchronous processing of about five minutes. A full refund cancels the buyer's unpaid installments and returns amounts already paid. A partial refund adjusts the installment plan for the reduced total. Check the Refund object's `succeeded` or `failed` status and final `refund.updated` or `refund.failed` event. Failure returns the amount to the Stripe balance, and the merchant must issue the refund another way. See November lines 145–167 and May lines 151–158.

The November guide allows one full dispute per payment within 210 calendar days of purchase. Stripe immediately holds the disputed amount and notifies the merchant by email, Dashboard and `charge.dispute.created` webhook. The deadline is seven calendar days from dispute creation. Submit evidence once through the Dashboard or Disputes API. Scalapay states it issues a final decision within 30 calendar days of creation. A merchant win restores the held amount to the Stripe balance. A customer win makes the balance charge permanent. The May guide gave 12 calendar days for evidence and described category approval at Scalapay's discretion. See November lines 169–204 and May lines 121–149.

## Related Pages

- [[stripe-bnpl]] — BNPL product and API matrix context
- [[source-stripe-scalapay-accept-payment]] — Dated integration variants and PaymentIntent manual capture
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-scalapay-2026-11-07|November 7, 2026 Scalapay payments]] — Full method guide
- [[raw/stripe-scalapay-2025|May 6, 2026 Scalapay payments]] — Earlier full guide, including the original video URL
