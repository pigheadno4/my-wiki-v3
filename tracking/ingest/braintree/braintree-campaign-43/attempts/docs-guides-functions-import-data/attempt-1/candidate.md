---
title: "Braintree Functions: Import Data"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/import-data"
raw_files:
  - "braintree/docs/guides/functions/import-data-2026-09-16.md"
tags: [braintree, functions, data-import, transactions, developer-tools]
---

## Overview

This captured [[braintree|Braintree]] webpage is a documentation-preview walkthrough for initializing a `dataImport` Function whose JavaScript accepts an incoming payload, transforms it into transaction attributes, and returns a transaction mapping for creation of corresponding Braintree entities. It also routes local testing and environment-qualified deployment. The snapshot is not evidence of current Functions support, account eligibility, an exact CLI or package version, deployed runtime behavior, or successful payment processing.

## Key takeaways

- The page initializes `MyImportFunction` from the `dataImport` template and says the CLI creates a directory with an `index.js` file for the Function.
- Its illustrative JavaScript parses `context.payload`, builds transaction attributes and returns them under `transaction`. The displayed payload mapping is an example, not a complete schema or guarantee that the captured code is runnable; the raw contains rendering artifacts in the JavaScript and deployment snippets.
- Returned data is subject to Braintree's normal validations. The page says nonconforming data produces a `422` with errors to the calling service and logs the errors to the console. It does not define the complete validation contract or prove a particular call succeeded.
- Before deployment, the guide advises local testing with a JSON file that mirrors the expected inbound payload and `btfns test -p tests/sample.json`. This is local simulation guidance, not hosted-runtime or payment proof.
- The deployment example uses a `dataImport` configuration with an HTTP `POST` event. Deployment defaults to the sandbox account; production requires selecting the production prompt option or running `btfns deploy --production`. A command or displayed success URL is not proof of deployment, endpoint availability, entity creation, authorization, settlement or funding.

## Detail locators

- **Preview availability:** `AVAILABILITY`, lines 17–20.
- **Project initialization:** `Initialize a New Function`, lines 23–30.
- **Payload parsing and illustrative transaction mapping:** `Write Code to Ingest Data`, lines 31–70.
- **Validation failure behavior:** `Validation Errors`, lines 72–76.
- **Local JSON test flow:** `Test and Deploy Your Function` > `Testing`, lines 77–102.
- **Configuration and sandbox-versus-production deployment:** `Test and Deploy Your Function` > `Deployment`, lines 104–126.

## Related

- [[braintree]]
- [[braintree-payment-platform]] — main provider concept route for the collected Braintree Functions documentation previews.
- [[braintree-data-migration]] — contrast route for bounded gateway customer and payment-method imports/exports; that process is distinct from this Function's incoming-payload example.

## Raw Sources

- [[raw/braintree/docs/guides/functions/import-data-2026-09-16|Braintree Functions — Import Data (2026-09-16 snapshot)]]
