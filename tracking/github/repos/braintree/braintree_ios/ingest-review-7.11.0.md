# Braintree iOS 7.11.0 ingest review

- Item `github-a67f34a9fcf4438cc133`; delta from 7.10.0; SHA `2a9aa1e20b1d066cb97c66af3e2ccd7f17e90fc0`.
- User explicitly approved focused reading for 7.11.0--7.13.0. Complete changed files, patch, notes and cumulative wiki context read; manifests and unchanged history mechanically verified. 291 files in both snapshots passed SHA-256; prior changelog history remains exact. No packet gaps/unclassified changes. Binary internals and excluded Xcode projects not reviewed.
- Delta justified by bounded dependency-packaging repair with unchanged DataCollector source, not an unbounded security-behavior claim. Release-notes signing-fix claim is distinguished from binary validation.

## Grounding quotes

In `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/files/`:
- `Package.swift`, dependencies: `.package(url: "https://github.com/paypal/paypal-risk-ios.git", exact: "5.6.0")`
- `Braintree.podspec`, DataCollector: `s.dependency "PayPalRisk", '5.6.0'`
- `Sources/BraintreeDataCollector/BTDataCollector.swift`: `import PPRiskMagnes`
- Release notes `raw/github/braintree/braintree_ios/releases/braintree-ios/7.11.0/2026-10-04/release-notes.md`: `Run `carthage update --use-xcframeworks` after upgrading`

## Cycle
- [x] Evidence and grounding
- [x] Concept audit/update
- [x] Source and changelog
- [x] Company/count and concept citations (272 unchanged)
- [x] Comparison/contradiction disposition (no cross-company comparison; historical risk packaging preserved)
- [x] Index/log
- [x] Validation and completion (five schema pages pass; item ingested)
