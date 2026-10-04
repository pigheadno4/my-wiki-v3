# C31 fixed query audit — Group J — 4/4 PASS

Scope: `lpm-grabpay` + `lpm-satispay`, the four fixed questions assigned to group J (`selection-review.md:42-54`). Both promoted jobs are approved (`jobs.json:307-342`). Repository remained read-only; the only write is this external handoff.

## Q1 — GrabPay exact route — PASS

**Object/action match:** locate the unversioned Braintree Local Payment Methods **GrabPay** method notice and descend to its pinned website raw.

**Exact route:** `wiki/index.md:11` → `wiki/braintree-index.md:399` → `wiki/concepts/braintree-payment-methods.md:26` → `wiki/sources/braintree/source-braintree-local-payment-methods-grabpay.md:2,6-8,42-44` → `raw/braintree/docs/guides/local-payment-methods/grabpay-2026-09-16.md`. The provider catalog also exposes the exact source directly at `wiki/braintree-index.md:126`. Source canonical/raw provenance (`source:6-8`) matches the raw URL/title/slug and GrabPay heading (`raw:1,6-8,14`). This dated website snapshot is not exact-SHA SDK/package evidence.

## Q2 — GrabPay method-specific applicability — PASS

The complete 26-line raw says GrabPay is in limited release, is available only to buyers and sellers in Singapore, and requires interested merchants to contact their Customer Success Manager (`raw:20-21`). Its applicability row separately identifies payment type `grabpay`, buyer country `Singapore`, seller countries `Global`, currency `SGD`, and customer limits `0.01 SGD`–`5,000 SGD` (`raw:23-25`). The Singapore-only seller prose conflicts with the `Global` seller table value; neither is selected as controlling. This short notice contains no SDK/platform, Sandbox/Production, initiation, notification, authorization, settlement or funding flow, so none is inferred (`source:18-28,32-34`).

## Q3 — Satispay exact route — PASS

**Object/action match:** locate the unversioned Braintree Local Payment Methods **Satispay** method notice and descend to its pinned website raw.

**Exact route:** `wiki/index.md:11` → `wiki/braintree-index.md:399` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-local-payment-methods-satispay.md:2,6-8,49-51` → `raw/braintree/docs/guides/local-payment-methods/satispay-2026-09-16.md`. The provider catalog also exposes the exact source directly at `wiki/braintree-index.md:127`. Source canonical/raw provenance (`source:6-8`) matches the raw URL/title/slug and Satispay heading (`raw:1,6-8,14`). This dated website snapshot is not exact-SHA SDK/package evidence.

## Q4 — Satispay method-specific applicability/redirect — PASS

The complete 26-line raw says Satispay is in limited release and available only to buyers in Italy, then routes prospective integrations to the separate generic Local Payment Methods configuration guides (`raw:20-21`). Its applicability row identifies payment type `satispay`, buyer country `Italy`, the captured seller-country label `EEA+ CH+ UK`, currency `EUR`, and customer limits `0.01 EUR`–`99,999 EUR` (`raw:23-25`). The page does not define the plus signs, so the seller label is not expanded. The generic integration link is navigation, not a Satispay-specific flow: this notice provides no method-specific request, approval, token, webhook, capture, settlement or funding procedure and no SDK/platform/version or environment evidence (`source:18-28,32-47`).

## Integrity and bounded gap sweep

- The fixed scope is group J's two 26-line selected raws (`selection-review.md:35-36,54`). Recomputed SHA-256 values exactly match the manifest: GrabPay `1aed55e8ecc8427e59b89fe2a31a3155c861a36da607091685d2e51240f56523` (`manifest.json:161-168`); Satispay `32c9a56362b3dc89c9a9b0ebf9e0db509db99a6326ff7fb3c0c1ee6e5855d7dd` (`manifest.json:169-177`). Both selected raws and promoted sources were read completely.
- Each pinned raw path has exactly one `raw_files` reverse owner in `wiki/sources/`: its expected promoted source. The GrabPay and Satispay sources link `[[braintree-payment-methods]]` at source lines 39 and 38; the concept links back at lines 26 and 25. Their `Raw Sources` links resolve to the selected raws.
- One bounded filename/content sweep found the selected raws, discovery/reporting inventory mentions, and generic Android/iOS method-table mentions. None supplies a needed fact or resolves the GrabPay seller conflict. Satispay's source lists three configuration raws as navigation-only related references; because the question is answered by the method notice and no platform-specific behavior may be imported, none was promoted to evidence or fully read. No older version, sibling guide or additional raw was fully read.
- No broken route, missing locator, reverse-link gap or additional material conflict blocks these four answers.

Analysis end UTC: 2026-10-04T02:28:28Z
