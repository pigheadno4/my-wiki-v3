<!-- Source: Stripe Terminal — Set up Verifone UX700 reader -->
<!-- Fetched: 2026-04-24 -->

# Verifone UX700 reader

Learn how to set up the Verifone UX700 reader.

> Verifone UX700 reader support is in public preview for the US and CA. To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

> Verifone UX700 reader support is in private preview for Ireland and the United Kingdom. To join the preview, you must [contact the Sales team to order the applicable reader](https://stripe.com/contact/sales).

The Stripe Terminal SDK connects to the reader over the internet, LAN, or handoff mode. This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For the UX700, we recommend the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the [UX700 product sheet](https://docs.stripe.com/terminal/readers/product-sheets.md).

## Turn the reader on and off

Connect the reader to power by plugging the 4-pin cable into the 6-pin port on the back of your UX700 reader. Plug the power adapter into a power outlet. Use of power adapters other than the one supplied from Verifone might invalidate your product warranty.
![Verifone UX700](assets/stripe-terminal-ux700-power.png)

Power button

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen to reveal a **Settings** button. Tap the **Settings** button and enter the admin pin `07139`. From here, you can update your WiFi settings or generate a pairing code for device registration. To close the settings menu, touch the back arrow in the top left corner.
![](assets/stripe-terminal-s700-settings-button.png)

Settings button
![](assets/stripe-terminal-s700-admin-pin-screen.png)

Admin PIN screen
![](assets/stripe-terminal-s700-settings-menu.png)

Settings menu

## Connect the reader to the internet

Because the UX700 is a smart reader, its reader software communicates directly with Stripe. The UX700 can connect to the internet using WiFi or Ethernet. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven)).

When communicating with the reader through the LAN, you must connect the reader to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, see the [UX700 troubleshooting guide](https://docs.stripe.com/terminal/readers/reference/ux700.md).

### WiFi

To connect to WiFi or switch networks, go to the network and WiFi settings, choose the network, and connect. Attempting to join a new network disconnects the reader from any existing wireless connection. To learn more about supported WiFi networks, see [Network requirements](https://docs.stripe.com/terminal/network-requirements.md).

### Ethernet

The UX700 reader provides wired 10/100 Ethernet connectivity.
![](assets/stripe-terminal-ux700-ethernet.png)

Ethernet connector

To set up Ethernet connectivity:

1. Connect the Ethernet cable from the UX700’s Ethernet port to your router.
1. Make sure the device is connected to the power adapter and powered on.

To confirm the reader’s Ethernet connectivity, make sure the Ethernet icon is visible in the status bar.

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.
![](assets/stripe-terminal-s700-battery-icon.png)

Charging icon
![](assets/stripe-terminal-s700-ethernet-icon.png)

Ethernet icon

For more information about the UX700’s accessories, see [Verifone accessories](https://docs.stripe.com/terminal/payments/verifone/accessories.md).

### Network priority

The UX700 prioritizes connecting through Ethernet if possible. If an Ethernet cable is connected, the reader uses the wired connection. If you disconnect the Ethernet cable, it switches back to the WiFi connection if configured.

## Change the UI appearance

By default, the UI of the UX700 reader uses a light theme.
![](assets/stripe-terminal-s700-welcome-screen.png)

Welcome screen
![](assets/stripe-terminal-s700-payment-screen.png)

Payment screen
![](assets/stripe-terminal-s700-processing-screen.png)

Processing screen
![](assets/stripe-terminal-s700-approved-screen.png)

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/ux700.md#settings), then select **Appearance**, and select a new theme from the dropdown.
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
