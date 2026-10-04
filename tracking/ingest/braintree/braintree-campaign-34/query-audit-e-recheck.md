# C34 query audit E — targeted recheck addendum

- recheckedUTC: `2026-10-04T05:19:59Z`
- Original evidence preserved unchanged: `/tmp/c34-query-audit-e.md` remains the historical **7 PASS / 1 FAIL** audit.
- Final affected-Q1 verdict: **PASS**. Effective post-repair result for group E: **8 PASS / 0 FAIL**.

## Repaired mechanical route

`wiki/index.md:11` → `wiki/braintree-index.md:506` (`[[payment-reconciliation-reporting]]`) → `wiki/concepts/payment-reconciliation-reporting.md:110` → `wiki/sources/braintree/source-braintree-articles-chase-reporting-reconciliation.md:38` → `raw/braintree/articles/chase/reporting-reconciliation-2026-09-16.md`.

- The promoted Chase source is byte-identical to its approved attempt-1 candidate; current source SHA-256 is `2bedb3483d3719d2f7c65f82bed16de083cc2ef6e485edf575d71bdcf80c211e`.
- The Chase raw SHA-256 remains `0597f533e17ea0b9e276662845132fb5f91f72923bc9837a52e4dcc7f8e37720`, matching the C34 manifest.
- The same Braintree-index edge also serves Adyen reconciliation through `wiki/concepts/payment-reconciliation-reporting.md:111`. Its promoted source remains byte-identical to the approved candidate (current source SHA-256 `82694da5ee7c2ac3d99335a434d0bec65b13bf4572d22adf61ceae0bfb810cee`), and its raw remains manifest-matched at `79fb24b1450f9c9946b4fde1649bfcc8f3df08edbbfffd160bf91718cc69fd58`.
- No source/raw content was reread or reanalyzed; this addendum records only the requested edge, byte-equality, and hash checks.
