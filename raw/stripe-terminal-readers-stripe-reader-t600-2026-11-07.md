<!-- Source URL: https://docs.stripe.com/terminal/readers/stripe-reader-t600 -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Stripe Reader T600

Learn about Stripe Reader T600.

Visit the [Dashboard](https://dashboard.stripe.com/terminal/shop/) to order your Stripe Reader T600.

The [Stripe Reader T600](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md) is an Android-based smart reader made specifically for countertop and pole-mount use. You can customize the on-reader checkout UI using both prebuilt and custom elements.

The [Stripe Terminal SDK connects to the reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=internet) over the internet, LAN, or [handoff mode](https://docs.stripe.com/terminal/features/apps-on-devices/build.md#discover-and-connect-a-reader). This reader is compatible with JavaScript SDK, iOS SDK, Android SDK, React Native SDK, and server-driven integrations.

If you use the Stripe Reader T600 with a point-of-sale system on a separate device and don’t need to [collect card payments while offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments.md), we recommend the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven).

## Expected sounds during payment

The following table describes sounds that occur during successful and failed payments on Stripe Reader T600.

|  | Tap | Chip | Swipe |
| --- | --- | --- | --- |
| Success | One long, high-pitched beep | No sound | Not applicable |
| Failure | Two short, low-pitched beeps | No sound | Two short beeps |

## Troubleshoot the reader 

Make sure your network meets all of our [network requirements](https://docs.stripe.com/terminal/network-requirements.md), and try the steps in the [network troubleshooting](https://docs.stripe.com/terminal/network-requirements.md#troubleshooting) section.

To begin troubleshooting, use the following common scenarios to help diagnose the issue.

### Run diagnostics 

The Stripe Reader T600 includes built-in diagnostics that can help you identify connectivity and configuration issues. We recommend running these diagnostics as the first step when troubleshooting any reader problems.

To access the diagnostics menu:

1. Swipe in from the left edge of the screen on your reader.
2. Tap **Settings**.
3. Enter the admin passcode. The default is **0-7-1-3-9**.
4. Select **Diagnostics**.

The diagnostics menu displays test results and information about your reader:

- **DNS resolution**: Verifies that the reader can resolve domain names.
- **Stripe connectivity**: Verifies that the reader can connect to Stripe servers. This test must pass for your reader to process payments and receive updates.
- **Terminal events connectivity**: Tests the reader’s connection to the Stripe event infrastructure.
- **WiFi information**: Shows WiFi frequency and signal strength (if connected using WiFi).
- **Hardware status**: Displays hardware health and hub connection status.

> If the Stripe connectivity test fails, your reader won’t be able to process payments or receive software updates. Follow the [network troubleshooting steps](https://docs.stripe.com/terminal/network-requirements.md#troubleshooting) to resolve connectivity issues.

We recommend running diagnostics whenever you experience issues with your reader, or as part of your regular maintenance routine to proactively identify potential problems.

### The reader won’t turn on 

The Stripe Reader T600 requires a recommended 20W of power for successful operation. The reader doesn’t contain a battery, so make sure you have a proper USB connection to the power supply. Refer to [Turn the reader on and off](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md#turn-the-reader-on-and-off) for proper routing and connection of the USB-C cable and the power button location.

Stripe recommends using the AC power adapter that was supplied with your reader to make sure ample power is supplied to the reader for operation. You can order a replacement power adapter in the [Dashboard](https://dashboard.stripe.com/terminal/shop/).

If you’re connecting the Stripe Reader T600 to a computer or laptop, make sure the USB-C port can support the recommended 20W of power. The USB-A port standard *does not* support this power level—*don’t* use it.

### The reader can’t connect 

To check connectivity, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md#settings) and select **Network**. This displays all available WiFi networks. To see more details about the connection, tap the connected network name.

To check WiFi signal strength, select **Advanced** -> **Diagnostics**. This displays diagnostic information about the reader including specific network information helpful in troubleshooting connection issues.

If you’re experiencing connectivity issues, run the [diagnostics tests](https://docs.stripe.com/terminal/readers/stripe-reader-t600.md#diagnostics) to check Stripe connectivity and identify the root cause.

### The reader won’t update 

If your reader doesn’t update, it’s possible that it can’t connect to Stripe. Run the [diagnostics tests](https://docs.stripe.com/terminal/readers/stripe-reader-t600.md#diagnostics) to check Stripe connectivity. Make sure the Stripe connectivity test says `Passed`. If the test fails, follow the [troubleshooting steps](https://docs.stripe.com/terminal/readers/stripe-reader-t600.md#troubleshooting).

If you use a router, refer to your router’s manual and reconfigure the networking setup.

## Stripe reader software 

Stripe maintains the software that controls the Stripe Reader T600. The reader receives updates automatically from Stripe when not in use. These can include improvements and required security updates from Stripe and our hardware partners. As reader software updates are made available, update your readers to the latest available version to continue using Stripe Terminal. Failing to install a required update can prevent a reader from accepting payments.

The reader restarts every day at midnight for PCI compliance, and disconnects from the POS app every morning. Leave your reader connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the time zone of the [assigned location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md)) to avoid interruption to sales. If you disconnect the reader from power at night, an update could start when you power it back on. To manually check for an update, reboot the reader.

### Reader software version 

The Stripe Reader T600 software consists of four components: the reader application, firmware, configuration, and ROM. The following table summarizes the latest version of each of these components for the countries where the Stripe Reader T600 is available. You can find your reader’s versions in the [Diagnostics menu](https://docs.stripe.com/terminal/readers/stripe-reader-t600.md#diagnostics).

> In PCI listings, the firmware identifier is in the format `STT6x-11-xxxxx-xxxxx`, where `xxxxx` is a placeholder for ROM version and firmware version, respectively. All versions are PCI compliant.
> 
> Specifically, a PCI firmware ID `STT6x-11-WXYZZ-ABCDD` maps to ROM version `W.X.Y.ZZ` and firmware version `AA.BB.CC.DD.SZZZ.07`. For example, `STT6x-11-22404-10016` maps to ROM version `2.2.4.4` and firmware version `1.00.00.16`. If the ROM version only has three digits `W.X.Y`, `ZZ` is `00`.

| Countries | Reader | Firmware | Configuration | ROM |
| --- | --- | --- | --- | --- |
| US | `2.44.1.0` | `1.00.06.00` | `szzz_us_v5` | `2.2.22` |
| CA | `2.44.1.0` | `1.00.06.00` | `szzz_ca_v2` | `2.2.22` |
| AU | `2.44.1.0` | `1.00.06.00` | `szzz_au_v5` | `2.2.22` |
| MYSG | `2.44.1.0` | `1.00.06.00` | `szzz_prod_apac_on_v1` | `2.2.22` |
| HK | `2.45.9.0` | `1.00.07.01` | `szzz_hk_v3` | `3.0.20.1` |
| NZ | `2.44.1.0` | `1.00.06.00` | `szzz_nz_v2` | `2.2.22` |
| GB | `2.44.1.0` | `1.00.06.00` | `szzz_gb_v3` | `2.2.22` |
| FI | `2.44.1.0` | `1.00.06.00` | `szzz_fi_v2` | `2.2.22` |
| FR | `2.44.1.0` | `1.00.06.00` | `szzz_fr_v1` | `2.2.22` |
| ATBECZDKIEITLUNLNOPTESSECH | `2.44.1.0` | `1.00.06.00` | `szzz_prod_eu_on_v1` | `2.2.22` |
| PL | `2.44.1.0` | `1.00.06.00` | `szzz_pl_v2` | `2.2.22` |

### Firmware versions 

| Version | Release date | Description |
| --- | --- | --- |
| `1.00.06.00` | `2026-08-04` | - General bug fixes and improvements. |
| `1.00.05.00` | `2026-06-30` | - General bug fixes and improvements. |
| `1.00.04.00` | `2026-05-26` | - General bug fixes and improvements. |
| `1.00.03.00` | `2026-04-20` | - General bug fixes and improvements. |
| `1.00.02.00` | `2026-03-18` | - General bug fixes and improvements. |
| `1.00.01.00` | `2026-02-24` | - General bug fixes and improvements. |

## Device specifications 

The following table provides the specifications for the Stripe Reader T600.

| Spec | Details |
| --- | --- |
| Approximate dimensions | Tablet face: 205 x 139 mm / 8.1 x 5.47 in. Height: 25 mm / 0.98 in (bare or VESA mount), 57 mm / 2.25 in (with base attached) |
| Approximate weight | 500g |
| Display | 8.0" IPS LCD display with Dragontrail glass, 1280 x 800, 500 nit |
| Power | USB-C powered |
| Memory | 4GB RAM |
| Storage | 64GB |
| Processor | Qualcomm SM6125 |
| Charging connection | USB-C port |
| Communication interface | WiFi, Ethernet (with optional hub) |
| Operating system | Android 15 |
| Camera | 5MP front-facing (future support) |
| Audio jack | Supported |
| Security | End-to-end encryption, P2PE ready, PCI 6.x |
| Accessories | Reader Hub, T-bridge, Third-party VESA stand |

## See also

- [Set up Stripe Reader T600](https://docs.stripe.com/terminal/payments/setup-reader/stripe-reader-t600.md)
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md)
- [Collect payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks doesn’t imply any endorsement by BBPOS or Verifone.
