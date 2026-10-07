---
title: "Braintree Functions: Act on a Fraud Score from a Vendor"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/act-on-fraud"
raw_files:
  - "braintree/docs/guides/functions/act-on-fraud-2026-09-16.md"
tags: [braintree, functions, fraud-scoring, before-authorization, gateway-rejection]
---

## Overview

This captured [[braintree|Braintree]] webpage is a documentation-preview walkthrough for a payment-method Function that runs at `beforeAuthorization`, sends transaction-derived data to an external fraud service, and maps the illustrated vendor decision back into transaction data. It is a custom Functions example rather than evidence for the built-in products routed through [[braintree-fraud-tools]]. The snapshot does not establish current availability, account eligibility, or successful execution.

## Key takeaways

- The page initializes `MyFraudCheck` with the `paymentMethod` template and `beforeAuthorization` trigger, then says transaction-call details are shared with the Function so its JavaScript can construct a request to a fraud service.
- In the illustrated response mapping, a vendor decision equal to `YES` returns `fraudDecision` in transaction custom fields; the other branch also returns that custom field and sets the transaction status to `braintree.Transaction.Status.GatewayRejected`. Both branches in the example return HTTP status code `200`. This is example behavior, not proof of a live vendor contract or a completed authorization.
- The page advises local testing before deployment, shows `btfns test` and optional custom mock-data generation, and says deployment defaults to the sandbox account. Production is a separately selected prompt option or the explicit `btfns deploy --production` command.
- A sale request can select the Function by `functionName`; the page says that selection calls it at every trigger defined in the Function configuration. It directs integrations to Custom Fields when the Function needs additional data unavailable in the Transaction API.
- The displayed code is illustrative and contains unresolved identifier inconsistencies, so the raw sample should not be treated as an executable guarantee.

## Detail locators

- **Preview availability:** `AVAILABILITY`, lines 17–18.
- **Function initialization and trigger:** `Initialize a New Function`, lines 21–28.
- **External request and response mapping:** `Write Code`, lines 29–135.
- **Local test and environment-qualified deployment:** `Test and Deploy Your Function`, lines 137–170.
- **Sale invocation and additional-data route:** `Create a Transaction`, lines 171–192.

## Related

- [[braintree]]
- [[braintree-payment-platform]] — main provider concept route for the collected Braintree Functions documentation previews.
- [[braintree-fraud-tools]] — contrast navigation for built-in fraud-tool mechanisms; keep them distinct from this custom external-vendor Function example.

## Raw Sources

- [[raw/braintree/docs/guides/functions/act-on-fraud-2026-09-16|Braintree — Act on a Fraud Score from a Vendor (2026-09-16)]]
