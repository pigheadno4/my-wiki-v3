---
title: "Stripe Terminal: Example Applications"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-example-applications-2025.md"
tags: [stripe, terminal, in-person, example, github, simulated-reader, quickstart, ios, android, javascript, react-native]
---

## Stripe Terminal: Example Applications

Official example apps for all Terminal SDKs, plus a shared Sinatra backend.

## Key Takeaways

### Example backend

- Repo: `github.com/stripe/example-terminal-backend` (Sinatra-based)
- Run locally or deploy to Render (free account)
- Authenticates Terminal SDK and finalizes payments — shared across all example apps

### Example app repos

| SDK | Repo | Setup notes |
| --- | --- | --- |
| JavaScript | `github.com/stripe/stripe-terminal-js-demo` | `npm run start`; enter backend URL in running app |
| iOS | `github.com/stripe/stripe-terminal-ios` | Open `Example/Example.xcworkspace`; set URL in `AppDelegate.swift` |
| Android | `github.com/stripe/stripe-terminal-android` | Import `Example` into Android Studio; set URL in `gradle.properties` |
| React Native | `github.com/stripe/stripe-terminal-react-native` | Expo CLI; copy `.env.example` → `.env`; `npx expo run:android/ios` |

### Simulated reader activation

- JavaScript: select **Use simulator**
- iOS / Android / React Native: select **Simulated**

### iOS Simulator location note

To run the iOS example in the Xcode Simulator, enable a simulated location via **Debug → Simulate Location**. Terminal uses device location for reader configuration.

### Payment collection sequence (examples)

1. Create payment (SDK collects payment method)
2. Collect payment method (simulated card received)
3. Process and capture (app + backend finalize)

Each example includes an **event log** to trace the full SDK interaction sequence.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-example-applications-2025]] — verbatim example applications guide
