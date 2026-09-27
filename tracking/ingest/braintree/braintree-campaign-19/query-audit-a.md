# Braintree C19 fixed retrieval audit — Group A

**Overall verdict: PASS (4/4).** No repair is required.

## Pinned evidence and actual routes

- **Getting Started Overview — PASS:** `wiki/index.md:5-11` → `wiki/braintree-index.md:206-208` → `wiki/concepts/braintree-payment-platform.md:8-18,24-27` → `wiki/sources/braintree/source-braintree-get-started-overview.md:1-54` → `raw/braintree/articles/get-started/overview-2026-09-16.md:1-94`. SHA-256 `634b57bc644633b3043b77c0a11dd65cf3120cadcaa8b787204f74b9a6908b16` matches `manifest.json`; manifest, source frontmatter, and raw line 1 agree on the canonical URL.
- **Explore — PASS:** `wiki/index.md:5-11` → `wiki/braintree-index.md:206-208` → `wiki/concepts/braintree-payment-platform.md:24-27` → `wiki/sources/braintree/source-braintree-get-started-explore.md:1-57` → `raw/braintree/articles/get-started/explore-2026-09-16.md:1-57`. SHA-256 `d10da9d7374843d2aaa960989cc180858dc3dad849aee6ec3812faa0d5526ab1` matches `manifest.json`; manifest, source frontmatter, and raw line 1 agree on the canonical URL.

## Fixed questions

1. **Where is the Braintree getting-started overview? — PASS.** Object/action match: the requested object is the Braintree Getting Started Overview and the action is to locate it; the route reaches that exact canonical page, not a product-specific guide. Direct answer: use `wiki/sources/braintree/source-braintree-get-started-overview.md`, whose pinned evidence is `raw/braintree/articles/get-started/overview-2026-09-16.md`. Exact raw locator: canonical URL at line 1; `# Overview` and page purpose at lines 14-16.

2. **Which topics does this page itself explain, and which does it only route to other pages? — PASS.** Object/action match: the exact overview page is being classified by self-contained explanation versus outbound navigation. Direct answer: the page itself explains its high-level acceptance/security orientation; the roles of a business bank account, merchant account, payment gateway, and developer work; the purposes and collected availability statements for Braintree Direct, Extend, and Auth; the Control Panel/API interaction split; and the no-developer partner-application alternative. It only routes outward for the product pages, PCI detail, Sales details for gateway-only integration, the Braintree Auth guide, dedicated Control Panel behavior, complete developer integration documentation, and named third-party integrations; those links do not prove the destinations' detailed behavior. Exact raw locators: purpose lines 14-16; required roles lines 19-41; product orientations lines 44-67; Control Panel/API split lines 70-88; alternative-integration route lines 91-93.

3. **Where is the Braintree explore guide? — PASS.** Object/action match: the requested object is the Braintree Explore guide and the action is to locate it; the route reaches the exact Explore canonical page. Direct answer: use `wiki/sources/braintree/source-braintree-get-started-explore.md`, whose pinned evidence is `raw/braintree/articles/get-started/explore-2026-09-16.md`. Exact raw locator: canonical URL at line 1; `# Explore Braintree` and its navigation purpose at lines 14-16.

4. **Which topics does it explain directly versus merely link to? — PASS.** Object/action match: the exact Explore page is being classified by its own statements versus linked-guide behavior. Direct answer: the page directly gives only brief orientations for eight routes: fraud tools (AVS/CVV and device-data framing), PCI compliance (reduced storage burden but all merchants remain responsible), Control Panel tasks, monthly recurring billing, chargebacks/retrievals, PayPal, reporting, and risk/security. Each heading is an outbound link to a dedicated article; the Explore page does not itself establish those articles' setup, complete scope, eligibility, procedures, reporting semantics, risk decisions, or current support. Exact raw locators: page boundary lines 14-16; fraud lines 19-21; PCI lines 24-26; Control Panel, recurring billing, and chargebacks/retrievals lines 29-41; PayPal, reporting, and risk/security lines 44-56.

## Shared bounded sweep and reciprocal links

- Filename and embedded-canonical-URL sweeps found exactly one collected raw for each requested page; no historical duplicate or unlinked same-canonical raw required an extra full read. `raw_files` ownership is unique to the corresponding source page.
- The sources' `## Related raw API references` were inspected as navigation. Their targets exist, but none was selected for a full read because all four questions explicitly concern what the two pinned pages themselves say; no claim was inferred from those unread destinations.
- Reciprocal primary routing passes: both sources link to `[[braintree-payment-platform]]`, and that concept links back to both sources. The Overview's additional fact-based `[[braintree-control-panel]]` route also links back to the Overview. Explore's other concept links are navigation-only and therefore do not require reciprocal factual citations.

**Concrete repair:** none.
