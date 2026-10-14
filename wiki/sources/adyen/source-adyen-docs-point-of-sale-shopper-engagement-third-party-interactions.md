---
title: "Adyen POS third-party terminal interactions"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-engagement/third-party-interactions"
raw_files:
  - "adyen/docs/point-of-sale/shopper-engagement/third-party-interactions/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-engagement, third-party, terminal-api, input, display, webhooks]
---

## Overview

This historical Adyen guide lets a **merchant-authorized third party** conduct non-payment interactions on the merchant's payment terminals without integrating with the merchant POS app. A merchant POS app still starts the payment; the third party can receive terminal display notifications and Adyen platform standard webhooks, then send Terminal API Input or Display requests for surveys, loyalty or digital-receipt prompts. The guide's example starts the third-party input **after** the payment process finishes and says the interaction does not interrupt payment. It does not delegate payment or card acquisition to the third party. See [[adyen-pos-shopper-engagement]] and [[adyen-terminal-api]].

## Key takeaways

- The third party may send **non-payment** Input/Display requests, receive terminal-generated display notifications and, when configured, receive platform-generated standard webhooks. Payment and card-acquisition requests from that credential are prohibited; the source describes refusal with the label `010 Not Allowed`. The guide says this route does **not** work with OPI, and lists a Terminal API integration with WebSockets enabled plus M400, P400 Plus, V210 and V400m as its dated model conditions. These are not current eligibility proof. See raw introduction and § Security and requirements (lines 19–44).
- The merchant configures notification/webhook destinations and creates a special third-party API credential. The credential has an API key, account scope and **Thirdparty interaction with in-store terminals** role only; creation requires a Merchant admin or Manage API credentials user role. The merchant shares the key securely. The third party uses notification `POIID` to target its request and sends the key in `x-API-key`. These are separate merchant, third-party, terminal and Adyen platform responsibilities. See raw §§ How it works, Set up third-party webhook endpoints, Set up the third-party API credential and Let the third party send requests (lines 45–56, 78–124, 255–306).
- The third-party endpoint receives terminal display notifications and optionally standard webhooks. The dated setup uses public display URLs; for **local** communications, the guide says Support must ensure terminal-generated display notifications are unencrypted so the third party can use them. It lists test HTTP/HTTPS versus live HTTPS/TLS 1.2 endpoint conditions. For standard webhooks it recommends HMAC verification and requires an HTTP success acknowledgement. Crucially, the guide says transaction-detail restrictions were not then enforced for third-party standard webhooks, so the merchant should enable only the minimum additional detail needed. See raw § Set up third-party webhook endpoints (lines 78–132).
- In the example, terminal `TENDER_CREATED` through `TENDER_FINAL` display notifications let the third party follow tender progress; a final notification adds the PSP reference to the tender reference for cross-reference with a later standard webhook. After payment, the third party sends Input, receives the customer's response, can show a timed thank-you Display, and separately receives the platform webhook. A displayed `READY_3RD_PARTY` sample and field-level examples are in raw lines 184–253. This described sequence does not establish a successful payment or customer-consent handling for a specific deployment. See raw §§ How it works and Third-party interaction flow (lines 45–76).
- Third-party Input/Display requests should set `MinimumDisplayTime`; otherwise the source says they time out after three seconds. The merchant POS app can override an in-progress third-party interaction with a higher-priority DisplayRequest for the standby screen because it lacks the third party's `ServiceID`; the terminal user can cancel with a keypad key or available on-screen icon. **Source conflict:** the POS-cancel prose says the third party receives `ErrorCondition: Cancel`, while its example response uses `Busy` with “A higher priority request has been received.” Treat the exact error condition as unresolved by this snapshot. See raw §§ Let the third party send requests and Canceling an in-progress interaction (lines 286–306, 308–502).
- The final testing section proposes test transactions, answer, timeout and both cancellation paths, then repeats across payment instruments and entry methods. These are suggested scenarios, not evidence they were run. See raw § Testing (lines 504–521).

## Detail locators

- Raw §§ Security and requirements, How it works and Third-party interaction flow: permitted requests, dated WebSocket/model scope, tender notifications and payment/interaction boundary (lines 35–76).
- Raw § Set up third-party webhook endpoints: merchant/third-party endpoint setup, local-notification security, standard-webhook information exposure and account scope (lines 78–253).
- Raw §§ Set up the third-party API credential and Let the third party send requests: credential roles/accounts, `POIID`, API key and timeout (lines 255–306).
- Raw § Canceling an in-progress interaction: POS versus terminal controls and conflicting POS-cancel error example (lines 308–502).

## Related

- [[adyen-pos-shopper-engagement]] — in-person Input/Display use cases and consent context.
- [[adyen-terminal-api]] — Terminal API request and notification architecture.
- [[adyen-webhooks]] — platform standard-webhook security and scope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-engagement/third-party-interactions/2026-09-15|Third-party interactions guide, fetched 2026-09-15]]
