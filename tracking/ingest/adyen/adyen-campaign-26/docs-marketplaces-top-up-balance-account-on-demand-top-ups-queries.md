# Retrieval checks — docs-marketplaces-top-up-balance-account-on-demand-top-ups

Q1. What is this guide's purpose and what must be in place before a Marketplace on-demand top-up?

A1. It documents a user-funded, one-off payment intended to increase that user's balance account (raw lines 15–19). It calls for Checkout credentials, webhook reception and Support enablement; verified-bank funding additionally needs both allowed/verification-valid capabilities and a SEPA-zone, UK or US bank account, while another payment method needs allowed/verification-valid `receiveFromPlatformPayments` (raw lines 21–52). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-top-up-balance-account-on-demand-top-ups]] → [[raw/adyen/docs/marketplaces/top-up-balance-account/on-demand-top-ups/2026-09-15]].

Q2. Can an authorized `/payments` response prove the user's balance account was credited, and what booking or debit caveats matter?

A2. No. The example response is `Authorised` (raw lines 193–216, 762–782), but top-up webhooks track through funds added or failure (raw lines 784–786). Initiation is POST `/payments`, not `/sessions` (raw lines 110–114). Omitted `splits` book to the liable account as a regular payment, rather than classifying a `TopUp` to the user account (raw lines 133–150). SEPA requires prior mandate; UK BACS requires per-top-up confirmations and advance notice, with the source's 10-day warning alongside its two-business-day due-date description (raw lines 63–108). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-top-up-balance-account-on-demand-top-ups]] → [[raw/adyen/docs/marketplaces/top-up-balance-account/on-demand-top-ups/2026-09-15]].
