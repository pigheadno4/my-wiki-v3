# Braintree C15 fixed query audit — Group D

- Scope: Best Practices (Node.js) + Server SDK Deprecation Policy
- UTC start: 2026-09-23T11:27:52Z
- UTC analysis end: 2026-09-23T11:29:24Z
- Evidence: both selected raw pages read completely

## Braintree Best Practices (Node.js)

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-best-practices-node]]` → `[[raw/braintree/docs/reference/general/best-practices/node-2026-09-16]]`.

### 1. Where is Braintree Best Practices (Node.js) documented?

- Object/action match: Braintree Node.js Best Practices documentation and its retrieval location; the route reaches that exact page, not a client-SDK or payment-method-specific best-practices page.
- Direct answer: use `[[source-braintree-best-practices-node]]`; its factual evidence is the path-qualified raw page `raw/braintree/docs/reference/general/best-practices/node-2026-09-16.md`.
- Raw locator: source URL at line 1; `# Best Practices` at line 14.
- Verdict: **PASS**.

### 2. Which integration, timeout, version and transport-security qualifications must remain visible, and where are exact configuration details?

- Object/action match: Node.js server-integration operating qualifications and exact-detail locations; this does not ask for a current SDK support matrix or a guarantee that a timed-out transaction failed.
- Direct answer: programmatic behavior should key on stable response codes rather than mutable response text (lines 29–42). The fetched page recommends the latest SDK and records Node `2.24.0` as its minimum for secure gateway communication, but that table is collected evidence rather than proof of the current supported/recommended version; exact npm inspection and update commands are at lines 68–107, where the surrounding RubySDK/.NET labels are visibly inconsistent. The gateway timeout is stated as 60 seconds; a shorter server-SDK timeout can return an exception before the gateway finishes, and the 10-second/19-second sale example requires checking gateway state because the customer may still be charged (lines 110–128; exact `gateway.config.timeout` example at lines 117–128). The page requires TLS 1.2+ for gateway connections and HTTPS for production payment-data forms, prefers TLS 1.3, and locates the collected cipher lists at lines 135–173. Its testing exception still requires HTTPS for a PayPal button in mobile webviews (lines 176–178). Certificate providers can change and Braintree does not recommend certificate pinning because changes may not be communicated proactively; the dated certificate table is historical collected evidence (lines 181–196).
- Raw locator: `## Code vs text`, lines 29–42; `## Server SDK versions`, lines 50–107; `## Timeouts`, lines 110–128; `## Transport Layer Security`, lines 135–178; `## SSL Certificates`, lines 181–196.
- Verdict: **PASS**.

## Braintree Server SDK Deprecation Policy

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-server-sdk-deprecation-policy]]` → `[[raw/braintree/docs/reference/general/server-sdk-deprecation-policy-2026-09-16]]`.

### 3. Where is Braintree Server SDK Deprecation Policy documented?

- Object/action match: Braintree's server-SDK lifecycle policy and its retrieval location; the route reaches the server policy, not the separate client-SDK deprecation policy.
- Direct answer: use `[[source-braintree-server-sdk-deprecation-policy]]`; its factual evidence is the path-qualified raw page `raw/braintree/docs/reference/general/server-sdk-deprecation-policy-2026-09-16.md`.
- Raw locator: source URL at line 1; `# Server SDK Deprecation Policy` at line 14.
- Verdict: **PASS**.

### 4. What lifecycle categories and update guidance are stated, without treating the collected version list as current support?

- Object/action match: general server-SDK lifecycle meanings and maintenance actions; no current language/version status is inferred.
- Direct answer: Braintree recommends regular integration updates and a server-SDK update at least every two years (lines 17–18). The policy defines `Active` as the single current fully supported major version receiving new features; `Inactive` as a version with a deprecation date receiving security updates but no new features; `Deprecated` as receiving no updates while processing is stated to continue for one year after the deprecation date, with immediate-upgrade guidance; and `Unsupported` as receiving neither developer nor Support assistance, with processing subject to suspension at any time (lines 37–44). Version-specific status and deprecation dates belong in each SDK README (lines 46–48), and users should watch the applicable GitHub repository for updates (lines 55–59). The policy allows unforeseen exceptions (lines 51–52), so neither collection nor a retained package version proves present status or a deadline.
- Raw locator: update note, lines 17–18; `## Status categories`, lines 37–52; `## Tips for following SDK versions`, lines 55–59.
- Verdict: **PASS**.

## Bounded group gap sweep and completeness

- Searched Braintree raw filenames for best-practices, server-SDK, deprecation, migration, upgrade and exceptions material; inspected both sources' related-raw routes and the two selected raws' cross-links.
- Client-SDK deprecation/migration, PayPal/Fastlane best-practices, Exceptions, Server SDK Migration Guide and Upgrade pages are distinct authorities or deeper navigation. Neither fixed Group D answer required facts from those unread pages; no claim from them was imported and no promotion gap was found.
- Reciprocal routes pass: root index links `braintree-index`; provider index links `braintree-server-sdk`; that concept links both selected sources; each source links the concept and its exact raw evidence.
- The campaign's company/provider source aggregates are not yet closed. Direct provider-index/company catalog entries for these two new sources remain a **pending coordinator-close item**, not a source or retrieval-route failure; the actual concept-led paths above already resolve.
- Completeness: exactly four fixed questions answered, two per page; both full selected raws read; object/action identity and exact locators recorded; **4/4 PASS**.

- UTC handoff: 2026-09-23T11:30:39Z
