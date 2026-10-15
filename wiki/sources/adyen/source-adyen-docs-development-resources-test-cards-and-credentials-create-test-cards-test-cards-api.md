---
title: "Adyen Test cards API reference"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/test-cards-and-credentials/create-test-cards/test-cards-api"
raw_files:
  - "adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/test-cards-api/2026-09-15.md"
tags: [adyen, test-cards, api, testing]
---

## Overview

This Adyen Docs reference describes test-platform endpoints and request/result objects for creating custom test-card ranges for QA. It lists a SOAP `TestCard/v1` service and the JSON/FORM `createTestCardRanges` endpoint. Valid API credentials are required; this page is limited to the test platform and does not establish live-card creation or production eligibility.

## Key takeaways

- `CreateTestCardRangesRequest` supplies `accountCode`, case-sensitive `accountTypeCode` (`Company` or `MerchantAccount`), and one or more `testCardRanges`. The `TestCardRange` table defines address, holder, expiry, start/end card numbers, and optional CVC and 3D Secure fields. For AVS-compliant address data, the table says to include at least `streetAddress`; the start and end numbers are described as BIN-compliant and 6–19 digits.
- `CreateTestCardRangesResult` contains `rangeCreationResults`; each `TestCardRangeCreationResult` exposes start/end numbers and `creationResultCode` with documented values `CREATED`, `ALREADY_EXISTS`, or `ERROR`. `ALREADY_EXISTS` in an example is not evidence that a newly requested range was created.
- The API reference gives the test SOAP service and WSDL separately from the JSON/FORM endpoint. The parent **Create test cards** guide adds a **Manage test cards** Customer Area role requirement; it does not expressly distinguish whether that role applies identically to the API path. Check the current account configuration before relying on eligibility.
- The parent guide's SOAP request example places `rangeStart` above `rangeEnd` numerically, while its error handling says a start larger than the end fails. Treat that example as internally inconsistent; follow the stated range constraint and verify against the service rather than copying the reversed pair.

## Detail locators

- Raw headings **Requirements**, **SOAP endpoints**, and **JSON and FORM endpoints**, lines 22–42: valid credentials, test service/WSDL, and JSON/FORM URL.
- Raw headings **AvsAddress**, **CreateTestCardRangesRequest**, **CreateTestCardRangesResult**, and **TestCardRange**, lines 44–113: request and address fields, exact required markers, range characteristics, and 3D Secure simulation options.
- Raw heading **TestCardRangeCreationResult**, lines 115–125: per-range identifiers and result-code values.
- Related parent raw **Create test cards**, lines 27–39, 51–67, 110–129 and 229–245: role, range prerequisites, and SOAP-example versus failure-rule conflict.

## Related

- [[adyen]] — provider context
- [[adyen-payment-testing]] — test-only payment and fixture boundaries

## Raw Sources

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/test-cards-api/2026-09-15|Test cards API reference (2026-09-15 snapshot)]]

## Related raw evidence

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15|Create test cards parent guide (2026-09-15 snapshot)]]
