# Fixed retrieval checks: Classic authorization with third-party-stored details

## Q1 — Purpose and lifecycle boundary

**Query:** What does this Classic guide do with payment details stored by a third party, and can a new integration use this endpoint as its tokenization route?

**Expected answer:** The page describes making new Classic payment authorizations with card details held by a third party. It does not explain how the third party stores or retrieves those details and does not create or look up an Adyen Vault token. Adyen marks the endpoint inactive and unsupported for new integrations, directs new builds to Checkout API, and tells existing integrations to contact Adyen about migration. The dated examples do not prove credential validity, account enablement or a successful authorization.

**Raw locators:** lifecycle notice and migration routes, lines 14–21; third-party-held detail purpose, line 23; example requests, lines 33–75. **Canonical retrieval route:** [[adyen-tokenization]] → [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-authorise-using-details-stored-with-a-third-party]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party/2026-09-15|pinned raw]].

## Q2 — Initial versus subsequent request fields

**Query:** Which Card-on-File or Subscription fields does the page name for initial and subsequent payments, and what does it say about scheduled versus unscheduled use?

**Expected answer:** It names `amount`, `shopperInteraction`, and `recurringProcessingModel` for Card-on-File/Subscription requests. It says `shopperInteraction` is `Ecommerce` for the initial payment and `ContAuth` for subsequent payments. It says `recurringProcessingModel` is `Subscription` for a fixed schedule and uses the wording `Card On File` when there is no fixed schedule; the intended current schema needs verification before implementation. Both examples include raw `card` details, amount, merchant account, reference and shopper email. They show request shape only; the page gives no authorization response or webhook outcome. Raw card collection has a separate PCI scope boundary in [[adyen-tokenization]].

**Raw locators:** named fields and model values, lines 25–31; initial example, lines 33–52; subsequent example, lines 54–75. **Canonical retrieval route:** [[adyen-tokenization]] → [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-authorise-using-details-stored-with-a-third-party]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/authorise-using-details-stored-with-a-third-party/2026-09-15|pinned raw]].
