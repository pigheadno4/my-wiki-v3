---
title: "Braintree NAB Chargebacks, Retrievals, and Pre-Arbs"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/chargebacks-retrievals-prearbs"
raw_files:
  - "braintree/articles/nab/chargebacks-retrievals-prearbs-2026-09-16.md"
tags: [braintree, disputes, chargebacks, retrievals, pre-arbitration, nab]
---

## Overview

This captured Braintree-hosted NAB account/processor article describes credit-card transaction disputes: notifications, Control Panel and stated API management routes, response cutoffs, chargebacks, retrievals, re-opens, pre-arbitrations, statuses, and the Dispute Report. It explicitly routes PayPal disputes elsewhere. As a 2026-09-16 documentation snapshot, it is not independent current NAB or card-network policy, proof of a merchant account's eligibility or configuration, or evidence that any dispute action or fund movement succeeded. See [[braintree]] and [[disputes]].

## Key takeaways

- Braintree says a dispute triggers an email from its disputes address. The first gateway admin is the default recipient, but notification frequency and recipients can be changed in the Control Panel. User Recipients remain constrained by their roles and sub-merchant associations, while an address entered in the Email Address field receives all dispute notifications. Webhooks can also report status changes to Open, Won, or Lost.
- The captured page shows two Control Panel instruction sets because Braintree says it was rolling out a dispute-management interface change. Both routes expose dispute review, evidence or acceptance actions; the page also states that disputes can be managed through the API.
- Every chargeback, retrieval, or pre-arb has a Control Panel reply-by date tied to the account time zone. At 12am on that date, the opportunity to submit evidence is lost; if the case expires, Braintree says it sends an Accept response on the merchant's behalf and the chargeback can no longer be disputed.
- For a chargeback, the article says the original transaction amount is automatically debited within seven days of the dispute report and held by the bank until resolution. A favorable ruling credits the transaction amount back and avoids the chargeback fee; losing or accepting returns the disputed amount to the cardholder and incurs a fee whose standard amount is in the merchant's pricing agreement.
- A retrieval is an information request for an unidentifiable charge. The article distinguishes it from chargebacks and pre-arbs because funds are not removed and no retrieval-processing fee is charged; it gives an 11-day response period and recommends providing identifying information. For a fraud-related retrieval, refunding is presented as advice that may help avoid a later chargeback fee, not as a requirement or guaranteed outcome.
- A re-open gives the merchant another opportunity to support the claim. When no additional evidence is available, the article says the case can remain open until expiry and the bank will decide from the evidence already supplied.
- A pre-arbitration is described as a second cardholder dispute after the merchant won the chargeback. The NAB-specific note says NAB treats disputes as one continuous dispute, so continued challenges may appear as additional chargebacks rather than a pre-arbitration escalation.

## Detail locators

- Notification defaults, recipient visibility, email-address behavior, and webhook status changes: raw lines 25-46.
- Interface-rollout variants, Control Panel actions, reply-by cutoff, expiry effect, reason-code guidance, and the stated API route: raw lines 49-85.
- Chargeback definition, debit and hold, ruling outcomes, fees, acceptance, evidence, and timeline: raw lines 90-127.
- Retrieval definition, no-debit/no-fee distinction, response period, and fraud-related refund advice: raw lines 130-136.
- Re-open handling and original-evidence continuation: raw lines 139-143.
- Pre-arbitration definition and NAB continuous-dispute treatment: raw lines 146-150.
- Displayed dispute statuses and meanings: raw lines 153-162.
- Dispute Report permission, access path, fields, and analysis/reconciliation use: raw lines 165-175.

## Related

- [[braintree]]
- [[disputes]]

## Raw Sources

- [[raw/braintree/articles/nab/chargebacks-retrievals-prearbs-2026-09-16|Braintree NAB Chargebacks, Retrievals, and Pre-Arbs (captured 2026-09-16)]]
