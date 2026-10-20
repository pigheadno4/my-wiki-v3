# C23 worker retrieval checks — docs-issuing-card-on-file-tokens

## Q1: What is the card-on-file network-token flow and what setup does the page require?

It is a **merchant** card-on-file route: the cardholder saves an issued card with a merchant, the merchant requests a network token via the card scheme, and the scheme forwards the request to Adyen (raw lines 19–21, 33–45). The guide requires an Issuing-supporting integration, Network token webhook subscription, and Adyen-contact check for a card manufacturing profile (lines 23–31). Adyen creates the token **inactive**, checks the merchant against the scheme allowlist, then activates an approved token or closes it when the merchant is not allowlisted; created and outcome webhooks are separate (lines 64–117). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-card-on-file-tokens]] → [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15]].

## Q2: Does a created or valid token prove activation or a successful payment?

No. Creation starts **inactive**; the merchant-allowlist decision and later outcome determine activation or closure (raw lines 74–85, 89–117). This page's simplified payment sketch says the scheme approves when a token is valid (line 57), but the separate [[source-adyen-docs-issuing-authorisation|Issuing authorisation guide]] describes additional card, balance, rule and optional relayed checks ([[raw/adyen/docs/issuing/authorisation/2026-09-15|related raw lines 19–41, 63–77]]). Neither token creation nor token validity alone proves payment approval or capture. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-card-on-file-tokens]] → [[raw/adyen/docs/issuing/card-on-file-tokens/2026-09-15]].
