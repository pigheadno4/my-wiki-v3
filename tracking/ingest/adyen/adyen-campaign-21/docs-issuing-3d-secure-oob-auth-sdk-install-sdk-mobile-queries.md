# Retrieval checks — docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile

## Q1 — Purpose and prerequisites

What mobile SDK does Adyen describe for Issuing OOB cardholder authentication, and what must the app/device satisfy? The captured guide describes a client-side Authentication SDK with device-binding possession plus knowledge or inherence; it can check SCA eligibility, register a device and authenticate online card transactions with 3D Secure (raw lines 19-27). It supports native Android Kotlin/Java and iOS Swift (raw lines 37-42). Android target API 21+ differs from authentication runtime API 26+ and Google Play Services is required (raw lines 46-50); iOS requires iOS 14+, Xcode 13.2+, Swift 5.5+, and a TestFlight/App Store release build for LIVE (raw lines 52-57). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] → [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile/2026-09-15]].

## Q2 — Scope and outcome boundary

Does the Issuing URL prove Issuing-only eligibility, or does installing the SDK prove completed SCA/payment authorization? No. The requirements table explicitly names an Adyen for Platforms integration (raw line 35), and the guide links registration and device management as later steps (raw lines 98-110). Android `0.2.1` and iOS minimum `1.0.0` are dated installation examples (raw lines 65-96). The guide contains no transaction outcome or card-payment authorization evidence. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] → [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile/2026-09-15]].
