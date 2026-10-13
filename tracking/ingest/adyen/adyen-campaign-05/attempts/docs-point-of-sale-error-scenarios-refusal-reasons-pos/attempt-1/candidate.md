---
title: "Terminal API refusal reasons | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/error-scenarios/refusal-reasons-pos"
raw_files:
  - "adyen/docs/point-of-sale/error-scenarios/refusal-reasons-pos/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, error-condition, refusal-reasons]
---

## Overview

This Adyen Docs page is a point-of-sale **declined PaymentRequest** reference for Terminal API `PaymentResponse` fields. It explains the stable routing identity Adyen recommends for POS code: `ErrorCondition` gives the error category in the response, while `refusalReason` and `message` provide extra explanation in `Response.AdditionalResponse`. The tables group common refusal examples and a **Retry?** indicator by `ErrorCondition`. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- Adyen says refusal reasons are based on acquirer/issuer raw responses, but the merchant POS **can code on `ErrorCondition`** and **should not code on `refusalReason` or `message`**. The linked raw-response page is separate; a raw string is not a universal code or behavioral rule.
- The tables list **Aborted, Busy, Cancel, DeviceOut, InvalidCard, NotAllowed, Refusal, UnreachableHost, and WrongPIN**. Their rows carry different actions. An `ErrorCondition` category alone does not turn every decline into an immediate same-card retry, and a checkmark is the row's retry indication, not a guarantee that the next attempt will succeed.
- **Busy** rows are marked no retry. In the payment-in-progress row, the listed `serviceId` belongs to the other ongoing transaction and can be used for an `AbortRequest` to cancel that in-progress request; do not treat Busy as proof the new request was processed. **Cancel / Approved** is marked no retry even though the issuer had initially approved it, while many other Cancel rows are marked retry.
- The **Refusal** table is mixed: acquirer error, mobile PIN requirement, insufficient balance, and some generic declines carry checkmarks, while AID banned, blocked card, issuer-suspected fraud, PIN-validation-not-possible, and restricted card carry X marks. Some entries instruct changing payment method, contacting a bank or Support, or satisfying a condition; do not collapse these into a blanket retry rule.
- **UnreachableHost** rows describe going offline or inability to contact the issuer and are marked retry; **WrongPIN / Invalid Pin** is also marked retry. These are **decline-response** rows. A missing payment response or uncertain payment outcome requires the separate response-handling/status flow and is not resolved by this table alone.
- The API Explorer link in this snapshot uses `latest`; the source does not lock a Terminal API version or prove a present-day merchant/device environment or actual decline outcome. For exact refusal text, message, row-specific instructions, and qualified examples, follow the raw locators.

## Detail locators

- `Terminal API refusal reasons`, lines 15–23: declined-response scope, `ErrorCondition` versus `refusalReason`/`message`, raw origin and code-against distinction.
- `Refusal reasons by error condition`, lines 25–41: common-table framing, nine literal category names, `PaymentResponse.Response` location, AdditionalResponse placement and Support route.
- `ErrorCondition: Aborted`, lines 43–47: contactless-fallback abandonment and retry checkmark.
- `ErrorCondition: Busy`, lines 49–55: payment-in-progress `serviceId`, optional AbortRequest path, and no-retry flags.
- `ErrorCondition: Cancel`, lines 57–86: no-retry Approved cancellation versus retry-marked Cancelled/card-removal/merchant/shopper cancellation rows.
- `ErrorCondition: DeviceOut` / `InvalidCard` / `NotAllowed`, lines 88–109: terminal crash/low-battery, mixed InvalidCard retry flags, and NotAllowed no-retry rows.
- `ErrorCondition: Refusal`, lines 111–140: row-by-row refusal reason, message, context and retry flags; fraud and blocked-card non-retry examples, conditional issuer/card/wallet examples, region-related restricted-card raw-code examples.
- `ErrorCondition: UnreachableHost` / `WrongPIN`, lines 142–153: network/issuer unreachability and invalid-PIN rows with their retry flags.
- `See also`, lines 155–158: raw-response and response-handling links are navigation; this page does not specify missing-result recovery.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — Terminal API response and POS error concept.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/error-scenarios/refusal-reasons-pos/2026-09-15|Terminal API refusal reasons (2026-09-15 snapshot)]]
