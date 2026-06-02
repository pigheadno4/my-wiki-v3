<!-- Source: Stripe Terminal — Set up Verifone V660p reader -->
<!-- Fetched: 2026-04-24 -->

# Verifone V660p reader

Learn how to set up the Verifone V660p reader.

> Verifone V660p reader support is in public preview for the US and CA. To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

> Verifone V660p reader support is in private preview for Ireland, the United Kingdom, and Singapore. To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

The Stripe Terminal SDK connects to the reader over the internet, LAN, or handoff mode. This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For the V660p, we recommend the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the [V660P product sheet](https://docs.stripe.com/terminal/readers/product-sheets.md).

## Turn the reader on and off

Connect the reader to power by plugging the provided USB-C cable into the port on the left side of your reader. Connect the opposite end of the USB-C cable to the provided power adapter and plug it into a power outlet. The V660p requires 11W of power to operate properly. Verifone power adapters and cables are recommended for the charging and operation of the V660p and its accessories. Using alternative power adapters or cables might result in failure modes, including inadequate V660p charging, and can invalidate your product warranty.
![Verifone V660p](assets/stripe-terminal-v660p-power.png)

Power button

Charge the V660p device for eight hours before initial use. After the reader is fully charged, hold the start button for about 3 seconds until the device displays the startup screen. Don’t let the battery charge fall below 10% for an extended period of time, because that can permanently diminish the battery capacity.

Hold the start button for about 1 second until the message is displayed on the screen. Touch the “Off” selection to turn it off.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about 10 hours or up to 72 hours in standby mode. Even when not in use, leave the V660p plugged in and powered on to receive automatic Stripe software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen to reveal a **Settings** button. Tap the **Settings** button and enter the admin pin `07139`. From here, you can update your WiFi settings or generate a pairing code for device registration. Battery status appears at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.
![](assets/stripe-terminal-s700-settings-button.png)

Settings button
![](assets/stripe-terminal-s700-admin-pin-screen.png)

Admin PIN screen
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour improves battery performance. To update this value, go to the settings, select **Appearance**, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen or picking up the device), or when the device enters the payments flow and a payment is initiated.

## Connect the reader to the internet

Because the V660p is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven)).

When communicating with the reader through the LAN, you must connect the reader to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, see the [V660p troubleshooting guide](https://docs.stripe.com/terminal/readers/reference/v660p.md).

### WiFi

To connect to WiFi or switch networks, go to the network and WiFi settings, choose the network, and connect. Attempting to join a new network disconnects the reader from any existing wireless connection. To learn more about supported WiFi networks, see [Network requirements](https://docs.stripe.com/terminal/network-requirements.md).

### Ethernet and USB Peripherals

Ethernet connectivity requires the optional Full Feature Base, which provides wired 10/100 Ethernet connectivity and allows your smart reader to remain fully charged with the charging cable. The Full Feature Base also provides two USB-A ports to connect peripherals. You can purchase the Full Feature Base separately in the [Dashboard](https://dashboard.stripe.com/terminal/shop).

To set up the feature base:

1. Connect the Ethernet cable from the feature base to your router.
1. Connect the feature base to power through the power adapter via the barrel connector. We recommend using the power adapter included with your Verifone V660p to make sure the appropriate power is provided to the feature base and attached peripherals.

To confirm the reader’s Ethernet connectivity, verify that the reader is charging and check whether the Ethernet icon is visible in the status bar.
![](assets/stripe-terminal-s700-battery-icon.png)

Charging icon
![](assets/stripe-terminal-s700-ethernet-icon.png)

Ethernet icon

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.
![](assets/stripe-terminal-v660p-accessories.png)

V660P and the Full Feature Base

For more information about these accessories, see [Verifone accessories](https://docs.stripe.com/terminal/payments/verifone/accessories.md).

### Network priority

The V660p prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

If you dock the reader, but you don’t have an Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

## Change the UI appearance

By default, the UI of the V660p reader uses a light theme.
![](assets/stripe-terminal-s700-welcome-screen.png)

Welcome screen
![](assets/stripe-terminal-s700-payment-screen.png)

Payment screen
![](assets/stripe-terminal-s700-processing-screen.png)

Processing screen
![](assets/stripe-terminal-s700-approved-screen.png)

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/v660p.md#settings), then select **Appearance**, and select a new theme from the dropdown.
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu
![](assets/stripe-terminal-s700-appearance-menu.png)

Appearance menu
![](assets/stripe-terminal-s700-settings-theme.png)

Theme menu

## Change the default reader language

Access your settings and find the language settings. Select the new language and confirm the change. You might need to restart the device for the change to take effect.

## See also

- [Verifone accessories](https://docs.stripe.com/terminal/payments/verifone/accessories.md)
- [Verifone product sheets](https://docs.stripe.com/terminal/readers/product-sheets.md)
