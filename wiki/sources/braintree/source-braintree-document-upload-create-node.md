---
title: "Braintree Document Upload Create (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/document-upload/create/node"
raw_files:
  - "braintree/docs/reference/request/document-upload/create/node-2026-09-16.md"
tags: [braintree, node-js, document-upload]
---

## Overview

This Braintree Node.js reference shows creating a document upload through `gateway.documentUpload.create()`. The example supplies an `EvidenceDocument` kind and a file stream, but it does not establish attaching the resulting upload to a dispute or submitting dispute evidence.

## Key takeaways

- The example opens `local_file.pdf` with `fs.createReadStream()` and passes that stream as `file` alongside `DocumentUpload.Kind.EvidenceDocument`. These are example values, not an exhaustive request schema or supported-file policy.
- The result-handling branch intends to test success, access `documentUpload` on success, and log errors otherwise.
- The displayed Promise callback is internally inconsistent: it binds the callback parameter as `result` but then reads `response.success`, `response.documentUpload`, and `response.errors`. This entry does not silently repair the example or claim that it runs verbatim.
- The page shows upload creation only. It does not state that creation attaches, submits, removes, or finalizes evidence for a dispute, and it provides no dispute identifier or dispute-state transition.

## Detail locators

- Document-upload creation identity: `# Document Upload: Create`, line 13.
- Node file-stream input, `EvidenceDocument` kind, and `gateway.documentUpload.create()` call: `## Examples > ### Node`, lines 19-26.
- Intended success/document result and error branches, including the `result`/`response` variable mismatch: `## Examples > ### Node`, lines 26-33.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/document-upload/create/node-2026-09-16|Braintree Node.js document-upload creation reference]] - complete collected page covering the example file stream, `EvidenceDocument` kind, create call, intended result handling, and displayed variable mismatch
