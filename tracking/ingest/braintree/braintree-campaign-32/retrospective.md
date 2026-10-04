# Braintree C32 timing and bounded optimization

Twenty sources approved; first pass 16/20 (80%, versus C31 70%). Twenty initial full reviews and four targeted reviews; no repeated full review. Queries 40/40 and typed validation 26/26. Runtime **43m41s**, versus C31 **44m21s**: only **40 seconds / 1.5% faster**, not a substantial speedup. Average 2m11.1s per page versus 2m13.1s.

Primary raw volume increased from 1,827 to 2,477 lines (+35.6%). Accepted source words decreased from 13,662 to 12,437 (-9.0%); average 622 versus 683 words. Five query groups replaced ten while retaining forty questions. Different content, new concept ownership and supporting authority reads prevent attributing the result to one change or treating this as a controlled A/B.

| Observed milestone | UTC | Elapsed from 02:40:39 |
| --- | --- | --- |
| First five worker handoffs complete | 02:44:42 | 4m03s |
| All twenty initial worker handoffs complete | 03:12:24 | 31m45s |
| Last independent review handoff | 03:18:53 | 38m14s |
| Final promotion/company/source catalogs observed ready | 03:19:58 | 39m19s |
| Last query analysis ended, auditor-reported | 03:21:14 | 40m35s |
| Last query report received and inspected by | 03:22:55 | 42m16s |
| Shared logs, mechanical checks and runtime close | 03:24:20 | **43m41s** |

Windows overlap and must not be added. Initial worker completion was 53 seconds faster than C31; final review completion was 2m08s later. Query analysis finished 2m34s earlier. The tail from catalogs ready to close fell from 7m14s to 4m22s, but the later review finish offset most of this saving. Last report analysis-to-receipt was 1m41s; inspectable artifact handoff and coordinator handling remain real costs, not just model reading.

Four bounded corrections:

- Cryptography reciprocal label lost the destination-dependent qualification by calling the feature optional.
- Android omitted the literal unverified android:scheme="https://" sample boundary.
- PGP called displayed key identity an authority and marked a behavioral supporting link as factual without its raw provenance; the smallest fix narrowed identity and made the link navigation-only.
- Shared Vault converted incomplete "or cloned via." into a universal cloning prohibition and inferred a missing link. The correction preserved the fragment without reconstructing its absent qualification.

No central misunderstanding required another full review. These failures concern modal scope, abnormal examples, provenance and incomplete raw text, not missing routine schemas. Two genuine concept gaps were independently reviewed once and promoted centrally. One worker initially failed to locate the trusted order from its default directory; the existing absolute checkout path resolved it without new machinery. A catalog patch's hunk order and one final newline were corrected mechanically; no content repair infrastructure was added.

Small next-round recommendation, requiring approval: **group query pages by dispatch/queue order rather than topic family**, retaining four pages/eight questions per group and the same evidence/link checks. Current B waited for late Shared Vault correction even though its other three pages were ready. Earlier four-page groups could start sooner and overlap more worker/reviewer time. Do not change this completed campaign's approved groups or add tests, roles, fields, classifiers or schedulers.

Keep prevention inside the existing worker bounded check: retain destination-dependent modality, do not infer absent qualifiers from truncated raw, distinguish name/identity from trust authority, and use navigation-only links unless supporting factual provenance is declared. Do not create another invariant registry or reread every related page. Avoid repeating the same outcome/snapshot caveat in several sections, but never rewrite accepted sources merely to shorten them.

The current result improves first-pass stability and audit overlap, not overall throughput materially. Keep the existing five rolling child slots and one close. No automatic next campaign, collection, commit or push.

Reports/status were observed ready by 03:25:47 UTC: post-close documentation 1m27s, initialization-to-report-ready 45m08s. Final chat follows that milestone.
