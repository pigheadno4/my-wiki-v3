<!-- Source URL: https://docs.stripe.com/terminal/fleet/configurations-overview -->
<!-- Fetched: 2026-05-01 -->

# Terminal configurations

Use the Terminal Configurations object to apply configurations to your readers.

The Terminal [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object contains all relevant configurations for a reader, such as the [splash screen](https://docs.stripe.com/terminal/fleet/splash-screen.md), [tipping settings](https://docs.stripe.com/terminal/fleet/tipping.md), [offline mode](https://docs.stripe.com/terminal/fleet/offline-mode.md), and so on (see individual configuration guides for specific instructions and options).

Because these settings are hierarchical, you can apply a configuration at either the account level or at the individual location level. You can set configurations in the following ways:

- On individual [Locations](https://docs.stripe.com/api/terminal/locations.md): Applies to all readers registered to that Location
- At the account level: Applies to all readers in your fleet

You can override account-level settings with location-level settings. If you don’t configure settings at the location level, they inherit the account-level settings.

> Creating configurations for zones is in private preview. You can [email us](mailto:terminal-zones-configuration-preview@stripe.com) to request to join the preview.

For example, you can model your `Configuration` objects as follows:
![Configuration Hierarchy](assets/stripe-terminal-configuration-hierarchy.png)

In this scenario, Location 3 inherits the configurations from the account “Default configuration”, while Locations 1 and 2 have their own configuration.

> If you don’t set a configuration on the location-level, the Location inherits the default configuration on the account. For example, if you don’t set the splash screen on the Location, it inherits it from the default configuration set at the account level.

Any configuration changes made with the API or Dashboard can take up to 10 minutes to reflect on the target readers.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=dashboard.

You can view and manage your configurations in the Stripe Dashboard. To manage your configurations, click **Manage locations** on the Readers tab. Stripe displays a list of configurations on the right hand side of the page. To view additional configurations, click **View more** at the bottom of the list.

## Update the default configuration for the account

1. Select the overflow menu (⋯) on the **All locations** list item (top).
1. Click **Edit configuration**.
1. Click **Override** for each configuration type you want to update.
1. Click **Apply changes**.

All readers across all locations inherit the configuration settings that you set, unless there’s an override set on the configuration for the location. The reader updates within 10 minutes after you add the configuration.

## Create a new configuration for a location

#### From the location details page

1. On the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page, click the location to go to the location details page.
1. Under **Inherited configurations**, click the edit icon (✏) for the configuration type you want to update.
1. Enter a name for the configuration. You can use this name more than once.
1. Enter the settings for the configuration type.
1. Click **Apply changes**.

#### From the manage locations page

1. Select the overflow menu (⋯) on the location item.
1. Click **Add configuration**.
1. Enter a name for the configuration. You can use this name more than once.
1. Click **Override** for each configuration type you want to update.
1. Click **Apply changes**.

All readers in the location inherit the configuration settings that you set. The reader updates within 10 minutes after you add the configuration.

## Update an existing configuration

#### From the location details page

1. On the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page, click the location to go to the location details page.
1. Under **Local configurations** or **Inherited configurations**, click the edit icon (✏) for the configuration type you want to update.
1. Enter the settings for the configuration type.
1. Click **Apply changes**.

#### From the manage locations page

1. Select the overflow menu (⋯) on either the location list item (left side) or the configuration itself (right side).
1. Click **Edit configuration**.
1. Click **Override** for each configuration type you want to update.
1. Click **Apply changes**.

All the readers in the location update within 10 minutes.

## Delete an existing configuration

#### From the location details page

1. On the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page, click the location to go to the location details page.
1. Click **Delete** next to **Local configurations**.
1. Click **Delete**.

#### From the manage locations page

1. Select the overflow menu (⋯) on either the location list item (left side) or the configuration itself (right side).
1. Click **Delete configuration**.

After you delete the configuration, the readers in the location default back to the account’s default configuration within 10 minutes.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api.

## Retrieve the account default configuration

Stripe automatically provisions the default configuration for your account. When you set up your hierarchy, any setting that isn’t established at the location level inherits the setting from the default configuration. You can’t apply the default configuration directly to a Location. To retrieve the account default configuration, use the [configuration retrieve](https://docs.stripe.com/api/terminal/configuration/retrieve.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configurations = await stripe.terminal.configurations.list({
  is_account_default: true,
});
```

## Create a configuration for an individual location

To create a `Configuration` object, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  bbpos_wisepos_e: {
    splashscreen: 'file_1KjBJdE7XUJuZdf0F6GgO9uY',
  },
});
```

To assign it to a location, provide the `Configuration` object you previously created to the [update location](https://docs.stripe.com/api/terminal/locations/update.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const location = await stripe.terminal.locations.update(
  'tml_DPJxAAnxbn3JQz',
  {
    configuration_overrides: 'tmc_EjHtMwLT8HmATT',
  }
);
```

## Update an existing configuration

To update a `Configuration` object, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  'tmc_EjHtMwLT8HmATT',
  {
    bbpos_wisepos_e: {
      splashscreen: 'file_1KjBJdE7XUJuZdf0F6GgO9uY',
    },
  }
);
```

## Delete a configuration

To delete a `Configuration` object, use the [delete configuration](https://docs.stripe.com/api/terminal/configuration/delete.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const deleted = await stripe.terminal.configurations.del('tmc_EjHtMwLT8HmATT');
```
