---
title: "Braintree GraphQL Uploading Files for Mutations Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/uploading_files"
raw_files:
  - "braintree/graphql/integration_guides/uploading_files-2026-09-16.md"
tags: [braintree, graphql, file-upload, multipart, disputes, evidence]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the multipart transport used when a Braintree GraphQL mutation requires a file. The snapshot says Braintree partially implements the GraphQL Multipart Request Spec, supports one file per request, and identifies `createDisputeFileEvidence` as the only mutation then requiring this route. It is an integration example, not an exact GraphQL schema baseline, proof of current support, merchant approval, Control Panel dispute access, evidence acceptance, submission to a bank, or a dispute outcome.

## Key takeaways

- The request changes from the ordinary JSON transport to `multipart/form-data` and attaches the GraphQL operation plus a file. The guide's cURL uses a Sandbox endpoint, a dated `Braintree-Version` example and an Authorization header placeholder; it separately says the version and authorization headers are the same as for a standard GraphQL request. Those values illustrate request structure and do not establish Production availability, valid credentials or successful authentication.
- The multipart `operations` part is required and has `application/json` type. It carries the GraphQL query and variables, including a `file: null` placeholder. A required `map` part links that placeholder's path, shown as `variables.file`, to the named file part. The file part supplies the local path and a valid MIME type.
- The snapshot supports one file at a time and identifies `createDisputeFileEvidence` as the only mutation then requiring file upload. For that mutation it lists PNG, JPG, JPEG and PDF, with a maximum file size of 4 MB. Do not generalize those limits to other APIs, mutations or current product behavior.
- The example mutation returns a dispute and an evidence object, and the page says the response has the same structure as another GraphQL API response. The displayed fields and response statement are transport guidance, not proof that a particular file passed validation, became admissible dispute evidence, was finalized or submitted, or changed the merchant's business approval or dispute result.

> [!warning] Upload and dispute-lifecycle boundary
> A multipart upload request is only the documented transport for the file-evidence mutation. This page does not establish that a merchant can access disputes, that the dispute is in an eligible state, that the uploaded material will be accepted or sent to the bank, or that any protection, reimbursement or dispute outcome follows. Verify the applicable account, dispute-state, evidence and finalization requirements separately.

## Detail locators

- Partial GraphQL Multipart Request Spec implementation, single-file support and `createDisputeFileEvidence` identity: opening paragraph, raw line 16.
- Example mutation selection for the dispute and evidence objects: `### Mutation`, raw lines 18-35.
- Changed content type and attached-file request requirement: raw line 37.
- Supported PNG, JPG, JPEG and PDF file types and 4 MB maximum: raw line 39.
- Sandbox cURL endpoint plus example Braintree version, Authorization, Accept and multipart headers: `### CURL`, raw lines 42-48.
- Required `operations` part, JSON type, query/variables object and `file: null` placeholder: raw lines 49-57 and 65-66.
- Required `map` part, placeholder-path-to-file-label association, local file path and valid MIME-type condition: raw lines 58-59 and 67-68.
- Standard GraphQL version/authorization-header relationship and ordinary GraphQL response-structure statement: raw lines 70-72.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Exact commit-qualified GraphQL contract route: [[source-github-graphql-api]]

## Related raw API references

The page links to the GraphQL reference entry for `createDisputeFileEvidence` and to the external GraphQL Multipart Request Spec. Those linked targets were not read as evidence for this entry and are navigation only; they do not establish exact schema equivalence, current service support, account authorization, dispute-state eligibility, evidence acceptance, finalization or outcome.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/uploading_files-2026-09-16|Braintree GraphQL Uploading Files for Mutations guide]] - complete collected page covering the partial multipart transport, single-file and type/size limits, required form objects, standard-header relationship and response structure
