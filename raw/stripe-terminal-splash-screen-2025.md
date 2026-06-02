<!-- Source URL: https://docs.stripe.com/terminal/fleet/splash-screen -->
<!-- Fetched: 2026-05-01 -->

# Configure readers with a custom splash screen

Customize the default splash screen for your readers.

A splash screen is the default screen that displays when your reader is ready to accept payments. You can set a custom splash screen for these readers in one of two ways:

- In the Dashboard
- Using the Configuration API

You can configure an account default splash screen, which applies to all readers in your fleet. You can also configure a custom splash screen for individual locations, which overrides the splash screen configured at the account level. Locations without a custom splash screen inherit the account default splash screen.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/terminal/fleet/splash-screen?dashboard-or-api=dashboard.

To update the splash screen, go to the relevant configuration you want to change and edit it. If adding a new configuration, create a new one first.

## From the location details page

1. Go to the [Terminal Locations](https://dashboard.stripe.com/terminal/locations) page.
1. Click the specific location you want to change the passcode for.
1. Click the edit icon (✏) next to the **Splash screen** row for your selected reader type under **Local configurations** or **Inherited configurations**.
   - You can’t upload or apply a single splash screen across every reader type.
1. Upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.
1. Click **Done**.
1. Review the final configuration for the location, and apply the configuration changes by clicking **Apply changes** on the configuration drawer.

## From the manage locations page

1. Go to the [Manage locations](https://dashboard.stripe.com/terminal/locations/manage) page.
1. Find the specific location you want to change.
1. Click the overflow menu (⋯) > **Edit configuration**.
1. Click **Edit** or **Override** next to the **Splash screen** icon.
1. Select the reader type (for example, S700, S710, BBPOS WisePOS E) to indicate which reader type to apply the splash screen to.
   - You can’t upload or apply a single splash screen across every reader type.
1. Upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.
1. Click **Done**.
1. Apply the configuration changes by clicking **Apply changes** on the configuration drawer.

> The BBPOS WisePad 3 can only use PNG images for the splash screen. Due to hardware specifications, BBPOS WisePad 3 splash screen images are automatically converted to black and white, and repositioned slightly.

> GIF files under 4 MB might still fail to upload. If this occurs, reduce the file size further by manually deleting frames. Try reducing the GIF’s frame count by 50% until the upload succeeds.

| Reader          | Resolution (W x H) | Accepts GIF |
| --------------- | ------------------ | ----------- |
| Stripe S700     | 1080 x 1920        | ✓ Supported |
| Stripe S710     | 1080 x 1920        | ✓ Supported |
| BBPOS WisePOS E | 720 x 1280         | ✓ Supported |
| Verifone P400   | 320 x 480          | –           |
| BBPOS WisePad 3 | 320 x 240          | –           |

After uploading, save the changes and apply the configuration. For [mobile readers](https://docs.stripe.com/terminal/mobile-readers.md), the splash screen updates when it’s connected to the Stripe Terminal SDK. For [smart readers](https://docs.stripe.com/terminal/smart-readers.md), the splash screen updates on the reader within 10 minutes.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/terminal/fleet/splash-screen?dashboard-or-api=api.

Use the Configuration API to specify settings and set a custom splash screen for your Stripe Reader 700, Stripe Reader 710, BBPOS WisePOS E, BBPOS WisePad 3, or Verifone P400.

1. Upload a file.
1. Create or update a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object.

## Upload a file

Use the [File Upload API](https://docs.stripe.com/file-upload.md) to upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.

> GIF files under 4 MB might still fail to upload. If this occurs, reduce the file size further by manually deleting frames. Try reducing the GIF’s frame count by 50% until the upload succeeds.

| Reader          | Resolution (W x H) | Accepts GIF |
| --------------- | ------------------ | ----------- |
| Stripe S700     | 1080 x 1920        | ✓ Supported |
| Stripe S710     | 1080 x 1920        | ✓ Supported |
| BBPOS WisePOS E | 720 x 1280         | ✓ Supported |
| Verifone P400   | 320 x 480          | –           |
| BBPOS WisePad 3 | 320 x 240          | –           |

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const fp = fs.readFileSync('/path/to/a/file.jpg');
const upload = await stripe.files.create({
  file: {
    data: fp,
    name: 'file.jpg',
    type: 'application.octet-stream',
  },
  purpose: 'terminal_reader_splashscreen',
});
```

## Create or update a Configuration object

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object to set the custom splash screen for your specified device type. The supported device types are `stripe_s700`, `stripe_s710`, `bbpos_wisepos_e`, `bbpos_wisepad3`, and `verifone_p400`.

> Stripe automatically provisions an account default configuration for you. You can optionally create a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object for another configuration, or you can continue to the next step to apply the default configuration settings to the entire account.

To create a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object, use the [create configuration](https://docs.stripe.com/api/terminal/configuration/create.md) request:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const configuration = await stripe.terminal.configurations.create({
  stripe_s700: {
    splashscreen: 'file_1KjBJdE7XUJuZdf0F6GgO9uY',
  },
});
```

To update a [Configuration](https://docs.stripe.com/api/terminal/configuration.md) object, use the [update configuration](https://docs.stripe.com/api/terminal/configuration/update.md) request:

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
