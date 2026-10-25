# Messaging Components recheck: 2026-10-25

Scope: approved recheck and collection only. No ingestion, canonical wiki editing, commit or push. Prior ingested release is `@paypal/messaging-components@1.99.0`, SHA `6c5b6649b08abbfd47e9e35029823bc278b4bb74`.

The configured future/all-stable track collected three releases. All three items remain `awaiting_approval`; the collector recommends delta for each. Manual evidence review identifies an additional dependency gap for the last release despite its structurally complete packet.

| Release | Release-note date | Exact SHA | Work item | Retained changes |
| --- | --- | --- | --- | --- |
| `1.99.1` | 2026-10-15 | `a85a51e837f8e4cccaacb5519a30b255285ea4ec` | `github-6aa08be3dc8170c4205f` | 15 modified, 711 unchanged |
| `1.100.0` | 2026-10-22 | `ab6c48b676bfdc439cb128f0a36ba920a6cc10d2` | `github-07f67ad5af2e72a51938` | 36 modified, 690 unchanged |
| `1.101.0` | 2026-10-22 | `f1092bb9c89377399bed184a786fde81bfa8b901` | `github-68fe35a7162ca6bf6502` | 4 modified, 722 unchanged |

## 1.99.1

- Austrian/German Pay Monthly, Pay in 30 and product-list content adds PayPal attribution and credit warnings; disclosures and terms-link labels are revised. PayIn1 now conditionally renders `creditWarning` and adds the `pay-in-1` disclosure class.
- Tile removes its explicit interpolated `aria-label` and removes `aria-hidden` from the visible text column. This changes authored accessible-name semantics, not a verified screen-reader outcome; click behavior is unchanged.
- US Apple-wallet content replaces broad shopping wording with single-purchase in-store/online wording, explicitly mentions adding an approved single-use virtual card to a digital wallet, and revises disclosure links. This is content evidence, not a new Apple Pay merchant API.
- Package diff is version-only; no dependency migration established. The changed shared `_content.scss` is policy-excluded, so visual styling is not fully evidenced. Recommend delta with that boundary explicit.

## 1.100.0

- Inline `data-pp-onclick`, `data-pp-onapply` and `data-pp-onrender` attribute values are captured in new options, passed through the message controller, and copied into `trackingDetails.INLINE_EXPRESSION*` fields. Existing `new Function(nodeValue)` construction predates this delta; do not call it newly introduced. Raw handler strings in tracking metadata warrant explicit mention; downstream transmission/storage has not been traced in this review.
- UK message/modal content adds a GBP15 first-use Pay Later cashback campaign and PayIn1/ShortTerm conditionally render `cashbackOffer`. Headline text says GBP100+ while detailed copy says over GBP100. Retain that source discrepancy; do not infer actual campaign eligibility or resolve it without terms evidence.
- French disclosure link text/accessibility labels change. US Pay Monthly content expands the visible excluded-state list with AZ, MN, NJ and OR, but the accompanying screen-reader text omits Minnesota. Preserve this authored inconsistency; no current eligibility or legal determination follows from historical copy.
- Retained UK mutation/CSS paths also change; modal `_content.scss` and ShortTerm `styles.scss` remain policy-excluded. No package dependency migration established. Recommend delta with complete changed implementation/content and affected prior code read during ingestion.

## 1.101.0

- TikTok PayLater content adds spending-power and autopay-method sections and revises disclosures. Spending-power copy explicitly describes an estimate, not a guaranteed credit line; autopay copy describes PayPal-account repayment-method management, not a merchant-facing editing API.
- ShortTerm conditionally passes those sections to newly imported `InfoSection`. Its implementation is absent from the snapshot, so the retained caller establishes wiring, not the new component's rendering/accessibility behavior.
- Before ingestion, recommend approved exact-SHA supplements for `src/components/modal/v2/parts/InfoSection.jsx`, `src/components/modal/v2/styles/components/_info-section.scss`, and `src/components/modal/v2/styles/index.scss` at `f1092bb9c89377399bed184a786fde81bfa8b901`. Do not alter the accepted snapshot or infer missing implementation. Reassess delta after reading the supplement; full mode alone cannot repair missing evidence.

## Verification and collection execution

- Each new snapshot retains 726 files. Verified all 2,904 prior/current file sizes, SHA-256 hashes and Git blob IDs across the four snapshots. No new collection errors; no unclassified upstream changes in the generated packets.
- Offline GitHub validation reports the same 12 existing unrelated errors across six other repositories, with three pending items; none belongs to Messaging Components.
- Collection initially spent several minutes sequentially hydrating blobs through `git cat-file --batch-check`. Reused 726 accepted prior raw blobs in the isolated temporary clone after verifying SHA-256 and Git blob identity. Only the temporary Git cache was populated; raw files, registry policy and collector code were not changed.
- This is pre-ingest findings review, not a claim that every assigned raw file or the entire upstream repository has been read. No upstream build, browser, screen-reader, payment or hosted-rollout test was run.

## Approved 1.101.0 supplement: collected and reviewed

After the preceding review, the user approved only the three specified files at exact accepted SHA `f1092bb9c89377399bed184a786fde81bfa8b901`. All were collected and read completely, along with their manifest, canonical attachment, the TikTok content file and the retained modal style consumer.

- Supplement: `raw/github/paypal/paypal-messaging-components/supplements/2026-10-25-f1092bb-8f31dd39/manifest.json`.
- Canonical attachment: `tracking/github/repos/paypal/paypal-messaging-components/evidence-attachments/github-68fe35a7162ca6bf6502/attachment.json`, linked through the pending work item's `evidence_attachments`. Future approval/ingestion revalidates the attachment and adds all three files plus the manifests to required reading.
- `InfoSection.jsx` renders a wrapper, an `h2` headline and one `p` per array element. A non-array `paragraphs` value produces no paragraphs. Paragraph values use `dangerouslySetInnerHTML`; no sanitization occurs within this component. This is a content-trust boundary, not proof of an exploitable vulnerability or arbitrary merchant-supplied HTML support.
- The existing retained ShortTerm caller renders spending-power/autopay sections only when their respective content objects exist, passing headline and paragraphs to `InfoSection`. The collected TikTok content describes a spending estimate rather than a guarantee/credit line, and repayment-method management inside the buyer's PayPal account. It establishes no merchant editing API or new generic checkout integration.
- `_info-section.scss` specifies left alignment, 12px vertical wrapper margins, 24px right padding, tablet-mixin left padding of 37px, 18px/24px bold headings and 14px/20px paragraphs. Text switches to the white color token under `.darkMode`. Token values and the tablet breakpoint are not established by this three-file supplement.
- `styles/index.scss` includes `components/info-section`; retained `Modal.jsx` imports that entry and inserts `styles._getCss()`. This establishes authored style wiring, not a compiled/hosted bundle or verified visual/screen-reader outcome.
- Original snapshot and registry policy are unchanged. Work item remains `awaiting_approval`; no ingestion, canonical wiki edits, upstream build/browser/payment execution, commit or push.

Next: seek approval for serial delta ingestion `1.99.1 -> 1.100.0 -> 1.101.0`, retaining all earlier history and including the linked supplement in the last item. The specific missing-component gap above is resolved; other previously recorded policy exclusions and runtime limits remain explicit.
