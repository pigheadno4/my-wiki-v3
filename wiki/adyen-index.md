# Adyen Index

> Adyen-specific catalog. Cross-cutting pages are in the root [[index]].

Operations history: [[adyen-log]]

## Company

- [[adyen]]

## Sources

- [[source-github-adyen-postman]] — exact-commit Postman baseline for Checkout v72, Recurring v68, BIN Lookup v54, Test Card v1, and 82 Terminal API examples (github-repo, 2026-08-12)
- [[changelog-github-adyen-postman]] — commit-qualified Adyen Postman collection history beginning at `default-branch@ecb2907` (github-repo, 2026-08-12)
- [[source-github-adyen-web]] — cumulative Adyen Web implementation history through `@adyen/adyen-web@6.42.0`: Drop-in, Components, Sessions, cards, 3DS2, payment-list analytics, address validation, accessibility, and Fastlane adapter (github-repo, 2026-08-09)
- [[changelog-github-adyen-web]] — package-qualified Adyen Web release ledger from `6.41.0` through `6.42.0` (github-repo, 2026-08-09)
- [[source-github-adyen-ios]] — cumulative `adyen-ios@5.25.1` native baseline: Drop-in, Session, Components, cards, actions, encryption, Apple Pay, and app handoffs (github-repo, 2026-08-01)
- [[changelog-github-adyen-ios]] — package-qualified Adyen iOS release ledger beginning at `5.25.1` (github-repo, 2026-08-01)
- [[source-github-adyen-android]] — cumulative `adyen-android@5.20.0` native baseline: Drop-in, Sessions, View and Compose Components, cards, actions, encryption, and delegated SDKs (github-repo, 2026-08-01)
- [[changelog-github-adyen-android]] — package-qualified Adyen Android release ledger beginning at `5.20.0` (github-repo, 2026-08-01)
- [[source-github-adyen-react-native]] — cumulative `@adyen/react-native@2.12.0` wrapper baseline: Drop-in, Components, Sessions, embedded CardView, wallets, actions, and native dependency boundaries (github-repo, 2026-08-02)
- [[changelog-github-adyen-react-native]] — package-qualified Adyen React Native release ledger beginning at `2.12.0` (github-repo, 2026-08-02)
- [[source-github-adyen-node-api-library]] — cumulative `@adyen/api-library@32.0.0` server baseline: Checkout API v72, transport, notifications, recurring operations, and Cloud Device API v1 (github-repo, 2026-08-02)
- [[changelog-github-adyen-node-api-library]] — package-qualified Adyen Node.js API Library release ledger beginning at `32.0.0` (github-repo, 2026-08-02)

## Concepts

- [[adyen-terminal-api]] — Nexo Terminal API message architecture, in-person flows, and Checkout/Management API boundaries
- [[adyen-ios-sdk]] — native iOS architecture, integration modes, payment and server boundaries, and delegated dependencies
- [[adyen-android-sdk]] — native Android architecture, integration modes, View and Compose surfaces, server boundaries, and delegated dependencies
- [[adyen-react-native-sdk]] — React Native wrapper architecture, flows, platform setup, and native SDK boundaries
- [[adyen-node-api-library]] — Node.js server SDK, Checkout API v72, Cloud Device, transport, and evidence boundaries

## Cross-cutting concepts

- [[co-badged-cards]] — includes version-qualified Adyen Web and Android dual-brand implementation evidence
- [[recurring-payments]] — includes the Checkout recurring endpoint preference and legacy Recurring API boundary

## Operations

- [[adyen-log]] — provider-specific collection and ingest history
- [GitHub collection status](../tracking/github/status.md)
