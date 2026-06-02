<!-- Source URL: https://docs.paypal.ai/payments/share-pay-links -->
<!-- Fetched: 2026-04-16 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Share a payment link

Share a payment link with customers through email, text message, social media, or your website. When customers open the link, they are directed to the PayPal payment page where they can complete their payment.

## Prerequisites

- PayPal Business Account
- (Optional) PayPal sandbox account to test the payment link before using it in production

## Share a payment link

1. Log in to your [PayPal Business Account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483).
2. From the left navigation, select **Sales** > **Payment Links and Buttons**.
3. Locate the payment link you want to share and select **Open**.
4. Select **View** > **Payment Link**, then copy the link to share with customers.

## Generate QR code

Customers can scan a QR code to open the same payment page as your payment link.

1. Log in to your PayPal Business Account.
2. From the left navigation, select **Sales** > **Payment Links and Buttons**.
3. Locate the payment link you want to share and select **Open**.
4. Select the **QR code** > **Download QR code** to share the QR code with customers for in-person or offline payments.

The QR code does not expire. If you delete the payment link, customers who scan the code are redirected to an expiration page.

## Test your payment link or QR code

Test your payment link or QR code by following these steps before sharing it with customers:

1. Open the payment link or scan the QR code to confirm the the correct product name, price, and payment options appear.
2. Complete a test payment:
   - Use a low-value transaction if testing in live mode.
   - Use a sandbox buyer account if testing in sandbox.
3. Confirm the payment completes successfully and appears in your Dashboard activity.
4. If **Auto-return** is set, confirm customers are redirected to the correct URL.

## Common issues

**Customer cannot see all payment methods**

- Payment method availability depends on the customer's country and eligibility. Not all payment methods appear for every buyer.
