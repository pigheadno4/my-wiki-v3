# docs-payment-methods-rakutenpay-react-native-component — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Rakuten Pay-specific **React Native Components** guide with an explicit **Sessions unsupported** statement and an Advanced-flow section (source-adyen-docs-payment-methods-rakutenpay-react-native-component; raw lines 15–31). The Advanced “Components integration” prerequisite URL points to Drop-in, so the link does not settle the matching base procedure (raw line 39). The page gives no API/SDK minimum, live approval or final outcome evidence; DGFT simulator/status directions remain TEST scope (raw lines 37–69).

Q2. What are its central capability, prerequisites and warnings?

For the supported Advanced route, the page requires an existing Components integration, `action.type: redirect` handling and Customer Area addition; no extra Rakuten Pay configuration or ordinary `/payments` fields are specified (raw lines 31–53). Recurring card-on-file use is review-gated, prohibited without periodic cadence in the stated case, primarily associated with Food & Beverage and requires an application for **every** Recurring Processing Model; explicit shopper permission is strongly recommended (raw lines 55–61). TEST uses a named DGFT acquirer account/simulator without the Rakuten Pay app, which is not merchant approval or authorization proof (raw lines 63–69).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-react-native-component]] → [[raw/adyen/docs/payment-methods/rakutenpay/react-native-component/2026-09-15]].
