---
title: "Adyen Classic Platforms: Manual payouts to cards"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards"
raw_files:
  - "adyen/docs/classic-platforms/payouts/manual-payout/payout-to-cards/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, cards, account-holders]
---

## Overview

This 2026-09-15 capture of a 2021-modified **Classic Adyen for Platforms** guide describes manually paying an account holder to an eligible Mastercard or Visa debit card, separate from bank-account payouts. It uses the account holder's Classic `accountCode`/`accountHolderCode` and a stored card `payoutMethodCode`; it is not the newer balance-platform Transfers API model. The page says card payouts are available with Fund API v5 and later, and directs new implementers to a separate integration guide. See [[adyen-classic-platforms]] and [[adyen]].

## Key takeaways

- The platform must contact Adyen Support to enable card payouts (raw lines 25–27). The page describes cardholder receipt within 30 minutes without bank-cutoff dependency (raw line 23); that is dated product guidance, not evidence or a guarantee of a particular card credit.
- First, submit a zero-value `/payments` request using the platform merchant account, a unique account-holder `shopperReference` of at least three characters, card `paymentMethod`, and `enablePayOut: true` to check eligibility and store card details (raw lines 29–79). Raw card data may be passed only if the platform is fully PCI compliant; otherwise use Adyen's Card Component to collect and encrypt it (raw line 38). Check `payoutEligible`: `Y` means eligible, `D` means Mastercard domestic-only, and `N` or `U` means unusable for payout (raw lines 81–86). A sample `fundsAvailability: I` means instant-payout eligibility in that example, not receipt (raw lines 63–76).
- For an eligible card, take `recurring.recurringDetailReference` as tokenized card details and submit it through Classic Account API `/updateAccountHolder` to add the card payout method (raw lines 88–113). A 200 response can contain `payoutMethodCode`, but the guide says to wait for `ACCOUNT_HOLDER_UPDATED` before business logic; a 202 response is queued and also needs the notification for confirmation and its code (raw lines 115–140). The example's returned `recurringDetailReference` differs from the submitted value (raw lines 105–106, 125–129), so do not use the sample identifiers as an identity invariant.
- Submit `/payoutAccountHolder` with `accountCode`, `accountHolderCode`, amount, reference and the `payoutMethodCode` (raw lines 142–160). The example response has `resultCode: Received`; the page then instructs waiting for `ACCOUNT_HOLDER_PAYOUT` to confirm payout status (raw lines 162–174). `Received` is not card-credit proof. The earlier text says the recurring detail reference is needed for future payout requests (raw line 88), whereas the explicit Step 3 request uses `payoutMethodCode`; retain this unresolved identifier distinction rather than substituting one for the other.

## Detail locators

- Classic-only scope, Fund API version, timing claim and Support enablement: raw lines 15–27.
- Zero-value card check, PCI boundary, response example, eligibility values and token: raw lines 29–88.
- Add card as payout method and 200/202 versus `ACCOUNT_HOLDER_UPDATED`: raw lines 90–140.
- Payout request, `Received` example and `ACCOUNT_HOLDER_PAYOUT` outcome notification: raw lines 142–174.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic account-holder/account model.
- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — separate payout status and return tracking.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/manual-payout/payout-to-cards/2026-09-15|Classic Platforms manual payout to cards, captured 2026-09-15]]
