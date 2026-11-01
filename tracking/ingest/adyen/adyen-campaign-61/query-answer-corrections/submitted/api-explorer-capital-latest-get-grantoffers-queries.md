# Fixed retrieval checks

1. What does Capital API v1 `GET /grantOffers` return for `accountHolderId`, and does it include static offers derived from dynamic selections? Use [[source-adyen-api-explorer-capital-latest-get-grantoffers]] (https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers), raw lines 5–7, 17–47.
2. Which offer response objects are optional, and are their nested `currency`, `value`, fee `amount`, and repayment `basisPoints` required only when their parents occur? Use [[source-adyen-api-explorer-capital-latest-get-grantoffers]] (https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers), raw lines 29–47; distinguish listing an offer from a funded grant.
