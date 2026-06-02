<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/app-review -->
<!-- Fetched: 2026-05-01 -->

# Prepare for app review

Learn how to prepare your app for Stripe's review process.

Stripe’s app review process ensures the right level of security and varies depending on the use case. We require reviews for apps from users of our [Point-to-Point Encryption (P2PE) solution](https://docs.stripe.com/terminal/overview.md#encryption) and for all apps intended for deployment on Verifone devices before they can be deployed. Your app qualifies for automated approval if:

- It’s used on Stripe readers without [Point-to-Point Encryption (P2PE)](https://docs.stripe.com/terminal/overview.md#encryption). You can limit the [compatible device types](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API.md#add-readers-to-device-deploy-group) to only Stripe device types (for example, [Stripe Reader S700/S710](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md)).
- It’s intended only for development and testing on a [DevKit](https://docs.stripe.com/terminal/features/apps-on-devices/build.md). You can limit the [compatible device types](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API.md#add-readers-to-device-deploy-group) to only DevKit device types (for example, Stripe Reader S700/S710 DevKit).
- When you re-upload an APK that Stripe has previously reviewed and approved.

The [following guidelines](https://docs.stripe.com/terminal/features/apps-on-devices/app-review.md#app-review-guidelines) apply to all applications deployed on Stripe Terminal devices to protect sensitive payment information and align with our [shared responsibility model](https://docs.stripe.com/security/guide.md), regardless of the review process.

## App review at a glance

If your app requires a review, Stripe reviews its [device asset version](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md#create-device-asset-version). This process doesn’t require any action from you.

1. A reviewer downloads your app and installs it on a Terminal smart reader.
1. Using the instructions you provided, the reviewer interacts with your app and identifies potential problems, focusing on your app’s payment collection user interface.
1. After the reviewer determines there are no present issues, they approve your app for deployment. Stripe [notifies you of app approval](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md#monitor-status). The reviewer might reject your app if they’re unable to follow instructions, or if the app contains features that might put payment information at risk.

The exact amount of time and effort required to review each app varies because no two apps are alike. Stripe typically reviews apps within 2 working days from the submission date. Most app submissions receive a review within 5 working days, with updates on the review status as mentioned above. In exceptional cases, such as the last week of December, app reviews might take longer than these estimated timelines. If you submit incomplete information, we might delay the review time, or your submission might not pass. The estimated timelines serve as an estimate for app review duration and don’t create an obligation for Stripe or its affiliates.

## App review guidelines

Use the guidelines below to help with a timely and successful app review.

### Build multi-tenant apps

If you’re a platform building apps for Terminal devices on behalf of individual businesses, we encourage you to build a multi-tenant app that serves all of your users. You can build business-specific workflows, such as different image or graphics assets per business, into your app’s configuration and settings. This approach also removes the need for you to submit individual apps per business.

### Prevent collecting keyed payment card numbers or PINs

Use the Terminal reader running the app to request payment from a customer and collect sensitive card and PIN information. The [Terminal SDK](https://docs.stripe.com/terminal/features/apps-on-devices/build.md#discover-and-connect-a-reader) allows you to display an appropriate prompt on the device screen.

Make sure that your app doesn’t display user interface elements (for example, an input field) that allow the manual entry of PINs, authentication values, or payment information.

### Support sandbox payments

During development and testing, use a DevKit device to [accept sandbox payments](https://docs.stripe.com/terminal/features/apps-on-devices/build.md). This allows Stripe to use a [physical Terminal test card](https://docs.stripe.com/terminal/references/testing.md#physical-test-cards) when we review your app.

If you must accept live payments, make sure the app accepts a minimal charge amount, such as 1 USD (or equivalent in another currency).

### Address technical defects

[Use your DevKit](https://docs.stripe.com/terminal/features/apps-on-devices/build.md) to identify defects before submitting your app for review.

Examples of common defects include:

- The app fails to install because of an error during its build process.
- The app crashes before we can interact with the app’s payment UI.
- The app can’t detect or connect to the reader.

Make sure to address the technical defects that can prevent us from successfully interacting with or using your app. We reject apps that can’t be fully reviewed due to technical defects.

### Write clear and complete instructions

When you submit your app for review, assume that Stripe hasn’t seen it before. Make sure your instructions are self-contained and don’t assume any special knowledge to complete the review. We must be able to follow your instructions exactly as submitted.

Include the following with your app’s instructions:

- Login information, such as a username or password (if applicable)
- Fixed authentication code that remains valid indefinitely (if applicable)
- How to reach your payment collection UI
- How to exercise the app fully to highlight any problems

Don’t provide credentials that permit access to sensitive information or to functionality that can cause any side effects. For example, an app that accepts orders for food must not cause any actual food preparation to occur as a result of orders placed during app review.

## Submit your app for review

Follow the steps to [submit your app](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md).

## Next steps

- [Submit your app for review](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md)
- [Deploy your app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API.md)
