# Braintree C19 ten-page selection review

Status: COMPLETE — the exact manifest was approved and the campaign closed on
2026-09-27. The selection below was metadata-only before execution.

## Purpose and boundary

Extend website retrieval to ten unowned `get-started` pages: six general
orientation pages and four data-migration pages. They total **984 file lines**
by `wc -l`. Selection checked only paths, embedded source URLs, SHA-256 hashes,
source-target absence and absence of primary `raw_files` ownership. Titles and
URLs do not establish product facts. One already owned sibling, Transaction
Lifecycle, is excluded; Control Panel Declines and SCIM remain outside this
round. Each worker and independent initial reviewer must read its assigned raw
page completely after approval.

Keep overview/navigation distinct from payment-method or currency evidence;
keep export, import and public-key migration routes distinct. Sources are
retrieval entries with material warnings, not replacement manuals. The
2026-09-16 collection date does not establish current behavior.

## Exact jobs and fixed query questions

`manifest.json` pins each raw path, SHA-256, embedded canonical URL and proposed
source target. Longer/more cross-boundary pages start earlier.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| get-started-data-migration-imports | 264 | Where is Braintree data import documented? | What import purpose, prerequisites, process and consequential boundaries does the collected page document? |
| get-started-data-migration-exports | 148 | Where is Braintree data export documented? | What export purpose, prerequisites, process and consequential boundaries does the collected page document? |
| get-started-overview | 94 | Where is the Braintree getting-started overview? | Which topics does this page itself explain, and which does it only route to other pages? |
| get-started-payment-methods | 90 | Where is the getting-started payment-method guide? | Which payment-method scope and qualifications does this page itself document? |
| get-started-currencies | 89 | Where is Braintree's getting-started currency guidance? | Which currency-related choices and qualifications does this page itself document? |
| get-started-data-migration-public-key | 82 | Where is the data-migration public-key guide? | What is the key's documented role and what handling boundaries are stated? |
| get-started-try-it-out | 77 | Where is trying Braintree out documented? | Which trial, sandbox or production boundaries does this page itself document? |
| get-started-explore | 57 | Where is the Braintree explore guide? | Which topics does it explain directly versus merely link to? |
| get-started-data-migration-overview | 47 | Where is the data-migration overview? | Which migration paths does it identify and which details are delegated to dedicated pages? |
| get-started-get-paid | 36 | Where is the getting-paid starting guide? | What starting action and scope does it describe without implying settlement or funding proof? |

## Fixed query groups

A: Getting Started Overview + Explore.
B: Try It Out + Get Paid.
C: Payment Methods + Currencies.
D: Data Migration Overview + Imports.
E: Exports + Public Key.

Two exact questions per page, four per group, **20 total**. For each page,
record a complete read, root/provider-index → concept → source → raw route,
object/action match, direct answer, exact raw locator and verdict. Make one
bounded gap sweep per group. The three `audit_job_ids` are exemplars within
these groups, not extra audits.

## Approval and execution boundary

- Recheck all hashes/URLs, source ownership and target absence, C18 closure,
  the 151-source baseline (135 website + 16 GitHub), and actual native-agent
  capacity immediately before execution.
- Only after exact-manifest approval, use the existing three dynamic child
  slots, Sol medium workers and different Sol high initial reviewers, at most
  three attempts, and coordinator-only repository writes.
- Promote approved concept routes before corresponding sources. Update company,
  provider index/log and source count once at close; keep website documents
  distinct from GitHub implementation evidence.
- This exact manifest was separately approved before runtime initialization.
  C19 execution does not authorize new collection, commit, push or C20.
