---
title: "Stripe: BLIK Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/blik"
raw_files:
  - "stripe-payments-blik-2026-11-07.md"
  - "stripe-blik-2025.md"
tags: [stripe, blik, poland, pln, bank-debit, recurring, disputes, connect]
---

## Summary

The November 7, 2026 BLIK overview describes a Polish-customer, PLN bank-debit method in which a customer enters a six-digit bank-app code and approves a bank push notification. It newly describes reusable BLIK PaymentMethods for off-session recurring payments, with a bank-app-authorized mandate. The May 3, 2026 capture instead called BLIK single use and recurring private preview. These are dated page descriptions, not evidence that a particular account, bank, or charge is enabled or successful. See [[stripe]], [[stripe-blik]], and [[stripe-bank-redirects]].

## Customer payment and eligibility

The code is valid for **2 minutes**; the customer must approve within **60 seconds** after the payment starts, typically in under 10 seconds. The merchant page remains open without a browser redirect. Stripe says it normally receives BLIK's asynchronous result within 60 seconds; on mobile the customer manually returns to the merchant page. The overview table labels confirmation timing immediate and access instant provisional, while settlement follows the standard payout schedule. The table and flow are not proof of an individual successful payment or settlement.

The November capture lists Polish customers, PLN presentment, a **2.00 PLN** minimum, a **999,999.99 PLN** one-time maximum, and a **2,000 PLN per-charge** maximum for off-session recurring payments. Its business-location list has **35** entries; the May 3 list has **36**, including IS, which is absent from the November list. The previous wiki source's **37** count was not supported by its old raw list. A list change does not prove any individual merchant lost eligibility. Merchants and Connect platforms appear in the account table, but Stripe may review an account after activation and restrict the BLIK capability. The page says BLIK has no additional website requirement beyond Stripe account activation requirements.

## Reuse, setup and Connect

The November overview marks BLIK **reusable** and recurring payments supported. A customer authorizes future off-session charges during initial recurring setup in their bank app; Stripe associates the mandate with the reusable PaymentMethod. To save during an initial payment, use a PaymentIntent with `setup_future_usage=off_session`; to set up without an initial payment, use a SetupIntent with `usage=off_session`. Future charges can use the reusable PaymentMethod without a new BLIK code while the mandate remains valid. Detaching the PaymentMethod unregisters the alias; the customer may revoke authorization in the bank app, and a new mandate is needed after revocation or expiry. Setup and mandate authorization are distinct from a future charge and its outcome.

Connect acceptance requires `blik_payments` active on the platform and each accepting connected account. For recurring BLIK, request `blik_payments` before `blik_recurring_payments`, and have **both active** on the platform and each relevant connected account before using `setup_future_usage=off_session` or a SetupIntent with `usage=off_session`. The captured broad support table does not prove account or bank enablement.

The overview supports Checkout Sessions, PaymentIntents, PaymentIntents with setup_future_usage, SetupIntents, off-session payments, Billing, Invoicing, Customer Portal, Connect, Payment Links, full-page and embedded Checkout, and Payment Element. It excludes Express Checkout Element, Payment Method Messaging Element, Terminal, Managed Payments and an "in-app payments" category. BLIK's same-day bank-redirects matrix also marks BLIK SetupIntents, setup future usage, Subscriptions and Invoicing supported; it separately marks Mobile Payment Element supported. The two tables use different "in-app payments" and "Mobile Payment Element" labels, so neither label alone resolves a specific mobile integration. The November bank-redirects matrix also marks BLIK Payment Element unsupported **when using Elements with the Checkout Sessions API** (its BLIK footnote 4); separately listed Checkout Sessions and Payment Element support does not establish that combined path. The May 3 bank-redirects matrix marked BLIK SetupIntents, setup future usage, Subscriptions and Invoicing unsupported. Neither overview table establishes a particular Checkout setup/subscription mode or invoice collection method. See [[raw/stripe-payments-bank-redirects-2026-11-07|November 7 bank-redirects matrix]] and [[raw/stripe-bank-redirects-2025|May 3 bank-redirects matrix]].

**Deferred intent scope:** the old BLIK page described client-side confirmation only in private preview, while the existing wiki source also stated deferred intent unsupported. The November BLIK overview says Payment Element does not support collecting payment details before PaymentIntent creation. The November bank-redirects guide says BLIK does not support the deferred-intent creation integration path. Preserve these as path- and date-specific restrictions; do not turn the old preview wording into a blanket November support claim.

## Refunds and disputes

Full and partial refunds are supported, but a BLIK refund must be submitted within **730 days** of payment. Refunds are asynchronous, cannot be canceled, and can take up to **120 minutes** depending on the bank. Check the Refund `status` or verified `refund.updated`/`refund.failed` event for final state. On failure, the amount returns to the merchant's Stripe balance, and the page says to refund the customer another way. Submission is not proof of refund completion. The May 3 capture stated only that refunds could be immediate or take hours; retain that as dated wording. Manual, partial, multi-, and over-capture are unsupported in the November capabilities table.

BLIK supports full disputes, not partial disputes. Stripe withholds a disputed amount and notifies the merchant by Dashboard, email, and `charge.dispute.created`. Submit evidence within **12 calendar days** of dispute creation; the Dispute object's `evidence_details.due_by` gives its deadline. BLIK decides without a guaranteed timeframe. If the merchant wins, Stripe returns the disputed amount to its balance; if the customer wins, the charge remains. The November page says there is no dispute fee or appeal. Its generally **13-month** customer notification maximum for unauthorized transactions, subject to statutory exceptions, is a different clock from the merchant's 12-day evidence window.

## Statement descriptors and enablement

Use the full `statement_descriptor` for non-card BLIK; `statement_descriptor_suffix` is for cards. Direct charges use the connected account descriptor. Destination charges and separate charges and transfers use the platform descriptor by default; `on_behalf_of` selects the connected account descriptor. The bank may render the descriptor differently. For Stripe front-end products, enable BLIK in Dashboard payment-method settings; manual method lists follow the accept-payment guide.

## Raw Sources

- [[raw/stripe-payments-blik-2026-11-07|BLIK overview — November 7, 2026 full capture]]
- [[raw/stripe-blik-2025|BLIK overview — May 3, 2026 capture; filename retains 2025 suffix]]
