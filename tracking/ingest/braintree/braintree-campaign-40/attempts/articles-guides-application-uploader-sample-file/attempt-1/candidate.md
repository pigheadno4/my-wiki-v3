---
title: "Braintree Application Uploader Sample File"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/application-uploader/sample-file"
raw_files:
  - "braintree/articles/guides/application-uploader/sample-file-2026-09-16.md"
tags: [braintree, paypal, application-uploader, intake-api, onboarding, csv]
---

## Overview

This collected Braintree-hosted landing page provides download routes for PayPal Intake sample files used to prepare application data. It offers full v1 and v2 samples plus a separate branded-solution sample, and it links the [[source-braintree-articles-guides-application-uploader-paypal-intake-data-dictionary|PayPal Intake Data Dictionary]] for the application information needed by the Intake API or [[source-braintree-articles-guides-application-uploader-overview|Application Uploader]]. The uploader is stated to be available only to select merchants. See [[braintree]] and [[braintree-payment-platform]].

## Key takeaways

- For Application Uploader preparation, the page describes the example file as a model of an application file and says erasing its test data yields a header template. The first row must contain headers.
- The page states that the PayPal Intake Data Dictionary accepts two input schemas, v1 and v2, and provides a sample download for each. It separately provides a branded-solution sample.
- This captured page is a download landing page, not the contents of the linked CSV files. Use the downloaded artifacts and the applicable data dictionary for exact columns, values, formatting, conditional requirements and schema differences; do not infer those details from the navigation labels or sample values.
- Downloading or preparing a sample does not submit an application, establish merchant eligibility, prove underwriting or Global Credit approval, configure a biller, enable payment or payout methods, or show processing readiness. The linked overview documents submission and later review as separate lifecycle steps.

## Detail locators

- Select-merchant Application Uploader availability: `# Sample File > AVAILABILITY`, raw lines 17-18.
- Data Dictionary purpose for the Intake API or Application Uploader: `# Sample File`, raw line 22.
- Full and branded-solution sample roles: `# Sample File`, raw line 24.
- Header-template instruction, first-row header requirement and v1/v2 schema statement: `# Sample File > NOTE`, raw lines 27-28.
- v1, v2 and branded-solution CSV download routes: `# Sample File`, raw lines 32-40.

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[braintree-index]]
- [[source-braintree-articles-guides-application-uploader-overview]] - separate uploader access, submission, correction, review and approval lifecycle route
- [[source-braintree-articles-guides-application-uploader-paypal-intake-data-dictionary]] - separate dictionary landing page for field-group purposes and linked schema artifacts

## Raw Sources

- [[raw/braintree/articles/guides/application-uploader/sample-file-2026-09-16|Braintree Application Uploader Sample File (2026-09-16)]] - complete collected landing page for sample roles, header preparation and v1/v2/branded download navigation; linked CSV bodies were not part of this pinned raw
