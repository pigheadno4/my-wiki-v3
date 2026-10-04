---
title: "Braintree Forward API Functions Reference"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/forward-api/functions"
raw_files:
  - "braintree/docs/reference/forward-api/functions-2026-09-16.md"
tags: [braintree, forward-api, functions, transformations, dsl, cryptography]
---

## Overview

This collected, unversioned Braintree reference identifies functions as part of the [[braintree-forward-api|Forward API]] domain-specific language used by transformations and says that DSL is intentionally minimal. It directs readers to contact Braintree when a needed function is unavailable. The captured page is sparse: despite its title and an empty Parameters heading, it does not enumerate function names, signatures, parameter or input schemas, outputs, errors, invocation modalities, or lifecycle/deprecation behavior. It is therefore a route to the fully read raw snapshot, not a complete callable-function catalog or evidence of runtime behavior. See [[braintree]].

This is Forward API transformation-language reference material, not [[braintree-orchestration]] processor-connection or transaction-lifecycle documentation. Nothing in this snapshot establishes destination acceptance, payment authorization, capture, settlement, funding, or any other successful execution.

## Key takeaways

- Production Forward API use is subject to eligibility. The page directs readers to an Account Manager or the Business Development inquiry route; this snapshot does not establish present availability, merchant approval, production enablement, or account readiness.
- The page describes the Forward API transformation DSL as intentionally minimal and supplies a contact route for requests for a new function. It does not name or define any function in the captured content, so no operation, signature, input, output, error, or runtime guarantee should be inferred.
- The Parameters section is empty in this capture. Routine function details cannot be reconstructed from the page title, linked navigation, or the embedded example.
- The remainder of the capture is labeled "Example RSA keypair" and includes public- and private-key-shaped text. Treat it only as published example material: do not copy, deploy, or reuse it as a credential, and do not infer any security property, environment support, or cryptographic lifecycle from its presence.

> [!warning] Sparse reference capture
> This snapshot does not contain the expected function/signature/error inventory. Consult separately verified authority before implementing a transformation function, and preserve the production-eligibility gate.

> [!warning] Example key material
> The raw includes an example RSA private-key block. Do not reuse it as secret or production key material. Its publication here does not prove that it is valid, safe, supported, or connected to any Braintree environment.

## Detail locators

- Production eligibility gate and contact routes: `# Functions > AVAILABILITY`, raw lines 17-20.
- Minimal Forward API DSL identity and new-function inquiry route: `# Functions`, raw line 22.
- Empty Parameters heading, with no captured function inventory beneath it: `# Functions > Parameters`, raw lines 25-29.
- Published example RSA public/private-key-shaped material: `# Example RSA keypair`, raw lines 30-66.

No function names, callable signatures, parameter tables, return values, error inventory, environment-specific execution semantics, deprecation dates, or lifecycle states are present elsewhere in the fully read raw.

## Related

- [[braintree]] - provider company and source catalog
- [[braintree-forward-api]] - main request-construction, transformation and security retrieval hub
- [[braintree-orchestration]] - separate processor-connection and transaction-lifecycle retrieval hub

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for the Forward API overview; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16|Braintree Forward API transformations guide]] - linked navigation-only route for the DSL context; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/forward-api/functions-2026-09-16|Braintree Forward API functions reference]] - complete collected snapshot for production eligibility, minimal-DSL identity, the absent function inventory and the embedded example RSA keypair
