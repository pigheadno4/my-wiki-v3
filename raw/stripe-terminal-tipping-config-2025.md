<!-- Source URL: https://docs.stripe.com/terminal/fleet/tipping -->
<!-- Fetched: 2026-05-01 -->

# Configure on-reader tips

Customize the tipping options displayed on your readers.

You can use [on-reader tips](https://docs.stripe.com/terminal/features/collecting-tips/overview.md) to display suggested tip amounts on the reader before customers present their payment method. We support the following on-reader tip types:

- **Suggest smart tips**: The reader dynamically displays three percentages or amounts, depending on the size of the pre-tip amount.
- **Suggest percentages**: The reader displays three percentage-based tip amounts.
- **Suggest amounts**: The reader displays three tip amounts.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/tipping?dashboard-or-api=dashboard.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **Tipping** row under **Local configurations** or **Inherited configurations**.
1. Choose the **Tipping mode**.
1. Choose the **Currency**.
1. Enter the desired tipping options (for example, you can enter 10%, 15%, and 20% for percentage-based tipping), and repeat this process for different tipping modes and currencies.
1. Click **Review** to view your changes, then click **Confirm**.
1. Review the final configuration for the location, and click **Apply changes**.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click the overflow menu (⋯) > **Edit configuration** to display the configuration drawer.
1. Click **Edit** or **Override** next to the **Tipping** icon.
1. Choose the **Tipping mode**.
1. Choose the **Currency**.
1. Enter the desired tipping options (for example, you can enter 10%, 15%, and 20% for percentage-based tipping), and repeat this process for different tipping modes and currencies.
1. Click **Review** to view your changes, then click **Confirm**.
1. Click **Apply changes**.

Stripe applies the tipping configurations on the reader within 10 minutes.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/tipping?dashboard-or-api=api.

You can specify on-reader tips when creating or updating a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object.

To create a `Configuration` object with specific tipping options, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  tipping: {
    usd: {
      percentages: [15, 20, 25],
      fixed_amounts: [100, 200, 300],
      smart_tip_threshold: 1000,
    },
  },
});
```

To update a `Configuration` object with specific tipping options, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  'tmc_EjHtMwLT8HmATT',
  {
    tipping: {
      usd: {
        percentages: [15, 20, 25],
        fixed_amounts: [100, 200, 300],
        smart_tip_threshold: 1000,
      },
    },
  }
);
```

Learn more about how to enable and customize [on-reader tips](https://docs.stripe.com/terminal/features/collecting-tips/on-reader.md#customize-tips-reader).
