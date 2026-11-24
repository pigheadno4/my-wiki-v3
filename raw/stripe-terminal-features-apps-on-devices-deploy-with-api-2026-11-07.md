<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-api -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Deploy your app with the API

Learn how to deploy your Android app to your devices through a webhook.

After Stripe reviews and approves your app for deployment, we [notify you](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md#monitor-status) by email and by sending an event. You can then follow the instructions below to deploy your app. To automatically deploy your app on approval, set up a [webhook](https://docs.stripe.com/webhooks.md) to listen for the [terminal.device_asset_version.app_review_approved](https://docs.stripe.com/api/events/types.md#event_types-terminal.device_asset_version.app_review_approved) event and trigger the deployment.

During deployment, your app is immediately sent and downloaded to your device. The device reboots to install the app. Devices reboot every 24 hours and apply any updates automatically. To check for and apply updates immediately, you can manually reboot your device.

Deploy your app to devices by creating a device deploy group and associating it with a [location](https://docs.stripe.com/api/terminal/locations.md).

> The Apps on Devices API is currently in private preview. If you’re interested in gaining access, [contact Stripe Support](https://support.stripe.com/contact) to assess your eligibility.
