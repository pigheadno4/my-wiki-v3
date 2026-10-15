# Fixed retrieval checks: Adyen documentation and knowledge tools

## Q1 — Discovery and page-content routes

**Query:** How does this Adyen page describe finding documentation and obtaining machine-readable page content?

**Expected answer:** The root `/llms.txt` groups documentation pages by product category for LLM discovery, while `/sitemap` is a general page list usable for scraping, search indexing and content discovery. Most documentation pages can be rendered as plain Markdown by appending `.md`; the webhooks URL is only an example of that pattern. A compressed ZIP mirror is described as containing documentation pages in Markdown for offline access and bulk AI context. These routes are documentation access, not evidence of endpoint behavior or current contents without reading the target.

**Raw locators:** discovery sections, lines 21–39; Markdown pages, lines 54–68; ZIP mirror, lines 70–80. **Canonical retrieval route:** [[source-adyen-docs-development-resources-documentation-tools]] → [[raw/adyen/docs/development-resources/documentation-tools/2026-09-15|pinned raw]].

## Q2 — OpenAPI, MCP and update boundaries

**Query:** What does the page say the Adyen OpenAPI repository can be used for, and what can be inferred from its MCP and release-note links?

**Expected answer:** Adyen describes its OpenAPI repository as holding specifications for public APIs with machine-readable endpoint parameters, request and response bodies, and headers. It names client generation, Postman collections and LLM context as uses. Its Adyen MCP reference is a link to another guide; this page does not define MCP tools, permissions or live operation. Release notes and RSS feeds are routes for following product/API changes, including a plugin-feed example. This 2026-09-15 snapshot does not establish later releases, current feed availability, credentials, authorization or payment execution. Version-specific SDK behavior belongs to an exact downstream release.

**Raw locators:** OpenAPI repository and MCP link, lines 43–52; release notes and RSS routes, lines 82–100. **Canonical retrieval route:** [[adyen-sdk-automation]] → [[source-adyen-docs-development-resources-documentation-tools]] → [[raw/adyen/docs/development-resources/documentation-tools/2026-09-15|pinned raw]].
