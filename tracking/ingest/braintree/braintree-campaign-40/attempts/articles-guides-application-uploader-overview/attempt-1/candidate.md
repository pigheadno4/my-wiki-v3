---
title: "Braintree Application Uploader Overview"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/application-uploader/overview"
raw_files:
  - "braintree/articles/guides/application-uploader/overview-2026-09-16.md"
tags: [braintree, application-uploader, bill-pay, onboarding, control-panel, csv]
---

## Overview

This collected Braintree article describes a Control Panel Application Uploader for select Bill Pay merchants that need to submit application information for hundreds of billers. The tool accepts bulk CSV submissions for review, while later Global Credit approval is what the page ties to automatic configuration of the payment and payout methods specified for a biller.

The page requires completion of an initial application, special account configuration by a PayPal Account Manager, and Braintree Control Panel credentials. This 2026-09-16 snapshot does not prove current availability, merchant or biller eligibility, account configuration, application approval, method enablement, or readiness to process.

## Key takeaways

- Availability is limited to select merchants, and the described actor is a Bill Pay merchant submitting application information for its billers. Access requires the initial application process, special account configuration by a PayPal Account Manager, and Control Panel login credentials.
- The uploader accepts only CSV documents and supports submitting tens or hundreds of applications at one time. The linked PayPal Intake Data Dictionary defines required application information, while a linked sample file provides the required headers; use the raw locator for those routine file-preparation details rather than inferring fields that this overview does not reproduce.
- Uploading is a submission for review, not approval. The page says successfully created applications are submitted to Underwriting, then separately says Global Credit reviews them; only after review and approval does it say billers are automatically configured with the payment and payout methods specified in their applications.
- Submission is consequential: after an application is submitted, it cannot be edited or altered. The article instructs merchants to vet the selected file first. For incorrect or missing data, its correction loop removes successful applications from the original file, edits only failed applications using the error breakdown, renames the file, and resubmits it.
- Uploaded File History exposes prior-upload summaries and error details only after at least one file has been uploaded. An Account Management follow-up about an individual biller or notice that a biller is ready to process remains a later step; this page is not evidence that either event occurred.

> [!warning] Submission is irreversible
> The captured page says a submitted application cannot be edited or altered. Verify the selected CSV and all application information before choosing **Submit Applications**; failed entries follow the page's remove-successes, correct, rename, and resubmit loop.

> [!warning] Submission, approval, and processing are separate
> A created and submitted application is under review. Do not treat upload success as Global Credit approval, biller configuration, payment- or payout-method enablement, or readiness to process. The snapshot also does not establish current Application Uploader availability or account eligibility.

## Detail locators

- Select-merchant availability, Bill Pay merchant and biller scope, bulk-submission purpose, and post-approval configuration statement: `# Overview`, lines 17-24.
- Initial application, special PayPal Account Manager configuration, and Control Panel credential prerequisites: `## Requirements`, lines 27-29.
- CSV-only input, linked PayPal Intake Data Dictionary, and sample-file header route: `## Create a file`, lines 32-38.
- Control Panel navigation, selected-file row-count check, submission action, and no-edit warning: `## Select and upload your file`, lines 41-56.
- Created-versus-failed submission results, error-detail and CSV download routes, failed-entry resubmission loop, and upload-history visibility: `## View the results, correct errors, and resubmit`, lines 61-89.
- Global Credit review and later Account Management follow-up/readiness boundary: `## Touch base with your Account Manager`, lines 94-98.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/guides/application-uploader/overview-2026-09-16|Braintree Application Uploader overview]] - complete collected article for availability, prerequisites, CSV preparation, Control Panel submission, irreversible submission, error correction, review and Account Management follow-up
