<!-- Source URL: https://docs.stripe.com/payments/bancontact/set-up-payment -->
<!-- Fetched: 2026-05-03 -->

# Use Bancontact to set up future SEPA Direct Debit payments

Learn how to save bank details from a Bancontact payment and charge your customers later with SEPA Direct Debit.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

> We recommend that you follow the [Set up future payments](https://docs.stripe.com/payments/save-and-reuse.md) guide. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Bancontact is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) each payment. With this integration, Stripe charges your customer 0.02 EUR through Bancontact to collect their bank details. After your customer authenticates the payment, Stripe refunds the payment and stores your customer’s [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) in a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) payment method. You can then use the SEPA Direct Debit [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) to [accept payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md) or [set up a subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit.md). If you want to save IBAN details when you accept a payment, see [Save bank details during payment](https://docs.stripe.com/payments/bancontact/save-during-payment.md).

> #### Activate SEPA Direct Debit
>
> To use Bancontact to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the [Dashboard](https://dashboard.stripe.com/account/payments/settings). You must also comply with the [Bancontact Terms of Service](https://stripe.com/bancontact/legal) and [SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal).

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/bancontact/set-up-payment?payment-ui=checkout.

You can use [Checkout in setup mode](https://docs.stripe.com/payments/save-and-reuse.md?platform=checkout) to collect payment details and set up future SEPA Direct Debit payments using Bancontact.

## Create or retrieve a Customer [Server-side]

To set up future SEPA Direct Debit payments using Bancontact, you must attach the SEPA Direct Debit payment method to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a `Customer` object when your customer creates an account with your business. You can retrieve and use a customer’s stored payment method details later if you associate the ID of the `Customer` object with your own internal representation of the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Set up future payments

This guide builds on the foundational [set up future payments](https://docs.stripe.com/payments/save-and-reuse.md?platform=checkout) Checkout integration and shows the differences between using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) and manually configuring payment methods.

### Enable Bancontact as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to add `bancontact` to the list of `payment_method_types`.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  mode: "setup",
  payment_method_types: ["card", "bancontact"],
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  mode: "setup",
  payment_method_types: ["card", "bancontact"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

## Charge the SEPA Direct Debit PaymentMethod later [Server-side]

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

When testing your Checkout integration, select Bancontact as the payment method and click the **Pay** button.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/bancontact/set-up-payment?payment-ui=direct-api.

Setting up future SEPA Direct Debit payments using Bancontact in your app consists of creating a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to track the process, collecting mandate acknowledgement, and redirecting your customer to Bancontact. Stripe uses the SetupIntent to track and handle all the states of the setup until the setup completes.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments and tracks the steps of this setup process. For Bancontact, this includes collecting a [SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate) from the customer and tracking its validity. Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["bancontact"],
  customer: "{{CUSTOMER_ID}}",
});
```

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a SetupIntent. This key lets the client access important fields from the SetupIntent (for example, status)), which is used on the client side to securely complete the setup process instead of passing the entire SetupIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

Create a form on your client to collect the required billing details from the customer.

#### HTML + JS

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method creates the accepted mandate. As the customer has implicitly signed the mandate when accepting these terms, you must communicate these terms in your form or through email.

| Field   | Value                                           |
| ------- | ----------------------------------------------- |
| `name`  | The full name (first and last) of the customer. |
| `email` | The customer’s email.                           |

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name"> Name </label>
    <input id="name" name="name" required />
  </div>

  <div class="form-row">
    <label for="email"> Email </label>
    <input id="email" name="email" required />
  </div>

  <button id="submit-button">Submit</button>

  <!-- Display mandate acceptance text. -->
  <div id="mandate-acceptance">
    By providing your payment information and confirming this payment, you
    authorise (A) Rocketship Inc and Stripe, our payment service provider, to
    send instructions to your bank to debit your account and (B) your bank to
    debit your account in accordance with those instructions. As part of your
    rights, you are entitled to a refund from your bank under the terms and
    conditions of your agreement with your bank. A refund must be claimed within
    8 weeks starting from the date on which your account was debited. Your
    rights are explained in a statement that you can obtain from your bank. You
    agree to receive notifications for future debits up to 2 days before they
    occur.
  </div>
  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>
```

#### React

#### npm

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

#### umd

We also provide a UMD build for sites that don’t use npm or modules.

Include the Stripe.js script, which exports a global `Stripe` function, and the UMD build of React Stripe.js, which exports a global `ReactStripe` object. Always load the Stripe.js script directly from **js.stripe.com** to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<!-- Stripe.js -->
<script src="https://js.stripe.com/dahlia/stripe.js"></script>

<!-- React Stripe.js development build -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.js"></script>

<!-- When you are ready to deploy your site to production, remove the
      above development script, and include the following production build. -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.min.js"></script>
```

> The [demo in CodeSandbox](https://codesandbox.io/s/react-stripe-official-q1loc?fontsize=14&hidenavigation=1&theme=dark) lets you try out React Stripe.js without having to create a new project.

### Add Stripe.js and Elements to your page

To use Element components, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key and pass the returned `Promise` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

## Submit the payment method details to Stripe [Client-side]

Rather than sending the entire SetupIntent object to the client, use its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret). This is different from your API keys that authenticate Stripe API requests. The client secret should be handled carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

Use [stripe.confirmBancontactSetup](https://docs.stripe.com/js/setup_intents/confirm_bancontact_setup) to complete the setup when the customer submits the form. Include the customer’s name and email address in `billing_details`.

The SetupIntent’s `status` is `succeeded` if the setup is successful. If the setup isn’t successful, inspect the returned `error` to determine the cause. As the SetupIntent was created with a [Customer](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer), the PaymentMethod is attached to the Customer. This enables you to use the payment method to collect future payments without prompting the customer for payment method details again.

```javascript
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
var accountholderName = document.getElementById("name");
var accountholderEmail = document.getElementById("email");

// Redirects away from the client
const { error } = await stripe.confirmBancontactSetup(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    payment_method: {
      billing_details: {
        name: accountholderName.value,
        email: accountholderEmail.value,
      },
    },
    return_url: "https://example.com/checkout/complete",
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

The `return_url` should correspond to a page on your website that displays the result of the setup. You can determine what to display by verifying the status of the `SetupIntent`. When Stripe redirects the customer to the `return_url`, the following URL query parameters are provided to verify status. You can also append your own query parameters to the `return_url`. They persist throughout the redirect process.

| Parameter                    | Description                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `setup_intent`               | The unique identifier for the `SetupIntent`                                                                                            |
| `setup_intent_client_secret` | The [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) of the `SetupIntent` object |

#### React

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

Use [stripe.confirmBancontactSetup](https://docs.stripe.com/js/setup_intents/confirm_bancontact_setup) to handle the redirect away from your page and to complete the setup. Add a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the setup on their bank’s website or mobile application.

To call `stripe.confirmBancontactSetup` from your setup form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import { useStripe, useElements } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const accountholderEmail = event.target["accountholder-email"];

    const { error } = await stripe.confirmBancontactSetup("{CLIENT_SECRET}", {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
          email: accountholderEmail.value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the setup with their bank.
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-row">
        <label>
          Name
          <input name="accountholder-name" placeholder="Jenny Rosen" required />
        </label>
      </div>
      <div className="form-row">
        <label>
          Email
          <input
            name="accountholder-email"
            placeholder="jenny.rosen@example.com"
            required
          />
        </label>
      </div>
      <button type="submit" disabled={!stripe}>
        Submit
      </button>
      {/* Display mandate acceptance text. */}
      <div id="mandate-acceptance">
        By providing your payment information and confirming this payment, you
        authorise (A) Rocket Rides and Stripe, our payment service provider, to
        send instructions to your bank to debit your account and (B) your bank
        to debit your account in accordance with those instructions. As part of
        your rights, you are entitled to a refund from your bank under the terms
        and conditions of your agreement with your bank. A refund must be
        claimed within 8 weeks starting from the date on which your account was
        debited. Your rights are explained in a statement that you can obtain
        from your bank. You agree to receive notifications for future debits up
        to 2 days before they occur.
      </div>
    </form>
  );
}
```

#### Class Components

```jsx
import React from "react";
import { ElementsConsumer } from "@stripe/react-stripe-js";

class CheckoutForm extends React.Component {
  handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    const { stripe, elements } = this.props;

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make  sure to disable form submission until Stripe.js has loaded.
      return;
    }

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const accountholderEmail = event.target["accountholder-email"];

    const { error } = await stripe.confirmBancontactSetup("{CLIENT_SECRET}", {
      payment_method: {
        billing_details: {
          name: accountholderName.value,
          email: accountholderEmail.value,
        },
      },
      return_url: "https://example.com/checkout/complete",
    });

    if (error) {
      // Show error to your customer.
      console.log(error.message);
    }

    // Otherwise the customer will be redirected away from your
    // page to complete the setup with their bank.
  };

  render() {
    const { stripe } = this.props;

    return (
      <form onSubmit={this.handleSubmit}>
        <div className="form-row">
          <label>
            Name
            <input
              name="accountholder-name"
              placeholder="Jenny Rosen"
              required
            />
          </label>
        </div>
        <div className="form-row">
          <label>
            Email
            <input
              name="accountholder-email"
              placeholder="jenny.rosen@example.com"
              required
            />
          </label>
        </div>
        <button type="submit" disabled={!stripe}>
          Submit
        </button>
        {/* Display mandate acceptance text. */}
        <div id="mandate-acceptance">
          By providing your payment information and confirming this payment, you
          authorise (A) Rocketship Inc and Stripe, our payment service provider,
          to send instructions to your bank to debit your account and (B) your
          bank to debit your account in accordance with those instructions. As
          part of your rights, you are entitled to a refund from your bank under
          the terms and conditions of your agreement with your bank. A refund
          must be claimed within 8 weeks starting from the date on which your
          account was debited. Your rights are explained in a statement that you
          can obtain from your bank. You agree to receive notifications for
          future debits up to 2 days before they occur.
        </div>
      </form>
    );
  }
}

export default function InjectedCheckoutForm() {
  return (
    <ElementsConsumer>
      {({ stripe, elements }) => (
        <CheckoutForm stripe={stripe} elements={elements} />
      )}
    </ElementsConsumer>
  );
}
```

## Charge the SEPA Direct Debit PaymentMethod later [Server-side]

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method                                                       | Description                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_bancontact_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_bancontact_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_bancontact_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_bancontact_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-setup events

Stripe sends a [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) event when the SetupIntent completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like saving the generated SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) to your database or charging your customer after a trial period.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/bancontact/set-up-payment?payment-ui=mobile&platform=ios.

Setting up future SEPA Direct Debit payments using Bancontact in your app consists of creating a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to track the process, collecting mandate acknowledgement, and redirecting your customer to Bancontact. Stripe uses the SetupIntent to track and handle all the states of the setup until the setup completes.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments and tracks the steps of this setup process. For Bancontact, this includes collecting a [SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate) from the customer and tracking its validity. Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["bancontact"],
  customer: "{{CUSTOMER_ID}}",
});
```

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a SetupIntent. This key lets the client access important fields from the SetupIntent (for example, status)), which is used on the client side to securely complete the setup process instead of passing the entire SetupIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address. Create an [STPPaymentMethodParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentMethodParams.html) object with these details.

#### Swift

```swift
let bancontactParams = STPPaymentMethodBancontactParams()

let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
billingDetails.email = "jane.doe@example.com"

let paymentMethodParams = STPPaymentMethodParams(bancontact: bancontactParams,
                                                 billingDetails: billingDetails,
                                                 metadata: nil)
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method creates the accepted mandate. As the customer has implicitly signed the mandate when accepting these terms, you must communicate these terms in your form or through email.

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>) to present a webview where the customer can complete the payment on their bank’s website or app. Handle the payment result in the completion block.

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: paymentIntentClientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams

STPPaymentHandler.shared().confirmSetupIntent(withParams: setupIntentParams, authenticationContext: self) { (handlerStatus, setupIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Setup succeeded

    case .canceled:
        // Setup was canceled

    case .failed:
        // Setup failed

    @unknown default:
        fatalError()
    }
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method                                                       | Description                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_bancontact_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_bancontact_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_bancontact_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_bancontact_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/bancontact/set-up-payment?payment-ui=mobile&platform=android.

Setting up future SEPA Direct Debit payments using Bancontact in your app consists of creating a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to track the process, collecting mandate acknowledgement, and redirecting your customer to Bancontact. Stripe uses the SetupIntent to track and handle all the states of the setup until the setup completes.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.5.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.5.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create or retrieve a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments and tracks the steps of this setup process. For Bancontact, this includes collecting a [SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate) from the customer and tracking its validity. Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["bancontact"],
  customer: "{{CUSTOMER_ID}}",
});
```

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a SetupIntent. This key lets the client access important fields from the SetupIntent (for example, status)), which is used on the client side to securely complete the setup process instead of passing the entire SetupIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address. Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) object with these details.

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(name = "Jenny Rosen", email = "jenny.rosen@example.com")
val paymentMethodCreateParams = PaymentMethodCreateParams.createBancontact(billingDetails)
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method creates the accepted mandate. As the customer has implicitly signed the mandate when accepting these terms, you must communicate these terms in your form or through email.

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690) to present a webview where the customer can complete the setup on their bank’s website or app. Handle the payment result in `onActivityResult`.

#### Kotlin

```kotlin
class BancontactSetupActivity : AppCompatActivity() {
    // ...
    private lateinit var setupIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.Companion.create(
            this,
            PaymentConfiguration.getInstance(applicationContext).publishableKey,
            PaymentConfiguration.getInstance(applicationContext).stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmSetupIntentParams
                .create(
                  paymentMethodCreateParams = paymentMethodCreateParams,
                  clientSecret = setupIntentClientSecret
                )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        val message = when (paymentResult) {
            is PaymentResult.Completed -> {
                "Completed!"
            }
            is PaymentResult.Canceled -> {
                "Canceled!"
            }
            is PaymentResult.Failed -> {
                // This string comes from the PaymentIntent's error message.
                // See here: https://stripe.com/docs/api/payment_intents/object#payment_intent_object-last_payment_error-message
                "Failed: " + paymentResult.throwable.message
            }
        }
    }
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method                                                       | Description                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_bancontact_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_bancontact_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_bancontact_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_bancontact_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-payment events

Stripe sends a [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) event when the SetupIntent completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like saving the generated SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) to your database or charging your customer after a trial period.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/bancontact/set-up-payment?payment-ui=mobile&platform=react-native.

Setting up future SEPA Direct Debit payments using Bancontact in your app consists of creating a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) to track the process, collecting mandate acknowledgement, and redirecting your customer to Bancontact. Stripe uses the SetupIntent to track and handle all the states of the setup until the setup completes.

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a Customer [Server-side]

Create a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) when they create an account with your business and associate it with your internal representation of their account. This enables you to retrieve and use their saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments and tracks the steps of this setup process. For Bancontact, this includes collecting a [SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate) from the customer and tracking its validity. Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) [ID](https://docs.stripe.com/api/customers/object.md#customer_object-id).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["bancontact"],
  customer: "{{CUSTOMER_ID}}",
});
```

The SetupIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a SetupIntent. This key lets the client access important fields from the SetupIntent (for example, status)), which is used on the client side to securely complete the setup process instead of passing the entire SetupIntent object.

## Collect payment method details and mandate acknowledgement [Client-side]

In your app, collect your customer’s full name and email address.

```javascript
export default function BancontactPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmai] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="Email"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

​​To process SEPA Direct Debit payments, you must collect a mandate agreement from your customer. Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method creates the accepted mandate. As the customer has implicitly signed the mandate when accepting these terms, you must communicate these terms in your form or through email.

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call `confirmSetupIntent`. This presents a webview where the customer can complete the setup on their bank’s website or app. Afterwards, the promise resolves with the result of the SetupIntent.

```javascript
export default function BancontactPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmai] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name,
      email,
    };
  };

  const { error, setupIntent } = await confirmSetupIntent(clientSecret, {
    paymentMethodType: 'Bancontact',
    paymentMethodData: {
      billingDetails,
    }
  });

  if (error) {
    Alert.alert(`Error code: ${error.code}`, error.message);
  } else if (setupIntent) {
    Alert.alert(
      'Success',
      `Setup intent created. Intent status: ${setupIntent.status}`
    );
  }

  return (
    <Screen>
      <TextInput
        placeholder="Email"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Charge the SEPA Direct Debit PaymentMethod later

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by [retrieving](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent and [expanding](https://docs.stripe.com/api/expanding_objects.md) the `latest_attempt` field where you’ll find the `generated_sepa_debit` ID inside of `payment_method_details`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["latest_attempt"],
});
```

Create a `PaymentIntent` with the SEPA Direct Debit ID and the customer’s ID.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["sepa_debit"],
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{SEPA_DEBIT_PAYMENT_METHOD_ID}}",
  confirm: true,
});
```

## Test your integration

#### Email

Set `payment_method.billing_details.email` to one of the following values to test the `PaymentIntent` status transitions. You can include your own custom text at the beginning of the email address followed by an underscore. For example, `test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct Debit PaymentMethod that always fails when used with a `PaymentIntent`.

| Email Address                                                      | Description                                                                                                                       |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `generatedSepaDebitIntentsSucceed@example.com`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `generatedSepaDebitIntentsSucceedDelayed@example.com`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `generatedSepaDebitIntentsFail@example.com`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `generatedSepaDebitIntentsFailDelayed@example.com`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `generatedSepaDebitIntentsSucceedDisputed@example.com`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `generatedSepaDebitIntentsFailsDueToInsufficientFunds@example.com` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

#### PaymentMethod

Use these PaymentMethods to test that the `PaymentIntent` status transitions. These tokens are useful for automated testing to immediately attach the PaymentMethod to the SetupIntent on the server.

| Payment Method                                                       | Description                                                                                                                       |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `pm_bancontact_generatedSepaDebitIntentsSucceed`                     | The `PaymentIntent` status transitions from `processing` to `succeeded`.                                                          |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDelayed`              | The `PaymentIntent` status transitions from `processing` to `succeeded` after at least three minutes.                             |
| `pm_bancontact_generatedSepaDebitIntentsFail`                        | The `PaymentIntent` status transitions from `processing` to `requires_payment_method`.                                            |
| `pm_bancontact_generatedSepaDebitIntentsFailDelayed`                 | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` after at least three minutes.               |
| `pm_bancontact_generatedSepaDebitIntentsSucceedDisputed`             | The `PaymentIntent` status transitions from `processing` to `succeeded`, but a dispute is created immediately.                    |
| `pm_bancontact_generatedSepaDebitIntentsFailsDueToInsufficientFunds` | The `PaymentIntent` status transitions from `processing` to `requires_payment_method` with the `insufficient_funds` failure code. |

## Optional: Handle post-setup events

Stripe sends a [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) event when the SetupIntent completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like saving the generated SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) to your database or charging your customer after a trial period.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle deep linking

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types *require* a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## See also

- [Accept a SEPA Direct Debit payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md)
- [Set up a subscription with SEPA Direct Debit in the EU](https://docs.stripe.com/billing/subscriptions/sepa-debit.md)
