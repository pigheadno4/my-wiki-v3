# PayPal v6 Sample Collection Review

## Scope And State

- User approved the 300 -> 350 source-file limit and then 1,000,000 -> 2,000,000 source-byte limit, preserving selection paths, exclusions and packet limits. Previous policy hashes remain registered. Matching registry expectations were updated.
- Prior ingested SHA: `a318bcf7cb8a458b180df553ab459db3a5a79586`, ingested 2026-10-04.
- Collected main SHA: `c4333b444368a67ad54fa4786fccb57021c5abdd`, collected 2026-11-03; upstream commit date 2026-10-30.
- Retained snapshot: `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-11-03-c4333b4/manifest.json`.
- Comparison: `comparisons/default-branch/a318bcf--c4333b4/comparison.json` and adjacent Markdown/patch.
- At the original collection stop, work item `github-4108c3990b081a22a6e2` was `needs_manual_review`, recommended full for `broad-change-set`. The packet recovery below supersedes that state; no ingestion or publication has occurred.

## Verified Inventory And Blocker

- Source selection succeeds: 316 files, 1,150,559 UTF-8 bytes; 11 excluded files, 397,902 bytes. Current/prior 580 files pass size, SHA-256 and Git blob identity checks.
- Manifest path comparison: 56 added, four removed, three modified, 257 unchanged. Git recognizes four Fastlane renames; these are not four lost behaviors.
- Full packet reading inventory calculated using both retained manifests/files, comparison JSON/Markdown/patch and the builder's six shared wiki paths: 591 paths, 3,540,368 bytes at review time. Existing 550-path / 3,000,000-byte limits are insufficient. Builder stopped at the path limit; no packet published.
- During collection, 264 verified prior blobs were reused only in the temporary Git object cache. No refs, existing snapshots or raw files modified.
- Targeted sample registry test passes. Full suite: 820 tests, 816 pass, same four unrelated registry expectation failures (Adyen Postman, Braintree GraphQL, PayPal Messages iOS tracks, Metronome Terraform cadence). Whitespace check passes.

## Preliminary Findings, Not Completed Ingestion

The comparison inventories were inspected; the current Fastlane HTML README and complete advanced `threeDSecure/fastlane.js` were read. Other changed source has not yet received full semantic review.

- Fastlane is reorganized into recommended and advanced 3DS examples. The advanced source calls `createFastlaneThreeDomainSecure()`, checks eligibility and invokes `show()`. Successful authentication with `POSSIBLE`/`YES` liability shift returns the enriched nonce for the order; cancellation/failed checks stop that submission. Ineligible cards continue using the original token. README explicitly warns that production should also confirm the Orders API authentication outcome. No execution, liability-shift or production-safety guarantee inferred.
- Inventory adds 24 local-payment-method example folders and changes the LPM README and client catalog. Folder presence is not verified availability, eligibility or a completed integration review.
- Existing server source, React source and returning-buyer saved-payment examples have no retained path/hash changes in this boundary. This does not establish unchanged hosted SDK behavior or external dependencies.

## Next Gate

Recommend approval to raise only this repository's packet limits to 650 paths / 4,000,000 bytes and regenerate from retained exact-SHA evidence, without recloning. Preserve all earlier source/history and collection selection policy. Review the complete packet and findings before requesting separate ingestion approval.

## Approved Packet Recovery

The user approved the preceding next gate. Only this repository's packet limits were raised to 650 paths / 4,000,000 bytes, with previous policy hashes preserved and matching registry test expectations updated. Selection paths, exclusions, source limits and retained evidence were not changed. No clone or network collection was repeated.

Using the existing builder, atomic packet publisher and collection-finalization APIs, the retained comparison and snapshots produced `ingest-packets/github-4108c3990b081a22a6e2/packet.json` and `packet.md`. The item is now `awaiting_approval`, approved_mode null, recommendation full/normal for `broad-change-set`; last_error cleared. No approval or next-ingest command was run.

- Required reading: 591 paths / 3,540,368 bytes at review time, within both approved packet budgets.
- Selected changes: 52 added, four renamed, three modified; 257 unchanged retained files. This reconciles with the manifest-only counts above, where renames appear as added/removed paths.
- Packet reports zero evidence gaps and zero unclassified changes. Packet Markdown hash verified; canonical offline rebuild validates this item.
- Current manifest SHA-256: `a7c13349b8d80e7f0b3a1cb4943a8b5753dc7be1d21b486d355988456c2172a8`; prior: `daa26e328177f6d350b41359ed113e15688b484fc3728f9ce61a5a2f9aafad60`.
- Full GitHub validator retains exactly 13 known unrelated structural errors, with one pending item (this packet). No error for this repository.

### Additional Source Review

Read complete advanced Fastlane SDK-initialization JS and HTML, current LPM README, and complete Bre-B and PromptPay QR app JS. This is collection-stage review, not a claim that every file in the full-ingest packet has been read.

- Advanced Fastlane initializes the hosted sandbox v6 SDK with the `fastlane` component and browser-safe token. The 3DS helper uses USD 205.00 to match the documented default cart, requests a challenge for demonstration, and replaces the payment token only after successful authentication with possible/yes liability shift. An ineligible card continues without 3DS. README requires production server-side confirmation of the Orders API result; no runtime authentication or liability-shift outcome was tested.
- New examples include Bre-B, CoDi, DiMo, Naver Pay, Mercado Pago, Nequi, PSE, PromptPay QR and VietQR, among 24 new folders. These are sandbox sample contracts, not proof of merchant enablement or general availability.
- Bre-B and PromptPay QR examples fetch client ID, check method/currency eligibility, mount name/email fields, validate, then start with `presentationMode: "auto"` and an order using `ORDER_COMPLETE_ON_PAYMENT_APPROVAL`. Approval retrieves the order; the client displays success without locally checking the returned payment status. Do not treat that label as settlement proof. The shared README still describes popup behavior and name-only fields; those descriptions are not exhaustive for these new files.
- No new React implementation, server implementation or returning-buyer saved-payment implementation is present in this retained diff. Hosted SDK and external dependency behavior are independent evidence boundaries.

Next: obtain separate full additive ingestion approval and choose reading method. Suggested focused reading fully covers changed authored files, affected prior code and dependencies; unchanged files and generated inventories may be verified mechanically only with explicit approval. Preserve all earlier wiki history; no commit or push yet.
