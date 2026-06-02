<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-with-venmo/test/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Test Venmo in sandbox
slug: /docs/checkout/pay-with-venmo/test/
createTime: '2025-02-20T09:56:55.040Z'
updateTime: '2025-12-16T15:38:56.942Z'
---


# Test Venmo in sandbox

Test the Pay with Venmo feature in the sandbox environment before going live.

 



## Getting started
- Start by following the instructions in the [PayPal sandbox testing guide](https://developer.paypal.com/tools/sandbox/) .
- During the test phase, use the PayPal sandbox endpoints and your PayPal sandbox account details in each PayPal API request that you make.
- Simulate the Venmo button in the PayPal sandbox, and add the buyer-country=US parameter to your JS SDK code.

Venmo is only available in the US.



## Use cases 
You can test the Venmo experience on a desktop or mobile web browser. You can expect the following experience in the sandbox:

- If you are testing on a desktop, you will experience the Venmo web login flow.
- If you are testing on the mobile web with the Venmo app installed, you will experience the Venmo app-switch flow.
- If you are testing on the mobile web without the Venmo app installed, you will experience the Venmo web login flow.



In the production environment, consumers will experience QR code-based checkout on their desktop browser. Sandbox testing of the desktop QR code is currently unavailable.



## Desktop web experience
 ![Desktop,web,experience](assets/paypal-venmo-sandbox-desktop-web.gif) 

## Mobile web experience with Venmo app installed




![Mobile,web,experience,with,Venmo,app,installed](assets/paypal-venmo-mobile-flow.png) 





## Mobile web experience with Venmo app not installed




![Mobile,web,experience,with,Venmo,app,not,installed](assets/paypal-venmo-sandbox-mobile-no-app.png) 







## Venmo features supported in sandbox 
The following Venmo features are supported for testing in the sandbox environment:

- App-switch checkout flow
- Web login based checkout flow suitable for non-US developer testing
- One-time checkout
- Vault setup
- RISK | INSUFICIENT_FUNDS
- RISK | ACCOUNT_CLOSED
- RISK | ACCOUNT_FROZEN
- RISK | SUSPECTED_FRAUD
- RISK | GENERIC_DECLINE

 

### Test error scenarios
You can test certain error scenarios in the sandbox using the specific amounts in thefollowing table. If any other amount value is used, responses will result in a SUCCESS .

 

| **Amount** | **Error scenario** |
| 12.34 | INSUFFICIENT_FUNDS |
| 21.43 | ACCOUNT_CLOSED |
| 11.45 | ACCOUNT_FROZEN |
| 10.23 | SUSPECTED_FRAUD |
| 13.42 | GENERIC_DECLINE |
| Other | SUCCESS |



## Venmo features not supported in sandbox 
The following Venmo features are not supported for testing in the sandbox environment:

- Vaultsubsequent purchases
- Self-service test account creation
- Post-purchase Venmo experience withfeed and ledger
- Settlement and disbursement
- Disputes
- Merchant reporting
