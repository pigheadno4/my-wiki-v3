<!-- Source URL: https://docs.paypal.ai/payments/methods/pay-later -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pay Later

PayPal offers special financing options that payers can use to buy now and pay later, while merchants get paid up front. Specific Pay Later offers differ by country.

The following illustration shows the basic user experience with Pay Later in the US.

![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some headphones. Step 2 shows the customer choosing between monthly and Pay in 4 options for Pay Later. In step 3, the user sees a screen that describes the Pay in 4 payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-us-flow.png)

To add Pay Later offers to an integration with a third-party commerce platform, see <a href="https://developer.paypal.com/docs/checkout/pay-later/us/commerce-platforms/">Commerce Platforms</a>.

For information about how you can use PayPal's JavaScript SDK for a low-code Pay Later integration, see <a href="https://docs.paypal.ai/payments/methods/pay-later/get-started/" target="_blank">Get started with Pay Later</a>.

## Features

With Pay Later, you can get:

- **Increased conversion:** Adding "buy now, pay later" messaging to your site can improve conversion, attract new customers, and increase order values.
- **Dynamic messages:** You can show your customers a Pay Later offer that is based on the contents of their shopping cart.
- **Multiple touch points:** Add messaging throughout your site such as on product pages, the shopping cart, and checkout pages.

## Country-specific details

For information about country-specific Pay Later offers, select a tab.

<Tabs>
  <Tab title="United States">
    PayPal offers special financing options that payers can use to buy now and pay later, while merchants get paid upfront. For more information about Pay Later, see <a href="https://www.paypal.com/us/digital-wallet/ways-to-pay/buy-now-pay-later?_ga=2.37466658.365520210.1755702720-1032254505.1740765755" target="_blank">Buy now, pay later</a>.

    | Product     | Number of payments | Due                      | Purchase amount  |
    | ----------- | ------------------ | ------------------------ | ---------------- |
    | Pay in 4    | 4                  | Every 2 weeks (biweekly) | \$30 to \$1,500  |
    | Pay Monthly | 3, 6, 12, or 24    | Monthly                  | \$49 to \$10,000 |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-us-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in the US if you meet all of the following requirements:

    * Are a US-based PayPal merchant.
    * Have a US-facing website.
    * Transact in US dollars (USD).
    * Have a one-time payment integration, and Pay Later options are available through PayPal checkout.
    * Abide by the <a href="https://www.paypal.com/us/legalhub/paypal/pay-later-messaging-tnc?locale.x=en_US&_ga=2.230264284.1105075193.1757947850-1032254505.1740765755" target="_blank">Pay Later Messaging Center Program Terms</a>.
    * Do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage the use of this product or remove any content. Render the Pay Later messaging in its entirety with all the links and language provided by PayPal. For noncompliant messaging, PayPal reserves the right to take action in accordance with the <a href="https://developer.paypal.com/studio/checkout/pay-later/paypal.com" target="_blank">PayPal User Agreement</a>.
    * Do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    > **Notes:**
    >
    > * Reference Transaction and Recurring Payment integrations aren't eligible for Pay Later offers.
    > * Pay in 4 loans to CA residents are made or arranged pursuant to a CA Financing Law License. PayPal, Inc., is a GA Installment Lender Licensee, NMLS #910457. RI Small Loan Lender Licensee.
    > * A Pay Monthly agreement is subject to consumer credit approval. Term lengths and fixed APR of 9.99-35.99% vary based on the customer’s creditworthiness. The lender for Pay Monthly is WebBank. PayPal, Inc. (NMLS #910457): RI Loan Broker Licensee. VT Loan Solicitation Licensee.

    **See also**

    * <a href="https://www.paypal.com/us/legalhub/paypal/pay-later-messaging-tnc?locale.x=en_US" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/us/legalhub/paypal/acceptableuse-full?locale.x=en_US&_ga=1.239760260.663165815.1628012939" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/us/legalhub/paypal/useragreement-full#advertising-program" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/us/legalhub/paypal/useragreement-full" target="_blank">PayPal User Agreement</a>

  </Tab>

  <Tab title="Australia">
    Pay Later in Australia includes **Pay in 4**, which eligible Australian buyers can use to pay in 4 interest-free payments for purchases of \$1 to \$1,999.99 AUD. The first payment is due at the time of the transaction, and subsequent payments are due every 2 weeks.

    | Product  | Number of payments | Due                      | Purchase amount       |
    | -------- | ------------------ | ------------------------ | --------------------- |
    | Pay in 4 | 4                  | Every 2 weeks (biweekly) | \$1 to \$1,999.99 AUD |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-au-messaging.png)

    **Eligibilty**

    You're eligible to integrate Pay Later offers in Australia if you meet all of the following requirements:

    * You're an Australia-based PayPal merchant.
    * You have an Australia-facing website.
    * You transact in Australian dollars (AUD).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/au/legalhub/paypal/acceptableuse-full?locale.x=en_AU&_ga=2.40974690.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage the use of this product or remove any content. Render the Pay Later messaging in its entirety with all the links and language provided by PayPal. For noncompliant messaging, PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/au/legalhub/paypal/useragreement-full?locale.x=en_AU&_ga=2.141621618.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal User Agreement</a>.
    * You do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    > **Note:** PayPal Credit Pty Limited (ABN 66 600 629 258) provides PayPal **Pay in 4**. PayPal Credit Pty Limited holds Australian Credit Licence Number 568848.

    The following illustration shows how Pay Later works for customers in Australia.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some headphones. Step 2 shows the customer choosing between monthly and Pay in 4 options for Pay Later. In step 3, the user sees a screen that describes the Pay in 4 payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-au-flow.png)

    **See also**

    * <a href="https://www.paypal.com/au/legalhub/paypal/pay-later-messaging-tnc?_ga=2.207893146.989760939.1760545530-1032254505.1740765755" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/au/legalhub/paypal/acceptableuse-full?locale.x=en_AU&_ga=2.207893146.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/au/legalhub/paypal/useragreement-full?_ga=2.207893146.989760939.1760545530-1032254505.1740765755#advertising-program" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/au/legalhub/paypal/useragreement-full?locale.x=en_AU&_ga=2.164894391.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal User Agreement</a>

  </Tab>

  <Tab title="France">
    Pay Later in France includes **Pay in 4**, which is an installment offer that allows consumers to spread the cost of a purchases across 4 equal payments for transactions between 30€ and 2,000€. The first payment is due at the time of the transaction. The subsequent payments spread across 90 days.

    | Product  | Number of payments | Due     | Purchase amount |
    | -------- | ------------------ | ------- | --------------- |
    | Pay in 4 | 4                  | Monthly | 30€ to 2,000€   |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-fr-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in France if you meet all of the following requirements:

    * You're a France-based PayPal merchant.
    * You have a France-facing website.
    * You transact in euros (EUR).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/fr/webapps/mpp/ua/acceptableuse-full?locale.x=fr_FR&_ga=2.37446752.1323232211.1760020831-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage use of this product. PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/fr/webapps/mpp/ua/useragreement-full?locale.x=fr_FR&_ga=2.189361387.1323232211.1760020831-1032254505.1740765755" target="_blank">PayPal User Agreement</a>.
    * You do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    > **Note:** PayPal Pay Later is not available in all markets. PayPal Pay Later eligibility and availability is subject to merchant status, sector and integration. Consumer eligibility is subject to status and approval. Product features differ by market. See relevant product terms for more details. PayPal Pay Later cross-border messaging is subject to approval by PayPal.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some sunglasses. Step 2 shows the customer choosing a payment option. In step 3, the user sees a screen that describes the Pay in 4 payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-fr-flow.png)

    **See also**

    * <a href="https://www.paypal.com/fr/legalhub/paypal/pay-later-messaging-tnc?_ga=2.172700203.989760939.1760545530-1032254505.1740765755" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/fr/legalhub/paypal/acceptableuse-full?locale.x=fr_FR&_ga=2.172700203.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/fr/legalhub/paypal/useragreement-full?_ga=2.172700203.989760939.1760545530-1032254505.1740765755#receive-payment1" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/fr/legalhub/paypal/useragreement-full?locale.x=fr_FR&_ga=2.173768107.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal User Agreement</a>

  </Tab>

  <Tab title="Germany">
    Pay Later in Germany includes installment options and **Pay in 30 Days**.

    | Product             | Number of payments           | Due                              | Purchase amount |
    | ------------------- | ---------------------------- | -------------------------------- | --------------- |
    | PayPal Ratenzahlung | 3, 6, 12, or 24 installments | Monthly                          | 99€ to 10,000€  |
    | Pay in 30 Days      | 1                            | Single payment due after 30 days | 1€ to 2,000€    |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-de-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in Germany if you meet all of the following requirements:

    * You're a Germany-based PayPal merchant.
    * You have a Germany-facing website.
    * You transact in euros (EUR).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/de/webapps/mpp/ua/acceptableuse-full?locale.x=en_DE&_ga=2.96210268.1323232211.1760020831-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage use of this product. PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/de/webapps/mpp/ua/useragreement-full?locale.x=de_DE&_ga=2.32687486.1323232211.1760020831-1032254505.1740765755" target="_blank">PayPal User Agreement</a>.
    * You do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    > **Note:** PayPal Pay Later is not available in all markets. PayPal Pay Later eligibility and availability is subject to merchant status, sector and integration. Consumer eligibility is subject to status and approval. Product features differ by market. See relevant product terms for more details. PayPal Pay Later cross-border messaging is subject to approval by PayPal.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy a purse. Step 2 shows the customer choosing a payment option. In step 3, the user sees a screen that describes the payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-de-flow.png)

    **See also**

    * <a href="https://www.paypal.com/de/legalhub/paypal/pay-later-messaging-tnc?_ga=2.173824299.989760939.1760545530-1032254505.1740765755" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/de/legalhub/paypal/acceptableuse-full?locale.x=en_DE&_ga=2.173824299.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/de/legalhub/paypal/useragreement-full?_ga=2.173824299.989760939.1760545530-1032254505.1740765755#receive-payment1" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/de/legalhub/paypal/useragreement-full?locale.x=de_DE&_ga=2.173824299.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal User Agreement</a>

  </Tab>

  <Tab title="Italy">
    Pay Later in Italy includes **Pay in 3** installments, which allows eligible buyers in Italy to spread the cost of a purchase across 3 interest-free payments for purchases of 30€-2,000€. The first payment is due at the time of the transaction, and subsequent payments are due every month.

    | Product  | Number of payments | Due     | Purchase amount |
    | -------- | ------------------ | ------- | --------------- |
    | Pay in 3 | 3                  | Monthly | 30€ to 2,000    |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-it-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in Italy if you meet all of the following requirements:

    * You’re an Italy-based PayPal merchant.
    * You have an Italy-facing website.
    * You transact in euros (EUR).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/it/legalhub/paypal/acceptableuse-full?locale.x=it_IT&_ga=2.264904015.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You don't edit Pay Later messages with additional content, wording, marketing, or other materials to encourage use of this product. PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/it/legalhub/paypal/home?locale.x=it_IT&_ga=2.100220126.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal User Agreement</a>.
    * You do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    > **Note:** PayPal Pay Later is not available in all markets. PayPal Pay Later eligibility and availability is subject to merchant status, sector and integration. Consumer eligibility is subject to status and approval. Product features differ by market. See relevant product terms for more details. PayPal Pay Later cross-border messaging is subject to approval by PayPal.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some sunglasses. Step 2 shows the customer choosing a payment option. In step 3, the user sees a screen that describes the payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-it-flow.png)

    **See also**

    * <a href="https://www.paypal.com/it/legalhub/paypal/acceptableuse-full?locale.x=it_IT&_ga=2.167933225.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>

  </Tab>

  <Tab title="Spain">
    Pay Later in Spain includes **Pay in 3** installments, which allows eligible buyers in Spain to spread the cost of a purchase across 3 interest-free payments for purchases of 30€-2,000€. The first payment is due at the time of the transaction, and subsequent payments are due every month.

    | Product  | Number of payments | Due     | Purchase amount |
    | -------- | ------------------ | ------- | --------------- |
    | Pay in 3 | 3                  | Monthly | 30€ to 2,000    |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-es-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in Spain if you meet all of the following requirements:

    * You're a Spain-based PayPal merchant.
    * You have a Spain-facing website.
    * You transact in euros (EUR).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/es/legalhub/paypal/acceptableuse-full?locale.x=es_ES&_ga=2.4282355.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You don't edit Pay Later messages with additional content, wording, marketing, or other materials to encourage use of this product. PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/es/legalhub/paypal/useragreement-full?_ga=2.4282355.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal User Agreement</a>.
    * You do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some sunglasses. Step 2 shows the customer choosing a payment option. In step 3, the user sees a screen that describes the payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-es-flow.png)

    **See also**

    * <a href="https://www.paypal.com/es/legalhub/paypal/acceptableuse-full?locale.x=es_ES&_ga=2.136142137.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>

  </Tab>

  <Tab title="United Kingdom">
    Pay Later in the UK includes the following two products:

    * With **Pay in 3**, eligible UK buyers can pay in 3 interest-free payments for purchases of £30 to £2,000. The first payment is due at the time of purchase, and subsequent payments are due in the following 2 months.
    * With **PayPal Credit**, eligible UK buyers receive a revolving line of credit that they can use to pay over time. PayPal Credit offers either 0% interest for 4 months on purchases over £99 or a merchant-specific Installment offers. For the 0% interest for 4 months offer, any remaining balance due after the promotional period or any transactions under £99 are charged interest at the standard variable rate. Terms and conditions apply. Representative 23.9% APR (variable). FCA credit broking permission required to advertise PayPal Credit.

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-uk-messaging.png)

    **Eligibility**

    Pay Later offers are available to UK merchants on a limited basis. To be eligible to integrate Pay Later offers in the UK, you must meet all of the following requirements:

    * You're a UK-based PayPal merchant.
    * You have a UK-facing website.
    * You transact in British pounds sterling (GBP).
    * You have a one-time payment integration.
    * You abide by the <a href="https://www.paypal.com/uk/legalhub/paypal/acceptableuse-full?locale.x=en_UK&_ga=2.59455597.1713818232.1760366701-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>.
    * You comply with the <a href="https://www.paypal.com/uk/legalhub/paypal/pay-later-messaging-tnc?_ga=2.263256268.1713818232.1760366701-1032254505.1740765755" target="_blank">Pay Later Messaging Center Program Terms</a> and the <a href="https://www.paypal.com/uk/legalhub/paypal/useragreement-full?_ga=2.263256268.1713818232.1760366701-1032254505.1740765755#receive-payment1" target="_blank">PayPal Advertiser Program Terms</a>. In particular, do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage the use of this product or remove any content. Render the Pay Later messaging in its entirety with all the links and language provided by PayPal. For noncompliant messaging, PayPal reserved the right to take action in accordance with the PayPal User Agreement.
    * You not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    PayPal Pay in 3 is an unregulated credit product. Merchant eligibility and availability is subject to merchant status, sector, and integration. Consumer eligibility is subject to status and approval.

    PayPal Pay Later Product features differ by market. See relevant product terms for more details. PayPal Pay Later cross-border messaging is subject to approval by PayPal.

    ![Image of 3 Pay Later screens on mobile apps. Step 1 shows that a Pay Later option is available for the user to buy some running shoes. Step 2 shows the customer choosing a payment option. In step 3, the user sees a screen that describes the payment schedule. The description of this step adds that PayPal handles the payment from here and that the merchant gets paid up front and in full.](assets/paypal-pay-later-uk-flow.png)

    **See also**

    * <a href="https://www.paypal.com/uk/legalhub/paypal/pay-later-messaging-tnc?_ga=2.176502445.989760939.1760545530-1032254505.1740765755" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/uk/legalhub/paypal/acceptableuse-full?locale.x=en_UK&_ga=2.163935671.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/uk/legalhub/paypal/useragreement-full?_ga=2.163935671.989760939.1760545530-1032254505.1740765755#receive-payment1" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/uk/legalhub/paypal/useragreement-full?_ga=2.163935671.989760939.1760545530-1032254505.1740765755" target="_blank">PayPal User Agreement</a>

  </Tab>

  <Tab title="Canada">
    PayPal offers special financing options that payers can use to buy now and pay later, while merchants get paid upfront. For more information about Pay Later, see <a href="https://developer.paypal.com/docs/checkout/pay-later/ca/" target="_blank">Buy now, pay later</a>.

    | Product  | Number of payments | Due                       | Purchase amount |
    | -------- | ------------------ | ------------------------- | --------------- |
    | Pay in 4 | 4                  | Every 2 weeks (Bi-weekly) | \$30 to \$1,500 |

    ![Example of Pay Later messaging on product pages.](assets/paypal-pay-later-au-messaging.png)

    **Eligibility**

    You're eligible to integrate Pay Later offers in Canada if you meet all of the following requirements:

    * Are a Canada-based PayPal merchant.
    * Have a Canada-facing website.
    * Transact in Canadian dollars (CAD).
    * Have a one-time payment integration, and Pay Later options are available through PayPal checkout.
    * Abide by the <a href="https://www.paypal.com/CA/legalhub/paypal/acceptableuse-full?locale.x=en_AU&_ga=2.266048202.491347162.1773069831-190704908.1758645993" target="_blank">Pay Later Messaging Center Program Terms</a>.
    * Do not edit Pay Later messages with additional content, wording, marketing, or other materials to encourage the use of this product or remove any content. Render the Pay Later messaging in its entirety with all the links and language provided by PayPal. For noncompliant messaging, PayPal reserves the right to take action in accordance with the <a href="https://www.paypal.com/ca/legalhub/paypal/useragreement-full?locale.x=en_AU&_ga=2.266048202.491347162.1773069831-190704908.1758645993" target="_blank">PayPal User Agreement</a>.
    * Do not create, display, or host your own Pay Later content. Instead, integrate only the official code that PayPal provides.

    **Enable Multilingual Support for Pay Later Buttons**

    To enable the **Pay in 4** button, include `buttons` and `enable-funding=paylater` when rendering buttons in your PayPal Checkout integration. You must also specify a value for the `locale` parameter.

    | Parameter | Description           | Setting        |
    | --------- | --------------------- | -------------- |
    | `locale`  | English-language site | `locale=en_CA` |
    | `locale`  | French-language site  | `locale=fr_CA` |

    > **Note:**
    >
    > * Reference Transaction and Recurring Payment integrations aren't eligible for Pay Later offers.

    **See also**

    * <a href="https://www.paypalobjects.com/crc-merchant-lifecycle/docs/CA_Pay_in_4_Messaging_Centre_Program_Terms.pdf" target="_blank">Pay Later messaging Center Program terms</a>
    * <a href="https://www.paypal.com/CA/legalhub/paypal/acceptableuse-full?locale.x=en_AU&_ga=2.237663173.491347162.1773069831-190704908.1758645993" target="_blank">PayPal Acceptable Use Policy</a>
    * <a href="https://www.paypal.com/ca/legalhub/paypal/useragreement-full#advertising-program" target="_blank">PayPal Advertising Program terms</a>
    * <a href="https://www.paypal.com/ca/legalhub/paypal/useragreement-full?locale.x=en_AU&_ga=2.237663173.491347162.1773069831-190704908.1758645993" target="_blank">PayPal User Agreement</a>

  </Tab>
</Tabs>
