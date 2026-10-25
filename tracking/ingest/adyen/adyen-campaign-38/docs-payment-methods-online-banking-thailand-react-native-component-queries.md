# Thailand online banking React Native Component retrieval checks

## Q1 — Purpose, scope and inference limit

The canonical source [[source-adyen-docs-payment-methods-online-banking-thailand-react-native-component]] is a 2026-09-15-captured method-specific React Native Components add-on. It explicitly says Sessions flow is unsupported and documents Advanced flow instead (raw lines 15–31). It does not establish current method/issuer enablement, redirect completion, authorization or settlement; the live request is separate and tests are instructions rather than observed outcomes (raw lines 55–61).

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-thailand-react-native-component]] → [[raw/adyen/docs/payment-methods/online-banking-thailand/react-native-component/2026-09-15]].

## Q2 — Capability, prerequisites and warnings

The Advanced path requires existing React Native Components, redirect handling with `action.type: redirect`, and Customer Area addition (raw lines 35–41). It states no additional method-specific configuration or `/payments` parameters, which does not erase base-flow request fields (raw lines 43–53). Its Components integration-type row links to `integration=Drop-in`, while nearby redirect/payment URLs use Components (raw lines 39–40, 53). It offers available issuer IDs for testing, test Customer Area payment-list inspection, and a separate live Customer Area request before live acceptance (raw lines 55–61). The page gives no API/SDK minimum or issuer-ID list.

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-thailand-react-native-component]] → [[raw/adyen/docs/payment-methods/online-banking-thailand/react-native-component/2026-09-15]].
