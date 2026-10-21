# docs-marketplaces-verification-overview — attempt 1 retrieval checks

## Q1. When does Adyen verify Marketplace users, and how are capabilities allowed?

Default capabilities are requested when a new account holder is created; nondefault ones need a request and can need more verification (raw lines 36–40). Data changes trigger reverification (raw lines 44–52), higher tiers trigger checks with payout-capability restriction (raw lines 56–60), and periodic/proactive data reviews check the entity and its associates (raw lines 64–72). Verification is asynchronous and updates come through webhooks; check the user’s capability settings for allowed use, rather than infer approval from a request (raw lines 19–23, 173–180). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview]] → [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15]].

## Q2. Does a deadline preserve all capabilities or make a higher-tier payout available?

No. An active deadline may preserve **previously allowed** capabilities while data is corrected, and v3/v4 deadlines have standard 30/60-day groups but can be shortened or removed (raw lines 74–106). On a higher tier, payout-related capabilities are disallowed, while an accepting-payment deadline is phrased as a **possible future** feature (raw lines 56–60, 198–212). A data review finalizes only after confirmation **and** all errors resolved (raw lines 68–72). Account-holder update webhooks are for capability-related changes, not legal-entity data changes alone (raw line 52). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-verification-overview]] → [[raw/adyen/docs/marketplaces/verification-overview/2026-09-15]].
