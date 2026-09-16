# PayPal documentation collection — profile router

Read [../psp-collection.md](../psp-collection.md), then the matching profile:

| Corpus | Profile | Implementation status |
| --- | --- | --- |
| `docs.paypal.ai` | [paypal-ai.md](paypal-ai.md) | Existing `fetch_psp.py paypal` in main; config key remains `paypal` |
| Legacy `developer.paypal.com` | [paypal-legacy.md](paypal-legacy.md) | Historical policy restored; no dedicated collector in main |
| Upgraded `developer.paypal.com` | [paypal-new.md](paypal-new.md) | Collector and data remain in `.worktrees/paypal-new-collection/` |

These are distinct documentation corpora, not interchangeable mirrors. Preserve existing raw provenance; do not rename or merge raw based on this routing update. Braintree has its own [braintree.md](braintree.md) profile. GitHub evidence follows the separate GitHub workflow.
