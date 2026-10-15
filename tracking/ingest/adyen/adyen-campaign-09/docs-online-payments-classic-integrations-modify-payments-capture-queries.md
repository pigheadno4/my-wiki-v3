# Fixed retrieval checks: Classic API capture

## Q1 — Route, capture modes, and lifecycle scope

**Query:** What capture routes does the dated Adyen Classic guide describe, and should a new integration use Classic `/capture`?

**Expected answer:** The Classic capture endpoint is marked inactive and unsupported for new integrations; Adyen directs new integrations to Checkout API and existing users to migration guidance. For payment methods supporting separate authorization and capture, the guide describes default immediate automatic capture, a merchant-account automatic delay of 1–7 days, manual `POST /capture`, and `captureDelayHours` in an individual payment request. Merchant-account capture settings require the Merchant admin role. Automatic capture and `captureDelayHours` ordinarily have no separate `CAPTURE` webhook, though Support can enable it for the documented delayed paths. The snapshot does not establish current endpoint availability or account configuration.

**Raw locators:** deprecation and migration, lines 15–24; modes and method qualification, lines 30–43; automatic delay and webhook qualification, lines 44–73; manual setup and `captureDelayHours`, lines 75–107. **Canonical retrieval route:** [[adyen-payment-capture]] → [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/2026-09-15|pinned raw]].

## Q2 — Request identity, partial capture, and final outcome

**Query:** How does Classic `/capture` identify the authorization and capture request, what happens to the remaining balance after a partial capture, and does `[capture-received]` or `CAPTURE success: true` guarantee final funds transfer?

**Expected answer:** `POST /capture` sends `merchantAccount`, `modificationAmount`, and `originalReference` equal to the authorization payment's `pspReference`; an optional `reference` helps reconcile the modification. The response's capture `pspReference` is a distinct modification identifier and `[capture-received]` only acknowledges receipt. A later `CAPTURE` webhook pairs original and capture references; `success: true` means the request was valid and sent onward, while `success: false` includes a failure reason. A rare scheme rejection can still produce `CAPTURE_FAILED` days later. Single partial capture automatically cancels the unclaimed balance; multiple partial captures preserve it and require Support enablement. Partial capture is payment-method dependent and uses less than the authorized amount. Do not expose refusal details to shoppers.

**Raw locators:** Classic request/response, lines 109–143; `CAPTURE` webhook, lines 145–158; partial capture, lines 214–235; later failures and refusal warning, lines 237–264. **Canonical retrieval route:** [[adyen-payment-capture]] → [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/2026-09-15|pinned raw]].
