# Retrieval checks

Q1. What does the Alipay HK iOS Drop-in guide add to Sessions and Advanced flows?
Answer: Sessions lists existing iOS Drop-in Sessions, Checkout API v68+ and Customer Area Alipay HK, with no extra method-specific `/sessions` or configuration parameters (raw lines 25–46). Advanced separately lists existing iOS Drop-in Advanced, `action.type: redirect` handling and Customer Area setup, with no extra method-specific `/payments` or configuration parameters (raw lines 62–84). Redirect is stated explicitly only in the Advanced requirements table; v68+ only in Sessions. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipayhk-ios-drop-in]] → [[raw/adyen/docs/payment-methods/alipayhk/ios-drop-in/2026-09-15]].

Q2. How are TEST and LIVE instructions separated, and do they prove a transaction?
Answer: The page provides test fixture credentials and a test Customer Area payment-list route, while saying a request in live Customer Area is needed before accepting live Alipay HK (raw lines 48–60 and 86–98). Test credentials and request submission do not establish live approval, final authorization, capture or settlement. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipayhk-ios-drop-in]] → [[raw/adyen/docs/payment-methods/alipayhk/ios-drop-in/2026-09-15]].
