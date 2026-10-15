# PayPal Checkout Components 5.0.437 ingest review

- Work item: `github-54919ba63e5200390b6d`.
- Package boundary: `@paypal/checkout-components@5.0.436` to `5.0.437`.
- Exact SHA: `7e1f97d5f50f6cc81a86932fa00c9258f8f7e3f9`.
- User approved delta ingest and focused reading on 2026-10-15; no commit/push approval implied.

## Reading scope

Fully read current Buttons (1,470 lines) and Checkout (450 lines) authored components, current package JSON, new changelog entry, authored patch sections, affected prior attributes/context and complete cumulative wiki source/changelog. Concept audit completed before source edits. Prior package metadata compared structurally: only version differs. Separate release notes are unavailable, not silently substituted with fabricated text.

Mechanical exception: both manifest inventories, unchanged raw changelog history, generated bundle and generated diff portions. All 214 prior and 214 current files verified by SHA-256 and size. Five modified retained files, 209 unchanged; no retained additions/removals. All eight upstream changes classified: five retained, three intentional test exclusions. No packet gaps or unclassified changes. Packet markdown/snapshot and comparison markdown/patch hashes verified; required paths exist.

## Grounding

Paths below are relative to `raw/github/paypal/paypal-checkout-components/snapshots/2026-10-15-7e1f97d/files/`.

- `CHANGELOG.md:3`: "Delegate payment Permissions Policy to buttons and checkout iframes".
- `src/zoid/buttons/component.jsx:246` and `src/zoid/checkout/component.jsx:106`: both assign the `allow` attribute using the `payment` feature plus `getPayPalDomain()`.
- `src/zoid/checkout/component.jsx:100`: "Delegates the Permissions Policy 'payment' feature so PaymentRequest".
- `src/zoid/checkout/component.jsx:112`: `defaultContext: supportsPopups() ? CONTEXT.POPUP : CONTEXT.IFRAME,`.

## Conclusions and boundaries

The authored change configures payment permission for both frames. Comments explain named-origin navigation rationale; full external Zoid/SDK-client implementation is not retained. Existing popup selection, legacy button attribute, title/role and callbacks remain. No new public payment/React API, account eligibility, browser-policy bypass or hosted deployment is established.

Both generated bundles are 408,914 bytes and contain no literal `allowpaymentrequest`; scoped-style normalization does not make them equal. No complete generated-code semantic equivalence or independent bundle proof of the authored change is claimed. Prior changelog is an identical suffix, and historical wiki findings remain preserved. Tests are excluded and were not executed. No upstream builds, installs, browser, screen-reader or payment execution.

Validation outcomes are recorded in the provider log after the final checks. Shared unrelated website-ingest work, raw evidence and registry/code/rules remain untouched.

## Close validation

Five typed pages pass `validate_wiki`; `git diff --check` passes. Old source/changelog body lines are preserved in order; relative evidence links resolve; company/provider catalog entries are unique and source_count remains 177. Work item is `ingested`, with zero pending items globally. Global collection validation is not clean: ten errors, comprising the previous eight plus an unrelated Adyen SDK Automation packet-budget/invalid-packet pair. No error names this item. That packet and its policy are unchanged by this work; they were not repaired within this scope.
