---
title: "Adyen UPI Autopay API-only recurring integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/upi-autopay/api-only"
raw_files:
  - "adyen/docs/payment-methods/upi/upi-autopay/api-only/2026-09-15.md"
tags: [adyen, upi, autopay, recurring, mandates, api-only]
---

## Overview

This 2026-09-15 UPI Autopay API-only guide covers **shopper-approved mandate registration**, later pre-debit notifications and recurring charges, then mandate cancellation. It assumes an existing API-only Advanced integration. The shopper approves the mandate in a UPI app; the UPI provider and issuing bank use it to track the billing plan. A request, app return, pending response, successful notification or stored-token reference alone does not establish successful authorization, capture, settlement or a usable live mandate. [[adyen]] [[adyen-tokenization]]

## Key takeaways

- **Registration and consent:** send a server `/payments` request with UPI `upi_intent`, `upi_qr` or legacy `upi_collect`, `storePaymentMethod: true`, `shopperInteraction: Ecommerce`, `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`, shopper reference, INR initial amount and mandate cap/rule/frequency/end date and related fields. Collect requires VPA; Intent appId targets a UPI app and is mandatory on iOS, with omitted/null appId yielding an Android generic drawer. Intent is mobile app/mobile web only, not desktop. The guide says the initial authorization happens automatically within five minutes **after successful mandate registration** and initial `amount.value` cannot exceed `mandate.amount`; these are historical source claims, not an outcome guarantee. Monthly/weekly billing day and attempt rule differ from adhoc.
- **Approval and final state:** Intent launches the app from `action.url`, with Android auto-return versus manual iOS app closing; QR displays `action.qrCode`; Collect asks the shopper to approve in-app within a five-minute countdown. The examples return `Pending` with `await` or `qrCode` actions, while the guide directs the merchant to an AUTHORISATION webhook for the payment result. Optional Standard webhook settings expose mandate ID/status and UPI metadata; store the NPCI Unique Mandate Number for later use. `AUTHORISATION` false/true has distinct failed/success handling, and its initial true description says the payment completed and a mandate was created. A stated 2–3-day return of any debited amount after failure is guidance, not proof of a refund.
- **Subsequent cycles:** a merchant triggers `/notifyShopper` with stored method, merchant, shopper, amount, billing date and, for adhoc mandates, a unique billing sequence number. Adyen forwards to UPI network/issuer for shopper alert; the page says the notification must precede each charge by at least **24 hours**, and shoppers may cancel the mandate. On successful notification, retain `shopperNotificationReference` for the later server `/payments` call with `shopperInteraction: ContAuth`, stored method ID, matching reference and adhoc sequence, and INR amount within the mandate rule. Its `Received` response indicates initiation; use the recurring AUTHORISATION webhook for the payment outcome. The snapshot also states non-customer-initiated work must run in specified IST non-peak windows and limits failed recurring authorization retries to three, at least one hour apart, then a new notification after exhaustion.
- **Cancellation and lifecycle:** shopper cancellation occurs in the UPI app; merchant cancellation deletes `/storedPaymentMethods/{storedPaymentMethodId}` to remove the stored token and cancel the linked mandate. The guide points to `recurring.token.disabled` webhook for cancellation status; deleting/requesting is not itself confirmation. `mandate.endsAt` sets a billing-plan end date, but this page gives no amendment flow.
- **Material source tensions:** the registration table's `mandate.amountRule` says `max`/`exact` compare with initial `amount.value`, whereas the later `/notifyShopper` table compares with `mandate.amount`. The acquirer rule says merchant-defined values are alphanumeric, while `mandate.remarks` says spaces are allowed and sample references/remarks contain spaces or underscores. Intent and QR response snippets have malformed JSON (missing comma after `paymentData`); the recurring response has an unterminated shopper-reference string. The recurring AUTHORISATION-success row repeats 'mandate was created' although it sits in the subsequent-charge section. Treat snippets and contradictory thresholds as unverified until the current contract is checked.
- **Historical method/test scope:** the captured page says NPCI announced a UPI Collect deprecation plan in November 2025, Adyen will no longer offer Collect for **new** integrations, and custom API/UI merchants should migrate toward Intent/QR; the Collect example remains in the page. TEST magic amounts are scenario examples requiring Implementation Manager setup; LIVE acceptance requires Account Manager onboarding. Neither statement proves current provider eligibility or an executed mandate/payment.

## Detail locators

- API-only prerequisite, alphanumeric warning, registration fields, amount/frequency/expiry/remark rules: raw lines 21–58. Intent app-switch/return/webhook and TEST v72 sample: raw lines 60–126. QR approval and sample: raw lines 128–185. Collect deprecation, five-minute wait and sample: raw lines 187–248.
- Optional webhook settings, mandate/UPI fields, initial AUTHORISATION outcomes and example: raw lines 250–322. Non-peak IST windows, pre-debit roles/24-hour lead time, `/notifyShopper` fields and v67 TEST example/response: raw lines 324–395. Recurring request, `Received` response, webhook/retry table: raw lines 397–471. Cancellation and TEST/LIVE gates: raw lines 473–503.

## Related

- [[adyen-tokenization]] — recurring stored-payment-method and token lifecycle concept.
- [[adyen-online-payments]] — initial and subsequent server payment/webhook flow context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/upi-autopay/api-only/2026-09-15|UPI Autopay API-only guide, captured 2026-09-15]]
