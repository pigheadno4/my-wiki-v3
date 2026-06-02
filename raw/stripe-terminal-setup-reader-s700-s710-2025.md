<!-- Source: Stripe Terminal — Set up Stripe Reader S700/S710 -->
<!-- Fetched: 2026-04-23 -->

# Set up Stripe Reader S700/S710

Learn how to set up Stripe Reader S700/S710.
Available in: US, CA, GB, IE, SG, AU, NZ, FR, DE, NL, BE, AT, ES, DK, SE, NO, CH, IT, LU, PT, FI, MY, CZ, PL, JPAvailable in: US, CA, GB, IE, SG, AU, NZ, FR, BE, AT, ES, SE, NO, PT, FI, MY
Visit the [Dashboard](https://dashboard.stripe.com/terminal/shop/) to order your Stripe Reader S700/S710.
![Front and back view of the Stripe Reader S700/S710](assets/stripe-terminal-s700-3d-view.png)

Stripe Reader S700/S710 is an Android-based smart reader for countertop and handheld use. You can customize the on-reader checkout UI using a suite of pre-built and custom elements.

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
![Side of Stripe Reader S700](assets/stripe-terminal-s700-side-view.png)

Stripe Reader S700/S710

After the reader is fully charged, hold down the power button on the right side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option appears on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about 15 hours.

Even when not in use, leave Stripe Reader S700/S710 plugged in and powered on to receive automatic software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen. Tap **Settings** and enter the admin passcode `07139`. From here, you can update your WiFi settings or generate a pairing code for device registration. The battery status displays at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.
![](assets/stripe-terminal-s700-settings-button.png)

Settings button
![](assets/stripe-terminal-s700-admin-pin-screen.png)

Admin PIN screen
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour improves battery performance. To update this value, go to the [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), select **Appearance**, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen or picking up the device), or when the device enters the payments flow and a payment is initiated.
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu
![](assets/stripe-terminal-s700-appearance-menu.png)

Appearance menu
![](assets/stripe-terminal-s700-settings-timeout.png)

Timeout menu

## Connect the reader to the internet

Because the Stripe Reader S700/S710 is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven)). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the [troubleshooting steps](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md#troubleshooting) to diagnose the issue.

### WiFi

To connect to WiFi or switch networks, go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), then select **WiFi settings** to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection. Learn more about our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) and how to [configure advanced network settings](https://support.stripe.com/questions/bbpos-wisepos-e-stripe-reader-s700-advanced-network-settings) for supported WiFi networks.

### Ethernet and USB Peripherals

Ethernet connectivity requires an optional hub, which provides wired 10/100 Ethernet connectivity and allows your smart reader to remain fully charged with the included charging cable. The hub also provides two USB-A ports to connect peripherals such as a barcode scanner and printer. The hub is compatible with the S700/S710 Dock for countertop applications. You can purchase the hub and dock separately in the [Stripe Dashboard](https://dashboard.stripe.com/terminal/shop).

To set up the hub:

1. Connect the Ethernet cable from your hub to your router.
1. Connect the hub to power through the built-in USB-C cable. We recommend using the power adapter included with your Stripe Reader S700/S710 to make sure the appropriate power is provided to the hub (27W) to power the reader and attached peripherals.
1. Connect the USB-C cable (provided with Stripe Reader S700/S710) to the hub and reader when both cables are in place. The right-angle USB-C connector connects to the reader.

To confirm the reader’s Ethernet connectivity, verify that the reader is charging and check if the Ethernet icon is visible in the status bar.
![](assets/stripe-terminal-s700-battery-icon.png)

Charging icon
![](assets/stripe-terminal-s700-ethernet-icon.png)

Ethernet icon

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.
![](assets/stripe-terminal-s700-ethernet-hub-with-dock.png)

Hub when used with Dock (sold separately)
![](assets/stripe-terminal-s700-ethernet-hub-peripherals.png)

Hub with peripherals. Ethernet connected and power connected to Stripe Reader S700/S710.

For more information about these accessories, see [Stripe Reader S700/S710 accessories](https://docs.stripe.com/terminal/payments/stripe-reader-s700-s710/accessories.md).

### Cellular

Stripe Reader S710 supports cellular connectivity in addition to WiFi and Ethernet. See [Configure the cellular network](https://docs.stripe.com/terminal/fleet/cellular.md) for more details.

## Network priority

The Stripe Reader S700/S710 prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

If you dock the reader, but you don’t have an Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

For cellular-enabled Stripe Reader S710 devices, the reader prioritizes network connectivity in the following order: Ethernet, then WiFi, then cellular. This is managed at the Android level so no direct network management is necessary.

## Change the UI appearance

By default, the user interface of your Stripe Reader S700/S710 reader uses a light theme.
![](assets/stripe-terminal-s700-welcome-screen.png)

Welcome screen
![](assets/stripe-terminal-s700-payment-screen.png)

Payment screen
![](assets/stripe-terminal-s700-processing-screen.png)

Processing screen
![](assets/stripe-terminal-s700-approved-screen.png)

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-s700-s710.md#settings), then select **Appearance**, and select a new theme from the dropdown.
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu
![](assets/stripe-terminal-s700-appearance-menu.png)

Appearance menu
![](assets/stripe-terminal-s700-settings-theme.png)

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
