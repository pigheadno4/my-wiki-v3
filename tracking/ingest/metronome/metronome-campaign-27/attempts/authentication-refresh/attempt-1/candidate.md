---
title: "Metronome API Authentication"
type: source
date_ingested: 2026-08-29
canonical_url: "https://docs.metronome.com/api-reference/authentication"
original_format: webpage
raw_files:
  - "metronome/api-reference/authentication-2026-08-28.md"
  - "metronome/api-reference/authentication-2026-07-13.md"
tags: [metronome, api-authentication, bearer-tokens, api-security]
---

## Overview

This API overview documents Metronome customer bearer-token creation, request authentication, SDK and Postman configuration, permission scoping, and irreversible archival. It is an operational credential guide rather than a complete token-lifecycle, authorization-policy, or error contract.

## Query-critical facts

- Metronome API requests use bearer tokens. The current app flow creates a descriptively named token under **Developer** → **API tokens** → **+ Add**; the full token must be copied to secure storage before completing the flow because it cannot be viewed again.
- Metronome says a token's name is associated with API calls made using it, which can help attribute changes and requests in audit logs.
- Direct calls provide the token through the `Authorization` header. The Python, Node.js, Ruby, and Go examples accept a token explicitly and document `METRONOME_BEARER_TOKEN` as the default environment-variable source when it is omitted.
- On this page, a valid token can yield endpoint data or a `404` JSON error when no resource is found; an invalid token yields `401` or `403`. These statements do not replace endpoint-specific success and error contracts.
- Tokens inherit the creating user's permissions by default. Metronome documents restriction by access level, environment, or endpoint and directs permission adjustments to its support portal.
- Tokens that are no longer used can be archived with the Trash control in the Metronome UI; the page says archival cannot be undone and recommends removing unused tokens and rotating active ones regularly.

## Material boundaries

- This page does not specify token format, expiry, automatic rotation, recovery after loss, rotation overlap, a self-service scope-change flow, or API endpoints for token creation, permission changes, or archival. It documents app-based creation and archival and a support-mediated permission route.
- Environment is a documented scope dimension, but this page does not define environment selection for API base URLs or establish that a token is valid in any particular environment unless its actual scope is known.
- The separate security-principles authority's 12-hour credential lifetime applies to credentials minted by Metronome engineers. This authentication page states no lifetime for customer-created bearer tokens, so the two credential classes must not be assigned the same lifecycle.

## Raw-detail coverage map

Use the complete raw page for the exact **Developer** and **API tokens** creation steps; the one-time token-display warning; token naming and audit-log association; Python, Node.js, Ruby, and Go initialization examples; page-local `404`, `401`, and `403` statements; OpenAPI import and Postman bearer-variable setup; permission-scope examples and support route; and the irreversible archival control and rotation guidance. Dedicated endpoint references remain authoritative for each operation's complete success and error behavior, and dedicated security and RBAC sources remain authoritative for broader credential and authorization policy.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-security-principles]]
- Related sources: [[source-metronome-guides-platform-configuration-security-principles]], [[source-metronome-guides-platform-configuration-role-based-access-rbac]], [[source-metronome-guides-platform-configuration-audit-logs]], [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-api-reference-api-quickstart]]

## Raw Sources

- [[raw/metronome/api-reference/authentication-2026-08-28|2026-08-28 snapshot - bearer-token creation, use, permissions, errors, Postman setup, and archival]]
- [[raw/metronome/api-reference/authentication-2026-07-13|2026-07-13 snapshot - prior immutable API-authentication reference]]
