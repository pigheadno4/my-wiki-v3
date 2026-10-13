---
title: "Adyen local Terminal API protection with libraries"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/local/protect-with-library"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect-with-library/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, local-communications, encryption, certificate-validation]
---

## Overview

This Adyen Docs webpage describes GitHub libraries for protecting **local** Terminal API communication between a merchant POS app and an Adyen payment terminal. It identifies two protections: validation of the terminal certificate to authenticate the terminal and encryption of POS-terminal messages. It is a setup guide and code-sample collection, not evidence that any particular deployment, library version, or sample has passed a production security review. The Terminal API libraries here are separate from Adyen's deprecated classic libraries.

## Key takeaways

- The page lists .NET, Terminal API for iOS, Java, and Node library routes. The .NET, Java, and Node sections show local request-service setup, encryption credential/key inputs, and sending a request. The iOS section shows shared-key derivation and message encryption/decryption, with the POS sending the encrypted message; do not infer that its snippet performs the transport step. These are webpage examples, not pinned GitHub release or SDK-version evidence.
- Before using a library, the relevant preparation lists library installation, Adyen's root certificate, and a shared key. The key identifier, passphrase, and version must match the values in Customer Area. The Node example configures a certificate path and terminal IP endpoint; the Java example configures a trust store, SSL context, and hostname verifier; the .NET example selects Test or Live and a local endpoint. Exact sample values and API calls need verification against the chosen library version and environment.
- The page allows local communication without encryption **only on test while implementing encryption**. Its crypto-error troubleshooting points to mismatched shared-key values; its SSL-connection troubleshooting identifies an incorrectly installed Adyen root certificate as a possible cause. Neither troubleshooting note proves that all other causes are excluded.

## Detail locators

- Scope, protections, classic-library deprecation, and listed GitHub library links: `# Protect with a library` and `## Encrypt communications`, raw lines 15–39. The linked repositories are navigation, not version-qualified evidence in this entry.
- .NET setup and encrypted request: `### Tab: .NET`, raw lines 41–105. iOS key derivation/encrypt/decrypt and separate send step: `### Tab: iOS`, lines 107–151. Java trust/key/service setup: `### Tab: Java`, lines 153–230. Node certificate/key/local-service setup: `### Tab: Node`, lines 232–298.
- Customer Area shared-key lookup and longer code samples: `## Full code samples`, raw lines 300–453. The examples contain placeholders, test endpoints, and unpinned library syntax; use the selected library's current documentation for implementation review.
- Shared-key crypto errors and possible root-certificate SSL issue: `## Troubleshooting`, raw lines 455–493.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — local Terminal API communication and its security boundary; this website guide is separate from exact-commit GitHub Postman examples and independently versioned SDK history.
- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-local]] — local architecture and live-versus-test security context.
- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-local-protect]] — merchant-written protection path.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/protect-with-library/2026-09-15|Adyen Docs: Protect with a library (2026-09-15 snapshot)]]
