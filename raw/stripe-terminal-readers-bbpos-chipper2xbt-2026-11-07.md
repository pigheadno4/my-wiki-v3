<!-- Source URL: https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# BBPOS Chipper 2X BT

Learn about the BBPOS Chipper 2X BT reader.

> #### No longer supported
> 
> This reader is no longer available for purchase. If you’re getting started with Stripe Terminal, we recommend [viewing our supported reader offerings](https://docs.stripe.com/terminal/payments/setup-reader.md).
![](https://b.stripecdn.com/docs-statics-srv/assets/bbpos-photo-no-white.bf21912a012f27483d48a968515d723c.png)

The [BBPOS Chipper 2X BT](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-chipper2xbt.md) is a handheld reader for use with mobile applications. It uses [Bluetooth Low Energy (LE)](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth) or [USB](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=android&reader-type=usb) (Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the [BBPOS Chipper 2X BT product sheet](https://docs.stripecdn.com/c2xbt-product-sheet.pdf).

## LED status lights 

The LEDs on the reader show the current reader and NFC status.

### Reader status

When you turn on the BBPOS Chipper 2X BT, the LED located beside the power button shows the reader’s current status.

| Light | Meaning |
| --- | --- |
| **None** | The reader is off. |
| **Flashing blue every second** | The reader is on and ready to connect to a device. It turns off after 5 minutes if it doesn’t connect. |
| **Multicolored flashing** | The reader has been discovered using [Bluetooth Proximity](https://docs.stripe.com/terminal/payments/connect-reader.md?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity) or USB (Android only) and is ready to connect. |
| **Steady blue** | The reader is connected to a device. |
| **Flashing blue every 5 seconds** | The reader is in standby mode. It remains in standby indefinitely. |
| **Alternating red and magenta** | The reader is charging. |
| **Flashing red** | The reader’s battery is low. |
| **Rapidly flashing blue and orange** | The reader has finished installing a software update. If the reader is unresponsive after the update completes, restart the reader by turning it off and on. |

### NFC status

The LEDs above the NFC marking show the NFC reading status.

### LED icon meanings

Use this table to understand what the icons in the subsequent table indicate.

| Icon | Meaning |
| --- | --- |
|  | The light is on. |
|  | The light is flashing. |
|  | The light is off. |

| LEDs | Meaning |
| --- | --- |
|  | (flashing) The reader is connecting to the POS terminal. |
|  | The reader is ready for tapping a card. |
|  | (LEDs on in consecutive order) The reader is reading card information. |
|  | (LEDs and one beep sound) The reader has successfully read the card. |
|  | (No LEDs and one beep sound) The transaction is complete. |
|  | (No LEDs and two beep sounds) Retry tapping a card. |

### Reader software releases 

- [deviceSoftwareVersion (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReader.html#/c:objc\(cs\)SCPReader\(py\)deviceSoftwareVersion)
- [softwareVersion (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader/software-version.html)

The software on the BBPOS Chipper 2X BT consists of a firmware version, configuration name, and key identifier. The reader **software version** joins these three components with underscores into a single string.

Note there are 3 different revisions to the BBPOS Chipper 2X BT. The first 6 characters in the serial number identifies which revision you have.

#### CHB20

| Latest Version |
| --- |
| `1.00.03.50-SZZZ_Generic_v47-300001` |

### Changelog

#### Firmware versions 

| Version | Release Date | Description |
| --- | --- | --- |
| `1.00.03.50` | `2023-07-24` | Maintenance updates. |
| `1.00.03.49` | `2022-08-30` | Maintenance updates. |
| `1.00.03.48` | `2022-05-05` | USB connectivity improvements and maintenance updates. |
| `1.00.03.47` | `2022-02-23` | Bluetooth connectivity improvements and maintenance updates. |
| `1.00.03.34.921a53dc` | `2021-10-20` | Updates reader CAPK keys. You must install before December 31, 2021 to continue accepting payments. |
| `1.00.03.34` | `2018-11-29` | Adds the ability for the reader to beep when a card is inserted. |
| `1.00.03.32` | `2018-09-20` |  |
| `1.00.02.31` | `2018-08-02` |  |
| `1.00.02.30` |  | The initial firmware version available for this device. |

#### Configurations 

| Name | Release Date | Description |
| --- | --- | --- |
| `SZZZ_Generic_v47` | `2023-07-24` | Updates production configuration for this device. |
| `SZZZ_Generic_v46` | `2021-09-13` | Enables contactless during `collectSetupIntentPaymentMethod`. |
| `SZZZ_Generic_v45` | `2020-08-06` | Fixes a bug in which the Chipper 2X BT no longer gave audible feedback on chip transactions |
| `SZZZ_Generic_v44` | `2020-06-25` | Updates American Express CVM contactless limit to 200 USD due to Covid-19. |
| `SZZZ_Generic_v40` | `2019-05-29` | Fixes an issue where certain Amex contactless transactions couldn’t be read. |
| `SZZZ_Generic_v37` | `2018-11-20` | Enables beeps when a card is inserted, the transaction is complete, and when a card is left in the reader. |
| `SZZZ_Generic_v36` | `2018-09-28` | Enabled card insert and removal detection outside of a transaction. |
| `SZZZ_Generic_v35` |  | The initial configuration available for this device. |

#### Key identifiers 

| Identifier | Release Date | Description |
| --- | --- | --- |
| `30000` |  | The initial key identifier available for this device. |
| `300001` | `2020-06-30` | An alias for `30000` that might be visible in newer Terminal SDK versions. |

#### CHB20Y

| Latest Version |
| --- |
| `1.03.00.07-SZZZ_Generic_Y_v3-300001` |

#### Firmware versions 

| Version | Release Date | Description |
| --- | --- | --- |
| `1.03.00.07` | `2023-07-24` | Maintenance updates. |
| `1.03.00.05` | `2022-05-05` | USB connectivity improvements and maintenance updates. |
| `1.03.00.02.5cc80c4b` | `2021-10-20` | Updates reader CAPK keys. You must install before December 31, 2021 to continue accepting payments. |
| `1.03.00.02` | `2021-08-27` | The initial firmware version available for this device. |

#### Configurations 

| Name | Release Date | Description |
| --- | --- | --- |
| `SZZZ_Generic_Y_v3` | `2023-07-24` | Updates production configuration for this device. |
| `SZZZ_Generic_Y_v2` | `2021-09-13` | Enables contactless during `collectSetupIntentPaymentMethod`. |
| `SZZZ_Generic_Y_v1` | `2021-08-27` | The initial configuration available for this device. |

#### Key identifiers 

| Identifier | Release Date | Description |
| --- | --- | --- |
| `30000` |  | The initial key identifier available for this device. |
| `300001` | `2020-06-30` | An alias for `30000` that might be visible in newer Terminal SDK versions. |

#### CHB20Z

| Latest Version |
| --- |
| `1.02.00.07-SZZZ_Generic_Z_v3-300001` |

#### Firmware versions 

| Version | Release Date | Description |
| --- | --- | --- |
| `1.02.00.07` | `2023-07-24` | Maintenance updates. |
| `1.02.00.02.5cc80c4b` | `2021-10-20` | Updates reader CAPK keys. You must install before December 31, 2021 to continue accepting payments. |
| `1.02.00.02` | `2021-08-27` | The initial firmware version available for this device. |

#### Configurations 

| Name | Release Date | Description |
| --- | --- | --- |
| `SZZZ_Generic_Z_v3` | `2023-07-24` | Updates production configuration for this device. |
| `SZZZ_Generic_Z_v2` | `2021-09-13` | Enables contactless during `collectSetupIntentPaymentMethod`. |
| `SZZZ_Generic_Z_v1` | `2021-08-27` | The initial configuration available for this device. |

#### Key identifiers 

| Identifier | Release Date | Description |
| --- | --- | --- |
| `30000` |  | The initial key identifier available for this device. |
| `300001` | `2021-08-27` | An alias for `30000` that might be visible in newer Terminal SDK versions. |

## See also

- [Set up BBPOS Chipper 2X BT](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-chipper2xbt.md)
- [Set up your integration](https://docs.stripe.com/terminal/payments/setup-integration.md)
- [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md)
- [Collect payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks doesn’t imply any endorsement by BBPOS or Verifone.
