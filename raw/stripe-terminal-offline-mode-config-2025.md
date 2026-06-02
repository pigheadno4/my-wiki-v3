<!-- Source URL: https://docs.stripe.com/terminal/fleet/offline-mode -->
<!-- Fetched: 2026-05-01 -->

# Configure offline mode

Enable or disable offline mode on your readers.

When you’re operating with intermittent, limited, or no network connectivity, Stripe Terminal allows you to store payments locally on [your POS device](https://docs.stripe.com/terminal/features/operate-offline/overview.md). When a network connection is restored, the SDK automatically forwards any stored payments to Stripe.

You can configure offline mode in the Dashboard or in the Configuration API.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/offline-mode?dashboard-or-api=dashboard.

To enable (or disable) offline mode, go to the relevant configuration you want to change and edit it. If adding a new configuration, create a new one first.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **Offline mode** row under **Local configurations** or **Inherited configurations**.
1. Enable (or disable) the toggle depending on your preference.
1. Click **Update**.
1. Review the final configuration for the location, and apply the configuration changes by clicking **Apply changes** on the configuration drawer.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click the overflow menu (⋯) > **Edit configuration**.
1. Click **Edit** or **Override** next to the **Offline mode** icon.
1. Enable (or disable) the toggle depending on your preference.
1. Click **Update**.
1. Apply the configuration changes by clicking **Apply changes** on the configuration drawer.

The offline mode setting updates on the reader within 10 minutes.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/offline-mode?dashboard-or-api=api.

You can specify offline mode when creating or updating a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object.

To create a `Configuration` object with offline mode enabled, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  offline: {
    enabled: true,
  },
});
```

To update a `Configuration` object with offline mode, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  'tmc_EjHtMwLT8HmATT',
  {
    offline: {
      enabled: true,
    },
  }
);
```

Learn more about how to enable [offline mode](https://docs.stripe.com/terminal/features/operate-offline/overview.md).
