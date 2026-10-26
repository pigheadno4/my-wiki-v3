---
title: "Adyen iDEAL | Wero iOS Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ideal/ios-drop-in/2026-09-15.md"
tags: [adyen, ideal, wero, ios, drop-in, sepa-direct-debit, recurring-payments]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing iOS Drop-in integration, separately for Sessions and Advanced server-side flows. It also routes recurring payments through SEPA Direct Debit tokenization, rather than documenting reuse of an iDEAL redirect itself. The snapshot does not establish current merchant eligibility or an executed payment. [[adyen]] [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions:** Requires an existing iOS Sessions Drop-in integration using Checkout API v68 or later and iDEAL | Wero added in Customer Area. The page says no iDEAL | Wero-specific additional `/sessions` parameters or configuration are needed. These statements do not waive the base integration's own request requirements. (raw lines 25–46)
- **Advanced:** Requires an existing iOS Advanced Drop-in integration, `action.type: redirect` handling and Customer Area setup. It says no method-specific additional configuration or ordinary `/payments` parameters. The Advanced requirements table does not separately state the Sessions Checkout API v68+ minimum. (raw lines 322–344)
- **Recurring boundary:** The page says recurring iDEAL | Wero payments use SEPA Direct Debit. Use the standard SEPA tokenization parameters for token creation; a `recurring.token.created` webhook provides `storedPaymentMethodId`. Reuse is limited here to shopper-absent `UnscheduledCardOnFile` or `Subscription` payments, again using standard tokenization parameters with no additional SEPA-specific fields. Its examples use `paymentMethod.type: sepadirectdebit`, a stored method ID and `ContAuth`; they are examples of the SEPA path, not a claim that an iDEAL redirect token is charged. The ordinary no-extra-parameters statements do not erase this separate token route. (raw lines 48–98, 346–396)
- **Outcome:** A successfully received recurring `/payments` request can return `resultCode: Received` with a `pspReference`; the page says to track payment success through webhooks. Receipt is therefore an intermediate state, not authorization, capture or settlement. The guide's bank-payment test steps likewise direct later status checks rather than demonstrating completed execution in this snapshot. (raw lines 275–280, 290–320, 573–578)
- **TEST and live:** The guide calls the iDEAL | Wero TEST environment unreliable, recommends live penny tests, and says TEST simulations may be possible when the environment is running. It lists a live bank-account/payment-page/QR-or-issuer/authorization/status-check sequence and a TEST `TESTNL2A` issuer with simulated success, cancellation, expiration and refusal results. The live test is a recommendation involving actual funds; no test or live payment was performed for this ingestion. The section heading says 'Request iDEAL | Wero for the live environment' but provides no accompanying request procedure or explicit approval condition; do not infer one from the heading alone. (raw lines 282–320, 580–618)
- **Example limits:** The SEPA examples are versioned TEST samples across server libraries, not proof of exact current SDK behavior. The Java sample omits `shopperReference` while other language samples include it; verify the applicable standard tokenization request before implementation. (raw lines 77–273, 375–571)

## Detail locators

- Sessions prerequisites and no-extra statements: raw lines 25–46.
- Sessions SEPA token route, recurring examples and `Received` outcome: raw lines 48–280.
- Sessions TEST/live testing qualifications: raw lines 282–320.
- Advanced prerequisites and no-extra statements: raw lines 322–344.
- Advanced repeated SEPA token route and examples: raw lines 346–578.
- Advanced repeated TEST/live qualifications: raw lines 580–618.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/ios-drop-in/2026-09-15|Adyen iDEAL | Wero iOS Drop-in guide, 2026-09-15 snapshot]]
