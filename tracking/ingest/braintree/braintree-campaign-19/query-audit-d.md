# Braintree C19 fixed retrieval audit — Group D

Scope: exactly the four fixed Group D questions for Data Migration Overview and Imports. Both promoted source pages and both pinned raw pages were read completely. The repository remained read-only.

## `get-started-data-migration-overview`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 211 → `[[braintree-data-migration]]`) → `wiki/concepts/braintree-data-migration.md` (`## Retrieval routes`, line 14 → `[[source-braintree-get-started-data-migration-overview]]`) → `wiki/sources/braintree/source-braintree-get-started-data-migration-overview.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 43–45) → `raw/braintree/articles/get-started/data-migration/overview-2026-09-16.md`.

1. **Where is the data-migration overview?**
   - **Object/action match:** Braintree's collected overview of migration directions and boundaries, not the dedicated import process, export process, or public-key material.
   - **Direct answer:** The promoted `source-braintree-get-started-data-migration-overview.md` retrieval entry routes to the complete collected `# Overview` raw at the path above.
   - **Exact raw locator:** provenance and canonical identity at lines 1 and 6–7; page identity and portability statement at lines 14–16.
   - **Verdict:** PASS.

2. **Which migration paths does it identify and which details are delegated to dedicated pages?**
   - **Object/action match:** overview-level inbound and outbound data portability plus its routing boundary; not either dedicated procedure or operational key content.
   - **Direct answer:** The page identifies two paths: importing sensitive customer and credit-card data into a new Braintree gateway, and exporting that data when leaving Braintree. It states overview-level fee, timing, and migration restrictions itself, including that customer and credit-card records can be imported/exported while subscription and transaction information cannot. It delegates the importing process to the Imports article and the leaving/exporting process to the Exports article, and separately provides a contact route for questions or scheduling. Those linked procedures are navigation only for this answer.
   - **Exact raw locator:** portability directions at `# Overview`, lines 14–16; overview-owned fee and timing qualifications at `## Fees` and `## Time frame`, lines 19–26; migratable and excluded data plus linked post-migration/report/API routes at `## Data migration restrictions`, lines 29–39; dedicated Imports, Exports, and contact routes at `## Getting started`, lines 42–46.
   - **Verdict:** PASS.

## `get-started-data-migration-imports`

Actual concept-led route: `wiki/index.md` (`## PSP Indexes`, line 11 → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts`, line 211 → `[[braintree-data-migration]]`) → `wiki/concepts/braintree-data-migration.md` (`## Retrieval routes`, line 16 → `[[source-braintree-get-started-data-migration-imports]]`) → `wiki/sources/braintree/source-braintree-get-started-data-migration-imports.md` (`raw_files`, lines 7–8; `## Raw Sources`, lines 52–54) → `raw/braintree/articles/get-started/data-migration/imports-2026-09-16.md`.

3. **Where is Braintree data import documented?**
   - **Object/action match:** Braintree's collected inbound customer/payment-method import guide, not outbound Vault export, periodic backup/failover, or migration public-key publication.
   - **Direct answer:** The promoted `source-braintree-get-started-data-migration-imports.md` retrieval entry routes to the complete collected `# Imports` raw at the path above.
   - **Exact raw locator:** provenance and canonical identity at lines 1 and 6–7; page identity at line 14; import scope and starting prerequisites at line 22.
   - **Verdict:** PASS.

4. **What import purpose, prerequisites, process and consequential boundaries does the collected page document?**
   - **Object/action match:** inbound migration of customers and payment methods from another processor into Braintree, including the collected page's prerequisites, preferred transfer flow, and material limits; not export, backup, failover, or guaranteed wallet transaction success.
   - **Direct answer:** The page offers to import customers and payment methods from another processor. To start, the merchant must request an export from the current/former processor and ask that processor to transfer it securely to Braintree. In Braintree's preferred flow, Braintree obtains the old processor's PGP public key, sends encrypted SFTP credentials, the old processor encrypts the data with Braintree's public key and uploads it, and Braintree performs the import; completion produces a logfile of created customer IDs and payment-method tokens. Consequential boundaries include no more than two imports and no periodic backup/failover imports; mandatory public-key encryption before transmission; a collision check when supplied customer IDs or tokens are reused; preferred UTF-8 CSV with possible delays for other formats; a matching PayPal Business Account for imported Billing Agreements; separate Apple Pay/Google Pay files and issuer-controlled transaction outcomes that may require re-adding consistently declining methods. The page also documents US ACH input and ownership mapping, but its field inventory remains at the raw locator rather than being copied here. The snapshot does not prove current availability, processor participation, timing, acceptance, or transaction success.
   - **Exact raw locator:** two-import and backup/failover boundary at `# Imports > **NOTE**`, lines 17–18; purpose and prerequisites at line 22; preferred transfer flow and output logfile at `## Data transfer process`, lines 25–35; mandatory encryption at lines 38–39; format qualification at `## Data format`, lines 44–46; identifier mapping/collision check at `## Mapping the data`, lines 49–55; PayPal account match at lines 159–165; Apple Pay boundaries at lines 170–181; Google Pay boundaries at lines 188–215; US ACH scope and ownership mapping at lines 222–263.
   - **Verdict:** PASS.

## Shared gap sweep and reciprocal-link check

- **Pinned evidence:** complete selected raws match the C19 manifest hashes: Data Migration Overview `5f3e96c3d93af6d52c2d6bf3ba40cb0fb78c59833dd0d73d26425b1803ee03f1`; Imports `09b75f999833e3ab809dc1bef17fdeb27172f3c47ddfa121aec60865dc02e359`. Canonical URLs agree across manifest, source frontmatter, and raw provenance.
- **Bounded gap sweep:** the data-migration raw directory contains Overview, Imports, Exports, and Public Key. Topic search also surfaced the discovery inventories and the import source's navigation-only Custom Fields reference. The four fixed questions are page-scoped and the two pinned raws answer them completely, so Exports, Public Key, Custom Fields, and discovery files required no extra full read. No export/public-key detail was imported into the answers; the import answer uses only the fully read Imports raw's own statements about its transfer flow and encryption prerequisite. No relevant conflict or older snapshot was found.
- **Reciprocal routes:** the root routes to `braintree-index`; the provider index routes to `braintree-data-migration` and also lists both sources directly; the concept links to both promoted sources; each source links back to the concept and to its exact pinned raw through both `raw_files` and `## Raw Sources`. Each audited source appears once in the concept's `## Retrieval routes`; the Imports source additionally appears once under `## Sources`, serving a distinct provenance-list role.
- **Completeness:** all 4/4 fixed questions include object/action match, a direct answer, exact raw locator, and verdict. **No repair is required.**

**Group verdict: PASS (4/4).**
