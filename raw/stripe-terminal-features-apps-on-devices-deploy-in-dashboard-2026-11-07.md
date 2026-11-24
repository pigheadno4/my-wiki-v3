<!-- Source URL: https://docs.stripe.com/terminal/features/apps-on-devices/deploy-in-dashboard -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Deploy your app in the Dashboard

Learn how to deploy your Android app to your devices in the Dashboard.

After Stripe reviews and approves your app for deployment, we [notify you](https://docs.stripe.com/terminal/features/apps-on-devices/submit.md#monitor-status) by email in the Dashboard. You can then follow the instructions below to deploy your app.

During deployment, your app is immediately sent and downloaded to your device, and the device reboots to install it. Devices reboot every 24 hours and apply any updates automatically. To check for and apply updates immediately, you can manually reboot your device.

You can deploy new and updated apps for Terminal devices in the Dashboard.

## Add or edit a deploy group 

Before you can add or edit a deploy group, you must create a Terminal [location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md) and add [readers](https://docs.stripe.com/api/terminal/readers/object.md) to that location. You can then assign locations to a deploy group, meaning all readers in the location receive updates from that deploy group.

After you create a deploy group, you can edit it at any time by selecting it.

### Add a deploy group

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Manage deploy groups**.
2. Click **Add deploy group**.
3. Complete the following steps in the **Add deploy group** drawer:
   - Enter a group name.
   - Choose your Terminal device type.
   - If desired, select the **Default deploy group** checkbox to create a default deploy group. A default deploy group automatically contains all locations that aren’t explicitly assigned to a different deploy group. You can create one default deploy group per device type.
   - Click **Done**.

### Manage deploy groups

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Manage deploy groups**.
2. Select the deploy group from the list.
3. Click **Add locations**.
4. Choose the locations to add.
5. Click **Done**.

### Manage deploy groups with direct charges

Platforms can add locations owned by Connected Accounts to the platform’s deploy groups.

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Manage deploy groups**.
2. Select the deploy group from the list.
3. Click **Add locations**.
4. Select the account that you want to add locations from in the account dropdown. You must select an account before adding locations.
5. Choose the locations to add.
6. Click **Done**.

## Deploy an app version 

You can deploy your app after a [Stripe reviewer approves](https://docs.stripe.com/terminal/features/apps-on-devices/app-review.md) it.

In the Dashboard, you can deploy apps in one of three ways:

- From the deploy group
- From the Software tab
- From the app itself

### From the deploy group details page

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Manage deploy groups**.
2. On the deploy group details page, click **Deploy** and **New deployment**.
3. Choose a version for each approved app you want to deploy, then click **Next**. You can’t deploy an earlier version of an app—the app version must be newer than the currently deployed app.
4. Select a rollout plan and a mandatory update configuration, then click **Next**.
5. Choose your preferred kiosk app, then click **Next**. The Stripe reader launches this app when it turns on and after each transaction.
6. Confirm the deployment details, then click **Deploy**. The app deploys according to the mandatory update configuration.

### From the Software tab

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, select the apps you want to deploy.
2. Click **Deploy**.
3. Choose a version for each app, then click **Next**. You can’t deploy an earlier version of an app—the app version must be newer than the currently deployed app.
4. Choose the deploy group, then click **Next**.
5. Select a rollout plan and a mandatory update configuration, then click **Next**.
6. Choose your preferred kiosk app, then click **Next**. The Stripe reader launches this app when it turns on and after each transaction. If you only have one app to deploy, choose that app.
7. Confirm the deployment details, then click **Deploy**. The app deploys according to the mandatory update configuration.

### From the app details page

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click the app that you want to deploy.
2. On the app details page, click **Deploy version**.
3. Choose a version of the approved app and each additional app you want to deploy, then click **Next**. You can’t deploy an earlier version of an app—the app version must be newer than the currently deployed app.
4. Choose the deploy group, then click **Next**.
5. Select a rollout plan and a mandatory update configuration, then click **Next**.
6. Choose your preferred kiosk app, then click **Next**. The Stripe reader launches this app when it turns on and after each transaction. If you only have one app to deploy, choose that app.
7. Confirm the deployment details, then click **Deploy**. The app deploys according to the mandatory update configuration.

> Updates will be immediately enforced in the following situations, even if you haven’t configured them to apply immediately:
> 
> - The device is newly unboxed.
> - A `device_asset` in your deploy plan isn’t already installed on the device.
> - The device has been offline or inactive for an extended period.
> 
> These mandatory updates keep all devices secure and up to date.

A mandatory update can also fail to install.

> If a device can’t install an update after three attempts, users can postpone the update to continue processing payments. This ensures that users can maintain payment capabilities in the event of technical difficulties beyond their control.

## Uninstall an app 

You can uninstall an app from a deploy group.

> Don’t uninstall an app to install an older version. Upload the earlier build with a higher version number and [deploy the new app version](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-in-dashboard.md#deploy-app-version). Devices with newer installs won’t accept the downgrade.

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click **Manage deploy groups**.
2. On the deploy group details page, in the top right corner of the **Target Assets** section, click the overflow menu (⋯) then **Select apps to uninstall**.
3. Choose the apps you want to uninstall from this deploy group, then click **Next**.
4. Select a rollout plan and a mandatory update configuration, then click **Next**.
5. Choose your preferred kiosk app, then click **Next**. The Stripe reader launches this app when it turns on and after each transaction. Don’t select the app you’re uninstalling.
6. Confirm the uninstallation details, then click **Deploy**. The app deploys according to the mandatory update configuration.

## Archive an app 

Archiving an app or app version hides it from the deploy interface without uninstalling it from devices where it’s already active. You can unarchive at any time to make it available for deployment again.

To archive an app, you must first archive all of its versions. To unarchive an app version, you must first unarchive the app.

### Archive an app version

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click the app.
2. Use the dropdown menu to choose the version you want to archive.
3. Click **Archive version**.
4. Confirm the action.

### Archive an app 

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click the app you want to archive.
2. On the app details page, click **Archive** in the top right.
3. Confirm the action.

### Unarchive an app or app version

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, navigate to the archived app or archived version as described above.
2. Click **Unarchive** or **Unarchive version**.
3. Confirm the action.

## Share apps across multiple accounts

[Contact your sales representative](https://stripe.com/contact/sales) to assess compatibility with your account and gain access to this feature.

Use this feature if you have multiple Stripe accounts and want to deploy the same app across accounts. Sharing one app across accounts avoids constraints with package name uniqueness and duplicate app reviews.

To create and manage one deployment across accounts in your organization, use [Organization Deployments](https://docs.stripe.com/terminal/fleet/organization-deployments.md).

Designate one account to create and manage the app. Only the account that owns the app can upload new app versions, but other accounts can view and deploy the app by searching for the app ID.

1. On the [Software](https://dashboard.stripe.com/terminal/software) tab, click the overflow menu (⋯ Overflow menu).
2. Click **Search for app**.
3. Enter the app ID and click **View app details**.
4. Click **Deploy version** and enter the deployment details.

## Deploy group best practices

You can sort devices into different deploy groups to roll out software independently and isolate fault in case of any issues. You might have fewer or more deploy groups based on tooling, risk tolerance, and specific business needs.

We recommend the following deploy group setup:

- **Alpha**: Contains locations that correspond to your internal devkits or internal production devices.
- **Beta**: Contains a small number of actual user locations. You can randomly choose these locations, select them based on meaningful criteria (for example, less risky locations), or have users opt in to the `Beta` deploy group based on their risk tolerance.
- **General**: Contains all remaining actual user locations, except those in the `Alpha` or `Beta` groups. You can use a default deploy group to avoid manually assigning each remaining location.

When your app is ready for deployment, promote deploy groups from least to most risky:

|  |  |  |
| --- | --- | --- |
| 1 | Alpha | First, deploy to the `Alpha` deploy group to test your app in a way that minimizes risk to users. Discovering a bug or undesirable behavior at this stage only affects a small number of internal devices, rather than actual users and real payments. |
| 2 | Beta | Second, deploy to the `Beta` deploy group. This balances exposing your app to real users and not exposing all users to potential issues. |
| 3 | General | Finally, deploy to the `General` deploy group after addressing any issues or confirming that no issues existed for the `Beta` deploy group. |

## Deploy an app to a deploy group in progressive stages

After your deploy groups are set up, use progressive deployments to roll out your application to readers within a deploy group in stages. Each stage corresponds to a percentage of the deploy group’s readers that’s greater than the previous stage’s percentage, with the final stage always at 100%. You can use one of our predefined plans or create your own custom plan.

### Set up a progressive deployment

To set up a progressive deployment:

1. Navigate to the desired app details page, click **Deploy version**, then select the intended app version and deploy group.
2. Select a custom or predefined plan under **Progressive Deployments**.
   - After creating the deploy plan, you can’t edit the percentage associated with each stage.
3. Confirm your deploy plan, then click **Deploy**.
4. The deployment starts according to the percentage specified for the initial stage.
   - If you selected a predefined plan, the deployment starts at 0%. You need to manually advance to the next stage for any readers to receive the new version of the Terminal app.
5. To advance a deployment, click **Update** under **Deployed Group** on the app details page, or click **Edit deployment** on the deploy group details page. Confirm the next stage to advance the plan.
6. To pause a deployment, click **Update** (or **Edit deployment** if on the deploy group page) to open a drawer, then click **Pause**. This stops the rollout of your application to any additional readers.
   - Pausing the rollout doesn’t affect devices that have already received the app. Devices that are currently downloading or installing the new app version continue the process. If you discover a bug in an app that’s already deployed, follow our [troubleshooting guidance](https://docs.stripe.com/terminal/features/apps-on-devices/troubleshooting.md#bugs-in-deployed-apps).

Keep the following in mind when using progressive deployments:

- Deployments don’t automatically advance. If you never manually advance the deploy plan, the deployment remains at its current percentage.
- Readers are randomly selected within a deploy group for inclusion in a stage of the progressive deploy plan. For example, if Version 2.0 of an app is currently deployed to 40% of Deploy Group A, then 40% of readers in Deploy Group A have Version 2.0 of the app and 60% have the version prior to 2.0.
- As the deployment advances, the group of readers receiving the new version includes all readers that received it in the previous stage.
- You need to select the desired progressive deploy plan each time you create a new deploy plan. Rollout stages don’t persist between old and new deployment plans.

## Next step

- [Monitor your deployment](https://docs.stripe.com/terminal/features/apps-on-devices/monitor.md)
