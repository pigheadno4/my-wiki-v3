---
title: "Metronome API Authentication"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/api-reference/authentication"
original_format: webpage
raw_files:
  - "metronome/api-reference/authentication-2026-07-13.md"
tags: [metronome, api-authentication, bearer-tokens, api-security]
---

## Overview

This Metronome API reference page describes how to create, use, scope, and archive API bearer tokens. It documents the dashboard creation flow, header and SDK configuration, invalid-token responses, Postman setup, and the permission model that starts from the creating user's permissions.

## Key takeaways

- Metronome API requests authenticate with bearer tokens, and token creation is performed in the Metronome app under Connections → API tokens & webhooks.
- The full token is displayed only during creation, so it must be copied to a secure location before the creation flow is completed.
- API calls use the `Authorization` header; the documented Python, Node.js, Ruby, and Go SDK examples default to the `METRONOME_BEARER_TOKEN` environment variable when a token is not supplied directly.
- A valid token can yield endpoint data or a 404 JSON error object when no resources are found; an invalid token yields a 401 or 403 error.
- Tokens inherit the creating user's permissions by default and can be limited by access level, environment, or endpoint; the source directs permission adjustments to a Metronome representative.

## Details

The documented app flow creates a named token through **Connections** and **API tokens & webhooks**, then requires the user to copy the token before selecting **Done**. Metronome says the token name is associated with API calls made using it, which can help track changes and requests in audit logs.

For direct API use, the page requires the `Authorization` header. Its SDK examples cover Python, Node.js, Ruby, and Go, and each shows an environment-variable default of `METRONOME_BEARER_TOKEN`. The Postman instructions import Metronome's OpenAPI specification, set collection authorization to **Bearer Token** with `{{api_token}}`, and add that variable to the Postman environment.

By default, a token retains the permissions of the user who created it. The documented scope dimensions are access level (such as read-only), environment (such as sandbox only), and endpoint (such as only `getCustomers`). The source says to contact a Metronome representative to adjust permissions.

Unused tokens can be archived with the Trash icon in the Metronome UI, and that action cannot be undone. The page recommends removing unused tokens and regularly rotating tokens that remain in use.

> [!info] Source boundary
> This source does not specify a token format, token expiry duration, a self-service procedure for changing scopes, or an API endpoint for creating, rotating, or archiving tokens. It documents UI-based creation and archiving, and directs permission adjustments to a Metronome representative.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-security-principles]]

## Raw Sources

- [[raw/metronome/api-reference/authentication-2026-07-13|2026-07-13 snapshot — Metronome API authentication]]
