---
title: "Stripe Subscriptions — Set Up BECS Direct Debit Subscription (Australia)"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/au-becs-debit"
raw_files:
  - "stripe-billing-subscriptions-au-becs-debit-2026-11-07.md"
  - "stripe-subscriptions-becs-debit-2026.md"
tags: [stripe, billing, subscriptions, becs, australia, aud, direct-debit, setup-intents, mandate]
---

## Overview

Stripe's Australian BECS Direct Debit subscription guide uses a Dashboard Product and recurring Price, a server-created SetupIntent, client-side Australia Bank Account Element and DDR authorization, then a saved default payment method on a customer-configured Account or Customer before server-side subscription creation. It recommends the Payment Element for new users instead of the legacy Elements path described here. The 2026-11-07 capture adds explicit first-payment fulfillment and conditional retry qualifications to the 2026-05-13 guide. See [[stripe]], [[stripe-au-becs-debit]] and [[stripe-subscriptions]].

## Integration flow

1. Create the Product and recurring AUD Price in the Dashboard and retain its Price ID. The November server example enables the payment method in the Dashboard and creates a SetupIntent with `automatic_payment_methods[enabled]=true`; Stripe displays eligible methods automatically. This does not establish BECS eligibility for any particular account. The May Node.js example explicitly uses `payment_method_types: ["au_becs_debit"]`; both are dated sample variants, not evidence that explicit selection is invalid.
2. Pass only the SetupIntent `client_secret` to the client. Do not log it, put it in a URL, or expose it to anyone other than the customer. Use the HTML/JS `auBankAccount` Element or React `AuBankAccountElement` to collect BSB and account number, plus account holder name and email. The guide requires HTTPS for live checkout, while allowing tests without it.
3. Display the DDR service agreement and authorization text, obtain the customer's Direct Debit Request, and confirm setup with `stripe.confirmAuBecsDebitSetup`. A successful setup has SetupIntent status `succeeded`; it is a payment-method setup result, not proof that the first debit has cleared.
4. Make the accepted DDR and its service agreement shareable with the customer at all times. After successful setup, the guide says to share the Mandate URL. It recommends also sending an explicit confirmation, business name on the bank statement, amount and schedule if applicable, and the DDR link; those extra details are recommendations, not individually mandatory steps.
5. For recurring charges, set the stored payment method as the default for the correct customer object: `configuration.customer.billing.default_payment_method` on a customer-configured Account v2, or `payment_method` and `invoice_settings.default_payment_method` when creating a Customer v1. Then create the subscription with that Account's `customer_account` or Customer's `customer` and the Price ID. Store the customer identity for subsequent use.

## Payment state and retries

A subscription may become `active` while its first BECS payment is still processing. Before fulfilling goods or services, wait for `invoice.paid` **or** confirm that the underlying PaymentIntent is `succeeded`, and also verify the related subscription is `active`. A SetupIntent success, subscription creation, or `active` status by itself does not prove the debit succeeded.

> [!warning] Contradiction
> The 2026-05-13 capture states that BECS payments are never automatically retried, even with another-method retry schedule. The 2026-11-07 guide says Stripe **can** automatically retry AU BECS payments failed for insufficient funds **if Direct Debit retries is enabled**. Keep the older sentence as historical wording; the newer condition is bounded by enablement and failure reason. Neither capture verifies this feature is available or enabled for a given account. [[stripe-au-becs-debit]] separately records a private-preview Billing Retries qualification from its own evidence.

## Mandate and customer-model qualifications

The online DDR form collects account holder name, BSB and account number. Display Stripe's exact DDR service agreement inline or through a clearly labeled link, and display its standard authorization text with the merchant name substituted. The accepted DDR and service agreement must remain shareable as print or a non-changeable electronic copy; Stripe hosts the Mandate URL.

The November guide says Accounts v2 is generally available for Connect users and in public preview for other Stripe users. Preview participants need a preview API version; its Account curl example shows `Stripe-Version: 2026-10-28.preview` and the Dashboard path to enable “Reusable payment methods for Global Payouts.” This is documentation of a preview path, not proof of account access. Customer v1 remains an alternative.

## Optional features and tests

A manual `billing_cycle_anchor` can produce a prorated charge until the anchor; `proration_behavior=none` suppresses that charge. A `trial_end` timestamp creates a free trial and can be combined with an anchor. These are guide examples, not evidence of a tested subscription.

The guide gives test BSB `000000` and ten test accounts. The table preserves the documented PaymentIntent and mandate outcomes; it does not report an actual payment in this workspace.

| Account | Token | Documented outcome |
|---|---|---|
| `000123456` | `pm_auBecsDebit_success` | PaymentIntent `processing` → `succeeded`; mandate active |
| `900123456` | `pm_auBecsDebit_successDelayed` | Same success after a three-minute delay; mandate active |
| `111111113` | `pm_auBecsDebit_accountClosed` | `requires_payment_method`; mandate inactive |
| `111111116` | `pm_auBecsDebit_noAccount` | `requires_payment_method`; mandate inactive |
| `222222227` | `pm_auBecsDebit_referToCustomer` | `requires_payment_method`; mandate active |
| `922222227` | `pm_auBecsDebit_referToCustomerDelayed` | Same failure after three minutes; mandate active |
| `333333335` | `pm_auBecsDebit_debitNotAuthorized` | `requires_payment_method`; mandate inactive |
| `666666660` | `pm_auBecsDebit_dispute` | `succeeded`, followed immediately by dispute |
| `343434343` | `pm_auBecsDebit_exceedsWeeklyLimit` | `charge_exceeds_source_limit` error |
| `121212121` | `pm_auBecsDebit_exceedsTransactionLimit` | `charge_exceeds_transaction_limit` error |

## Detail locators

- November: Product and Price (raw lines 13–29); SetupIntent and client secret (31–45); DDR requirements (75–95 and 265–285); HTML/React Element setup (97–382); client confirmation and mandate URL (384–576); Account v2 preview and Customer v1 defaults (584–688); subscription creation, first-payment state and retries (690–720); test table, anchor and trial (722–789).
- May: explicit Node.js `payment_method_types` SetupIntent (raw lines 30–56); DDR requirements (86–106); mandate URL advice (417–424, 575–582); customer and subscription examples (594–736); former status and never-retry wording (738–742); ten test accounts and optional billing cases (744–843). Its Stripe.js example uses a `dahlia` path; November uses `endive`. The path and Node.js-to-curl rendering do not alone establish a new payment capability.

## Related

- [[stripe-au-becs-debit]] — AU BECS mandates, settlement and retries
- [[stripe-subscriptions]] — subscription lifecycle and fulfillment
- [[stripe]] — company

## Raw Sources

- [[raw/stripe-billing-subscriptions-au-becs-debit-2026-11-07|AU BECS subscription guide — captured 2026-11-07]]
- [[raw/stripe-subscriptions-becs-debit-2026|AU BECS subscription guide — captured 2026-05-13]]
