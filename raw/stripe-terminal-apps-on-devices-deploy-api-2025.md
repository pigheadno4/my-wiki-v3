<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API -->
<!-- Fetched: 2026-05-01 -->

# Deploy your app with the API

Learn how to deploy your Android app to your devices through a webhook.

After Stripe reviews and approves your app for deployment, we [notify you](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md#monitor-status) by email through a webhook. You can then follow the instructions below to deploy your app.

During deployment, your app is immediately sent and downloaded to your device. The device reboots to install the app. Devices reboot every 24 hours and apply any updates automatically. To check for and apply updates immediately, you can manually reboot your device.

Deploy your app to devices by creating a device deploy group and associating it with a [location](https://docs.stripe.com/api/terminal/locations.md).

> The Apps on Devices API is currently in private preview. If you’re interested in gaining access, [contact Stripe Support](https://support.stripe.com/contact) to assess your eligibility.
