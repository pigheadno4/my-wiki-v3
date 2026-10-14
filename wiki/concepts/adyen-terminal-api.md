---
title: "Adyen Terminal API"
type: concept
category: technology
tags: [adyen, terminal-api, in-person-payments, point-of-sale, nexo]
---

## Adyen Terminal API

Adyen Terminal API is a Nexo-based message interface between a point-of-sale system and an Adyen payment terminal. A request wraps a message header containing protocol, class, category, type, sale ID, service ID, and terminal `POIID`, followed by category-specific payment, reversal, input, display, print, reconciliation, or stored-value data.

## Integration boundary

Adyen's POS timeout guide separates a confirmed issuer-processing timeout (platform cancellation and `PaymentResponse` `Failure`/`Communication timeout`) from a request timeout that can leave the terminal payment active. A device interaction timeout usually cancels but can instead advance the screen, as with tipping. Missing payment results and request-timeout `Reject` notifications call for `TransactionStatusRequest` before retry, because the original payment may still progress or complete. The guide's 120-second local and 150-second cloud windows describe specific timeout types, not a general safe-retry timer. [[source-adyen-docs-point-of-sale-error-scenarios-pos-timeouts]]


The Adyen website Terminal API checklist frames merchant implementation as test-account and terminal setup, architecture/payment-feature choice, test transactions and reconciliation, then a separate live-account application and signed contract. It says to consult Adyen before building a cloud integration and to inform Adyen if P2PE is required because different terminal software is supplied. These website setup gates are distinct from the exact-commit Postman request examples; the checklist does not establish account-specific enablement or current SDK-version behavior.


Cellular failover protects the terminal's Adyen-service internet path, subject to terminal/SIM configuration; it does not restore a cloud POS app's lost internet path or a local POS-to-terminal LAN link. Offline payment is a separate local-communications alternative with merchant liability for failed captures, chargebacks and disputes. The website's terminal models, firmware gates and dated cellular-fee language belong to the linked source and raw snapshot, not the versioned GitHub Terminal API examples.


The Adyen POS Device settings guide requires **Enable Terminal API** for both local and cloud Terminal API integrations, and **Enable WebSockets** for a cloud architecture. A terminal feature's availability in a Terminal API integration also depends on the POS app supporting it. These are website-documentation settings, distinct from the retained Postman repository baseline. [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-configure-features]]


For local communications, the merchant POS sends Terminal API requests over the LAN to an Adyen terminal, which routes shopper-completed transactions to Adyen and returns a synchronous response. Live local processing requires terminal-certificate validation against Adyen's root and shared-key protection between POS and terminal; the guide describes test as unenforced while building. Missing or timed-out payment responses call for a transaction-status check before operators risk a duplicate transaction. This website architecture guide is separate from the exact-commit Postman examples and independently versioned SDK implementations.


The retained Postman collection demonstrates Terminal API operations for terminal-present payments, refunds, shopper input, display and printing, reconciliation, card acquisition, tipping, instalments, and gift cards. It explicitly routes capture, recurring token charges, and authorization adjustments to Checkout API, and store or terminal-fleet administration to Management API.

Cloud transport requires an API key and a terminal ID. Merchant implementations must keep credentials private, generate unique request identities, correlate asynchronous or in-process operations, handle result and error fields, and avoid treating Postman test scripts as a production POS state machine.



## POS solution route

Adyen's dated in-person “Solutions” overview distinguishes POS-to-Adyen-terminal Terminal API integration from direct standalone-terminal transactions, mobile POS app paths, and partner-platform plugins. Its mobile path uses Mobile SDK for payment routing while retaining the Terminal API specification; its standalone and partner-plugin paths do not imply that a merchant POS app directly sends Terminal API messages. The overview is navigation and does not prove present-day device, SDK, market, or payment-method compatibility. [[source-adyen-docs-point-of-sale-what-we-support-solutions]]


## Terminal tipping amount boundary

An optional Terminal API tip-base override keeps `PaymentTransaction.AmountsReq.RequestedAmount` as the full purchase amount while `AmountToTipOn` controls the amount on which the terminal offers tip suggestions; the chosen tip increases the response's `AuthorizedAmount`. This per-payment override also replaces configured Customer Area tipping options and requires `AskGratuity` plus an encoded `Operation` with `TipSuggestions`. The 2026-09-15 guide limits it to terminal software 1.103+ and excludes pay-at-table split checks.


Adyen's 2026-09-15 website guide describes `AskGratuity` in a Terminal API payment request whose `RequestedAmount` is the original purchase amount. After the shopper enters a tip or a higher total at the terminal, the terminal sends the original amount plus tip for authorization; the response separates `TipAmount` from the total `AuthorizedAmount`. This is terminal tipping during payment, not a separate capture operation. After-card tipping and total-entry mode require Support enablement; details and configuration scope remain in the source. [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]]


## Quick Chip acquisition boundary

Adyen's US-only Quick Chip guide describes a card-acquisition interaction that lets a shopper remove an EMV chip card before the final sale amount is known, followed by a separate Terminal API Payment request. The acquisition can use a placeholder `TotalAmount`; the later payment supplies the final `RequestedAmount` and references the acquisition response's `POIData.POITransactionID` timestamp and transaction ID. Card acquisition is not payment authorization. The guide requires terminal software 1.95+ and Support enablement, and its sample request/response IDs and amounts conflict; see the source for the exact evidence boundary. [[source-adyen-docs-point-of-sale-quick-chip]]


## Payment-network application penalty box

Adyen's dated POS guide describes a temporary penalty box for a card application when its payment-network route is unavailable. The platform informs a terminal on an authorization attempt; the terminal then checks configured offline EMV followed by Store and Forward, or selects another application when available. A single-branded card still gets an authorization attempt in case the outage has cleared, then conditional offline processing. If no alternative or offline path is available, the payment declines. This is application/payment-network routing, not local POS-terminal connectivity or a license to retry an unresolved transaction; the four-hour duration belongs to the test fixture. [[source-adyen-docs-point-of-sale-error-scenarios-penalty-box]]


## POS cashback amount boundary

Adyen's dated Terminal API cashback guide distinguishes cash with a purchase from no-purchase cashout. The `PaymentRequest` uses `AmountsReq.RequestedAmount` for purchase plus cash and `CashBackAmount` for the cash portion. On `PaymentResponse.Response.Result=Success`, the issuer authorized both and the merchant pays the response `CashBackAmount` in cash; `Partial` authorizes the purchase but not the cashback. Support enablement and card/region restrictions apply, with several listed card routes purchase-only. This POS cash handoff is separate from online capture or payout mechanics. [[source-adyen-docs-point-of-sale-cashback-and-cash-out]]
## Payment and interaction patterns

A merchant POS can override Customer Area terminal tipping suggestions for one Terminal API payment by sending `AskGratuity` with a version-appropriate Base64 `Operation` object. The shopper chooses among the presented tip/no-tip options; `RequestedAmount` is the purchase base, while the payment response's `AuthorizedAmount` includes any selected tip. The website guide requires terminal software 1.97+ and changes the `Operation` shape at 1.101; exact formats stay in its source/raw snapshot.


A merchant POS `AbortRequest` is for an unfinished terminal payment: it carries a new request ID while `MessageReference` identifies the original Payment request. The abort HTTP acknowledgement is separate from the original payment's `Failure`/`Aborted` response and optional transaction-status confirmation. A completed or already-authorized payment requires its condition-specific authorization-cancel or refund path; pressing Cancel on an already-authorized signature screen does not undo the payment. [[source-adyen-docs-point-of-sale-basic-tapi-integration-cancel-a-transaction]]


For a basic in-person Terminal API payment, the merchant POS supplies a per-terminal request `ServiceID` (1–10 alphanumeric characters, unique for the preceding 48 hours for that `POIID`) and its own sale-transaction reference; the `PaymentResponse` supplies a distinct terminal transaction ID to retain for lookup, reconciliation, or later operations. Asynchronous cloud-terminal communication delivers the response through an event notification. A missing response calls for transaction-status verification before staff retry or refund, since the payment may still be in progress. This website request/response guide does not establish capture or settlement, and its examples do not update versioned SDK baselines.


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

- [[source-adyen-docs-point-of-sale-aid-selection-rules]] — 2026-09-15 POS terminal/standalone card-application guide for automatic selection, configurable cost, PIN and menu priorities (compliance and supported-feature rules fixed), and shopper Card options choice with an EEA software 1.109 qualification.


- [[source-adyen-docs-point-of-sale-custom-cards]] — 2026-09-15 custom-magstripe-card Terminal API acquisition guide for merchant POS handoff to the card issuer and `EnableService` closure; acquisition is distinct from an Adyen gift-card payment.


- [[source-adyen-docs-point-of-sale-payment-facilitators]] — POS payment-facilitator Terminal API data route (2026-09-15 snapshot): request-supplied sub-merchant data for payments and referenced/unreferenced refunds overrides store fields; full role/data boundary belongs to [[adyen-pos-payment-facilitators]].


- [[source-adyen-docs-point-of-sale-classic-library-deprecation]] — Adyen Docs deprecation notice captured 2026-09-15 for migration from embedded classic POS libraries to Terminal API, with an Xstore JNI/OPI exception and dated timeline.


- [[source-adyen-docs-point-of-sale-alternative-payment-methods]] — 2026-09-15 POS alternative-methods overview for gift cards, one-time numeric codes, QR wallet payments, and Brazil voucher navigation; method behavior remains in separate guides.


- [[source-adyen-docs-point-of-sale-release-updating]] — Adyen Docs 2026-09-15 terminal software update strategy for Terminal API and standalone terminals: automatic rollout, approved manual LTS updates, beta testing and restart-hour conditions; separate from Terminal API message or SDK versions.


- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-terminal-actions-api]] — Adyen Management API guide (2026-09-15 raw snapshot) for scheduling Android terminal app/certificate actions and checking their status; distinct from Terminal API payment messages.


- [[source-adyen-docs-point-of-sale-installments]] — Adyen Docs 2026-09-15 POS credit-card installments overview routing to Brazil, Japan and Mexico country guides; detailed terms and eligibility require those separate sources.


- [[source-adyen-docs-point-of-sale-tipping]] — Adyen Docs website overview routing POS-proposed, terminal-selected, receipt-after-preauthorization, and standalone tipping choices (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-add-data-sale-to-acquirer-data]] — Adyen POS Terminal API website sample collection of `SaleToAcquirerData` JSON and key-value names/paths for terminal or Mobile payments, with non-exhaustive and example-only scope (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-installments-japan-installments]] — Adyen website guide to Japan terminal-selected regular/revolving credit installments, Support enablement, and bank/merchant money flow (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-reconciling-totals-reconcile-a-balance-mismatch]] — 2026-09-15 Adyen Terminal API balance-mismatch guide distinguishing current-period `SaleReconciliation` (starts a new period) from prior-period `PreviousReconciliation` (read without new period).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-cancel-unreferenced]] — Adyen POS website guide captured 2026-09-15 for Support-delayed unreferenced-refund cancellation through backend Payment API /voidPendingRefund, tender/PSP reference identities and asynchronous VOID_PENDING_REFUND result


- [[source-adyen-docs-point-of-sale-cashback-and-cash-out]] — dated Adyen Terminal API cashback/cashout guide for request amount split, Success/Partial cash handoff, Support enablement, and card/region restrictions (fetched 2026-09-15).


- [[source-adyen-docs-point-of-sale-card-acquisition-insights]] — Adyen 2026-09-15 webpage overview of POS shopper-insight inputs and standard-webhook versus Terminal API payment-response collection routes, with conditional PAR availability.


- [[source-adyen-docs-point-of-sale-enter-payment-manually]] — Adyen Docs website guide to Support-enabled Terminal API Manual Key Entry fallback, shopper card entry/signature, max amount and liability boundary (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal-change-amount-to-tip-on]] — Adyen POS Terminal API website guide to per-payment tip-base override, configured-option replacement, version and pay-at-table limits, and purchase/tip/authorized amount fields (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-make-a-payment-greece-tax]] — dated Adyen website guide to Greece Terminal API e-invoicing signature and conditional autonomous-mode payment/refund routes (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-reconciling-totals-retrieve-totals-from-the-terminal]] — 2026-09-15 Adyen Terminal API `GetTotals` guide for reading terminal transaction totals with operator/group filters without starting a new reconciliation period.


- [[source-adyen-docs-point-of-sale-error-scenarios-penalty-box]] — dated Adyen POS guide to payment-network application penalty routing, conditional offline/alternate paths, and suffix-158 test refusal (fetched 2026-09-15).


- [[source-adyen-docs-point-of-sale-add-data-tender-options]] — Adyen POS website guide captured 2026-09-15 for Terminal API tenderOption names, SaleToAcquirerData encoding, ReceiptHandler printer-failure default and Support-configured defaults


- [[source-adyen-docs-point-of-sale-error-scenarios-pos-timeouts]] — Adyen POS guide (2026-09-15 webpage snapshot) to processing, device and request timeout distinctions, local/cloud durations and status-gated recovery.


- [[source-adyen-docs-point-of-sale-reconciling-totals-log-in-and-log-out]] — Adyen Docs 2026-09-15 Terminal API Login/Logout guide for operator, group and shift attribution before totals retrieval; Login does not authenticate the operator.


- [[source-adyen-docs-point-of-sale-tipping-tipping-from-cash-register]] — Adyen Docs website guide to POS-proposed TipAmount, shopper terminal choice, and actual tip/total response fields (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal-override-tipping-configuration]] — Adyen website guide to per-payment terminal tipping overrides, versioned request formats, and purchase/tip/authorized amounts (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-tipping-tipping-on-receipt]] — 2026-09-15 Adyen Docs receipt-tip guide for initial Terminal API authorization followed by eligible backend adjustment or overcapture and manual capture.


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-pass-application-information]] — Adyen Terminal API application-information guide captured 2026-09-15 for POS platform/app/device-OS metadata, conditional versions, SaleToAcquirerData formats and AdditionalResponse format


- [[source-adyen-docs-point-of-sale-installments-mexico-installments]] — 2026-09-15 Adyen Mexico POS Terminal API guide for debit/credit choice, 3–18 credit installments, issuer-program limits, and merchant installment-fee responsibility.


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-refund-webhooks]] — Adyen POS website guide captured 2026-09-15 for referenced CANCEL_OR_REFUND versus unreferenced REFUND_WITH_DATA validation outcomes, distinct PSP reference meanings and later exception risk


- [[source-adyen-docs-point-of-sale-quick-chip]] — 2026-09-15 Adyen US Quick Chip guide for pre-amount EMV card acquisition, final-amount payment linkage, 1.95+ software and Support conditions, and inconsistent examples.


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-cancel-a-transaction]] — Adyen 2026-09-15 website guide to POS/terminal cancellation of in-progress requests, original-reference lookup, result verification and completed-payment boundary.


- [[source-adyen-docs-point-of-sale-diagnostics-check-cloud-connection]] — Adyen Docs 2026-09-15 guide to checking live terminal cloud WebSocket status via Customer Area, Cloud device API, legacy Terminal API endpoint, or terminal diagnostics; a connectivity check is not a payment result.


- [[source-adyen-docs-point-of-sale-mail-and-telephone-order-moto]] — Adyen Docs website guide to card-not-present MOTO tender-option payments keyed on a terminal, standalone/Terminal API scope, AVS, PCI and liability limits (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-unreferenced]] — unversioned Adyen POS guide captured 2026-09-15 for unreferenced Terminal API PaymentType Refund, enablement limits, merchant fraud liability and qualified refund outcomes


- [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v1]] — Adyen white v1 physical POS card test guide for Terminal API decline fixtures and response-field limits (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-card-acquisition-identifiers]] — Adyen Terminal API card/shopper identifier guide (2026-09-15 webpage snapshot) for response/webhook fields, alias/PAR versus payment-token meaning, enablement and privacy scope.


- [[source-adyen-docs-point-of-sale-error-scenarios-refusal-reasons-pos]] — 2026-09-15 Adyen Docs Terminal API declined-response reference for codeable `ErrorCondition`, explanatory refusal fields, and condition-specific retry flags.


- [[source-adyen-docs-point-of-sale-installments-brazil-installments]] — Adyen website guide to Brazil POS credit/debit/voucher choice, terminal or merchant UI installments, and installment settlement (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-referenced]] — unversioned Adyen POS Terminal API guide captured 2026-09-15 for referenced full/partial ReversalRequest refunds, offline tender-reference and ecommerce PSP-reference forms, and asynchronous webhook outcomes


- [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]] — 2026-09-15 Adyen terminal-tipping guide for tip/total prompts, configuration, `AskGratuity` payment request, authorized amount, response, and optional warnings.


- [[source-adyen-docs-point-of-sale-diagnostics-request-diagnosis]] — Adyen Terminal API diagnosis guide captured 2026-09-15 for terminal health/host checks, Mobile SDK security/offline checks, conditional response fields, and Busy failure boundary


- [[source-adyen-docs-point-of-sale-pay-at-x]] — 2026-09-15 Adyen Pay-at-table Terminal API guide for terminal-initiated staff wake-up, POS bill selection and successive equal/unequal split requests.


- [[source-adyen-docs-point-of-sale-error-scenarios-raw-acquirer-responses]] — 2026-09-15 Adyen Docs POS lookup for optional raw acquirer responses, mapped Terminal API refusal fields, and row-specific status/action examples; raw strings are unstable.


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-generate-receipts]] — Adyen Docs 2026-09-15 Terminal API receipt-data, scheme-compliance, language, and terminal-printer guide for shopper and merchant receipts.


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-verify-transaction-status]] — Adyen Docs website guide to TransactionStatusRequest recovery of missing terminal/mobile transaction responses and original-result interpretation (2026-09-15 snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment]] — Adyen POS Terminal API refund overview comparing referenced `ReversalRequest` and unreferenced refund `PaymentRequest`, method/routing limits, and asynchronous outcomes (2026-09-15 webpage snapshot).


- [[source-adyen-docs-point-of-sale-basic-tapi-integration-make-a-payment]] — Adyen website guide to basic in-person Terminal API payment request, response identities/results, and missing-response recovery (2026-09-15 snapshot).


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
