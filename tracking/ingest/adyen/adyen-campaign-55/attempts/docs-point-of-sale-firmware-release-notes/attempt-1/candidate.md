---
title: "Adyen POS release notes: terminal software and mobile solutions"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/firmware-release-notes"
raw_files:
  - "adyen/docs/point-of-sale/firmware-release-notes/2026-09-15.md"
tags: [adyen, point-of-sale, release-notes, terminal-software, mobile-pos]
---

## Overview

Adyen's 2026-09-15 snapshot of chronological release notes covers physical **Terminal software** (Verifone Engage and Android terminals), **Android SDK on mobile**, **iOS SDK on mobile**, and the **Android Payments app**. It records dated versions, patches, new and changed behavior, fixes, breaking changes, deprecations, expiry/removal or support dates, and known issues. Use the dated release entry and applicable product/model rather than a version number alone. See [[adyen]], [[adyen-terminal-management]], [[adyen-payment-terminals]], and [[adyen-mobile-pos]].

## Key takeaways

- For manually updated physical terminals, the page points to Android LTS v1.133, v1.130, or v1.126 and Verifone Engage v1.120, with release-schedule guidance in the separate update guide. It calls 1.120 the final **major** Engage update due to PCI PTS 6 transition, while 1.120 is maintained with patches until 2030; 1.120.17 cannot be downgraded to an earlier Engage patch. This is a release-note snapshot, not evidence of a device's installed version or eligibility. See raw lines 20–35, 1019–1023 and 1133–1179.
- Availability and issue status are patch/model-specific. For example, terminal 1.127 is unavailable for S1U2 and records an Adyen-app unassignment issue (lines 558–572); 1.126.3–1.126.5 are unavailable for S1U2 and record the same issue, with a 1.126.6 fix (lines 594–665). The 1.120 entry similarly records S1U2 patch exclusions and later Android/Engage patch fixes (lines 1019–1179). Do not read a later fix as applying to every earlier patch.
- The mobile categories have separate lifecycles and implementation changes. The 2026 iOS and Android SDK entries state version-specific expiry/removal dates, while Android Payments app entries state support expiry. Examples of migration gates include Android SDK 2.14.0's dataSync foreground-service Play declaration (lines 513–525), iOS SDK 3.18.0's iOS 18.4 and device-passcode requirements for SDK functionality (lines 203–229), and Android Payments app 1.0.0's App Links replacement for deprecated deep links (lines 784–799). Consult the entry for the version actually integrated.
- The release notes include outcome-sensitive defects and fixes. Terminal 1.126.8 fixes a case where capture occurred but the successful payment response was missing (lines 594–608). Android SDK 2.18.0 and iOS SDK 3.16.0 introduce beta recent-transaction outcome queries with Adyen account-manager contact (lines 193–201 and 352–365). These entries do not confirm a particular payment's outcome; use the appropriate transaction-status workflow.
- Historical known issues must remain tied to the affected release. Examples include pre-1.103 Store-and-Forward transactions failing after later updates and being discarded after two months in 2024 entries, with later fixes recorded (lines 2224–2253 and 2328–2330), and the 2020 UX/Engage security-patch split (lines 4648–4657 and 4763–4765).

## Detail locators

- **Current snapshot entry heads and support clocks:** lines 43–260 (September–June 2026); 269–694 (June–January 2026).
- **Engage final-major/LTS patch sequence:** lines 1019–1179; **Android LTS/model caveats:** lines 139–145, 293–350, 594–669.
- **Mobile SDK/API migration and reader firmware history:** lines 160–229, 513–555, 1719–1794, 2628–2691, 2726–2765.
- **Older terminal software changes, exceptions, and known issues:** lines 1805–2253, 2272–2607, 2693–2815, 2950–3120, 3121–4765.
- **Release-update strategy and device state:** follow [[source-adyen-docs-point-of-sale-release-updating]] and [[source-adyen-docs-point-of-sale-release-updating-manual-deployment]] separately. The page metadata's 2025-11-27 `last_modified` predates its 2026 entries (raw lines 1–14, 43–65); treat the dated release entries as snapshot content, not that metadata field as a reliable latest-entry cutoff.

## Related

- [[adyen-terminal-management]]
- [[adyen-payment-terminals]]
- [[adyen-mobile-pos]]
- [[source-adyen-docs-point-of-sale-release-updating]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/firmware-release-notes/2026-09-15|Adyen POS release notes, 2026-09-15 capture]]
