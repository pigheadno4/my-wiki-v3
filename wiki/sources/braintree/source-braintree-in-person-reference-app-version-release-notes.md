---
title: "Braintree In-Person Payment Application Version Release Notes"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/reference/app-version-release-notes"
raw_files:
  - "braintree/in-person/reference/app-version-release-notes-2026-09-16.md"
tags: [braintree, in-person, payment-application, firmware, card-readers, release-notes]
---

## Overview

This collected Braintree website page is a release-note inventory for sandbox and production versions of the Braintree Payment Application used on card readers. The snapshot lists versions 1.2.2 through 6.0.1 and records reader- or version-qualified features, fixes, behavior changes, prerequisites and known issues. It is historical release documentation: it does not establish the version currently deployed to a merchant's readers, the latest version available after collection, reader eligibility, or successful payment execution. [[braintree]] [[braintree-payment-platform]]

## Key takeaways

- The page-level notice captured on 2026-09-16 warned that the application's SSL certificates were set to expire on January 1, 2026, named 6.0.1 as the minimum required upgrade, and said reader interactions would fail after that date without the upgrade. This is a dated warning, not evidence of a reader's installed version or present certificate state.
- The page says production releases occur four weeks after sandbox availability. Version 5.1.0 is separately labeled sandbox-only for testing and integration, with 5.2.0 identified as the production release for those features; do not treat a sandbox entry as production availability.
- Consequential version-specific changes include disabling the magstripe interface for all offline transactions in 5.2.2 and blocking firmware updates while offline transactions remain cached in reader memory in 5.1.0. These statements are scoped to the named release entries and payment-application context.
- The 5.0.0 entry requires readers to reach 4.0.0 first. The 4.0.0 entry describes an operating-system upgrade, warns against unplugging power, gives a duration of up to 20 minutes, and makes 4.0.0 a prerequisite for newer reader-application versions.
- The 3.1.0 entry records an older certificate-related statement that readers on 3.0.0 or earlier could no longer update and might require replacement, while saying they would continue to work in sandbox and production. Keep that older release statement distinct from the later page-level January 2026 certificate warning; the snapshot does not establish current device support.

## Detail locators

### Release context and notices

- Document purpose and environment scope: raw lines 14-16.
- Page-level SSL-certificate warning and minimum 6.0.1 statement: raw lines 19-22.
- Sandbox-to-production timing statement: raw lines 26-27.

### Version inventory

- `Version 6.0.1 - Released on 2025-05-07`: raw heading line 30; SSL certificate and V400m Ethernet-base items at lines 33-46.
- `Version 5.5.0 - Released on 2024-09-12`: raw heading line 51; V400m, receipt-printing, partial-authorization, payment-initiator, offline and beta RMS items at lines 54-91.
- `Version 5.4.0 - Released on 2024-04-11`: raw heading line 96; multiple-choice prompt and offline `cardholderName` format change at lines 98-115.
- `Version 5.3.0 - Released on 2024-01-04`: raw heading line 120; UI, offline-data, reader-network and privacy-statement items at lines 123-160.
- `Version 5.2.2 - Released on 2023-08-30`: raw heading line 165; offline magstripe behavior change at lines 168-171.
- `Version 5.2.0 - Released on 2023-06-27`: raw heading line 176; prompt, non-PCI card-data, display-field and text-position changes at lines 179-213.
- `Version 5.1.0 - Released on 2023-06-16`: raw heading line 218; sandbox-only qualification, authorization and SAF additions, firmware-update block and sandbox known issue at lines 220-264.
- `Version 5.0.0 - Released on 2023-01-13`: raw heading line 269; 4.0.0 prerequisite, SAF and reader-admin changes at lines 271-298.
- `Version 4.0.0 - Released on 2022-09-01`: raw heading line 303; M400 availability, operating-system upgrade and power/duration warnings, upgrade prerequisite, reader and prompt changes at lines 305-349.
- `Version 3.3.0 - Released on 2022-07-08`: raw heading line 354; custom-prompt additions and SAF, admin-menu and E285 fixes at lines 357-386.
- `Version 3.2.0 - Released on 2022-03-30`: raw heading line 391; Store and Forward idempotency, battery/card/network validation and fixes at lines 394-420.
- `Version 3.1.0 - Released on 2021-11-18`: raw heading line 425; older-version certificate/update qualification, configurable update, QRC and Store-and-Forward changes at lines 427-454.
- `Version 2.0.0 - Released on 2021-10-01`: raw heading line 459; status-bar, security/stability and P2PE items at lines 462-471.
- `Version 1.2.2 - Released on 2021-08-05`: raw heading line 476; configuration-qualified offline charging and pairing/network fixes at lines 479-502.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/in-person/reference/app-version-release-notes-2026-09-16|Braintree In-Person payment application version release notes (2026-09-16 snapshot)]]
