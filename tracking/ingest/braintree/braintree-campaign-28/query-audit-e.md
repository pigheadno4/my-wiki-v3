# C28 fixed query audit — Group E

Scope: `hosted-fields-faq-javascript-v3` and `hosted-fields-styling-javascript-v3`. Both approved manifest hashes were independently verified, and both pinned raws were read in full. The sources are JavaScript v3 Hosted Fields documentation snapshots fetched 2026-09-16; their links to supported Hosted Fields options/properties are specifically pinned to `braintree-web` 3.92.1. They document browser Hosted Fields configuration and presentation, not Drop-in, server transaction completion, current SDK support, merchant eligibility, or successful payment execution.

## 1. Where is the JavaScript v3 Hosted Fields FAQ?

**PASS.** Navigate `[[index]]` → `[[braintree-index]]` → `[[braintree-web-sdk]]` → `[[source-braintree-hosted-fields-faq-javascript-v3]]` → `[[raw/braintree/docs/guides/hosted-fields/faq/javascript/v3-2026-09-16]]`. The source page identifies the canonical JavaScript v3 FAQ URL and the pinned raw; the raw identifies the same URL and `/javascript/v3/` slug.

Raw locators: `raw/braintree/docs/guides/hosted-fields/faq/javascript/v3-2026-09-16.md:1-9` (source URL, fetch date, title and JavaScript v3 slug), `:14-17` (FAQ title and first question).

## 2. Which central integration boundaries and consequential cautions does this FAQ snapshot state?

**PASS.** The snapshot says:

- For CVV verification of a vaulted card, configure only the Hosted Fields `cvv` field. Tokenization returns a nonce whose data contains only the CVV; use that nonce together with the stored card's payment-method token. The separate `Transaction.Sale()` link is the transaction route, so this FAQ does not itself establish authorization or payment success (`:17-47`).
- Hosted Fields inputs are synthetic inputs inside iframes. iframe-injected media queries use the iframe viewport, not the parent page; merchant `<div>` containers limit injection side effects and carry merchant-page styling (`:50-52`, `:138-145`).
- Expiration month and year can use dropdowns (`:55-136`). On iOS, the guide says label-click focus is disabled because of buggy behavior, unlike its stated usual behavior elsewhere (`:148-150`).
- Every field declaration requires a valid CSS2 selector or DOM node (`:153-187`). Aggressive iframe sandboxing on CodePen, JS Bin, JSFiddle and similar sites can restrict Hosted Fields functions, so the guide recommends retesting outside those sites (`:189-193`).

These claims remain snapshot- and object-qualified; they do not project the linked 3.92.1 API reference onto every JavaScript v3 release.

## 3. Where is JavaScript v3 Hosted Fields styling documented?

**PASS.** Navigate `[[index]]` → `[[braintree-index]]` → `[[braintree-web-sdk]]` → `[[source-braintree-hosted-fields-styling-javascript-v3]]` → `[[raw/braintree/docs/guides/hosted-fields/styling/javascript/v3-2026-09-16]]`. The source page and raw agree on the canonical styling URL and JavaScript v3 scope.

Raw locators: `raw/braintree/docs/guides/hosted-fields/styling/javascript/v3-2026-09-16.md:1-9` (source URL, fetch date, title and JavaScript v3 slug), `:14-20` (styling responsibility split and the 3.92.1 property-reference link).

## 4. Which styling responsibilities and limitations does this styling snapshot state?

**PASS.** The merchant stylesheet owns container layout, width, height and outer presentation, and Hosted Fields requires an explicit container height (`:16-18`). Internal field text is styled through the JavaScript `styles` configuration; the exact supported-property list is delegated to the linked `braintree-web` 3.92.1 reference (`:20`). The examples cover all inputs, specific fields, focus/valid/invalid states and iframe-scoped media queries, while warning that custom web fonts are unsupported, only system-installed fonts should be used, and media queries apply to the iframe rather than the root window (`:23-105`). Hosted Fields toggles focused, invalid and valid classes on the corresponding merchant container for outer-state styling (`:107-143`) and allows CSS transitions only for allowed properties (`:144-191`). These examples do not prove rendered appearance, validation acceptance, tokenization, or payment execution.

## Route and reverse-link check

**PASS.** The root index routes Braintree queries to `[[braintree-index]]`; the provider index routes Hosted Fields/Web SDK queries to `[[braintree-web-sdk]]`. The concept reciprocally links both promoted source pages (`wiki/concepts/braintree-web-sdk.md:79-80`), and each source links back to the concept (`wiki/sources/braintree/source-braintree-hosted-fields-faq-javascript-v3.md:37`; `wiki/sources/braintree/source-braintree-hosted-fields-styling-javascript-v3.md:40`). Each source owns exactly its matching pinned raw through `raw_files` and a resolving Raw Sources wikilink. Direct provider-index source catalog entries are not yet present, matching the coordinator-stated pending aggregation; the concept route is already complete.

Verified SHA-256:

- FAQ: `dc8580d277f776abbcc1424eb8d29e1d3772d992ea5c85ad3327e535af1e93e9`
- Styling: `74b0ffc3fe6281d1ebe46830db9fbdb417ae9d993e6439c18265483ee0374185`

The bounded filename sweep found the expected JavaScript events/examples pages and native sibling variants. Neither fixed query requires them, and no retained claim or conflict justified expanding authority beyond the two pinned raws.

## Overall verdict

**PASS.** All four fixed questions are answerable accurately from the promoted concept/source routes and matching pinned raw snapshots. Hashes, JavaScript v3 identity, Hosted Fields object/action scope, precise raw locators, and reciprocal links are sound. The only incomplete route is the already-known direct provider-index catalog aggregation, which is not a query-answering defect because the indexed concept route resolves both sources.
