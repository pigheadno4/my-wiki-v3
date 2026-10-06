# Braintree C41 fixed-query audit E — positions 17–20

- Audit mode: read-only; exactly eight questions, two per selected page
- Prompt UTC: collaboration runtime did not expose the receipt timestamp; first recorded audit check was `2026-10-06T15:15:25Z`
- Analysis ended UTC: `2026-10-06T15:16:57Z`
- Handoff UTC: `2026-10-06T15:16:57Z`

## Shared checks (run once)

- **PASS — pinned identity and immutability.** Manifest positions 17–20 are the four assigned jobs. The selected raws' SHA-256 values exactly match the manifest: `9a533d3f…ab003`, `a1ac4876…ddfb2`, `5bf2c228…ddac`, and `ea63f3bd…43448`. Each raw `Source URL` matches the manifest canonical URL, and each promoted source frontmatter points to the one pinned raw.
- **PASS — complete selected evidence reads.** All four selected raws and all four promoted source pages were read in full. Relevant root/provider indexes and the three main concepts (`braintree-in-person`, `paypal-fastlane`, `braintree-payment-platform`) were inspected. No linked page was treated as evidence without a full read.
- **PASS — bounded gap sweep.** The filename sweep found the expected neighboring In-Person transaction/offline/receipt pages and Fastlane flexible/reference/best-practices/FAQ pages. The assigned questions ask what these four selected snapshots themselves document; their selected raws are sufficient, so no extra authority was needed. Linked neighbors remain navigation/detail routes, not evidence silently imported into these answers.
- **No third synthesis or style pass.** This is the requested fixed-query content audit only.

## Deferred catalog/index edges (not content failures)

- Root `[[index]]` links both `[[braintree-index]]` and `[[paypal-index]]`. `[[paypal-index]]` links `[[paypal-fastlane]]`; `[[braintree-index]]` links `[[braintree-payment-platform]]`.
- `[[braintree-index]]` does not yet link `[[braintree-in-person]]`, and it does not yet directly catalog the four new C41 source pages. The concept-to-source and source-to-pinned-raw edges are present for every page. These provider-catalog aggregate edges are deferred to campaign close and are reported separately from the content verdicts below.

## 17. `in-person-guides-additional-api-calls`

**Actual route:** `[[index]] → [[braintree-index]] →` **deferred missing edge** `→ [[braintree-in-person]] → [[source-braintree-in-person-guides-additional-api-calls]] → raw/braintree/in-person/guides/additional-api-calls-2026-09-16.md`.

1. **PASS — exact scope and non-inference.** This is a collected, unversioned Braintree In-Person website guide containing GraphQL examples for `pingInStoreReader`, a reader-local offline `{ping}`, `inStoreLocations`, `search.inStoreReaders`, and `search.transactions`. The object/action match is exact: reported reader reads and a no-charge ping, then location/reader/transaction record reads. It is not exact-commit schema authority and must not be extended to current support/account eligibility, real-time reader health, pairing, charge/context state, authorization, capture, settlement, funding, or completed reconciliation. Evidence: raw title/scope at lines 14–16; operations at lines 19–53; source overview and boundaries at lines 12–22.

2. **PASS — central action, conditions, warnings, and detail retrieval.** The page's purpose is to retrieve reader status/firmware, validate reachability of the offline endpoint without sending a charge, list locations/readers, and search transaction records as one reconciliation aid. Consequential qualifications are retained: ping data is several minutes stale and offline routing should use request-charge reader status (raw 19–26); the offline prose calls the call a mutation while the example is labeled/query-shaped and its displayed `readerId` is not consumed (27–33); reader filtering uses `locationId.is` (39–45); and the transaction search's `>= 800.00` plus `SETTLED`/`VOIDED` criteria are illustrative, not an execution or reconciliation result (46–53). Precise fields, variables, responses, pagination, and filters are retrieved at those raw sections.

## 18. `docs-guides-fastlane-advanced-option`

**Actual route:** `[[index]] → [[paypal-index]] → [[paypal-fastlane]] → [[source-braintree-docs-guides-fastlane-advanced-option]] → raw/braintree/docs/guides/fastlane/advanced-option-2026-09-16.md`. The absent direct Braintree catalog edge is deferred above.

3. **PASS — exact scope and non-inference.** This is an unversioned Braintree-hosted Fastlane browser/component advanced-options snapshot; it captures no Braintree Web SDK or Fastlane runtime version. Its payment-path objects/actions are an authenticated member profile and saved-card selection or `FastlaneCardComponent`, acquisition of a `paymentToken`, and handoff of that token plus device data to the merchant server. Its server examples use Braintree `transaction.sale()` and customer/payment-method routes; they must not be rewritten as the direct PayPal Orders API pattern. Do not infer current availability, merchant enablement, buyer eligibility, SDK compatibility, rendering, vaulting, or payment success. Evidence: raw 126–218 and 236–256; source 12–30.

4. **PASS — central action, conditions, warnings, and detail retrieval.** The flexible template renders a saved card only when member authentication succeeded and a card exists; otherwise it renders card fields, then gets a token from the selected card ID or `getPaymentToken` and sends it server-side (raw 126–218). Material local conditions are preserved: CSP directives and the Hosted Card Fields exception (16–35), exact locale values (36–51), watermark/preload behavior (54–113), US billing versus merchant-supported shipping and new-address server handoff (115–124), recommended server fields (220–226), `pickupInStore`/`shipToStore` safeguards (229–235), optional transact-and-vault versus vault-first routes (236–246), and PayPal-member/no-Fastlane-profile outcomes (247–256). A token is an input to later processing, not an authorization/capture/settlement/funding result. Exact code, values, and routes remain at those raw locators.

## 19. `in-person-guides-graphql-error-handling`

**Actual route:** `[[index]] → [[braintree-index]] → [[braintree-payment-platform]] → [[source-braintree-in-person-guides-graphql-error-handling]] → raw/braintree/in-person/guides/graphql-error-handling-2026-09-16.md`.

5. **PASS — exact scope and non-inference.** This is a collected, unversioned Braintree In-Person GraphQL API error-interpretation guide for a point-of-sale application. The object/action match is exact: interpret response layers, locate stable diagnostic codes/IDs, and log request/response context. It is not exact-schema or SDK authority, current reader/merchant support evidence, retry policy for unlisted cases, or proof of a successful reader operation, transaction, settlement, or funding. Evidence: raw 14–53; source 12–25.

6. **PASS — central action, conditions, warnings, and detail retrieval.** The central rule is that HTTP 200 is transport behavior, not operation success: inspect JSON `data`, `errors`, and `extensions`, and preserve mixed data/error partial success (raw 14–30). Do not parse the unstable human-readable `message`; use `extensions.legacyCode` for the page's catalog and preserve `extensions.requestId` (30–48). The POS logging recommendation covers `requestId`, `transactionId`, and API request/response (51–53). Exact reader/context/location/pagination/configuration/printing conditions and codes are in the table (56–87), while processor response codes are a separate layer and the amount note is a simulation direction (90–96), not production or payment-success proof.

## 20. `docs-guides-fastlane-testing-go-live`

**Actual route:** `[[index]] → [[paypal-index]] → [[paypal-fastlane]] → [[source-braintree-docs-guides-fastlane-testing-go-live]] → raw/braintree/docs/guides/fastlane/testing-go-live-2026-09-16.md`. The absent direct Braintree catalog edge is deferred above.

7. **PASS — exact scope and non-inference.** This is an unversioned Braintree-hosted **Sandbox checklist** for Fastlane guest/member identity, consent/profile creation, OTP fallback, saved address/card changes, missing supported data, and test-card inputs; it identifies no Braintree Web SDK or Fastlane runtime version. The object/action match is testing fixtures and expected integration behavior, not production launch or payment execution. Despite the `testing-go-live` URL, the captured content provides no production credentials, enablement, eligibility, domain approval, or launch procedure. Do not infer token validity, authorization, capture, settlement, funding, or live-payment success. Evidence: raw 14–116; source 12–27.

8. **PASS — central action, conditions, warnings, and detail retrieval.** Guest testing uses a new Sandbox email, consent toggle, any valid phone number with no SMS, and a test card; the expected profile creation is recorded at raw 19–37. Member testing first requires a created profile; `111111` is the Sandbox success OTP and any other six-digit number simulates failure, with address/card update cases at 40–96. PayPal-member/no-Fastlane-profile handling is only a link to the separate advanced-options route (99–103). Exact card values and as-captured labels are at 106–114; the duplicated number and conflicting brand labels must remain snapshot data, not independently validated network behavior. The table's “should” outcomes are checklist expectations rather than observed successful payments.

## Verdict

**8/8 PASS for content retrieval and direct answers.** One direct provider-index-to-`braintree-in-person` edge and direct Braintree catalog entries remain deferred close work; they do not change the eight content verdicts.
