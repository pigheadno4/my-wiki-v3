---
title: "Adyen StoreToken batch request file"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file/2026-09-15.md"
tags: [adyen, batch-processing, store-token, request-file, merchant-reference]
---

## Overview

This Adyen SFTP batch **StoreToken request-file** page defines the parent `L` line that carries metadata for associated `SL` sub-lines. It stops after introducing the StoreToken sub-line section; retrieve the separate child guide for sub-line fields. The raw snapshot was captured 2026-09-15. A correctly shaped request line is not proof of token creation, payment authorisation, payout, or batch acceptance. See [[adyen]] and [[adyen-batch-processing]].

## Key takeaways

- The table marks `L` fields 1–6 required: `L` record type, sequential line number within its batch block, `MerchantAccount` account type, merchant-account name, lowercase `storeToken` processing type, and a merchant reference. The merchant reference may keep a value referring to the original payment authorisation reference or take a new value for this modification request. It remains a **merchant reference**, not a PSP reference inferred from the field description.
- Field 7 `EchoData` is optional, can be returned exactly as supplied and is not used by Adyen's payments platform; the table caps it at 80 characters. The table's `ValidationError` wording routes to a separate validation-error **result** file, not an alternate StoreToken request status.
- This parent page gives no substantive `SL` field inventory despite its `## StoreToken sub-lines` heading. Use the separately ingested payout-oriented StoreToken child guide for its specific shopper, recurring and instrument sub-lines and prerequisites. Do not import its behavior into this parent line definition.
- The page supplies no result record, generated token identifier, authorization state, payout state, or final financial outcome. Distinguish request formatting from validation ACK, token result, and payment or payout outcomes.

## Detail locators

- `## storeToken lines`, lines 16–29: `L` metadata purpose, required fields 1–6, optional EchoData, and linked validation-error result format.
- `## StoreToken sub-lines`, lines 31–33: section heading and introductory sentence only, without sub-line schemas.

## Related

- [[adyen-batch-processing]] — batch-file route and reciprocal source link.
- [[adyen-tokenization]] — separate stored-payment-method lifecycle.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-storetoken-request-file-storetoken-request-for-payout]] — child sub-line guide; its detailed behavior is not imported here.
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]] — common outer request-file records.

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/storetoken-request-file/2026-09-15|StoreToken request parent-line schema, captured 2026-09-15]]
