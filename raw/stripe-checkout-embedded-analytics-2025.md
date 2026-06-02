<!-- Source: Stripe Checkout — Track analytics events in Embedded Checkout -->
<!-- Fetched: 2026-04-20 -->
<!-- Note: Private preview feature as of ingestion date -->

# Track analytics events in Embedded Checkout

Use analytics events from Embedded Checkout to monitor user behavior.

> #### Private preview
>
> Embedded Checkout analytics is in private preview.

Stripe Embedded Checkout supports real-time analytics events, allowing you to track user behavior, optimize conversion rates, and attribute sales to marketing campaigns.

## Overview

With the analytics feature, you can:

- Receive real-time events during the checkout process
- Link events to specific funnels or campaigns using client metadata
- Integrate with popular analytics platforms or your own systems

## Available events

Embedded Checkout send the following analytics events throughout the checkout lifecycle:

| Event                  | When we send it                                 | Key data                                                          |
| ---------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| `deviceData`           | When the checkout UI renders                    | Device category, language, platform, viewport                     |
| `checkoutRendered`     | When the checkout UI renders                    | Line items, currency, amount                                      |
| `promotionCodeApplied` | When a promotional code is successfully applied | Promotion code                                                    |
| `lineItemChange`       | When items, quantities, or currency change      | Line items, currency, amount                                      |
| `checkoutSubmitted`    | When a customer submits payment information     | Payment method type, line items, currency, amount                 |
| `checkoutSubmitFailed` | When a payment submission fails                 | Payment method type, failure reason, line items, currency, amount |

### Event structure

All analytics events follow this structure:

```typescript
{
  eventType: string;                        // Event name (for example, 'checkoutRendered')
  checkoutSession: string;                  // Checkout Session ID
  details: object;                          // Event-specific data (see below)
  clientMetadata: {[key: string]: string};  // Your custom metadata
  timestamp: number;                        // Unix timestamp in seconds
}
```

### Event details

Each event includes specific details in the `details` object:

#### deviceData

Sent when the checkout UI loads and renders to the customer. Provides information about the user’s device and browser.

```typescript
{
  device: {
    category: 'mobile' | 'tablet' | 'desktop';
    language?: string;
    platform?: string;
    viewport?: {width: number; height: number};
  }
}
```

#### checkoutRendered

Sent when the checkout UI loads and renders to the customer.

```typescript
{
  items?: Array<{
    quantity?: number; // metered items won't show quantity
    product?: string;
    amount?: number; // in smallest currency unit (for example, cents)
    rateCard?: string;
    pricingPlan?: string;
    price?: string;
  }>;
  currency?: string;
  amount?: number; // in smallest currency unit (for example, cents)
}
```

#### promotionCodeApplied

Sent when a promotion code is successfully applied.

```typescript
{
  code: string;
}
```

#### lineItemChange

Sent when line items, quantities, or currency are updated. This includes quantity changes, currency changes, optional items, cross-sells, and upsells.

```typescript
{
  items?: Array<{
    quantity?: number;
    product?: string;
    amount?: number; // total (not unit amount)
    rateCard?: string;
    pricingPlan?: string;
    price?: string;
  }>;
  currency?: string;
  amount?: number; // total in smallest currency unit (for example, cents)
}
```

#### checkoutSubmitted

Sent when the customer submits their payment information.

```typescript
{
  items?: Array<{
    quantity?: number;
    product?: string;
    amount?: number; // total (not unit amount)
    rateCard?: string;
    pricingPlan?: string;
    price?: string;
  }>;
  currency?: string;
  amount?: number; // total in smallest currency unit (for example, cents)
  paymentMethodType: string; // for example, 'card', 'klarna', and so on.
}
```

> All amounts are provided in the smallest currency unit (for example, cents for USD). Always use the amounts provided in the event details—don’t recalculate them on the client side. These analytics events are a best effort, and provide behavioral tracking and conversion analytics.

#### checkoutSubmitFailed

Sent when a valid payment submission fails.

```typescript
{
  items?: Array<{
    quantity?: number;
    product?: string;
    amount?: number; // total (not unit amount)
    rateCard?: string;
    pricingPlan?: string;
    price?: string;
  }>;
  currency?: string;
  amount?: number; // total in smallest currency unit (for example, cents)
  paymentMethodType: string; // for example, 'card', 'klarna', and so on.
  failureReason: 'api_error' | 'user_cancelled' | 'reverification' | 'unexpected';
}
```

The `failureReason` field indicates why the payment submission failed:

| Failure Reason   | Description                                                                                                                                       | Examples                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_error`      | Network or API errors, card declines, 3DS authentication failures, or server validation errors after valid payment information has been submitted | Such as `card_declined`, `expired_card`, `incorrect_cvc`, `insufficient_funds`, `processing_error`, `api_connection_error`, or payment method provider errors |
| `user_cancelled` | User canceled the payment flow after valid payment information has been submitted                                                                 | Such as Link Klarna sign up flow dismissal                                                                                                                    |
| `reverification` | Link reverification required after valid payment information has been submitted                                                                   | Link session expired                                                                                                                                          |
| `unexpected`     | Unknown or unexpected errors after valid payment information has been submitted                                                                   | Unknown or unexpected errors                                                                                                                                  |

## Implementation

1. Create a Checkout Session with client metadata

   When creating your Checkout Session, include `client_metadata` to link events to specific funnels or campaigns:

   ```javascript
   const session = await stripe.checkout.sessions.create({
     ui_mode: "embedded_page",
     line_items: [
       {
         price: "{{PRICE_ID}}",
         quantity: 1,
       },
     ],
     mode: "payment",
     return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
     client_metadata: {
       funnel_id: "summer_sale_2025",
       campaign: "email_promo",
       variant: "version_A",
     },
   });
   ```

   > Any data included in `client_metadata` is accessible on the client. Avoid sharing sensitive or confidential information through these fields.

1. Initialize Embedded Checkout with an analytics event handler

   When initializing Embedded Checkout, include the `onAnalyticsEvent` handler:

   ```javascript
   const checkout = await stripe.createEmbeddedCheckoutPage({
     clientSecret: session.client_secret,
     onAnalyticsEvent: (event: StripeCheckoutAnalyticsEvent) => {
       // Handle the event here
       console.log('Received event:', event);
     },
   });
   ```

1. Handle analytics events

   In your `onAnalyticsEvent` handler, you can process events and send them to your analytics platform.

   Here’s an example using Segment:

   ```javascript
   const checkout = await stripe.createEmbeddedCheckoutPage({
     clientSecret: session.client_secret,
     onAnalyticsEvent: (event) => {
       const {
         eventType,
         details,
         clientMetadata,
         checkoutSession,
         timestamp,
       } = event;

       switch (eventType) {
         case "deviceData":
           // Custom Segment e-commerce event
           analytics.track("Checkout Device Data Collected", {
             device_category: details.device.category,
             language: details.device.language,
             platform: details.device.platform,
             viewport_width: details.device.viewport?.width,
             viewport_height: details.device.viewport?.height,
             checkout_id: checkoutSession,
             ...clientMetadata,
           });
           break;

         case "checkoutRendered":
           // Standard Segment e-commerce event
           analytics.track("Checkout Started", {
             checkout_id: checkoutSession,
             currency: details.currency?.toUpperCase(),
             value: details.amount ? details.amount / 100 : 0,
             products: details.items?.map((item) => ({
               product_id: item.product,
               price: item.amount ? item.amount / 100 : 0,
               quantity: item.quantity,
             })),
             ...clientMetadata,
           });
           break;

         case "promotionCodeApplied":
           // Standard Segment e-commerce event
           analytics.track("Coupon Applied", {
             checkout_id: checkoutSession,
             coupon_id: details.code,
             ...clientMetadata,
           });
           break;

         case "lineItemChange":
           // Custom Segment event
           analytics.track("Checkout Items Updated", {
             checkout_id: checkoutSession,
             currency: details.currency?.toUpperCase(),
             value: details.amount ? details.amount / 100 : 0,
             products: details.items?.map((item) => ({
               product_id: item.product,
               price: item.amount ? item.amount / 100 : 0,
               quantity: item.quantity,
               ...(item.price && { sku: item.price }),
             })),
             ...clientMetadata,
           });
           break;

         case "checkoutSubmitted":
           // Standard Segment e-commerce event
           analytics.track("Payment Information Entered", {
             checkout_id: checkoutSession,
             payment_method: details.paymentMethodType,
             currency: details.currency?.toUpperCase(),
             value: details.amount ? details.amount / 100 : 0,
             products: details.items?.map((item) => ({
               product_id: item.product,
               price: item.amount ? item.amount / 100 : 0,
               quantity: item.quantity,
               ...(item.price && { sku: item.price }),
             })),
             ...clientMetadata,
           });
           break;

         case "checkoutSubmitFailed":
           // Custom Segment event for failed submissions
           analytics.track("Payment Submission Failed", {
             checkout_id: checkoutSession,
             payment_method: details.paymentMethodType,
             failure_reason: details.failureReason,
             currency: details.currency?.toUpperCase(),
             value: details.amount ? details.amount / 100 : 0,
             products: details.items?.map((item) => ({
               product_id: item.product,
               price: item.amount ? item.amount / 100 : 0,
               quantity: item.quantity,
               ...(item.price && { sku: item.price }),
             })),
             ...clientMetadata,
           });
           break;
       }
     },
   });
   ```

   You can also send events to your own back end for processing:

   ```javascript
   const checkout = await stripe.createEmbeddedCheckoutPage({
     clientSecret: session.client_secret,
     onAnalyticsEvent: async (event) => {
       const {
         eventType,
         details,
         clientMetadata,
         checkoutSession,
         timestamp,
       } = event;

       // Send to your backend analytics endpoint
       await fetch("/api/analytics", {
         method: "POST",
         headers: { "Content-Type": "application/json" },
         body: JSON.stringify({
           event_type: eventType,
           checkout_session: checkoutSession,
           details,
           client_metadata: clientMetadata,
           timestamp,
         }),
       });
     },
   });
   ```

## Use webhooks for conversion tracking

Use the `checkout.session.completed` webhook event to record successful payments:

```javascript
// Server-side webhook handler

app.post("/webhook", express.raw({ type: "application/json" }), (req, res) => {
  const payload = req.body;
  const sig = req.headers["stripe-signature"];

  let event;

  try {
    event = stripe.webhooks.constructEvent(
      payload,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET,
    );
  } catch (err) {
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  if (event.type === "checkout.session.completed") {
    const session = event.data.object;

    // Track successful conversion with Segment
    analytics.track({
      userId: session.customer,
      event: "Purchase Completed",
      properties: {
        checkout_id: session.id,
        amount: session.amount_total / 100,
        currency: session.currency,
        funnel_id: session.client_metadata?.funnel_id,
        campaign: session.client_metadata?.campaign,
      },
    });
  }

  res.status(200);
});
```

This approach gives you both real-time behavioral tracking (through analytics events) and accurate conversion data (through webhooks) to understand your checkout funnel performance.

## TypeScript Types

If you’re using TypeScript, you can import the event types:

```typescript
import type { StripeCheckoutAnalyticsEvent } from "@stripe/stripe-js";

const checkout = await stripe.createEmbeddedCheckoutPage({
  clientSecret: session.client_secret,
  onAnalyticsEvent: (event: StripeCheckoutAnalyticsEvent) => {
    // TypeScript will provide full type checking
  },
});
```
