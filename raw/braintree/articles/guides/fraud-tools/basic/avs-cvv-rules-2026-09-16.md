<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: AVS and CVV Rules
slug: /articles/guides/fraud-tools/basic/avs-cvv-rules/
createTime: '2025-04-02T01:48:32.330Z'
updateTime: '2025-04-02T01:48:32.459Z'
---



# AVS and CVV Rules


**AVAILABILITY**
 AVS and CVV rules only apply to credit cards.

 

We offer customizable Address Verification System (AVS) and Card Verification Value (CVV) rules as part of our Basic Fraud Tools. These rules will confirm that the address information or CVV included with a transaction matches what the issuing bank has on file for the associated card, ensuring that only authorized card users are able to make purchases from you.


## How AVS and CVV rules work

When you submit a transaction or verification request for a new credit card, we pass the address and CVV information provided to the card-issuing bank. If the bank approves, their approval response will include [AVS and CVV response codes](/braintree/docs/reference/general/processor-responses/avs-cvv-responses) ; these codes indicate whether the numeric values for the address and CVV match their records.

If the issuing bank’s response triggers one of your AVS or CVV rules, we will reject the transaction or verification and send a void request to the issuing bank. Keep in mind that [some banks don't recognize void requests immediately](/braintree/articles/control-panel/transactions/refunds-voids-credits#voids). If you do not have AVS or CVV rules enabled, we will ignore the response code.


## Enabling AVS and CVV rules

To enable AVS and CVV rules:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Fraud Management**from the drop-down menu
- Next to**AVS**or**CVV**, click the**Options**link
- Select your desired AVS or CVV rejection criteria
- Transactions will be rejected if any of the rules you enabled are violated
- For AVS rules, you have the option to reject transactions only if both the postal code and address rules are violated
- You have the option to apply the rules to all transactions or only to specific card types, amounts, or merchant accounts


- Click the**Save**button



 If you use our [Drop-in UI](/braintree/docs/guides/drop-in/setup-and-integration#fields) and you enable CVV rules or AVS rules for postal codes in the Control Panel, the fields needed to collect that information will automatically appear on your checkout form.

 


## Recommended setup options

It's best practice for most merchants to collect CVV information — this can help lower the risk of fraudulent transactions and can be used as supporting evidence in your favor if the customer issues a [dispute](/braintree/articles/risk-and-security/chargebacks-retrievals/overview). Regardless of whether you choose to verify the CVV, selecting to reject transactions if CVV is not provided will at least ensure that your customers provide this information.

Because AVS rules only check the numeric values of an address, we typically don't recommend enabling the Street Address does not match or Street address not verified rules. If your customer lives at 12345 6th Street, depending on how they enter the information, it could confuse the system and cause false rejections.


### AVS and CVV rules in the Vault

By default, AVS and CVV rules only apply to first time transactions and will not be applied to recurring payments or any transactions created using credit cards stored in the Vault. If you'd like to verify that credit cards pass your AVS and CVV rules before storing them in the Vault, you must enable [card verification](/braintree/articles/control-panel/vault/card-verification) in the Control Panel.

You can re-verify a customer’s address information for a card that is already stored in the Vault via the API. This re-verification will occur by default any time you update the vaulted payment method's information, including making it the default payment method for a customer. You can choose to skip this re-verification process if desired. [Learn more in our developer docs.](/braintree/docs/reference/request/payment-method/update#card-verification)


**NOTE**
 Due to PCI compliance restrictions, we never store your customers’ CVVs; you’ll need to collect this from them again if you would like to re-verify a card.

 


#### International AVS

By default, AVS rules will only apply to transactions and verifications that:


- Have a billing address in the United States
- Don’t specify a country of origin

If you prefer to apply AVS rules to all transactions and verifications, set the **Country Scope** to Global when editing your AVS rules.


**IMPORTANT**
Many card issuing banks outside of the US, UK, and Canada do not consistently support AVS. If you choose to enable Global AVS, you could see an increased decline rate for transactions and verifications originating in countries without AVS support. To avoid this, we recommend that you **do not select the following as reasons to reject transactions**: 
- Issuing bank does not support AVS
- Postal Code not verified
- Street Address not verified

  Additionally, you can manually skip AVS checks when processing transactions via the API from countries other than the US, UK, and Canada; [learn more in our developer docs](/braintree/docs/reference/request/transaction/sale/ruby#options-skip_avs).

 


#### International postal codes

If your customers are located in a country where postal codes include both letters and numbers, the **Postal Code** AVS rules may not be enough to protect you from fraud. This is because our rules will only check the order of numbers in the postal code, and will not check letters or the placement of numbers.

For example, take the fictional postal code of 1ABCD2. The customer could provide any postal code that included the numbers 1 and 2 – as long as all other values were letters and the 1 always came before the 2 – and AVS rules would not reject the transaction. Successful postal codes could range from 1AB2CD to 12HIJK.


## Maestro cards and CVV rules

If you have CVV rules enabled in the Control Panel, you must pass CVV information with every submitted credit card transaction or verification. Because Maestro cards do not typically include a CVV, you may find that your CVV rules reject most attempted Maestro transactions and verifications. When this happens, Maestro recommends you have your customer contact their card-issuing bank to request a CVV (referred to as a security number) for their card.


## Overriding rejections

When creating transactions via the API, you can selectively skip [AVS](/braintree/docs/reference/request/transaction/sale/ruby#options-skip_avs) and [CVV](/braintree/docs/reference/request/transaction/sale/ruby#options-skip_cvv) checks. Alternatively, you can always ask the customer to provide a different payment method.

