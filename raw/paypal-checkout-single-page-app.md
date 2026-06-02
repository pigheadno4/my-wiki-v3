---
title: 'PayPal payments with single-page applications '
slug: /docs/checkout/standard/customize/single-page-app/
createTime: '2024-03-03T22:56:26.663Z'
updateTime: '2025-05-09T11:19:11.251Z'
---

# PayPal payments with single-page applications

Use this guide if your integration uses a single-page application to accept payments, built on a library or framework such as React, Vue, or Angular.

## Know before you code

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

## Script tag placement

Place the following script tag in your `index.html` page based on how you plan to render payment buttons:

**Immediate rendering** (buttons render on page load):

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID">
</script>
```

**On change** (buttons render after user action, navigation, or page change):

```javascript
<script defer src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID">
</script>
```

Use `defer` when rendering buttons after a route change or user interaction — this is the common SPA pattern.

> **Note:** This sample code is optimized for JavaScript performance. See JavaScript SDK performance optimization for more details.

## Framework drivers

Use `paypal.Buttons.driver()` to integrate with your framework:

```javascript
// React
const PayPalButton = paypal.Buttons.driver("react", { React, ReactDOM });

// Angular (1.x)
paypal.Buttons.driver("angular", window.angular);

// Angular 2
paypal.Buttons.driver("angular2", ng.core);

// Vue
const PayPalButton = paypal.Buttons.driver("vue", window.Vue);
```

## React

### Component implementation

```javascript
import React from "react";
import ReactDOM from "react-dom"
const PayPalButton = paypal.Buttons.driver("react", { React, ReactDOM });

class YourComponent extends React.Component {
    createOrder(data) {
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer ACCESS-TOKEN",
                    "PayPal-Partner-Attribution-Id": "BN-CODE",
                    "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                body: JSON.stringify({
                    cart: [{ sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT", quantity: "YOUR-PRODUCT-QUANTITY" }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    }
    onApprove(data) {
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ orderID: data.orderID })
            })
            .then((response) => response.json());
    }
    render() {
        return (
            <PayPalButton
                createOrder={(data, actions) => this.createOrder(data)}
                onApprove={(data, actions) => this.onApprove(data)}
            />
        );
    }
}
```

### Functional implementation

```javascript
import React from "react";
import ReactDOM from "react-dom"
const PayPalButton = paypal.Buttons.driver("react", { React, ReactDOM });

function YourComponent() {
    const createOrder = (data) => {
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer ACCESS-TOKEN",
                    "PayPal-Partner-Attribution-Id": "BN-CODE",
                    "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                body: JSON.stringify({
                    cart: [{ sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT", quantity: "YOUR-PRODUCT-QUANTITY" }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    };
    const onApprove = (data) => {
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ orderID: data.orderID })
            })
            .then((response) => response.json());
    };
    return (
        <PayPalButton
            createOrder={(data) => createOrder(data, actions)}
            onApprove={(data) => onApprove(data, actions)}
        />
    );
}
```

## Angular (1.x)

```javascript
paypal.Buttons.driver("angular", window.angular);
angular
    .module("app", ["paypal-buttons"])
    .controller("appController", function($scope) {
        $scope.opts = {
            createOrder: function(data) {
                return fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": "Bearer ACCESS-TOKEN",
                            "PayPal-Partner-Attribution-Id": "BN-CODE",
                            "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                        },
                        body: JSON.stringify({
                            cart: [{ sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT", quantity: "YOUR-PRODUCT-QUANTITY" }],
                        }),
                    })
                    .then((response) => response.json())
                    .then((order) => order.id);
            },
            onApprove: function(data) {
                return fetch("/my-server/capture-paypal-order", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ orderID: data.orderID })
                    })
                    .then((response) => response.json());
            },
        };
    });
```

Template:
```html
<body ng-app="app" ng-controller="appController">
    <paypal-buttons props="opts"></paypal-buttons>
</body>
```

## Angular 2 (using TypeScript)

```javascript
@ng.core.Component({
    selector: 'my-app',
    template: `<div id="app">
        <paypal-buttons [props]="{createOrder: createOrder, onApprove: onApprove}"></paypal-buttons>
    </div>`,
})
class AppComponent {
    createOrder(data) {
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "PayPal-Partner-Attribution-Id": "BN-CODE",
                    "Authorization": "Bearer ACCESS-TOKEN",
                    "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                },
                body: JSON.stringify({
                    cart: [{ sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT", quantity: "YOUR-PRODUCT-QUANTITY" }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    }
    onApprove(data, actions) {
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ orderID: data.orderID })
            })
            .then((response) => response.json());
    }
}
@ng.core.NgModule({
    imports: [
        ng.platformBrowser.BrowserModule,
        paypal.Buttons.driver('angular2', ng.core)
    ],
    declarations: [AppComponent],
    bootstrap: [AppComponent]
})
class AppModule {}
ng.platformBrowserDynamic.platformBrowserDynamic().bootstrapModule(AppModule);
```

## Vue

```javascript
const PayPalButton = paypal.Buttons.driver('vue', window.Vue)

Vue.component("app", {
    // Note: use `style-object` or `styleObject` (not `style`) to avoid conflict with Vue's reserved `style` prop
    template: `
        <paypal-buttons
            :on-approve="onApprove"
            :create-order="createOrder"
            :on-shipping-address-change="onShippingAddressChange"
            :on-shipping-options-change="onShippingOptionsChange"
            :on-error="onError"
            :style-object="style"
        />
    `,
    components: { "paypal-buttons": PayPalButton },
    computed: {
        createOrder: function() {
            return (data) => {
                return fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": "Bearer ACCESS-TOKEN",
                            "PayPal-Partner-Attribution-Id": "BN-CODE",
                            "PayPal-Auth-Assertion": "AUTH-ASSERTION-JWT",
                        },
                        body: JSON.stringify({
                            cart: [{ sku: "YOUR-PRODUCT-STOCK-KEEPING-UNIT", quantity: "YOUR-PRODUCT-QUANTITY" }],
                        }),
                    })
                    .then((response) => response.json())
                    .then((order) => order.id);
            }
        },
        onApprove: function() {
            return (data) => {
                return fetch("/my-server/capture-paypal-order", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ orderID: data.orderID })
                    })
                    .then((response) => response.json());
            }
        },
        onShippingAddressChange(data, actions) {
            if (data.shippingAddress.countryCode !== 'US') {
                return actions.reject(data.errors.COUNTRY_ERROR);
            }
        },
        onShippingOptionsChange(data, actions) {
            if (data.selectedShippingOption.type === 'PICKUP') {
                return actions.reject(data.errors.STORE_UNAVAILABLE);
            }
        },
        onError: function() {
            return (err) => {
                console.error(err);
                window.location.href = "/your-error-page-here";
            }
        },
        style: function() {
            return {
                shape: 'pill',
                color: 'gold',
                layout: 'horizontal',
                label: 'paypal',
                tagline: false,
            }
        },
    },
});

const vm = new Vue({ el: "#container" });
```

## Next steps

- **Test in sandbox** — Test in the PayPal sandbox.
- **Go live** — Move from PayPal's production environment to go live.
