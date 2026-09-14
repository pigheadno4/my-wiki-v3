---
title: "Metronome API: Archive a Package"
type: source
date_ingested: 2026-09-11
canonical_url: "https://docs.metronome.com/api-reference/packages/archive-a-package"
original_format: webpage
raw_files:
  - "metronome/api-reference/packages/archive-a-package-2026-07-13.md"
tags: [metronome, api, packages, contracts, archival]
---

## Overview

Bearer-authenticated `POST /v1/packages/archive` archives a package identified by UUID. It is the package-lifecycle operation for preventing that package from being used for new contracts; it does not end contracts already associated with the package.

## Key takeaways

- An archived package cannot be used to create new contracts, while existing associated contracts continue to function normally.
- The archived package remains retrievable through the UI and API, but it cannot be unarchived. Treat archival as irreversible.
- Within the JSON payload schema, `package_id` is the required UUID target and additional properties are disallowed. The enclosing `requestBody` is not itself marked required, so the raw does not establish omitted-body runtime behavior.

## Raw-detail coverage map

| Detail | Exact raw locator |
| --- | --- |
| Operation and lifecycle effects | `## OpenAPI` -> `paths./v1/packages/archive.post`, especially `description` |
| Package target identification | `## OpenAPI` -> `paths./v1/packages/archive.post.requestBody.content.application/json.schema.properties.package_id` |
| Success response | `## OpenAPI` -> `paths./v1/packages/archive.post.responses.200` and `components.schemas.Id` |

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-packages-and-aliases]]

## Raw Sources

- [[raw/metronome/api-reference/packages/archive-a-package-2026-07-13|2026-07-13 snapshot - complete package archival POST operation and schema]]
