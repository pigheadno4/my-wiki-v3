# Braintree C34 Group A route recheck addendum

Affected question: `articles-adyen-reconciliation` Q1 only. Original report preserved unchanged.

## Correction and final verdict

The initial **PASS** missed that `[[braintree-index]]` directly listed the Adyen reconciliation source but did not link `[[payment-reconciliation-reporting]]`; therefore the required index → concept edge was absent and the original exact route verdict was incorrect.

Targeted recheck now confirms the coordinator-added edge at `wiki/braintree-index.md:506`:

[[index]] → [[braintree-index]] → [[payment-reconciliation-reporting]] → [[source-braintree-articles-adyen-reconciliation]] → [[raw/braintree/articles/adyen/reconciliation-2026-09-16]].

- Root → Braintree index: `wiki/index.md:11`.
- Braintree index → concept: `wiki/braintree-index.md:506`.
- Concept → source: `wiki/concepts/payment-reconciliation-reporting.md:111`.
- Source → concept/raw: `wiki/sources/braintree/source-braintree-articles-adyen-reconciliation.md:45,51`.
- Source bytes remain identical to the approved candidate: SHA-256 `82694da5ee7c2ac3d99335a434d0bec65b13bf4572d22adf61ceae0bfb810cee` **MATCH**.
- Pinned raw remains identical to the manifest: SHA-256 `79fb24b1450f9c9946b4fde1649bfcc8f3df08edbbfffd160bf91718cc69fd58` **MATCH**; embedded source identity remains `https://developer.paypal.com/braintree/articles/adyen/reconciliation`.

Final affected-Q1 verdict: **PASS after route repair**. No semantic answer, source bytes, raw bytes, or other question verdict was re-reviewed or changed.

Completed UTC: `2026-10-04T05:20:44Z`
