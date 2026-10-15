---
title: "Adyen API-interacting MCP server"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/mcp-server"
raw_files:
  - "adyen/docs/development-resources/mcp-server/2026-09-15.md"
tags: [adyen, mcp, developer-tools, api-credentials, checkout-api]
---

## Overview

This [[adyen]] guide describes a locally run Model Context Protocol (MCP) server that lets an LLM client invoke tools which make Adyen API requests. The documented API families are Checkout API and Management API, with a separate linked GitHub list for the exact supported endpoints. This is an API-interacting tool, not merely a documentation search service: the page gives refund and payment-link creation as example tasks. Execution depends on the configured API credential, its roles, environment, and endpoint support; the page does not prove any request was made or succeeded. See [[adyen-api-access]] for credential and permission context.

## Key takeaways

- The setup uses an Adyen API key to authenticate MCP-originated API requests. The page lists Merchant PAL, Checkout, and Management API roles, including terminal action and settings read/write roles, and states those roles are assigned to web service users by default. That statement is snapshot guidance, not verification of a particular credential's current permissions. The linked GitHub endpoint inventory has not been read for this source entry, so the two API-family names are not proof that every endpoint is exposed as an MCP tool.
- The server runs locally. The test command uses `--env=TEST` with an API key. The live command uses `--env=LIVE` plus `--livePrefix` from the live Customer Area API URL prefix. The raw examples pass the key through `--adyenApiKey`; they contain only a placeholder, and no credential is stored in this entry.
- A user prompt goes through the LLM client to the MCP server, which translates it into function calls and Adyen API requests. The page's refund and payment-link examples show that a configured tool can request financial or merchant operations; authorization, role scope, endpoint availability, and resulting payment state still need transaction-specific evidence.
- The page was collected on 2026-09-15 but carries a 2025-06-11 last-modified value. Treat its role list, package invocation and endpoint-family scope as versioned snapshot documentation rather than a current tool inventory or live-account entitlement.

## Detail locators

- **Purpose, tool mechanism, supported API families, exact-endpoint navigation:** raw lines 15–40, under `# Adyen Model Context Protocol (MCP) server` and `## How it works`.
- **API-key requirement and listed credential roles:** raw lines 42–58, under `## Get your API credentials`.
- **Local package invocation and test/live configuration:** raw lines 60–87, under `## Run the MCP server`, `### Test environment`, and `### Live environment`.
- **Prompt-to-client-to-server-to-API request sequence and action examples:** raw lines 89–98, under `## Use the MCP server`.

## Related

- [[adyen]]
- [[adyen-api-access]]
- [[source-adyen-docs-development-resources-api-credentials]]
- [[source-adyen-docs-development-resources-live-endpoints]]

## Raw Sources

- [[raw/adyen/docs/development-resources/mcp-server/2026-09-15|Adyen MCP server setup and API tool guide — collected 2026-09-15]]
