---
title: "Adyen EPS React Native Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/eps/react-native-drop-in/2026-09-15.md"
tags: [adyen, eps, react-native, drop-in, sessions, advanced, redirect, recurring]
---

## Overview

This 2026-09-15 EPS React Native Drop-in add-on lists only EPS-specific steps for existing Sessions or Advanced integrations. Both rely on the base flow's `action.type=redirect` handling and describe future recurring payments through SEPA Direct Debit. It does not by itself establish a working integration, current EPS eligibility, completed bank redirect or successful recurring payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions flow, Checkout API v68 or later, redirect handling, and EPS added in Customer Area. The Sessions integration-type link is mislabeled: its text says Sessions but its URL points to an Advanced-flow path; the separate redirect and session-creation links do point to Sessions. Do not use that one URL as evidence that Sessions is Advanced.
- Advanced requires an existing React Native Drop-in Advanced flow, redirect handling and EPS added in Customer Area. Its requirements do not state the Sessions v68+ minimum. For ordinary EPS payment creation, the page says no extra `/sessions` parameters in Sessions, no extra `/payments` parameters in Advanced, and no EPS-specific Drop-in configuration in either path. These statements are scoped to the ordinary flow, not the later recurring token recipe.
- The repeated recurring section routes EPS recurring transactions through SEPA Direct Debit, not repeated EPS bank redirects. It strongly recommends explicit shopper permission and clear schedule/amount communication to reduce chargeback risk. Token creation is described via `/payments` with `storePaymentMethod=true` and `shopperReference` of at least three characters; after settlement, `recurring.token.created` supplies `storedPaymentMethodId` and the server must receive token lifecycle events. Future `/payments` uses that ID, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. The Sessions subsection gives this `/payments` token recipe without specifying a Sessions-specific token-creation variant.
- The test Customer Area payment list is a status-check route. Live EPS acceptance requires submitting an EPS request in live Customer Area. This source gives no test outcome, SDK version, bank issuer values or live-processing proof.

## Detail locators

- Page scope and flow split: pinned raw lines 15–25. Sessions prerequisites, mislabeled integration-type URL, v68+ and redirect handling: lines 29–36. No extra Sessions request fields or EPS configuration: lines 38–48.
- Sessions recurring permission, token request, settlement webhook and future fields: pinned raw lines 50–89. Sessions test/live gates: lines 91–95. Advanced prerequisites: lines 97–107; no extra configuration or ordinary `/payments` fields: lines 109–119.
- Advanced repeated SEPA recurring recipe: pinned raw lines 121–160. Advanced test/live gates: lines 162–166. Base flow guides linked in prerequisites own the generic redirect/result implementation.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-eps]] — method overview and capability marks

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/react-native-drop-in/2026-09-15|EPS React Native Drop-in guide, captured 2026-09-15]]
