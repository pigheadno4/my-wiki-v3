---
title: JavaScript SDK reference
slug: /sdk/js/reference/
createTime: "2024-03-14T23:47:37.606Z"
updateTime: "2026-02-04T13:28:50.196Z"
---

# JavaScript SDK reference

**warning**
**Important:** This documentation covers the JavaScript SDK v5 with the CardFields component. For the legacy HostedFields component, see the [archived reference](/sdk/js/v1/reference/) .

The PayPal JavaScript SDK dynamically exposes objects and methods based on the components you select. Add components to your &lt;script&gt; by passing them in the src URL using the components query string parameter.

#### **`Overview`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=YOUR_COMPONENTS"></script>
```

The JavaScript SDK supports the following components:

- [buttons](/sdk/js/reference/#buttons) (default)
- [marks](/sdk/js/reference/#marks)
- [card-fields](/sdk/js/reference/#card-fields)
- [funding-eligibility](/sdk/js/reference/#funding-eligibility)
- [messages](/sdk/js/reference/#messages)

The payment buttons component automatically shows all eligible buttons in a single location on your page. See the [standard payments](/studio/checkout/standard) integration.

#### **`Vanilla JS`**

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons"></script>
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
    // Add other options as needed
  };
  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
        // Add other options as needed
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal.Buttons().render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### paypal.Buttons(options)

- [style](/sdk/js/reference/#style)
- [message](/sdk/js/reference/#message)
- [createOrder](/sdk/js/reference/#createorder)
- [createSubscription](/sdk/js/reference/#create-subscription)
- [onApprove](/sdk/js/reference/#onapprove)
- [onCancel](/sdk/js/reference/#oncancel)
- [onError](/sdk/js/reference/#onerror)
- [onInit/onClick](/sdk/js/reference/#oninitonclick)
- [onShippingChange](/sdk/js/reference/#onshippingchange)
- [onShippingAddressChange](/sdk/js/reference/#on-shipping-address-change)
- [onShippingOptionsChange](/sdk/js/reference/#on-shipping-options-change)

### style

Customize your buttons using the style option.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    style: {
      layout: "vertical",
      color: "blue",
      shape: "rect",
      label: "paypal",
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const styles = {
    shape: "rect",
    layout: "vertical",
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons style={styles} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const styles: PayPalButtonsComponentProps["style"] = {
        shape: "rect",
        layout: "vertical",
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons style={styles}/>
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        style: {
          layout: "vertical",
          color: "blue",
          shape: "rect",
          label: "paypal",
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### Layout

Set the style.layout option to determine how the buttons show up when multiple buttons are available:

| Value                                                    | Description                                                                                                                                                                                                                                                                                                                                                                     | Layout |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| vertical                                                 | **Default**. Buttons are stacked vertically with a maximum of 6 buttons. Recommended when:- Presenting a dynamic list of payment options on checkout and shopping cart pages.                                                                                                                                                                                                   |
| - Leveraging Checkout as a full-stack payments platform. | ![](https://www.paypalobjects.com/ppdevdocs/v1/img/icon-mobile.svg)**Mobile** ![](https://www.paypalobjects.com/ppdevdocs/v1/img/docs/pay-later/vertical_mobile.png) Venmo is available on mobile in US markets only.![](https://www.paypalobjects.com/ppdevdocs/v1/img/icon-web.svg)**Web** ![](https://www.paypalobjects.com/ppdevdocs/v1/img/docs/checkout/vertical_web.png) |
| horizontal                                               | Buttons are stacked horizontally with a maximum of 2 buttons. Recommended when:- Placing buttons on a product page, next to the product.                                                                                                                                                                                                                                        |

- Space on the page is limited.
- Alternative payment options are already provided. | ![](https://www.paypalobjects.com/ppdevdocs/v1/img/icon-mobile.svg)**Mobile** Venmo is available on mobile in US markets only.![](https://www.paypalobjects.com/ppdevdocs/v1/img/icon-web.svg)**Web** ![](https://www.paypalobjects.com/ppdevdocs/v1/img/docs/pay-later/horizontal_web.png) |

### Which buttons will I see?

The buttons that show up are decided automatically, based on a range of factors, including:

- Buyer country
- Device type
- Funding sources the buyer has opted to see

As a result, each buyer sees a unique combination of buttons. Pay Later offers differ by country and have different buttons. To prevent certain buttons from showing up, see [Disable funding](https://developer.paypal.com/sdk/js/configuration/#disable-funding) in the JavaScript SDK reference.

### Color

Set the style.color option to 1 of these values:

| Value            | Description                                                                                                                                                                                                                                                     | Button |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| gold             | **Recommended** People around the world know us for the color gold and research confirms it. Extensive testing determined just the right shade and shape that help increase conversion. Use it on your website to leverage PayPal’s recognition and preference. |        |
| blue             | **First alternative** If gold doesn't work for your site, try the PayPalbluebutton. Research shows that people know it is our brand color, which provides a halo of trust and security to your experience.                                                      |        |
| silverwhiteblack | **Second alternatives** If gold or blue doesn't work for your site design or aesthetic, try thesilver,white, orblackbuttons. Because these colors are less capable of drawing people’s attention, we recommend these button colors as a second alternative.     |        |

### Shape

Set the style.shape option to 1 of these values:

| Value | Description                               | Button |
| ----- | ----------------------------------------- | ------ |
| rect  | **Recommended** The default button shape. |        |
| pill  | Rounds the sides of the button.           |        |
| sharp | Gives the button sharp corners.           |        |

#### Border radius

style.borderRadius is used to define a custom border radius of the buttons.

To define the border radius of the buttons, set the style.borderRadius option to a number that is greater than or equal to 0 .

**Note:** If style.borderRadius and style.shape are both defined, style.borderRadius will take priority.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    style: {
      borderRadius: 10,
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const styles = {
    borderRadius: 10,
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons style={styles} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const styles : PayPalButtonsComponentProps["style"] = {
        borderRadius: 10,
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons style={styles}/>
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        style: {
          borderRadius: 10,
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

#### Size

- The button adapts to the size of its container element by default.

- Your button container element needs to be wide enough for your horizontal payment buttons.

#### Height

To customize the button height, set the style.height option to a value from 25 to 55 .
The button has a default maximum height of 55px. Remove this limitation and set the button height to fill its parent container:

- Set style.disableMaxHeight to true .
- Select a valid funding source: fundingSource: 'paypal' | 'venmo' | 'paylater' | 'credit'
- Change the height value at the parent container level.

**Note:** If style.disableMaxHeight and style.height are both defined on the PayPal button, an error will be thrown and the button will not render. You must choose one or the other.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    style: {
      disableMaxHeight: true,
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const styles = {
    disableMaxHeight: true,
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons style={styles} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const styles : PayPalButtonsComponentProps["style"] = {
        disableMaxHeight: true,
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons style={styles}/>
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        style: {
          disableMaxHeight: true,
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

#### Width

The button has a default maximum width of 750px, but you can make the button larger:

- Set style.disableMaxWidth to true .
- Change the max-width value at the container level.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    style: {
      disableMaxWidth: true,
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const styles = {
    disableMaxWidth: true,
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons style={styles} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const styles : PayPalButtonsComponentProps["style"] = {
        disableMaxWidth: true,
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons style={styles}/>
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        style: {
          disableMaxWidth: true,
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

#### Label

Set the style.label option to 1 of these values:

| Value                      | Description                                                                                                                                                                                                                                                                                       | Button |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| paypal                     | **Recommended** The default option. Shows the PayPal logo.                                                                                                                                                                                                                                        |        |
| checkout                   | Shows the Checkout button.                                                                                                                                                                                                                                                                        |        |
| buynow                     | Shows the PayPal Buy Now button and initializes the checkout flow.                                                                                                                                                                                                                                |        |
| pay                        | Shows the Pay With PayPal button and initializes the checkout flow.                                                                                                                                                                                                                               |        |
| installment                | Shows the PayPal installment button and offers a specified number of payments during a payment installment period.**Note:**Theinstallmentfeature is available only inMXandBR.Setstyle.periodto set the number of payments during the installment period:- BR : 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 |
| - en_MX , MX : 3, 6, 9, 12 |                                                                                                                                                                                                                                                                                                   |

#### Tagline

Set the style.tagline to false to disable the tagline text:

**Note:** Set the style.layout to horizontal for taglines. If using the message option it will replace the tagline.

| Value | Description                                | Button               |
| ----- | ------------------------------------------ | -------------------- |
| true  | **Recommended** Show tagline text Default. | Two easy ways to pay |
| false | Disable tagline text.                      |                      |

### Message

Customize the message with your buttons using the message option.

**Note:** Messaging is currently supported for US merchants and US customers only. Merchants must be eligible for Pay Later to display Pay Later offers with buttons. Other PayPal value propositions appear, even if a merchant isineligible for Pay Later.

#### **`Message`**

```javascript
paypal
  .Buttons({
    message: {
      amount: 100,
      align: "center",
      color: "black",
      position: "top",
    },
  })
  .render("#paypal-button-container");
```

#### Amount

Set the message.amount option to show the most relevant offer and price breakdown to your customers.

To define the amount of the message, set the message.amount option to a number that is greater than 0 . This value should reflect the current product or cart value that will be used once a checkout session has started.

| Value     | Description                                                                   | Message |
| --------- | ----------------------------------------------------------------------------- | ------- |
| undefined | **Default**. When no amount value is provided a generic message is shown.     |         |
| 100       | An example qualifying amount for Pay in 4 with a weekly amount breakdown.     |         |
| 2000      | An example qualifying amount for Pay Monthly with a monthly amount breakdown. |         |

#### Align

Set the message.align option to align the message content to the buttons.

| Value  | Description                                                          | Message |
| ------ | -------------------------------------------------------------------- | ------- |
| center | **Default**. Aligned in the center between the edges of the buttons. |         |
| left   | Aligned to the left edge of the buttons.                             |         |
| right  | Aligned to the right edge of the buttons.                            |         |

#### Color

Set the message.color option to change the message color from black or white depending your website background so the message is visible.

| Value | Description                                                            | Message |
| ----- | ---------------------------------------------------------------------- | ------- |
| black | **Default**. Black text with a colored PayPal logo and blue link text. |         |
| white | White text with a white PayPal logo and white link text.               |         |

#### Position

Set the message.position option to place the message above or below the buttons.

| Value  | Description                                           | Message |
| ------ | ----------------------------------------------------- | ------- |
| top    | Position the message above the buttons.               |         |
| bottom | **Default** . Position the message below the buttons. |

**Note:** When the Debit/Credit Card button is present as part of your button stack only top is supported and will be the default value. | |

### displayOnly

The displayOnly parameter determines the payment methods your customers see. By default, buyers see all eligible payment methods. Options passed to displayOnly are applied in order from left to right.

We have the following options available:

| Value     | Description                                                                                                                                                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vaultable | Display only the[payment methods that support save](https://developer.paypal.com/docs/checkout/save-payment-methods/). Your integration, merchant settings, and customer location determine which payment methods can be saved. |

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    displayOnly: ["vaultable"],
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const displayOnly = ["vaultable"];

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons displayOnly={displayOnly} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const displayOnly: PayPalButtonsComponentProps["displayOnly"] = ["vaultable"];

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons displayOnly={displayOnly}/>
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        displayOnly: ["vaultable"],
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### createOrder

The createOrder function sets up the details of the transaction. Pass createOrder as a parameter in paypal.Buttons . When the buyer selects the PayPal button, createOrder launches the PayPal Checkout window. The buyer logs in and approves the transaction on the paypal.com website.

#### createOrder

#### **`Vanilla JS`**

```javascript
<!DOCTYPE html>
<html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <!-- Set up a container element for the button -->
        <div id="paypal-button-container"></div>

        <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD"></script>

        <script>
            paypal.Buttons({
                async createOrder() {
                    const response = await fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            cart: [{
                                sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
                                quantity: "YOUR_PRODUCT_QUANTITY",
                            }]
                        })
                    });

                    const order = await response.json();

                    return order.id;
                }
            }).render('#paypal-button-container');
        </script>
    </body>
</html>

```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const createOrder = async () => {
    try {
      const response = await fetch("/my-server/create-paypal-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          cart: [{ id: "YOUR_PRODUCT_ID", quantity: "YOUR_PRODUCT_QUANTITY" }],
        }),
      });

      const orderData = await response.json();

      if (!orderData.id) {
        const errorDetail = orderData.details[0];
        const errorMessage =
          errorDetail ?
            `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
          : "Unexpected error occurred, please try again.";

        throw new Error(errorMessage);
      }

      return orderData.id;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons createOrder={createOrder} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

interface OrderData {
    id: string;
    details?: Array<{
      issue: string;
      description: string;
    }>;
    debug_id?: string;
}

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const createOrder: PayPalButtonsComponentProps["createOrder"] = async () => {
        try {
            const response = await fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: { "Content-Type": application/json" },
                body: JSON.stringify({
                    cart: [{ id: "YOUR_PRODUCT_ID", quantity: "YOUR_PRODUCT_QUANTITY" }],
                }),
            });

          const orderData: OrderData = await response.json();

          if (!orderData.id) {
              const errorDetail = orderData?.details?[0];
              const errorMessage = errorDetail
                  ? `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
                  : "Unexpected error occurred, please try again.";

              throw new Error(errorMessage);
          }

          return orderData.id;

        } catch (error) {
            console.error(error);
            throw error;
        }
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons createOrder={createOrder} />
            </PayPalScriptProvider>
        </div>
  );
};

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({ clientId: "YOUR_CLIENT_ID" });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        async createOrder() {
          try {
            const response = await fetch("/my-server/create-paypal-order", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                cart: [
                  { id: "YOUR_PRODUCT_ID", quantity: "YOUR_PRODUCT_QUANTITY" },
                ],
              }),
            });

            const orderData = await response.json();

            if (!orderData.id) {
              const errorDetail = orderData.details[0];
              const errorMessage =
                errorDetail ?
                  `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
                : "Unexpected error occurred, please try again.";

              throw new Error(errorMessage);
            }

            return orderData.id;
          } catch (error) {
            console.error(error);
            throw error;
          }
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

#### Server (Node.js):

#### **`Vanilla JS`**

```javascript

app.post("/my-server/create-paypal-order", async (req, res) => {
  const order = await createOrder();
  res.json(order);
});

// use the orders api to create an order
function createOrder() {
  // create accessToken using your clientID and clientSecret
  // for the full stack example, please see the Standard Integration guide
  // https://developer.paypal.com/docs/multiparty/checkout/standard/integrate/
  const accessToken = "REPLACE_WITH_YOUR_ACCESS_TOKEN";
  return fetch ("https://api-m.sandbox.paypal.com/v2/checkout/orders", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    }
    body: JSON.stringify({
      "purchase_units": [
        {
          "amount": {
            "currency_code": "USD",
            "value": "100.00"
          },
          "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b"
        }
      ],
      "intent": "CAPTURE",
      "payment_source": {
        "paypal": {
          "experience_context": {
            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
            "payment_method_selected": "PAYPAL",
            "brand_name": "EXAMPLE INC",
            "locale": "en-US",
            "landing_page": "LOGIN",
            "shipping_preference": "GET_FROM_FILE",
            "user_action": "PAY_NOW",
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl"
          }
        }
      }
    })
  })
  .then((response) => response.json());
}

```

#### Orders v2 API options

- intent : The intent to either capture the payment immediately or authorize a payment for an order after order creation. The values are:

- CAPTURE : **Default** . The merchant intends to capture payment immediately after the customer makes a payment.

- AUTHORIZE : The merchant intends to authorize a payment and place funds on hold after the customer makes a payment.Confirm the successful capture before providing goods or services. Authorized payments can be captured for up to 3 days, and may extend up to 29 days. After the 3-day honor period, the original authorized payment expires and you need to re-authorize the payment. You need to make a separate request to capture payments on demand. This intent isn't supported when you have more than 1 purchase_unit within your order.

See [authorize a payment and capture funds later](https:/docs/checkout/standard/customize/authorization/) .

- purchase_units : **Required** . An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee. See [purchase unit request object definition](https:/docs/api/orders/v2/#definition-model-update_purchase_unit_request) for additional information.

- payment_source : Optionally define the payment_source when creating the order. This payment source can be paypal , a vault token , card information for PCI-compliant merchants, or alternative payment methods such as blik and apple_pay . For more information, see [Orders v2 API](https:/docs/api/orders/v2/#orders_create) and [payment_source](https:/docs/api/orders/v2/#definition-payment_source) .

### createSubscription

Provides a simplified and secure subscription experience. PayPal presents payment types to your buyers automatically, making it easier for them to complete their purchase using methods such as Pay with Venmo, PayPal Credit, and credit card payments without reintegration as they are made available.

Pass vault=true and intent=subscription in the JavaScript SDK to set up a subscription, rather than a one-time transaction.

#### **`Vanilla JS`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons&vault=true&intent=subscription"></script>
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
    vault: true,
    intent: "subscription",
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalScriptProvider, ReactPayPalScriptOptions } from '@paypal/react-paypal-js';

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
        vault: true,
        intent: "subscription",
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
              <PayPalButtons />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
    vault: true,
    intent: "subscription",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal.Buttons().render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

Finally, implement the createSubscription function that's called when the buyer selects the PayPal button.

#### Actions

- create : Creates a subscription for your plan and includes the plan ID, subscriber details, shipping, and other details. The plan_id needs to belong to the client-id configured on the script.

actions.subscription.create options: See the [create subscription](https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_create) endpoint for supported options defined in the request body. Also see [create a payment button for the subscription](https://developer.paypal.com/docs/subscriptions/integrate/#3-create-payment-button) for more examples.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    createSubscription(data, actions) {
      return actions.subscription.create({
        plan_id: "YOUR_PLAN_ID",
      });
    },

    onApprove(data) {
      alert(
        `You have successfully created subscription ${data.subscriptionID}`,
      );
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
    vault: true,
    intent: "subscription",
  };

  const createSubscription = (data, actions) => {
    return actions.subscription.create({
      plan_id: "YOUR_PLAN_ID",
    });
  };

  const onApprove = (data) => {
    alert(`You have successfully subscribed to ${data.subscriptionID}`); // Optional message given to subscriber
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons
          createSubscription={createSubscription}
          onApprove={onApprove}
        />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { PayPalButtons, PayPalButtonsComponentProps, PayPalScriptProvider, ReactPayPalScriptOptions } from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
        vault: true,
        intent: "subscription"
    };

    const createSubscription: PayPalButtonsComponentProps["createSubscription"] = (data, actions) => {
        return actions.subscription.create({
            "plan_id": "YOUR_PLAN_ID"
          });
    }

    const onApprove: PayPalButtonsComponentProps["onApprove"] = async (data) => {
        alert(`You have successfully subscribed to ${data.subscriptionID}`); // Optional message given to subscriber
    }

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons
                    createSubscription={createSubscription}
                    onApprove={onApprove}
                />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
    vault: true,
    intent: "subscription",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        createSubscription(data, actions) {
          return actions.subscription.create({
            plan_id: "YOUR_PLAN_ID",
          });
        },
        onApprove(data) {
          alert(`You have successfully subscribed to ${data.subscriptionID}`); // Optional message given to subscriber
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

- revise : Updates the subscription which could be in ACTIVE or SUSPENDED status. See [upgrade or downgrade a subscription](https:/docs/subscriptions/customize/revise-subscriptions/) to make a revision using the Subscriptions API.

### onApprove

Captures the funds from the transaction and shows a message that tells the buyer the payment was successful. The method is called after the buyer approves the transaction on the paypal.com website.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    async createOrder() {
      const response = await fetch("/my-server/create-paypal-order", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          cart: [
            {
              sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
              quantity: "YOUR_PRODUCT_QUANTITY",
            },
          ],
        }),
      });

      const data = await response.json();

      return data.id;
    },
    async onApprove(data) {
      // Capture the funds from the transaction.
      const response = await fetch("/my-server/capture-paypal-order", {
        method: "POST",
        body: JSON.stringify({
          orderID: data.orderID,
        }),
      });

      const details = await response.json();

      // Show success message to buyer
      alert(`Transaction completed by ${details.payer.name.given_name}`);
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "MY_CLIENT_ID",
  };

  const createOrder = async () => {
    const response = await fetch("/my-server/create-paypal-order", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        cart: [
          {
            sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
            quantity: "YOUR_PRODUCT_QUANTITY",
          },
        ],
      }),
    });

    const data = await response.json();

    return data.id;
  };

  const onApprove = async (data) => {
    // Capture the funds from the transaction.
    const response = await fetch("/my-server/capture-paypal-order", {
      method: "POST",
      body: JSON.stringify({
        orderID: data.orderID,
      }),
    });

    const details = await response.json();

    // Show success message to buyer
    alert(`Transaction completed by ${details.payer.name.given_name}`);
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons createOrder={createOrder} onApprove={onApprove} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const createOrder: PayPalButtonsComponentProps["createOrder"] = async () => {
        const response = await fetch("/my-server/create-paypal-order", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                cart: [
                    {
                        sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
                        quantity: "YOUR_PRODUCT_QUANTITY",
                    },
                ],
            }),
        });

        const data = await response.json();

        return data.id;
    };

    const onApprove: PayPalButtonsComponentProps["onApprove"] = async (data) => {
        // Capture the funds from the transaction.
        const response = await fetch("/my-server/capture-paypal-order", {
            method: "POST",
            body: JSON.stringify({
                orderID: data.orderID,
            }),
        });

        const details = await response.json();

        // Show success message to buyer
        alert(`Transaction completed by ${details.payer.name.given_name}`);
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons createOrder={createOrder} onApprove={onApprove} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        async createOrder() {
          const response = await fetch("/my-server/create-paypal-order", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              cart: [
                {
                  sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
                  quantity: "YOUR_PRODUCT_QUANTITY",
                },
              ],
            }),
          });

          const data = await response.json();

          return data.id;
        },
        async onApprove(data) {
          // Capture the funds from the transaction.
          const response = await fetch("/my-server/capture-paypal-order", {
            method: "POST",
            body: JSON.stringify({
              orderID: data.orderID,
            }),
          });

          const details = await response.json();

          // Show success message to buyer
          alert(`Transaction completed by ${details.payer.name.given_name}`);
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

For the list of order details you receive from /my-server/capture-paypal-order , see [capture payment for order](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) in the Orders API reference.

### onCancel

When a buyer cancels a payment, they typically return to the parent page. You can instead use the onCancel function to show a cancellation page or return to the shopping cart.

#### Data attributes

orderID : The ID of the order.

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    onCancel(data) {
      // Show a cancel page, or return to cart
      window.location.assign("/your-cancel-page");
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "MY_CLIENT_ID",
  };

  const onCancel = (data) => {
    // Show a cancel page, or return to cart
    window.location.assign("/your-cancel-page");
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onCancel={onCancel} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onCancel: PayPalButtonsComponentProps["onCancel"] = (data) => {
        // Show a cancel page, or return to cart
        window.location.assign("/your-cancel-page");
    }

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onCancel={onCancel} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        onCancel(data) {
          // Show a cancel page, or return to cart
          window.location.assign("/your-cancel-page");
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### onError

If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the onError callback:

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    onError(err) {
      // For example, redirect to a specific error page
      window.location.assign("/your-error-page-here");
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "MY_CLIENT_ID",
  };

  const onError = (err) => {
    // For example, redirect to a specific error page
    window.location.assign("/your-error-page-here");
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onError={onError} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onError: PayPalButtonsComponentProps["onError"] = (err) => {
        // For example, redirect to a specific error page
        window.location.assign("/your-error-page-here");
    }

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onError={onError} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        onError(error) {
          // For example, redirect to a specific error page
          window.location.assign("/your-error-page-here");
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

**info**
**Note:** This error handler is a catch-all. Errors at this point aren't expected to be handled beyond showing a generic error message or page.

### onInit/onClick

Called when the button first renders. You can use it for validations on your page if you are unable to do so prior to rendering. For example, enable buttons when form validation passes or disable if it fails.

#### Data attributes

fundingSource : The funding source of the button that was selected. See the funding sources in the [standalone buttons](https://developer.paypal.com/docs/checkout/standard/customize/standalone-buttons/) guide.

#### **`Vanilla JS`**

```javascript

<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </head>
    <body>
        <p id="error" class="hidden">Click the checkbox</p>
        <label><input id="check" type="checkbox" required /> Click here to continue</label>

        <div id="paypal-button-container"></div>

        <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons"></script>

        <script>
            paypal.Buttons({
                // onInit is called when the button first renders
                onInit(data, actions) {
                    // Disable the buttons
                    actions.disable();

                    // Listen for changes to the checkbox
                    document.querySelector("#check").addEventListener("change", function (event) {
                        // Enable or disable the button when it is checked or unchecked
                        if (event.target.checked) {
                            actions.enable();
                        } else {
                            actions.disable();
                        }
                    });
                },

                // onClick is called when the button is selected
                onClick() {
                    // Show a validation error if the checkbox isn't checked
                    if (!document.querySelector("#check").checked) {
                        document.querySelector("#error").classList.remove("hidden");
                    }
                },
            }).render("#paypal-button-container");
        </script>
    </body>
</html>

```

#### **`React (JS)`**

```javascript
import { useState } from "react";
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const [showError, setShowError] = useState(false);
  const [isCheckboxChecked, setIsCheckboxChecked] = useState(false);

  const checkboxChangeHandler = () => {
    setIsCheckboxChecked(!isCheckboxChecked);
  };

  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  // onInit is called when the buttons first render
  const onInit = (data, actions) => {
    /**
     * NOTE: With react-paypal-js, use the disabled prop in the
     * PayPalButtons component instead of actions.disable()
     */
  };

  // onClick is called when a button is selected
  const onClick = () => {
    //  Show a validation error if the checkbox isn't checked
    if (!isCheckboxChecked) setShowError(true);
  };

  return (
    <div className="App">
      {showError && <p>Click the checkbox</p>}
      <label>
        <input type="checkbox" onChange={checkboxChangeHandler} />
        Click here to continue
      </label>

      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons
          onInit={onInit}
          onClick={onClick}
          disabled={!isCheckboxChecked}
        />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import { useState } from "react";
import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const [showError, setShowError] = useState(false);
    const [isCheckboxChecked, setIsCheckboxChecked] = useState(false);

    const checkboxChangeHandler = () => {
        setIsCheckboxChecked(!isCheckboxChecked);
    };

    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    // onInit is called when the buttons first render
    const onInit: PayPalButtonsComponentProps["onInit"] = (data, actions) => {
        /**
         * NOTE: With react-paypal-js, use the disabled prop in the
         * PayPalButtons component instead of actions.disable()
         */
    };

    // onClick is called when a button is selected
    const onClick: PayPalButtonsComponentProps["onClick"] = () => {
        //  Show a validation error if the checkbox isn't checked
        if (!isCheckboxChecked) setShowError(true);
    };

    return (
        <div className="App">
            {showError && <p>Click the checkbox</p>}
            <label>
                <input type="checkbox" onChange={checkboxChangeHandler} />
                Click here to continue
            </label>

            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onInit={onInit} onClick={onClick} disabled={!isCheckboxChecked} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;
const checkbox = document.querySelector("#check");
const errorMessage = document.querySelector("#error");

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        // onInit is called when the buttons first render
        onInit(data, actions) {
          // Disable the buttons
          actions.disable();

          // Listen for changes to the checkbox
          checkbox.addEventListener("change", function (event) {
            // Enable or disable the button when it is checked or unchecked
            if (event.target.checked) {
              actions.enable();
            } else {
              actions.disable();
            }
          });
        },

        // onClick is called when a button is selected
        onClick() {
          // Show a validation error if the checkbox isn't checked
          if (!checkbox.checked) {
            errorMessage.classList.remove("hidden");
          }
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

For cases when you need asynchronous validation, see [asynchronous validation](/docs/checkout/standard/customize/validate-user-input/#asynchronous-validation) .

### paypal.Buttons().isEligible

Commonly used for [standalone buttons](https://developer.paypal.com/docs/checkout/standard/customize/standalone-buttons/) when you need to check if the funding source is eligible.

#### **`Vanilla JS`**

```javascript
// Loop over each funding source / payment method
paypal.getFundingSources().forEach(function (fundingSource) {
  // Initialize the buttons
  const button = paypal.Buttons({
    fundingSource: fundingSource,
  });

  // Check if the button is eligible
  if (button.isEligible()) {
    // Render the standalone button for that funding source
    button.render("#paypal-button-container");
  }
});
```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;
try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    // Loop over each funding source / payment method
    paypal.getFundingSources().forEach(function (fundingSource) {
      // Initialize the buttons
      const button = paypal.Buttons({
        fundingSource: fundingSource,
      });

      // Check if the button is eligible
      if (button.isEligible()) {
        // Render the standalone button for that funding source
        button.render("#paypal-button-container");
      }
    });
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### paypal.Buttons().render( container )

Renders the buttons in the defined container selector.

#### **`Vanilla JS`**

```javascript
paypal.Buttons().render("#paypal-buttons-container");
```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;
try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal.Buttons().render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### onShippingChange

**Deprecated** . See [onShippingAddressChange](/sdk/js/reference/#on-shipping-address-change) and [onShippingOptionsChange](/sdk/js/reference/#on-shipping-options-change) .

While the buyer is on the PayPal site, you can update their shopping cart to reflect the shipping address they selected on PayPal. You can use the callback to:

- Validate that you support the shipping address.
- Update shipping costs.
- Change the line items in the cart.
- Inform the buyer that you don't support their shipping address.

**Availability:** The onShippingChange function isn't compatible with Subscriptions.

#### Data attributes

data : An object containing the buyer’s shipping address. Consists of the following fields:

- orderID (required): An ID that represents an order.
- paymentID (optional): An ID that represents a payment.
- paymentToken (required): An ID or token that represents the resource.
- shipping_address (required): The buyer's selected city, state, country, and postal code. - city : Shipping address city.
- state : Shipping address state or province.
- country_code : Shipping address country.
- postal_code : Shipping address ZIP code or postal code.

- selected_shipping_option (optional): Shipping option selected by the buyer. - label : Custom shipping method label.
- type : Shipping method type ( SHIPPING or PICKUP ).
- amount : Additional cost for this method. - currency_code : ISO currency code, such as USD .
- value : String-formatted decimal format, such as 1.00 .

#### Actions

actions : An object containing methods to update the contents of the buyer’s cart and interact with PayPal Checkout. Consists of the following methods:

- resolve : Indicates to PayPal that you don't need to make any changes to the buyer’s cart.
- reject : Indicates to PayPal that you won't support the shipping address provided by the buyer.
- order : Client-side order API method. - PATCH : To make the update, pass an array of change operations in the request, as described in the [order update](https://developer.paypal.com/docs/api/orders/v2/) API reference. The response returns a promise.

#### Examples

- This example shows not supporting international transactions:

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    onShippingChange(data, actions) {
      if (data.shipping_address.country_code !== "US") {
        return actions.reject();
      }

      return actions.resolve();
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const onShippingChange = (data, actions) => {
    if (data.shipping_address.country_code !== "US") {
      return actions.reject();
    }

    return actions.resolve();
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onShippingChange={onShippingChange} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onShippingChange: PayPalButtonsComponentProps["onShippingChange"] = (data, actions) => {
        if (data.shipping_address?.country_code !== "US") {
            return actions.reject();
        }

        return actions.resolve();
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onShippingChange={onShippingChange} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        onShippingChange(data, actions) {
          if (data.shipping_address.country_code !== "US") {
            return actions.reject();
          }

          return actions.resolve();
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

- This example shows a more complex situation in which a state has free shipping, but flat-rate shipping is the standard for the rest of the US:

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    async onShippingChange(data, actions) {
      // Reject non-US addresses
      if (data.shipping_address.country_code !== "US") {
        return actions.reject();
      }

      // Patch the shipping amount
      const response = await fetch("/my-server/patch-paypal-order", {
        method: "PATCH",
        body: JSON.stringify({
          shippingAddress: data.shipping_address,
        }),
      });
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const onShippingChange = async (data, actions) => {
    // Reject non-US addresses
    if (data.shipping_address.country_code !== "US") {
      return actions.reject();
    }

    // Patch the shipping amount
    const response = await fetch("/my-server/patch-paypal-order", {
      method: "PATCH",
      body: JSON.stringify({
        shippingAddress: data.shipping_address,
      }),
    });
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onShippingChange={onShippingChange} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onShippingChange: PayPalButtonsComponentProps["onShippingChange"] = async (data, actions) => {
        // Reject non-US addresses
        if (data.shipping_address?.country_code !== 'US') {
            return actions.reject();
        }

        // Patch the shipping amount
        const response = await fetch("/my-server/patch-paypal-order", {
            method: "PATCH",
            body: JSON.stringify(
            {
                shippingAddress: data.shipping_address
            })
        })
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onShippingChange={onShippingChange} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        async onShippingChange(data, actions) {
          // Reject non-US addresses
          if (data.shipping_address.country_code !== "US") {
            return actions.reject();
          }

          // Patch the shipping amount
          const response = await fetch("/my-server/patch-paypal-order", {
            method: "PATCH",
            body: JSON.stringify({
              shippingAddress: data.shipping_address,
            }),
          });
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### onShippingAddressChange

While the buyer is on the PayPal site, you can update their shopping cart to reflect the shipping address they selected on PayPal. You can use the callback to:

- Validate that you support the shipping address.
- Update shipping costs.
- Change the line items in the cart.
- Inform the buyer that you don't support their shipping address.

**Availability:** The onShippingAddressChange function isn't compatible with Subscriptions.

#### Data attributes

data : An object containing the buyer’s shipping address. Consists of the following properties:

- errors : Errors to show to the user. - ADDRESS_ERROR : "Your order can't be shipped to this address."
- COUNTRY_ERROR : "Your order can't be shipped to this country."
- STATE_ERROR : "Your order can't be shipped to this state."
- ZIP_ERROR : "Your order can't be shipped to this zip."

- orderID : An ID that represents an order.
- paymentID : An ID that represents a payment.
- paymentToken : An ID or token that represents a resource.
- shippingAddress : The buyer's selected city, state, country, and postal code. - city : Shipping address city.
- countryCode : Shipping address country.
- postalCode : Shipping address ZIP code or postal code.
- state : Shipping address state or province.

#### Actions

actions : An object containing a method to interact with PayPal Checkout. Consists of the following property:

#### **`Javascript`**

```javascript
* `reject`: Indicates to PayPal that you won't support the shipping address provided by the buyer.
```

#### Examples

- This example shows how to reject international transactions using actions.reject() :

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    onShippingAddressChange(data, actions) {
      if (data.shippingAddress.countryCode !== "US") {
        return actions.reject(data.errors.COUNTRY_ERROR);
      }
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const onShippingAddressChange = (data, actions) => {
    if (data.shippingAddress.countryCode !== "US") {
      return actions.reject(data.errors.COUNTRY_ERROR);
    }
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onShippingAddressChange={onShippingAddressChange} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onShippingAddressChange: PayPalButtonsComponentProps["onShippingAddressChange"] = (data, actions) => {
        if (data.shippingAddress.countryCode !== "US") {
              return actions.reject(data.errors?.COUNTRY_ERROR);
        }
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onShippingAddressChange={onShippingAddressChange} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        onShippingAddressChange(data, actions) {
          if (data.shippingAddress.countryCode !== "US") {
            return actions.reject(data.errors.COUNTRY_ERROR);
          }
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

### onShippingOptionsChange

This callback is triggered any time the user selects a new shipping option. You can use the callback to:

- Validate that you support the shipping method.
- Update shipping costs.
- Change the line items in the cart.
- Inform the buyer that you don't support their shipping method.

**Availability:** The onShippingOptionsChange function isn't compatible with Subscriptions.

#### Data attributes

data : An object containing the payer’s selected shipping option. Consists of the following properties:

- errors : Errors to show to the payer. - METHOD_UNAVAILABLE : "The shipping method you selected is unavailable. To continue, choose another way to get your order."
- STORE_UNAVAILABLE : "Part of your order isn't available at this store."

- orderID : An ID that represents an order.
- paymentID : An ID that represents a payment.
- paymentToken : An ID or token that represents a resource.
- selectedShippingOption : Shipping option selected by the payer. - id : Custom shipping method ID.
- label : Custom shipping method label.
- selected : Set to true by PayPal when selected by the buyer.
- type : Shipping method type ( SHIPPING or PICKUP ).
- amount : Additional cost for this method. - currencyCode : ISO currency code, such as USD .
- value : String-formatted decimal format, such as 1.00 .

#### Actions

actions : An object containing a method to interact with PayPal Checkout. Consists of the following property:

#### **`Javascript`**

```javascript
* `reject`: Indicates to PayPal that you won't support the shipping method selected by the buyer.
```

#### Customize shipping options

Add support for [multiple shipping options](/docs/checkout/standard/customize/shipping-options/) when buyers make changes to their shipping information.

#### Examples

- This example shows how to disable store pickup using actions.reject() :

#### **`Vanilla JS`**

```javascript
paypal
  .Buttons({
    onShippingOptionsChange(data, actions) {
      if (data.selectedShippingOption.type === "PICKUP") {
        return actions.reject(data.errors.STORE_UNAVAILABLE);
      }
    },
  })
  .render("#paypal-button-container");
```

#### **`React (JS)`**

```javascript
import { PayPalButtons, PayPalScriptProvider } from "@paypal/react-paypal-js";

export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
  };

  const onShippingOptionsChange = (data, actions) => {
    if (data.selectedShippingOption.type === "PICKUP") {
      return actions.reject(data.errors.STORE_UNAVAILABLE);
    }
  };

  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons onShippingOptionsChange={onShippingOptionsChange} />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`React (TS)`**

```javascript

import {
    PayPalButtons,
    PayPalButtonsComponentProps,
    PayPalScriptProvider,
    ReactPayPalScriptOptions,
} from "@paypal/react-paypal-js";

export default function App() {
    const initialOptions: ReactPayPalScriptOptions = {
        clientId: "YOUR_CLIENT_ID",
    };

    const onShippingOptionsChange: PayPalButtonsComponentProps["onShippingOptionsChange"] = (data, actions) => {
        if (data.selectedShippingOption.type === 'PICKUP') {
            return actions.reject(data.errors?.STORE_UNAVAILABLE);
        }
    };

    return (
        <div className="App">
            <PayPalScriptProvider options={initialOptions}>
                <PayPalButtons onShippingOptionsChange={onShippingOptionsChange} />
            </PayPalScriptProvider>
        </div>
    );
}

```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";

let paypal;

try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}

if (paypal) {
  try {
    await paypal
      .Buttons({
        onShippingOptionsChange(data, actions) {
          if (data.selectedShippingOption.type === "PICKUP") {
            return actions.reject(data.errors?.STORE_UNAVAILABLE);
          }
        },
      })
      .render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

Use marks when the PayPal buttons are presented alongside other funding sources on the page and the PayPal buttons are shown when the buyer selects a radio button. See [Display other payment methods](https://developer.paypal.com/docs/checkout/standard/customize/display-payment-methods/) .

#### **`Marks`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,marks"></script>
```

### paypal.Marks(options)

- [paypal.Marks().isEligible](/sdk/js/reference/#paypal-marks-iseligible)
- [paypal.Marks().render( container )](/sdk/js/reference/#link-paypalmarksrendercontainer)

#### paypal.Marks().isEligible

#### **`paypal.Marks().isEligible`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,funding-eligibility,marks"></script>
```

Commonly used for [standalone buttons](https://developer.paypal.com/docs/checkout/standard/customize/standalone-buttons/) when you need to check if the funding source is eligible.

#### **`paypal.Marks().isEligible 2`**

```javascript
// Loop over each funding source / payment method
paypal.getFundingSources().forEach(function (fundingSource) {
  // Initialize the marks
  var mark = paypal.Marks({
    fundingSource: fundingSource,
  });

  // Check if the mark is eligible
  if (mark.isEligible()) {
    // Render the standalone mark for that funding source
    mark.render("#paypal-mark-container");
  }
});
```

#### paypal.Marks().render( container )

Renders the radio buttons that are passed in container selector.

#### **`paypal.Marks().render( container )`**

```javascript
paypal.Marks().render("#paypal-marks-container");
```

#### **`paypal.Marks().render( container ) 2 `**

```javascript
<!-- Render the radio buttons and marks -->
<label>
  <input type="radio" name="payment-option" value="paypal" checked>
  <div id="paypal-marks-container"></div>
</label>

<label>
  <input type="radio" name="payment-option" value="alternate">
</label>

<div id="paypal-buttons-container"></div>
<div id="alternate-button-container">
  <button>Pay with a different method</button>
</div>

<script>
  // Render the PayPal marks
  paypal.Marks().render('#paypal-marks-container');

  // Render the PayPal buttons
  paypal.Buttons().render('#paypal-buttons-container');

  // Listen for changes to the radio buttons
  document.querySelectorAll('input[name=payment-option]')
    .forEach(function (el) {
      el.addEventListener('change', function (event) {

        // If PayPal is selected, show the PayPal button
        if (event.target.value === 'paypal') {
          document.body.querySelector('#alternate-button-container')
            .style.display = 'none';
          document.body.querySelector('#paypal-buttons-container')
            .style.display = 'block';
        }

        // If alternate funding is selected, show a different button
        if (event.target.value === 'alternate') {
          document.body.querySelector('#alternate-button-container')
            .style.display = 'block';
          document.body.querySelector('#paypal-buttons-container')
            .style.display = 'none';
        }
      });
    });

  // Hide non-PayPal button by default
  document.body.querySelector('#alternate-button-container')
    .style.display = 'none';
</script>
```

Use PayPal-hosted card fields to accept and save credit and debit cards without handling card information. PayPal handles all security and compliance issues associated with processing cards.

### Request: Initialize cardFields

Initialize the card fields component by creating an instance of paypal.CardFields :

#### **`Request: Initialize cardFields`**

```javascript
const cardFields = paypal.CardFields({
  style,
  createOrder,
  onApprove,
});
```

#### Options

You can pass the following options when instantiating the card fields component:

| Option                                         | Description                                        | Required |
| ---------------------------------------------- | -------------------------------------------------- | -------- |
| [createOrder](/sdk/js/reference/#create-order) | The callback to create the order on your server.   | Yes      |
| [onApprove](/sdk/js/reference/#on-approve)     | The callback to capture the order on your server.  | Yes      |
| [onError](/sdk/js/reference/#link-onerror)     | The callback to catch errors during checkout.      | Yes      |
| [inputEvents](/sdk/js/reference/#input-events) | An object containing callbacks for an input event. | No       |
| style                                          | A custom style object.                             | No       |

#### createOrder

Creates an order ID for any case involving a purchase. This callback is called whenever the payer submits card fields.

#### Request: Create order from server

#### **`Request: Create order from server`**

```javascript
const createOrder = (data, actions) => {
  return fetch("/api/paypal/order", {
    method: "POST",
  })
    .then((res) => {
      return res.json();
    })
    .then((json) => {
      return json.orderID;
    });
};
```

Set up your server to call the [Create Order API](https://developer.paypal.com/docs/api/orders/v2/#orders_create) . The button pressed on the client side determines the payment source sent. In the following sample, the payer opted to send their card as a payment source.

#### Request: Create order with a card as the payment source

#### **`Request`**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \n -H "Content-Type: application/json" \n -H "Authorization: Bearer ACCESS-TOKEN" \n -d '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "amount": {
                "currency_code": "USD",
                "value": "100.00"
            }
        }
    ],
}
```

#### Response

Pass the order.id to the JavaScript SDK to update the order with the number, CVV, and expiration date entered.

#### **`Javascript`**

```javascript

  {
      "id": "5O190127TN364715T",
      "status": "CREATED",
      "intent": "CAPTURE",
      "purchase_units": [
          {
              "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
              "amount": {
                  "currency_code": "USD",
                  "value": "100.00"
              }
          }
      ],
      "create_time": "2022-10-03T11:18:49Z",
      "links": [
          {
              "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
              "rel": "self",
              "method": "GET"
          },
          {
              "href": "https://www.paypal.com/checkoutnow?token=5O190127TN364715T",
              "rel": "approve",
              "method": "GET"
          },
          {
              "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
              "rel": "update",
              "method": "PATCH"
          },
          {
              "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T/capture",
              "rel": "capture",
              "method": "POST"
          }
      ]
  }

```

#### onApprove

Signals that a payer approved a purchase by submitting a card or selecting a button.

#### Request: Capture order from server

Set up your server to call the [Capture Order API](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) , then run the following script to capture an order from your server:

#### **`Request`**

```javascript
const onApprove = (data, actions) => {
  return fetch("/api/paypal/order/capture", {
    method: "POST",
    body: JSON.stringify({
      orderID: data.orderID,
    }),
  })
    .then((res) => {
      return res.json();
    })
    .then((json) => {
      // Show a success page
    });
};
```

#### Request

#### **`onApprove`**

```javascript

curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/<order_id>/capture
 -H "Content-Type: application/json"
 -H "Authorization: Bearer ACCESS-TOKEN"
```

#### Response

#### **`onApprove`**

```javascript

{
  "id": "some_id",
  "status": "COMPLETED",
  "payment_source": {
    "card": {
      "brand": "VISA",
      "last_digits": "1111",
      "type": "CREDIT"
    }
  },
  "purchase_units": [
    {
      "reference_id": "reference_id",
      "payments": {
        "authorizations": [
          {
            "id": "id",
            "status": "CREATED",
            "amount": {
              "currency_code": "USD",
              "value": "100.00"
            },
            "seller_protection": {
              "status": "ELIGIBLE",
              "dispute_categories": [
                "ITEM_NOT_RECEIVED",
                "UNAUTHORIZED_TRANSACTION"
              ]
            },
            "expiration_time": "2022-10-04T14:37:39Z",
            "links": [
              {
                "href": "https://api-m.paypal.com/v2/payments/authorizations/5O190127TN364715T",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.paypal.com/v2/payments/authorizations/5O190127TN364715T/capture",
                "rel": "capture",
                "method": "POST"
              },
              {
                "href": "https://api-m.paypal.com/v2/payments/authorizations/5O190127TN364715T/void",
                "rel": "void",
                "method": "POST"
              },
              {
                "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "up",
                "method": "GET"
              }
            ]
          }
        ]
      }
    }
  ],
  "payer": {
    "name": {
      "given_name": "Firstname",
      "surname": "Lastname"
    },
    "email_address": "payer@example.com",
    "payer_id": "QYR5Z8XDVJNXQ"
  },
  "links": [
    {
      "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
      "rel": "self",
      "method": "GET"
    }
  ]
}

```

#### onError

Handles any errors that occur while the payer submits the form.

#### **`onError`**

```javascript
const cardFields = paypal.CardFields({
    // ...
    onError = (error) => {
        // Handle the error object
        console.error(error);
    },
    // ...
});
```

#### onCancel

For 3D Secure usecases, you can choose what to present to the customer if they close the verification modal. This will also mean the transaction was cancelled.

#### **`onCancel`**

```javascript

const cardFields = paypal.CardFields({
    // ...
    onCancel = () => {
        console.log("Your order was cancelled due to incomplete verification");
    },
    // ...
});

```

### Card field properties

The following card field properties are used to capture a payment. Use the render() method to render these instances to the DOM.

| Property    | Type     | Field created                        | Required |
| ----------- | -------- | ------------------------------------ | -------- |
| CVVField    | Function | Card CVV or CID, a 3 or 4-digit code | Yes      |
| ExpiryField | Function | Card expiration date                 | Yes      |
| NameField   | Function | Name for the card                    | No       |
| NumberField | Function | Card number                          | Yes      |

#### Card field options

Customize event callbacks or the style of each field with the following options:

| Property    | Type               | Description                                                                                       | Required |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------- | -------- |
| inputEvents | Object inputEvents | An object containing callbacks for when a specified input event occurs for a field.               | No       |
| style       | Object style guide | Style a field with supported CSS properties.                                                      | No       |
| placeholder | String             | Each card field has a default placeholder text. Pass a placeholder object to customize this text. | No       |

#### Example: Card field properties

#### **`Example: Card field properties`**

```javascript
const cardNameContainer = document.getElementById("card-name-field-container");
const nameField = cardField.NameField({
  placeholder: "Enter your full name as it appears on your card",
inputEvents: {
    onChange: (event)=> {
        console.log("returns a stateObject", event);
    }
},
style: {
    ".invalid": {
        "color": "purple",
    }
}
});
  });
nameField.render(cardNameContainer);
const cardNumberContainer = document.getElementById("card-number-field-container");
const numberField = cardField.NumberField(/*options*/);
numberField.render(cardNumberContainer);
const cardExpiryContainer = document.getElementById("card-expiry-field-container");
const expiryField = cardField.ExpiryField(/*options*/);
expiryField.render(cardExpiryContainer);
const cardCvvContainer = document.getElementById("card-cvv-field-container");
const cvvField = cardField.CVVField(/*options*/);
cvvField.render(cardCvvContainer);
```

### Style card fields

Change the layout, width, height, and outer styling of the card fields. Modify the elements you supply as containers with your current stylesheets. For example, input: { border: 1px solid #333; } .

#### Supported CSS properties

The CSS properties listed are the only properties supported in the advanced credit and debit card payments configuration. If you specify an unsupported CSS property, a warning is logged to the browser console.

- appearance
- color
- direction
- font
- font-family
- font-size
- font-size-adjust
- font-stretch
- font-style
- font-variant
- font-variant-alternates
- font-variant-caps
- font-variant-east-asian
- font-variant-ligatures
- font-variant-numeric
- font-weight
- letter-spacing
- line-height
- opacity
- outline
- padding
- padding-bottom
- padding-left
- padding-right
- padding-top
- text-shadow
- transition
- -moz-appearance
- -moz-osx-font-smoothing
- -moz-tap-highlight-color
- -moz-transition
- -webkit-appearance
- -webkit-osx-font-smoothing
- -webkit-tap-highlight-color
- -webkit-transition

### Style parent fields

Pass a style object to the parent cardField component to apply the object to every field.

#### **`Style parent fields`**

```javascript
const cardStyle = {
  input: {
    "font-size": "16px",
    "font-family": "courier, monospace",
    "font-weight": "lighter",
    color: "#ccc",
  },
  ".invalid": {
    color: "purple",
  },
};
const cardField = paypal.CardFields({
  style: cardStyle,
});
```

#### Style individual fields

Pass a style object to an individual card field to apply the object to that field only. This overrides any object passed through a parent component.

#### **`Style individual fields`**

```javascript

const nameFieldStyle = {
    'input': {
        'color': 'blue'
    }
    '.invalid': {
        'color': 'purple'
    },
};
const nameField = cardField.NameField({
    style: nameFieldStyle
}).render('#card-name-field-container');

```

### inputEvents

You can pass an inputEvents object into a parent cardField component or each card field individually.

Pass an inputEvents object to the parent cardField component to apply the object to every field.

Pass an inputEvents object to an individual card field to apply the object to that field only. This overrides any object passed through a parent component.

#### Supported input event callbacks

You can pass the following callbacks to the inputEvents object:

| Event Name           | Description                                 |
| -------------------- | ------------------------------------------- |
| onChange             | Called when the input in any field changes. |
| onFocus              | Called when any field gets focus.           |
| onBlur               | Called when any field loses focus.          |
| onInputSubmitRequest | Called when a payer submits the field.      |

#### Example: inputEvents into parent component

Pass the inputEvents object into the parent CardFields component.

#### **`Example: inputEvents into parent component`**

```javascript
const cardField = paypal.CardFields({
    inputEvents: {
        onChange: function(data) => {
            // Do something when an input changes
        },
        onFocus: function(data) => {
            // Do something when a field gets focus
        },
        onBlur: function(data) => {
            // Do something when a field loses focus
        }
        onInputSubmitRequest: function(data) => {
            if (data.isFormValid) {
                // Submit the card form for the payer
            } else {
                // Inform payer that some fields aren't valid
            }
        }
    }
})
```

#### Example: inputEvents into individual component

Pass the inputEvents object into each individual field component:

#### **`inputEvents into individual component`**

```javascript

const cardField = paypal.CardFields(/* options */)
const nameField = cardField.NameField({
       inputEvents: {
        onChange: function(data) => {
            // Do something when the input of only the name field changes
        },
        onFocus: function(data) => {
            // Do something when only the name field gets focus
        },
        onBlur: function(data) => {
            // Do something when only name field loses focus
        }
        onInputSubmitRequest: function(data) => {
            if (data.isFormValid) {
                // Submit the card form for the payer
            } else {
                // Inform payer that some fields aren't valid
            }
        }
    }
});

```

#### sample-state-object

Each of the event callbacks returns a state object similar to the following example:

#### **`Sample state object`**

```javascript
data: {
    cards: [{code: {name: 'CVV', size: 3}, niceType: "Visa", type: "visa"}]
    emittedBy: "number", // Not returned for getState()
    isFormValid: false,
    errors: ["INVALID_CVV"]
    fields: {
        cardCvvField: {
            isFocused: false,
            isEmpty: true,
            isValid: false,
            isPotentiallyValid: true,
        },
        cardNumberField: {
            isFocused: true,
            isEmpty: false,
            isValid: false,
            isPotentiallyValid: true,
        },
        cardNameField: {
            isFocused: false,
            isEmpty: true,
            isValid: false,
            isPotentiallyValid: true,
        },
        cardExpiryField: {
            isFocused: false,
            isEmpty: true,
            isValid: false,
            isPotentiallyValid: true,
        },
    },
}
```

#### Validate individual fields

Validate individual fields when an input event occurs:

#### **`Validate individual fields`**

```javascript
const cardFields = paypal.CardFields({
  /* options */
});
let cardContainer = document.getElementById("#card-number-field-container");
const cardNumberField = cardFields.NumberField({
  // Add valid or invalid class when the validation changes on the field
  inputEvents: {
    onChange: (data) => {
      cardContainer.className =
        data.fields.cardNumberField.isValid ? "valid" : "invalid";
    },
  },
});
```

### Validate entire card form&lt;

Validate an entire card form when an input event occurs:

#### **`Validate entire card form`**

```javascript
const formContainer = document.getElementById("form-container");
const cardFields = paypal.CardFields({
  inputEvents: {
    onChange: (data) => {
      formContainer.className = data.isFormValid ? "valid" : "invalid";
    },
  },
});
```

### Methods on parent card fields

The following methods are supported on parent card fields:

- getState()
- isEligible()
- submit()

#### getState() -&gt; {promise | void}

Returns a promise that resolves into a stateObject . Includes the state of all fields, possible card types, and an array of errors.

#### Example

#### **`getState() -> {promise | void}`**

```javascript
const cardField = paypal.CardFields(/* options */);
// ...
// Render the card fields
// ...
cardFields.getState().then((data) => {
  // Submit only if the current
  // state of the form is valid
  if (data.isFormValid) {
    cardFields
      .submit()
      .then(() => {
        //Submit success
      })
      .catch((error) => {
        //Submit error
      });
  }
});
```

#### &gt;isEligible() -&gt; {Boolean}

Checks if a cardField instance can render based on configuration and business rules.

#### Example

#### **`isEligible() -> {Boolean}`**

```javascript
const cardField = paypal.CardFields(/* options */);
if (cardFields.isEligible()) {
  cardFields.NumberField().render("#card-number-field-container");
  cardFields.CVVField().render("#card-cvv-field-container");
  // ...
}
```

### submit() -&gt; {promise | void}

Submits payment information.

#### **`submit() -> {promise | void}`**

```javascript
// Add click listener to merchant-supplied submit button
// and call the submit function on the CardField component
multiCardFieldButton.addEventListener("click", () => {
  cardField
    .submit()
    .then(() => {
      console.log("Card Fields submit");
    })
    .catch((err) => {
      console.log("There was an error with card fields: ", err);
    });
});
```

### Methods on individual card fields

The following methods are supported on individual card fields:

- addClass()
- clear()
- focus()
- removeAttribute()
- removeClass()
- render()
- setAttribute()
- setMessage()
- close()

| Method                           | Description                                                                               |
| -------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addClass() -&gt; {promise        | void}                                                                                     | Adds a class to a field. Use this method to update field styles when events occur elsewhere during checkout.                                                            |
| clear() -&gt; {void}             | Clears the value of the field.                                                            |
| focus() -&gt; {void}             | Focuses the field.                                                                        |
| removeAttribute() -&gt; {promise | void}                                                                                     | Removes an attribute from a field where called You can remove the following attributes with removeAttribute: - aria-invalid - aria-required - disabled - placeholder    |
| removeClass() -&gt; {promise     | void}                                                                                     | Pass the class name as a string in removeClass to remove a class from a field. Use this method to update field styles when events occur elsewhere in the checkout flow. |
| render() -&gt; {promise          | void}                                                                                     | Renders the individual card fields to the DOM for checkout. Pass the HTML element reference or CSS selector string for the input field.                                 |
| setAttribute() -&gt; {promise    | void}                                                                                     | Sets the supported attributes and values of a field. Pass in attributes and values as strings.                                                                          |
| setMessage() -&gt; {void}        | Sets a message on a field for screen readers. Pass the message as a string in setMessage. |

#### **`addClass()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const numberField = cardField.NumberField(/* options */);
numberField.addClass("purple");
numberField.render(cardNumberContainer);
```

#### **`clear()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const nameField = cardField.NameField(/* options */);
nameField.render(cardNameContainer);
nameField.clear();
```

#### **`focus()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const nameField = cardField.NameField(/* options */);
nameField.render(cardNameContainer);
nameField.focus();
```

#### **`removeAttribute()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const numberField = cardField.NumberField(/* options */);
numberField.render(cardNumberContainer);
numberField.removeAttribute("placeholder");
```

#### **`removeClass()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const numberField = cardField.NumberField(/* options */);
numberField.render(cardNumberContainer);
numberField.removeClass("purple");
```

#### **`render() `**

```javascript
const cardNumberContainer = document.getElementById(
  "card-number-field-container",
);
const cardField = paypal.CardFields(/* options */);
cardField.NumberField(/* options */).render(cardNumberContainer);
// OR use a selector string
cardField.NumberField(/*options*/).render("#card-number-field-container");
```

#### **`setAttribute() `**

```javascript
const cardField = paypal.CardFields(/* options */);
const nameField = cardField.NameField(/* options */);
nameField.setAttribute("placeholder", "Enter your full name");
nameField.render(cardNameContainer);
```

#### **`setMessage()`**

```javascript
const cardField = paypal.CardFields(/* options */);
const nameField = cardField.NameField(/* options */);
nameField.render(cardNameContainer);
nameField.setMessage("Enter your full name");
```

### Type definitions

- [cardSecurityCode](/sdk/js/reference/#cardsecuritycode)
- [cardType](/sdk/js/reference/#cardtype)
- [cardFieldData](/sdk/js/reference/#cardfielddata)
- [stateObject](/sdk/js/reference/#stateobject)

#### cardSecurityCode

Information about the security code for a card.

| Property | Type   | Description                                                              |
| -------- | ------ | ------------------------------------------------------------------------ |
| name     | String | The name of a security code for a card. Valid values areCVV,CID, andCVC. |
| size     | Number | The expected length of the security code, typically3or4digits.           |

#### cardType

Information about the card type sent in the cards array as a part of the [stateObject](https://developer.paypal.com/sdk/js/reference/#link-stateobject) .

| Property | Type   | Description                                                      |
| -------- | ------ | ---------------------------------------------------------------- |
| type     | String | The code-readable card type. Valid values are:- american-express |

- diners-club
- discover
- jcb
- maestro
- mastercard
- unionpay
- visa
- elo
- hiper , hipercard |
  | code | ObjectcardSecurityCode | Contains data about the card brand's security code requirements. For example, on a Visa card, the CVV is 3 digits. On an American Express card, the CID is 4 digits. |
  | niceType | String | The human-readable card type. Valid values are:- American Express
- Diner Club
- discover
- JCB
- Maestro
- Mastercard
- UnionPay
- Visa
- Elo
- Hiper , Hipercard |

#### cardFieldData

Field data for card payments is sent for each card field in the [stateObject](https://developer.paypal.com/sdk/js/reference/#link-stateobject) .

| Property           | Type    | Description                                                                                                                                                                                  |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isFocused          | Boolean | Shows whether the input field is currently focused.                                                                                                                                          |
| isEmpty            | Boolean | Shows whether the user has entered a value in the input.                                                                                                                                     |
| isPotentiallyValid | Boolean | Shows whether the current input can be valid. For example, if a payer enters41for the card number, the input can become valid. However, if the payer enters4x, the input can't become valid. |
| isValid            | Boolean | Shows whether the input is valid and can be submitted.                                                                                                                                       |

#### stateObject

| Property    | Type             | Description                                                                                                                                                                                                 |
| ----------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cards       | Array ofcardType | Returns an array of potential cards. If the card type has been determined, the array contains only 1 card.                                                                                                  |
| emittedBy   | String           | The name of the field associated with an event.emittedByisn't included if returned bygetState. Valid values are"name","number","cvv", and"expiry".                                                          |
| errors      | Array            | Array of card fields that are currently not valid. Potential values are"INELIGIBLE_CARD_VENDOR","INVALID_NAME","INVALID_NUMBER","INVALID_EXPIRY"or"INVALID_CVV".                                            |
| isFormValid | Boolean          | Shows whether the form is valid.                                                                                                                                                                            |
| fields      | Object           | Contains data about the field in the context of the event. Valid values are"cardNameField","cardCvvField","cardNumberField"and"cardExpiryField". Each of these keys contain an object of typecardFieldData. |

### Full example

The following sample shows how a full hosted card fields script might show up in HTML:

#### **`Full example`**

```html
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Checkout Page</title>
  </head>
  <body>
    <div id="checkout-form">
      <div id="card-name-field-container"></div>
      <div id="card-number-field-container"></div>
      <div id="card-expiry-field-container"></div>
      <div id="card-cvv-field-container"></div>
      <button id="multi-card-field-button" type="button">
        Pay now with Card Fields
      </button>
    </div>
  </body>
  <script src="https://www.paypal.com/sdk/js?client-id=<your-client-id>&components=card-fields"></script>
  <script>
    // Custom styles object (optional)
    const styleObject = {
      input: {
        "font-size": "16 px",
        "font-family": "monospace",
        "font-weight": "lighter",
        color: "blue",
      },
      ".invalid": {
        color: "purple",
      },
      ":hover": {
        color: "orange",
      },
      ".purple": {
        color: "purple",
      },
    };
    // Create the card fields component and define callbacks
    const cardField = paypal.CardFields({
      style: styleObject,
      createOrder: function (data, actions) {
        return fetch("/api/paypal/order/create/", {
          method: "post",
        })
          .then((res) => {
            return res.json();
          })
          .then((orderData) => {
            return orderData.id;
          });
      },
      onApprove: function (data, actions) {
        const { orderID } = data;
        return fetch("/api/paypal/orders/${orderID}/capture/", {
          method: "post",
        })
          .then((res) => {
            return res.json();
          })
          .then((orderData) => {
            // Redirect to success page
          });
      },
      inputEvents: {
        onChange: function (data) {
          // Handle a change event in any of the fields
        },
        onFocus: function (data) {
          // Handle a focus event in any of the fields
        },
        onBlur: function (data) {
          // Handle a blur event in any of the fields
        },
        onInputSubmitRequest: function (data) {
          // Handle an attempt to submit the entire card form
          // while focusing any of the fields
        },
      },
    });
    // Define the container for each field and the submit button
    const cardNameContainer = document.getElementById(
      "card-name-field-container",
    ); // Optional field
    const cardNumberContainer = document.getElementById(
      "card-number-field-container",
    );
    const cardCvvContainer = document.getElementById(
      "card-cvv-field-container",
    );
    const cardExpiryContainer = document.getElementById(
      "card-expiry-field-container",
    );
    const multiCardFieldButton = document.getElementById(
      "multi-card-field-button",
    );
    // Render each field after checking for eligibility
    if (cardField.isEligible()) {
      const nameField = cardField.NameField();
      nameField.render(cardNameContainer);
      const numberField = cardField.NumberField();
      numberField.render(cardNumberContainer);
      const cvvField = cardField.CVVField();
      cvvField.render(cardCvvContainer);
      const expiryField = cardField.ExpiryField();
      expiryField.render(cardExpiryContainer);
      // Add click listener to the submit button and call the submit function on the CardField component
      multiCardFieldButton.addEventListener("click", () => {
        cardField
          .submit()
          .then(() => {
            // Handle a successful payment
          })
          .catch((err) => {
            // Handle an unsuccessful payment
          });
      });
    }
  </script>
</html>
```

The payment buttons automatically render all eligible buttons in a single location on your page by default.

If your use case permits, you can render individual, standalone buttons for each supported payment method. For example, render the PayPal, Venmo, PayPal Credit, and alternative payment method buttons on different parts of the checkout page, alongside different radio buttons, or on entirely different pages.

Even with standalone buttons, your integrations take advantage of the eligibility logic the PayPal JavaScript SDK provides, meaning only the appropriate buttons for the current buyer automatically show up.

### Paypal.rememberFunding( fundingSources )

When the customer chooses to save a funding source, that source is stored and available to use for future payments.

### paypal.getFundingSources

Loop over funding sources and payment methods.

### paypal.isFundingEligible( fundingSource )

Check for funding eligibility from current funding sources.

#### **`Basic integration`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=funding-eligibility"></script>
```

#### **`paypal.rememberFunding( fundingSources )`**

```javascript
paypal.rememberFunding([paypal.FUNDING.VENMO]);
```

#### **`paypal.getFundingSources`**

```javascript
paypal.getFundingSources().forEach(function (fundingSource) {
  // ...
});
```

#### **`paypal.isFundingEligible( fundingSource )`**

```javascript
paypal.isFundingEligible(fundingSource);
```

## Funding

This table includes the available funding sources. The payment buttons automatically render all eligible buttons in a single location on your page by default. If you need to override this, you can specify the buttons you want to show by following the [Standalone payment buttons](/docs/checkout/standard/customize/standalone-buttons/) guide.

| Funding source             | Payment button         |
| -------------------------- | ---------------------- |
| paypal.FUNDING.PAYPAL      | PayPal                 |
| paypal.FUNDING.CARD        | Credit or debit cards  |
| paypal.FUNDING.CREDIT      | PayPal Credit          |
| paypal.FUNDING.VENMO       | Venmo                  |
| paypal.FUNDING.SEPA        | SEPA-Lastschrift       |
| paypal.FUNDING.BANCONTACT  | Bancontact             |
| paypal.FUNDING.EPS         | eps                    |
| paypal.FUNDING.GIROPAY     | giropay (Legacy)**\*** |
| paypal.FUNDING.IDEAL       | iDEAL                  |
| paypal.FUNDING.MERCADOPAGO | Mercado Pago           |
| paypal.FUNDING.MYBANK      | MyBank                 |
| paypal.FUNDING.P24         | Przelewy24             |
| paypal.FUNDING.SOFORT      | SOFORT (Legacy)**\***  |

**error**
**\*** **Important:** giropay was sunset on June 30, 2024. PayPal will not support giropay payments starting July 1, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/giropay-deprecation-help1183) .

**error**
**\*** **Important:** Sofort was sunset on April 18, 2024. PayPal will not support Sofort payments starting April 19, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/sofort-deprecation-help1145) .

## Messages

Use when you want to show Pay Later messages on your site. Because Pay Later offers differ by country, certain options for the messages component render differently depending on the buyer's location. For complete details, as well as country-specific examples, see Pay Later [Reference](https://developer.paypal.com/docs/checkout/pay-later/us/integrate/reference/) .

## See also

- [JavaScript SDK script configuration](https://developer.paypal.com/sdk/js/configuration/) .
- [Optimize the performance of the JavaScript SDK](https://developer.paypal.com/sdk/js/performance/) .
