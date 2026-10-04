# Braintree C34 query audit — Group A

Scope: `articles-guides-at-most-once`, `articles-guides-refund-authorizations`, `articles-guides-account-updater`, `articles-adyen-reconciliation`; eight fixed questions from `selection-review.md`. Verdict: **8/8 PASS**.

## `articles-guides-at-most-once`

Route: [[index]] → [[braintree-index]] → [[braintree-at-most-once-processing]] → [[source-braintree-articles-guides-at-most-once]] → [[raw/braintree/articles/guides/at-most-once-2026-09-16]].

1. **PASS — identity/scope.** Object/action: Braintree At-Most-Once Processing is logical-intent idempotency for duplicate payment-operation API requests, keyed by the merchant-supplied `ApiRequestKey`, not network-response replay (raw lines 20–35). The page is limited to a select/specific audience, is not generally public, and directs sharing questions to the product team (14–15); it documents no region, pricing model, merchant eligibility, enablement or SDK-support guarantee.
2. **PASS — action/conditions/warnings/locators.** Object/action: the merchant reuses the same key for the same logical action; identical keys inside 30 days are duplicates, with same-details in-flight, completed, and changed-details behavior at 33–42. The feature is mutually exclusive with transaction duplicate checking (20–30); returned state can be unsuccessful or advanced, and a new key is safe only under action-specific record/state rules. Supported operations are at 45–57; scenario matrices and retry qualifications are Authorize 59–87, Charge 90–106, Refund 109–122, Submit for Settlement 125–141, Partial Settlement 144–157, Credit 160–171, Reverse 174–194; errors `915232`–`915234` are at 197–203.

## `articles-guides-refund-authorizations`

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-articles-guides-refund-authorizations]] → [[raw/braintree/articles/guides/refund-authorizations-2026-09-16]].

1. **PASS — identity/scope.** Object/action: Braintree refund authorization lets an issuer accept or decline a card refund before refund processing (raw lines 24, 44–66). The captured scope is all US merchants and selected Australian merchants; authorization and capture can incur merchant fees in some markets (17–20). Named networks are Visa, Discover, Mastercard and Amex, and named methods are credit cards, Apple Pay and Google Pay (27–41); the snapshot does not establish current rollout outside those qualifications.
2. **PASS — action/conditions/warnings/locators.** Object/action: first refund the original sale through Braintree's refund API or Control Panel; after an issuer decline, an alternate refund method may be used, subject to the disclosed merchant refund policy (105–121). A current refund API success reports request success, not overall refund outcome (124–130); real-time processor responses are future/release-qualified by network and region (132–135), and some declined authorizations may be force-captured by response code (65–66). SDK thresholds, processor codes, GraphQL scope and legacy validation errors are at 137–176; sandbox sale/settlement/refund amount instructions are at 179–190.

## `articles-guides-account-updater`

Route: [[index]] → [[braintree-index]] → [[braintree-account-updater]] → [[source-braintree-articles-guides-account-updater]] → [[raw/braintree/articles/guides/account-updater-2026-09-16]].

1. **PASS — identity/scope.** Object/action: Braintree Account Updater requests new account numbers and/or expiry dates from participating issuers for eligible vaulted cards and applies returned updates (raw lines 14–16, 50–52). It is a non-default Braintree Direct feature for merchants based in the US or transacting primarily with US customers; pricing varies by pricing model (19–26, 45–47). Issuer participation still controls eligibility; only Visa, Mastercard and Discover are listed, while prepaid, Apple Pay and Google Pay cards are excluded (29–40).
2. **PASS — action/conditions/warnings/locators.** Object/action: after enablement, Braintree submits initial batches of 600,000 and then rolling requests using expiry, recurring-billing, activity and Next Day Card Refresh criteria (50–78); Vaults over 2 million methods get the narrower initial 13-month expired-card scope (55–56). Next Day Card Refresh requires retry logic and its qualifying decline codes are at 81–99. Reporting routes are at 102–154, including the 40,000-row Control Panel cap and 24-hour webhook CSV scope; event outcomes are at 159–173, including four outcomes that stop resubmission until manual Control Panel/API update. Requests do not guarantee issuer participation, an updated card or a successful later payment.

## `articles-adyen-reconciliation`

Route: [[index]] → [[braintree-index]] → [[payment-reconciliation-reporting]] → [[source-braintree-articles-adyen-reconciliation]] → [[raw/braintree/articles/adyen/reconciliation-2026-09-16]].

1. **PASS — identity/scope.** Object/action: this Braintree-hosted Adyen account article documents the Settlement Details Report used to reconcile Adyen-processed payouts, not the separate PayPal Orchestration Adyen integration and not independent Adyen authority. The report is generated upon payout and requires Create, Run, and Download Reports permission (raw lines 14–24); reporting is separate per MID when more than one MID processes transactions (74–76). The raw states no regional eligibility or universal pricing model; its €0.10/1000-transaction minimum is explicitly an example conditioned on agreed pricing (45–49).
2. **PASS — action/conditions/warnings/locators.** Object/action: an authorized user runs **Reports → Settlement Details Report → Run Report** and reconciles report payout/reference amounts to bank records (16–34). The report covers included captures/refunds/chargebacks, fees, corrections and reported transfer amount (25); report values are reconciliation evidence, not proof that a particular bank deposit arrived. Fee period/totals are at 37–39; reserve/outstanding-fee, invoice and inter-batch adjustments at 42–59; transaction types and detailed amount/currency/reference/commission/payment-method fields at 62–136. Adyen `Psp Reference` and Braintree `Merchant Reference` are distinct at 79–86.

## Shared evidence checks

- Manifest SHA-256: at-most-once `e6c138ab587cc2f155b7b82d174ffb4868f7d4fc5191d3f5cb408a52507ab2a8` **MATCH**; refund-authorizations `edde1a14ebf8751076acf5d37dbf8fd1635380198cc86eeb47c5907ac8ca65d0` **MATCH**; account-updater `8dba196742d04b02a470a8513fa3f78cf3ae6604f28cf2367b18402c74f86888` **MATCH**; Adyen reconciliation `79fb24b1450f9c9946b4fde1649bfcc8f3df08edbbfffd160bf91718cc69fd58` **MATCH**. Embedded source URLs match source-page canonical URLs.
- Reciprocal links: each applicable concept links its promoted source and each source links back to that concept; root and Braintree catalogs expose the required route. Each source's `raw_files` and Raw Sources link resolve to the pinned raw.
- Gap sweep: bounded filename/path and content sweeps found the selected raws plus adjacent duplicate-checking, AIB-AF idempotency, transaction-refund, Control Panel refund, expiring-card, Account Updater webhook, settlement-summary and Orchestration-Adyen routes. The selected raws directly answer all fixed questions; no relevant contradiction requires another authority. The AIB-AF and Orchestration pages are distinct processor/product routes and were not imported.
- Extra full reads: none. Only the four selected pinned raws were fully read; adjacent raws remained navigation/gap-sweep hits because no answer or conflict required them.

Overall verdict: **PASS — 8/8 questions supported; no material retrieval, hash, identity, scope, locator or reciprocal-link failure.**

Analysis ended UTC: `2026-10-04T05:15:47Z`
Artifact completed UTC: `2026-10-04T05:16:50Z`
