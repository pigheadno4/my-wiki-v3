---
title: "Braintree GrabPay Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/grabpay"
raw_files:
  - "braintree/docs/guides/local-payment-methods/grabpay-2026-09-16.md"
tags: [braintree, local-payment-methods, grabpay, singapore, sgd]
---

## Overview

This collected Braintree GrabPay page is a short method-specific availability and applicability notice. It identifies the payment type as `grabpay` and provides captured buyer-country, seller-country, currency and transaction-limit fields. The 2026-09-16 snapshot does not establish current availability, merchant enablement, buyer eligibility, a supported SDK or platform, an execution environment, or a completed payment.

## Key takeaways

- The notice says GrabPay is in limited release, says it is available only to buyers and sellers in Singapore, and directs merchants interested in integrating it as a Local Payment Method to contact their Customer Success Manager.
- The applicability table identifies `grabpay`, buyers in Singapore, sellers `Global`, `SGD`, and customer transaction limits from `0.01 SGD` through `5,000 SGD`. The table's global-seller value conflicts with the notice's Singapore-only seller wording; the snapshot does not resolve which seller scope controls.
- The page does not document a client or server SDK, a platform, an environment, or an initiation-to-notification flow. Do not import procedures from other Local Payment Method pages or treat availability metadata as evidence of authorization, settlement or funding.

## Evidence boundaries

> [!warning] Internal seller-country conflict
> The prose says GrabPay is only available to buyers and sellers in Singapore, while the table says buyer country `Singapore` and seller country `Global`. Preserve both captured statements and do not infer an eligible seller region from this snapshot alone.

> [!warning] Snapshot, platform and lifecycle scope
> This fully read page is a dated documentation snapshot, not proof of current release status, account enablement, buyer eligibility or live execution. It provides no SDK, platform, Sandbox or Production, initiation, notification, settlement or funding evidence.

## Detail locators

- Page identity: `# GrabPay`, line 14.
- Limited-release notice, Singapore buyer-and-seller wording and Customer Success Manager route: `### Overview > **AVAILABILITY**`, lines 20-21.
- Payment type, buyer country, conflicting seller country, currency and customer transaction limits: applicability table under `### Overview`, lines 23-25.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Local-method family guide: [[source-braintree-payment-methods-local-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/grabpay-2026-09-16|Braintree GrabPay guide]] - complete collected page containing the GrabPay heading, limited-release notice and applicability table
