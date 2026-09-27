# Braintree C18 ten-page selection review

Status: COMPLETE — the exact manifest was approved and the campaign closed on
2026-09-27. The selection below was metadata-only before execution.

## Purpose and boundary

Extend Braintree website retrieval into Control Panel administration and Vault.
The ten pinned raw pages total **1,194 file lines** by `wc -l` (versus C17's 666), so
this round may take longer. Selection is metadata-only: paths, provenance URLs,
hashes, absent source targets and absent primary source ownership were checked;
no content fact is inferred from a title. Each assigned worker and initial
reviewer must read its raw page in full after dispatch approval.

Keep credentials/security, user permissions, account access, Vault customers,
payment methods and card verification separate. A source should give a useful
retrieval route and material warnings, leaving procedural detail in immutable
raw. The 2026-09-16 collection date does not establish current product behavior.

## Exact jobs and fixed query questions

`manifest.json` pins the raw path, SHA-256, canonical URL and proposed source
target for each job. Queue order starts longer or cross-boundary pages early.

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| control-panel-important-gateway-credentials | 188 | Where are Braintree important gateway credentials documented? | Which credential types, access paths and environment or security boundaries does the collected page document? |
| control-panel-search | 170 | Where is Braintree Control Panel search documented? | Which search purposes, result boundaries and permission or date qualifications does this page document? |
| control-panel-users-roles-managing-users-roles | 138 | Where is managing Braintree Control Panel users and roles documented? | Which management actions, prerequisites and scope limits does this page document? |
| control-panel-vault-update | 129 | Where is updating customer information in Braintree Control Panel Vault documented? | Which customer-information update actions and boundaries does this page document? |
| control-panel-vault-card-verification | 126 | Where is Braintree Control Panel Vault card verification documented? | Which verification purpose, access, outcome and payment or Vault boundaries does this page document? |
| control-panel-custom-fields | 123 | Where are Braintree Control Panel custom fields documented? | Which configuration and visibility boundaries does this page document? |
| control-panel-users-roles-log-in-with-paypal | 94 | Where is Log In with PayPal for Braintree Control Panel documented? | Which setup, account and access boundaries does this page document? |
| control-panel-vault-create | 83 | Where is creating customers in Braintree Control Panel Vault documented? | Which creation steps and resulting Vault or payment-method boundaries does this page document? |
| control-panel-users-roles-role-permissions | 80 | Where are Braintree Control Panel role permissions documented? | Which role-permission categories and action scopes does this page define? |
| control-panel-vault-overview | 63 | Where is Braintree Control Panel Vault overview documented? | Which Vault administration routes does this overview identify, and what does it leave to dedicated pages? |

## Fixed query groups

A: Important Gateway Credentials + Custom Fields.
B: Search + Role Permissions.
C: Managing Users and Roles + Log In with PayPal.
D: Vault Overview + Create New Customers.
E: Vault Update Customer Information + Card Verification.

Two exact questions per page, four per group, **20 total**. For each page,
record a complete read, root/provider-index → concept → source → raw route,
object/action match, direct answer, exact raw locator and verdict. Make one
bounded gap sweep per group. The three `audit_job_ids` are exemplars within
these groups, not extra audits.

## Approval and execution boundary

- Before execution, recheck hashes/URLs, source ownership and target absence,
  C17 closure, the 141-source baseline (125 website + 16 GitHub), and actual
  native-agent capacity.
- After exact-manifest approval, use the existing three dynamic child slots,
  Sol medium workers and different Sol high initial reviewers, at most three
  attempts, coordinator-only repository writes, and bounded corrections.
- Promote approved concept routes before corresponding sources. Update the
  company page, provider index/log and source count once at close; retain the
  distinction between website documentation and GitHub implementation evidence.
- Four other unowned Control Panel pages are outside C18: Transactions Declines,
  Refunds/Voids/Credits, SCIM FAQ and SCIM Integration. They are not silently
  classified as unnecessary.
- This exact manifest was separately approved before runtime initialization.
  No new raw collection, commit, push or next campaign is authorized here.
