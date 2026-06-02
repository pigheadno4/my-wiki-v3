<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/submit -->
<!-- Fetched: 2026-05-01 -->

# Submit your app

Learn how to submit your Android app to Stripe.

After you finalize your app, you must submit it to Stripe. You can upload your app using the Stripe Dashboard.

If your app requires a review, follow the [app review guidelines](https://docs.stripe.com/terminal/features/apps-on-devices/app-review.md#app-review-guidelines) to help with a timely and successful review. For example, verify the instructions you provide for the Stripe reviewer to ensure they’re complete.

### Upload your app

1. In the Stripe Dashboard, click **Terminal** > **Software**.
1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Create app**.
1. In the **App information** window, enter the name of your app and the package name, then click **Create app**.
1. Complete the following steps in the **Upload your APK** window:
   - Choose the compatible devices for your app.
   - Upload your APK file.
   - If your app requires an app review, add [instructions](https://docs.stripe.com/terminal/features/apps-on-devices/app-review.md#instructions) for the Stripe reviewer.
   - Enter the email address where Stripe can send updates about your app review. You can enter one or multiple email addresses.
   - Click **Submit for review**.

## Monitor the status

After you submit your app, you can monitor the following for status updates:

| Delivery method | Description                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| Email           | Stripe sends an email notification of your app review results to the email address you provided during submission. |
| Dashboard       | Your app review status appears on the [app details](https://dashboard.stripe.com/terminal/software) page.          |
| Webhook         | Stripe sends a [webhook](https://docs.stripe.com/webhooks.md) to your webhook endpoint:                            |

- `terminal.device_asset_version.app_review_approved` - Stripe approves your app for deployment.
- `terminal.device_asset_version.app_review_rejected` - The app reviewer couldn’t approve your app. You must fix the problem and resubmit your app for review.

You can find all webhook events on the [Events](https://dashboard.stripe.com/events) page. |

## Next steps

- [Deploy your app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API.md)
