# docs-issuing-network-tokens retrieval checks

Q1. What is the main purpose of Issuing network tokens and what must be in place first?

Answer: For Adyen-issued cards, they stand in for sensitive card details for digital-wallet use or merchant card-on-file single/recurring payments (raw lines 19, 30-38, 46-49). The captured guide requires an Issuing-supporting integration and says to contact Adyen to confirm a card manufacturing profile (raw lines 21-28). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-network-tokens]] → [[raw/adyen/docs/issuing/network-tokens/2026-09-15]].

Q2. When can the token be used, and which lifecycle limit prevents reactivation?

Answer: A new token is inactive and unusable until provisioning/risk review leads to approval and active status; a declined creation closes it (raw lines 53-66, 78-80, 84-87). Suspension temporarily blocks payment use and may be reversed to active, while closed is permanently deactivated and cannot be updated (raw lines 68, 82-87). The overview does not prove that a specific token, authorization or payment succeeded. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-network-tokens]] → [[raw/adyen/docs/issuing/network-tokens/2026-09-15]].
