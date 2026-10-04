# Stripe React Native serial ingest, 2026-10-04

Approved order: 0.76.0 full, 0.77.0 full, 0.78.0 full, 0.79.0 delta,
0.80.0 delta. The user approved focused reading of changed code, affected
prior code and migration guidance, with mechanical hash verification of
unchanged files and inventories. Full mode adds knowledge without erasing
older version history. No commit or push is authorized.

## 0.76.0 - github-5b7b7125a474bec8891c

- [x] Read evidence and record grounding quotes.
- [x] Audit and update related concepts first.
- [x] Add source and changelog knowledge.
- [x] Update company; keep source count unchanged.
- [x] Check remaining concept implications.
- [x] Assess cross-company comparison need (none; one-repository update).
- [x] Check contradictions and preserve history.
- [x] Update provider index.
- [x] Update provider and root logs.
- [x] Validate and complete work item.

## 0.77.0 Checkpoints

- [x] Read changed code, affected prior code, guidance and verify inventories.
- [x] Concept audit/update first.
- [x] Source/changelog additions.
- [x] Company update, unchanged count.
- [x] Remaining concept implications.
- [x] Comparison need (none).
- [x] Contradiction/history check.
- [x] Provider index.
- [x] Logs.
- [x] Validation and terminal state: six wiki pages and GitHub validation pass; diff check passes; completed.

233 current/247 prior file hashes pass; packet/comparison/notes identities and
unchanged changelog history pass. Grounding quotes: current README.md:76,
"The React Native **new architecture** (TurboModules and Fabric) is required.";
src/types/Onramp.ts:250, "Type of the provided ID number. Defaults to 'social_security_number'.";
StripeSdkModule.kt:895, "A Google Pay request is already in progress.";
src/connect/EmbeddedComponent.tsx:663, "Financial Connections completed without a session".
The complete new GooglePayRequestLauncher and Checkout configuration mappers
were reviewed through their complete added-file hunks; older removed manager
implementations and changed production hunks were read under focused reading.
Unchanged Checkout stubs remain hash-identical, so mapper presence is not runtime
availability. Android Onramp implementation remains patch-only evidence.

## 0.78.0 Checkpoints

- [x] Read changed production hunks, affected prior code and complete migration guidance; verify inventories.
- [x] Concept audit/update first (React Native concept; no new major topic).
- [x] Source/changelog additions.
- [x] Company update, unchanged count.
- [x] Remaining concept implications (small error-code additions stay in SDK concept).
- [x] Comparison need (none).
- [x] Contradiction/history check: 0.76/0.77 unavailable APIs remain historical; 0.78 partial implementation is version-qualified.
- [x] Provider index.
- [x] Logs.
- [x] Validation and terminal state: six wiki pages, GitHub validator and diff check pass; completed.

233 current/233 prior hashes, packet/comparison/notes and older changelog history
pass. Both unchanged hook/view stubs are hash-identical. Complete added native
controllers/serializers and the SPM helper were read from added-file hunks;
the latter is patch-only evidence outside the capsule. Grounding quotes:
README.md:79, "React Native verions < 0.75 are deprecated.";
MIGRATING.md:7, `use_frameworks! :linkage => :dynamic`;
src/checkout/createCheckout.ts:122, `present: notImplemented,`;
ios/StripeSdkImpl+Checkout.swift:91, "The installed Stripe iOS SDK does not support CheckoutController.updateEmail yet."

## Serial Progress

Each cycle uses the same ten checkpoints above and starts only after its
predecessor is validated and completed.

| Version | Item | Mode | Progress |
| --- | --- | --- | --- |
| 0.76.0 | github-5b7b7125a474bec8891c | full | Completed |
| 0.77.0 | github-5f21519e3eed9f164ede | full | Completed |
| 0.78.0 | github-d9f1ae40b60cf515676a | full | Completed |
| 0.79.0 | github-1a16bda9bfe31d157849 | delta | Completed |
| 0.80.0 | github-9be7291cb2f1d1ffc9b4 | delta | Completed |

## 0.79.0 Checkpoints

- [x] Read changed production hunks and affected prior code; complete hook/controller/new handshake read. Guidance unchanged.
- [x] Concept audit/update first: existing React Native concept.
- [x] Source/changelog additions.
- [x] Company update, unchanged count.
- [x] Remaining concept implications (no new major topic).
- [x] Comparison need (none).
- [x] Contradiction/history check: hook/handshake changes version-qualified, payment gaps preserved.
- [x] Provider index.
- [x] Logs.
- [x] Validation and terminal state: six wiki pages, GitHub validator and diff check pass; completed.

0.79.0: 234 current/233 prior hashes, packet/comparison/notes, unchanged historical
changelog pass. 212 unchanged files; 1 added and 21 modified retained paths.
All upstream changes classified; the SPM helper's small build-dir guard is
patch-only evidence. Grounding: useCheckout.ts:40-41, "Changing getConfiguration does"
/ "not reload automatically; reload uses its latest value.";
createCheckout.ts:136, `present: notImplemented,`; :173, `confirm: notImplemented,`;
EmbeddedComponent.tsx:855, `const textColor = appearance?.variables?.colorText || '#000000';`.
The new hook/server-update path is a contained addition to the already ingested
partial preview bridge, not a payment confirmation or public-access claim.

## 0.80.0 Checkpoints

- [x] Read changed production hunks and affected prior code; complete new native view/spec implementations; hash inventories.
- [x] Concept audit/update first: existing SDK concept owns consent/inline rendering additions.
- [x] Source/changelog additions.
- [x] Company update, unchanged count.
- [x] Remaining concept implications (no new product concept needed).
- [x] Comparison need (none).
- [x] Contradiction/history check: inline rendering replaces only the view stub; modal/confirmation remain unimplemented.
- [x] Provider index.
- [x] Logs.
- [x] Validation and terminal state: six wiki pages, GitHub validator and diff check pass; completed.

0.80.0: 240 current/234 prior hashes, packet/comparison/notes and older cumulative
history pass. 6 added/15 modified retained paths, 219 unchanged. Native dependency
pins remain unchanged. Demo is patch-only evidence, outside the capsule; its
custom-secret-in-mobile pattern is not production integration guidance.
Grounding: FinancialConnections.ts:7, "Stripe may still show its own consent pane in";
:16, "time, and reuse the same value on retries instead of the time Financial";
createCheckout.ts:153, `present: notImplemented,`; :190, `confirm: notImplemented,`;
CheckoutPaymentElementContainerView.swift:35, "A Checkout Payment Element can only be mounted once."
No claim of complete upstream-tree read or native build/payment proof.

## Reading notes

Final audit: all five work items are `ingested` in approved serial order.
Provider-index/root-log wikilinks, cumulative source/changelog literal evidence
paths, unique headings/catalog entries and unchanged company source count pass.
Corrected two historical NotificationBanner links from `src/components/` to
the retained `src/connect/` file; raw evidence was not modified.
No native build/device/payment testing, commit or push was performed.

0.76.0 validation: six schema-bearing pages pass validate_wiki; the provider
index and root log have pre-existing no-frontmatter formats and are not
schema-bearing sources. Passing GitHub validation: 164 snapshots, 150 release
records, 107 comparisons, 164 work items. git diff --check passes. Item completed.

0.76.0: complete cumulative source/changelog read; changed production hunks
and affected prior code reviewed, complete new Checkout contract/stubs and
migration guide read. All 247 current and 252 prior retained file hashes,
packet Markdown, comparison Markdown/patch, release notes and unchanged
upstream changelog history verified. The effective full inventory is covered
by those hashes under the approved exception, not a claim of full-tree reading.

Grounding excerpts (paths below are relative to snapshot `files/`):

- Current `src/hooks/useOnramp.tsx:313-314`: "Deletes the given crypto wallet from the current Link account." and "Requires an authenticated Link user."
- Current `src/hooks/useCheckout.ts:5`: "This version of @stripe/stripe-react-native does not include native support for the Checkout private preview."
- Current `src/hooks/useCheckout.ts:32`: `status: enabled ? 'error' : 'idle',`
- Prior `ios/StripeSdkImpl.swift:41`: "Checkout Sessions are temporarily unavailable while the native integration is being rebuilt."

Important correction: prior 0.75.0 Checkout bridges already rejected calls;
currency views were zero-height placeholders. The new contract is not a
regression from an established working Checkout integration. Current source
must distinguish ordinary Intent-based PaymentSheet from this preview.

The 0.76.0 comparison exposes removal of CurrencySelectorElement and the
previous Checkout bridge, plus replacement private-preview APIs that are
explicitly unimplemented. The user separately approved promoting this item
from delta to full on that evidence. Release notes alone mention only
Crypto Onramp wallet deletion. No native device or payment test is implied.
