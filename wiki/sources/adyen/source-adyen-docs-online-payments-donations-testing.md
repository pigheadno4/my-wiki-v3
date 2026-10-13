---
title: "Adyen Docs: Test your Giving integration"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/donations/testing"
raw_files:
  - "adyen/docs/online-payments/donations/testing/2026-09-15.md"
tags: [adyen, giving, donations, testing, webhooks]
---

## Overview

This Adyen guide describes checks for a Giving integration **before going live**, separately in test and live environments: create and activate a donation campaign, make a donation, then observe the donation outcome. It routes through [[adyen-giving]] and [[adyen-payment-testing]]. Test cards and test webhooks exercise the test integration; they do not establish that a live nonprofit received funds. The live-environment step instructs a real donation to the merchant's nonprofit, so it is distinct from a test-card fixture.

## Key takeaways

- In the **test environment**, the merchant creates a campaign with a demo nonprofit in test Customer Area and starts it. Activation starts returning a `donationToken` in eligible `/payments` or `/payments/details` responses. The guide then asks the merchant to verify that token, check the `/donationCampaigns` response details, make test donations with the listed test cards, and verify a **DONATION webhook for each test donation**. A token or campaign response is an intermediate check, not the donation outcome.
- Testing donations with **iDEAL** needs additional configuration from Adyen Support. The test-card table includes a Visa fixture for which the text says CVC is not required, plus 3D Secure 2 enrolled fixtures and a TRA-exemption test request using `threeDSRequestorChallengeInd: "05"`; consult the raw table and conditions rather than treating examples as live card or exemption behavior.
- In the **live environment**, the merchant creates and starts a campaign for its nonprofit in live Customer Area and separately enables the **Adyen Giving merchant webhook** there. If Giving is absent from live Customer Area, the guide directs the merchant to its Adyen contact or Support. After verifying `donationToken` and campaign details, the merchant makes a donation to its nonprofit through the integration. It can verify the outcome through the **DONATION webhook or Giving report/dashboard**.
- For issues with **test donation requests**, the guide points to API logs. The page prescribes checks; it does not report that any merchant completed them or that a nonprofit received a live donation.

## Detail locators

- **Purpose and checklist, raw lines 15–23** — test and live recommendation, campaign activation, donation, and merchant webhook outcome.
- **Test campaign and donation, raw lines 25–50** — test Customer Area, demo nonprofit, `donationToken`, iDEAL Support setup, test cards, and DONATION webhook.
- **Live campaign and outcome, raw lines 52–84** — live Customer Area, Support fallback, live merchant webhook enablement, actual donation, and webhook/report verification.
- **Troubleshooting and fixtures, raw lines 86–129** — API logs, ordinary donation test cards, Visa CVC note, 3D Secure 2 cards, and TRA-exemption request value.

## Related

- [[adyen]]
- [[adyen-giving]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/online-payments/donations/testing/2026-09-15|Adyen Docs — Test your Giving integration (2026-09-15)]]
