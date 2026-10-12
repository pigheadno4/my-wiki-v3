---
title: "Adyen Docs: Disputes API reference"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/disputes-api/disputes-api-reference"
raw_files:
  - "adyen/docs/risk-management/disputes-api/disputes-api-reference/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, api-reference]
---

## Overview

This Adyen Disputes API reference supplements [[adyen-risk-management]] with request-error messages and scheme-specific defense reason and document type codes. The Defend Disputes API is described as a way to retrieve applicable defense reasons, supply or delete defense documents, and accept or defend disputes. This is a 2026-09-15 documentation snapshot, not proof that a specific dispute is defendable or that an API operation succeeded.

## Key takeaways

- Before using the API, the page calls for an online-payments integration, an API credential with API key and **API dispute management** role, and a Standard webhook subscription with dispute events enabled. It also directs readers to scheme/payment-method chargeback guidelines and scenarios that Adyen handles automatically. Not all dispute types can be defended. See **Requirements**.
- A failed Disputes API request is described as returning `success: false` and an `errorMessage`. The **Possible errors** table maps messages to accept, defend, supply-document, or delete-document requests, including expiration, an ended defense period, a dispute already defended, and document validation or deletion failures. Do not infer a completed defense from request submission alone.
- For a specific dispute, `/retrieveApplicableDefenseReasons` returns applicable scheme defense reason codes and associated defense document type codes, including whether requirements are satisfied and whether documents are required or available. The JSON block is an example response, not a universal set of reasons or requirements. See **Retrieving defense reasons and documents**.
- When defending a dispute, only document type codes returned for the chosen defense reason may be used. `AlternativeDefenseMaterial` is a generalized document type only after Adyen Support enables it; its listing in the table alone does not establish availability for an account. See **Defense document type codes**.

## Detail locators

- **Requirements** — credential role, webhook setup, non-defendable disputes, scheme guidance, and automatic handling.
- **Possible errors** — operation-specific `errorMessage` matrix; error strings are not a complete dispute-state model.
- **Retrieving defense reasons and documents** — `/retrieveApplicableDefenseReasons` response fields and illustrative JSON.
- **Defense reason codes** — snapshot table of codes, descriptions, and applicable schemes.
- **Defense document type codes** — snapshot table of document codes and schemes, returned-code restriction, and support-enabled generalized document option.
- **See also** — overview, dispute notifications, defense requirements, and broader dispute guidance.

## Related

- [[adyen]]
- [[adyen-risk-management]]
- [[disputes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/disputes-api/disputes-api-reference/2026-09-15|Adyen Docs — Disputes API reference (2026-09-15)]]
