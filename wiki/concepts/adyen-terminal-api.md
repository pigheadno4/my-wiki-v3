---
title: "Adyen Terminal API"
type: concept
category: technology
tags: [adyen, terminal-api, in-person-payments, point-of-sale, nexo]
---

## Adyen Terminal API

Adyen Terminal API is a Nexo-based message interface between a point-of-sale system and an Adyen payment terminal. A request wraps a message header containing protocol, class, category, type, sale ID, service ID, and terminal `POIID`, followed by category-specific payment, reversal, input, display, print, reconciliation, or stored-value data.

## Integration boundary

The Adyen website Terminal API checklist frames merchant implementation as test-account and terminal setup, architecture/payment-feature choice, test transactions and reconciliation, then a separate live-account application and signed contract. It says to consult Adyen before building a cloud integration and to inform Adyen if P2PE is required because different terminal software is supplied. These website setup gates are distinct from the exact-commit Postman request examples; the checklist does not establish account-specific enablement or current SDK-version behavior.


Cellular failover protects the terminal's Adyen-service internet path, subject to terminal/SIM configuration; it does not restore a cloud POS app's lost internet path or a local POS-to-terminal LAN link. Offline payment is a separate local-communications alternative with merchant liability for failed captures, chargebacks and disputes. The website's terminal models, firmware gates and dated cellular-fee language belong to the linked source and raw snapshot, not the versioned GitHub Terminal API examples.


The Adyen POS Device settings guide requires **Enable Terminal API** for both local and cloud Terminal API integrations, and **Enable WebSockets** for a cloud architecture. A terminal feature's availability in a Terminal API integration also depends on the POS app supporting it. These are website-documentation settings, distinct from the retained Postman repository baseline. [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-configure-features]]


For local communications, the merchant POS sends Terminal API requests over the LAN to an Adyen terminal, which routes shopper-completed transactions to Adyen and returns a synchronous response. Live local processing requires terminal-certificate validation against Adyen's root and shared-key protection between POS and terminal; the guide describes test as unenforced while building. Missing or timed-out payment responses call for a transaction-status check before operators risk a duplicate transaction. This website architecture guide is separate from the exact-commit Postman examples and independently versioned SDK implementations.


The retained Postman collection demonstrates Terminal API operations for terminal-present payments, refunds, shopper input, display and printing, reconciliation, card acquisition, tipping, instalments, and gift cards. It explicitly routes capture, recurring token charges, and authorization adjustments to Checkout API, and store or terminal-fleet administration to Management API.

Cloud transport requires an API key and a terminal ID. Merchant implementations must keep credentials private, generate unique request identities, correlate asynchronous or in-process operations, handle result and error fields, and avoid treating Postman test scripts as a production POS state machine.



## POS solution route

Adyen's dated in-person “Solutions” overview distinguishes POS-to-Adyen-terminal Terminal API integration from direct standalone-terminal transactions, mobile POS app paths, and partner-platform plugins. Its mobile path uses Mobile SDK for payment routing while retaining the Terminal API specification; its standalone and partner-plugin paths do not imply that a merchant POS app directly sends Terminal API messages. The overview is navigation and does not prove present-day device, SDK, market, or payment-method compatibility. [[source-adyen-docs-point-of-sale-what-we-support-solutions]]
## Payment and interaction patterns

Adyen's website basic-flow hub frames a viable integrated POS flow around payment, refund, in-progress cancellation, receipts, application details, and transaction-status recovery when a response is missing. It links PaymentRequest, ReversalRequest, AbortRequest, and TransactionStatusRequest as routes, but the hub does not specify all refund variants or the API ownership of optional industry features. Detailed behavior belongs to each linked operation/source and independently versioned implementation evidence.


For a configured POS signature check, the Terminal API transaction is already authorized when the signature screen appears; the terminal approves that screen even if the shopper cancels it. The merchant POS can use `CapturedSignature` from `PaymentResponse` for staff review; a declined check then requires refund, or cancellation of the authorization if a suitable capture delay was arranged. This website guide also has conflicting summary/detail wording about whether every contactless transaction above the CVM limit requires online PIN: its detailed NFC passage makes online PIN conditional on the card selecting PIN. [[source-adyen-docs-point-of-sale-cardholder-verification-methods]]


- Payment messages can carry amounts, cashback, platform splits, tokenization data, MOTO/manual-entry conditions, tipping, or card-acquisition references.
- Reversal supports referenced full or partial refund examples; an unreferenced refund is represented as a refund payment.
- Abort and transaction-status messages control or inspect an in-process request.
- Input, display, print, barcode/QR, and admin messages let a POS coordinate shopper-terminal interactions outside the payment payload itself.
- Stored-value examples cover gift-card activation, payment, balance inquiry, loading, reversing a load, and refund.

These are exact-commit examples. Supported hardware, merchant enablement, regional rules, and current schema behavior must be confirmed from current Adyen documentation and live/test responses.

## Cloud Device distinction

Terminal API defines terminal messages. Adyen's Cloud Device API, represented separately by the Node.js library baseline, is a newer cloud transport and device-management surface using generated `tapi` models. Local Terminal API communication and legacy cloud Terminal clients remain distinct architectures; do not merge their version histories.

## Related

- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity]] — Adyen POS network/connectivity topic directory (2026-09-15 snapshot) routing to detailed network, Wi-Fi, cellular, Bluetooth and troubleshooting guides; directory descriptions are navigation only.


- [[source-adyen-docs-point-of-sale-what-we-support]] — 2026-09-15 Adyen Docs navigation overview for in-person countries/languages, solution types, payment methods, terminal models, and industry features; broader than Terminal API.


- [[source-adyen-docs-point-of-sale-reconciling-totals]] — Adyen Docs 2026-09-15 navigation overview for terminal login/logout, operator/group totals, and terminal-versus-POS app mismatch investigation; separate from financial settlement reporting.


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-networking-issues]] — 2026-09-15 Adyen POS networking page on possible MTU-related payment-packet loss despite apparent connectivity, Endpoints test and network-team MSS guidance.


- [[source-adyen-docs-point-of-sale-diagnostics]] — Adyen Docs website overview of remote Terminal API diagnosis, cloud WebSocket connection checks, and terminal-side connectivity/hardware tests; diagnostic state is separate from payment outcome (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration]] — Adyen website hub for a basic integrated Terminal API payment flow and six detailed next-step routes (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-design-your-integration-terminal-api-get-the-terminal-id]] — Adyen Terminal API terminal-ID guide captured 2026-09-15 for POIID model/serial construction and conditional physical, Customer Area, cloud, local-diagnosis and Android retrieval routes


- [[source-adyen-docs-point-of-sale-what-we-support-payment-methods-manage-payment-methods]] — Adyen POS Customer Area merchant-account guide captured 2026-09-15 for viewing, activating/deactivating and country/region settings, including 90-day inactive-unused deletion


- [[source-adyen-docs-point-of-sale-what-we-support-solutions]] — dated Adyen in-person solutions overview distinguishing integrated Terminal API, standalone, Mobile SDK/Adyen Payments app, and partner-plugin routes (fetched 2026-09-15).


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-end-of-3g]] — Adyen Docs 2026-09-15 snapshot of 2G/3G-limited terminal models, dated regional coverage table and 4G/Wi-Fi replacement routes; verify current carrier status independently.


- [[source-adyen-docs-point-of-sale-design-your-integration-notifications-display-notifications-tender-state-reference-sheet]] — Adyen Docs website reference for in-progress POS tender states versus final tender results (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-what-we-support-supported-languages]] — 2026-09-15 Adyen Docs in-person region and terminal UI-language support tables; broader than Terminal API, with separate Mobile and legacy-terminal limits.


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-bt-base-station]] — Adyen website troubleshooting for V400m Bluetooth-base Ethernet connectivity and DHCP/pairing checks (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-risk-management-pos]] — dated Adyen POS risk guide for MOTO/MKE risk-rule refusals in Terminal API PaymentResponse and a no-retry test instruction (fetched 2026-09-15).


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-bluetooth-pan]] — 2026-09-15 Adyen webpage snapshot for mobile-POS-to-terminal Bluetooth PAN, terminal or mobile internet access, pairing and connectivity checks; requirement names e285p while setup names e285.


- [[source-adyen-docs-point-of-sale-get-started-go-live-tapi]] — 2026-09-15 Adyen Docs go-live checklist for Adyen-provided Terminal API payment terminals, live account/terminal setup, architecture-specific credential and security changes, and suggested validation.


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-set-up-beacons]] — Adyen Docs website guide to supported terminal iBeacon advertisements and cloud/local Terminal API request routing (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-get-started-tapi-checklist]] — Adyen website checklist for test Terminal API integration, architecture, terminals, payment/reconciliation tests, and separate go-live application (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-what-we-support-select-your-terminals]] — Adyen physical-terminal catalog captured 2026-09-15 for model, region, use-case, connectivity, suitability, feature and PCI PTS labels, with order-availability exceptions


- [[source-adyen-docs-point-of-sale-partial-authorizations]] — 2026-09-15 Adyen POS Terminal API guide for issuer-dependent partial authorization, collecting a shopper's outstanding amount, and reconciling related payments.


- [[source-adyen-docs-point-of-sale-design-your-integration-notifications-event-notifications]] — unversioned Adyen POS guide captured 2026-09-15 for terminal-generated EventNotification callbacks and asynchronous cloud SaleToPOIResponse delivery


- [[source-adyen-docs-point-of-sale-cardholder-verification-methods]] — Adyen POS Terminal API CVM guide (2026-09-15 webpage snapshot) for PIN, signature, card CVM lists, response results and qualified contactless limits.


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-network-configuration]] — 2026-09-15 Adyen Docs website network guide for Terminal API POS/terminal local and cloud communication, addressing, TLS, Wi-Fi, and connectivity limits.


- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-local-protect-with-library]] — Adyen Docs website guide to .NET, iOS, Java, and Node library examples for local terminal certificate validation and encrypted Terminal API messaging (2026-09-15 snapshot; no pinned library version).


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-cellular-failover]] — Adyen website guide to terminal cellular failover, local/cloud failure boundaries, SIM management, and model-specific options (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-add-data]] — Adyen Docs website guide to adding in-person payment `SaleToAcquirerData` and choosing the encoding of `AdditionalResponse` (2026-09-15 snapshot; separate from versioned GitHub examples).


- [[source-adyen-docs-point-of-sale-what-we-support-payment-methods]] — Adyen Terminal API payment-method overview captured 2026-09-15 for method and region tables, refund/chargeback flags, QR-flow and IRIS exceptions, and Mobile-solution scope


- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-configure-features]] — Adyen POS feature-setting and Customer Area inheritance guide (2026-09-15 webpage snapshot), including Terminal API local/cloud enablement.


- [[source-adyen-docs-point-of-sale-pre-authorisation]] - unversioned Adyen POS guide, captured 2026-09-15, for a Terminal API pre-authorization followed by backend amount updates and capture


- [[source-adyen-docs-point-of-sale-error-scenarios]] — 2026-09-15 Adyen Terminal API response and POS error-handling guide, including missing-result status checks, cloud Reject events, and condition-specific decline/time-out recovery.


- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-cloud]] — 2026-09-15 Adyen Docs website guide to cloud Terminal API transport, result delivery, credentials, regional endpoints, and legacy endpoint migration; distinct from commit-qualified GitHub examples.


- [[source-adyen-docs-point-of-sale-offline-payment]] — Adyen Docs website guide to configured POS offline EMV/store-and-forward payments, later processing, and merchant risk across eligible terminal and Mobile SDK paths (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-design-your-integration-notifications-display-notifications]] — Adyen Docs website guide to configuring terminal-generated DisplayRequest webhooks for POS staff messages (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-card-acquisition]] — Adyen Docs website guide to POS card acquisition, payment referencing, completed cancellation, and in-progress abort (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-local]] — Adyen website guide to local POS-to-terminal communications, live security prerequisites, and synchronous status recovery (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-capturing-payments]] — unversioned Adyen POS capture guide captured 2026-09-15 for Terminal API authorization and per-payment capture flags, Checkout API capture/cancel modifications, payment-method limits, and asynchronous outcomes


- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture-local-protect]] — 2026-09-15 Adyen local POS protection guide for merchant-written terminal certificate validation and encrypted Terminal API messages; its sample code does not establish production security.


- [[source-adyen-docs-point-of-sale-design-your-integration-network-and-connectivity-wi-fi-profiles]] — Adyen webpage guide (2026-09-15 snapshot) to remote terminal Wi-Fi profiles through Customer Area or Management API; terminal connectivity settings affect Terminal API communication.


- [[source-adyen-docs-point-of-sale-design-your-integration-choose-your-architecture]] — 2026-09-15 Adyen Docs website guide to local versus cloud Terminal API communication and architecture selection; distinct from the commit-qualified Postman and SDK examples.


- [[source-adyen-docs-point-of-sale-design-your-integration-terminal-api]] — Adyen Docs website explanation of Terminal API message structure, local/cloud transport, and result identifiers (2026-09-15 snapshot); separate from exact-commit GitHub examples.


- [[source-adyen-docs-point-of-sale-design-your-integration]] — Adyen Docs website overview of in-person integration choices and which solutions each topic applies to (2026-09-15 snapshot)


- [[source-adyen-docs-point-of-sale-get-started]] — Adyen Docs website overview of the test-integration and go-live checklist routes for Terminal API with Adyen-provided terminals; separate from versioned GitHub examples.


- [[source-adyen-docs-point-of-sale]] — Adyen website overview of in-person terminal payments, standalone or Terminal API integration choices, and local/cloud architecture (2026-09-15 snapshot; separate from versioned GitHub examples).


- [[source-github-adyen-postman]] - Postman request examples at exact commit
- [[changelog-github-adyen-postman]] - commit-qualified collection history
- [[adyen-node-api-library]] - Checkout v72 and Cloud Device API v1
- [[adyen]] - company and knowledge-status page
