---
title: "List all packages"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/list-all-packages"
raw_files:
  - "metronome/api-reference/list-all-packages-2026-08-28.md"
tags: [metronome, api-reference, packages, aliases, pagination]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/packages/list`, which enumerates reusable package definitions and returns their package details. For contracts associated with one package, the page explicitly routes readers to the separate `listContractsOnPackage` endpoint.

## Query-critical behavior and warning

- Package selection uses the optional JSON `archive_filter`; pagination uses the `limit` and `next_page` query parameters. The operation description says `limit` defaults to 10, while the reusable parameter schemas contain the exact accepted bounds and cursor shape.
- HTTP `200` requires top-level `data` and `next_page`. `data` is an array of `Package` objects, and `next_page` is a nullable string cursor.

> [!warning] Archived packages are excluded by default
> Although the operation is titled "List all packages," `archive_filter` defaults to `NOT_ARCHIVED`. Use the raw request schema to select archived packages or both archive states explicitly.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/packages/list` -> `post`.
- **Selection and pagination:** `paths./v1/packages/list.post.parameters` references `components.parameters.PageLimit` and `components.parameters.NextPage`; `paths./v1/packages/list.post.requestBody.content.application/json.schema.properties.archive_filter` documents archive selection. The enclosing `requestBody` is not marked required, so this page does not establish omitted-body runtime behavior.
- **Response envelope:** `paths./v1/packages/list.post.responses.200.content.application/json.schema` documents the required `data` array and nullable sibling `next_page`.
- **Returned package detail:** `components.schemas.Package` is the package object entry point. Its references route alias schedules to `PackageAlias`, duration to `RelativeDate`, and package terms to the referenced commit, credit, override, scheduled-charge, recurring, threshold, spend-tracker, and subscription schemas.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-packages-and-aliases]]

## Raw Sources

- [[raw/metronome/api-reference/list-all-packages-2026-08-28|2026-08-28 snapshot - package-definition listing, archive selection, pagination, and returned package schema routes]]
