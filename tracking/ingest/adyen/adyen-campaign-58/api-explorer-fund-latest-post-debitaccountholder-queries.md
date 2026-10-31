# Fixed queries — Fund API POST /debitAccountHolder

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-debitaccountholder.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/debitAccountHolder

## Q1

For `Fund/latest/post/debitAccountHolder`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: The TEST Fund v6 endpoint sends a direct debit request to the bank account identified by `bankAccountUUID` for `accountHolderCode`; `merchantAccount`, minor-unit `amount` with `currency` and `value`, and at least one `splits` item are also required. Split destination account and amount/reference requirements depend on integration/type: Classic needs split amount for all types and a reference for `MarketPlace`; the page includes separate Balance Platform rules. Its Classic type list says `Marketplace` while the example/condition say `MarketPlace`, so the accepted token casing is unresolved here. It lists a 403 permission failure but no named role or mandate/eligibility criteria. See canonical source above and pinned raw `raw/adyen/api-explorer/Fund/latest/post/debitAccountHolder/2026-09-15.md` lines 5–33, 35–66, 135–145.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: The page says successful debit funds settle to the split accounts and the debit result arrives by `DIRECT_DEBIT_INITIATED` webhook. A 200 reports request success; 202 is accepted but unfinished. Optional response identifiers and the 200 example's `pspReference`/`submittedAsync: "false"` do not prove completed bank collection or credited split funds; `submittedAsync` is not in the listed schema. Errors include 400, 401, 403, 422 and 500. This captured TEST v6 page supplies no live eligibility, actual debit, final funds receipt, or detailed consent/limit rules. See canonical source above and pinned raw lines 5–12, 67–106, 109–183.
