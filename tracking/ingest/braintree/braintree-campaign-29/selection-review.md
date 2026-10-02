# Braintree C29 five-slot ten-page selection

Status: COMPLETE — approved execution closed 2026-10-02T15:36:20Z. Ten independently approved sources, 20/20 fixed queries, five shared rolling child slots. Fresh preflight preceded initialization; comparative timings are in retrospective.md. No commit or push.

## Scope and concurrency

Ten collected, unowned website pages; **2,130 file lines**. Baseline **252 sources = 235 website + 17 GitHub**; C28 is complete but remains uncommitted/unpushed. Preserve its work and unrelated shared-checkout edits.

The current host exposes six total slots: primary coordinator plus five children. Use **five shared dynamic child slots** across workers, reviewers and query auditors, not five per role. Manifest worker_concurrency/review_concurrency are each 5, but the coordinator always supplies a combined budget bounded by actual free host capacity and subtracts active auditors. No extra shared-slot schema field or new scheduler is needed.

Start longest pages early. On each completion persist/accept the result and dispatch eligible next work immediately, before routine promotion/report prose. Prefer ready reviews with the existing one-worker reserve only when queued work exists and no worker is active. Prioritize eligible targeted corrections within each role; do not preempt active jobs. No batch barrier.

## Fixed questions

| Job | Lines | Navigation question | Detail question |
| --- | ---: | --- | --- |
| 3ds-advanced-javascript-v3 | 464 | Where are JavaScript v3 3DS advanced options documented? | Which central option purposes and consequential prerequisites or qualifications does this snapshot state? |
| 3ds-advanced-android-v5 | 426 | Where are Android v5 3DS advanced options documented? | Which Android-scoped option purposes and consequential prerequisites or qualifications does this snapshot state? |
| 3ds-rules-android-v5 | 343 | Where is the Android v5-routed 3DS Rules Manager guide? | Which rule-management responsibilities and consequential conditions or limitations does this snapshot state? |
| 3ds-advanced-ios-v7 | 334 | Where are iOS v7 3DS advanced options documented? | Which iOS-scoped option purposes and consequential prerequisites or qualifications does this snapshot state? |
| 3ds-rules-javascript-v3 | 319 | Where is the JavaScript v3-routed 3DS Rules Manager guide? | Which rule-management responsibilities and consequential conditions or limitations does this snapshot state? |
| 3ds-overview | 75 | Where is the Braintree 3DS overview? | Which central authentication purpose and material integration qualifications does this snapshot state? |
| start-hosted-fields | 62 | Where is Braintree's Hosted Fields start page? | Which central Hosted Fields role, integration route and consequential qualifications does this snapshot state? |
| hf-examples-javascript-v3 | 52 | Where are JavaScript v3 Hosted Fields examples documented? | Which example purposes and consequential qualifications or implementation routes does this snapshot state? |
| start-checkout-ui-comparison | 34 | Where is Braintree's checkout UI comparison? | Which central UI-selection distinctions and material qualifications does this snapshot state? |
| hf-upgrading-javascript-v3 | 21 | Where is the JavaScript v3 upgrading-from-custom Hosted Fields guide? | Which transition instructions, support qualifications or alternative routes does this snapshot state? |

Groups: A = 3DS overview + JavaScript advanced; B = Android/iOS advanced; C = Android/JavaScript Rules Manager; D = Hosted Fields examples/upgrading; E = checkout UI comparison/Hosted Fields start. **20 questions total**, five concise groups. Three manifest audit IDs are exemplars, not another audit layer.

## Provider and handoff notes

Adopt rules/psp/braintree-ingest.md, its adopted Metronome retrieval/coordinator contract, and rules/ingest-roles.md. The Braintree authorization explicitly overrides the inherited three-slot budget for this exact approved five-slot campaign. Metronome remains unchanged. Sol medium workers and different Sol high initial reviewers; complete pinned raw reads, 3–5 exact located quotes, maximum three attempts and bounded targeted corrections remain mandatory.

Navigate root index → Braintree index → relevant existing concept. Likely routes: braintree-3d-secure, braintree-web-sdk, braintree-web-drop-in, braintree-android-sdk, braintree-ios-sdk and braintree-payment-platform; verify relevance rather than linking all. Keep 3DS authentication distinct from authorization, settlement and payment completion. Preserve SDK/platform/version, rule-management versus client execution, advice versus requirements, and captured support/alternative-route notices. Titles/paths alone establish none of these facts; workers and first reviewers still read the complete raw.

Sources are purpose-fit retrieval entries, not replacement specifications: summarize central meaning and material warnings, route routine option inventories and examples to verified raw locators. Related authority is read only for retained claims or discovered relevant conflicts. Missing rendered labels are not absence evidence against separately sourced authority. Default reciprocal concept descriptions to document type/version and purpose. Correct source identity must be copied from source_target; add a distinct guide route without replacing sibling request-reference authority. Preserve consequential conflicts affecting retained claims; do not expand to every adjacent document merely to hunt differences.

Raw Sources contains fully read factual evidence, including supporting conflict raws when needed; unread navigation belongs in Related raw API references. Reverse raw lookup is derived from raw_files, never raw edits. warnings is a string array. Repository writes and runtime transitions belong solely to coordinator.

## Close and timing

Promote individually approved concept updates before exact candidates; aggregate company/index/log/count once. Overlap disjoint fixed query groups when their routes are ready. Ask for concise direct answers, evidence locators and verdicts, not copied prompts or polished prose. Do not send a timing-only message to an already completed agent; use the initial handoff and existing records, and reuse roles only for real approved work.

One campaign-wide mechanical close checks candidate bytes, pinned raw hashes, factual links, approved updates, reciprocity, catalogs, counts and touched typed pages. Enumerate nested provider sources recursively and allow additional fully read factual raw evidence. No default third coordinator full-source review, new validator, registry, worktree, priority field or monitoring subsystem.

Rule-change tests run once during this preparation, not again for a documentation-only execution unless code/rules/validators change. Capture existing operational start/end and observed stages; distinguish overlapping role windows and post-close reports. C29 is 2,130 lines versus C28's 1,586 and has different topics, so elapsed alone cannot establish a controlled five-versus-three-slot effect.

## Preparation verification

Hash/embedded URL, absent targets, source raw/canonical ownership and 252-source baseline checks passed for all ten jobs. Manifest review configuration and a pure five-slot scheduler projection passed: five initial workers, then an immediately eligible reviewer uses a released slot while four workers remain active. The configuration is 5 children and the current host advertises 6 total agents. No campaign state was initialized.

The existing ingestion test suite passed **114 tests**. The requested full unit-suite run did not complete: a GitHub secret-scanning exception test raised `AttributeError: SecretFindingsBlocked is immutable` when Python/contextlib/unittest attempted to assign the exception traceback. The affected GitHub modules were not modified by this preparation. No full-suite success is claimed; the unrelated defect is recorded rather than fixed or hidden. Scoped rule whitespace checks passed.

Preparation authorizes no collection, ingestion, commit, push, GitHub work or next campaign. Recheck hashes/ownership/counts and actual native capacity before any separately approved execution.
