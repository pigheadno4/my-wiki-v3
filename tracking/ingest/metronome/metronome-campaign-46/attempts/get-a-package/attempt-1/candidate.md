---
title: "Metronome API: Get a Package"
type: source
date_ingested: 2026-09-13
canonical_url: "https://docs.metronome.com/api-reference/packages/get-a-package"
original_format: webpage
raw_files:
  - "metronome/api-reference/packages/get-a-package-2026-08-28.md"
tags: [metronome, api-reference, packages, aliases, contracts]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/packages/get` (`getPackage-v1`) for retrieving one package by its UUID. It is the direct route for inspecting a package's identifying details, alias schedule, duration, and reusable contract terms rather than enumerating package definitions.

## Retrieval boundary and qualifications

- Within the JSON payload schema, `package_id` is the required UUID selector. The enclosing OpenAPI `requestBody` is not marked `required: true`, so the page does not establish omitted-body runtime behavior.
- HTTP `200` requires top-level `data`, which references `components.schemas.Package`; the operation also documents a `404` route for a resource that was not found.
- `Package` is the entry point for returned detail. Alias schedules and duration are optional properties there, and the success example omits both; do not infer that every returned package has either value. Package terms remain discoverable through the referenced commit, credit, override, scheduled-charge, recurring, threshold, spend-tracker, and subscription schemas without copying those inventories here.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths./v1/packages/get.post` for the method, path, purpose, and operation ID.
- **Package selector:** `paths./v1/packages/get.post.requestBody.content.application/json.schema` documents the required `package_id` UUID property.
- **Success and not-found responses:** `paths./v1/packages/get.post.responses.200` documents the `data` envelope and example; `responses.404`, `components.responses.NotFound`, and `components.schemas.Error` document the not-found route.
- **Returned package detail:** `components.schemas.Package` is the response object entry point. Follow `PackageAlias` for alias names and effective timestamps, `RelativeDate` for duration value and unit, and the referenced template/configuration schemas for package terms. `Package.archived_at` is the raw locator for archive-state timestamp data when present.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-packages-and-aliases]]

## Raw Sources

- [[raw/metronome/api-reference/packages/get-a-package-2026-08-28|2026-08-28 snapshot - single-package retrieval, selector, response envelope, and package-detail schema routes]]
