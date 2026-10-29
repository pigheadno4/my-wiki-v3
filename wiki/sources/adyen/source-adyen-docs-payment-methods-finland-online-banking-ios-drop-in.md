---
title: "Online banking Finland iOS Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/ios-drop-in/2026-09-15.md"
tags: [adyen, finland-online-banking, ios, drop-in, redirect, paytrail]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland to an existing iOS Drop-in** integration. It separates Sessions and Advanced server-side flows, required shopper email, conditional issuer selection, redirect action handling, and Paytrail test guidance. It is a method add-on, not a complete base integration or evidence of current merchant/bank coverage or a successful live payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-finland-online-banking|method overview]].

## Key takeaways

- **Sessions:** use an existing iOS Drop-in Sessions integration with Checkout API **v68 or later** and add Online banking Finland in Customer Area. The `/sessions` table marks `shopperEmail` required. Its v71 sample uses **FI/EUR** and an app-scheme `returnUrl`; the sample email contains `@@`, so it is a placeholder, not a valid address to copy. No additional method configuration is required (raw lines 25–44, 46–67, 340–344).
- **Advanced:** use an existing iOS Drop-in Advanced integration with `action.type: redirect` handling and Customer Area setup. The `/payments` table requires `paymentMethod.type = ebanking_FI` and `shopperEmail`; `paymentMethod.issuer` is **required only for the Issuer redirect flow**, and `returnUrl` has no required mark in this method-specific table and has a 1024-character maximum; the guide does not establish base-flow requiredness. The example response contains `RedirectShopper` and a redirect action, which is a handoff state rather than proof that the shopper completed bank payment (raw lines 354–383, 670–684).
- **Advanced example warning:** the v72 curl and all shown language-specific `/payments` examples include amount, reference, returnUrl, merchantAccount and shopperEmail but **omit the required `paymentMethod` object**. They cannot be treated as complete method-selection requests. The example email again contains `@@`, and library-version labels are example environments, not minimum SDK requirements (raw lines 385–668).
- **Testing:** both flow sections say to test with the Paytrail test environment and sample data before live acceptance, and state that testing **multiple partial refunds is currently unavailable**. This is a test-environment limitation in the captured guide; the separate method overview's matrix marks multiple partial refunds available but gives a “See note” refund pointer with no note in its capture. Neither statement proves live refund availability for a specific merchant (child raw lines 346–352, 686–692; overview raw lines 34–36).
- The separate [[source-adyen-docs-payment-methods-finland-online-banking|method overview]] labels the method **FI/EUR** and describes bank authentication and return after redirect. It gives two unresolved bank-selection locations—merchant checkout dropdown versus Adyen-hosted page—without scoping them by integration. This iOS Drop-in guide's conditional issuer field does not settle that overview ambiguity (overview pinned raw lines 23–36).

## Detail locators

- Sessions prerequisites and required shopperEmail: raw lines 25–44.
- Sessions example requests and placeholder email: raw lines 46–338.
- Sessions no-extra-configuration/test limitation: raw lines 340–352.
- Advanced prerequisites, redirect and conditional issuer/request fields: raw lines 354–383.
- Advanced examples omitting paymentMethod: raw lines 385–668.
- Advanced RedirectShopper response and Paytrail testing/refund limitation: raw lines 670–692.
- Method-level FI/EUR, bank-selection ambiguity and missing refund note: [[source-adyen-docs-payment-methods-finland-online-banking]] and its pinned raw lines 23–36; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/ios-drop-in/2026-09-15|Online banking Finland iOS Drop-in guide, captured 2026-09-15]]
