---
title: "PayCo iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/ios-component"
raw_files:
  - "adyen/docs/payment-methods/payco/ios-component/2026-09-15.md"
tags: [adyen, payco, ios, components, redirect]
---

## Overview

Adyen's 2026-09-15 PayCo iOS Component page gives method-specific additions for existing iOS Components Sessions and Advanced integrations. It uses `InstantPaymentComponent` with the `kcp_payco` method and relies on the respective base flow for redirect and result handling. This snapshot does not establish current merchant eligibility, a live setup procedure, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing iOS Components Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and PayCo added in Customer Area. The page says no PayCo-specific extra `/sessions` parameters or Component configuration are needed. Its Swift example guards for `.other("kcp_payco")`, sets the session as delegate, and initiates the `InstantPaymentComponent`; the guard is a method-availability check in the example, not merchant enablement proof. [Raw lines 25–69]
- **Advanced:** Requires an existing iOS Components Advanced flow, redirect handling, and PayCo added in Customer Area. It says no extra PayCo-specific configuration or ordinary `/payments` parameters are needed. Its Swift example sets the enclosing object as Component delegate before initiating payment. The Advanced **Components** prerequisite label links to a **Drop-in** URL, while its redirect and payment links point to Components; preserve the mismatch rather than changing the stated integration type. [Raw lines 78–121]
- **Testing:** The page says PayCo has no specific test credentials and directs testing assistance to Adyen Support. It does not state a TEST simulator, live activation gate, final result-code sequence, webhook outcome, capture or settlement rule. Starting the Component or receiving a redirect is not evidence of a successful payment. [Raw lines 72–76, 123–127]

## Detail locators

- Sessions versus Advanced delegate examples: raw lines 58–70 and 104–115. No iOS SDK minimum is stated here; Checkout API v68+ appears only in the Sessions prerequisites.
- Country/currency and `kcp_payco` server request details require separate evidence. This page's method type is established by its Swift examples, not a full country/eligibility table.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/ios-component/2026-09-15|PayCo iOS Component (2026-09-15)]]
