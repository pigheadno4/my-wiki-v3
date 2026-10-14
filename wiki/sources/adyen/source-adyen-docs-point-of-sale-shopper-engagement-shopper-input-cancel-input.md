---
title: "Cancel Adyen Terminal API shopper input"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/shopper-input/cancel-input"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/shopper-input/cancel-input/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, terminal-api, input, cancellation]
---

## Overview

Adyen's guide, captured 2026-09-15, describes canceling an **in-progress Terminal API InputRequest** either from the merchant POS app with a separate `AbortRequest` or at the payment terminal with Cancel. This is a [[adyen-pos-shopper-engagement]] input-control procedure. The analogy to canceling an in-progress payment does not make it a payment cancellation or prove that any financial transaction has stopped.

## Key takeaways

- **POS-side abort targets the input request.** Send a Terminal API request whose header uses protocol 3.0, `MessageClass: Service`, `MessageCategory: Abort`, `MessageType: Request`, a new terminal-scoped ServiceID, SaleID and POIID. Set `AbortReason: MerchantAbort`. `AbortRequest.MessageReference` must identify `MessageCategory: Input`, the SaleID of the POS component that sent that input, and the **original input request's ServiceID**. The abort request's own ServiceID is distinct from its target reference; the page's 48-hour ServiceID uniqueness rule does not establish idempotent replay.
- **Check the input outcome after an accepted abort.** The guide says a successful `AbortRequest` returns HTTP `200 OK` with no body. Confirm that the input screen disappears and the original `InputRequest` returns `Result: Failure`, `ErrorCondition: Aborted`; HTTP 200 alone is not the stated completion check. The sample abort targets input ServiceID `21796`, but its illustrative `InputResponse.MessageHeader.ServiceID` is `010`, so the displayed sample does not itself verify matching request/response IDs.
- **Terminal Cancel has type-specific outcomes.** On a keyed terminal press Cancel; on a terminal without a keypad select the displayed Cancel icon. If successful, the prompt disappears. For Confirmation and Signature input, the table reports `Result: Success` with `ConfirmedFlag: false`; for Menu, Digit and Text input, it reports `Result: Failure` with `ErrorCondition: Cancel`. Do not equate the Confirmation/Signature `Success` with affirmative shopper consent.
- The page addresses an active input prompt. It does not define a general payment-abort result, a pending-payment recovery rule, or a guarantee that every cancellation races successfully with new POS work. Follow the original input and any separate payment response.

## Detail locators

- Raw `# Cancel collecting input` and `## Requirements` (lines 15–30): in-progress input scope, POS/terminal routes and Terminal API prerequisite.
- Raw `## Cancel from POS app` request table and sample (lines 32–85): Service/Abort header, MerchantAbort, target MessageReference fields, and different sample abort versus input ServiceIDs.
- Raw `## Cancel from POS app` response checks (lines 87–136): HTTP 200 with no body, disappeared screen and original input `Failure`/`Aborted`; the sample input response ServiceID does not match the target shown earlier.
- Raw `## Cancel from terminal` (lines 138–160): keypad or display Cancel, screen disappearance, Confirmation/Signature false flag versus Menu/Digit/Text failure.
- Raw `## See also` (lines 162–166): separate input, session and in-progress transaction cancellation guides; navigation only.

## Related

- [[adyen-pos-shopper-engagement]] — POS input interaction hub.
- [[adyen-terminal-api]] — Terminal API request and financial-operation boundary.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/shopper-input/cancel-input/2026-09-15|Cancel collecting input, fetched 2026-09-15]]
