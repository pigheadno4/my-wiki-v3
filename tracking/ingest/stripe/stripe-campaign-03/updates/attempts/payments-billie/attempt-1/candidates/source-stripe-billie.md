---
title: "Stripe: Billie Payments"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/billie"
raw_files:
  - "stripe-payments-billie-2026-11-07.md"
  - "stripe-billie-2025.md"
tags: [stripe, bnpl, billie, buy-now-pay-later, b2b, europe, connect, disputes]
---

## Overview

Billie is a **B2B, single-use, Pay in 30** buy now, pay later method. A business customer selects it at checkout, is redirected to Billie to authorize, and returns to the merchant site or app. The 2026-11-07 page describes immediate payment confirmation and immediate merchant payment, but labels access **instant provisional** and settlement **standard payout schedule**. Stripe separately notifies success or failure after the return; the redirect or authorization alone does not prove payment success or an instant external payout. See [[stripe]], [[stripe-bnpl]] and [[source-stripe-billie-accept-payment]] for the separate integration guide (new raw lines 5-16, 200-220; old raw lines 4-40).

## Eligibility and payment scope

- The November capture lists Billie for merchant and business-customer locations AT, CH, DE, DK, ES, FI, FR, GB, NL, NO and SE, marks B2B supported and B2C unsupported, and marks domestic but not cross-border coverage. Presentment currencies are CHF, DKK, EUR, GBP, NOK and SEK. Its account-country settlement table maps EUR/SEK/NOK/DKK to DE/FR/NL/SE/NO/FI/AT/ES/DK, GBP to GB, and CHF to CH (new raw lines 18-67). The May capture also lists the eleven account countries and six currencies (old raw lines 8-20, 54-68, 178-187). A listed country/currency is not proof of a particular account's enabled capability.
- The November minimum is **0.01 EUR** and it says maximum amounts **vary by country and currency** (new raw lines 54-67). The May page stated a 0.01 EUR or equivalent minimum without giving a maximum (old raw lines 105-107); that omission did not establish an unlimited maximum.
- November has a 13-row prohibited MCC table, including construction, car rental, real-estate rental and tax-payment entries, alongside previously named gambling, adult content, financial institutions and crypto categories. It distinguishes prohibited MCCs from restricted categories that may require more account information (new raw lines 24-44). Consult the full table for a category decision; the capture does not prove merchant approval.
- November marks manual and partial capture supported, but multicapture, overcapture, extended/incremental/decremental/re-authorization, and recurring payments unsupported (new raw lines 69-83). The May Billie page also said recurring payments were not supported and manual capture was supported (old raw lines 30-48).

## Refunds and disputes: dated change

- **Refunds:** November requires refund submission within **365 days of the original payment**, replacing the May guide's **up-to-180-day** statement (new raw lines 85-109; old raw lines 147-154). Full and partial refunds are supported and processed asynchronously, up to five minutes. The November guide says Billie refunds **cannot be canceled**. A full refund cancels the remaining Billie obligation; a partial one lowers it. Retrieve the Refund `status` or use `refund.updated`/`refund.failed` and verify webhook signatures. On failure the Refund status becomes `failed`, Stripe returns the amount to the merchant Stripe balance, and the merchant must refund the customer another way. Submission and an initial refund response are not completion.
- **Disputes:** November gives customers up to **365 calendar days from purchase** to file, merchants **35 calendar days from dispute creation** to submit evidence, and Billie seven calendar days after evidence submission to issue a decision (new raw lines 91-94, 111-142). May required merchant evidence within **12 calendar days** and named suspected fraud, double payment and order/amount discrepancy as examples (old raw lines 123-145). Stripe withholds the disputed amount while the case is open; a merchant win returns it to the Stripe balance, while a customer win makes the balance charge permanent. The Dashboard and Disputes API support responses; `evidence_details.due_by` is the dispute object's deadline locator (new raw lines 115-142).

## Product/API and cross-source conflicts

The November Billie-specific matrix marks Checkout full page and embedded form, Payment Links, Payment Element, in-app payments, Billing, Invoicing and Connect supported. It marks Express Checkout Element, Payment Method Messaging Element, Managed Payments, Customer Portal, Radar and Terminal unsupported; Checkout Sessions and PaymentIntents are listed APIs, while SetupIntents, off-session payments, and PaymentIntents with `setup_future_usage` are unsupported. Checkout subscription and setup modes are also excluded (new raw lines 144-176). A footnote says **only `send_invoice` collection method**, but its exact attachment within the text-captured matrix is unclear; verify the route-specific Billing/Invoicing integration. Product support does not imply automatic recurring charges or Checkout subscription-mode support.

> [!warning] Dated documentation conflicts
> The 2026-05-06 cross-BNPL overview marks Billie `setup_future_usage` **supported** (that raw's API table, line 63), whereas the November Billie-specific matrix marks PaymentIntents with it **unsupported** (new raw lines 163-168); both Billie overview captures say recurring payments are unsupported (old raw lines 30-32; new raw lines 69-70). The older cross-BNPL product table also marks Billie **Invoicing unsupported** (cross-BNPL raw lines 40-45), whereas the November Billie-specific table marks **Invoicing supported** with the `send_invoice` footnote below (new raw lines 154-170). The May Billie-specific product list merely omitted Invoicing (old raw lines 70-79). Keep the old matrix dated and verify the exact integration route; neither capture resolves account eligibility or turns invoice collection into off-session recurring Billie.

The May get-started section recommended `line_items` data for approval rates through early Payments line items access (old raw lines 86-103). Its absence from this November overview does not show that advice or the integration feature was removed.

## Connect and identifier

Both captures require `billie_payments` capability `active` on the platform and on connected accounts enabled for Billie. Direct charges derive the descriptor from the connected account; destination and separate-charge-and-transfer payments use the platform unless `on_behalf_of` selects the connected account (new raw lines 178-198; old raw lines 156-176). After a Billie **payment succeeds**, expanding `latest_charge` on the PaymentIntent yields `latest_charge.payment_method_details.billie.transaction_id` for Billie support (new raw lines 218-220); it is not a request-time or authorization-return identifier.

## Detail locators

- November eligibility, MCCs, country/currency, amount and capture: new raw lines 18-83; May comparison: old raw lines 12-79, 105-121, 178-187.
- November refund and dispute lifecycle: new raw lines 85-142; May prior windows: old raw lines 123-154.
- November product/API matrix and Connect: new raw lines 144-198; May product and Connect: old raw lines 70-79, 156-176.

## Raw Sources

- [[raw/stripe-payments-billie-2026-11-07|Billie overview — 2026-11-07 full capture]]
- [[raw/stripe-billie-2025|Billie overview — 2026-05-06 full capture (historical filename)]]
