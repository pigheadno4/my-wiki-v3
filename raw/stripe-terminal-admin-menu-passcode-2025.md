<!-- Source URL: https://docs.stripe.com/terminal/fleet/admin-menu-passcode -->
<!-- Fetched: 2026-05-01 -->

# Configure the admin menu passcode

Customize the admin menu passcode for your readers.

The admin menu on [smart readers](https://docs.stripe.com/terminal/smart-readers.md) provides access to a readers’s wifi settings, appearance settings, and diagnostics details.

The default passcode to access the admin menu on your smart reader is `07139`. For security, you should set your own custom 5 digit passcode.

> Ensure your admin passcodes are secure and not easily guessable. Avoid common patterns like sequential numbers (12345) or repeated digits (11111).

You can set an account-level default passcode, which applies to all readers in your fleet. You can also set a custom passcode for individual locations, which overrides the account-level default passcode. Locations that don’t have a custom passcode inherit the account-level default passcode, or the Stripe default passcode if you don’t set an account-level default.

You can configure admin menu passcodes in the Dashboard or with the Configuration API. You can also use the Dashboard to see the currently set or inherited passcode.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/admin-menu-passcode?dashboard-or-api=dashboard.

Stripe restricts access to passcode management based on the following user roles:

- Only users with Super Administrator, Administrator, Terminal Specialist, or Developer roles can view passcodes.
- Only users with Super Administrator, Administrator, or Terminal Specialist roles can modify passcodes.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **Admin menu passcode** row under **Local configurations** or **Inherited configurations**.
1. To set a custom passcode, enable the toggle. To use the Stripe default passcode, disable the toggle.
1. Enter a five digit numeric passcode.
1. Click **Update**.
1. Review the final configuration for the location, and apply the configuration changes by clicking **Apply changes** on the configuration drawer.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change the passcode for.
1. Click the overflow menu (⋯) > **Edit configuration**.
1. Click **Edit** or **Override** next to the **Admin menu passcode** icon.
1. To set a custom passcode, enable the toggle. To use the Stripe default passcode, disable the toggle.
1. Enter a five digit numeric passcode.
1. Click **Update**.
1. Apply the configuration changes by clicking **Apply changes** on the configuration drawer.

Stripe applies the new passcode within 10 minutes.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/admin-menu-passcode?dashboard-or-api=api.

You can specify an admin menu passcode when creating or updating a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object.

To create a `Configuration` object with a custom admin menu passcode, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```curl
curl https://api.stripe.com/v1/terminal/configurations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "reader_security[admin_menu_passcode]=\"13700\""
```

To update a `Configuration` object with a custom admin menu passcode, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

```curl
curl https://api.stripe.com/v1/terminal/configurations/tmc_EjHtMwLT8HmATT \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "reader_security[admin_menu_passcode]=\"13700\""
```
