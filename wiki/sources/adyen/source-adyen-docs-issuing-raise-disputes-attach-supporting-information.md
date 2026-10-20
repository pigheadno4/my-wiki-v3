---
title: "Adyen Issuing: Attach supporting information to raised disputes"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/raise-disputes/attach-supporting-information"
raw_files:
  - "adyen/docs/issuing/raise-disputes/attach-supporting-information/2026-09-15.md"
tags: [adyen, issuing, disputes, attachments, evidence]
---

## Overview

This Adyen Issuing guide, modified and captured 2026-09-15, explains how a card-issuing platform supplies evidence files for a **raised cardholder dispute** through the Balance Platform Transfers API. Adyen recommends adding receipts, merchant correspondence or other reviewable evidence before submitting the dispute. The parent [[source-adyen-docs-issuing-raise-disputes|Raise disputes]] guide owns general requirements, eligibility and lifecycle. This issuer-side evidence flow is distinct from acquiring-side merchant dispute defense. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- Base64-encode a cardholder-provided file, then POST `/disputes/{disputeId}/attachments` with `attachmentType` (`receipt`, `correspondence` or `other`), `fileName` and `content`. The guide lists JPEG, PDF and TIFF support, asks for clear photos, and says the filename including extension must be **4–17 characters** with `jpeg`, `pdf` or `tiff` extension. Send a separate POST for each attachment. Its examples use a TEST `btl/api/v4` endpoint.
- Save the returned `attachmentId` separately from the dispute ID. GET `/disputes/{disputeId}/attachments/{attachmentId}` returns metadata and Base64 `content` that can be decoded for viewing; GET `/disputes/{disputeId}/attachments/` lists attachments for that dispute. The list example shows IDs and filenames, while the individual GET example includes content.
- DELETE `/disputes/{disputeId}/attachments/{attachmentId}` removes an attachment from the dispute when the response is HTTP **204 No Content**. If reuploading a recently deleted file, use a unique filename. Adyen says it **may retain attached files for audit and compliance**, so API deletion is not proof of physical erasure.
- The page recommends attachments **before submission**; it does not itself establish that post-submission attachment changes are allowed. Upload, retrieval or deletion confirms an attachment operation, not card-scheme acceptance, dispute success or returned funds.

## Detail locators

- Pinned raw lines 15–23: purpose, recommended pre-submission evidence and parent-guide requirements.
- Pinned raw lines 25–45: Base64, POST path, supported formats, filename constraints and one POST per file; lines 47–73: TEST example and returned `attachmentId`.
- Pinned raw lines 75–101: individual GET and decoded content; lines 103–137: per-dispute attachment list.
- Pinned raw lines 139–161: DELETE, possible retained files, HTTP 204 and unique-name reupload warning.

## Related

- [[source-adyen-docs-issuing-raise-disputes]] — issuer-side dispute requirements and lifecycle.
- [[source-adyen-docs-issuing-raise-disputes-manage-disputes]] — draft edit, submit and close transitions.
- [[adyen-issuing]] — Issuing cardholder dispute context.

## Raw Sources

- [[raw/adyen/docs/issuing/raise-disputes/attach-supporting-information/2026-09-15|Adyen Issuing dispute-attachment guide, captured 2026-09-15]]
