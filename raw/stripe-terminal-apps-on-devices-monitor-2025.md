<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/monitor -->
<!-- Fetched: 2026-05-01 -->

# Monitor your deployment

Monitor your Android apps on Stripe SmartPOS Android devices.

After you deploy your app, you can monitor its deployment progress using the Stripe Dashboard. This allows you to investigate any issues during deployment and to deploy a new app, if needed.

Follow these steps to monitor your app:

1. In the Stripe Dashboard, click **Terminal** > **Software**.
1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, choose the app that you want to monitor.
1. On the app details page, under **App info**, choose the release version to view the deployment status and number of Stripe readers in that status.

| Deployment status | Description                                                                           |
| ----------------- | ------------------------------------------------------------------------------------- |
| Pending           | The device hasn’t called the Terminal backend to check for updates yet.               |
| Served            | The app has been served to the device and will attempt to install on the next reboot. |
| Installed         | The app has successfully installed on the device.                                     |
| Failed            | An error occurred while attempting to install the app on the device.                  |

## See also

- [Troubleshooting](https://docs.stripe.com/terminal/features/apps-on-devices/troubleshooting.md)
