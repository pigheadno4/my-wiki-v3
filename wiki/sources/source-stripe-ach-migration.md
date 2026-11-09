---
title: "Stripe: Migrating to New ACH Direct Debit APIs"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ach-direct-debit/migrating-to-new-apis"
raw_files:
  - "stripe-payments-ach-direct-debit-migrating-to-new-apis-2026-11-07.md"
  - "stripe-ach-migration-2025.md"
tags: [stripe, ach, us-bank-account, migration, legacy, payment-intents, checkout-sessions, mandates, webhooks]
---

## Summary

Stripe's 2026-05-02 and 2026-11-07 captures say merchants creating legacy ACH Direct Debit payments must migrate to the Payment Intents API or Checkout Sessions API. The guide compares the legacy and newer paths, with a staged migration: enable ACH Direct Debit, integrate the newer path, reuse eligible saved BankAccount objects, test, gradually move payments, then remove the legacy integration (new raw lines 9–11, 39–53). The snapshots are migration guidance, not proof of a particular account's faster-settlement eligibility or live payment outcome.

## Capability and timing comparison

The guide's table lists Checkout, Payment Element, and dynamic payment methods in the newer API path, along with Financial Connections instant bank-account verification and fraud tools. It compares legacy T+6 settlement with newer T+4, or T+2 **when faster settlement applies**; it lists legacy US versus newer US, EU, and UK support (new raw lines 13–27). These are captured product-scope statements, not account-specific entitlements. Checkout Sessions is recommended for common checkout workflows; Payment Intents is the lower-level custom-flow path (new raw lines 29–37).

The newer APIs enforce an **active mandate** before ACH initiation; a mandate can become inactive after disputes, failures, or invalid account status. The guide says a Tokens API BankAccount reused in the newer path needs a mandate first (new raw lines 59–63). [[source-stripe-ach-migrate-bank-accounts]] has the saved-bank-account prerequisites and dated acknowledgment options.

## Balance transactions, payouts, and Connect transfers

Legacy integrations create the Balance Transaction with the charge; the guide says it appears in the legacy `charge.pending` event and API response. In the newer path, the Balance Transaction is created **when the payment is submitted to the banking partner**, and appears in `charge.updated`, not the initial API response (new raw lines 64–66, 84–87). That milestone does not establish customer-bank receipt, final settlement, or payment success.

Legacy funds settle in `source_type=bank_account`; newer API funds settle in `source_type=card`. **If** payout or Connect-transfer logic manually specifies a balance type, update it for the new source type. During migration, the guide says there can be a payout for each type. For separate charges and transfers using `source_transaction`, wait for `charge.updated` before creating the transfer (new raw lines 67–70). The November guide adds that payout statement descriptors **might** differ between bank-account and card source-type payouts; it does not say they differ for every account or payout (new raw line 71).

## Verification and email changes

Legacy verification used two small random microdeposits and no hosted verification UI. The newer flow usually uses one 1-cent microdeposit with a descriptor code and a hosted verification page, but **rarely uses two small random deposits instead**. Customers have 10 days to verify; after that, the PaymentIntent or SetupIntent returns to requiring new payment-method details (new raw lines 72–75). This verification step is separate from payment finality.

The guide contrasts no automatic emails in the legacy path with mandate-confirmation and microdeposit-verification emails in the newer path. The verification email applies when a customer attempts microdeposit verification. Stripe emails can be disabled in Dashboard if custom notices are sent instead (new raw lines 76–78). See [[source-stripe-ach-direct-debit]] for the billing-email condition and mandate-copy details; this migration table does not establish that every customer receives each email.

## Webhook migration matrix

This table preserves the guide's **Checkout versus Payment Intents branch labels**; it is a migration event comparison, not a substitute for paid-status checks before fulfillment (new raw lines 80–91).

| Legacy event | Checkout column | Payment Intents column | Guide qualification |
| --- | --- | --- | --- |
| `charge.pending` | `payment_intent.processing` | `payment_intent.processing` | New Balance Transaction is unavailable until `charge.updated`. |
| `charge.updated` | `charge.updated` | `charge.updated` | Banking-partner submission; includes Balance Transaction. |
| `charge.succeeded` | `checkout.session.completed` | `payment_intent.succeeded` | `charge.succeeded` is also sent. Checkout completion alone can be unpaid for delayed methods; inspect payment status before fulfillment. |
| `charge.failed` | No direct row equivalent; customer can retry on the same Session until expiry, then `checkout.session.expired` | `payment_intent.payment_failed` | `charge.failed` is also sent. |
| `charge.dispute.created` | `charge.dispute.created` | `charge.dispute.created` | Dispute event persists. |
| No legacy equivalent | `mandate.updated` | `mandate.updated` | Sent when a mandate becomes inactive. |

The Checkout paid-status qualification follows [[source-stripe-checkout-dashboard-payment-methods]] and [[stripe-checkout]]; the migration table itself does not prove funds are paid on every completed Session.

## Identify legacy ACH payments

The guide identifies legacy ACH on a Charge by `payment_method_details.type: ach_debit` versus `us_bank_account` for the newer integration. Its examples are direct Create Charge calls; an Invoice or Subscription charging a Customer's legacy BankAccount `default_source` **when no `default_payment_method` is set** on the Customer, invoice, or subscription; and a PaymentIntent using `payment_method_type: ach_debit` (new raw lines 93–101). These are guide criteria, not evidence that a specific merchant's Charges were migrated.

## Related pages

- [[stripe-ach-direct-debit]] — ACH Direct Debit concept and migration route
- [[stripe-payment-intents]] — PaymentIntent event lifecycle
- [[stripe-checkout]] — Checkout Session and delayed-method fulfillment
- [[source-stripe-ach-migrate-bank-accounts]] — saved BankAccount reuse and mandate acknowledgment

## Raw Sources

- [[raw/stripe-payments-ach-direct-debit-migrating-to-new-apis-2026-11-07|2026-11-07 migration guide]]
- [[raw/stripe-ach-migration-2025|2026-05-02 earlier migration guide]]
