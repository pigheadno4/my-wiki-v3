<!-- Source URL: https://docs.stripe.com/glossary -->
<!-- Fetched: 2026-04-20 -->

# Stripe Glossary

Learn about the terms we use.

**3D Secure (3DS)**
3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments.

**3D Secure 2 (3DS2)**
3D Secure 2 (3DS2) removes friction from the authentication process and improves the purchase experience compared to 3D Secure 1. It's the main card authentication method used to meet Strong Customer Authentication (SCA) requirements in Europe and is a key mechanism for businesses to request exemptions to SCA.

**account configuration**
Account configurations represent role-based functionality that you can enable for accounts, such as merchant, customer, or recipient.

**account ID**
When you create a Stripe account, Stripe generates a unique account ID for you. Find your account ID in the Dashboard by navigating to Profile > Accounts.

**AccountSession client secret**
The client secret is a unique string returned from Stripe as part of an AccountSession. This string lets the client access a specific Stripe account with Connect embedded components.

**ACH**
Automated Clearing House (ACH) is a US financial network used for electronic payments and money transfers that doesn't rely on paper checks, credit card networks, wire transfers, or cash.

**Adaptive acceptance**
A Stripe feature that uses AI to selectively optimize transactions in real-time.

**advanced risk factors (Radar Session disabled)**
Advanced risk factors refer to device characteristics and activity indicators that are automatically captured by Stripe.js and our SDKs.

**advanced risk factors (Radar Session enabled)**
Advanced risk factors refer to device characteristics and activity indicators that are automatically captured by Stripe.js and our SDKs. You can also capture advanced risk factors with Radar Sessions.

**AES-CBC**
Advanced Encryption Standard-Cipher Block Chaining (AES-CBC) mode is a block cipher technique that encrypts data blocks by chaining each block to the previous ciphertext block.

**AES-ECB**
Advanced Encryption Standard-Electronic Codebook (AES-ECB) mode is a simple block cipher technique where each data block is encrypted independently without chaining.

**financing package**
A financing package is a configuration on your Stripe account to set the Affirm payment option terms for your buyers.

**AFT**
Account Funding Transactions (AFT) are card-based transactions where funds are simply transferred from one account to another.

**AI model**
A system trained on data that learns patterns and performs tasks such as prediction and classification.

**approval required access**
This payment method requires approval before you can start accepting payments.

**application fee**
A fee that Connect platforms collect from connected accounts for each payment they receive.

**asynchronous**
Asynchronous refers to events happening at independent times in independent systems.

**asynchronous payment methods**
Asynchronous payment methods can take up to several days to confirm whether the payment has been successful. During this time, the payment can't be guaranteed.

**authentication rate**
The percentage of card payments where 3D Secure authentication was attempted, out of all card payments.

**authentication success rate**
The percentage of payments where 3D Secure authentication was successful, out of all 3DS requests.

**authorized person**
An individual with significant management responsibility for a business entity, such as an executive officer or senior manager. The authorized person provides business information to Stripe and claims authorization to act on behalf of the business.

**authorization rate**
The percentage of card payments approved by card issuers, out of all attempted card payments. Excludes blocked payments and payments that didn't complete 3D Secure authentication.

**Address verification system (AVS)**
The address verification system (AVS) is used to pass billing address information to issuers to verify the data if available.

**app manifest**
In a Stripe App, the app manifest is a stripe-app.json file in your app's root directory. It defines your app's ID, views, permissions, and other essential properties.

**beneficial owner**
Individuals with a threshold percentage or more equity in a business entity. The threshold percentage can range from 25% to 51%, as determined by the relevant banking partner.

**billing period**
The frequency at which invoices are generated and sent to customers. The billing period operates independently of the service period.

**BIN sponsor**
A BIN sponsor is a regulated financial institution that lets another business access its payment environment using the sponsor's Bank Identification Number (BIN).

**buy now, pay later (BNPL)**
Buy now, pay later (BNPL) allows customers to purchase a product immediately and pay for it over time—often interest free.

**capture (a charge)**
Another way to say that you receive payment for a charge is to say that you "capture" the charge. Capturing the charge is often asynchronous and takes place after authorization. The capture is what transfers the money from the customer to you.

**automatic capture**
Automatically capture funds when a charge is authorized.

**manual capture**
Manually capture funds separately from an authorization.

**card account updater**
A Stripe feature that automatically maintains up-to-date card information for your customers.

**card authentication**
A bank might require the customer to authenticate a card payment before processing. Implementation varies by bank but commonly consists of a customer entering in a security code sent to their phone.

**card issuer**
The entity that issued a payment card to a cardholder. This could be a bank, such as with the Visa or Mastercard network, or it could be the card network itself, such as with American Express.

**card network costs**
Interchange and scheme fees.

**card networks**
A network that processes the transactions of a particular card brand. It might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express.

**card networks (network cost reporting)**
Visa, Mastercard, and Discover.

**card-not-present**
A card-not-present (CNP) transaction is a purchase made remotely, without processing a physical card in a card reader, or without the cardholder manually entering a PIN. Common CNP transactions include online shopping, card-on-file payments, phone or mail orders, recurring payments, and online invoices.

**card token**
A card token replaces the cardholder's primary account number (PAN) with a series of randomly-generated numbers. It's purpose is to protect sensitive customer data.

**charge card**
A type of credit card that requires payment in full at the end of every credit period rather than allowing a minimum payment with a balance carryover.

**chargeback**
The action taken by a cardholder's bank to debit a business's account in response to a dispute from the cardholder. The debited funds are held until the dispute is resolved.

**client secret**
A client secret is used with your publishable key to authenticate a request for a single object. Each client secret is unique to the object it's associated with.

**climate product**
Products represent the different types of carbon removal units that are available for purchase.

**offtake**
Carbon removal units represent amounts of carbon that has been removed from the atmosphere and retired on behalf of the buyer.

**climate order delayed**
We consider a project to be delayed if it is unable to deliver by the original expected_delivery_year but expects to deliver within two years.

**climate order failed**
We consider a project to have have failed if it is unable to deliver within 2 years of the original expected_delivery_year.

**climate offtake agreement**
A contractual agreement to purchase carbon removal at a certain price if and when tons of carbon removal are delivered and verified.

**climate beneficiary**
The beneficiary is the entity that can claim to have removed carbon from the atmosphere.

**Stripe Checkout**
A low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website, redirect customers to a Stripe-hosted payment page, or create a customized checkout page with Stripe Elements.

**checkout session**
A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription.

**commercial volume**
Commercial volume includes transactions made to business, corporate, and purchasing cards.

**Connect**
Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients.

**connected account**
A person or business accepting payments or receiving payouts on a Connect platform.

**connected account onboarding**
Platforms onboard connected accounts to a Stripe account using a hosted onboarding flow, an embedded onboarding flow, or a custom onboarding flow that they build using the API.

**ConfirmationTokens**
ConfirmationTokens help capture data from your client, such as your customer's payment instruments and shipping address, and are used to confirm a PaymentIntent or SetupIntent.

**conversion on-session**
A payment is described as on-session if it occurs with the direct involvement of the customer. Off-session transactions rely on previously-collected payment information.

**Cross-Origin Isolation**
Cross-origin isolation is an opt-in security feature that helps prevent side-channel attacks by ensuring that a document loads in a unique, isolated browsing environment.

**Content Security Policy**
Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross-Site Scripting (XSS) and data injection attacks.

**Customers**
Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments.

**customer portal**
The customer portal is a secure, Stripe-hosted page that lets your customers manage their subscriptions and billing details.

**Card verification code check (CVC)**
The card verification code (CVC) or card verification value (CVV) is a three- or four-digit number printed directly on a card used to verify the entered card number.

**dashboard access**
Platforms can provide connected accounts with access to the full Stripe Dashboard or the Express Dashboard. Otherwise, platforms build an interface for connected accounts using embedded components or the Stripe API.

**debounce**
A programming technique that limits the rate at which events are processed, by ignoring all but the first (or the last) event that occurred in close succession.

**define products inline**
Instead of creating Products and Prices upfront, you can define them inline as part of the Order by passing the line_items.product_data and line_items.price_data parameters.

**delayed notification payment method**
A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods.

**deprecated**
Technology that's no longer recommended and that might stop working after a specific date.

**destination charge**
A charge type where customers transact with your platform for products or services provided by a connected account. Your platform pays Stripe fees and immediately transfers funds to the connected account with each payment.

**digital wallet**
A digital wallet is a contactless payment method that stores payment options, such as credit and debit cards, allowing customers to use a smart device to make a purchase.

**direct charge**
A charge type where customers transact directly with a connected account, which is always the merchant of record. With each payment, the connected account pays fees to Stripe and, optionally, to your platform.

**direct to authorization**
Where Stripe requests an SCA exemption as part of the authorization message.

**dispute inquiry**
A pre-dispute request from a card issuer, asking for information about a charge. Based on the response from the business, an inquiry might or might not escalate to a full chargeback. Inquiries are sometimes called "retrievals" or "requests for information."

**dunning email**
A dunning email helps prevent lost revenue by asking a customer to update their payment method. You can define the schedule to send these payment reminder emails in your Subscriptions and email settings.

**European Economic Area**
The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association.

**effective rate**
Effective rate is equal to network costs divided by total processing volume.

**Stripe Elements**
A set of UI components for building a web checkout flow. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server.

**Electronic Commerce Indicator (ECI)**
An Electronic Commerce Indicator (ECI) is a code returned alongside a 3D Secure authentication result. It indicates the authentication method and result and may be used subsequently to, for example, determine eligibility for liability shift.

**e-mandate**
An e-mandate is a form of authorization provided by cardholders to issuing banks that grants permission for recurring payments on their card. Any recurring payment arrangements (for example, monthly subscriptions to OTT services) need an associated e-mandate to be successful. The e-mandate needs to be registered and then validated through AFA, such as 3DS.

**EMV**
EMV refers to the standards governing acceptance of chip-enabled cards and some contactless payment methods. Today most payment cards issued around the world support EMV.

**entitlement**
An entitlement represents a feature that a customer is "entitled" to.

**event destination**
A tool to send events to your application via webhook or directly to your cloud infrastructure.

**exclusive tax**
Exclusive tax is tax that changes the final purchase price—the listed price the buyer sees doesn't include it, and it's added to the total. An example of exclusive tax is US sales tax.

**exposure limit**
The exposure limit is the maximum aggregate amount that can be spent beyond pre-funded balances.

**FCA**
A Financial Connections Account is an API object that represents an external financial account (such as a checking or credit card account) that your customer has linked to your application using the Stripe Financial Connections product.

**FDIC**
Federal Deposit Insurance Corporation (FDIC) is an independent agency created by Congress to insure deposits, regulate financial institutions, make large and complex financial institutions resolvable, and manage receiverships.

**feature**
A feature represents a monetizable ability or functionality in your system. Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.

**first-class fields**
First-class fields are prominent input fields that appear at the top level of the payment form and API, rather than being grouped within other sections such as billing or shipping details.

**fiscal representation**
Fiscal representation is a process where a local entity acts as a representative of a foreign business for VAT purposes, usually in countries where they must register for VAT but can't do so independently.

**fixed and variable portion**
For example, if the interchange plan is 2.04% + $0.10, 2.04% is the variable portion, and $0.10 is the fixed portion.

**FSA/HSA**
Flexible Spending Account or Health Savings Account debit cards use pre-tax funds to cover certain types of purchases, such as medical expenses. Their use is restricted only to businesses that directly provide eligible products and services.

**fulfillment**
Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected.

**General Data Protection Regulation**
GDPR is a regulation in EU law on data protection and privacy in the European (EU) and the European Economic Area (EEA).

**gross sales**
Gross sales refers to the total number of sales over a period of time including sales for resale, taxable and exempt sales.

**GST**
A goods and services tax (GST), known in some countries as a value added tax (VAT), is a type of tax levied on the price of a product or service at each stage of production, distribution, or sale to the end consumer. GST and VAT are also generally known as "consumption" taxes. The buyer pays the tax and the seller forwards it to the government.

**hard decline code**
A hard decline code means the issuing bank has rejected the transaction and you can't retry it.

**HST**
In many Canadian provinces the Goods and Services Tax (levied by the country) is merged with the Provincial Sales Tax (levied by the province) and is called Harmonized Sales Tax (HST).

**IBAN**
The International Bank Account Number (IBAN) identifies bank accounts across national borders to facilitate cross border transactions with a reduced risk of transcription errors. An IBAN uniquely identifies the account of a customer at a financial institution.

**IC+**
A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs.

**iDEAL**
iDEAL is a payment method in the Netherlands that uses direct, online transfers from the user's bank account.

**immediate confirmation timing**
This payment method immediately returns a payment status when a customer attempts a transaction. A status of "succeeded" on the PaymentIntent guarantees that you receive the funds from your customers.

**inclusive tax**
Inclusive tax is tax that doesn't change the final purchase price—the price the buyer sees already includes it. Examples of inclusive tax include VAT and GST outside of the US.

**incremental onboarding**
Incremental onboarding is a type of onboarding where you gradually collect required verification information from your users. You collect a minimum amount of information at sign-up, and you collect more information as the connected account earns more revenue.

**indirect charge**
A charge type where customers transact directly with your platform instead of with a connected account. Indirect charges include destination charges and separate charges and transfers.

**instant access**
Instant access allows you start accepting payments with this payment method immediately.

**instant provisional access**
Instant provisional access allows you start accepting payments with this payment method immediately, but payment method eligibility is subject to review after the first transaction.

**confirm (PaymentIntent)**
Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment.

**confirm (intent)**
Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects.

**IV**
The initialization vector (IV) is a cryptographically-secure generated random value that enhances encryption security and ensures that unique ciphertexts are produced for the same message.

**PaymentIntent client secret**
The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer).

**interchange fee**
Interchange or interchange fee is a term used by the card networks to describe a fee paid between banks for the acceptance of card-based transactions. Usually it's a fee on transactions that a business's bank (the "acquiring bank") pays a customer's bank (the "issuing bank").

**invoices**
Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice.

**know your customer**
Know your customer (KYC) regulations require that professionals and businesses make an effort to verify the identity, suitability, and risks involved with maintaining a business relationship. The procedures fall under the broader scope of anti-money laundering (AML) policy.

**legacy**
Technology that's no longer recommended.

**Legacy Checkout**
A modal dialog to collect card details.

**liability shift**
With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer.

**Link**
Stripe's digital wallet. It securely saves and autofills customer address and payment details, with support for cards, US bank accounts, BNPLs, and more.

**local payment methods**
Payment methods used in specific countries or regions, such as bank transfers, vouchers, and digital wallets. Examples include Pix (Brazil, bank transfers), Konbini (Japan, vouchers), and WeChat Pay (China, digital wallet).

**live mode**
Use this mode when you're ready to launch your app. Card networks or payment providers process payments.

**mandate**
A written notice of authorization to debit a bank account, agreed to by the customer before the first debit.

**marketplace**
A Connect platform that provides a platform-branded storefront for products and services from its connected accounts.

**MCC**
A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers.

**merchant-initiated transaction**
A payment made off-session with a properly authenticated saved card, can qualify as merchant-initiated transaction and be exempt from SCA.

**merchant of record**
The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account.

**metered billing**
Metered billing is a subscription billing model where you charge your customers based on their consumption of your service during the billing cycle, instead of explicitly setting quantities.

**minor currency unit**
The Stripe API expects currency values using the given denomination's smallest unit represented without decimals. For example, enter 1099 to charge 10.99 USD (or any other two-decimal currency). Enter 10 to charge 10 JPY (or any other zero-decimal currency).

**Mobile Elements**
A set of UI components for building mobile checkout flows. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server.

**MRR**
Monthly Recurring Revenue, the total predictable monthly revenue from subscriptions.

**multi-currency price**
A single Price object can support multiple currencies. Each purchase uses one of the supported currencies for the Price, depending on how you use the Price in your integration.

**Nacha**
Nacha is the governing body that oversees the ACH network.

**negative balance liability**
The responsibility for managing risk and recovering negative balances on connected accounts. Stripe or the Connect platform can be liable for negative balances on connected accounts.

**NSF**
A shorthand way of referring to the Non-sufficient Funds ACH return code R01.

**Offline PIN**
Offline PIN is a card verification method for EMV chip cards. These cards store the PIN securely on the chip itself, so PIN verification can occur without a network connection.

**off-session payment**
A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information.

**on_behalf_of**
A parameter that allows a Connect platform to create an indirect payment where the connected account is the merchant of record (MoR).

**on-demand payment**
When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app.

**Online PIN**
Online PIN is a card verification method for EMV chip cards. These cards require the terminal to contact the issuer over a network connection to verify the PIN.

**on-session payment**
A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method.

**open loop wallet**
An account with a monetary value that can be funded through payments or transfers and used to make purchases within or outside of a platform.

**submit (order)**
Submitting an order indicates that the customer intends to pay. Upon submission, the order can no longer be updated and is ready for payment.

**originating event**
The activity that triggers a subsequent action, such as the application of a network cost.

**partial refund**
A partial refund is any refund in which less than the remaining refundable amount is refunded in a single request. The remaining refundable amount is the payment_intent.amount_received - charge.amount_refunded.

**paydown**
A paydown is an automatic or manual payment toward a financing balance.

**PaymentIntent**
API object that represents your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

**Payment Intents API**
The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods.

**Payment Links**
A link to a secure, hosted payment page that you can generate without code. Share it directly with your customers, or point them to it with a button or QR code.

**PaymentMethods**
PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs.

**Payment Method Provider (PMP)**
A Payment Method Provider integrates with Stripe so that businesses can support the payment method using Stripe.

**payment rails**
A financial network that provides the technological infrastructure to electronically move money from a payer to a payee.

**payout**
A payout is the transfer of funds to an external account, usually a bank account, in the form of a deposit.

**standard payout**
Funds are paid out according to your account's configured schedule. The timing follows the normal T+X day schedule for your country. In most countries, standard payout timing is T+2 business days, meaning funds from a transaction become available for payout approximately 2 business days after the transaction is captured. However, this varies by country.

**T+2 payout**
Your payout timing is T+2 business days, meaning funds from a transaction become available for payout approximately 2 business days after the transaction is captured.

**T+3 payout**
Your payout timing is T+3 business days, meaning funds from a transaction become available for payout approximately 3 business days after the transaction is captured.

**T+4 payout**
Your payout timing is T+4 business days, meaning funds from a transaction become available for payout approximately 4 business days after the transaction is captured.

**T+5 payout**
Your payout timing is T+5 business days, meaning funds from a transaction become available for payout approximately 5 business days after the transaction is captured.

**PCI compliance**
Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business.

**Personally identifiable information**
Personally identifiable information (PII) is information that, when used alone or with other relevant data, can identify an individual. Examples include passport numbers, driver's license, mailing address, or credit card information.

**PIX**
PIX is an instant payment platform created and managed by the Central Bank of Brazil.

**post-fund**
Post-funding is the ability to use Stripe Credit to fund Issuing card spend after it's accrued, rather than by pre-funding.

**presentment currency**
The presentment currency is the currency the customer uses to make a payment.

**Prices**
Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions.

**pricing model**
The pricing model consists of the products or services you sell, how much they cost, what currency you accept for payments, and the service period to charge (for subscriptions). To build the pricing model, you use Products—what you sell—and Prices—how much and how often to charge for your products.

**pricing table**
A pricing table is an embeddable UI that displays different pricing levels for your subscription, and then takes your customers to a prebuilt checkout flow to complete their purchase.

**private app**
A private app is only available to users who have access to your Stripe account. Stripe users can't discover private apps on the Stripe App Marketplace.

**Products**
Products represent what your business sells—whether that's a good or a service.

**Product Categories**
Product Categories describe a hierarchy of categories of products you offer to your customers. For example, you might have a category for Clothes, and under that a category for Mens' Shirts.

**Product Classes**
Product Classes describe the classes of products you offer to your customers. For example you might offer t-shirts that vary by size and color. Each specific combination of t-shirt size and color would be a Product. The grouping of all t-shirt size and color combinations would be a Product Class.

**subscription products**
Products represent items your customer can subscribe to with a Subscription. An associated Price object describes the pricing and other terms of the subscription.

**PST**
A Provincial Sales Tax (PST) is a type of tax imposed on consumers and levied by provinces in several Canadian provinces.

**public app**
A public app is discoverable on the Stripe App Marketplace.

**QST**
The province-specific sales tax in Quebec is called Quebec Sales Tax (QST).

**Quick Chip EMV**
Quick Chip is a contact EMV transaction process, designed to expedite transaction times and allows the removal of the card before the transaction response is validated against the chip, through the second generate application cryptogram. This is only available in the US through most major card networks.

**Radar**
Stripe Radar helps detect and block fraud for any type of business using machine learning that trains on data across millions of global companies. It's built into Stripe and requires no additional setup to get started.

**Radar client risk factors**
Client risk factors refer to information such as IP address, User-Agent, and checkout URL that are used to help enhance fraud prevention.

**Radar customer risk factors**
Customer risk factors refer to information such as user email, name, and billing address that are passed through the customer object in the API.

**Radar for Fraud Teams**
Radar for Fraud Teams helps you fine-tune how Radar operates, get fraud insights on suspicious charges, and assess your fraud management performance from a unified dashboard.

**Radar Plus**
Radar Plus helps you fine-tune how Radar operates, get fraud insights on suspicious charges, and assess your fraud management performance from a unified dashboard.

**Recall**
Customer-originated attempt to undo a previously sent EUR bank transfer payment (SEPA Credit Transfer). Recipients can freely accept or reject the recall.

**referrer model**
A Connect business model where the platform refers its connected accounts to process payments through Stripe and might qualify for revenue share on the Stripe fees paid by those accounts.

**requires_action**
This status appears as "requires_source_action" in API versions before 2019-02-11.

**requires_payment_method**
This status appears as "requires_source" in API versions before 2019-02-11.

**reseller model**
A Connect business model where the platform purchases Stripe products and services to resell to its connected accounts.

**retail sales**
For tax purposes, retail sales don't include sales of resale goods.

**requirement collection**
The responsibility for collecting required information from connected accounts to keep their Stripe accounts active. Stripe or the Connect platform can be responsible for requirement collection.

**reusable**
Reusable payment methods can be saved to a customer for future payments. After the initial setup, customers don't need to re-enter their payment details for subsequent transactions.

**reversal**
A reversal is the cancellation of a transaction. Stripe doesn't withhold any fees for payment reversals.

**reverse_charge_mechanism**
A reverse charge is a transaction where the responsibility for calculating and remitting tax shifts from the seller to the buyer.

**RST**
The Retail Sales Tax (RST) is a tax imposed by the Canadian province of Manitoba to the retail sale of goods and services.

**SaaS platform**
A Software as a Service (SaaS) Connect platform that provides Stripe products and services to its connected accounts.

**sandbox**
A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes.

**Strong Customer Authentication**
Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase.

**SCA exemptions**
Some transactions that are deemed low risk, based on the volume of fraud rates associated with the payment provider or bank, may be exempt from Europe's Strong Customer Authentication requirements.

**scoped grant**
Shared Payment Tokens are restricted to a single merchant with usage limits and expiration.

**secret key**
Stripe APIs use your secret API key to authenticate requests from your server; you can use this key to make any API call on behalf of your account, such as creating a charge or performing a refund.

**Single Euro Payments Area**
Single Euro Payments Area (SEPA) is a payment-integration initiative to simplify bank transfers involving euros. Several dozen countries comprise SEPA. Most of the participating countries are in the European Union and have euro-based economies, but this is not a requirement.

**separate charges and transfers**
A charge type where customers transact with your platform for products or services provided by one or more connected accounts. With each payment, your platform pays Stripe fees and transfers funds to connected accounts as separate transactions.

**service interval**
The timeframe used to measure usage and apply pricing. The service interval resets independently of the billing cadence.

**service period**
The timeframe used to measure usage and apply pricing. The service period resets independently of the billing period.

**settle**
When funds are available in your Stripe balance.

**settlement timing**
The amount of time it takes for a settlement to occur.

**settlement currency**
The settlement currency is the currency your bank account uses.

**Setup Intents API**
The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method.

**SetupIntent client secret**
The client secret is a unique key returned from Stripe as part of a SetupIntent. This key lets the client access important fields from the SetupIntent (for example, status).

**single use**
Single-use payment methods can only be used once for a payment. You can't save them for future transactions. After they're used in a payment attempt, you can't reuse them or attach them to customers.

**SKU**
SKUs (Stock Keeping Units) represent a specific Product variation, taking into account any combination of attributes and cost (for instance, size, color, currency, cost).

**soft decline**
A soft decline occurs when an issuing bank declines an authorization request with a decline code of "authentication required."

**soft decline code**
A soft decline code means the issuing bank has rejected the transaction, but you can retry it.

**stablecoin**
A cryptocurrency that's pegged to the value of a fiat currency or other asset in order to limit volatility.

**Standard EMV**
Standard EMV, or Full EMV flow, is a contact EMV transaction process that requires the card to remain inserted throughout the online authorization, with the transaction only being captured after the EMV chip validates the authorization and provides a second application cryptogram. If this validation fails, the transaction is reversed.

**stored-value account**
An account that can store funds. The funds are typically transferred in from an external bank account.

**Stripe app**
An app that you can build on top of Stripe to customize the functionality of the Stripe Dashboard UI, leverage Stripe user data, store data on Stripe, and more.

**Stripe App Marketplace**
A marketplace to browse, search, and install Stripe apps.

**Stripe fee collection**
In a Connect implementation, Stripe collects Stripe fees either from the platform account or from the platform's connected accounts.

**Stripe.js**
Use Stripe.js' APIs to tokenize customer information, collect sensitive card data, and accept payments with browser payment APIs.

**subscriptions**
A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis.

**tax code**
A tax code is the category of your product for tax purposes.

**tax behavior**
Tax behavior determines whether you want to include taxes in the price ("inclusive") or add them on top ("exclusive").

**tax liability**
The responsibility for collecting and reporting taxes for transactions in a Connect integration. It can belong to the platform or to connected accounts, depending on your business model, government regulations, and individual transaction details.

**team member**
A team member is a user with controlled access to some features of your Stripe account, like an administrator, developer, or support specialist.

**test mode**
Test mode is another way to test changes to your integration without affecting production. A sandbox is the default and recommended way to test integrations. All Stripe features are available in test mode but you can't create live charges unless you're in live mode.

**test mode sandbox**
Every Stripe account includes the test mode sandbox. It shares some settings with live mode, has characteristics that differ from other sandboxes you create, but you can't delete it.

**test helper**
Test helpers are test-only API endpoints that allow you to simulate actions that happen outside of Stripe's API, like funding balances or advancing time.

**TLS**
TLS refers to the process of securely transmitting data between the client—the app or browser that your customer is using—and your server. This was originally performed using the SSL (Secure Sockets Layer) protocol.

**TLV**
TLV (sometimes called BER-TLV) stands for basic encoding rules-tag length value, and is a data encoding scheme used in payment processing systems.

**top up**
The act of adding funds to a Stripe account, typically through a transfer from a bank external to Stripe.

**TR 31 KeyBlock**
TR-31 key blocks are standardized data structures that securely encapsulate cryptographic keys, enabling their reliable exchange and management across diverse systems and applications. They consist of a header, key component, and optional additional information such as key usage, expiration, and other metadata.

**Track 2**
Track 2 data is a numerical format that contains information necessary for processing in-person card transactions. The data consists of the primary account number (PAN) and the card expiration date, along with issuer specific data.

**Treasury**
A collection of API endpoints and cloud- and web-based features that enable platforms to offer embedded financial solutions to their users.

**2FA**
Two-factor authentication (2FA), also known as two-step verification, is a security process that requires users to provide two different authentication factors to verify their identity.

**ui extension**
A set of APIs that allow you to inject user interface elements into the Stripe Dashboard using TypeScript and React.

**usage-based billing**
A pricing model that lets you charge customers based on their usage of your product or service in a billing period.

**VAT**
A value-added tax (VAT), known in some countries as a goods and services tax (GST), is a type of tax levied on the price of a product or service at each stage of production, distribution, or sale to the end consumer. VAT and GST are also generally known as "consumption" taxes. The buyer pays the tax and the seller forwards it to the government.

**view**
A view is a React component that creates UI extensions in the Stripe Dashboard.

**viewport**
A viewport specifies the page in the Dashboard where your view can appear.

**virtualization**
Virtualization is a technique that allows a payment method to be used outside of Stripe by generating a token that can be used to process payments.

**UCC-1**
A publicly available notice filed by a creditor that secures the creditor's interest in certain assets of a debtor. Creditors file UCC-1 statements with the secretary of state where a business debtor is incorporated at the time a loan first originates.

**Universal links**
Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app.

**upfront onboarding**
Upfront onboarding is a type of onboarding where you collect all required verification information from your users at sign-up.

**upsert**
A combined operation that updates an existing record if it exists or inserts it if it doesn't.

**webhook**
A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests.

**wire transfer**
Also called a bank transfer or credit transfer, wire transfers are a method of electronic funds transfers that move money from a payer to a payee.

**XLIFF file**
XLIFF (XML Localization Interchange File Format) is a standardized format used to store and transfer localizable content between different translation and localization systems.
