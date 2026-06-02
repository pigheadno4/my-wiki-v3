<!-- Source URL: https://docs.stripe.com/terminal/fleet/cellular -->
<!-- Fetched: 2026-05-01 -->

# Configure the cellular network

Remotely configure a cellular network for your readers.

> #### Information
>
> Cellular configuration only applies to the Stripe Reader S710.

Terminal readers that support cellular capability can operate in either WiFi or cellular mode. When cellular mode is enabled, the device automatically connects to the internet over cellular whenever WiFi is unavailable. To indicate which readers you want to enable cellular on, create cellular-enabled [Locations](https://docs.stripe.com/api/terminal/locations.md) in the Dashboard or with the [Configuration API](https://docs.stripe.com/api/terminal/configuration.md).

After you configure the location, you can register your reader to the `Location`, which tells the reader to enable cellular functionality. By default, locations have cellular functionality disabled.

> Cellular-capable readers, such as the Stripe S710, are billed for cellular usage. Cellular usage fees are billed on a monthly basis and are in addition to other fees. You incur cellular usage fees for a reader when you enable cellular on that reader at any time during a calendar month. See [Terminal pricing](https://stripe.com/terminal#pricing) for more details.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/cellular?dashboard-or-api=dashboard.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to enable cellular for.
1. Click Edit (✏) next to the **Cellular** row under **Local configurations** or **Inherited configurations**.
1. Toggle it to `Enabled`. Acknowledge that enabling cellular affects your billing.
1. Click **Done**.
1. Review the final configuration for the location, and click **Apply changes**.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click Edit (✏) next to the **Cellular** row under **Local configurations** or **Inherited configurations**.
1. Toggle it to `Enabled`. Acknowledge that enabling cellular affects your billing.
1. Click Done.
1. Review the final configuration for the location, and click **Apply changes**.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/cellular?dashboard-or-api=api.

You can specify the cellular mode when creating or updating a `Configuration` object.

## Create a configuration

[Create a Configuration](https://docs.stripe.com/api/terminal/configuration/create.md) object with cellular mode enabled:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  cellular: {
    enabled: true,
  },
});
```

## Update a configuration

[Update a Configuration](https://docs.stripe.com/api/terminal/configuration/update.md) object with cellular mode:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  '{{TERMINALCONFIGURATION_ID}}',
  {
    cellular: {
      enabled: true,
    },
  }
);
```
