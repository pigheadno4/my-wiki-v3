---
title: "Adyen Docs: Donations in Standard Drop-in"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/donations"
raw_files:
  - "adyen/docs/standard/integration/drop-in/donations/2026-09-15.md"
tags: [adyen, giving, donations, drop-in, checkout]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] Standard Drop-in guide describes presenting an Adyen Giving campaign after a successful original payment. If the shopper opts in, the donation amount is charged to the same payment method used for that payment. Drop-in handles the donation form and processing; the merchant receives a client callback and a distinct donation-outcome webhook. This is a guide for [[adyen-giving]], not evidence that a particular merchant, shopper, method, or nonprofit is eligible.

## Key takeaways

- The stated integration is a standard payments integration with Drop-in. The page calls for the Donation campaigns manager Customer Area role, general Giving requirements, Standard webhooks, and the Adyen Giving merchant webhook. An active donation campaign is needed for Drop-in to show the donation form after successful payment.
- The server creates a payment session without donation-specific request parameters. The checkout-side global configuration may add a `donation` object; the documented event handlers are `onDonationSuccess` and `onDonationFailure`. `onDonationSuccess` fires both for completed donation and shopper decline, distinguished by `didDonate`; it is not by itself proof that a donation was made.
- With an active campaign after successful payment, Drop-in shows campaign details and amount choices and processes the donation. `autoMount` defaults to true, mounting in Drop-in's container; setting it false suppresses automatic display. The page also provides a display `delay`.
- The Adyen Giving merchant webhook reports donation outcome. In its successful `DONATION` example, `success` is true and `originalReference` associates the donation with the original transaction. Payment outcome arrives in a separate webhook message. A UI callback, the example payload, or an original payment result does not establish completed donation or nonprofit receipt.
- Test and live campaigns are created and activated separately. The testing section says starting a campaign produces a `donationToken` in `/payments` or `/payments/details` responses, then asks merchants to verify campaign data and a donation webhook. Those endpoint references appear alongside the guide's session-creation flow; this snapshot does not reconcile the routes or establish that a merchant must issue a separate `/payments` request in a Drop-in Sessions integration. The live section also offers Giving reporting as an outcome check; the page does not demonstrate actual settlement or bank receipt.

## Detail locators

- **Purpose, role and webhook prerequisites** — raw lines 15–31.
- **Drop-in session, payment and donation sequence** — raw lines 33–77.
- **Configuration, callbacks and display behavior** — raw lines 79–130.
- **Donation outcome and example payload** — raw lines 132–180.
- **Separate test/live campaign, token and outcome checks** — raw lines 182–249; troubleshooting and test cards at 251–288.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-giving]]
- Related source: [[source-adyen-docs-online-payments-donations-integration-options-sessions-flow]]

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/donations/2026-09-15|Adyen Docs — Standard Drop-in donations (2026-09-15)]]
