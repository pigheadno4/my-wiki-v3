# Fixed retrieval checks

1. What does A2A Issuer `POST /ideal/profile/auth-link` generate, and what is the account-holder prerequisite? Use [[source-adyen-api-explorer-a2aissuer-api-latest-post-ideal-profile-auth-link]] (https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link), raw lines 5–41 and 127–138.
2. Does a 200 response guarantee a redirect URL or completed iDEAL authentication/payment? Use [[source-adyen-api-explorer-a2aissuer-api-latest-post-ideal-profile-auth-link]] (https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/ideal/profile/auth-link), raw lines 32–41 and 100–111; distinguish optional `redirectUrl` from required nested `href`.
