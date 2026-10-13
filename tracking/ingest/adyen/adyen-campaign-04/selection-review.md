# Adyen C04 selection and execution plan

Status: **COMPLETE — execution approved and validated**.
Prepared 2026-10-13 after C03 commit `b47b8a439a2c398de88ee66196995db0bb7449a1` was pushed; exact remote main SHA verified.

50 previously unreferenced English General Docs snapshots. Metadata selection covers all available in-person design, get-started and support paths, then core payment lifecycle/testing routes to fill 50 slots. Five orientation hubs run first; remaining pages are largest-first. Total metadata words: **93,040** (including code/navigation). All selected pages are below 10,000 metadata words. Counts inform scheduling only.

Baseline: **164 source summaries = 150 website + 14 GitHub**. Existing Adyen Terminal API/SDK concepts must be audited for version/actor boundaries before any concept promotion; no new concepts preselected. Firmware release notes, NFC-tag guide, mobile SDK expansion, device manuals, advanced features, remaining online/risk oversized guides, API Explorer and GitHub ingestion are deferred, not assigned raw_reference or semantically approved. No collection/refresh.

Use the existing ten shared rolling child slots with gpt-6-sol medium workers and separate high independent reviewers; coordinator-only repository writes. Full individual raw read, 3–5 located quotes, full first review, at most three attempts and bounded corrections. Exact execution contract: [dispatch-contract.md](dispatch-contract.md). Aggregate catalogs/counts/logs once at close. 100 fixed retrieval answers and three fixed coordinator full-read exemplars; all-source structural and touched typed validation. No new framework/rules/validators.

## Fixed exemplar jobs

- `docs-point-of-sale`.
- `docs-point-of-sale-design-your-integration-network-and-connectivity-wi-fi-profiles`.
- `docs-point-of-sale-offline-payment`.

## Preparation checks

- [x] C03 complete and pushed, exact remote SHA verified.
- [x] 50 unique jobs, canonical URLs, latest raw pins and absent source targets/ownership.
- [x] Every selected raw hash matches; English frontmatter and metadata size verified.
- [x] Three distinct exemplar jobs in the exact manifest.
- [x] Explicit approval of manifest and provider authorization before execution.

## Exact selection

| # | Path | Metadata words | Raw snapshot |
| --- | --- | ---: | --- |
| 1 | point-of-sale | 565 | [[raw/adyen/docs/point-of-sale/2026-09-15]] |
| 2 | point-of-sale/get-started | 230 | [[raw/adyen/docs/point-of-sale/get-started/2026-09-15]] |
| 3 | point-of-sale/design-your-integration | 619 | [[raw/adyen/docs/point-of-sale/design-your-integration/2026-09-15]] |
| 4 | point-of-sale/design-your-integration/terminal-api | 1324 | [[raw/adyen/docs/point-of-sale/design-your-integration/terminal-api/2026-09-15]] |
| 5 | point-of-sale/design-your-integration/choose-your-architecture | 1371 | [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/2026-09-15]] |
| 6 | point-of-sale/design-your-integration/network-and-connectivity/wi-fi-profiles | 7546 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/wi-fi-profiles/2026-09-15]] |
| 7 | point-of-sale/design-your-integration/determine-account-structure/automate-store-management | 7025 | [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/automate-store-management/2026-09-15]] |
| 8 | point-of-sale/pre-authorisation | 5897 | [[raw/adyen/docs/point-of-sale/pre-authorisation/2026-09-15]] |
| 9 | point-of-sale/design-your-integration/choose-your-architecture/local/protect | 5175 | [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect/2026-09-15]] |
| 10 | point-of-sale/capturing-payments | 4391 | [[raw/adyen/docs/point-of-sale/capturing-payments/2026-09-15]] |
| 11 | point-of-sale/design-your-integration/choose-your-architecture/local | 3536 | [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/2026-09-15]] |
| 12 | point-of-sale/card-acquisition | 3267 | [[raw/adyen/docs/point-of-sale/card-acquisition/2026-09-15]] |
| 13 | point-of-sale/design-your-integration/notifications/display-notifications | 3224 | [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/2026-09-15]] |
| 14 | point-of-sale/offline-payment | 3095 | [[raw/adyen/docs/point-of-sale/offline-payment/2026-09-15]] |
| 15 | point-of-sale/design-your-integration/choose-your-architecture/cloud | 3064 | [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/cloud/2026-09-15]] |
| 16 | point-of-sale/design-your-integration/determine-account-structure/configure-features | 2913 | [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/configure-features/2026-09-15]] |
| 17 | point-of-sale/error-scenarios | 2834 | [[raw/adyen/docs/point-of-sale/error-scenarios/2026-09-15]] |
| 18 | point-of-sale/what-we-support/payment-methods | 2512 | [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/2026-09-15]] |
| 19 | point-of-sale/design-your-integration/network-and-connectivity/cellular-failover | 2448 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/2026-09-15]] |
| 20 | point-of-sale/design-your-integration/choose-your-architecture/local/protect-with-library | 2131 | [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect-with-library/2026-09-15]] |
| 21 | point-of-sale/recurring-payments | 2005 | [[raw/adyen/docs/point-of-sale/recurring-payments/2026-09-15]] |
| 22 | point-of-sale/add-data | 1898 | [[raw/adyen/docs/point-of-sale/add-data/2026-09-15]] |
| 23 | point-of-sale/design-your-integration/network-and-connectivity/network-configuration | 1898 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/network-configuration/2026-09-15]] |
| 24 | point-of-sale/cardholder-verification-methods | 1855 | [[raw/adyen/docs/point-of-sale/cardholder-verification-methods/2026-09-15]] |
| 25 | point-of-sale/design-your-integration/notifications/event-notifications | 1836 | [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/event-notifications/2026-09-15]] |
| 26 | point-of-sale/partial-authorizations | 1754 | [[raw/adyen/docs/point-of-sale/partial-authorizations/2026-09-15]] |
| 27 | point-of-sale/what-we-support/select-your-terminals | 1717 | [[raw/adyen/docs/point-of-sale/what-we-support/select-your-terminals/2026-09-15]] |
| 28 | point-of-sale/get-started/tapi-checklist | 1541 | [[raw/adyen/docs/point-of-sale/get-started/tapi-checklist/2026-09-15]] |
| 29 | point-of-sale/design-your-integration/determine-account-structure | 1445 | [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/2026-09-15]] |
| 30 | point-of-sale/testing-pos-payments | 1384 | [[raw/adyen/docs/point-of-sale/testing-pos-payments/2026-09-15]] |
| 31 | point-of-sale/design-your-integration/network-and-connectivity/set-up-beacons | 1245 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/set-up-beacons/2026-09-15]] |
| 32 | point-of-sale/get-started/go-live-tapi | 1239 | [[raw/adyen/docs/point-of-sale/get-started/go-live-tapi/2026-09-15]] |
| 33 | point-of-sale/design-your-integration/network-and-connectivity/bluetooth-pan | 1074 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bluetooth-pan/2026-09-15]] |
| 34 | point-of-sale/risk-management-pos | 1023 | [[raw/adyen/docs/point-of-sale/risk-management-pos/2026-09-15]] |
| 35 | point-of-sale/design-your-integration/network-and-connectivity/bt-base-station | 998 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bt-base-station/2026-09-15]] |
| 36 | point-of-sale/design-your-integration/notifications/standard-notifications | 854 | [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/standard-notifications/2026-09-15]] |
| 37 | point-of-sale/design-your-integration/notifications/display-notifications/tender-state-reference-sheet | 815 | [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/display-notifications/tender-state-reference-sheet/2026-09-15]] |
| 38 | point-of-sale/design-your-integration/network-and-connectivity/end-of-3g | 727 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/end-of-3g/2026-09-15]] |
| 39 | point-of-sale/what-we-support/supported-languages | 649 | [[raw/adyen/docs/point-of-sale/what-we-support/supported-languages/2026-09-15]] |
| 40 | point-of-sale/what-we-support/payment-methods/add-payment-methods | 533 | [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/add-payment-methods/2026-09-15]] |
| 41 | point-of-sale/what-we-support/solutions | 502 | [[raw/adyen/docs/point-of-sale/what-we-support/solutions/2026-09-15]] |
| 42 | point-of-sale/what-we-support/payment-methods/manage-payment-methods | 488 | [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/manage-payment-methods/2026-09-15]] |
| 43 | point-of-sale/design-your-integration/network-and-connectivity/networking-issues | 452 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/networking-issues/2026-09-15]] |
| 44 | point-of-sale/design-your-integration/terminal-api/get-the-terminal-id | 428 | [[raw/adyen/docs/point-of-sale/design-your-integration/terminal-api/get-the-terminal-id/2026-09-15]] |
| 45 | point-of-sale/basic-tapi-integration | 361 | [[raw/adyen/docs/point-of-sale/basic-tapi-integration/2026-09-15]] |
| 46 | point-of-sale/diagnostics | 267 | [[raw/adyen/docs/point-of-sale/diagnostics/2026-09-15]] |
| 47 | point-of-sale/design-your-integration/notifications | 264 | [[raw/adyen/docs/point-of-sale/design-your-integration/notifications/2026-09-15]] |
| 48 | point-of-sale/reconciling-totals | 244 | [[raw/adyen/docs/point-of-sale/reconciling-totals/2026-09-15]] |
| 49 | point-of-sale/what-we-support | 227 | [[raw/adyen/docs/point-of-sale/what-we-support/2026-09-15]] |
| 50 | point-of-sale/design-your-integration/network-and-connectivity | 150 | [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/2026-09-15]] |

User approval activated this exact campaign. All 50 sources are promoted, reviews and closure checks retained. No commit or push.
