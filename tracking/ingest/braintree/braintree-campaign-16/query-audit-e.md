# Braintree C16 Query Audit — Group E

- Scope: Descriptors + Bank Identification Numbers.
- Audited: `2026-09-23` UTC after both source promotions.
- Evidence: both selected raw pages read completely; source and root/provider-index → concept routes inspected.

## Descriptors

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-descriptors]]` → `[[raw/braintree/articles/control-panel/transactions/descriptors-2026-09-16]]`.

1. **Query:** Where is Braintree Control Panel Descriptors documented?
   - **Object/action match:** Account and transaction descriptor visibility/configuration, distinguishing Control Panel, transaction API and PayPal console.
   - **Direct answer:** The route above finds the dedicated Descriptors source and complete collected raw.
   - **Exact raw locator:** `# Descriptors`, lines 14–33.
   - **Verdict:** PASS; provider-index direct cataloging awaits aggregate close.

2. **Query:** Which descriptor types and visibility/configuration boundaries does this article document?
   - **Object/action match:** Soft, hard, dynamic descriptors and their specific configuration routes.
   - **Direct answer:** Soft descriptors show while a post-authorization charge is pending; hard descriptors show after settlement and bank finalization. Dynamic descriptors are configured and passed per transaction via API, subject to processor support for soft-only or both soft and hard. The bank ultimately decides exact statement rendering. The collected page routes US/Europe/Australia account-descriptor viewing/editing to the Control Panel Business page, other regions to Braintree, and PayPal-transaction descriptor changes to PayPal console. It gives no processor-specific request shape or current support guarantee.
   - **Exact raw locator:** purpose and bank authority lines 16–18; descriptor types and processor qualification lines 20–25; regional Control Panel/contact route lines 27–31; PayPal path line 33.
   - **Verdict:** PASS.

## Bank Identification Numbers

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-bank-identification-numbers]]` → `[[raw/braintree/articles/control-panel/transactions/bank-identification-numbers-2026-09-16]]`.

3. **Query:** Where is Braintree Control Panel Bank Identification Numbers documented?
   - **Object/action match:** Collected BIN/IIN lookup article; not a current PCI ruling or SDK response schema.
   - **Direct answer:** The concept routes to the dedicated BIN source and complete raw article above.
   - **Exact raw locator:** `# Bank Identification Numbers`, lines 14–24; `## Finding BINs in the gateway`, lines 27–41.
   - **Verdict:** PASS; provider-index direct cataloging awaits aggregate close.

4. **Query:** Which BIN information and Control Panel lookup/use boundaries does this article document?
   - **Object/action match:** Single and multi-transaction lookup, linked API route, six-digit versus eight-digit scope, dated PCI qualification.
   - **Direct answer:** The article defines BIN/IIN as the first six card digits and suggests purchase/decline trend analysis. A single Control Panel Transaction Search shows them in Payment Information; CSV download exposes `First Six of Credit Card` for many transactions. The article separately links API transaction-ID search without naming a current SDK field path. Although it discusses April 2022 eight-digit issuer BIN processing, it says Braintree APIs, GraphQL, console search and BIN reports continue providing six digits. PCI masking and data-at-rest passages cite PCI DSS v3.2.1 and cannot establish current requirements or eight-digit display permission.
   - **Exact raw locator:** definition/use lines 16–20; Control Panel/CSV/API lookup lines 27–41; expansion and six-digit availability lines 44–61; historical PCI passages lines 64–78.
   - **Verdict:** PASS.

## Bounded gap sweep

- Inspected selected raws plus current concept/source routes. Linked transaction-sale, search, decline-analysis and PCI pages remain navigation-only; no API request shape or current compliance conclusion is inferred.
- Both source/raw backlinks and reciprocal Control Panel concept entries resolve. No material omission, broken route, date/region overclaim or answer gap found. Group E: **4/4 PASS**.
