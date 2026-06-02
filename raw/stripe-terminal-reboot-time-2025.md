<!-- Source URL: https://docs.stripe.com/terminal/fleet/reboot-time -->
<!-- Fetched: 2026-05-01 -->

# Configure the reboot time window

Customize the reboot time window for your readers.

By default, [smart readers](https://docs.stripe.com/terminal/smart-readers.md) reboot every 24 hours at midnight. If your business is open or processing payments during this time, you might want to set a custom reboot window to avoid any interruptions.

You can set a specific time period for the devices to reboot according to their registered location’s local time. For example, if you register a device in a location with a local time corresponding to UTC-8:00, but it’s managed from a location in UTC-5:00, the scheduled reboot time is UTC-8:00.

> To avoid disruption, not every reader in the same registered location updates simultaneously. Instead, the readers reboot randomly within the configured time period.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/reboot-time?dashboard-or-api=dashboard.

To change the reboot window, go to the relevant configuration you want to change and edit it. Add a new configuration first if you don’t have an existing one.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **Reboot time** row under **Local configurations** or **Inherited configurations**.
1. Select a start and end time. If `start_hour` is less than `end_hour`, we consider them as values for the same day. If `start_hour` is greater than `end_hour`, we consider the `end_hour` a value for the next day.
1. Click **Update**.
1. Review the final configuration for the location, and apply the configuration changes by clicking **Apply changes** on the configuration drawer.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click the overflow menu (⋯) > **Edit configuration**.
1. Click **Edit** or **Override** next to the **Reboot time** icon.
1. Select a start and end time. If `start_hour` is less than `end_hour`, we consider them as values for the same day. If `start_hour` is greater than `end_hour`, we consider the `end_hour` a value for the next day.
1. Click **Update**.
1. Apply the configuration changes by clicking **Apply changes** on the configuration drawer.

Stripe sets the new reboot window within 10 minutes. If the reader has already rebooted for the day, the reboot window takes effect during the next time period.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/reboot-time?dashboard-or-api=api.

You can specify a reboot window when creating or updating a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object.

To create a `Configuration` object with a specific reboot window, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  reboot_window: {
    start_hour: 1,
    end_hour: 3,
  },
});
```

To update a `Configuration` object with a specific reboot window, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  'tmc_EjHtMwLT8HmATT',
  {
    reboot_window: {
      start_hour: 1,
      end_hour: 3,
    },
  }
);
```

- `start_hour`: Integer between 0 to 23 that represents the start hour of the reboot time window.
- `end_hour`: Integer between 0 to 23 that represents the end hour of the reboot time window. The value must be different than the `start_hour`.

If `start_hour` is less than `end_hour`, we consider them as values for the same day. If `start_hour` is greater than `end_hour`, we consider the `end_hour` a value for the next day. In the code example above, the devices are scheduled to reboot anytime between 1 AM to 3 AM. As another example, if you specify the reboot time window as [`start_hour`: 15, `end_hour`: 3], the devices reboot anytime between 3 PM to 3 AM.
