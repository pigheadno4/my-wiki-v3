# Fixed retrieval checks: Checkout API v72 validation guide

## Q1 — Purpose and scope

**Query:** What does this Adyen Checkout API v72 upgrade page tell an existing online-payments integration to do, and what does it not prove?

**Expected answer:** It tells a Checkout API online integration to make request values satisfy new v72 validations, with a table of fields and limits. It does not say only v71 can be the starting version, give an SDK-family migration path, enumerate API error/action handling, or prove an integration has been upgraded and is succeeding in test or live processing. Its prerequisites include Checkout webservice API-credential role and Merchant admin or Manage API credentials Customer Area role.

**Raw locators:** `# Upgrade to Checkout API v72`, lines 15–19; `## Requirements`, lines 21–28; `## Validate the data that you send`, lines 30–57. **Canonical retrieval route:** [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-checkout-api-v72]] → [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-checkout-api-v72/2026-09-15|pinned raw]].

## Q2 — Central validation changes and warning

**Query:** Which v72 value checks are notable, and what should be done with the inconsistent date example?

**Expected answer:** Read the exact row for each request field. This snapshot gives `captureDelayHours` max 672 (28 days), `reference` max 80 characters, `metadata` key/value limits 20/80, and `returnUrl` RFC 2396 format, URL encoding of spaces/special letters and max 1024 characters; it also lists address, entity type, email and other field constraints. `dateOfBirth` requires ISO-8601 `YYYY-MM-DD`, but its sample `2005-03-01` is wrongly captioned March 1, 2025; preserve the discrepancy and use the format rule, not the inconsistent caption. A locally valid request value does not establish a successful provider response or financial outcome.

**Raw locators:** `## Validate the data that you send`, lines 30–57, particularly `captureDelayHours` line 38, `dateOfBirth` line 39, `metadata` lines 44–45, `reference` line 46 and `returnUrl` line 47. **Canonical retrieval route:** [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-checkout-api-v72]] → [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-checkout-api-v72/2026-09-15|pinned raw]].
