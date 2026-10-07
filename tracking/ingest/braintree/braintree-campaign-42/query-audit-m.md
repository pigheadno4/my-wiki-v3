# Braintree campaign 42 query audit M

- Scope: manifest entries 49–50 only; exactly two questions per canonical source page.
- UTC started: `2026-10-07T01:25:55Z`
- UTC completed: `2026-10-07T01:27:44Z`
- Overall verdict: **PASS — 4/4 queries passed.**
- Extra authority reads: none.

## Shared checks

Both pinned raw files and both canonical source pages were read in full. Computed SHA-256 values exactly match the manifest: `05bb7862…b07a` and `8a05d24d…dc01`. Each source has a valid root → provider → primary concept → source → raw route and reciprocal source/concept links. For Functions, [[braintree-payment-platform]] is correctly primary and [[braintree-fraud-tools]] is contrast navigation only.

Answers remain within each assigned Braintree website snapshot and make no current-state, account-eligibility, sibling-platform, successful-execution, authorization, settlement, or funding inference. A bounded filename/related-reference sweep found no additional authority needed to answer these four questions and no source-to-raw material conflict. Illustrative raw syntax or identifier defects are nonblocking because neither source makes a false source claim or runnable-code guarantee. Provider source-catalog closure remains deferred to the coordinator.

## Manifest 49 — Functions: act on a vendor fraud score

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:759` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-functions-act-on-fraud.md:12-40` → `raw/braintree/docs/guides/functions/act-on-fraud-2026-09-16.md`.

1. **PASS — What exact scope does this page establish, without availability or outcome inference?** It is a Braintree Functions documentation preview for initializing `MyFraudCheck` as a `paymentMethod` Function with a `beforeAuthorization` trigger, then using transaction-call data to request an external vendor fraud decision. It does not establish current Functions availability, account eligibility, a live vendor contract, a completed authorization, or any settlement/funding outcome. Evidence: source `Overview`, `Key takeaways`, and `Detail locators`; raw lines 14–34.

2. **PASS — What central action, material test/deploy conditions, warnings, and detail routes must be preserved?** In the illustration, a vendor decision of `YES` writes `fraudDecision` to transaction custom fields; the other branch writes the same field and sets `GatewayRejected`, while both branches return HTTP `200`. The page directs local testing with `btfns test`, offers generated mock data, defaults deployment to sandbox, requires an explicit production selection or `--production`, and invokes the Function from a sale with `functionName`, using Custom Fields for extra data absent from the Transaction API. The raw sample has unresolved identifier/file/name inconsistencies, so it is illustrative rather than a runnable guarantee; the source states that boundary and routes the details. Evidence: source `Key takeaways` and `Detail locators`; raw lines 35–192.

## Manifest 50 — Shopper Insights (Beta), iOS v7

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:772` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-shopper-insights-ios-v7.md:12-42` → `raw/braintree/docs/guides/shopper-insights/ios/v7-2026-09-16.md`.

3. **PASS — What exact product and platform scope does this captured page establish?** This 2026-09-16 iOS v7 route documents Shopper Insights as beta and says the feature is available for merchants using iOS SDK v6+ or Android SDK v4+, not JavaScript or Drop-in. It describes requesting PayPal or Venmo recommendations from customer information, but does not prove current availability, merchant/customer eligibility, a recommendation result, or payment execution. Customer consent is required before sharing the information with PayPal services, and the feature requires a client token rather than a tokenization key. Evidence: source `Overview`, `Key takeaways`, and `Detail locators`; raw lines 14–18 and 31–52.

4. **PASS — What central session/recommendation action, presentment conditions, warnings, and analytics routes must be preserved?** The Swift examples create or update a customer session from hashed email/phone inputs and then request recommendations that may identify PayPal or Venmo. The captured terms require checking PayPal-network eligibility before other methods; confirmed recommendations receive preferential placement and, when available, preselection, while unconfirmed eligibility leaves PayPal at least at parity. The page also routes displayed and selected/tapped button analytics and preserves a prose/code mismatch between `sendPresentedEvents` and `sendPresentedEvent`. Its March 30, 2026 certificate-expiry warning and iOS `6.17.0+` upgrade direction are historical snapshot evidence, not current certificate or traffic status. The client-class variation in the examples is likewise illustrative and not a callable-signature guarantee. Evidence: source `Key takeaways` and `Detail locators`; raw lines 23–26 and 53–153.
