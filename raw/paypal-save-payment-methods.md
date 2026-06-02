<!-- Source URL: https://developer.paypal.com/docs/checkout/save-payment-methods/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Save payment methods
slug: /docs/checkout/save-payment-methods/
createTime: '2024-05-13T23:48:30.186Z'
updateTime: '2025-05-09T10:37:28.431Z'
---


# Save payment methods

Save payment methods so payers don't have to enter details for future transactions. Payers can check out faster or pay without being present after they agree to save a payment method.

Use the JavaScript SDK to save a payer's card if you aren't [PCI Compliant - SAQ A](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) but want to save credit or debit cards during checkout.

A payment method is saved and exchanged for a unique token through a process called tokenization. The token is stored securely and used instead of the original account number.

The benefits of using saved payment tokens include:

- Increased security by reducing opportunities for data theft.
- Simplified payment processing.
- Helps maintain Payment Card Industry Data Security Standard compliance.



## Save payment methods with or without transaction 
- **With a transaction** - The customer's payment method is saved during checkout. They can select it again at checkout for faster transactions.
- **Without a transaction** - The customer's payment method is saved without checkout. Customers don't have to be present for future transactions. A common use case is offering a free trial of a product and charging customers later.



## Payer flow 
- The payer begins the checkout experience.
- The payer chooses to save their payment method.
- You identify the payer with a unique customer ID. When the buyer returns to your website and is ready to check out, pass their customer ID to PayPal. This indicates that the payer wants to save or reuse a saved payment method.
- If the payer chooses PayPal as their payment method, the payer completes a billing agreement. There's no billing agreement required for card payments.
- When the payer returns to your website, each saved payment method displays as a one-click button on the checkout page.


![vault-flow.svg](assets/paypal-vault-flow.svg)

**Supports transactions with or without payer present**

You can save a payment method for on or off-session purchases. If the payer is present, they can select to pay with their saved payment method, or a different one. If the payer is not present, you can charge their saved payment method.


![vault-card-payment.svg](assets/paypal-vault-card-payment.svg)


## Supported payment methods 
PayPal can save the following payment methods to the vault:

- Credit and debit cards
- PayPal Wallets
- Venmo



## Eligibility 
To save credit and debit cards, ensure you are approved to process [Expanded Checkout](https://developer.paypal.com/studio/checkout/advanced) .

See supported countries:

- Australia
- Austria
- Belgium
- Bulgaria
- Canada
- China
- Cyprus
- Czech Republic
- Denmark
- Estonia
- Finland
- France
- Germany
- Hong Kong
- Hungary
- Ireland
- Italy
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malta
- Netherlands
- Norway
- Poland
- Portugal
- Romania
- Singapore
- Slovakia
- Slovenia
- Spain
- Sweden
- United Kingdom
- United States



## Options 

### Save during purchase
- Save cards, PayPal, and Venmo with the JS SDK
- Save cards and PayPal with the Orders API

 

 ![image](assets/paypal-vault-during-purchase.png) 


### Save for purchase later
- Save cards and PayPal for future transactions
- Save payment methods outside of the checkout process
- Uses the Vault Payment Methods API

 ![image](assets/paypal-vault-purchase-later.png)  



## See also 
- [Orders API](/docs/api/orders/v2/)
- [Payment Method Tokens API](/docs/api/payment-tokens/v3/)
- [Set up Expanded Checkout](https://developer.paypal.com/studio/checkout/advanced)
- [Set up PayPal Checkout](https://developer.paypal.com/studio/checkout/standard)
