---
title: "Adyen Marketplace: test verification errors"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/test-verification-errors"
raw_files:
  - "adyen/docs/marketplaces/test-verification-errors/2026-09-15.md"
tags: [adyen, marketplaces, verification, testing]
---

## Overview

This 2026-09-15 Marketplace-path guide describes **TEST-environment** simulation of failed verification checks and remediation for Adyen for Platforms or Issuing integrations. It uses Legal Entity Management API request headers, an account holder linked to the affected legal entity, account-holder webhooks or object GETs for errors, then a separate PATCH with a test resolution code. It does not establish a live user's KYC outcome, enabled capability, payout eligibility or payment result. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The prerequisites include Legal Entity Management API credentials, a Configuration API web-service credential if inspecting errors by API, and subscription to `balancePlatform.accountHolder.updated` for failed-verification updates. The guide says TEST checks pass by default **when required fields and documents are provided**; the test header forces a failure scenario. This is not a production verification guarantee.
- For a forced failure, send **one suberror code at a time** in `x-requested-verification-code` on Legal Entity Management API `POST /legalEntities`, `POST /documents`, or `POST /transferInstruments`. The header is **TEST-only** and **cannot be used with hosted onboarding**. The illustrated codes are `1_3004` for individual name/residence, `1_3008` for an incomplete ID image, and `1_7002` for an invalid bank-account number.
- Create an account holder for the legal entity under test, or for the legal entity owning the document or transfer instrument. Read errors via `balancePlatform.accountHolder.updated` or a GET for the affected object. The examples show parent `verificationErrors`, nested `subErrors` and `remediatingActions`; a sample account holder can have `status: Active` while `sendToTransferInstrument.allowed` is false and `verificationStatus` is invalid. Do not equate account-holder Active with a usable capability.
- To simulate successful remediation in TEST, send `x-requested-verification-code: 0_0001` with a PATCH to the corresponding legal entity, document or transfer instrument. The page says this resolves associated suberrors **if the error handling is successful**. It does not prove that a real person's data or document was accepted.
- Treat the language and webhook payloads as examples. The transfer-instrument webhook sample has missing JSON commas and a different nesting of `transferInstruments` from the other samples; it cannot be copied verbatim as valid JSON or taken as a definitive schema. The document-remediation curl example uses an `SE...` path ID, unlike the document-ID placeholder used elsewhere, so verify IDs against the actual object.

## Detail locators

- Raw lines 19–47 define TEST behavior, credentials/webhook prerequisites, allowed POST targets, one-code limit and hosted-onboarding exclusion.
- Raw lines 49–1161 contain the legal-entity, document and transfer-instrument forced-failure examples and versioned TEST SDK snippets.
- Raw lines 1162–1174 require the owning account holder and describe webhook/GET checks; lines 1175–1505 show object errors and webhook examples, including the malformed transfer-instrument sample near the end.
- Raw lines 1507–1520 define the conditional `0_0001` remediation flow; lines 1521–2529 contain corresponding PATCH examples, including the document path-ID mismatch.

## Related

- [[adyen-platforms]] — main platform concept for this Marketplace-path test guide.
- [[adyen]] — provider context.
- [[adyen-issuing]] — also named in the integration prerequisites.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/marketplaces/test-verification-errors/2026-09-15|Adyen Marketplace verification-error TEST scenarios, captured 2026-09-15]]
