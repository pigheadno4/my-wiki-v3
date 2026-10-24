# docs-payment-methods-paynow-react-native-drop-in — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a PayNow-specific **React Native Drop-in** add-on for already-existing Sessions or Advanced integrations (source-adyen-docs-payment-methods-paynow-react-native-drop-in; raw lines 15–25, 59–69). It does not contain a full base implementation, QR expiry or final payment-response/webhook sequence and cannot establish live merchant eligibility, authorization or settlement (raw lines 19–23, 37–91). The Sessions prerequisite URL points to Advanced flow, and the Advanced QR action links to a redirect-named anchor; those labels cannot change the stated flow/action type (raw lines 33, 68).

Q2. What are its central capability, prerequisites and warnings?

Sessions calls for Checkout API v68+, PayNow in Customer Area, and an existing React Native Drop-in flow, with no extra PayNow `/sessions` or configuration additions (raw lines 29–47). Advanced separately requires additional handling for `action.type: qrCode` and gives no extra PayNow configuration or ordinary `/payments` fields (raw lines 63–81). Both flow sections require Support addition in live Customer Area before live acceptance, describe live penny testing with a real banking app, and warn that test Customer Area bank transfers **cannot be reversed** and deduct bank funds (raw lines 49–57, 83–91). The source describes these as payment-testing guidance and risk, not proof or an instruction to carry out a financial operation.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-react-native-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/react-native-drop-in/2026-09-15]].
