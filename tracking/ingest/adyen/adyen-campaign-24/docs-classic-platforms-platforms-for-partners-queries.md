# C24 Classic partner platform retrieval checks

## Q1 — What does a Classic partner platform need before routing ecommerce payments?

This applies only to the partner arrangement, where Adyen connects each sub-merchant directly to card schemes and the partner platform cannot process on its behalf (raw lines 19–28). Create the account holder, collect/verify SAQ A and KYC, have Support enable ecommerce stores, add the store, and await `ACCOUNT_HOLDER_STORE_STATUS_CHANGE` to `Active` before payment processing (raw lines 40–71, 146–243). A sub-merchant's own payment domain must be in allowed origins (raw lines 265–267). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-platforms-for-partners]] → [[raw/adyen/docs/classic-platforms/platforms-for-partners/2026-09-15]].

## Q2 — Which channel, session and routing limits matter?

Ecommerce sub-merchants complete SAQ A; POS sub-merchants need stores but the guide exempts them from SAQ A (raw lines 25–30). In a custom flow, `/getPciQuestionnaireUrl` gives a one-time link usable within 15 seconds and a 30-minute session; late redirect/reload gives HTTP 401 and requires a new URL, while verification results arrive by webhook (raw lines 79–123). Prose `redirectURL` differs from JSON `redirectUrl` (raw lines 98–112). A payment can split across holders but routes through only one store (raw lines 269–277); Pending store or example `/payments` body does not establish activation or payment outcome. Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-platforms-for-partners]] → [[raw/adyen/docs/classic-platforms/platforms-for-partners/2026-09-15]].
