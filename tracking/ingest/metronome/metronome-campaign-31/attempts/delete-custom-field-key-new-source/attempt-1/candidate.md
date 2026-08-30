---
title: "Metronome Delete a Custom Field Key"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/api-reference/custom-fields/delete-a-custom-field-key"
original_format: webpage
raw_files:
  - "metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md"
tags: [metronome, api-reference, custom-fields, lifecycle, idempotency]
---

## Overview

This API reference documents the bearer-authenticated production `POST /v1/customFields/removeKey` mutation. It removes one key from the custom-field allowlist for one managed entity type, blocking future use across that entity type and making existing values inaccessible; it does not establish physical data erasure.

## Query-critical facts

- The operation identifies the allowlist entry by `entity` plus `key`. If a JSON payload is supplied, its object schema requires both properties; `key` is a string and `entity` references `ManagedEntity`. The enclosing `requestBody` itself is not marked required, and the request object has no explicit `additionalProperties` policy, so omitted-body and unknown-field behavior are not established.
- `ManagedEntity` is a string enum covering `alert`, `billable_metric`, `charge`, `commit`, `contract_credit`, `contract_product`, `contract`, `customer`, `discount`, `invoice`, `professional_service`, `product`, `rate_card`, `scheduled_charge`, `subscription`, `package_commit`, `package_credit`, `package_subscription`, and `package_scheduled_charge`. The `professional_service` enum member carries client-specific `x-mint-enum` metadata whose availability meaning is not explained.
- Removal is scoped to the selected entity type and applies across all its instances: the key cannot be used in the future, and values already set under it become inaccessible. The page does not say those values are physically erased, whether they remain in storage or exports, or whether re-adding the key restores access.
- The operation documents only HTTP `200` with description `Success`; it supplies no response-body schema, returned deletion record, affected-instance count, or explicit error response. A successful response therefore does not expose which historical values became inaccessible or prove propagation to every read, export, invoice, or integration surface.
- The separate API-wide authority applies `Idempotency-Key` to all POST endpoints: identical same-key parameters replay the original result, changed parameters conflict, keys persist for at least 24 hours, and cached results can include HTTP `500`. This endpoint adds no remove-key-specific behavior for an already absent key, another or expired key, concurrent removal or re-creation, read-after-write visibility, or recovery after cached or ambiguous failure.

## Material boundaries and contradictions

> [!warning] Delete label versus documented lifecycle effect
> The title and summary call this operation a delete, while its description and request text define removal from an allowlist. The durable documented effects are prevention of future use and inaccessibility of existing values; the page does not establish irreversible value deletion, retention duration, or restoration behavior.

The endpoint does not define authorization beyond bearer authentication, environment-to-environment scope, atomicity across entity instances, propagation timing, audit history, effects on finalized historical artifacts, partial failure, or ordering against value writes and key creation. The API-wide request-result replay contract must not be treated as fresh proof that allowlist state or downstream visibility has converged.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation identity and authority | Production server, bearer security, `POST /v1/customFields/removeKey`, Custom fields tag, summary, and `disableCustomFieldKey-v1` operation ID |
| Request identity and requiredness | Enclosing request-body description, JSON object schema, payload-required `entity` and `key`, string key type, and customer-key example |
| Managed-entity applicability | Complete 19-value `ManagedEntity` enum and the unexplained client-specific metadata attached to `professional_service` |
| Lifecycle and propagation | Selected-entity allowlist removal, future-use prevention across all instances, existing-value inaccessibility, and undocumented erasure, restoration, timing, and downstream visibility |
| Result, failure, and retry | Sole HTTP `200` description, absent response/error schemas, separate API-wide POST idempotency authority, and endpoint-local concurrency and recovery unknowns |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-custom-fields]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13|2026-07-13 snapshot - remove-key identity, managed-entity scope, lifecycle effect, request schema, and success boundary]]
