<!-- Source URL: https://docs.stripe.com/disputes/reason-codes-defense-requirements -->
<!-- Fetched: 2026-05-09 -->

# Dispute reason codes

Use this disputes center to learn about the reason codes of three major networks.

You can manage disputes using the [Dashboard](https://docs.stripe.com/disputes/responding.md) or the [API](https://docs.stripe.com/disputes/api.md).

Each card network defines hundreds of codes representing very specific reasons for dispute claims, many of which overlap across all networks. Stripe maps each network code into one of seven categories based on the general claim. This guide covers the most common dispute reasons for Visa, Mastercard, and American Express. We’ve organized these into seven categories and provide examples of evidence you can use to challenge each type of dispute.

The cardholder’s bank, not Stripe, decides the outcome of each dispute. For general guidance on what you need for each category, see [Category defense guidelines](https://docs.stripe.com/disputes/categories.md#dispute-category-types). For more comprehensive network guidance, reference the official network’s documentation.

> The following tables include possible evidence to submit when countering a claim, but each dispute is different. We encourage you to review each situation individually to determine how to respond.

#### Visa

## Credit not processed

The _Credit Not Processed_ dispute category typically occurs when a cardholder claims they were entitled to a refund or credit, but it was never processed or received. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#credit-not-processed).

| Reason code | Reason                   | Description                                                                                                                                                                                                                                                                                                                     | Evidence examples                                                                                      |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 13.6        | **Credit Not Processed** | A cardholder claims they were due a refund or credit, but it wasn’t issued or processed correctly. This typically happens when a business agrees to a refund but doesn’t complete it, or when a return or cancellation is processed, but the credit doesn’t appear on the cardholder’s statement within a reasonable timeframe. | - **Proof of refund issuance:** Provide refund transaction logs, timestamps, and confirmation numbers. |

- **Bank or processor statements:** Show when the refund was issued and that it matches with the disputed charge.
- **Customer communications:** If the refund was promised or denied, include relevant messages or policy explanations.
- **Return and refund policies:** Show the clear terms agreed to at purchase and how the customer did (or didn’t) meet them.
- **Delivery confirmation:** If the dispute involves returned goods, provide tracking details showing whether the return was received and processed. |
  | 13.7 | **Canceled Merchandise or Services** | A cardholder claims they canceled a purchase (either for goods or services) but were still charged. This can happen when a subscription isn’t correctly canceled, a refund isn’t processed after a cancellation, or a customer misunderstands cancellation terms. | - **Cancellation policy:** Provide a copy of your refund or cancellation terms and proof that the customer agreed to them at checkout or signup.
- **Cancellation request logs:** If the customer didn’t submit a cancellation request, show that no record exists.
- **Usage logs (for services or subscriptions):** If the customer continued to use the service after cancellation, provide access logs or usage timestamps.
- **Refund processing confirmation:** If a refund was issued, provide transaction logs showing the refund amount and processing date.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the customer was informed about non-refundable terms or given an alternative resolution, include this. |

## Duplicate

The _Duplicate_ dispute category refers to situations where a cardholder claims they were charged multiple times for a single transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#duplicate).

| Reason code | Reason               | Description                                                                                                                                                                       | Evidence examples |
| ----------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 12.6.1      | Duplicate Processing | The cardholder claims that a single transaction was processed more than once using the same payment credential on the same transaction date, and for the same transaction amount. | - System log      |

- Transaction confirmation
- Customer communications
- Terms from site
- CVV and AVS checks |
  | 12.6.2 | Paid by Other Means | A cardholder claims they were charged for a transaction they had already paid for using a different payment method. For example: cash, check, another credit or debit card, store credit, or a third-party payment service like PayPal. | - **Payment logs:** Show that no alternative payment was received or that the charge was valid.
- **Refund records (if applicable):** If a duplicate charge occurred and was already refunded, provide proof.
- **Pre-authorization details:** If the charge was a temporary hold that later cleared, include transaction timestamps.
- **Transaction receipts:** Provide itemized receipts showing the final payment method used.
- **Split payment documentation:** If the customer used multiple payment methods, show records of each payment.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the cardholder inquired about the charge before disputing, include support responses clarifying the transaction.
- **Compare timestamps of alleged duplicate transactions:** If one was a hold and the other was a final charge, this can explain the confusion.
- **Show transaction matching records:** If the customer claimed they paid by cash but the system only recorded a card payment, include this. |

## Fraudulent

The _Fraudulent_ dispute category refers to situations where a cardholder claims they didn’t authorize or participate in a transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#fraudulent).

| Reason code | Reason                               | Description                                                                                                                                                                                                                                                                                                    | Evidence examples                                                                                                                          |
| ----------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 10.3        | Other Fraud—Card-Present Environment | The cardholder claims they didn’t authorize a transaction that took place in a _card-present environment_ (an in-person transaction where the card was physically used). This typically means the customer is alleging fraud, often due to stolen or counterfeit cards, unauthorized use, or skimming attacks. | - **EMV transaction data:** If the transaction was completed using a chip and PIN, provide details showing the cardholder’s participation. |

- **Signed receipt:** If a signature was captured, provide it so that it can be compared to the cardholder’s signature on file.
- **Surveillance footage:** If available, include timestamps or images showing the cardholder at the point of sale.
- **Merchant logs and POS data:** Provide details of the transaction, including card type, method of entry, and authorization response.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the customer contacted you about the transaction before disputing, include any relevant interactions. |
  | 10.4 | Other Fraud—Card Absent Environment | The cardholder claims they didn’t authorize a transaction that took place in a _card-not-present (CNP) environment_, such as online, over the phone, or through a mobile app. These disputes typically occur due to stolen card information, account takeovers, or unauthorized recurring charges. | - **AVS and CVV matching:** If the billing address and CVV matched, show these results to support the legitimacy of the transaction.
- **Device and IP address data:** Show that the transaction was completed using a known device or from a location consistent with previous customer activity.
- **Order and transaction history:** If the cardholder has successfully completed past purchases, include the pattern of legitimate transactions.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the cardholder contacted support about the purchase before disputing, provide chat or email logs.
- **Terms and conditions agreement:** For subscriptions or digital goods, show proof that the customer agreed to the purchase terms. |

## General

The _General_ dispute category typically serves as a catch-all for disputes that don’t fit neatly into other more specific categories. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#general).

| Reason code | Reason                     | Description                                                                                                                                                                                                 | Evidence examples                                                                                                                                             |
| ----------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12.2        | Incorrect Transaction Code | You processed a debit when you were supposed to process a credit (vice versa), or a credit was processed when you were supposed to process a reversal to correct a transaction that was processed in error. | - **Transaction logs:** Provide detailed transaction logs showing the original intent of the transaction (debit or credit) and how it was actually processed. |

- **Merchant records:** Show internal records or communications that indicate the intended transaction type.
- **Correction attempt evidence:** If you’ve already tried to correct the error, provide documentation of the reversal or correction attempt.
- **System error reports:** If the incorrect processing was due to a system error, include any relevant error logs or reports.
- **Customer communications:** Provide any correspondence with the customer acknowledging the error and steps taken to resolve it. |
  | 12.5 | Incorrect Amount | A cardholder contends that the transaction amount on their statement is incorrect. This can occur when the charge appears higher (or lower) than what was agreed upon or expected, due to pricing errors, tax miscalculations, currency conversion issues, or other processing mistakes. | - **Order confirmations and receipts:** Provide itemized receipts that detail the base price, taxes, fees, and any discounts applied.
- **Point-of-sale (POS) data:** Present logs and system records showing the pricing presented to the customer during the transaction.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. Include any pre-purchase communications (emails, website screenshots, or chat logs) that outline the correct amount.
- **System logs:** If applicable, show that your payment processing system recorded and transmitted the correct amount. |

## Product not received

The _Product Not Received_ dispute category refers to situations where a cardholder claims they didn’t receive the purchased goods or services. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-not-received).

| Reason code | Reason                               | Description                                                                                                                                              | Evidence examples                                                                                                  |
| ----------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 13.1        | Merchandise or Services Not Received | The cardholder claims that merchandise or services that they ordered weren’t received by the expected date (or merchandise was unavailable for pick-up). | - **Proof of shipment and delivery:** Provide tracking details, carrier confirmation, or signed delivery receipts. |

- **Proof of digital access:** For digital goods, include login records, download logs, or timestamps of product usage.
- **Proof of service completion:** Provide appointment records, work logs, or check-in confirmations.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. Include any customer interactions confirming receipt, troubleshooting requests, or delivery inquiries.
- **Terms and policies:** Show refund, fulfillment, and delivery policies, including agreement at checkout. |

## Product unacceptable

The _Product Unacceptable_ dispute category refers to situations where a cardholder claims the received product or service doesn’t match what was described or expected. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-unacceptable).

| Reason code | Reason                                                | Description                                                                                                                                                                                                                             | Evidence examples                                                                                                                                  |
| ----------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 13.3        | Not as Described or Defective Merchandise or Services | A cardholder claims that the goods or services they received were materially different from what was advertised, were damaged or defective, or otherwise didn’t meet their reasonable expectations based on the merchant’s description. | - **Marketing materials and listings:** Provide screenshots or archived versions of how you presented the item or service at the time of purchase. |

- **Order and fulfillment records:** Show timestamps for purchase, delivery, and any acceptance confirmations.
- **Usage logs (if applicable):** For digital products, provide logs showing customer login, downloads, or usage post-purchase.
- **Customer communications:** If the customer reached out about dissatisfaction, show responses offering troubleshooting or solutions.
- **Return policies and terms:** Display return or refund terms and the customer’s agreement to them
- **Technical support logs (if relevant):** If the item or service was allegedly defective, provide evidence of troubleshooting attempts or the customer’s lack of engagement in resolution steps. |
  | 13.4 | Counterfeit Merchandise | A cardholder claims that the merchandise or services delivered were misrepresented. Meaning, the product or service didn’t match the description, features, or quality that was promised by the merchant. This covers cases where the advertised attributes differ significantly from the actual offering. | - **Marketing materials and listings:** Provide screenshots or archived versions showing the authentic product details as advertised.
- **Supplier and certification records:** Include invoices, certificates of authenticity, or official distributor agreements.
- **Order and fulfillment records:** Show timestamps for purchase, shipping, and delivery confirmations.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the customer raised concerns before disputing, provide responses that clarified authenticity.
- **Return policies and terms:** Display terms that were agreed upon regarding product authenticity and returns. |
  | 13.5 | Misrepresentation | A cardholder claims that the merchandise or services delivered were misrepresented. Meaning, the product or service didn’t match the description, features, or quality that was promised by the merchant. This covers cases where the advertised attributes differ significantly from the actual offering. | - **Marketing materials and listings:** Provide screenshots or archived versions of how you presented the item or service at the time of purchase.
- **Order and fulfillment records:** Show timestamps for purchase, delivery, and any acceptance confirmations.
- **Usage logs (if applicable):** For digital products, provide logs showing customer login, downloads, or usage after purchase.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. Include any interactions where customers raised concerns and you offered troubleshooting or clarifications.
- **Return policies and terms:** Display return or refund terms and show that the customer agreed to them.
- **Technical support logs (if relevant):** If the item or service was alleged to be defective, provide evidence of troubleshooting attempts or the customer’s lack of engagement in resolution step. |

## Subscription canceled

The _Subscription Canceled_ dispute category refers to situations where a cardholder claims they were charged for a recurring service or subscription after cancellation. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#subscription-canceled).

| Reason code | Reason             | Description                                                                                                                                                                                                                                                                                                            | Evidence examples                                                                                                               |
| ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 13.2        | Canceled Recurring | A cardholder claims they were charged for a recurring transaction after canceling their subscription or payment agreement. This often happens when the cancellation request wasn’t processed correctly, the customer misunderstood the cancellation policy, or the charge was part of a billing cycle they overlooked. | - **Cancellation policy:** Show proof that the customer agreed to the subscription terms, including any cancellation deadlines. |

- **Cancellation request records:** If the customer never submitted a cancellation request or canceled after the charge was processed, provide system logs showing the exact date and time.
- **Usage logs (for digital services):** If the customer accessed the service post-cancellation, include timestamps and IP logs.
- **Shipping and fulfillment records (for physical goods):** If a recurring order was already shipped before cancellation, provide tracking information.
- **Customer communications:** The customer is obligated to proactively communicate the issue before filing a dispute. If the customer was informed of their billing cycle or non-refundable terms, include chat logs or email confirmations.
- **Refund records (if applicable):** If a refund was issued before the dispute, show proof of the transaction. |

#### Mastercard

## Credit not processed

The _Credit Not Processed_ dispute category typically occurs when a cardholder claims they were entitled to a refund or credit, but it was never processed or received. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#credit-not-processed).

| Reason code | Reason               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Evidence examples                                                                              |
| ----------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 4860        | Credit Not Processed | The cardholder claims they were entitled to a refund or credit, but it was never processed. This can apply to returns where the merchant agreed to issue a refund but didn’t process it; canceled services or orders where the cardholder expected a credit; duplicate charges where one charge was supposed to be refunded but wasn’t; and timeshares or travel bookings where a cancellation policy applied, but the refund wasn’t issued. | - **Proof of refund issuance:** Provide a transaction record showing the credit was processed. |

- **Refund policy:** Show that the cardholder agreed to terms stating when a refund would or wouldn’t be provided.
- **Return or cancellation policy:** Provide evidence that the cardholder didn’t comply with return or cancellation requirements.
- **Customer communications:** If you informed the cardholder about refund timelines or non-refundable terms, include these interactions.
- **Transaction logs:** Show that the charge was valid and no duplicate credit was required. |

## Duplicate

The _Duplicate_ dispute category refers to situations where a cardholder claims they were charged multiple times for a single transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#duplicate).

| Reason code | Reason                                | Description                                                                                                                                                                                                                                                                                                                                                                                                      | Evidence examples                                                             |
| ----------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 4834        | Duplicate Processing of a Transaction | The cardholder claims they were charged more than once for the same transaction. This typically happens due to a merchant processing error, where the transaction was unintentionally submitted multiple times; a customer misunderstanding, where they mistake a pending authorization for a duplicate charge; or a technical issue, such as a system glitch that caused the same charge to be processed twice. | - **Transaction logs:** Show that only one charge was successfully processed. |

- **Payment processing records:** If a duplicate did occur but was voided, reversed, or refunded, provide documentation.
- **Receipts and invoices:** Show that the charges correspond to different transactions, dates, or services.
- **Recurring or installment payment agreements:** If the charge is part of a subscription or payment plan, provide the agreement.
- **Pre-authorization and settlement proof:** Demonstrate that one charge was an authorization hold that later cleared, not an actual duplicate transaction.
- **Customer communications:** If the cardholder reached out before filing a chargeback, include any relevant interactions confirming their misunderstanding. |

## Fraudulent

The _Fraudulent_ dispute category refers to situations where a cardholder claims they didn’t authorize or participate in a transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#fraudulent).

| Reason code | Reason                      | Description                                                                                                                                                                                                                                                                                                                                                     | Evidence examples                |
| ----------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 4837        | No Cardholder Authorization | The cardholder claims they didn’t authorize a transaction. This applies to transactions that the issuer has identified as fraudulent, typically due to lost, stolen, or counterfeit cards. These chargebacks often arise from card-not-present (CNP) transactions, but they can also occur in card-present scenarios where the cardholder denies participation. | - For card-present transactions: |

    - **EMV transaction data:** If the transaction was completed with a chip or PIN, provide details showing cardholder participation.
    - **Signed receipt:** If a signature was captured, provide it for comparison with the cardholder’s signature on file.
    - **Surveillance footage:** If available, include timestamps or images showing the cardholder at the point of sale.
    - **Merchant logs and POS data:** Provide details of the transaction, including card type, method of entry, and authorization response.

- For card-not-present transactions:
  - **3D Secure authentication:** If the transaction was authenticated using 3D Secure, provide proof.
  - **AVS and CVV match:** Show that the cardholder provided correct billing details and security codes.
  - **IP address and device data:** Demonstrate that the transaction originated from a familiar device or location associated with the cardholder.
  - **Customer communications:** Include any emails, chats, or support inquiries where the cardholder acknowledges the purchase. |

## General

The _General_ dispute category typically serves as a catch-all for disputes that don’t fit neatly into other more specific categories. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#general).

| Reason code | Reason                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                             | Evidence examples                                                                                                         |
| ----------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 4831        | Transaction Amount Differs | The cardholder claims that the amount they were charged differs from what they agreed to pay. This can happen due to pricing errors at checkout, incorrect tip adjustments (for example, in restaurants and salons), exchange rate discrepancies on international transactions, and additional fees the cardholder didn’t expect or authorize. It can also occur due to a processing error where the wrong amount was entered manually. | - **Proof of transaction authorization:** Provide receipts, invoices, or digital confirmations showing the agreed amount. |

- **Signed receipts or digital acknowledgment:** If the cardholder signed or confirmed the amount, this serves as strong evidence.
- **Breakdown of charges:** Itemized receipts that show the base price, taxes, fees, tips, or currency conversion details.
- **Merchant policies:** Show refund, tipping, or pricing policies that you disclosed before the transaction.
- **Exchange rate proof:** For international transactions, provide documentation of the exchange rate at the time of processing.
- **Customer communications:** If the cardholder reached out with concerns about the charge before disputing, include those interactions. |
  | 4846 | Currency Errors | A cardholder claims that they were charged an incorrect amount due to currency conversion errors. These disputes typically arise from discrepancies between the advertised price and the final charged amount when foreign currencies are involved. This reason is most frequently encountered in Europe, where multi-currency transactions are common and conversion rate fluctuations or additional fees (such as bank surcharges) can lead to unexpected differences in the charged amount. | - **Exchange rate documentation:** Provide time-stamped records showing the exchange rate used at the time of the transaction, along with reference data from reputable financial sources.
- **Pricing and communication records:** Include screenshots or copies of your website or point-of-sale system displaying pricing information, conversion policies, and any disclaimers about potential fees or fluctuations.
- **Transaction records:** Offer detailed order confirmations, receipts, and processor logs that show the currency conversion steps and the final charged amount.
- **Customer communications:** Present any emails or chat transcripts where you informed customers about currency conversion details and potential fees. |

## Product not received

The _Product Not Received_ dispute category refers to situations where a cardholder claims they didn’t receive the purchased goods or services. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-not-received).

| Reason code | Reason                         | Description                                                                                                                                                                                                                                                                                                                                             | Evidence examples                                                                                                  |
| ----------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 4855        | Goods or Services Not Provided | The cardholder claims that they didn’t receive the goods or services they paid for. This can apply to physical goods that were never delivered or services that weren’t rendered as expected. It can also apply to digital goods that were inaccessible, or travel-related transactions where a flight, hotel, or rental was canceled but not refunded. | - **Proof of shipment and delivery:** Provide tracking details, carrier confirmation, or signed delivery receipts. |

- **Proof of digital access:** For digital goods, include login records, download logs, or timestamps of product usage.
- **Proof of service completion:** Provide appointment records, work logs, check-in confirmations, or service contracts.
- **Customer communications:** Include any interactions confirming receipt, troubleshooting requests, or delivery inquiries.
- **Terms and policies:** Show refund, fulfillment, and delivery policies, including agreement at checkout. |

## Product unacceptable

The _Product Unacceptable_ dispute category refers to situations where a cardholder claims the received product or service doesn’t match what was described or expected. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-unacceptable).

| Reason code | Reason                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Evidence examples                                                                                                                                     |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4853        | Defective or Not As Described | The cardholder claims that the goods or services they received were defective, damaged, or not as described at the time of purchase. This can apply to physical goods that arrive in poor condition, are defective, or don’t match the product listing. It can also apply to digital goods or services that don’t function as expected or differ from the advertised description, as well as travel services that don’t meet expectations based on the booking details. | - **Proof of product or service description:** Provide product listings, service descriptions, and customer agreements that match what was delivered. |

- **Proof of delivery and acceptance:** If the customer signed for or confirmed receipt of the product or service, include this evidence.
- **Photographic evidence:** Provide images of the item before shipment, including serial numbers or inspection tags.
- **Proof of digital access:** For digital goods, include logs showing usage, downloads, or customer interactions with the product.
- **Customer communications:** If the customer didn’t report an issue before filing the chargeback, provide any messages indicating acceptance of the product or service.
- **Refund and return policies:** Highlight policies agreed to at checkout, especially if the customer bypassed the proper refund process. |

## Subscription canceled

The _Subscription Canceled_ dispute category refers to situations where a cardholder claims they were charged for a recurring service or subscription after cancellation. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#subscription-canceled).

| Reason code | Reason                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Evidence examples                                                                                                          |
| ----------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 4841        | Canceled Recurring or Digital Goods Transactions | The cardholder claims they were charged for a recurring subscription or digital product after canceling or that they never authorized the charge. This applies to recurring billing disputes, where the cardholder claims they canceled a subscription, but the merchant continued billing them. It also applies to digital goods disputes, where the cardholder disputes a charge for a digital subscription product, claiming they never received or authorized it. This category also includes trial conversions, where the cardholder forgot to cancel a free trial and disputes the charge. | - **Proof of subscription agreement:** Show that the customer signed up for a recurring charge and agreed to auto-renewal. |

- **Cancellation policy:** Provide terms and conditions stating how and when customers must cancel to avoid charges.
- **Proof of non-cancellation:** Show that the customer didn’t submit a cancellation request before the billing date.
- **Usage logs:** For digital goods, provide login records, access logs, downloads, or service usage timestamps.
- **Customer communications:** If the customer asked about cancellation but didn’t complete it, include chat logs or emails.
- **Refund and dispute policies:** Show policies regarding cancellations and refunds, especially for digital goods. |

#### American Express

## Credit not processed

The _Credit Not Processed_ dispute category typically occurs when a cardholder claims they were entitled to a refund or credit, but it was never processed or received. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#credit-not-processed).

| Reason code | Reason                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Evidence examples                                                                               |
| ----------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| A01         | Charge Amount Exceeds Authorization Amount | When the final transaction amount submitted by the merchant is greater than the originally approved authorization amount. This can happen when: Additional charges, fees, or gratuities were added after the authorization approval. The total transaction exceeded the approved authorization by more than 15% (for hotels, car rentals, or cruise lines) or 30% (for restaurants), without obtaining a new authorization. Check your current industry-specific guidelines for this. An authorization wasn’t properly updated to reflect the final transaction total. | - **Proof of authorization:** Show that the final transaction amount had a valid authorization. |

- **Signed agreement or consent:** If the customer agreed to additional charges (for example, hotel incidentals, car rental fees), provide signed documents.
- **Itemized invoice or receipt:** Break down all charges, including gratuities, fees, and incidentals.
- **Customer communications:** If you informed the customer about additional fees and they acknowledged them, provide emails or chat logs. |
  | C02 | Credit Not Processed | A cardholder claims they were entitled to a refund or credit, but it was never processed. This applies to returned merchandise where a refund was promised but not issued. It also covers canceled services where the cardholder expected a credit. Additionally, this category includes duplicate charges where one charge was supposed to be refunded but wasn’t. Furthermore, it applies to travel or event cancellations where the merchant agreed to issue a refund but failed to do so. | - **Proof of refund issuance:** Provide a transaction record showing the credit was processed, including date and amount.
- **Refund policy:** Show that the cardholder agreed to terms stating when a refund would or wouldn’t be provided.
- **Return or cancellation policy:** Provide evidence that the cardholder didn’t comply with return or cancellation requirements.
- **Customer communications:** If you informed the cardholder about refund timelines or non-refundable terms, include these interactions.
- **Transaction logs:** Show that the charge was valid and no duplicate credit was required. |
  | C04 | Goods/Services Returned | A cardholder claims they returned goods or canceled services, but didn’t receive a refund. This applies to e-commerce returns where the merchant allegedly didn’t process a refund. It also covers in-store returns where the cardholder claims they returned an item but weren’t credited. Additionally, this category includes subscription cancellations where the cardholder claims they followed the return policy but were still billed. | - **Return tracking and receipts:** If the item was never returned, provide shipping records showing no return was received.
- **Refund confirmation:** If you already processed the refund, provide a transaction record with the date and reference number.
- **Return policy and deadlines:** Show that the customer failed to return the item within the required timeframe.
- **Product inspection reports:** If the returned item was damaged, used, or different from the original, include photos or notes from the quality control team.
- **Customer communications:** If you notified the customer of return requirements, include emails or chat logs. |
  | C05 | Goods/Services Canceled | This applies to hotel or travel reservations that were canceled but still charged. It also covers memberships or subscriptions that continued billing after cancellation. Additionally, this category includes retail orders that were canceled before shipping but were still charged. | - **Proof of cancellation policy:** Provide terms stating cancellation deadlines and refund conditions.
- **Proof of non-cancellation:** Show that you didn’t receive a cancellation request before the charge.
- **Service usage logs:** If the service was used (for example, hotel stay, gym membership), provide check-in records or access logs.
- **Customer communications:** If you informed the cardholder about non-refundable terms, include those emails or chat logs.
- **Signed agreements:** If the cardholder agreed to a contract with cancellation policies, include it. |
  | C18 | No Show or CARDeposit Canceled | A cardholder claims they canceled a lodging reservation or expected a refund for a Car Rental Deposit (CARDeposit), but didn’t receive it. This can happen when the cardholder canceled a reservation, but the merchant didn’t process the cancellation or refund in time. It can also occur when the cardholder misunderstood the cancellation policy and believed they were eligible for a refund. In some cases, a reservation cancellation might have been attempted but was unsuccessful due to system or communication errors. Additionally, this category includes instances where the cardholder was charged a “No Show” fee despite canceling the reservation within the required timeframe. | - **Proof of cancellation policy:** Provide the terms that you presented to the customer at the time of booking.
- **Booking confirmation:** Show that the cardholder agreed to the cancellation terms when making the reservation.
- **Cancellation logs:** If the cardholder attempted to cancel too late, provide timestamps or customer service interactions.
- **Proof of refund (if applicable):** Show that you already processed a refund before the dispute was filed.
- **No show records:** If you billed the cardholder for non-arrival, provide check-in records showing that the customer didn’t show up. |
  | P03 | Credit Processed as Charge | A cardholder claims that a credit (refund) they were expecting was instead processed as a charge. This can happen due to processing errors, miscommunication regarding refunds, or customer misunderstandings. | - **Proof of refund processing:** Provide records showing you issued the credit, including transaction IDs, timestamps, and system logs.
- **Proof that no refund was due:** If you never promised or required a refund, provide terms and conditions supporting this.
- **Pre-authorization or temporary hold details:** If the charge was actually a pre-authorization that later dropped off, include authorization and settlement records.
- **Customer communications:** Include email or chat transcripts where you discussed, approved, or clarified the refund.
- **Merchant system logs:** Show any internal notes on refunds, cancellations, or transaction adjustments.
- **Comparison of charge and credit transactions:** If the customer received a refund but confused it with a new charge, provide documentation showing both transactions. |
  | P05 | Incorrect Charge Amount | A cardholder claims they were charged an incorrect amount for a transaction. This applies to pricing errors at checkout, where the amount charged differs from what was displayed. It also covers tip adjustments (for example, in restaurants and salons) where the final charge is higher than expected. Additionally, this category includes incorrectly processed refunds or partial refunds, where the credited amount was less than promised. Furthermore, it applies to currency conversion discrepancies, where the final charge differs from what was displayed due to exchange rates or fees. | - **Proof of transaction authorization:** Provide receipts, invoices, or digital confirmations showing the agreed amount.
- **Signed receipts or digital acknowledgment:** If the cardholder signed or confirmed the amount, this serves as strong evidence.
- **Breakdown of charges:** Itemized receipts showing base price, taxes, fees, tips, or currency conversion details.
- **Merchant policies:** Show refund, tipping, or pricing policies that you disclosed before the transaction.
- **Exchange rate proof:** For international transactions, provide documentation of the exchange rate at the time of processing.
- **Customer communications:** If the cardholder reached out with concerns about the charge before disputing, include those interactions. |

## Duplicate

The _Duplicate_ dispute category refers to situations where a cardholder claims they were charged multiple times for a single transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#duplicate).

| Reason code | Reason              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Evidence examples                                                                                                                         |
| ----------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| C14         | Paid by Other Means | A cardholder claims that they were charged on their American Express card for a transaction that was already paid for using a different payment method. This can happen when: The charge was billed to an Amex card instead of another payment method the cardholder intended to use. A cardholder made a duplicate payment, and you didn’t issue a credit for the extra charge. Another person (for example, a travel companion, business partner, or guest) paid for the charge, but you also charged the Amex card. The cardholder expected the charge to be covered by a third party, such as insurance or employer reimbursement. | - **Proof of cardholder authorization:** Show signed receipts, emails, or agreements where the cardholder confirmed payment through Amex. |

- **Payment records:** Demonstrate that no duplicate charge exists, or provide proof of how you applied the payments.
- **Transaction logs:** Show timestamps and approval details for the charge.
- **Refund confirmation:** If you found a duplicate charge and already refunded it, provide evidence of the credit transaction. |
  | P08 | Duplicate Charge | A cardholder claims they were charged more than once for the same transaction. This applies to: Accidental duplicate processing, where the merchant unintentionally submits the charge multiple times. Cardholder misunderstanding, where they mistake a pending authorization for a duplicate charge. Technical issues, such as a system glitch causing the same charge to be processed twice. | - Transaction logs: Show that only one charge was successfully processed.
- Payment processing records: If a duplicate did occur but was voided, reversed, or refunded, provide documentation.
- Receipts and invoices: Show that the charges correspond to different transactions, dates, or services.
- Recurring or installment payment agreements: If the charge is part of a subscription or payment plan, provide the agreement.
- Pre-authorization and settlement proof: Demonstrate that one charge was an authorization hold that later cleared, not an actual duplicate transaction.
- Customer communications: If the cardholder reached out before filing a chargeback, include any relevant interactions confirming their misunderstanding. |

## Fraudulent

The _Fraudulent_ dispute category refers to situations where a cardholder claims they didn’t authorize or participate in a transaction. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#fraudulent).

| Reason code | Reason          | Description                                                                                                                                                                                                                                                                                                                                                                                                                               | Evidence examples                                                                                                                     |
| ----------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| F10         | Missing Imprint | A cardholder denies participation in a transaction, and the merchant failed to obtain a physical or electronic imprint of the card. This can happen when you didn’t swipe, insert, or tap the card at the time of purchase. It can also occur when you manually entered the transaction without a manual imprint of the card. Additionally, this applies when you failed to collect and store proof that the card was physically present. | - **Proof of card imprint:** If you obtained an imprint, provide a copy showing the Primary Account Number (PAN) and cardholder name. |

- **Transaction logs:** Show details of the transaction, including card entry method and approval status.
- **Surveillance footage:** If available, provide video evidence showing the cardholder present at the point of sale.
- **Signed receipt:** If you captured a signature, include a copy for verification.
- **Keyed No Imprint Program enrollment:** If applicable, provide proof that your business is enrolled in this program. |
  | F24 | Multiple ROCs | A cardholder denies participating in one or more transactions after previously making a valid purchase with the same merchant. This can happen when you processed multiple transactions using the same card but didn’t clearly link them. It can also occur when you submitted additional transactions without clear cardholder authorization. Additionally, this applies when the cardholder mistakenly believes you double-charged them or charged them for an unauthorized transaction. | - **Proof of cardholder authorization:** Provide signed receipts, online purchase confirmations, or agreement to terms.
- **Itemized invoice or receipt:** Show how multiple charges were part of a valid transaction set.
- **Transaction logs:** Provide timestamps, payment methods, and authorization approvals.
- **Refund confirmation (if applicable):** Show that you already credited the customer for any duplicate charge. |
  | F29 | Card Not Present | A cardholder claims they didn’t authorize a Card-Not-Present (CNP) transaction. This applies to e-commerce purchases where no physical card was used. It also covers mail or telephone orders (MOTO) transactions. Additionally, this category includes subscription-based billing where the customer claims they didn’t agree to the charge. | - **3D Secure authentication records:** Show that the cardholder completed multi-factor authentication.
- **AVS and CID verification results:** Provide evidence that the billing address and security code matched.
- **IP address and device fingerprinting:** Show that the transaction was made from a familiar device or location.
- **Order confirmation and invoices:** Include records of purchase confirmation sent to the cardholder.
- **Delivery tracking and signed receipts:** If physical goods were delivered, provide tracking logs and signed delivery confirmation.
- **Customer communications:** If the cardholder contacted you before disputing (for example, support inquiries, refund requests), include those interactions. |
  | F30 | EMV Liability Shift—Counterfeit | A cardholder denies participating in a transaction, and the charge was processed on a counterfeit EMV chip card at a point-of-sale (POS) terminal that wasn’t chip-enabled. This happens when a counterfeit card was used in a card-present transaction, but the merchant’s POS system was unable to process chip transactions. It can also occur when the merchant processed the transaction manually instead of using the EMV chip. Additionally, this applies when a non-compliant terminal accepted a counterfeit card without chip verification, triggering the liability shift to the merchant. | - **Proof of EMV chip transaction:** Provide logs showing you used the chip for the transaction.
- **Transaction logs:** Show details of the transaction, including authorization method and approval status.
- **POS system records:** Demonstrate that the terminal was chip-enabled and processed the card correctly.
- **Surveillance footage (if applicable):** If available, provide video evidence showing the cardholder at the point of sale. |
  | F31 | EMV Liability Shift—Lost/Stolen/Non-Received | A cardholder denies participating in a transaction, and the charge was processed on a lost, stolen, or non-received EMV chip card at a point-of-sale (POS) terminal that wasn’t chip-and-PIN enabled. This happens when someone used a lost or stolen card at a terminal that didn’t support PIN verification or intercepted the card before it reached the cardholder and used it fraudulently. This also happens when a non-compliant POS system accepted the transaction without proper chip-and-PIN security, shifting liability to the merchant. | - **Proof of EMV chip-and-PIN transaction:** Provide logs showing you used chip-and-PIN authentication for the transaction.
- **Transaction logs:** Show details of the transaction, including authorization method and approval status.
- **POS system records:** Demonstrate that the terminal was chip-and-PIN enabled and processed the card correctly.
- **Surveillance footage (if applicable):** If available, provide video evidence showing the cardholder at the point of sale. |
  | FR2 | Fraud Full Recourse Program | A cardholder denies authorizing a charge, and the merchant is enrolled in the Fraud Full Recourse Program. This means American Express considers the merchant high-risk for fraud-related disputes, leading to automatic chargebacks when a cardholder claims fraud. In this scenario, the cardholder claims they didn’t authorize the transaction, and American Express doesn’t require further proof before initiating the chargeback. Once a merchant is in this program, they bear full liability for fraud-related chargebacks, even if they processed the transaction securely. | - **Proof of enrollment status:** Provide evidence that you weren’t in the Fraud Full Recourse Program at the time of the charge.
- **Refund confirmation (if applicable):** Show that you already processed a refund before the dispute.
- **Transaction logs:** Provide transaction details, including authorization status and fraud prevention measures you used. |

## General

The _General_ dispute category typically serves as a catch-all for disputes that don’t fit neatly into other more specific categories. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#general).

| Reason code | Reason                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Evidence examples                                                                     |
| ----------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| A02         | No Valid Authorization | A merchant submits a charge without a valid authorization approval. This can happen when an authorization was required but never obtained. It can also occur when an authorization was declined, yet the charge was still submitted. Additionally, this applies when the charge was processed after the authorization had expired. Furthermore, this category includes instances where the card was expired or not yet valid at the time of the transaction. | - **Proof of authorization:** Show the valid authorization code and approval details. |

- **Transaction logs:** Demonstrate that the charge matches the authorized amount and date.
- **Authorization system data:** Provide logs showing when and how you requested and received approval for the authorization.
- **Card validity confirmation:** If disputed due to an expired card, prove that the charge occurred before the expiration date. |
  | A08 | Authorization Approval Expired | A merchant submits a charge after the original authorization approval has expired. This can happen when the merchant didn’t submit the transaction for settlement within the allowable time frame (typically 7 days). It can also occur when a transaction took place in a delayed service industry (for example, lodging, car rentals, cruises) but wasn’t re-authorized. Additionally, this applies when an order was placed but not fulfilled immediately, and the charge was submitted too long after the initial authorization. | - **Proof of valid authorization:** Provide logs showing that you submitted the charge within the allowed timeframe.
- **Updated authorization records:** If you obtained a new authorization, submit that proof.
- **Industry-specific authorization policies:** If applicable (for example, hotels, car rentals), show how the charge adhered to extended authorization rules.
- **Transaction logs:** Demonstrate that you properly submitted and received approval for the charge. |
  | M10 | Incorrect Liability for Vehicle Rental | A cardholder claims they were incorrectly billed for capital damages, theft, or loss of use related to a vehicle rental. This typically happens when the cardholder disputes liability for some or all of the vehicle damages. It can also occur when the cardholder believes a third party (such as insurance) should have covered the charges. Additionally, this applies when the billed amount doesn’t match the amount the cardholder agreed to pay. Furthermore, this category includes instances where the repair costs exceed the original estimate without the cardholder’s additional consent. The cardholder may also dispute a charge for loss of use or theft of the rental vehicle. | - **Signed liability agreement:** Provide proof that the cardholder acknowledged responsibility for damages.
- **Itemized repair invoice:** Show that the charges align with documented repair costs.
- **Rental agreement:** Demonstrate that the cardholder accepted rental terms, including liability for damages, theft, or loss of use.
- **Proof of insurance waiver (if applicable):** Show that the cardholder declined coverage and accepted financial responsibility. |
  | R03 | Insufficient Reply | A merchant fails to provide an adequate or timely response to a chargeback inquiry. This can happen when the merchant didn’t submit evidence in time to counter a dispute. It can also occur when the merchant’s response lacked sufficient documentation to refute the claim. Additionally, this applies when the merchant’s reply didn’t directly address the reason for the chargeback. | - **Proof of response submission:** Show timestamps, email confirmations, or dispute platform records proving you submitted the response within the deadline.
- **Complete dispute documentation:** If the original response lacked information, submit a full package with all required documents (for example, receipts, shipping confirmations, customer communications).
- **Dispute acknowledgment from American Express:** If you received confirmation that your response was received but still lost the case, provide this as evidence.
- \*\*Internal records of submission process: If you handled the dispute through a third-party processor or chargeback management system, provide logs from that system.
- **Customer communications:** If you could have resolved the dispute with the cardholder before escalating, provide proof of attempts to engage. |
  | R13 | No Reply | A merchant fails to respond to a chargeback inquiry within the required timeframe. This applies to cases where the merchant didn’t submit any response to the dispute. It also covers situations where the merchant missed the deadline to provide supporting documentation. Additionally, this category includes instances where the dispute was automatically decided in favor of the cardholder due to non-response. | - **Proof of response submission:** Show timestamps, email confirmations, or chargeback system records proving you submitted the response before the deadline.
- **Payment processor logs:** If using a third-party chargeback management system, provide records showing that the response was forwarded to American Express.
- **Dispute case reference numbers:** Include any American Express dispute case numbers that can verify when you filed the response.
- **Customer communications:** If you could have resolved the chargeback with the cardholder before escalating, provide proof of attempts to engage.
- **Technical issue reports:** If a system failure or processing error caused the lack of response, provide documentation supporting this claim. |
  | P01 | Unassigned Card Number | This chargeback occurs when a transaction is processed using an invalid or unassigned card number. This typically happens due to clerical errors, use of outdated or canceled card numbers, or incorrectly entered account details. | - Proof of authorization: Documentation showing you authorized the transaction using a valid card number.
- Charge record: If you processed the charge through a payment terminal, include a record of the transaction with the correct card details.
- Card imprint or digital transaction record: For manually entered transactions, an imprint or digital confirmation showing the correct card number can support your case.
- Customer communication: If the cardholder later provided updated payment details, include proof of that communication.
- Billing policies: Provide any terms stating that customers must update their payment methods for recurring transactions. |
  | P04 | Charge Processed as Credit | A cardholder claims that a transaction expected to be a charge was instead processed as a credit. This typically happens due to merchant processing errors, system misconfigurations, or customer misunderstanding of how transactions are displayed on their statements. | - **Proof of proper transaction processing:** Provide records showing you completed the charge as expected, including transaction IDs and timestamps.
- **Merchant system logs:** Show internal records verifying how you processed the transaction.
- **Customer communications:** Include email or chat logs confirming the charge, any refund discussions, or clarifications on the transaction.
- **Pre-authorization or temporary credit details:** If the credit was a pending adjustment that later cleared, include settlement records.
- **Comparison of credit and charge transactions:** If the customer misunderstood a pending credit, provide documentation showing the final charge. |
  | P07 | Late Submission | A transaction isn’t submitted within the required timeframe, causing the cardholder to dispute the charge. This typically happens when a merchant delays processing a transaction, and by the time it’s submitted, the cardholder no longer recognizes or expects the charge | - **Proof of submission date:** Provide transaction records showing the exact date you processed the charge.
- **Industry-specific processing rules:** If your business operates in an industry where delayed submissions are permitted, reference these rules.
- **Customer communications:** Include any emails or agreements where you informed the customer of potential billing delays.
- **Authorization details:** Show that the original authorization was valid and within American Express guidelines.
- **Merchant system logs:** Provide internal records verifying when and how you processed the transaction. |
  | P22 | Non-Matching Card Number | A cardholder claims that a transaction was processed using a card number that doesn’t match any card on their account. This often results from merchant processing errors, data entry mistakes, or issues with account number validation. | - **Transaction logs:** Provide details showing the card number used, authorization response, and settlement records.
- **Issuer authorization records:** If American Express approved the charge, this confirms that the card was valid at the time of purchase.
- **Merchant system logs:** Show internal records verifying how you processed the transaction and which card details you used.
- **Customer communications:** Include emails or chat logs where the customer acknowledges the transaction or provides card details.
- **Tokenization or stored credential verification:** If you correctly stored and retrieved the card number, provide system logs confirming this. |
  | P23 | Currency Discrepancy | A cardholder claims that the transaction was processed in the wrong currency or that the exchange rate applied was incorrect. This applies to international transactions where the cardholder expected to be charged in their home currency but was billed in a different one. It also covers Dynamic Currency Conversion (DCC) disputes, where the cardholder claims they didn’t opt into currency conversion. Additionally, this category includes exchange rate discrepancies, where the final charge in the cardholder’s currency was higher than expected. | - **Proof of currency selection:** Show that the cardholder opted into a particular currency at checkout.
- **Checkout confirmation:** Provide invoices, receipts, or digital confirmations displaying the agreed-upon currency and amount.
- **Dynamic Currency Conversion (DCC) agreement:** If DCC was used, provide proof that the cardholder accepted the conversion.
- **Exchange rate details:** Show the exchange rate used at the time of the transaction.
- **Merchant policies:** Provide terms stating how you handle currency conversion and international transactions.
- **Customer communications:** If the cardholder inquired about currency conversion before disputing, include any relevant interactions. |

## Product not received

The _Product Not Received_ dispute category refers to situations where a cardholder claims they didn’t receive the purchased goods or services. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-not-received).

| Reason code | Reason                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Evidence examples                                                                                                  |
| ----------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| C08         | Goods/Services Not Received or Only Partially Received | A cardholder claims they didn’t receive the goods or services they paid for, or they only received part of what was purchased. This can apply to physical goods that were never delivered or only partially shipped. It also covers services that weren’t rendered as expected. Additionally, this category includes digital goods that were inaccessible. Furthermore, it applies to event tickets, travel bookings, or appointments where the cardholder claims they were denied access. | - **Proof of shipment and delivery:** Provide tracking details, carrier confirmation, or signed delivery receipts. |

- **Proof of digital access:** For digital goods, include login records, download logs, or timestamps of product usage.
- **Proof of service completion:** Provide appointment records, work logs, check-in confirmations, or service contracts.
- **Customer communications:** Include any interactions confirming receipt, troubleshooting requests, or delivery inquiries.
- **Terms and policies:** Show refund, fulfillment, and delivery policies, including agreement at checkout. |

## Product unacceptable

The _Product Unacceptable_ dispute category refers to situations where a cardholder claims the received product or service doesn’t match what was described or expected. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#product-unacceptable).

| Reason code | Reason                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Evidence examples                                                                                                                                     |
| ----------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| C31         | Goods/Services Not as Described | A cardholder claims that the goods or services they received were defective, damaged, or didn’t match the description provided at the time of purchase. This applies to physical goods that differ from what was advertised or arrive damaged. It also covers services that weren’t performed as expected. Additionally, this category includes digital products or software that didn’t function as described. Furthermore, it applies to travel accommodations that didn’t meet the booking details. | - **Proof of product or service description:** Provide product listings, service descriptions, and customer agreements that match what was delivered. |

- **Proof of delivery and acceptance:** If the customer signed for or confirmed receipt of the product or service, include this evidence.
- **Photographic evidence:** Provide images of the item before shipment, including serial numbers or inspection tags.
- **Proof of service completion:** If the dispute is related to a service, include work logs, appointment records, or signed agreements.
- **Customer communications:** If the customer didn’t report an issue before filing the chargeback, provide any messages indicating acceptance of the product or service.
- **Refund and return policies:** Highlight policies agreed to at checkout, especially if the customer bypassed the proper refund process. |
  | C32 | Goods/Services Damaged or Defective | A cardholder claims that the goods they received were damaged or defective or that the services provided were faulty or incomplete. This applies to physical goods that arrived broken, malfunctioning, or otherwise unusable. It also covers services that were performed incorrectly or didn’t meet the expected quality. Additionally, this category includes digital products or software that contained errors or didn’t function as promised. Furthermore, it applies to travel accommodations where conditions were unsatisfactory (for example, a hotel with non-working utilities). | - **Proof of product or service description:** Provide product listings, service descriptions, and customer agreements that match what was delivered.
- **Proof of delivery and acceptance:** If the customer signed for or confirmed receipt of the product or service, include this evidence.
- **Photographic evidence:** Provide images of the item before shipment, including serial numbers or inspection tags.
- **Inspection reports:** If you checked the product before shipping or at delivery, provide quality control records.
- **Customer communications:** If the customer didn’t report an issue before filing the chargeback, provide any messages indicating acceptance of the product or service.
- **Return and refund policies:** Highlight policies agreed to at checkout, especially if the customer bypassed the proper refund process. |

## Subscription canceled

The _Subscription Canceled_ dispute category refers to situations where a cardholder claims they were charged for a recurring service or subscription after cancellation. To help guide you through sample evidence submission scenarios, see the following [visual examples](https://docs.stripe.com/disputes/visual-evidence.md#subscription-canceled).

| Reason code | Reason                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Evidence examples                                                                                                          |
| ----------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| C28         | Canceled Recurring Billing | A cardholder claims they were charged for a recurring subscription or service after canceling. This applies to subscription-based services (for example, streaming platforms, SaaS, memberships) where the cardholder claims they canceled but were still charged. It also covers trial periods that auto-renewed when the cardholder claims they opted out. Additionally, this category includes recurring utility, insurance, or installment payments that continued despite a cancellation request. | - **Proof of subscription agreement:** Show that the customer signed up for a recurring charge and agreed to auto-renewal. |

- **Cancellation policy:** Provide terms stating how and when customers must cancel to avoid charges.
- **Proof of non-cancellation:** Show that the customer didn’t submit a cancellation request before the billing date.
- **Usage logs:** For digital goods or services, provide login records, downloads, or timestamps showing product or service usage after the charge.
- **Customer communications:** If the customer asked about cancellation but didn’t complete it, include chat logs or emails.
- **Refund and dispute policies:** Show policies regarding cancellations and refunds, especially if the subscription was non-refundable. |

## Local payment method reason codes

The reason codes on this page apply to Visa, Mastercard, and American Express. Local payment methods (LPMs) don’t use card network reason codes. Instead, each LPM provider defines its own reason codes based on the types of disputes on its platform.

Stripe maps LPM reason codes to the same [seven dispute categories](https://docs.stripe.com/disputes/categories.md) used for card disputes, so you can manage LPM disputes through the same Stripe Dashboard and API interfaces. However, the underlying reason codes and evidence requirements for each category can differ from card disputes.

For LPM-specific reason codes and evidence guidance, see the dispute information for each payment method:

- [Klarna dispute reason codes](https://docs.stripe.com/disputes/categories.md?card-network=klarna)
- [PayPal disputed payments](https://docs.stripe.com/payments/paypal/disputed-payments.md)
