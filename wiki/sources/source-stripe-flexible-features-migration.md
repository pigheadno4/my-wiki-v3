---
title: "Stripe — Flexible Payment Features Beta-to-GA Migration"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/flexible-features-migration"
raw_files:
  - "stripe-flexible-features-migration-2026.md"
tags: [stripe, incremental-authorization, overcapture, extended-authorization, multicapture, migration, ic-plus]
---

## Overview

The **2026-05-11 full guide** describes migration of four non-card-present flexible payment scenarios from private beta to general release: incremental authorization, overcapture, extended authorization and multicapture. It documents PaymentIntent card request changes, post-confirmation `latest_charge` status checks and capture behavior. The **2026-11-07 capture is only a variant index** for the four scenarios; it does not contain the variant bodies or verify their current API behavior. For feature-specific current rules, follow the linked variant and dedicated guide. See [[stripe]], [[stripe-incremental-authorization]], [[stripe-overcapture]], [[stripe-extended-authorization]] and [[stripe-multicapture]].

## May 2026 migration details

### Incremental authorization

The formerly optional `request_incremental_authorization_support: true` becomes a required pre-confirmation request, `payment_method_options.card.request_incremental_authorization: "if_available"`, in this dated beta-to-GA migration. After confirmation, the expanded `latest_charge.payment_method_details.card.incremental_authorization.status` reports `available` or `unavailable`; requesting is not proof of availability. The `increment_authorization` endpoint step is unchanged (May raw lines 22-150).

### Overcapture

The beta had no request parameter; the May GA migration requires `payment_method_options.card.request_overcapture: "if_available"` before PaymentIntent confirmation. The expanded `latest_charge.payment_method_details.card.overcapture` provides `status` (`available` or `unavailable`) and, in the example, `maximum_amount_capturable`. Where available, the guide uses the capture endpoint with `amount_to_capture` up to that maximum; the capture endpoint step itself is unchanged (May raw lines 153-229). The example amount and maximum are illustrative, not account-level availability.

### Extended authorization

The May migration adds a mandatory pre-confirmation `payment_method_options.card.request_extended_authorization: "if_available"` where beta had no such step. The guide says `capture_before` is now present even without using extended authorization, and capture must occur before that field's date; the capture endpoint step is unchanged (May raw lines 231-310).

> [!warning] Contradiction in the 2026-05-11 full guide
> Its prose says `latest_charge.payment_method_details.card.extended_authorization.status` has `available`/`unavailable` values (May raw line 264), while the adjacent response example uses `enabled`/`disabled` (May raw lines 280-284). The November variant index has no response schema, so it does not resolve the discrepancy. Do not treat either value set as verified by that index.

### Multicapture

The May beta-to-GA guide adds a mandatory pre-confirmation `payment_method_options.card.request_multicapture: "if_available"`. For its beta migration, it instructs passing `multicapture_migrate_to_ga_from_beta` in the `Stripe-Version` header before confirmation; the Node example pins `2026-04-22.preview; multicapture_migrate_to_ga_from_beta`. This is a **dated migration example**, not a current API-version prescription. Check `latest_charge.payment_method_details.card.multicapture.status` for `available`/`unavailable` after confirmation (May raw lines 312-374).

Multiple partial captures require the PaymentIntent to remain `requires_capture`. A non-final capture with `final_capture: false` can leave a capturable remainder, as the 700-of-1000 example shows. In the GA behavior described by this guide, trying to capture the **full remaining capturable amount** with `final_capture: false` returns HTTP 400; the beta example had captured the remaining 300 and reached `succeeded` (May raw lines 376-476). This boundary concerns the remaining amount, not any capture equal to the original authorized amount.

The May table changes a **non-final** capture event from `charge.captured` to `charge.updated`; final capture remains `charge.captured`. For `final_capture=true`, GA does not create a refund *to represent uncaptured funds*; this does not mean refunds generally cease (May raw lines 478-489).

### Combining overcapture and incremental authorization

The May example requests both features on one manually captured card PaymentIntent, then inspects each status on the expanded `latest_charge`. **Only if both are available after confirmation** does its strategy offer overcapture when desired capture is at or below `maximum_amount_capturable`, or incremental authorization before capture for a higher desired amount (May raw lines 491-549). A request or example response does not prove live feature access, successful incremental authorization or capture.

## Detail locators

- May full guide: incremental authorization lines 22-150; overcapture 153-229; extended authorization 231-310; multicapture 312-489; combined strategy 491-549.
- November variant index: new raw lines 5-16. The four URLs are navigation to unpinned variant bodies in this update.

## Related raw API references

- [[raw/stripe-payments-flexible-features-migration-2026-11-07|2026-11-07 variant index]] — navigation only: incremental authorization, overcapture, extended authorization and multicapture variant URLs; no behavioral body captured.

## Raw Sources

- [[raw/stripe-flexible-features-migration-2026|2026-05-11 full migration guide]]
