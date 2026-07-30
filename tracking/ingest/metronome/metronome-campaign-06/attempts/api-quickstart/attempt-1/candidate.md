---
title: "Metronome API Quickstart"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/api-quickstart"
raw_files:
  - "metronome/api-reference/api-quickstart-2026-07-13.md"
tags: [metronome, api, api-authentication, developer-sdks, onboarding]
---

## Overview

This quickstart gives the first-connection path for Metronome's API: create and securely save a token, install and configure one of four SDKs, then list account customers to confirm connectivity. It is an SDK onboarding page, not a complete authentication, SDK-behavior, or endpoint reference.

## Key takeaways

- Create a named token in the Metronome App through **Connections → API tokens & webhooks → Add**, and save it securely before selecting **Done**.
- The documented SDK installation paths are Python (`pip install --pre metronome-sdk`), Node.js (`npm install @metronome/sdk`), Ruby (`gem install metronome-sdk`), and Go (`go get -u 'github.com/Metronome-Industries/metronome-go'`).
- The configuration examples accept a supplied credential and otherwise use `METRONOME_BEARER_TOKEN`; the source labels the credential an "API key" in prose while the example fields and comments call it a bearer token.
- Connectivity is checked by listing customers. The page says that call works with an empty customer list; after connection it points readers toward usage tracking, pricing, and invoicing.

## Onboarding sequence

1. Log into the Metronome App, open **Connections → API tokens & webhooks → Add**, create a descriptively named token, and copy it to a secure location before clicking **Done**.
2. Install the Python, Node.js, Ruby, or Go SDK using the package command documented for that language.
3. Configure the SDK with a supplied bearer-token value or let the language client use the `METRONOME_BEARER_TOKEN` environment variable by default. The constructor/property names differ by language: Python `bearer_token`, Node.js `bearerToken`, Ruby `bearer_token`, and Go `option.WithBearerToken(...)`.
4. List customers to test the connection: Python, Node.js, and Ruby call the customers list method and handle an empty `data` collection; the Go example calls `client.V1.Customers.List(...)`, returns its error if present, and checks `resp.Data`.

## Warnings, boundaries, and unknowns

> [!warning] Credential handling
> The source says to copy the newly created token to a secure location before clicking **Done**. It does not state a recovery, rotation, expiry, scope, or revocation policy on this page.

The setup prose calls the supplied value an "API key", while the SDK code/configuration uses bearer-token terminology. The quickstart does not define whether those labels carry a distinct meaning, so implementations should not infer one from this page.

This page specifies no numeric API or SDK limits, supported SDK versions, retry policy, direct HTTP request format, authorization-header syntax, or general error-handling contract. Apart from the Go listing example's returned error, it provides no endpoint-specific error behavior. It links to separate authentication and SDK documentation for deeper detail.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-security-principles]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-api-reference-authentication]], [[source-metronome-guides-get-started-developer-sdks]]

## Raw Sources

- [[raw/metronome/api-reference/api-quickstart-2026-07-13|2026-07-13 snapshot — API token, SDK setup, and connectivity check]]
