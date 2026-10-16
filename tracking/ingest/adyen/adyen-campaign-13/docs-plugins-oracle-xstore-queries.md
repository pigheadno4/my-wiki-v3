# Fixed retrieval checks — Oracle Xstore

Q1. What integration does this overview describe, and what cannot be inferred?
- Expected: Adyen in-person POS integration with Oracle Xstore through EFTLink/OPI and Adyen terminals, plus a distinct Xstore Mobile Android-terminal app route. The page is a 2023-modified, 2026-captured orientation snapshot; it does not prove current version/device/merchant eligibility, an online checkout behavior, successful live payment, refund or settlement, nor child-guide detail.
- Raw locators: `raw/adyen/docs/plugins/oracle-xstore/2026-09-15.md:15-31`, `:52-56`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-oracle-xstore.md` → proposed `[[adyen-oracle-xstore]]`.

Q2. What version, device, feature and setup conditions are central?
- Expected: Xstore 15+ and EFTLink/OPI 17+; EFTLink maps transaction messages to terminals. Only S1E2L, S1F2 and S1F2L have Xstore Mobile marks in the dated table; V240m Plus is Brazil-only. Void is same-settlement-day only, and private-label card support is Bread Financial only. Setup requires a test account, Support-enabled OPI, stores, assigned/boarded terminals and additional APK/certificate/deployment steps for Xstore Mobile. The feature list is not a guarantee every feature works for every merchant/model.
- Raw locators: `raw/adyen/docs/plugins/oracle-xstore/2026-09-15.md:25-50`, `:52-101`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-oracle-xstore.md` → proposed `[[adyen-oracle-xstore]]`.
