---
title: "Adyen Classic CSE library public key, location and token"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption/cse-library-public-key-location-and-token"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/cse-library-public-key-location-and-token/2026-09-15.md"
tags: [adyen, classic-api, client-side-encryption, cse, public-key, api-credentials]
---

## Overview

This Classic CSE subguide tells a merchant where to **generate and retrieve** the CSE library's Public Key, Library location and Library token in Customer Area. It labels **CSE Web** integrations as being phased out, no longer developed or accepted as new CSE integrations, and points website builds to newer Web integrations; it expressly says mobile integrations are unaffected by that Web phaseout. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption]].

## Key takeaways

- The documented navigation starts with a **company-account** Customer Area login, then **Developers > API credentials**. The user adds a credential if needed or selects an existing web-service user, opens its **Client-Side Encryption** panel, selects **Generate**, and copies the three named values for use in its system.
- The **Public Key**, **Library location** and **Library token** are distinct named outputs of the CSE panel. The location identifies where to retrieve the CSE library; the public key is for the client-side encryption setup described by the parent guide. This page does not define the library token's request protocol, secrecy or rotation semantics, nor say it is interchangeable with a server API key or Basic-authentication secret. Do not infer a specific Customer Area user role from this page.
- The guide warns that all three values change when the account switches from **test to live**. A test value is therefore not proof of a live CSE configuration, library load, encrypted request or accepted payment.
- This page is a credential-location procedure, not a PCI validation document or security guarantee. The parent CSE guide and [[adyen-pci-dss-compliance]] retain the merchant-served form, SRI, SAQ A eligibility and additional-controls boundaries. The Web phaseout does not establish behavior of any mobile CSE implementation.

## Detail locators

- Lines 16–24: CSE Web phaseout, newer Web route and mobile exception.
- Lines 26–35: three required named values and company-account/credential navigation.
- Lines 37–43: Generate action, copied values and test-to-live change warning.

## Related

- [[adyen-online-payments]] — provider concept and reciprocal Classic source route.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption]] — parent CSE flow, library loading, SRI and server `/authorise`.
- [[adyen-api-access]] — server API credential identity and role boundaries; separate from this page's CSE panel values.
- [[adyen-pci-dss-compliance]] — merchant PCI and SAQ qualifications.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/client-side-encryption/cse-library-public-key-location-and-token/2026-09-15|CSE library values, captured 2026-09-15]]
