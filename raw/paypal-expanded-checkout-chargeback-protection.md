<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Chargeback Protection
slug: /docs/checkout/advanced/customize/chargeback-protection/
createTime: '2025-05-21T12:21:53.794Z'
updateTime: '2025-10-28T09:29:52.939Z'
---


# Chargeback Protection

The Chargeback Protection Tool* reduces the risk of fraudulent credit or debit card transactions by approving or declining transactions using fraud analysis. If you can prove that the product was delivered and supply evidence of delivery, PayPal waives the chargeback fees** and resolves the dispute up to the amount of your loss cap.

Without the Chargeback Protection Tool, you are responsible for making transaction risk decisions and are liable for any associated chargebacks when processing debit and credit card payments with PayPal.



## Eligibility 
- Have a PayPal business account.
- You'll need to have an existing [Expanded Checkout](https://developer.paypal.com/studio/checkout/advanced) integration.
- The Chargeback Protection Tool is available in the US, CA, AU, MX, FR, IT, ES, UK, and DE. See [PayPal Merchant Fees](https://www.paypal.com/us/business/paypal-business-fees) for more information.



## Choose your protection tool 
The Fraud Protection Tool and the Chargeback Protection Tool help detect and manage fraud with PayPal's machine learning algorithm. The Chargeback Protection Tool helps businesses manage the costs of chargebacks, while the Fraud Protection Advanced Tool helps businesses manage fraud risks. See the following table to see which protection toolfits specific business needs.

| Feature | Fraud Protection Advanced Tool | Chargeback Protection Tool |
| Get help detecting fraud with PayPal's machine learning algorithm | X | X |
| Set and test premade fraud filters | X | - |
| Create custom fraud filters | X | - |
| Manage block and allow lists | X | - |
| Review and investigate transactions | X | - |
| Eligible chargeback fees waived | - | X |
| Holds removed on disputed amount for eligible chargebacks | - | X |
| No evidence required for unauthorized chargebacks | - | - |
| Tool pricing | See[PayPal Merchant Fees](https://www.paypal.com/us/business/paypal-business-fees)for your region | See[PayPal Merchant Fees](https://www.paypal.com/us/business/paypal-business-fees)for your region |



## Activate chargeback protection  


**Note:** When you use Fraud Protection tools, you must deactivate the Chargeback Protection Tool.



You can activate the Chargeback Protection Tool using either of the following options:

- Option 1: In **Business Tools** , navigate to the **Manage Risk** section. Select the **Fraud Tools** tile.
![FPA discovery via Business Tools](assets/FPA_Home_Discovery_BusinessTools.png)

- Option 2: Go to your **Account Settings** , and select **Payment preferences** . Next to the **Manage fraud** section, select **Choose a fraud tool.**
![Activate via Account Settings](assets/Activate_dirmerch_acct_settingSS.png)

- Select **Chargeback Protection Tool** and select **Activate** .
![CBP Activate screen](assets/CBP_Activate.png)


## Integration
Ensure that you pass all mandatory fields. Your business's risk profile determines whether you need to pass additional data when signing up for the Chargeback Protection Tool. See the [Chargeback Protection Tool integration guide](https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/integrate/) for more information.



## Fraud evaluation and chargebacks 
PayPal's Chargeback Protection Tool employs a real-time risk evaluation process to assess each credit and debit transaction. This automated system quickly identifies and flags high-risk transactions, preventing them from being processed. When a transaction is deemed low-risk, PayPal processes the payment. When a transaction is considered high-risk, PayPal declines to process the payment. All risk decisions happen in real time, so there is no manual review process and no option to review declined transactions later.

In the event of an eligible chargeback, PayPal requests proof of delivery or shipment. The specific evidence requirements vary depending on the goods or services sold. For more information, see the [PayPal User Agreement](https://www.paypal.com/us/legalhub/useragreement-full?locale.x=en_US#spp-proof-delivery) .

 

### Transaction statuses
When PayPal declines a transaction with the Chargeback Protection Tool enabled, there is no option to override or bypass this decision. The [Transaction Details](https://www.paypal.com/unifiedtransactions/details/payment/) page displays all transactions. The Chargeback Protection Tool evaluates transactions and marks them with **Chargeback Protection** , ensuring that it is eligible for Chargeback Protection Tool services.

 

### Manage chargebacks
PayPal notifies you when a chargeback case is open and gives you the option to submit evidence for that case. Refer to the [integration guide](https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/integrate/) to pass evidence using the [Disputes API](https://developer.paypal.com/docs/api/customer-disputes/v1/) . Alternatively, you can pass the evidence using the [Resolution Center](https://www.paypal.com/disputes/insights) . See the proof of delivery and proof of shipment requirements  in the [PayPal User Agreement](https://www.paypal.com/us/legalhub/useragreement-full?locale.x=en_US#spp-proof-delivery) .

 

* Terms apply to the Chargeback Protection Tool. The use of the Chargeback Protection Tool is subject to a monthly loss cap rate. Certain transactions and chargebacks are not eligible for the Chargeback Protection Tool. See [PayPal Online Payment Services Agreement](https://www.paypal.com/us/legalhub/paypal/pocpsa-full#chargeback) for details.

** Acquiring banks and card networks may charge you additional chargeback fees. These fees won't be waived and will be passed through to you at cost.
