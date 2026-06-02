---
title: Multiple subscription buttons
slug: /docs/subscriptions/customize/multiple-buttons-website/
createTime: "2024-08-15T08:00:31.231Z"
updateTime: "2024-08-15T08:00:31.497Z"
---

# Multiple subscription buttons

You can let your buyers choose a subscription plan from multiple plans available from a single page of your website.

![Two,sets,of,subscription,buttons,where,a,basic,plan,is,$5,and,a,premium,plan,is,$10](assets/paypal-subscriptions-multi-buttons.svg)

## 1. Modify JavaScript SDK code

Modify the JavaScript SDK code to render multiple buttons on a single webpage.

Add the SDK script before the first PayPal button div . Add the SDK script only once on your web page ensure that the SDK doesn't render multiple times on your webpage.

&lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&amp;vault=true&amp;intent=subscription"&gt;&lt;/script&gt;## 2. Add ID for each button
Add a unique container HTML id for each button code.

**Tip:** Use the same ID for the container ID that you used for the plan ID.

&lt;div id="paypal-button-container"&gt;&lt;/div&gt; // A unique ID for each button
&lt;script&gt;
paypal.Buttons({
createSubscription: function(data, actions) {
return actions.subscription.create({
'plan_id': 'YOUR-PLAN-ID'
});
},
onApprove: function(data, actions) {
alert(data.subscriptionID);
}
}).render('#paypal-button-container');
&lt;/script&gt;### Example
This sample creates 2 different plans:

- Basic plan priced at $5 per month with plan ID P-89K58960WT101463BMA2QTGQ .
- Premium plan priced at $10 per month with plan ID P-8D325842DA922762MMA2QT6Q .

&lt;!DOCTYPE html&gt;

&lt;head&gt;
&lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt; &lt;!-- Ensures optimal rendering on mobile devices. --&gt;
&lt;meta http-equiv="X-UA-Compatible" content="IE=edge" /&gt; &lt;!-- Optimal Internet Explorer compatibility --&gt;
&lt;style&gt;
body {
display: flex;
direction: 'column';
}

    .column {
      border: 1px solid #ccc;
      margin: 20px;
      padding: 20px;
    }

    p {
      text-align: center;
      margin-bottom: 50px;
    }

&lt;/style&gt;
&lt;/head&gt;

&lt;body&gt;
&lt;script src="https://www.paypal.com/sdk/js?CLIENT-ID=AUwAEZzkXUVAhmO10ESMB7i9jBlp9PlvrpgX1RGo5APTKMKFSRBNmCW98BxjzhAyDU0sIslCMdeOsDm3&amp;vault=true&amp;intent=subscription"&gt;
&lt;/script&gt;&lt;!-- Replace CLIENT-ID with your client ID --&gt;
&lt;div class="column"&gt;
&lt;p&gt;
BASIC PLAN&lt;br /&gt;$5 per month
&lt;/p&gt;
&lt;div id="paypal-button-container-P-89K58960WT101463BMA2QTGQ"&gt;&lt;/div&gt; &lt;!-- Replace with your plan ID --&gt;
&lt;/div&gt;

&lt;script&gt;
paypal.Buttons({
createSubscription: function(data, actions) {
return actions.subscription.create({
'plan_id': 'P-89K58960WT101463BMA2QTGQ' // Replace with your plan ID
});
},
onApprove: function(data, actions) {
alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
}
}).render('#paypal-button-container-P-89K58960WT101463BMA2QTGQ'); // Renders the PayPal button. Replace with your plan ID

&lt;/script&gt;

&lt;div class="column"&gt;
&lt;p&gt;
PREMIUM PLAN&lt;br /&gt;$10 per month
&lt;/p&gt;
&lt;div id="paypal-button-container-P-8D325842DA922762MMA2QT6Q"&gt;&lt;/div&gt; &lt;!-- Replace with your plan ID --&gt;
&lt;/div&gt;
&lt;script&gt;
paypal.Buttons({
createSubscription: function(data, actions) {
return actions.subscription.create({
'plan_id': 'P-8D325842DA922762MMA2QT6Q' // Replace with your plan ID
});
},
onApprove: function(data, actions) {
alert('You have successfully subscribed to ' + data.subscriptionID); // Optional message given to subscriber
}
}).render('#paypal-button-container-P-8D325842DA922762MMA2QT6Q'); // Replace with your plan ID

&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;
