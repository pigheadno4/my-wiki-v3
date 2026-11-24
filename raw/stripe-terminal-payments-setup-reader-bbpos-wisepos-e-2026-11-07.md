<!-- Source URL: https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set up BBPOS WisePOS E

Learn how to set up the BBPOS WisePOS E.
Available in: US, CA, GB, IE, SG, AU, NZ, FR, DE, NL, BE, AT, ES, DK, SE, NO, CH, IT, LU, PT, FI, MY, CZ, PL![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-floating-tall.e8478124cda0e088b2e19f503f574f53.png)

The BBPOS WisePOS E is a countertop reader for Stripe Terminal apps. The [Stripe Terminal SDK connects to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet) over the internet or LAN.

This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For BBPOS WisePOS E, we recommend the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the [BBPOS WisePOS E product sheet](https://docs.stripecdn.com/wpe-product-sheet.pdf).

> Stripe readers aren’t liquid-proof and we recommend that users make appropriate efforts to make sure their devices remain dry. If your device has experienced liquid ingress, we recommend that you stop using the device and let it dry thoroughly before attempting to re-use or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Turn the reader on and off 

> Some WisePOS E readers that shipped January 2026 or later have a pre-installed battery. The reader box includes a leaflet that indicates which readers this applies to.&nbsp;If you have a WisePOS E reader with a pre-installed battery, follow the charging instructions below.

When you first receive the device, install the battery. With the back of the device facing you, lift up from the indentation at the bottom left corner to detach the back cover. Insert the battery by sliding it into the exposed slot with the gold connectors at the top aligned. After the battery is in place, charge the reader by using an outlet or the optional ethernet dock. Connect the reader to power by plugging the provided cable into the port with the lightning bolt symbol.
![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-power.97a74f498008baacd6b6d88a30cd5dfc.jpg)

After the reader is fully charged, hold down the power button on the right hand side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option is shown on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about eight hours.

> Even when it’s not in use, leave the BBPOS WisePOS E plugged in and powered on to receive automatic software updates.

## Access settings 

To open the settings menu, swipe right from the left edge of the reader screen. Tap **Settings** and enter the admin passcode `07139`. From here, you can update your WiFi settings or generate a pairing code for device registration. The battery status displays at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.
![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-settings-panel.527bfcfb5009c6fe05b374b6f717fa00.png)

Settings button
![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-pin-screen.9a2fe095ebd9ef5bbfe92a12e405411e.png)

Admin PIN screen
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu

## Screen timeout 

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour improves battery performance. To update this value, go to the [settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings), select **Appearance**, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen), or when the device enters the payments flow and a payment is initiated.
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-appearance-menu.4abf84bd3fe14a1061eaed8b93d4bd70.png)

Appearance menu
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-timeout-menu.1b82032fea1418ca99c72a71c071b713.png)

Timeout menu

## Connect the reader to the internet 

Because the BBPOS WisePOS E is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven)). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the [troubleshooting steps](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md#troubleshooting) to diagnose the issue.

### WiFi

To connect to Wi-Fi or switch networks, go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings), then select **Wi-Fi settings** to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection. Learn more about our [network requirements](https://docs.stripe.com/terminal/network-requirements.md) and how to [configure advanced network settings](https://support.stripe.com/questions/bbpos-wisepos-e-stripe-reader-s700-advanced-network-settings) for supported Wi-Fi networks.

### Ethernet

Ethernet connectivity requires the use of an optional dock ([View dock product sheet](https://docs.stripecdn.com/wpe-dock.pdf)), which provides wired Ethernet connectivity and keeps your smart reader fully charged using the included charging cable. You can purchase the dock separately through the Stripe Dashboard. The Ethernet Dock features a 10/100 Ethernet port and rubber feet for stable countertop use.

To set up the dock:

- Connect the Ethernet cable from your dock to your router.
- Connect the dock to power. It has a minimum power requirement of 5V-2A (10W) and comes with a wall plug to USB-C charging cable.
- When both cables are connected, insert the reader into the dock.

To confirm that the reader is properly docked, verify the reader is charging and the Ethernet icon is visible in the status bar.
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-battery-icon.d1e81d69ea61041f809e60d79e25be54.png)

Charging icon
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-ethernet-icon.c5ae0533a503eb51ee9c8d587a854af0.png)

Ethernet icon

> The WisePOS E dock also ships with a USB-A to USB-C cable, which you can use to charge the dock with your own USB-A power adapter if you prefer. We recommend charging with the dock wall plug to USB-C charging cable.

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.
![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-ethernet-dock.340a1e6d1be6fcab4fd2d577d79e5939.png)

## Network priority

The BBPOS WisePOS E prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

If you dock the reader, but you don’t have an Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

## Change the UI appearance 

By default, the user interface of your BBPOS WisePOS E reader uses a dark theme.
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-splash-screen.319df062b5b694a4ec91e1c309c48e48.png)

Welcome screen
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-pay.fdf5e2100ca53b54e100a28b8589b1d1.png)

Payment screen
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-subtotal.50779461be74aa98f600aef3e7715a16.png)

Tipping selection screen*
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-total.eb4f25263c136bed268f68a6f5e82933.png)

Total screen
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-approved.6eb33af4ca019de7621d07363e24dd8e.png)

Approved screen

\*The tipping selection screen appears if [on-reader tipping](https://docs.stripe.com/terminal/features/collecting-tips/on-reader.md) is configured.

You can change the appearance of the UI to use a different theme in the settings menu. Go to [settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings), then select **Appearance**, and select a new theme from the dropdown.
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-appearance-menu.4abf84bd3fe14a1061eaed8b93d4bd70.png)

Appearance menu
![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-theme-menu.fc7bd14827a7767e62c9f1bcd49110fa.png)

Theme menu

## Change the default reader language 

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) supports changing the reader language in the settings menu. Swipe right across the screen to access the settings menu, and select your language.

## Accessories for the reader 

You can design your own accessories for the BBPOS WisePOS E. To download the BBPOS WisePOS E mechanical design files (.STP), you must first review and accept our [Terminal Design File License Agreement](https://stripe.com/legal/terminal-design). By downloading the file below, you agree to the terms outlined in the license.

[Download Stripe design files](https://d37ugbyn3rpeym.cloudfront.net/terminal/bbpos_wpe_mechanical_design_files_and_guidelines.zip)

## Device specifications 

The following table provides the specifications for the BBPOS WisePOS E. The battery life is only an estimate. The actual battery life varies depending on product settings and deployed features.

| Spec | Details |
| --- | --- |
| Approximate dimensions | 188.6 x 76.2 x 32.7 mm / 7.43 x 3 x 1.29 in |
| Approximate weight | 318g |
| Display | 5" IPS display capacitive touch screen |
| Battery capacity | Rechargeable Li-polymer, 3.7v, 3,200mAh |
| Battery life | 2.75 hours time to charge, 250 hours (standby), 12 hours (active use) |
| Memory | 2GB RAM |
| Storage | 16GB |
| Processor | Quad Core Cortex A7 |
| Charging connection | Micro-USB port, Accessory dock |
| Communication interface | WiFi, Ethernet (with optional dock) |
| Operating system | Android 9 |
| Camera | Rear present but not supported |
| Audio jack | Supported |
| Microphone | Front and rear present but not supported |
| Security | End-to-end encryption, P2PE ready, Mail order telephone order (MO/TO) P2PE. [PCI listing](https://listings.pcisecuritystandards.org/popups/pts_device.php?appnum=4-90102) |
| Accessories | Dock |

## See also

- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [WisePOS E reference](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks doesn’t imply any endorsement by BBPOS or Verifone.
