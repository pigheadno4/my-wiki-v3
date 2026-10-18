# Retrieval probes — Capital financing-offer hub

Q1. What choice does this guide give between dynamic and static financing offers, and are the offer counts guaranteed?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-get-grant-offers]] → [[raw/adyen/docs/capital/get-grant-offers/2026-09-15]].

Expected answer: Dynamic offers expose amount ranges for available terms; users may receive up to three, one each for 90/180/360 days. Static offers expose fixed amount-term choices; users may receive up to nine, three per available term. Both counts and the example EUR values depend on processing history and user qualification, not a guarantee. The variable repayment terms are marked pilot. Raw locators: lines 19–37; opening comparison and Example.

Q2. Does this overview establish an actual formal offer, expiry, user consent or funded grant?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-get-grant-offers]] → [[raw/adyen/docs/capital/get-grant-offers/2026-09-15]].

Expected answer: No. It states proactive assessment and describes UI offer options, then links child dynamic/static implementation guides. The hypothetical 90/180-day EUR 25,000 example is not a user-specific offer or 360-day promise. No API role, country, calculation/formalization, expiry, selection/ToS or grant-payout rule is specified in this hub; retrieve those separately. Raw locators: lines 17–47; opening, Example, `## Next steps`.
