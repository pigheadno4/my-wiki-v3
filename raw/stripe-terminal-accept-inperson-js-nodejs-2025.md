<!-- Source: Stripe Terminal — Accept in-person payments (US / S700 / JavaScript SDK / Node.js) -->
<!-- Fetched: 2026-04-24 -->

# Accept in-person payments

Country: United States  
Reader: Stripe Reader S700  
Architecture: JavaScript SDK  
Frontend: JavaScript  
Backend: Node.js

This guide shows you how to accept in-person payments in your own point of sale (POS) application using Stripe Terminal. You don't need any hardware to complete these steps with our simulated reader. Optionally, you can download the example and run the application.

When you're ready to use a physical reader, you only need to update the reader registration step (for server-driven integrations) or reader discovery step (for SDK integrations).

Don't code? Use Stripe's no-code options or get help from our partners.

## 1. Set up the server

### Install the Stripe Node library

Install the package and import it in your code. Alternatively, if you're starting from scratch and need a package.json file, download the project files using the Download link in the code editor.

```
npm install --save stripe
```

### Create a ConnectionToken endpoint

To connect to a reader, your back end needs to give the SDK permission to use it with your Stripe account by providing it with the secret from a ConnectionToken. Create connection tokens only for trusted clients, and pass a location ID when creating a connection token to control access to readers. If you're using Connect, scope the connection token to the relevant connected accounts.

> **Terminal access on macOS**: The Stripe Terminal SDK requires local network access. When using macOS, you must explicitly allow your browser apps access to local network devices. For more information, see the Stripe Support article.

## 2. Set up the SDK

### Install the SDK

This script must always load directly from https://js.stripe.com for compatibility with the latest reader software. Don't include the script in a bundle or host a copy yourself as this could break your integration without warning. We also provide an npm package that makes it easier to load and use the Terminal JS SDK as a module. For more information, check out the project on GitHub.

### Create Locations for your readers

Create Locations to organize your readers. Locations group readers and allow them to automatically download the reader configuration needed for their region of use. You must assign a Location to each reader when you register it, which you can do using the API or the Dashboard.

### Fetch ConnectionToken

To give the SDK access to this endpoint, create a function in your web application that requests a ConnectionToken from your back end and returns the secret from the ConnectionToken object.

### Initialize the SDK

To initialize a StripeTerminal instance in your JavaScript application, provide the onFetchConnectionToken function. You must also provide the onUnexpectedReaderDisconnect function to handle unexpected disconnects from the reader.

## 3. Connect to the simulated reader

### Discover readers

The Stripe Terminal SDK comes with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. To use the simulated reader, call discoverReaders to search for readers, with the simulated option set to true. To discover intended readers more easily, filter by location.

### Connect to the simulated reader

When discoverReaders returns a result, call connectReader to connect to the simulated reader.

## 4. Collecting Payments

### Create a PaymentIntent

Add an endpoint on your server that creates a PaymentIntent. A PaymentIntent tracks the customer's payment lifecycle, keeping track of any failed payment attempts and ensuring they're only charged once. Return the PaymentIntent's client secret in the response. If you're using Connect, you can also specify connected account information based on your platform's charge logic.

### Fetch the PaymentIntent

Make a request to your server for a PaymentIntent to initiate the payment process.

### Collect payment method details

Call collectPaymentMethod with the PaymentIntent's client secret to collect a payment method. When connected to the simulated reader, calling this method immediately updates the PaymentIntent object with a simulated test card. When connected to a physical reader, the connected reader waits for a card to be presented.

### Process the payment

After successfully collecting payment method data, call processPayment with the updated PaymentIntent to process the payment. A successful call results in a PaymentIntent with a status of requires_capture for manual capture or succeeded for automatic capture.

### Create an endpoint to capture the PaymentIntent

Create an endpoint on your back end that accepts a PaymentIntent ID and sends a request to the Stripe API to capture it.

### Capture the PaymentIntent

If you defined capture_method as manual during PaymentIntent creation, the SDK returns an authorized but not captured PaymentIntent to your application. When the PaymentIntent status is requires_capture, notify your back end to capture the PaymentIntent.

For connected accounts, before manually capturing a payment, inspect the PaymentIntent's application_fee_amount and modify it if needed.

## 5. Test the integration

### Run the application

Run your server and go to localhost:4242.

```
npm start
```

### Use a test card number to try your integration

You can configure the simulated reader to test different flows within your point of sale application such as different card brands or error scenarios like a declined charge. To enable this behavior, insert this line of code before you call collectPaymentMethod.

- Payment succeeds: `4242 4242 4242 4242`
- Payment is declined: `4000 0000 0000 9995`

## Next steps

- Connecting to a reader — Learn what it means to connect your app to a reader.
- Fleet management — Group and manage a fleet of readers by physical location.
- Connect — Integrate Stripe Terminal with your Connect platform.

---

## Server code (server.js / index.js — Node.js + Express)

```javascript
const express = require("express");
const app = express();
const { resolve } = require("path");
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("sk_test_Ou1w6LVt3zmVipDVJsvMeQsc");

app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const createLocation = async () => {
  const location = await stripe.terminal.locations.create({
    display_name: 'HQ',
    address: {
      line1: '1272 Valencia Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94110',
    },
  });

  return location;
};

// The ConnectionToken's secret lets you connect to any Stripe Terminal reader
// and take payments with your Stripe account.
// Be sure to authenticate the endpoint for creating connection tokens.
app.post("/connection_token", async (req, res) => {
  let connectionToken = await stripe.terminal.connectionTokens.create();
  res.json({secret: connectionToken.secret});
});

app.post("/create_payment_intent", async (req, res) => {
  // For Terminal payments, the 'payment_method_types' parameter must include
  // 'card_present'.
  // To automatically capture funds when a charge is authorized,
  // set `capture_method` to `automatic`.
  const intent = await stripe.paymentIntents.create({
    amount: req.body.amount,
    currency: 'usd',
    payment_method_types: [
      'card_present',
    ],
    capture_method: 'automatic',
    payment_method_options: {
      card_present: {
        capture_method: 'manual_preferred'
      }
    }
  });
  res.json(intent);
});

app.post("/capture_payment_intent", async (req, res) => {
  const intent = await stripe.paymentIntents.capture(req.body.payment_intent_id);
  res.send(intent);
});

app.listen(4242, () => console.log('Node server listening on port 4242!'));
```

---

## Client HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Accept in-person payments</title>
    <meta name="description" content="A demo of an in-person payment on Stripe" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <link rel="stylesheet" href="global.css">
    <script src="client.js" defer></script>
    <script src="https://js.stripe.com/terminal/v1/"></script>
  </head>
  <body>
    <div class="container-fluid h-100">
      <div class="row h-100">
        <div class="col-sm-6 offset h-100">
          <div class="row title">Simulate reader pairing</div>
          <div class="row margin pad">
            <button id="discover-button">
              1. Discover readers
              <svg aria-hidden="true" height="16" width="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.293 2.709A1 1 0 0 1 6.71 1.293l6.3 6.3a1 1 0 0 1 0 1.414l-6.3 6.3a1 1 0 0 1-1.416-1.416L10.884 8.3z" fill-rule="evenodd"></path>
              </svg>
            </button>
          </div>
          <div class="row margin pad">
            <button id="connect-button">
              2. Connect to a reader
              <svg aria-hidden="true" height="16" width="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.293 2.709A1 1 0 0 1 6.71 1.293l6.3 6.3a1 1 0 0 1 0 1.414l-6.3 6.3a1 1 0 0 1-1.416-1.416L10.884 8.3z" fill-rule="evenodd"></path>
              </svg>
            </button>
          </div>
          <hr/>
          <div class="row title">Simulate a transaction</div>
          <div class="row margin pad text">Enter an amount</div>
          <div class="row pad">
            <div class="">
              <input id="amount-input" type="text" value="2000">
            </div>
          </div>
          <div class="row margin pad">
            <button id="collect-button">
              3. Collect Payment
              <svg aria-hidden="true" height="16" width="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.293 2.709A1 1 0 0 1 6.71 1.293l6.3 6.3a1 1 0 0 1 0 1.414l-6.3 6.3a1 1 0 0 1-1.416-1.416L10.884 8.3z" fill-rule="evenodd"></path>
              </svg>
            </button>
          </div>
          <div class="row margin pad">
            <button id="capture-button">
              4. Capture Payment
              <svg aria-hidden="true" height="16" width="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.293 2.709A1 1 0 0 1 6.71 1.293l6.3 6.3a1 1 0 0 1 0 1.414l-6.3 6.3a1 1 0 0 1-1.416-1.416L10.884 8.3z" fill-rule="evenodd"></path>
              </svg>
            </button>
          </div>
        </div>
        <div class="col-sm-6 h-100 log-col">
          <div class="row title">Logs</div>
          <div class="row">
            <div class="col-sm-12" id="logs"></div>
          </div>
        </div>
      </div>
    </div>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```

---

## Client CSS (global.css)

```css
/* Variables */
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: none;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
  line-height: 1.4em;
}

html,
body {
  overflow: hidden;
  height: 100%;
}

.pad {
  padding-right: 35px;
  padding-left: 35px;
}

hr {
  margin-right: 20px;
  margin-left: 20px;
}

#logs>hr {
  margin-right: 0px;
  margin-left: 0px;
}

svg {
  height: -webkit-fill-available;
  float: right;
}

.margin {
  margin-top: 15px;
}

.title {
  padding-right: 35px;
  padding-left: 35px;
  margin-top: 20px;
  margin-bottom: 5px;
  font-size: 20px;
  font-weight: 600;
}

.text {
  font-size: 15px;
  font-weight: 500;
  color: #525f7f;
}

.log-col {
  overflow-y: scroll;
}

#logs {
  padding-right: 35px;
  padding-left: 35px;
  margin-top: 20px;
  margin-bottom: 5px;
  color: black;
}

.offset {
  background: #f7fafc;
}

.green {
  color: #09825d;
}

.log-title {
  font-size: 16px;
  font-weight: 500;
  padding-left: 15px;
  margin-bottom: 10px;
}

.log {
  padding-left: 15px;
}

pre {
  color: #585050 !important;
}

button {
  color: black;
  padding: 16px;
  border: 0;
  background: white;
  -webkit-box-shadow: none;
  box-shadow: none;
  outline: none;
  cursor: pointer;
  -webkit-transition: all 0.15s ease;
  -o-transition: all 0.15s ease;
  transition: all 0.15s ease;
  width: 100%;
  height: 54px;
  border-radius: 6px !important;
  font-size: 16px;
  font-weight: 500;
  text-align: left;
  text-transform: capitalize;
  box-shadow: 0px 7px 14px rgba(60, 66, 87, 0.12), 0px 3px 6px rgba(0, 0, 0, 0.08);
}

.input-icon {
  position: relative;
  border-radius: 4px;
}

.input-icon>i {
  position: absolute;
  border-radius: 4px;
  display: block;
  transform: translate(0, -50%);
  top: 50%;
  pointer-events: none;
  width: 25px;
  text-align: center;
  font-style: normal;
}

.input-icon>input {
  border-radius: 4px;
  border: 1px solid #E3E8EE;
  width: 100%;
  height: 40px;
  color: black;
  font-size: 16px;
  font-weight: normal;
  padding-left: 25px;
  padding-right: 0;
}
```

---

## Client JavaScript (client.js)

```javascript
var terminal = StripeTerminal.create({
  onFetchConnectionToken: fetchConnectionToken,
  onUnexpectedReaderDisconnect: unexpectedDisconnect,
});

function unexpectedDisconnect() {
  // In this function, your app should notify the user that the reader disconnected.
  // You can also include a way to attempt to reconnect to a reader.
  console.log("Disconnected from reader")
}

function fetchConnectionToken() {
  // Do not cache or hardcode the ConnectionToken. The SDK manages the ConnectionToken's lifecycle.
  return fetch('/connection_token', { method: "POST" })
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      return data.secret;
    });
}

// Handler for a "Discover readers" button
function discoverReaderHandler() {
  var config = {simulated: true};
  terminal.discoverReaders(config).then(function(discoverResult) {
    if (discoverResult.error) {
      console.log('Failed to discover: ', discoverResult.error);
    } else if (discoverResult.discoveredReaders.length === 0) {
        console.log('No available readers.');
    } else {
        discoveredReaders = discoverResult.discoveredReaders;
        log('terminal.discoverReaders', discoveredReaders);
    }
  });
}

// Handler for a "Connect Reader" button
function connectReaderHandler(discoveredReaders) {
  // Just select the first reader here.
  var selectedReader = discoveredReaders[0];
  terminal.connectReader(selectedReader).then(function(connectResult) {
    if (connectResult.error) {
      console.log('Failed to connect: ', connectResult.error);
    } else {
        console.log('Connected to reader: ', connectResult.reader.label);
        log('terminal.connectReader', connectResult)
    }
  });
}

function fetchPaymentIntentClientSecret(amount) {
  const bodyContent = JSON.stringify({ amount: amount });
  return fetch('/create_payment_intent', {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: bodyContent
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    return data.client_secret;
  });
}

function collectPayment(amount) {
  fetchPaymentIntentClientSecret(amount).then(function(client_secret) {
      // Use test card number to simulate different payment flows within your point of sale application
      terminal.setSimulatorConfiguration({testCardNumber: '4242424242424242'});
      terminal.collectPaymentMethod(client_secret).then(function(result) {
      if (result.error) {
        // Placeholder for handling result.error
      } else {
          log('terminal.collectPaymentMethod', result.paymentIntent);
          terminal.processPayment(result.paymentIntent).then(function(result) {
          if (result.error) {
            console.log(result.error)
          } else if (result.paymentIntent) {
              paymentIntentId = result.paymentIntent.id;
              log('terminal.processPayment', result.paymentIntent);
          }
        });
      }
    });
  });
}

function capture(paymentIntentId) {
  return fetch('/capture_payment_intent', {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
      body: JSON.stringify({"payment_intent_id": paymentIntentId})
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    log('server.capture', data);
  });
}

var discoveredReaders;
var paymentIntentId;

const discoverButton = document.getElementById('discover-button');
discoverButton.addEventListener('click', async (event) => {
  discoverReaderHandler();
});

const connectButton = document.getElementById('connect-button');
connectButton.addEventListener('click', async (event) => {
  connectReaderHandler(discoveredReaders);
});

const collectButton = document.getElementById('collect-button');
collectButton.addEventListener('click', async (event) => {
  amount = document.getElementById("amount-input").value
  collectPayment(amount);
});

const captureButton = document.getElementById('capture-button');
captureButton.addEventListener('click', async (event) => {
  capture(paymentIntentId);
});

function log(method, message) {
  var logs = document.getElementById("logs");
  var title = document.createElement("div");
  var log = document.createElement("div");
  title.classList.add('row');
  title.classList.add('log-title');
  title.textContent = method;
  log.classList.add('row');
  log.classList.add('log');
  var hr = document.createElement("hr");
  var pre = document.createElement("pre");
  var code = document.createElement("code");
  code.textContent = formatJson(JSON.stringify(message, undefined, 2));
  pre.append(code);
  log.append(pre);
  logs.prepend(hr);
  logs.prepend(log);
  logs.prepend(title);
}

function stringLengthOfInt(number) {
  return number.toString().length;
}

function padSpaces(lineNumber, fixedWidth) {
  return " ".repeat(2 + fixedWidth - stringLengthOfInt(lineNumber));
}

function formatJson(message) {
  var lines = message.split('\n');
  var json = "";
  var lineNumberFixedWidth = stringLengthOfInt(lines.length);
  for(var i = 1; i <= lines.length; i += 1) {
    line = i + padSpaces(i, lineNumberFixedWidth) + lines[i-1];
    json = json + line + '\n';
  }
  return json
}
```
