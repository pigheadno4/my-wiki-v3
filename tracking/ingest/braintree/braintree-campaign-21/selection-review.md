# Braintree C21 ten-page selection review

Status: PREPARED — not approved for execution. Selection is metadata-only.

## Purpose and boundary

Add retrieval routes for ten unowned website payment-method guides. These
pinned raw files total **1,174 file lines** by `wc -l`. Selection checked paths,
embedded URLs, SHA-256 hashes, missing source targets and absence of primary
source ownership. No raw page was read in full for this selection, and a title
or URL does not establish a capability. Workers and initial reviewers must
read their assigned complete raw after exact-manifest approval.

Keep ACH, SEPA Direct Debit, wallets, local methods, PayPal Credit, Pay Later,
UnionPay and Secure Remote Commerce distinct. Do not infer current support
from a 2026-09-16 collection snapshot. Preserve material restrictions and
route procedural and field detail to exact raw locations. The existing
**171-source** Braintree baseline is 155 website plus 16 GitHub sources.

## Exact jobs and fixed query questions

`manifest.json` pins each raw path, hash, embedded canonical URL and new source
target. Longer pages start earlier; dispatch may reprioritize a ready review
under the existing dynamic-slot rule.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| payment-methods-ach | 273 | Where is the Braintree ACH payment-method guide? | What availability, setup and payment-lifecycle boundaries does this page itself state? |
| payment-methods-venmo | 224 | Where is Braintree's Venmo payment-method guide? | What prerequisites, customer flow and limitations does this page itself state? |
| payment-methods-apple-pay | 133 | Where is Braintree's Apple Pay guide? | What setup, platform and use boundaries does this page itself state? |
| payment-methods-google-pay | 117 | Where is Braintree's Google Pay guide? | What setup, platform and use boundaries does this page itself state? |
| payment-methods-local-payment-methods | 92 | Where is the local payment methods guide? | What scope, availability and flow qualifications does this page itself state? |
| payment-methods-secure-remote-commerce | 91 | Where is Secure Remote Commerce documented? | What purpose, prerequisites and limitations does this page itself state? |
| payment-methods-paypal-credit | 68 | Where is PayPal Credit documented in Braintree? | What offer identity, eligibility and integration boundaries does this page itself state? |
| payment-methods-unionpay | 66 | Where is UnionPay documented in Braintree? | What setup, flow and limitations does this page itself state? |
| payment-methods-paypal-pay-later-offers | 59 | Where are PayPal Pay Later offers documented in Braintree? | What offer identity, eligibility and presentation boundaries does this page itself state? |
| payment-methods-sepa-direct-debit | 51 | Where is SEPA Direct Debit documented in Braintree? | What availability, timing and lifecycle boundaries does this page itself state? |

## Fixed query groups

A: ACH + SEPA Direct Debit. B: Venmo + PayPal Credit. C: Apple Pay + Google Pay.
D: Local Payment Methods + UnionPay. E: Secure Remote Commerce + Pay Later
Offers. Two exact questions per page, four per group, **20 total**. For each
page, record a complete read, index → concept → source → raw route,
object/action match, direct answer, exact raw locator and verdict. Make one
bounded gap sweep per group. The three `audit_job_ids` are exemplars, not
additional audits.

## Approval and execution boundary

- Recheck exact hashes, URLs, ownership, target absence, C20 closure, baseline
  count and native-agent capacity before initializing any runtime.
- Execution requires approval of **this exact C21 manifest**. Then use three
  dynamic child slots, Sol medium workers and different Sol high initial
  reviewers, per-page approval and at most three attempts.
- The coordinator alone promotes approved concept routes and source candidates,
  then updates company/index/log/count once at close. Website docs remain
  separate from GitHub implementation evidence.
- Preparation authorizes no worker dispatch, collection, source creation,
  commit or push.
