---
title: "Adyen PayBright Android Redirect Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/android-component"
raw_files:
  - "adyen/docs/payment-methods/paybright/android-component/2026-09-15.md"
tags: [adyen, paybright, affirm, android, components, redirect, capture, refund]
---

## Overview

This 2026-09-15 Adyen Docs page describes PayBright in an existing Android Components integration. It opens by saying Affirm acquired PayBright and Adyen will not accept new PayBright integrations. The instructions therefore describe a historical/existing integration path, not current new-merchant eligibility or evidence of payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The requirements table specifies an **Advanced-flow Android Components** integration and PayBright added in Customer Area, although the opening and See also links point to Sessions-flow Components; use the Advanced requirement for the described server path and do not infer that the Sessions link establishes supported Sessions behavior. `/paymentMethods` uses CA, CAD and amount in minor units and returns `paymentMethod.type: paybright`; the merchant form need not collect PayBright-specific shopper information. The page's later instruction to request PayBright in live Customer Area does not override its upfront statement that Adyen accepts no new PayBright integrations.
- The server `/payments` request specifies `paybright`, shopper name, date of birth, email, phone, country, billing/delivery addresses, `lineItems` and `returnUrl` from `RedirectComponent.getReturnUrl(context)`; locale is explicitly optional. The example uses a CAD 60 basket with shoes, socks and a negative discount line. The server passes the returned redirect `action` to Android; after the Redirect Component returns, send its `actionComponentData.details` to `/payments/details`, then present the result. If the shopper fails to return, use `AUTHORISATION` webhooks. `Authorised` is a payment result, not proof of capture or merchant settlement.
- PayBright payments are automatically captured after authorization by default. Delayed or manual capture is needed to capture after shipping or to partially capture. The page says the shopper is charged the first installment at capture. Partial capture is unavailable with Customer Area automatic capture enabled. Its `/capture` section uses `modificationAmount` and optional `additionalData.openinvoicedata`; an initial partial capture cancels the remainder unless the account is enabled for multiple partial captures, which requires Support setup and creates a new invoice per capture.
- Cancel an uncaptured payment; refund a captured one. For partial refunds, the page links Checkout `/payments/{paymentPspReference}/refunds` but illustrates a legacy-style `/refund` body with `modificationAmount` and optional `additionalData.openinvoicedata`. The guide does not reconcile the endpoint/body families, so verify the applicable API before use.

> [!warning] Example inconsistency
> The partial-capture prose says the shopper kept one pair of socks, but its example includes shoes and socks; its `modificationAmount.value` is 4500 while the pictured item totals are 4000 plus 1500, and currency fields are empty. The sample also has a trailing comma in a `json` fence. These values do not establish a valid partial capture request.

## Detail locators

- Acquisition/no-new-integration statement, Advanced requirement versus Sessions links, CA/CAD method discovery: pinned raw lines 15–42 and 1006–1010.
- Server request fields and language-specific TEST examples: lines 44–817; redirect action, details and result/webhook handling: lines 819–889.
- Automatic/manual capture, partial-capture effects and example: lines 891–950. Cancel/refund and partial-refund endpoint/example: lines 952–996. Test/live page statements: lines 998–1004.

## Related

- [[adyen-online-payments]] — provider payment integration concept
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm overview; PayBright acquisition does not make the two integration paths interchangeable

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/android-component/2026-09-15|PayBright Android Component guide, captured 2026-09-15]]
