# Fixed retrieval checks: Adyen MCP server

## Q1 — API interaction and endpoint boundary

**Query:** Does this Adyen MCP server only search documentation, or can it make Adyen API requests, and which endpoint scope is established by the page?

**Expected answer:** The page describes a locally run MCP server whose tools translate an LLM client's natural-language instruction into Adyen API requests. It names Checkout API and Management API as supported API families and links to a separate GitHub endpoint list for exact coverage. Its examples include requesting a refund or creating a payment link. The two family names do not prove every endpoint is exposed, and the guide itself does not prove a request was made, authorized or successful. This is an API-interacting tool rather than a documentation navigation service.

**Raw locators:** purpose and supported families, lines 15–40; prompt-to-client-to-server-to-API sequence and examples, lines 89–98. **Canonical retrieval route:** [[adyen-api-access]] → [[source-adyen-docs-development-resources-mcp-server]] → [[raw/adyen/docs/development-resources/mcp-server/2026-09-15|pinned raw]].

## Q2 — Credential, role and environment conditions

**Query:** What API credential and environment configuration does the dated MCP guide describe, and does its role list establish a merchant's live entitlement?

**Expected answer:** The setup generates an Adyen API key for MCP-originated requests and lists Merchant PAL, Checkout and Management API roles, including terminal settings and actions. It says the listed roles are assigned to web service users by default, but that dated statement does not verify a particular credential's current permissions. The server runs locally; its test command uses `--env=TEST` and an API key, while live uses `--env=LIVE`, the API key and `--livePrefix` from live Customer Area. The 2026-09-15 snapshot has a 2025-06-11 last-modified value; current package behavior, endpoint access, role scope and transaction outcomes need separate evidence.

**Raw locators:** metadata, line 11; credential and roles, lines 42–58; local test/live setup, lines 60–87. **Canonical retrieval route:** [[adyen-api-access]] → [[source-adyen-docs-development-resources-mcp-server]] → [[raw/adyen/docs/development-resources/mcp-server/2026-09-15|pinned raw]].
