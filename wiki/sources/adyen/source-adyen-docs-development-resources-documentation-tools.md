---
title: "Adyen Documentation and Knowledge Tools"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/documentation-tools"
raw_files:
  - "adyen/docs/development-resources/documentation-tools/2026-09-15.md"
tags: [adyen, documentation, openapi, llms-txt, developer-tools]
---

## Overview

This [[adyen]] documentation guide identifies ways for developers and AI tools to discover Adyen documentation, access machine-readable copies, and follow product and API updates. It is a documentation-access map, not an API operation or an integration runtime contract. Its OpenAPI route is relevant to [[adyen-sdk-automation]], which separately documents Adyen's retained OpenAPI-to-SDK generation repository.

## Key takeaways

- **Discover:** the documentation site's root `/llms.txt` lists pages grouped by product category for LLM discovery; the general-purpose `/sitemap` lists documentation pages for scraping, search indexing and content discovery. These are indexes to pages, not evidence that an indexed page is currently correct or applicable to an account.
- **Access API descriptions:** the Adyen OpenAPI repository is described here as containing specifications for public Adyen APIs, including machine-readable endpoint parameters, bodies and headers; the page gives client generation, Postman collections and LLM context as possible uses. Its mention of pairing specifications with Adyen MCP is a link to another guide, not a description of MCP tools, permissions or live behavior. Use a specific API/version schema and its own evidence for implementation claims.
- **Access page content:** most documentation pages can be fetched as plain Markdown by appending `.md` to the URL. A separate compressed ZIP mirror is described as containing the full documentation set in Markdown for offline use and bulk AI context, reducing repeated network fetches. The webhooks URLs are examples of the suffix pattern, not webhook behavior evidence.
- **Follow updates:** the page routes readers to product-area release notes and RSS feeds, including a plugin release-notes feed example. The source snapshot does not establish later release changes, current ZIP content, or current feed availability; inspect the specific release notes or feed when making a version decision.
- The page does not describe API Explorer operation, endpoint credentials, an MCP server's tool surface, API authorization, or payment execution. Its links are navigation until their targets are read.

## Detail locators

- Purpose and developer/AI-tool scope: raw lines 15–19.
- `/llms.txt` product grouping and `/sitemap` discovery purposes: `## Discover documentation`, raw lines 21–39.
- OpenAPI specification repository, listed uses and MCP link: `### OpenAPI Specification`, raw lines 43–52.
- `.md` suffix, webhooks example, and plain-text use cases: `### Markdown pages`, raw lines 54–68.
- ZIP mirror content, offline/bulk-use reasons and download route: `### Full documentation mirror`, raw lines 70–80.
- Release notes and RSS update routes: `## Get updates`, raw lines 82–100.

## Related

- [[adyen]] — provider documentation context.
- [[adyen-sdk-automation]] — separately retained OpenAPI-to-SDK generation evidence.
- [[source-adyen-docs-development-resources-versioning]] — API and library versioning route.

## Raw Sources

- [[raw/adyen/docs/development-resources/documentation-tools/2026-09-15|Adyen documentation and knowledge tools — collected 2026-09-15]]
