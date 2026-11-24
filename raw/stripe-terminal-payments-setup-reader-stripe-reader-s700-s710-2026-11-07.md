<!-- Source URL: https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710 -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set up Stripe Reader S700/S710

Learn how to set up Stripe Reader S700/S710.
Available in: US, CA, GB, IE, SG, AU, NZ, FR, DE, NL, BE, AT, ES, DK, SE, NO, CH, IT, LU, PT, FI, MY, CZ, PL, JPAvailable in: AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, HK, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, MX, MY, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK, US
Visit the [Dashboard](https://dashboard.stripe.com/terminal/shop/) to order your Stripe Reader S700/S710.
![Front and back view of the Stripe Reader S700/S710](https://b.stripecdn.com/docs-statics-srv/assets/S700-3D.041eca5dfd580cdc451a41020b4dd45a.png)

Stripe Reader S700/S710 is an Android-based smart reader for countertop and handheld use. You can customize the on-reader checkout UI using a suite of prebuilt and custom elements.

The [Stripe Terminal SDK connects to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet) over the internet, LAN, or [handoff mode](https://docs.stripe.com/terminal/features/apps-on-devices/build.md#discover-and-connect-a-reader).

This reader is compatible with the following integrations:

- Server-driven
- JavaScript SDK
- iOS SDK (S710 requires v4.7.3 or later)
- Android SDK (S710 requires v3.8.0 or later)
- React Native SDK (S710 requires v0.0.1-beta.28 or later)

For Stripe Reader S700/S710, we recommend the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the [Stripe Reader S700 product sheet](https://stripe.com/s700/manual) or [Stripe Reader S710 product sheet](https://stripe.com/s710/manual).

## Turn the reader on and off

Connect the reader to power by plugging the provided USB-C cable into the port on the left side of your reader. Connect the opposite end of the USB-C cable to the provided power adapter and plug it into a power outlet. The Stripe Reader S700/S710 requires a recommended 12W of power to operate properly. Stripe power adapters and cables are recommended for the charging and operation of the S700/S710 and its accessories. Using alternative power adapters or cables might result in failure modes including inadequate S700/S710 charging, and might invalidate your product warranty.
![Side of Stripe Reader S700](https://b.stripecdn.com/docs-statics-srv/assets/s700-side-view.66affe17a0aeac5999a561f44d67bfbc.png)

Stripe Reader S700/S710

After the reader is fully charged, hold down the power button on the right side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option appears on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about 15 hours.

Even when not in use, leave Stripe Reader S700/S710 plugged in and powered on to receive automatic software updates.

## Access settings 

To open the settings menu, swipe right from the left edge of the reader screen. Tap **Settings** and enter the admin passcode `07139`. From here, you can update your WiFi settings or generate a pairing code for device registration. The battery status displays at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-button.6f47bb2572f4ac12b13286dde247ad88.png)

Settings button
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-admin-pin-screen.37e0ae6a621abb2c506db9ae762c8e91.png)

Admin PIN screen
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour improves battery performance. To update this value, go to the [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), select **Appearance**, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen or picking up the device), or when the device enters the payments flow and a payment is initiated.
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-appearance-menu.b83b814d09f1344e1407174e969def1c.png)

Appearance menu
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-timeout.4fa38fc09ee1092d47eb737d46155a15.png)

Timeout menu

## Connect the reader to the internet

Because the Stripe Reader S700/S710 is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven)). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the [troubleshooting steps](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md#troubleshooting) to diagnose the issue.

### WiFi

To connect to Wi-Fi or switch networks, go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), then select **Wi-Fi settings** to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection. Learn more about our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) and how to [configure advanced network settings](https://support.stripe.com/questions/bbpos-wisepos-e-stripe-reader-s700-advanced-network-settings) for supported Wi-Fi networks.

### Ethernet and USB Peripherals

Ethernet connectivity requires an optional hub, which provides wired 10/100 Ethernet connectivity and allows your smart reader to remain fully charged with the included charging cable. The hub also provides two USB-A ports to connect peripherals such as a barcode scanner and printer. The hub is compatible with the S700/S710 Dock for countertop applications. You can purchase the hub and dock separately in the [Stripe Dashboard](https://dashboard.stripe.com/terminal/shop).

To set up the hub:

1. Connect the Ethernet cable from your hub to your router.
2. Connect the hub to power through the built-in USB-C cable. We recommend using the power adapter included with your Stripe Reader S700/S710 to make sure the appropriate power is provided to the hub (27W) to power the reader and attached peripherals.
3. Connect the USB-C cable (provided with Stripe Reader S700/S710) to the hub and reader when both cables are in place. The right-angle USB-C connector connects to the reader.

To confirm the reader’s Ethernet connectivity, verify that the reader is charging and check if the Ethernet icon is visible in the status bar.
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-battery-icon.d1e81d69ea61041f809e60d79e25be54.png)

Charging icon
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-ethernet-icon.c5ae0533a503eb51ee9c8d587a854af0.png)

Ethernet icon

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.
![](https://b.stripecdn.com/docs-statics-srv/assets/USB_Ethernet_Hub_with_Dock_and_S700.a26b62b93fad05b1dcc65f74341f3447.png)

Hub when used with Dock (sold separately)
![](https://b.stripecdn.com/docs-statics-srv/assets/USB_Ethernet_Hub_with_S700.03e29d9d225b2677b7f86da50926ec25.png)

Hub with peripherals. Ethernet connected and power connected to Stripe Reader S700/S710.

For more information about these accessories, see [Stripe Reader S700/S710 accessories](https://docs.stripe.com/terminal/payments/stripe-reader-s700-s710/accessories.md).

### Cellular

Stripe Reader S710 supports cellular connectivity in addition to WiFi and Ethernet. See [Configure the cellular network](https://docs.stripe.com/terminal/fleet/cellular.md) for more details.

## Network priority

The Stripe Reader S700/S710 prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

If you dock the reader, but you don’t have an Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

For cellular-enabled Stripe Reader S710 devices, the reader prioritizes network connectivity in the following order: Ethernet, then WiFi, then cellular. This is managed at the Android level so no direct network management is necessary. To learn how network transitions affect payment processing and the SDK connection, see [Network transitions on cellular readers](https://docs.stripe.com/terminal/features/operate-offline/network-transitions.md).

## Change the UI appearance

By default, the user interface of your Stripe Reader S700/S710 reader uses a light theme.
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-welcome-screen.903f1751a4041eefd1840d9a5d2f110f.png)

Welcome screen
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-payment-screen.4dd5fc4be4c989e6af7bd1b2a635ba5d.png)

Payment screen
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-processing-screen.f99410ddc0d26e095ffdda92e953e7ac.png)

Processing screen
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-approved-screen.ae53ca99ba84aefbf2cb1aacf9ef1a2e.png)

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), then select **Appearance**, and select a new theme from the dropdown.
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-appearance-menu.b83b814d09f1344e1407174e969def1c.png)

Appearance menu
![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-theme.b07df3b6d20482df8790ecb9e19e8893.png)

Theme menu

## Change the default reader language

Stripe Reader S700/S710 supports changing the reader language in the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings) menu. Swipe right across the screen to access the settings menu, and select your language.

## Design your own accessories

You can design your own accessories for the Stripe Reader S700/S710. To download the Stripe Reader S700/S710 mechanical design files (.STP), you must first review and accept our [Terminal Design File License Agreement](https://stripe.com/legal/terminal-design). By downloading the file below, you agree to the terms outlined in the license.

[Download Stripe design files](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-and-Accessories-Design-Files.zip)

### Custom mounting attachment

If you’re interested in designing your own custom mounting attachment, see the [Stripe Reader S700/S710 Accessory Design Guidelines](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-Accessories-Design-Files-Mechanical-Usage-Guidelines.pdf).

## See also

- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [Stripe Reader S700/S710 reference](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md)
