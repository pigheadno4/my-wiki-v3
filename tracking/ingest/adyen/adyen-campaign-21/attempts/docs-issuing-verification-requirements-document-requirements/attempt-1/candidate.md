---
title: "Adyen Issuing: requirements for document uploads"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-requirements/document-requirements"
raw_files:
  - "adyen/docs/issuing/verification-requirements/document-requirements/2026-09-15.md"
tags: [adyen, issuing, verification, documents]
---

## Overview

Adyen's Issuing document-requirements webpage (last modified 2023-08-09; raw captured 2026-09-15) describes additional documents Adyen may request when automatic verification of a user, legal entity, or bank account fails. It groups requirements for UBOs, signatories, sole proprietors, organizations, and bank accounts. This is a dated requirements snapshot, not evidence of a particular user's verification or current eligibility. [[adyen-issuing]]

## Key takeaways

- The document type in a Legal Entity API `POST /documents` request depends on the verification evidence requested. Use the corresponding section's stated `type` and document conditions rather than applying one rule to every upload. The page covers bank statements, constitutional and registration documents, photo IDs, address and residential address, source of funds and wealth, individual and organization tax IDs, industry, national ID, ownership, relationship for minors, and VAT.
- A bank-account proof must show the account holder name matching the legal business or trading name, account number or IBAN, bank location, and bank-issued indicator. The page disallows bank-card photos, edited or personalized documents, missing data, poor images, and third-party software documents. Its issuance-date bullets distinguish RIBs, cheques, online banking and TAMIEYTHPIO, with a conditional date rule for some RIBs and online banking; the later rejection list says documents older than 12 months are not accepted without repeating those exceptions. Preserve this tension instead of treating the exception as universal.
- For identity cards and driver's licenses, the front and back must be separate files in the same `POST /documents` request; the photo ID must be physical, non-expired, and match the legal-entity name. The same section also says “maximum 1 file” in its format bullets, so the snapshot contains an apparent file-count conflict for two-sided IDs. It rejects digital IDs, secondary copies, AI-enhanced or edited images, and low-quality images.
- Proof of ownership requires a visual chart covering intermediate entities, UBOs, ownership/control percentages and a signature dated within six months; whether supporting external official documents are also needed depends on who signs. Source-of-wealth supporting-document examples are illustrative when the required information is provided, and Adyen says to confirm other document types with an Adyen contact.
- The page has document-specific and country/region-specific dates, formats, sizes and accepted examples. The constitutional-document section allows up to 30 MB, while many other listed document sections say 2 MB. Check the exact section, including photo-ID regional exceptions and residential-address three- versus twelve-month windows.

## Detail locators

- Raw lines 21–53 map requested evidence to UBOs/signatories/sole proprietors, organizations, sole proprietorships and bank accounts.
- Raw lines 55–124 cover bank-account evidence, date exceptions, rejected documents, regional cheque rules and upload size.
- Raw lines 128–195 cover constitutional documents, country/region examples including “New Zealand(pilot),” and its 30 MB limit; lines 197–250 cover photo IDs, front/back requirements, prohibited alterations and regional notes.
- Raw lines 253–359 cover organization proof of address and funding/wealth evidence; lines 294–352 contain the source-of-wealth information and illustrative-document table.
- Raw lines 360–424 cover individual and organization tax IDs, industry and national ID evidence; lines 425–477 cover ownership diagrams and conditional external-document support.
- Raw lines 478–571 cover residential address, a minor's legal-representative relationship, registration and VAT documents.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-requirements/document-requirements/2026-09-15|Adyen Issuing document upload requirements, captured 2026-09-15]]
