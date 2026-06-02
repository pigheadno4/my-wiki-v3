---
title: Manage online risk with FraudNet
slug: /limited-release/fraudnet/
createTime: "2024-08-15T05:57:40.168Z"
updateTime: "2024-08-15T05:57:40.424Z"
---

# Manage online risk with FraudNet

FraudNet is a JavaScript library developed by PayPal and embedded into a merchant’s web page to collect browser-based data to help reduce fraud. Upon checkout, these data elements are sent directly to PayPal Risk Services for fraud and risk assessment.

To integrate FraudNet, embed a short code snippet in the merchant website and add a custom header to the PayPal call. See [Integrating FraudNet](/limited-release/fraudnet/integrate/) .

## Data collection, usage and privacy

Data collected by FraudNet is used for risk analysis and authentication. PayPal does not share FraudNet data with third parties for their own independent benefit.

For details of what information FraudNet collects, refer to the [payload descriptions](/limited-release/fraudnet/reference/) .

Please note that FraudNet is for browser-based integrations only. For risk analysis data gathered on mobile devices, please refer to [Magnes documentation](/limited-release/magnes/) .
