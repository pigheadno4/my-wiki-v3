# Fixed retrieval checks: Classic authorisation adjustment

## Q1 — Purpose and scope

**Query:** What is this Classic Adyen authorisation-adjustment guide for, and can it establish that a new integration should use the endpoint?

**Expected answer:** It documents an existing Classic Payment API flow to pre-authorise a payment, change its authorised amount and manually capture the final amount. The endpoint is marked inactive and unsupported for new integrations; new builds are directed to Checkout API and existing users to Adyen about migration. This dated snapshot cannot establish a merchant's eligibility, active endpoint status or a successful transaction. The flow is conditional on payment method, card scheme/MCC and issuer support.

**Raw locators:** `# Pre-authorisation and authorisation adjustment`, lines 15–28; `## Availability`, lines 297–325. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-modify-payments-adjust-authorisation]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/adjust-authorisation/2026-09-15|pinned raw]].

## Q2 — Central operation and warnings

**Query:** How does the Classic pre-authorisation adjustment flow identify a payment, set the new amount, establish an outcome, and handle capture or expiry?

**Expected answer:** Pre-authorise first and retain its PSP reference. Both `/adjustAuthorisation` and final `/capture` use that original reference; adjustment and capture responses each carry their own distinct PSP references. `modificationAmount` is the new total amount in minor units, not the increment; zero-value adjustment is prohibited. An asynchronous adjustment's received response needs a webhook to establish success. Synchronous adjustment needs Support enablement and the latest `adjustAuthorisationData` blob; omitting it permanently falls back to asynchronous for that payment. The synchronous `Authorised` response reports the adjustment result, while capture still needs webhook confirmation. An expired pre-authorisation cannot be adjusted; scheme validity differs from Adyen's default expiration, and a refused Visa or American Express extension can terminate the original authorisation. Do not infer capture from authorization or from a received response.

**Raw locators:** `## Asynchronous or synchronous adjustment`, lines 57–69; `## Requirements`, lines 71–78; `## Step 1`, lines 90–129; `## Step 2`, lines 131–252; `## Step 3`, lines 254–295; `## Expiration of authorizations`, lines 327–342. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-modify-payments-adjust-authorisation]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/adjust-authorisation/2026-09-15|pinned raw]].
