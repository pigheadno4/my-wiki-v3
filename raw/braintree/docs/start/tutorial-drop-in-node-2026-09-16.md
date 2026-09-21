<!-- Source URL: https://developer.paypal.com/braintree/docs/start/tutorial-drop-in-node -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Drop-in Tutorial
slug: /docs/start/tutorial-drop-in-node/
createTime: '2025-04-01T22:14:09.541Z'
updateTime: '2026-09-02T15:27:57.280Z'
---



# Drop-in Tutorial


**IMPORTANT**
 **Starting October 1, 2026**, the Drop-in SDK will be [**deprecated**](/braintree/docs/guides/client-sdk/deprecation-policy/ios/v6/#status-categories). No new features, improvements, or bug fixes will be released after this date. Payment processing will continue to be supported until **October 1, 2027**, but we strongly recommend migrating to the Braintree SDK as soon as possible to avoid future disruption.

  **Starting October 1, 2027**, the Drop-in SDK will become [**unsupported**](/braintree/docs/guides/client-sdk/deprecation-policy/ios/v6/#status-categories). Braintree support team will no longer provide assistance for this SDK, and payment processing may be suspended at any time.

  **Action required:** Migrate to the [Braintree Android SDK](/braintree/docs/guides/client-sdk/setup/android/v5/), [Braintree iOS SDK](https://braintree.github.io/braintree_ios/current/), or [Braintree JavaScript SDK](/braintree/docs/guides/client-sdk/setup/javascript/v3/) to continue processing payments and receive ongoing updates, security fixes, and support.

 

Time
##### 25mins

Platforms
##### Windows & Mac

Difficulty
##### Easy

Technologies
##### JavaScript, Node.js, Express

For a more detailed walkthrough of a complete Braintree integration using the Drop-in UI, see our [Get Started](/braintree/docs/start/overview) guide.


## Before you begin

First, make sure you have the latest versions of [Node.js](https://nodejs.org/en/) and [npm](https://www.npmjs.com/get-npm) installed. You’ll also need a console (e.g. Terminal on Mac, Command Line on Windows) and a text editor of your choice.

To get you up and running quickly, we’ll use [Express](https://expressjs.com/) to generate a Node app with basic routing.


### Install the Express app generator


### console
```python
npm install --global express-generator@4
```
If you’re interested in how the Express generator works or its options, see the [Express generator docs](https://expressjs.com/en/starter/generator.html).


### Get a Braintree sandbox

To successfully run a test transaction, you’ll need a Braintree sandbox account. [Log in](https://sandbox.braintreegateway.com/login) or [sign up for one now](https://www.braintreepayments.com/sandbox).


## 1. Set up a basic app

Now that you have all the necessary tools installed, we can use the Express app generator to quickly create the basic application structure we’ll use for the tutorial.


### Generate the app

In your console, run this command in the directory where you want to store the tutorial code. Use --view=hbs to set the template engine to Handlebars – this is what we will use throughout the tutorial.


### console
```applescript
express braintreeTutorial --view=hbs
```

### Open your newly created app

The command above will have created a new folder with your app structure inside. Open that folder now.


### console
```bash
cd braintreeTutorial
```

### Install dependencies


### console
```cmake
npm install
```

### Install Braintree

The [Braintree Node.js library](https://github.com/braintree/braintree_node) is the server-side Braintree SDK that will communicate with Braintree’s servers. Install it now so that when we’re ready, we can wire up the payment form.


### console
```sql
npm install braintree --save
```

## 2. Add the Drop-in UI

Our basic app will have one page on the client and one [route](https://expressjs.com/en/starter/basic-routing.html) on the server.

Express already generated an index view that we’ll use for the payment form markup on the client. From here, we'll use Braintree's Drop-in UI to quickly create the form.

To load the Drop-in UI on the page, we’ll need to do 3 things:


- Include the Braintree client SDK
- Get a tokenization key
- Add the Drop-in UI markup


### Include the Braintree client SDK

For this tutorial, we'll use the latest Braintree JavaScript SDK. Add the following code just above the closing &lt;/head&gt; tag in views/layout.hbs.


### HTML
```html
<!-- includes the Braintree JS client SDK -->
<script src="https://js.braintreegateway.com/web/dropin/1.44.0/js/dropin.min.js"></script>
<!-- includes jQuery -->
<script src="http://code.jquery.com/jquery-3.2.1.min.js" crossorigin="anonymous"></script>
```

**NOTE**
We only include jQuery here to reduce the complexity of our tutorial code. It’s not a requirement in order to use Braintree.


### Get a tokenization key

There are 2 ways to authorize the client to collect payment information:


- A[client token](/braintree/docs/guides/authorization/client-token), which requires a round trip to your server and enables you to use all of Braintree’s client API capabilities
- A[tokenization key](/braintree/docs/guides/authorization/tokenization-key/javascript/v3), which is a static key with reduced privileges that authorizes a subset of Braintree’s client API capabilities

For this tutorial, we’ll use a **tokenization key**, which is stored in your Braintree Control Panel. To find it:


- Log into your[sandbox Control Panel](https://sandbox.braintreegateway.com)
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**Tokenization Keys**section
- You should see your key under the**Tokenization Keys**section; if no key appears, click the**Generate New Tokenization Key**button
- Keep this page open so you can add your key in the code below

For more information or help with this step, see our [API Credentials support article](/braintree/articles/control-panel/important-gateway-credentials#api-credentials).


### Add the Drop-in UI markup

Our Drop-in UI consists of a small amount of HTML markup, which will be initialized using the Braintree JavaScript SDK we included above.



Replace the contents of views/index.hbs with this code:




### HTML
```html
<div id="dropin-wrapper">
  <div id="checkout-message"></div>
  <div id="dropin-container"></div>
  <button id="submit-button">Submit payment</button>
</div>

<script>
  var button = document.querySelector('#submit-button');
  braintree.dropin.create({
    // Insert your tokenization key here
    authorization: '<use_your_tokenization_key>',
    container: '#dropin-container'
  }, function (createErr, instance) {
    button.addEventListener('click', function () {
      instance.requestPaymentMethod(function (requestPaymentMethodErr, payload) {
        // When the user clicks on the 'Submit payment' button
        // this code will send the encrypted payment information in a variable called a payment method nonce
        $.ajax({
          type: 'POST',
          url: '/checkout',
          data: { 'paymentMethodNonce': payload.nonce }
        }).done(function (result) {
          // Tear down the Drop-in UI instance.
          instance.teardown(function (teardownErr) {
            if (teardownErr) {
              console.error('Could not tear down Drop-in UI!');
            } else {
              console.info('Drop-in UI has been torn down!');
              // Remove the 'Submit payment' button
              $('#submit-button').remove();
            }
          });
          if (result.success) {
            $('#checkout-message').html('<h1>Success</h1>Your Drop-in UI is working! Check your <a href="https://sandbox.braintreegateway.com/login">sandbox Control Panel</a> for your test transactions. Refresh to try another transaction.');
          } else {
            console.log(result);
            $('#checkout-message').html('<h1>Error</h1>Check your console.');
          }
        });
      });
    });
  });
</script>
```

**NOTE**
Be sure to set the authorization parameter to your tokenization key as a string above.

The paymentMethodNonce is a string returned by the client SDK.It’s a one-time-use reference to the payment information that your customer provided in your payment form. In the next step, we’ll set up your server to receive this string so it can be used to create a transaction request.


## 3. Handle checkout

Now that the client is set up to securely collect payment information, we’ll create a route on your server that accepts the paymentMethodNonce from the Drop-in UI and then uses that nonce to create a sale transaction request for $10.


### Create a file called routes/checkout.js

Create this file in your text editor, IDE, or console.


#### On Mac


### console
```irpf90
touch routes/checkout.js
```

#### On Windows


### console
```css
echo.>routes\\checkout.js
```

### Add the payment logic


#### Get your sandbox API credentials

Next, get your sandbox API credentials from the [sandbox Control Panel](https://sandbox.braintreegateway.com). You'll need your:


- Sandbox merchant ID
- Public key
- Private key

You can get all the public and private key values on the same **API** page where you found your tokenization key. Your sandbox merchant ID can be located on the **Business** page. For full instructions, [follow this quick guide](/braintree/articles/control-panel/important-gateway-credentials#api-credentials).


**IMPORTANT**
Never share your public or private key.


#### Add the route code to routes/checkout.js

In routes/checkout.js, add the following to create the checkout route.


### Node
```javascript
const express = require('express');
const router = express.Router();
const braintree = require('braintree');

router.post('/', (req, res, next) => {
  const gateway = new braintree.BraintreeGateway({
    environment: braintree.Environment.Sandbox, // Use your own credentials from the sandbox Control Panel here
    merchantId: '<use_your_merchant_id>',
    publicKey: '<use_your_public_key>',
    privateKey: '<use_your_private_key>'
  });

  // Use the payment method nonce here
  const nonceFromTheClient = req.body.paymentMethodNonce;

  // Create a new transaction for $10
  const newTransaction = gateway.transaction.sale({
    amount: '10.00',
    paymentMethodNonce: nonceFromTheClient,
    options: {
      // This option requests the funds from the transaction
      // once it has been authorized successfully
      submitForSettlement: true
    }
  }, (error, result) => {
    if (result) {
      res.send(result);
    } else {
      res.status(500).send(error);
    }
  });
});

module.exports = router;
```

**IMPORTANT**
⚠️ This code snippet creates a gateway instance using the latest version of the Node SDK. [Learn more](braintree/docs/reference/general/server-sdk-migration-guide/node#creating-a-gateway-instance) 


**NOTE**
Be sure to set the merchantId , publicKey and privateKey parameters above.

To learn more about how the transaction.sale method works and which options you can specify, [see the reference](/braintree/docs/reference/request/transaction/sale/node).


### Connect the route to app.js

app.js is the file that serves as the main entry point for Node and Express apps. All routes, as well as other critical information that define how your app will work, are stored here. We’ll use the app.js file to link up the route we created in the previous step.


#### Add a /checkout route to app.js

After app.use('/users', usersRouter); in app.js, add your checkout route:


### JavaScript
```javascript
// The checkout route
const checkout = require('./routes/checkout');
app.use('/checkout', checkout);
```

## 4. Create a test transaction

At this point, you should have a properly-initialized payment form when you run your app.

To see your payment UI in action, we’ll run a few test transactions and then view them in the sandbox Control Panel.


### Run the app

Run the following command in your console.


### console
```coffeescript
npm start
```
Then open [http://localhost:3000/](http://localhost:3000/) in your browser.


### Enter a test card in the payment form

The Braintree sandbox only accepts specific test values. To create a successful transaction in your app, be sure to use the card information below for this test.


- **Card number**: 4111 1111 1111 1111
- **Expiry**: 09/23


**NOTE**
The Expiry date can be any date as long as it is in the future. The other valuesabove are required to match.

Once you create a successful transaction, feel free to try out other test cards listed on our [Testing reference page](/braintree/docs/reference/general/testing/node).


### See your transaction in the sandbox

You can view test transactions by logging back into the [sandbox Control Panel](https://sandbox.braintreegateway.com). At a highlevel, you'll see your new sale transaction reflected in the graph on your dashboard, but to see its details:


- Search for1111(the last 4 digits of the test card number above) in the search box, or
- Click**Transactions**in the top navigation to search with full control over your parameters

To learn more about searching in the Control Panel, see our [Search support article](/braintree/articles/control-panel/search).


## Next steps

Give yourself a high five! Now that you have a basic working integration, choose what you'd like to do next:


- Follow the[Get Started guide](/braintree/docs/start/overview)for a guided Drop-in integration with flow diagrams and additional context
- Add error handling to your[client](https://braintree.github.io/braintree-web/current/BraintreeError.html)and[server](/braintree/docs/reference/general/validation-errors/overview/)
- Learn how to add more payment method types and other features in our[integration guides](/braintree/docs/guides/overview)
- Explore the[API reference](/braintree/docs/reference/overview)for in-depth details on our API functionality
- [Get in touch with our Sales team](https://www.braintreepayments.com/contact/sales)to take your integration live
- Visit[Risk and Fraud Management solutions](/braintree/articles/guides/fraud-tools/premium/overview)and their integration requirements to protect yourself against fraud.

