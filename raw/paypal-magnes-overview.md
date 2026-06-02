---
title: Manage mobile risk with Magnes
slug: /limited-release/magnes/
createTime: "2024-08-15T07:18:03.979Z"
updateTime: "2024-09-23T22:03:20.759Z"
---

# Manage mobile risk with Magnes

The rapid growth of mobile commerce has expanded the payment ecosystem. When integrated as a preferred payment method in a mobile application, PayPal helps eliminate fraud and manage risk.

PayPal Magnes accesses iOS and Android data for PayPal Risk Services to perform early risk identification and mitigation.

This section compares the basic PayPal payment model and the Magnes implementation model.

For non-mobile risk solutions, please see [Fraudnet](/limited-release/fraudnet) .

## PayPal payment model

For standard mobile payment processing, the merchant application interacts directly with the merchant's server. In this case, PayPal is unable to access necessary device fingerprinting information critical for risk management.

![PayPal,payment,model](assets/paypal-magnes-payment-model.svg)

### PayPal payment flow

- During a PayPal transaction, the mobile app sends the transaction to the merchant server.
- The merchant server sends the transaction data in the call to the PayPal API.

Contact your PayPal representative for information about using the PayPal API.

## Magnes implementation model

Magnes is integrated within the client app. It collects device-related information required for risk management. Magnes sends the information to PayPal Risk Services, which performs risk adjudication, thus providing a better customer experience.

![Magnes,implementation,model](assets/paypal-magnes-risk-flow.svg)

### Magnes payment flow

- Add required Android permissions or iOS frameworks.
- The mobile app sets up Magnes.
- Magnes generates a PayPal-Client-Metadata-Id , or accepts one passed in, and sends it to the app.
- Magnes collects and submits a payload of key device information along with the PayPal client metadata ID to PayPal Risk Services.
- During PayPal transactions, the mobile app sends the transaction, along with the PayPal client metadata ID, to the merchant server.
- The merchant server includes the PayPal-Client-Metadata-Id in the call to the [PayPal Mobile API](/docs/api/rest-sdks) .
- PayPal Risk Services utilizes the payload data to perform risk management for the transaction and reduce friction.

Magnes does not make payment or risk decisions, it only provides data to PayPal Risk Services to facilitate risk management.

**Note:** Some code samples reference "Dyson," an the earlier code name for the Magnes library. Magnes and Dyson are interchangeable.

## Data collection, usage, and privacy

Magnes collects mobile device data based on the permissions granted during the installation of the mobile app.

Data collected by Magnes is used for risk analysis and authentication. PayPal does not share Magnes data with third parties for their own benefit.

For a complete list of what data Magnes collects, see [Magnes payload parameters](/limited-release/magnes/reference/payload-parameters) .
