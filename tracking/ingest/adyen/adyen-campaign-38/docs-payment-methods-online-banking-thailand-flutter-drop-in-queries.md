# docs-payment-methods-online-banking-thailand-flutter-drop-in — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

This is Adyen's **Online banking Thailand Flutter Drop-in** add-on, divided by Sessions and Advanced server-side flow (source-adyen-docs-payment-methods-online-banking-thailand-flutter-drop-in; raw lines 15–25, 58–62). It does not give a full base integration, currency, Flutter SDK version, issuer-ID list, current merchant eligibility or payment completion (raw lines 19–23, 50–56, 82–88). The Sessions requirements row labels a Sessions integration but its link targets `advanced-flow` (raw lines 31–35).

Q2. What is its central capability, prerequisites and warnings?

Sessions requires an existing Flutter Drop-in integration, Checkout API v68+, redirect handling and Support contact to add the method; no extra `/sessions` or method configuration parameters are specified (source-adyen-docs-payment-methods-online-banking-thailand-flutter-drop-in; raw lines 25–48). Advanced requires an existing Advanced Drop-in integration, redirect handling and Customer Area method addition, with no extra configuration or `/payments` parameters stated (raw lines 58–80). The setup directions differ between the sections, and the testing copy calls the method a “Component” despite this Drop-in title (raw lines 36, 52, 68, 84). Test status inspection and the separate live Customer Area request do not prove approval, authorization or settlement (raw lines 50–56, 82–88).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-thailand-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/online-banking-thailand/flutter-drop-in/2026-09-15]].
