<!-- Source URL: https://docs.stripe.com/terminal/fleet/wifi -->
<!-- Fetched: 2026-05-01 -->

# Configure the WiFi network

Remotely configure a WiFi network for your readers.

You can remotely configure and manage WiFi networks for [smart readers](https://docs.stripe.com/terminal/smart-readers.md). We support the following network security types:

- WPA/WPA2 Personal (PSK)
- WPA/WPA2 Enterprise (EAP-PEAP)
- WPA/WPA2 Enterprise (EAP-TLS)

To fetch the remotely configured network from the server, the reader must first connect to a local WiFi network.

After you set the WiFi configuration, it displays as a `Configured network` on the reader. You can then select this network to connect automatically, without requiring the end user to enter any additional information.

If you update the WiFi profile, Stripe sends these updates to the reader, which stays connected to the network as long as the credentials are accurate.

> Stripe doesn’t perform validation checks when you configure the WiFi profile. If you enter an incorrect password, expired EAP-TLS certificate, or other invalid credentials, the reader won’t connect to the network.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/wifi?dashboard-or-api=dashboard.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **WiFi** row under **Local configurations** or **Inherited configurations**.
1. Use the **Security** dropdown to select a security type.
1. Enter the relevant credentials.
1. Click **Done**.
1. Review the final configuration for the location, and click **Apply changes**.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click the overflow menu (⋯) > **Edit configuration**.
1. Click **Edit** or **Override** next to the **WiFi** icon.
1. Use the **Security** dropdown to select a security type.
1. Enter the relevant credentials.
1. Click **Done**.
1. Click **Apply changes**.

After registering to the location, readers display a prompt to connect to the configured network. For readers that are already registered, the WiFi network might take up to 10 minutes to appear under `Configured networks` in the reader’s network settings screen.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/wifi?dashboard-or-api=api.

> For EAP-TLS networks, use the [Files](https://docs.stripe.com/api/files.md) API to upload certificate and private key files to Stripe and use the resulting `file_...` identifier in the configuration request. Use `terminal_wifi_certificate` as the file purpose for client and CA certificates, and `terminal_wifi_private_key` for the private key. Certificate and private key files must be in PEM format.

Create a `Configuration` object with WiFi using the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request. Set the WiFi type and the field with the corresponding name.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  wifi: {
    type: 'personal_psk',
    personal_psk: {
      ssid: 'Example network',
      password: 'password123',
    },
  },
});
```

To update an existing `Configuration` object to include WiFi or change the existing WiFi credentials, pass the type and new credentials into the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.update(
  'tmc_EjHtMwLT8HmATT',
  {
    wifi: {
      type: 'personal_psk',
      personal_psk: {
        ssid: 'New example network',
        password: 'password456',
      },
    },
  }
);
```
