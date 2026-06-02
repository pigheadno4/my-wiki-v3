<!-- Source: Stripe Terminal — Connect to a reader (all platforms + reader types) -->
<!-- Fetched: 2026-04-24 -->

# Connect to a reader

Connect your application to a Stripe Terminal reader.

> If you haven’t chosen a reader yet, compare the available [Terminal readers](https://docs.stripe.com/terminal/payments/setup-reader.md) and choose one that best suits your needs.

# Simulated Reader

> This is a Simulated Reader for when terminal-sdk-platform is server-driven and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=server-driven&reader-type=simulated.

Stripe provides a simulated server-driven reader so you can develop and test your app and simulate Terminal payments, without connecting to physical hardware.

## Create a simulated reader

To create a simulated reader, use one of the designated registration codes (`simulated-wpe`, `simulated-s700`, or `simulated-s710`) when registering the reader. This registration code creates a simulated WisePOS E, Stripe S700 reader, or Stripe S710 reader object in a sandbox only. You can register the simulated reader using the Stripe API:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  location: "{{TERMINALLOCATION_ID}}",
  registration_code: "simulated-wpe",
});
```

This returns a [reader](https://docs.stripe.com/api/terminal/readers.md) object representing your simulated reader:

```json
{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "simulated-wpe-xxx-xxx-xx-xxx",
  "livemode": false,
  "location": "tml_xxx",
  "serial_number": "simulated-wpe-xxx-xxx-xx-xxx",
  "status": "online"
}
```

## Query your simulated reader

The simulated reader behaves like a real reader. You can retrieve its information from the [reader endpoint](https://docs.stripe.com/api/terminal/readers/retrieve.md):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.retrieve("tmr_xxx");
```

```json
{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  "action": null,
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "simulated-wpe-xxx-xxx-xx-xxx",
  "livemode": false,
  "location": "tml_xxx",
  "metadata": {},
  "serial_number": "simulated-wpe-xxx-xxx-xx-xxx",
  "status": "offline"
}
```

# Simulated Reader

> This is a Simulated Reader for when terminal-sdk-platform is js and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=js&reader-type=simulated.

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

The simulated reader doesn’t provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to [simulate card presentment](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment).

To use the simulated reader, call [discoverReaders](https://docs.stripe.com/terminal/references/api/js-sdk.md#discover-readers) to search for readers, with the `simulated` option set to `true`. When `discoverReaders` returns a result, call [connectReader](https://docs.stripe.com/terminal/references/api/js-sdk.md#connect-reader) to connect to the simulated reader.

```javascript
// Handler for a "Connect Reader" button
async function connectReaderHandler() {
  const config = { simulated: true };
  const discoverResult = await terminal.discoverReaders(config);
  if (discoverResult.error) {
    console.log("Failed to discover: ", discoverResult.error);
  } else if (discoverResult.discoveredReaders.length === 0) {
    console.log("No available readers.");
  } else {
    // Just select the first reader here.
    const selectedReader = discoverResult.discoveredReaders[0];

    const connectResult = await terminal.connectReader(selectedReader);
    if (connectResult.error) {
      console.log("Failed to connect: ", connectResult.error);
    } else {
      console.log("Connected to reader: ", connectResult.reader.label);
    }
  }
}
```

### Simulated Reader configuration

- [setSimulatorConfiguration (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-setsimulatorconfig)

The simulated reader supports a small amount of configuration, enabling you to test different flows within your point of sale application such as different card brands or error scenarios like a declined charge. To enable this behavior, use the following code before you collect your payment method:

```javascript
terminal.setSimulatorConfiguration({ testCardNumber: "4242424242424242" });
```

# Simulated Reader

> This is a Simulated Reader for when terminal-sdk-platform is ios and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=simulated.

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

The simulated reader doesn’t provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to [simulate card presentment](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment).

To use the simulated reader, call [discoverReaders](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>) to search for readers, with the `simulated` option set to `true`. When `discoverReaders` returns a result, call [connectReader](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:delegate:completion:>) to connect to the simulated reader.

When connecting to a mobile reader or to a Tap to Pay reader, your integration must include the `locationId` in the connection configuration, even for the simulated reader. Because the simulated reader can’t be associated with a real location, provide the simulated reader’s mock `locationId` instead.

```swift
import UIKit
import StripeTerminal

class DiscoverReadersViewController: UIViewController, DiscoveryDelegate {

    var discoverCancelable: Cancelable?

    // ...

    // Action for a "Discover Readers" button
    func discoverReadersAction() throws {let config = try BluetoothScanDiscoveryConfigurationBuilder().setSimulated(true).build()
        self.discoverCancelable = Terminal.shared.discoverReaders(config, delegate: self) { error in
            if let error = error {
                print("discoverReaders failed: \(error)")
            } else {
                print("discoverReaders succeeded")
            }
        }
    }

    // ...

    // MARK: DiscoveryDelegate

    // This delegate method can get called multiple times throughout the discovery process.
    // You might want to update a UITableView and display all available readers.
    // Here, we're automatically connecting to the first reader we discover.
    func terminal(_ terminal: Terminal, didUpdateDiscoveredReaders readers: [Reader]) {

        // Select the first reader we discover
        guard let selectedReader = readers.first else { return }

        // Since the simulated reader is not associated with a real location, we recommend
        // specifying its existing mock location.
        guard let locationId = selectedReader.locationId else { return }

        // Only connect if we aren't currently connected.
        guard terminal.connectionStatus == .notConnected || terminal.connectionStatus == .discovering else { return }
// Replace 'yourMobileReaderDelegate' with your actual MobileReaderDelegate implementation
        let mobileReaderDelegate = yourMobileReaderDelegate
        do {
            connectionConfig = try BluetoothConnectionConfigurationBuilder(
                // When connecting to a physical reader, your integration should specify either the
                // same location as the last connection (selectedReader.locationId) or a new location
                // of your user's choosing.
                delegate: mobileReaderDelegate,
                locationId: locationId
            )
            .setAutoReconnectOnUnexpectedDisconnect(true) // This is optional as it's the default value
            .build()
        } catch {
            // Handle error building the connection configuration
            return
        }

        // Note `readerDelegate` should be provided by your application.
        // See our Quickstart guide at https://stripe.com/docs/terminal/quickstart
        // for more example code.
        Terminal.shared.connectReader(selectedReader, connectionConfig: connectionConfig) { reader, error in
            if let reader = reader {
                print("Successfully connected to reader: \(reader)")
            } else if let error = error {
                print("connectReader failed: \(error)")
            }
        }
    }
}
```

### Simulated Reader configuration

- [SimulatorConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPSimulatorConfiguration.html)

The simulated reader supports a small amount of configuration, enabling you to test different flows within your point of sale application such as different card brands or error scenarios like a declined charge. To enable this behavior, use the following code before you collect your payment method:

#### Swift

```swift
let simulatorConfiguration = Terminal.shared.simulatorConfiguration
simulatorConfiguration.simulatedCard = SimulatedCard(type: .amex)
simulatorConfiguration.simulatedTipAmount = 1000
```

# Simulated Reader

> This is a Simulated Reader for when terminal-sdk-platform is android and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=simulated.

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

The simulated reader doesn’t provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to [simulate card presentment](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment).

To use the simulated reader, call [discoverReaders](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html) to search for readers, with the `isSimulated` option in the chosen `DiscoveryConfiguration` set to `true`. When `discoverReaders` returns a result, call [connectReader](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html) to connect to the simulated reader.

When connecting to a mobile reader, your integration must include the `locationId` in the connection configuration, even for the simulated reader. Because the simulated reader can’t be associated with a real location, provide the simulated reader’s mock `locationId` instead.

```kotlin
// Handler for a "Connect Reader" button
fun onConnect() {
    val config = BluetoothDiscoveryConfiguration(timeout = 0, isSimulated = true)

    Terminal.getInstance().discoverReaders(
        config,
        object : DiscoveryListener {
            override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
                // Select the first reader here.
                val firstReader = readers.first()
                // Replace 'yourMobileReaderListener' with your actual MobileReaderListener implementation
                val mobileReaderListener = yourMobileReaderListener
                val autoReconnectOnUnexpectedDisconnect = true

                // When connecting to a physical reader, specify either the
                // same location as the last connection (selectedReader.location?.id) or a new location
                // of your user's choosing.
                //
                // Since the simulated reader isn't associated with a real location, we recommend
                // specifying its existing mock location.
                val connectionConfig = BluetoothConnectionConfiguration(
                    locationId = firstReader.location?.id.orEmpty(),
                    autoReconnectOnUnexpectedDisconnect = autoReconnectOnUnexpectedDisconnect,
                    bluetoothReaderListener = mobileReaderListener
                )

                Terminal.getInstance().connectReader(
                    firstReader,
                    connectionConfig,
                    object : ReaderCallback {
                        override fun onSuccess(reader: Reader) {
                            // Placeholder for handling successful operation
                        }

                        override fun onFailure(e: TerminalException) {
                            // Placeholder for handling exception
                        }
                    }
                )
            }
        },
        object : Callback {
            override fun onSuccess() {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
}
```

### Simulated Reader configuration

- [SimulatorConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-simulator-configuration/index.html)

The simulated reader supports a small amount of configuration, enabling you to test different flows within your point of sale application such as different card brands or error scenarios like a declined charge. To enable this behavior, use the following code before you collect your payment method:

#### Kotlin

```kotlin
val simulatedFixedTipAmount = 1000L;

val simulatorConfig = SimulatorConfiguration(
    simulatedCard = SimulatedCard(SimulatedCardType.AMEX),
    simulatedTipAmount = simulatedFixedTipAmount
);

Terminal.getInstance().setSimulatorConfiguration(simulatorConfig);
```

# Simulated Reader

> This is a Simulated Reader for when terminal-sdk-platform is react-native and reader-type is simulated. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=react-native&reader-type=simulated.

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

The simulated reader doesn’t provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to [simulate card presentment](https://docs.stripe.com/terminal/references/testing.md#simulated-card-presentment).

To use the simulated reader, call [discoverReaders](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders) to search for readers, with the `simulated` option set to `true`. When the `onUpdateDiscoveredReaders` callback is called with an array of the readers as an argument, call [connectReader](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1) to connect to the simulated reader.

When connecting to a mobile reader or to a TapToPay reader, your integration must include the `locationId` in the connection configuration, even for the simulated reader. Because the simulated reader can’t be associated with a real location, provide the simulated reader’s mock `locationId` instead.

```js
function DiscoverReadersScreen() {
  const { discoverReaders, connectReader, discoveredReaders } =
    useStripeTerminal({
      onUpdateDiscoveredReaders: (readers) => {
        // After the SDK discovers a reader, your app can connect to it.
        // Here, we're automatically connecting to the first discovered reader.
        handleConnectBluetoothReader(readers[0]);
      },
    });

  useEffect(() => {
    handleDiscoverReaders();
  }, []);

  const handleDiscoverReaders = async () => {
    // The list of discovered readers is reported in the `onUpdateDiscoveredReaders` method
    // within the `useStripeTerminal` hook.
    const { error } = await discoverReaders({
      discoveryMethod: 'bluetoothScan',
      simulated: true,
    });

    if (error) {
      Alert.alert(
        'Discover readers error: ',
        `${error.code}, ${error.message}`
      );
    }
  };

  const handleConnectBluetoothReader = async (discoveredReader: Reader.Type) => {
    const { reader, error } = await connectReader({
        discoveryMethod: 'bluetoothScan',
        reader: discoveredReader,
        // Since the simulated reader is not associated with a real location, we recommend
        // specifying its existing mock location.
        locationId: discoveredReader.locationId,
      });

    if (error) {
      console.log('connectReader error', error);
      return;
    }

    console.log('Reader connected successfully', reader);
  };

  return <View />;
}
```

### Simulated Reader configuration

- [setSimulatedCard (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#setSimulatedCard)

The simulated reader supports a small amount of configuration, enabling you to test different flows within your point of sale application such as different card brands or error scenarios like a declined charge. To enable this behavior, use the following code before you collect your payment method:

```js
const { error } = await setSimulatedCard("4242424242424242");

if (error) {
  // Placeholder for handling exception
}

// Placeholder for handling successful operation
```

# Bluetooth Readers

> This is a Bluetooth Readers for when terminal-sdk-platform is ios and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth.

Bluetooth-connected readers are Bluetooth LE devices. They collect payment details, but rely on a paired mobile device for communication with Stripe.

Follow these steps to connect your app to a Terminal reader using Bluetooth:

1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers).
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader).

> Don’t use mobile device settings to pair with your reader. Pairing the reader through device settings makes the reader unavailable to connect to your app.

## Discover readers [Client-side]

- [discoverReaders (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>)
- [BluetoothScanDiscoveryConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothScanDiscoveryConfiguration.html)

To start, make sure your reader is powered on and within close proximity.

Then from your app, search for nearby Bluetooth-connected readers with the `discoverReaders` method, using `BluetoothScanDiscoveryConfiguration`.

#### Swift

```swift
import StripeTerminal

class DiscoverReadersViewController: UIViewController, DiscoveryDelegate {

    var discoverCancelable: Cancelable?

    // ...

    // Action for a "Discover Readers" button
    func discoverReadersAction() throws {
        let config = try BluetoothScanDiscoveryConfigurationBuilder().build()
        // In addition to Terminal's completion block methods, Swift async alternatives are available.
        // See our Example app for usage examples: https://github.com/stripe/stripe-terminal-ios/tree/master/Example
        self.discoverCancelable = Terminal.shared.discoverReaders(config, delegate: self) { error in
            if let error = error {
                print("discoverReaders failed: \(error)")
            } else {
                print("discoverReaders succeeded")
            }
        }
    }

    // ...

    // MARK: DiscoveryDelegate

    func terminal(_ terminal: Terminal, didUpdateDiscoveredReaders readers: [Reader]) {
        // In your app, display the discovered readers to the user.
        // Call `connectReader` after the user selects a reader to connect to.
    }
}

```

#### Bluetooth proximity \* (BBPOS Chipper 2X BT only)

Bluetooth proximity filters search results to return the closest reader. When discovered, the reader flashes multicolored lights, allowing your user to identify the discovered reader among many other readers. After the SDK discovers a reader, it won’t switch to a closer reader unless you turn off the discovered reader.

Note that when using Bluetooth proximity, the SDK returns the reader to your app’s callback twice. The first time, your app receives a `Reader` object populated with only the reader’s serial number. After a short delay, your app receives the same `Reader` object populated with new information, such as the reader’s battery level.

We recommend displaying the discovered reader in your app’s UI, letting the user either confirm connection to the reader or cancel if they don’t want to connect to this reader.

#### Bluetooth scan

Bluetooth scan searches for all nearby readers and returns a list of discovered readers to your app. As the discovery process continues, the SDK continues to invoke the `DiscoveryDelegate.didUpdateDiscoveredReaders` method with the latest list of nearby readers.

During the discovery process, the Terminal’s `SCPConnectionStatus` transitions to `SCPConnectionStatus.SCPConnectionStatusDiscovering` while the discovery is in progress.

With the Bluetooth scan discovery method, you can set a timeout to scan for a set period of time, which you can use for managing battery life or triggering an error message if no devices are found.

In your mobile application, we recommend displaying an auto-updating list of discovered readers with serial numbers to help users identify their mobile reader. The `label` property isn’t populated for mobile readers during reader discovery. If you need to display friendly names for readers, maintain your own mapping of serial numbers to labels in your application.

#### Bluetooth pairing

To improve security and comply with EU regulations, as of November 2025 Stripe uses the numeric comparison Bluetooth pairing process for WisePad 3 card readers. The numeric comparison process requires you to verify a passkey on both your card reader and the POS device when pairing. After you update your device to the [latest software version](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md#reader-software-releases), follow these steps when connecting your WisePad 3 to a new mobile application. After your POS device discovers and displays the WisePad 3 reader:

1. Verify that the 6-digit code matches on both the WisePad 3 and on the POS device.
1. Select **Confirm** on the WisePad 3.
1. Select **Pair** on your POS device.

> #### Note
>
> You only need to do numeric comparison pairing when you pair a WisePad 3 with a new POS device, or when re-pairing with an existing “forgotten” POS device.

## Connect to a reader [Client-side]

- [connectReader (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:connectionConfig:completion:>)
- [BluetoothConnectionConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothConnectionConfiguration.html)

To connect to a discovered reader, call the `connectReader` method from your app. Always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session, because stale reader objects can cause connection failures.

Mobile readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your mobile reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, create and use a `BluetoothConnectionConfiguration` with the `locationId` set to the relevant location ID when connecting.

#### Swift

```swift
// Call `connectReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig: BluetoothConnectionConfiguration
do {
    connectionConfig = try BluetoothConnectionConfigurationBuilder(delegate: yourMobileReaderDelegate, locationId: ""{{LOCATION_ID}}"")
    .build()
} catch {
    // Handle the error building the connection configuration
    return
}
Terminal.shared.connectReader(selectedReader, connectionConfig: connectionConfig) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectReader failed: \(error)")
    }
}
```

For your app to run in the background and remain connected to the reader, [configure your app](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios#configure) to include the required background mode.

> #### Use standby mode
>
> Don’t program your app to call `disconnectReader` to conserve power. The reader efficiently handles power management using its standby mode.

## Handle reader disconnects

- [MobileReaderDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPMobileReaderDelegate.html)
- [DisconnectReason (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPDisconnectReason.html)

Reader disconnects can sometimes occur between your app and the reader. For example, the reader can disconnect from your app if it’s out of range, or runs out of battery. You can simulate an unexpected disconnect while testing by powering off the reader.

The `MobileReaderDelegate` includes a `reader:didDisconnect:` method that provides your application with the `DisconnectReason` to help identify why the reader disconnected.

To handle reader disconnects yourself, you can do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` during connection.
1. Handle the disconnect callback to display a message in the app alerting the user that the reader unexpectedly disconnected and initiate reader discovery and connection.

#### Swift

```swift
import StripeTerminal

class ReaderViewController: UIViewController, MobileReaderDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Set the reader delegate when connecting to a reader
    }

    // ...



    func reader(_ reader: Reader, didDisconnect reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
}
```

### Reboot the connected reader

- [rebootReader (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)rebootReader:.html>)

Stripe Reader M2 and BBPOS WisePad 3 automatically reboot after operating for 24 hours. However, you can force the reader to reboot and reset its 24-hour timer by using the `rebootReader` API. After this action, the reader disconnects from the SDK and then reboots. If you’re using automatic reconnect, the SDK attempts to restore the connection with the reader.

#### Swift

```swift
Terminal.shared.rebootReader { error in
    if let error = error {
        // Placeholder for handling the error
    } else {
        // Reboot succeeded and the reader will disconnect.
        // If your app is using automatic reconnect the reconnect will begin.
    }
}

```

#### Automatically attempt reconnection

When a reader disconnects, we automatically attempt reconnection by default and recommend that you display notifications in your app relaying the reader status throughout the process.

To display notifications in your app during automatic reconnection, do the following:

1. Implement the reader reconnect callbacks in the `MobileReaderDelegate`.
1. Pass the `MobileReaderDelegate` to your `BluetoothConnectionConfiguration`.

   #### Swift

   ```swift
   let connectionConfig: BluetoothConnectionConfiguration
   do {
       connectionConfig = BluetoothConnectionConfigurationBuilder(delegate: yourMobileReaderDelegate, locationId: presentLocationId)
           .build()
   } catch {
       // Handle error building the connection configuration
       return
   }

   Terminal.shared.connectReader(reader, connectionConfig: connectionConfig, completion: connectCompletion)
   ```

1. When the SDK sends [`reader:didStartReconnect:disconnectReason:`](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didStartReconnect:disconnectReason:>) to your app, display a message announcing that the reader lost connection and reconnection is in progress.
   - You can use the `Cancelable` object to stop the reconnection attempt at any time.
1. When the SDK indicates successful reconnection by sending [`readerDidSucceedReconnect:`](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)readerDidSucceedReconnect:>), display a message announcing the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader and sends both [`readerDidFailReconnect:`](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)readerDidFailReconnect:>) and `reader:didDisconnect:`, display a message stating that an unexpected disconnect occurred.

#### Swift

```swift
import StripeTerminal

extension ReaderViewController: MobileReaderDelegate {
    // MARK: MobileReaderDelegate

    func reader(_ reader: Reader, didStartReconnect cancelable: Cancelable, disconnectReason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    func readerDidSucceedReconnect(_ reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }
    func readerDidFailReconnect(_ reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

#### Automatic reconnection on application start

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [UserDefaults API](https://developer.apple.com/documentation/foundation/userdefaults) (iOS).

1. When your app launches, check the persistent data storage location for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is happening.

## Update reader software [Client-side]

- [MobileReaderDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPMobileReaderDelegate.html)

Your application must update mobile readers to apply the following:

- Regional configurations that keep you up to date with card network and issuer requirements
- Security updates

Required updates start installing on connection to the reader. You can’t use the reader until updating completes.

> To install updates, the reader’s battery level must be higher than 50%.

### Required updates

When immediately required updates are available for the reader, the integration’s `MobileReaderDelegate` receives the `didStartInstallingUpdate` callback with a `ReaderSoftwareUpdate`.

The `ReaderSoftwareUpdate` provides the necessary details of the update, including an estimate of the total update duration, indicated by `durationEstimate`.

During the installation process, the Terminal’s `connectionStatus` transitions to `connecting` while the update installs on the reader.

Your application must notify users that an update is installing and display the progress in your UI. Make it clear why connecting might take longer than usual.

If the required update process fails, Stripe communicates the error to the `MobileReaderDelegate` with `didFinishInstallingUpdate`. You can’t reconnect to the reader after a required update fails, unless the following conditions are met:

- The reader runs the latest software version for the location within the last 30 days.
- The iOS SDK version is greater than or equal to `3.5.0`.

If the conditions are met, the connection process succeeds despite an incomplete update. Stripe retries the required update the next time you connect to that reader until it’s successfully installed.

#### Swift

```swift
import UIKit
import StripeTerminal

class ReaderViewController: UIViewController, MobileReaderDelegate {

    // ...

    // MARK: MobileReaderDelegate

    func reader(_ reader: Reader, didStartInstallingUpdate update: ReaderSoftwareUpdate, cancelable: Cancelable?) {
        // Show UI communicating that a required update has started installing
    }

    func reader(_ reader: Reader, didReportReaderSoftwareUpdateProgress progress: Float) {
        // Update the progress of the installation
    }

    func reader(_ reader: Reader, didFinishInstallingUpdate update: ReaderSoftwareUpdate?, error: Error?) {
        // Report success or failure of the update
    }

    // ...
}
```

You can cancel required updates using the `Cancelable` object, which also results in a failed connection to the reader. You can’t cancel in-progress incremental-only updates.

### Optional updates

You can defer optional updates until the specified date, after which they become required. The SDK notifies you of optional updates through the `MobileReaderDelegate` any time the reader is connected but not performing a transaction. If an optional update is available, your application’s `MobileReaderDelegate` receives the `didReportAvailableUpdate` callback with the `ReaderSoftwareUpdate` object containing the update details, including:

- Estimated time for update to complete (`durationEstimate`)
- Timestamp after which the update becomes required (`requiredAt`)

In your application, notify users that an update is available, and display a prompt to optionally continue with the update.

To proceed with the update previously reported with `didReportAvailableUpdate`, call `Terminal.shared.installAvailableUpdate`.

The available update is also stored on the reader object as `reader.availableUpdate`.

As the update proceeds, block the user from leaving the page in your app, and instruct the user to keep the reader in range and powered on until the update completes. We recommend also providing your user with a visual indicator of the update’s progress. The `MobileReaderDelegate` reports the update’s progress in the `didReportReaderSoftwareUpdateProgress` method.

When an optional update’s `requiredAt` date has passed, the update installs the next time the reader is connected.

#### Swift

```swift
import UIKit
import StripeTerminal

class ReaderViewController: UIViewController, MobileReaderDelegate {

    // ...

    // MARK: MobileReaderDelegate

    func reader(_ reader: Reader, didReportAvailableUpdate update: ReaderSoftwareUpdate) {
        // An update is available for the connected reader. Show this update in your application.
        // Install this update using `Terminal.shared.installAvailableUpdate`.
    }

}
```

See [Testing reader updates](https://docs.stripe.com/terminal/references/testing.md#simulated-reader-updates) to learn more about making sure your application handles the different update types that a reader can have.

# Bluetooth Readers

> This is a Bluetooth Readers for when terminal-sdk-platform is android and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=bluetooth.

Bluetooth-connected readers are Bluetooth LE devices. They collect payment details, but rely on a paired mobile device for communication with Stripe.

Follow these steps to connect your app to a Terminal reader using Bluetooth:

1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers).
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader).

> Don’t use mobile device settings to pair with your reader. Pairing the reader through device settings makes the reader unavailable to connect to your app.

## Discover readers [Client-side]

- [discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [BluetoothDiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-bluetooth-discovery-configuration/index.html)

To start, make sure your reader is powered on and within close proximity.

Then from your app, search for nearby Bluetooth-connected readers with the `discoverReaders` method, using `BluetoothDiscoveryConfiguration`.

#### Kotlin

```kotlin
class DiscoverReadersActivity : AppCompatActivity(), DiscoveryListener {

    var discoverCancelable: Cancelable? = null

    // ...

    // Action for a "Discover Readers" button
    fun discoverReadersAction() {
        val timeout = 0
        val isSimulated = false

        val config = BluetoothDiscoveryConfiguration(
            timeout = timeout,
            isSimulated = isSimulated
        )

        discoverCancelable = Terminal.getInstance().discoverReaders(
            config,
            this,
            object : Callback {
                override fun onSuccess() {
                    // Placeholder for handling successful operation
                }

                override fun onFailure(e: TerminalException) {
                    // Placeholder for handling exception
                }
            }
        )
    }

    // DiscoveryListener
    override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
        // In your app, display the discovered readers to the user.
        // Call `connectReader` after the user selects a reader to connect to.
    }
}
```

#### Bluetooth scan

Bluetooth scan searches for all nearby readers and returns a list of discovered readers to your app. As the discovery process continues, the SDK continues to invoke the `onUpdateDiscoveredReaders` method with the latest list of nearby readers.

During the discovery process, the Terminal’s `connectionStatus` transitions to `ConnectionStatus.DISCOVERING` while the discovery is in progress.

With the Bluetooth scan discovery method, you can set a timeout to scan for a set period of time, which you can use for managing battery life or triggering an error message if no devices are found.

In your mobile application, we recommend displaying an auto-updating list of discovered readers with serial numbers to help users identify their mobile reader. The `label` property isn’t populated for mobile readers during reader discovery. If you need to display friendly names for readers, maintain your own mapping of serial numbers to labels in your application.

#### Bluetooth pairing

To improve security and comply with EU regulations, as of November 2025 Stripe uses the numeric comparison Bluetooth pairing process for WisePad 3 card readers. The numeric comparison process requires you to verify a passkey on both your card reader and the POS device when pairing. After you update your device to the [latest software version](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md#reader-software-releases), follow these steps when connecting your WisePad 3 to a new mobile application. After your POS device discovers and displays the WisePad 3 reader:

1. Verify that the 6-digit code matches on both the WisePad 3 and on the POS device.
1. Select **Confirm** on the WisePad 3.
1. Select **Pair** on your POS device.

> #### Note
>
> You only need to do numeric comparison pairing when you pair a WisePad 3 with a new POS device, or when re-pairing with an existing “forgotten” POS device.

## Connect to a reader [Client-side]

- [connectReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [BluetoothConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/index.html)

To connect to a discovered reader, call the `connectReader` method from your app. Always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session, because stale reader objects can cause connection failures.

Mobile readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your mobile reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, create and use a `BluetoothConnectionConfiguration` with the `locationId` set to the relevant location ID when connecting.

#### Kotlin

```kotlin
// Implement your MobileReaderListener
val mobileReaderListener = yourMobileReaderListener
val autoReconnectOnUnexpectedDisconnect = true

val connectionConfig = BluetoothConnectionConfiguration(
    ""{{LOCATION_ID}}"",
    autoReconnectOnUnexpectedDisconnect,
    mobileReaderListener
)

Terminal.getInstance().connectReader(
    selectedReader,
    connectionConfig,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

> #### Use standby mode
>
> Don’t program your app to call `disconnectReader` to conserve power. The reader efficiently handles power management using its standby mode.

## Handle reader disconnects

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)
- [DisconnectReason (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-disconnect-reason/index.html)

Reader disconnects can sometimes occur between your app and the reader. For example, the reader can disconnect from your app if it’s out of range, or runs out of battery. You can simulate an unexpected disconnect while testing by powering off the reader.

The `MobileReaderListener` includes an `onDisconnect` callback that provides your application with the `DisconnectReason` to help identify why the reader disconnected.

To handle reader disconnects yourself, you can do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` during connection.
1. Handle the disconnect callback to display a message in the app alerting the user that the reader unexpectedly disconnected and initiate reader discovery and connection.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onDisconnect(reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

### Reboot the connected reader

- [rebootReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/reboot-reader.html)

Stripe Reader M2 and BBPOS WisePad 3 automatically reboot after operating for 24 hours. However, you can force the reader to reboot and reset its 24-hour timer by using the `rebootReader` API. After this action, the reader disconnects from the SDK and then reboots. If you’re using automatic reconnect, the SDK attempts to restore the connection with the reader.

#### Kotlin

```kotlin
Terminal.getInstance().rebootReader(
    object : Callback {
        override fun onSuccess() {
            // Reboot succeeded and the reader will disconnect.
            // If your app is using automatic reconnect the reconnect will begin.
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

#### Automatically attempt reconnection

When a reader disconnects, we automatically attempt reconnection by default and recommend that you display notifications in your app relaying the reader status throughout the process.

To display notifications in your app during automatic reconnection, do the following:

1. Implement the reader reconnect callbacks in the `MobileReaderListener`.
1. Pass the `MobileReaderListener` to your `BluetoothConnectionConfiguration`.

   #### Kotlin

   ```kotlin
   val mobileReaderListener = yourMobileReaderListener

   Terminal.getInstance().connectReader(
       reader,
       BluetoothConnectionConfiguration(
           ""{{LOCATION_ID}}"",
           true,
           mobileReaderListener
       ),
       readerCallback
   )
   ```

1. When the SDK sends [onReaderReconnectStarted](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-started.html) to your app, display a message announcing that the reader lost connection and reconnection is in progress.
   - You can use the `Cancelable` object to stop the reconnection attempt at any time.
1. When the SDK indicates successful reconnection by sending [`onReaderReconnectSucceeded`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-succeeded.html), display a message announcing the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader and sends both [`onReaderReconnectFailed`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-failed.html) and `onDisconnect`, display a message stating that an unexpected disconnect occurred.

#### Kotlin

```kotlin
class CustomMobileReaderListener : MobileReaderListener {
    // ...

    override fun onReaderReconnectStarted(reader: Reader, cancelReconnect: Cancelable, reason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    override fun onReaderReconnectSucceeded(reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }

    override fun onReaderReconnectFailed(reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }

    // ...
}
```

#### Automatic reconnection on application start

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [Shared Preferences API](https://developer.android.com/training/data-storage/shared-preferences) (Android).

1. When your app launches, check the persistent data storage location for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is happening.

## Update reader software [Client-side]

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)

Your application must update mobile readers to apply the following:

- Regional configurations that keep you up to date with card network and issuer requirements
- Security updates

Required updates start installing on connection to the reader. You can’t use the reader until updating completes.

> To install updates, the reader’s battery level must be higher than 50%.

### Required updates

When immediately required updates are available for the reader, the integration’s `MobileReaderListener` receives `onStartInstallingUpdate` with a `ReaderSoftwareUpdate`.

The `ReaderSoftwareUpdate` provides the necessary details of the update, including an estimate of the total update duration, indicated by `durationEstimate`.

During the installation process, the Terminal’s `connectionStatus` transitions to `ConnectionStatus.CONNECTING` while the update installs on the reader.

Your application must notify users that an update is installing and display the progress in your UI. Make it clear why connecting might take longer than usual.

If the required update process fails, Stripe communicates the error to the `MobileReaderListener` with `onFinishInstallingUpdate`. You can’t reconnect to the reader after a required update fails, unless the following conditions are met:

- The reader runs the latest software version for the location within the last 30 days.
- The Android SDK version is greater than or equal to `3.5.0`.

If the conditions are met, the connection process succeeds despite an incomplete update. Stripe retries the required update the next time you connect to that reader until it’s successfully installed.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onStartInstallingUpdate(update: ReaderSoftwareUpdate, cancelable: Cancelable) {
        // Show UI communicating that a required update has started installing
    }

    override fun onReportReaderSoftwareUpdateProgress(progress: Float) {
        // Update the progress of the installation
    }

    override fun onFinishInstallingUpdate(update: ReaderSoftwareUpdate?, e: TerminalException?) {
        // Report success or failure of the update
    }

    // ...
}
```

You can cancel required updates using the `Cancelable` object, which also results in a failed connection to the reader. You can’t cancel in-progress incremental-only updates.

### Optional updates

You can defer optional updates until the specified date, after which they become required. The SDK notifies you of optional updates through the `MobileReaderListener` any time the reader is connected but not performing a transaction. If an optional update is available, your application’s `MobileReaderListener` receives the `onReportAvailableUpdate` callback with the `ReaderSoftwareUpdate` object containing the update details, including:

- Estimated time for update to complete (`durationEstimate`)
- Date after which the update becomes required (`requiredAt`)

In your application, notify users that an update is available, and display a prompt to optionally continue with the update.

To proceed with the update previously reported with `onReportAvailableUpdate`, call `Terminal.getInstance().installAvailableUpdate`.

The available update is also stored on the reader object as `reader.availableUpdate`.

As the update proceeds, block the user from leaving the page in your app, and instruct the user to keep the reader in range and powered on until the update completes. We recommend also providing your user with a visual indicator of the update’s progress. The `MobileReaderListener` reports the update’s progress in the `onReportReaderSoftwareUpdateProgress` method.

When an optional update’s `requiredAt` date has passed, the update installs the next time the reader is connected.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onReportAvailableUpdate(update: ReaderSoftwareUpdate) {
        // An update is available for the connected reader. Show this update in your application.
        // Install this update using `Terminal.getInstance().installAvailableUpdate`.
    }

    // ...
}
```

See [Testing reader updates](https://docs.stripe.com/terminal/references/testing.md#simulated-reader-updates) to learn more about making sure your application handles the different update types that a reader can have.

# Bluetooth Readers

> This is a Bluetooth Readers for when terminal-sdk-platform is react-native and reader-type is bluetooth. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=react-native&reader-type=bluetooth.

Bluetooth-connected readers are Bluetooth LE devices. They collect payment details, but rely on a paired mobile device for communication with Stripe.

Follow these steps to connect your app to a Terminal reader using Bluetooth:

1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers).
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader).

> Don’t use mobile device settings to pair with your reader. Pairing the reader through device settings makes the reader unavailable to connect to your app.

## Discover readers [Client-side]

- [discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders)

To start, make sure your reader is powered on and within close proximity.

Then from your app, search for nearby Bluetooth-connected readers with the `discoverReaders` method, setting `discoveryMethod` to `bluetoothScan`.

```js
function DiscoverReadersScreen() {
  const { discoverReaders, discoveredReaders } = useStripeTerminal({
    onUpdateDiscoveredReaders: (readers) => {
      // After the SDK discovers a reader, your app can connect to it.
    },
  });

  useEffect(() => {
    handleDiscoverReaders();
  }, [discoverReaders]);

  const handleDiscoverReaders = async () => {
    // The list of discovered readers is reported in the `onUpdateDiscoveredReaders` method
    // within the `useStripeTerminal` hook.
    const { error } = await discoverReaders({
      discoveryMethod: "bluetoothScan",
    });

    if (error) {
      Alert.alert(
        "Discover readers error: ",
        `${error.code}, ${error.message}`,
      );
    }
  };

  return <View />;
}
```

#### Bluetooth scan

Bluetooth scan searches for all nearby readers and returns a list of discovered readers to your app. As the discovery process continues, the SDK continues to invoke `onUpdateDiscoveredReaders` within the `useStripeTerminal` hook with the latest list of nearby readers.

With the Bluetooth scan discovery method, you can set a timeout to scan for a set period of time, which you can use for managing battery life or triggering an error message if no devices are found.

In your mobile application, we recommend displaying an auto-updating list of discovered readers with serial numbers to help users identify their mobile reader. The `label` property isn’t populated for mobile readers during reader discovery. If you need to display friendly names for readers, maintain your own mapping of serial numbers to labels in your application.

#### Bluetooth pairing

To improve security and comply with EU regulations, as of November 2025 Stripe uses the numeric comparison Bluetooth pairing process for WisePad 3 card readers. The numeric comparison process requires you to verify a passkey on both your card reader and the POS device when pairing. After you update your device to the [latest software version](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md#reader-software-releases), follow these steps when connecting your WisePad 3 to a new mobile application. After your POS device discovers and displays the WisePad 3 reader:

1. Verify that the 6-digit code matches on both the WisePad 3 and on the POS device.
1. Select **Confirm** on the WisePad 3.
1. Select **Pair** on your POS device.

> #### Note
>
> You only need to do numeric comparison pairing when you pair a WisePad 3 with a new POS device, or when re-pairing with an existing “forgotten” POS device.

## Connect to a reader [Client-side]

- [connectReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1)

To connect to a discovered reader, call the `connectReader` method from your app. Always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session, because stale reader objects can cause connection failures.

Mobile readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your mobile reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, make sure `locationId` is set to the relevant location ID when connecting.

```js
const handleConnectBluetoothReader = async (id) => {
  const { reader, error } = await connectReader({
    discoveryMethod: 'bluetoothScan',
    reader: selectedReader,
    locationId: {{LOCATION_ID}},
  });

  if (error) {
    console.log('connectReader error', error);
    return;
  }

  console.log('Reader connected successfully', reader);
};
```

> #### Use standby mode
>
> Don’t program your app to call `disconnectReader` to conserve power. The reader efficiently handles power management using its standby mode.

## Handle reader disconnects

- [REPORT_UNEXPECTED_READER_DISCONNECT (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#REPORT_UNEXPECTED_READER_DISCONNECT)
- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)
- [DisconnectReason (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/modules/Reader.html#DisconnectReason)

Reader disconnects can sometimes occur between your app and the reader. For example, the reader can disconnect from your app if it’s out of range, or runs out of battery. You can simulate an unexpected disconnect while testing by powering off the reader.

`UserCallbacks` includes `onDidDisconnect` that provides your application with the `DisconnectReason` to help identify why the reader disconnected.

To handle reader disconnects yourself, you can do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` during connection.
1. Handle the disconnect callback to display a message in the app alerting the user that the reader unexpectedly disconnected and initiate reader discovery and connection.

```js
const terminal = useStripeTerminal({
  onDidDisconnect: (result) => {
    // Consider displaying a UI to notify the user and start rediscovering readers
  },
});
```

### Reboot the connected reader

- [rebootReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#rebootReader)

Stripe Reader M2 and BBPOS WisePad 3 automatically reboot after operating for 24 hours. However, you can force the reader to reboot and reset its 24-hour timer by using the `rebootReader` API. After this action, the reader disconnects from the SDK and then reboots. If you’re using automatic reconnect, the SDK attempts to restore the connection with the reader.

```js
const { error } = await rebootReader();

if (error) {
  console.log("rebootReader error:", error);
  return;
}

console.log("rebootReader succeeded");
```

#### Automatically attempt reconnection

When a reader disconnects, we automatically attempt reconnection by default and recommend that you display notifications in your app relaying the reader status throughout the process.

To display notifications in your app during automatic reconnection, do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to true on the `ConnectBluetoothReaderParams`.
1. Implement the auto reconnect callbacks found in the `UserCallbacks`.
1. When the SDK sends `onDidStartReaderReconnect` to your app, display a message announcing that the reader lost connection and reconnection is in progress.
   - You can use `cancelReaderReconnection` to stop the reconnection attempt at any time.
1. When the SDK indicates successful reconnection by sending `onDidSucceedReaderReconnect`, display a message announcing the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader and sends `onDidFailReaderReconnect`, display a message stating that an unexpected disconnect occurred.

#### Automatic reconnection on application start

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as [Async Storage](https://github.com/react-native-async-storage/async-storage) (React Native).

1. When your app launches, check the persistent data storage location for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is happening.

## Update reader software [Client-side]

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

Your application must update mobile readers to apply the following:

- Regional configurations that keep you up to date with card network and issuer requirements
- Security updates

Required updates start installing on connection to the reader. You can’t use the reader until updating completes.

> To install updates, the reader’s battery level must be higher than 50%.

### Required updates

When immediately required updates are available for the reader, the integration receives `onDidStartInstallingUpdate` from the `useStripeTerminal` hook with a `Reader.SoftwareUpdate`.

The `Reader.SoftwareUpdate` provides the necessary details of the update, including an estimate of the total update duration, indicated by `estimatedUpdateTime`.

During the installation process, the Terminal’s `connectionStatus` transitions to `"connecting"` while the update installs on the reader.

Your application must notify users that an update is installing and display the progress in your UI. Make it clear why connecting might take longer than usual.

If the required update process fails, Stripe communicates the error to the `useStripeTerminal` hook with `onDidFinishInstallingUpdate`. You can’t reconnect to the reader after a required update fails, unless the following conditions are met:

- The reader runs the latest software version for the location within the last 30 days.
- The React Native SDK version is greater than or equal to `0.0.1-beta.18`.

If the conditions are met, the connection process succeeds despite an incomplete update. Stripe retries the required update the next time you connect to that reader until it’s successfully installed.

```js
const terminal = useStripeTerminal({
  onDidReportReaderSoftwareUpdateProgress: (progress) => {
    setCurrentProgress((Number(progress) * 100).toFixed(0).toString());
  },
  onDidFinishInstallingUpdate: ({ error }) => {},
  onDidStartInstallingUpdate: (update) => {},
});
```

You can cancel required updates using the `cancelInstallingUpdate` API, which also results in a failed connection to the reader. You can’t cancel in-progress incremental-only updates.

### Optional updates

You can defer optional updates until the specified date, after which they become required. The SDK notifies you of optional updates through the `onDidReportAvailableUpdate` callback from the `useStripeTerminal` hook any time the reader is connected but not performing a transaction. If an optional update is available, your application’s `useStripeTerminal` hook receives the `onDidReportAvailableUpdate` callback with the `SoftwareUpdate` object containing the update details, including:

- Estimated time for update to complete (`estimatedUpdateTime`)
- Date after which the update becomes required (`requiredAt`)

In your application, notify users that an update is available, and display a prompt to optionally continue with the update.

To proceed with the update previously reported with `onDidReportAvailableUpdate`, call `installAvailableUpdate` from the `useStripeTerminal` hook.

The available update is also stored on the reader object as `reader.availableUpdate`.

As the update proceeds, block the user from leaving the page in your app, and instruct the user to keep the reader in range and powered on until the update completes. We recommend also providing your user with a visual indicator of the update’s progress. The `useStripeTerminal` hook reports the update’s progress in the `onDidReportReaderSoftwareUpdateProgress` method.

When an optional update’s `requiredAt` date has passed, the update installs the next time the reader is connected.

```js
const terminal = useStripeTerminal({
  onDidReportAvailableUpdate: (update) => {
    // An update is available for the connected reader. Show this update in your application.
    // Install this update using the `installAvailableUpdate` method from the `useStripeTerminal` hook.
  },
});
```

See [Testing reader updates](https://docs.stripe.com/terminal/references/testing.md#simulated-reader-updates) to learn more about making sure your application handles the different update types that a reader can have.

# USB Readers

> This is a USB Readers for when terminal-sdk-platform is android and reader-type is usb. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=usb.

Use the Stripe Terminal Android SDK 3.0.0 (or later) to support USB connections for the [Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md) and [BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md) readers.

You must use a USB cable that supports both data and charging, like the USB 2.0 cable that’s included with the Stripe Reader M2 and BBPOS WisePad 3. If the cable included with your Terminal reader is charge-only, use a third-party USB 2.0 cable that can also transfer data.

To connect your app to a Terminal reader with a USB cable:

1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers).
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader).

## Discover readers [Client-side]

- [discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [UsbDiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-usb-discovery-configuration/index.html)

Make sure the reader is powered on and connected with a USB 2.0 cable to the device running your app, and permission has been granted to access the USB-connected reader.

If you’re plugging in the reader for the first time, an Android system prompt displays to connect to the reader. You can select the “Always open” checkbox to open your app without prompting when it’s connected to a reader.

Then from your app, search for the connected reader with the `discoverReaders` method, using `UsbDiscoveryConfiguration`.

#### Kotlin

```kotlin
class DiscoverReadersActivity : AppCompatActivity(), DiscoveryListener {
    // ...

    var discoverCancelable: Cancelable? = null

    // Action for a "Discover Readers" button
    fun discoverReadersAction() {
        val timeout = 0
        val isSimulated = false

        val config = UsbDiscoveryConfiguration(
            timeout = timeout,
            isSimulated = isSimulated
        )

        Terminal.getInstance().discoverReaders(
            config,
            this,
            object : Callback {
                override fun onSuccess() {
                    // Placeholder for handling successful operation
                }

                override fun onFailure(e: TerminalException) {
                    // Placeholder for handling exception
                }
            }
        )
    }

    override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
        // In your app, display the discovered readers to the user.
        // Call `connectReader` after the user selects a reader to connect to.
    }

    // ...
}
```

## Connect to a reader [Client-side]

- [connectReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [UsbConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-usb-connection-configuration/index.html)

To connect to a discovered reader, call the `connectReader` method from your app.

Mobile readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your mobile reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, create and use a `UsbConnectionConfiguration` with the `locationId` set to the relevant location ID when connecting.

#### Kotlin

```kotlin
// Implement your MobileReaderListener
val mobileReaderListener = yourMobileReaderListener
val autoReconnectOnUnexpectedDisconnect = true

val connectionConfig = UsbConnectionConfiguration(
    ""{{LOCATION_ID}}"",
    autoReconnectOnUnexpectedDisconnect,
    mobileReaderListener
)

Terminal.getInstance().connectReader(
    selectedReader,
    connectionConfig,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

> #### Use standby mode
>
> Don’t program your app to call `disconnectReader` to conserve power. The reader efficiently handles power management using its standby mode.

## Handle reader disconnects

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)
- [DisconnectReason (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-disconnect-reason/index.html)

Reader disconnects can sometimes occur between your app and the reader. For example, the reader can disconnect from your app if the USB cable connecting it to your device is disconnected. You can simulate an unexpected disconnect while testing by powering off the reader.

The `MobileReaderListener` includes an `onDisconnect` callback that provides your application with the `DisconnectReason` to help identify why the reader disconnected.

To handle reader disconnects yourself, you can do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` during connection.
1. Handle the disconnect callback to display a message in the app alerting the user that the reader unexpectedly disconnected and initiate reader discovery and connection.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onDisconnect(reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

### Reboot the connected reader

- [rebootReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/reboot-reader.html)

Stripe Reader M2 and BBPOS WisePad 3 automatically reboot after operating for 24 hours. However, you can force the reader to reboot and reset its 24-hour timer by using the `rebootReader` API. After this action, the reader disconnects from the SDK and then reboots. If you’re using automatic reconnect, the SDK attempts to restore the connection with the reader.

#### Kotlin

```kotlin
Terminal.getInstance().rebootReader(
    object : Callback {
        override fun onSuccess() {
            // Reboot succeeded and the reader will disconnect.
            // If your app is using automatic reconnect the reconnect will begin.
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

#### Automatically attempt reconnection

When a reader disconnects, we automatically attempt reconnection by default and recommend that you display notifications in your app relaying the reader status throughout the process.

To display notifications in your app during automatic reconnection, do the following:

1. Implement the reader reconnect callbacks in the `MobileReaderListener`.
1. Pass the `MobileReaderListener` to your `UsbConnectionConfiguration`.

   #### Kotlin

   ```kotlin
   val mobileReaderListener = yourMobileReaderListener
   val autoReconnectOnUnexpectedDisconnect = true

   Terminal.getInstance().connectReader(
       reader,
       UsbConnectionConfiguration(
           ""{{LOCATION_ID}}"",
           autoReconnectOnUnexpectedDisconnect,
           mobileReaderListener
       ),
       object : ReaderCallback {
           override fun onSuccess(reader: Reader) {
               // Placeholder for handling successful operation
           }

           override fun onFailure(e: TerminalException) {
               // Placeholder for handling exception
           }
       }
   )
   ```

1. When the SDK sends [onReaderReconnectStarted](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-started.html) to your app, display a message announcing that the reader lost connection and reconnection is in progress.
   - You can use the `Cancelable` object to stop the reconnection attempt at any time.
1. When the SDK indicates successful reconnection by sending [`onReaderReconnectSucceeded`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-succeeded.html), display a message announcing the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader and sends both [`onReaderReconnectFailed`](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-reconnection-listener/on-reader-reconnect-failed.html) and `onDisconnect`, display a message stating that an unexpected disconnect occurred.

#### Kotlin

```kotlin
class CustomMobileReaderListener : MobileReaderListener {
    // ...

    override fun onReaderReconnectStarted(reader: Reader, cancelReconnect: Cancelable, reason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    override fun onReaderReconnectSucceeded(reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }

    override fun onReaderReconnectFailed(reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }

    // ...
}
```

#### Automatic reconnection on application start

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [Shared Preferences API](https://developer.android.com/training/data-storage/shared-preferences) (Android).

1. When your app launches, check the persistent data storage location for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is happening.

## Update reader software [Client-side]

- [MobileReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-mobile-reader-listener/index.html)

Your application must update mobile readers to apply the following:

- Regional configurations that keep you up to date with card network and issuer requirements
- Security updates

Required updates start installing on connection to the reader. You can’t use the reader until updating completes.

> To install updates, the reader’s battery level must be higher than 50%.

### Required updates

When immediately required updates are available for the reader, the integration’s `MobileReaderListener` receives `onStartInstallingUpdate` with a `ReaderSoftwareUpdate`.

The `ReaderSoftwareUpdate` provides the necessary details of the update, including an estimate of the total update duration, indicated by `durationEstimate`.

During the installation process, the Terminal’s `connectionStatus` transitions to `ConnectionStatus.CONNECTING` while the update installs on the reader.

Your application must notify users that an update is installing and display the progress in your UI. Make it clear why connecting might take longer than usual.

If the required update process fails, Stripe communicates the error to the `MobileReaderListener` with `onFinishInstallingUpdate`. You can’t reconnect to the reader after a required update fails, unless the following conditions are met:

- The reader runs the latest software version for the location within the last 30 days.
- The Android SDK version is greater than or equal to `3.5.0`.

If the conditions are met, the connection process succeeds despite an incomplete update. Stripe retries the required update the next time you connect to that reader until it’s successfully installed.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onStartInstallingUpdate(update: ReaderSoftwareUpdate, cancelable: Cancelable) {
        // Show UI communicating that a required update has started installing
    }

    override fun onReportReaderSoftwareUpdateProgress(progress: Float) {
        // Update the progress of the installation
    }

    override fun onFinishInstallingUpdate(update: ReaderSoftwareUpdate?, e: TerminalException?) {
        // Report success or failure of the update
    }

    // ...
}
```

You can cancel required updates using the `Cancelable` object, which also results in a failed connection to the reader. You can’t cancel in-progress incremental-only updates.

### Optional updates

You can defer optional updates until the specified date, after which they become required. The SDK notifies you of optional updates through the `MobileReaderListener` any time the reader is connected but not performing a transaction. If an optional update is available, your application’s `MobileReaderListener` receives the `onReportAvailableUpdate` callback with the `ReaderSoftwareUpdate` object containing the update details, including:

- Estimated time for update to complete (`durationEstimate`)
- Date after which the update becomes required (`requiredAt`)

In your application, notify users that an update is available, and display a prompt to optionally continue with the update.

To proceed with the update previously reported with `onReportAvailableUpdate`, call `Terminal.getInstance().installAvailableUpdate`.

The available update is also stored on the reader object as `reader.availableUpdate`.

As the update proceeds, block the user from leaving the page in your app, and instruct the user to keep the reader connected until the update completes. We recommend also providing your user with a visual indicator of the update’s progress. The `MobileReaderListener` reports the update’s progress in the `onReportReaderSoftwareUpdateProgress` method.

When an optional update’s `requiredAt` date has passed, the update installs the next time the reader is connected.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), MobileReaderListener {
    // ...

    override fun onReportAvailableUpdate(update: ReaderSoftwareUpdate) {
        // An update is available for the connected reader. Show this update in your application.
        // Install this update using `Terminal.getInstance().installAvailableUpdate`.
    }

    // ...
}
```

See [Testing reader updates](https://docs.stripe.com/terminal/references/testing.md#simulated-reader-updates) to learn more about making sure your application handles the different update types that a reader can have.

# USB Readers

> This is a USB Readers for when terminal-sdk-platform is react-native and reader-type is usb. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=react-native&reader-type=usb.

> #### Platform support
>
> Support for connecting to mobile readers using the React Native SDK is limited to the Android platform at this time.

Use the Stripe Terminal React Native SDK beta.13 (or later) to support USB connections for the [Stripe Reader M2](https://docs.stripe.com/terminal/payments/setup-reader/stripe-m2.md) and [BBPOS WisePad 3](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepad3.md) readers.

You must use a USB cable that supports both data and charging, like the USB 2.0 cable that’s included with the Stripe Reader M2 and BBPOS WisePad 3. If the cable included with your Terminal reader is charge-only, use a third-party USB 2.0 cable that can also transfer data.

To connect your app to a Terminal reader with a USB cable:

1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers).
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader).

## Discover readers [Client-side]

- [discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverreaders-1)
- [DiscoveryReaderParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/types/DiscoverReadersParams.html)

Make sure the reader is powered on and connected with a USB 2.0 cable to the device running your app, and permission has been granted to access the USB-connected reader.

If you’re plugging in the reader for the first time, an Android system prompt displays to connect to the reader. You can select the “Always open” checkbox to open your app without prompting when it’s connected to a reader.

Then from your app, search for the connected reader with the `discoverReaders` method, using `usb` as the `DiscoveryMethod` .

```js
function DiscoverReadersScreen() {
  const { discoverReaders, discoveredReaders } = useStripeTerminal({
    onUpdateDiscoveredReaders: (readers) => {
      // After the SDK discovers a reader, your app can connect to it.
    },
  });

  useEffect(() => {
    handleDiscoverReaders();
  }, []);

  const handleDiscoverReaders = async () => {
    // The list of discovered readers is reported in the `onUpdateDiscoveredReaders` method
    // within the `useStripeTerminal` hook.
    const { error } = await discoverReaders({
      discoveryMethod: "usb",
    });

    if (error) {
      Alert.alert(
        "Discover readers error: ",
        `${error.code}, ${error.message}`,
      );
    }
  };

  return <View />;
}
```

## Connect to a reader [Client-side]

- [connectReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1)
- [ConnectUsbReaderParams (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/ConnectUsbReaderParams.html)

To connect to a discovered reader, call the `connectReader` method from your app.

Mobile readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your mobile reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, pass the relevant `locationId` to `ConnectUsbReaderParams` when connecting.

```js
const handleConnectUsbReader = async (id) => {
  const { reader, error } = await connectReader({
    discoveryMethod: 'usb',
    reader: selectedReader,
    locationId: {{LOCATION_ID}},
  });

  if (error) {
    console.log('connectReader error', error);
    return;
  }

  console.log('Reader connected successfully', reader);
};
```

> #### Use standby mode
>
> Don’t program your app to call `disconnectReader` to conserve power. The reader efficiently handles power management using its standby mode.

## Handle reader disconnects

- [REPORT_UNEXPECTED_READER_DISCONNECT (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#REPORT_UNEXPECTED_READER_DISCONNECT)
- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)
- [DisconnectReason (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/modules/Reader.html#DisconnectReason)

Reader disconnects can sometimes occur between your app and the reader. For example, the reader can disconnect from your app if the USB cable connecting it to your device is disconnected. You can simulate an unexpected disconnect while testing by powering off the reader.

`UserCallbacks` includes `onDidDisconnect` that provides your application with the `DisconnectReason` to help identify why the reader disconnected.

To handle reader disconnects yourself, you can do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` during connection.
1. Handle the disconnect callback to display a message in the app alerting the user that the reader unexpectedly disconnected and initiate reader discovery and connection.

```js
const terminal = useStripeTerminal({
  onDidDisconnect: (result) => {
    // Consider displaying a UI to notify the user and start rediscovering readers
  },
});
```

### Reboot the connected reader

- [rebootReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#rebootReader)

Stripe Reader M2 and BBPOS WisePad 3 automatically reboot after operating for 24 hours. However, you can force the reader to reboot and reset its 24-hour timer by using the `rebootReader` API. After this action, the reader disconnects from the SDK and then reboots. If you’re using automatic reconnect, the SDK attempts to restore the connection with the reader.

```js
const { error } = await rebootReader();

if (error) {
  console.log("rebootReader error:", error);
  return;
}

console.log("rebootReader succeeded");
```

#### Automatically attempt reconnection

When a reader disconnects, we automatically attempt reconnection by default and recommend that you display notifications in your app relaying the reader status throughout the process.

To display notifications in your app during automatic reconnection, do the following:

1. Set `autoReconnectOnUnexpectedDisconnect` to true on the `ConnectUsbReaderParams`.
1. Implement the auto reconnect callbacks found in the `UserCallbacks`.
1. When the SDK sends `onDidStartReaderReconnect` to your app, display a message announcing that the reader lost connection and reconnection is in progress.
   - You can use `cancelReaderReconnection` to stop the reconnection attempt at any time.
1. When the SDK indicates successful reconnection by sending `onDidSucceedReaderReconnect`, display a message announcing the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader and sends `onDidFailReaderReconnect`, display a message stating that an unexpected disconnect occurred.

#### Automatic reconnection on application start

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as [Async Storage](https://github.com/react-native-async-storage/async-storage) (React Native).

1. When your app launches, check the persistent data storage location for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is happening.

## Update reader software [Client-side]

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

Your application must update mobile readers to apply the following:

- Regional configurations that keep you up to date with card network and issuer requirements
- Security updates

Required updates start installing on connection to the reader. You can’t use the reader until updating completes.

> To install updates, the reader’s battery level must be higher than 50%.

### Required updates

When immediately required updates are available for the reader, the integration receives `onDidStartInstallingUpdate` from the `useStripeTerminal` hook with a `Reader.SoftwareUpdate`.

The `Reader.SoftwareUpdate` provides the necessary details of the update, including an estimate of the total update duration, indicated by `estimatedUpdateTime`.

During the installation process, the Terminal’s `connectionStatus` transitions to `"connecting"` while the update installs on the reader.

Your application must notify users that an update is installing and display the progress in your UI. Make it clear why connecting might take longer than usual.

If the required update process fails, Stripe communicates the error to the `useStripeTerminal` hook with `onDidFinishInstallingUpdate`. You can’t reconnect to the reader after a required update fails, unless the following conditions are met:

- The reader runs the latest software version for the location within the last 30 days.
- The React Native SDK version is greater than or equal to `0.0.1-beta.18`.

If the conditions are met, the connection process succeeds despite an incomplete update. Stripe retries the required update the next time you connect to that reader until it’s successfully installed.

```js
const terminal = useStripeTerminal({
  onDidReportReaderSoftwareUpdateProgress: (progress) => {
    setCurrentProgress((Number(progress) * 100).toFixed(0).toString());
  },
  onDidFinishInstallingUpdate: ({ error }) => {},
  onDidStartInstallingUpdate: (update) => {},
});
```

You can cancel required updates using the `cancelInstallingUpdate` API, which also results in a failed connection to the reader. You can’t cancel in-progress incremental-only updates.

### Optional updates

You can defer optional updates until the specified date, after which they become required. The SDK notifies you of optional updates through the `onDidReportAvailableUpdate` callback from the `useStripeTerminal` hook any time the reader is connected but not performing a transaction. If an optional update is available, your application’s `useStripeTerminal` hook receives the `onDidReportAvailableUpdate` callback with the `SoftwareUpdate` object containing the update details, including:

- Estimated time for update to complete (`estimatedUpdateTime`)
- Date after which the update becomes required (`requiredAt`)

In your application, notify users that an update is available, and display a prompt to optionally continue with the update.

To proceed with the update previously reported with `onDidReportAvailableUpdate`, call `installAvailableUpdate` from the `useStripeTerminal` hook.

The available update is also stored on the reader object as `reader.availableUpdate`.

As the update proceeds, block the user from leaving the page in your app, and instruct the user to keep the reader in range and powered on until the update completes. We recommend also providing your user with a visual indicator of the update’s progress. The `useStripeTerminal` hook reports the update’s progress in the `onDidReportReaderSoftwareUpdateProgress` method.

When an optional update’s `requiredAt` date has passed, the update installs the next time the reader is connected.

```js
const terminal = useStripeTerminal({
  onDidReportAvailableUpdate: (update) => {
    // An update is available for the connected reader. Show this update in your application.
    // Install this update using the `installAvailableUpdate` method from the `useStripeTerminal` hook.
  },
});
```

See [Testing reader updates](https://docs.stripe.com/terminal/references/testing.md#simulated-reader-updates) to learn more about making sure your application handles the different update types that a reader can have.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is server-driven and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=server-driven&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Before you can connect your application to a smart reader, you must register the reader to your Stripe account.

#### Dashboard

You can register your reader directly in the [Dashboard](https://dashboard.stripe.com/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader. You can only register readers that you or your platform have ordered.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your application, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. Go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings), and then tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

After you register your reader, it’s ready to use with the server-driven integration. We recommend storing the reader ID (`tmr_xxx`) within your application so you know which reader to send transactions to from your point of sale. You can retrieve reader IDs using the [list readers](https://docs.stripe.com/api/terminal/readers/list.md) endpoint.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is js and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=js&reader-type=internet.

> #### Recommendation for smart readers
>
> For smart readers, such as the [BBPOS WisePOS E reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md), [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), and [Verifone readers](https://docs.stripe.com/terminal/payments/setup-reader/verifone.md), we recommend using the [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven) instead of the JavaScript SDK.
>
> The JavaScript SDK requires your POS and reader on the same local network with working local DNS. The server-driven integration uses the Stripe API instead, which can be simpler in complex network environments. See our [platform comparison](https://docs.stripe.com/terminal/payments/setup-reader.md#sdk) to help you choose the best platform for your needs.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [discoverReaders (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#discover-readers)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application with `discoverReaders`, setting `discoveryMethod` to `internet`.

You can scope your discovery using the `location` you registered the reader to in the previous step.

```javascript
async function discoverReaders() {
  const config = { simulated: false, location: "{{LOCATION_ID}}" };
  const discoverResult = await terminal.discoverReaders(config);
  if (discoverResult.error) {
    console.log("Failed to discover: ", discoverResult.error);
  } else if (discoverResult.discoveredReaders.length === 0) {
    console.log("No available readers.");
  } else {
    // You should show the list of discoveredReaders to the
    // cashier here and let them select which to connect to (see below).
    connectReader(discoverResult);
  }
}
```

## Connect to a reader [Client-side]

> Chrome 142 (released October 28, 2025) and later versions require explicit permission before websites can access local network devices (like Terminal readers) when using the Stripe Terminal JavaScript SDK. For setup steps and troubleshooting, see [Chrome 142+ instructions](https://support.stripe.com/questions/ensuring-stripe-terminal-javascript-sdk-functionality-on-chrome-142).

To connect your point-of-sale application to a reader, call [connectReader](https://docs.stripe.com/terminal/references/api/js-sdk.md#connect-reader) with the selected reader.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

```javascript
async function connectReader(discoverResult) {
  // Just select the first reader here.
  const selectedReader = discoverResult.discoveredReaders[0];

  const connectResult = await terminal.connectReader(selectedReader);
  if (connectResult.error) {
    console.log("Failed to connect:", connectResult.error);
  } else {
    console.log("Connected to reader:", connectResult.reader.label);
  }
}
```

- [connectReader (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#connect-reader)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `connectReader` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `connectReader` method takes a configuration object with a `fail_if_in_use` property, whose default value is `false`. When your application sets `fail_if_in_use` to true, the `connectReader` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `collectPaymentMethod` or `processPayment` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `collectPaymentMethod` is called), setting `fail_if_in_use` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

```javascript
const connectResult = await terminal.connectReader(reader, {
  fail_if_in_use: true,
});
```

|                                                                           | fail_if_in_use is false (default)                                                                                                                                                                                   | fail_if_in_use is true                                                                                                                                                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectReader` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. |
| `connectReader` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                       |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `fail_if_in_use` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `fail_if_in_use` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [StripeTerminal.create (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#stripeterminal-create)

Your app must implement the `onUnexpectedReaderDisconnect` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `discoverReaders` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

```javascript
const terminal = StripeTerminal.create({
  onFetchConnectionToken: fetchConnectionToken,
  onUnexpectedReaderDisconnect: unexpectedDisconnect,
});

function unexpectedDisconnect() {
  // Consider displaying a UI to notify the user and start rediscovering readers
}
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [localStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
1. When your app launches, check that persistent store for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is ios and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [discoverReaders (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>)
- [InternetDiscoveryConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPInternetDiscoveryConfiguration.html)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application with `discoverReaders`, using `InternetDiscoveryConfiguration`.

You can scope your discovery using the `location` you registered the reader to in the previous step.

#### Swift

```swift
import StripeTerminal

class DiscoverReadersViewController: UIViewController, DiscoveryDelegate {
  func discoverReadersAction() throws {
      let config = try InternetDiscoveryConfigurationBuilder()
                          .setLocationId(""{{LOCATION_ID}}"")
                          .build()
      // In addition to Terminal's completion block methods, Swift async alternatives are available.
      // See our Example app for usage examples: https://github.com/stripe/stripe-terminal-ios/tree/master/Example
      self.discoverCancelable = Terminal.shared.discoverReaders(config, delegate: self) { error in
          if let error = error {
              print("discoverReaders failed: \(error)")
          } else {
              print("discoverReaders succeeded")
          }
      }
  }
}
```

When discovering smart readers, the `DiscoveryDelegate.didUpdateDiscoveredReaders` method is only called once per call to `discoverReaders`. `didUpdateDiscoveredReaders` returns an empty list of readers if there are no registered readers or if there are no readers associated with the given location. If you make a subsequent `discoverReaders` call to refresh the list, you must first cancel the previous call with the `Cancelable` returned by `discoverReaders`.

The `InternetDiscoveryConfiguration` supports an optional `timeout` value for discovering readers online. This ensures quicker fallback to offline reader discovery if the online attempt fails.

## Connect to a reader [Client-side]

> In version `5.1.0` of the iOS SDK, you can use the `easyConnect` method to combine reader discovery and connection into a single API call to simplify integration. See the [SDK migration guide](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#update-your-reader-connection-usage-ios) for details.

To connect your point-of-sale application to a reader, call `connectReader` with the selected reader, using the `InternetConnectionConfiguration`.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

#### Swift

```swift
let config: InternetConnectionConfiguration
do {
    config = try InternetConnectionConfigurationBuilder(delegate: yourInternetReaderDelegate)
        .build()
} catch {
    // Handle error building the connection configuration
    return
}

Terminal.shared.connectReader(selectedReader, connectionConfig: config) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectReader failed: \(error)")
    }
}
```

- [connectReader (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:connectionConfig:completion:>)
- [InternetConnectionConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPInternetConnectionConfiguration.html)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `connectReader` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `connectReader` method takes a configuration object with a `failIfInUse` property, whose default value is `false`. When your application sets `failIfInUse` to true, the `connectReader` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `collectPaymentMethod` or `confirmPaymentIntent` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `collectPaymentMethod` is called), setting `failIfInUse` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

#### Swift

```swift
let internetReaderDelegate = yourInternetReaderDelegate // implement your internetReaderDelegate

let config: InternetConnectionConfiguration
do {
    config = try InternetConnectionConfigurationBuilder(delegate: internetReaderDelegate)
          .setFailIfInUse(true)
          .build()
} catch {
    // Handle error building the connection configuration
    return
}
Terminal.shared.connectReader(selectedReader, connectionConfig: config, completion: { reader, error in
    // ...
})
```

|                                                                           | failIfInUse is false (default)                                                                                                                                                                                       | failIfInUse is true                                                                                                                                                                                                  |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectReader` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `didDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `didDisconnect` method is called. |
| `connectReader` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `didDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                        |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `failIfInUse` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `failIfInUse` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [didDisconnect (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didDisconnect:>)

Your app must implement the `reader(_, didDisconnect:)` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `discoverReaders` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

#### Swift

```swift
import StripeTerminal

class ReaderViewController: UIViewController, InternetReaderDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Set the reader delegate when connecting to a reader
    }

    // ...



    func reader(_ reader: Reader, didDisconnect reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
}
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [UserDefaults API](https://developer.apple.com/documentation/foundation/userdefaults) (iOS)
1. When your app launches, check that persistent store for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is android and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [InternetDiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-internet-discovery-configuration/index.html)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application with `discoverReaders`, using `InternetDiscoveryConfiguration`.

You can scope your discovery using the `location` you registered the reader to in the previous step.

#### Kotlin

```kotlin
var discoveryCancelable: Cancelable? = null

fun onDiscoverReaders() {
    val timeout = 0
    val isSimulated = false

    val config = InternetDiscoveryConfiguration(
        timeout = timeout,
        isSimulated = isSimulated,
        location = ""{{LOCATION_ID}}""
    )

    // Save this cancelable to an instance variable
    discoveryCancelable = Terminal.getInstance().discoverReaders(
        config,
        object : DiscoveryListener {
            override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
                // Display the discovered readers to the user
            }
        },
        object : Callback {
            override fun onSuccess() {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
}

override fun onStop() {
    super.onStop()

    // If you're leaving the activity or fragment without selecting a reader,
    // make sure you cancel the discovery process or the SDK will be stuck in
    // a discover readers phase.
    discoveryCancelable?.cancel(
        object : Callback {
            override fun onSuccess() {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
}
```

## Connect to a reader [Client-side]

> In version `5.0.0` of the Android SDK, you can use the `easyConnect` method to combine reader discovery and connection into a single API call for a simpler integration experience. See the [SDK migration guide](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#update-your-reader-connection-usage) for details.

To connect your point-of-sale application to a reader, call `connectReader` with the selected reader, using the `InternetConnectionConfiguration`.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

#### Kotlin

```kotlin
val internetReaderListener = yourInternetReaderListener

val config = InternetConnectionConfiguration(internetReaderListener)
Terminal.getInstance().connectReader(
    firstReader,
    config,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

- [connectReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [InternetConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-internet-connection-configuration/index.html)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `connectReader` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `connectReader` method takes a configuration object with a `failIfInUse` property, whose default value is `false`. When your application sets `failIfInUse` to true, the `connectReader` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `collectPaymentMethod` or `confirmPaymentIntent` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `collectPaymentMethod` is called), setting `failIfInUse` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

#### Kotlin

```kotlin
val failIfInUse = true
val internetReaderListener = yourInternetReaderListener

val config = InternetConnectionConfiguration(internetReaderListener, failIfInUse)
Terminal.getInstance().connectReader(
    reader,
    config,
    object : ReaderCallback {
        override fun onSuccess(reader: Reader) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

|                                                                           | failIfInUse is false (default)                                                                                                                                                                                      | failIfInUse is true                                                                                                                                                                                                 |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectReader` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. |
| `connectReader` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                       |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `failIfInUse` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `failIfInUse` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [onDisconnect (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-reader-disconnect-listener/on-disconnect.html)

Your app must implement the `onDisconnect` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `discoverReaders` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), InternetReaderListener {
    // ...

    override fun onDisconnect(reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [Shared Preferences API](https://developer.android.com/training/data-storage/shared-preferences) (Android).
1. When your app launches, check that persistent store for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is react-native and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=react-native&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application with `discoverReaders`, setting `discoveryMethod` to `internet`.

You can scope your discovery using the `location` you registered the reader to in the previous step.

```js
export default function DiscoverScreen() {
  const { discoverReaders, discoveredReaders } = useStripeTerminal({
    onUpdateDiscoveredReaders: (readers) => {
      // After the SDK discovers a reader, your app can connect to it.
    },
  });

  useEffect(() => {
    const fetchReaders = async () => {
      const { error } = await discoverReaders({
        discoveryMethod: "internet",
      });
    };

    fetchReaders();
  }, [discoverReaders]);

  return <View />;
}
```

## Connect to a reader [Client-side]

> In version `0.0.1-beta.29` of the React Native SDK, you can use the [easyConnect](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#easyconnect) method to combine reader discovery and connection into a single API call for a simpler integration experience.

To connect your point-of-sale application to a reader, call `connectReader` with the selected reader.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

```js
const { reader, error } = await connectReader({
  discoveryMethod: "internet",
  reader,
});

if (error) {
  console.log("connectReader error:", error);
  return;
}

console.log("Reader connected successfully", reader);
```

- [connectReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `connectReader` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `connectReader` method takes a configuration object with a `failIfInUse` property, whose default value is `false`. When your application sets `failIfInUse` to true, the `connectReader` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `collectPaymentMethod` or `confirmPaymentIntent` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `collectPaymentMethod` is called), setting `failIfInUse` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

```js
const { reader: connectedReader, error } = await connectReader({
  discoveryMethod: "internet",
  reader,
  failIfInUse: true,
});
```

|                                                                                   | failIfInUse is false (default)                                                                                                                                                                                         | failIfInUse is true                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectInternetReader` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDidDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDidDisconnect` method is called. |
| `connectInternetReader` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDidDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                          |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `failIfInUse` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `failIfInUse` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#UserCallbacks)

Your app must implement the `onDidDisconnect` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `discoverReaders` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

```js
const terminal = useStripeTerminal({
  onDidDisconnect: (result) => {
    // Consider displaying a UI to notify the user and start rediscovering readers
  },
});
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is java and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=java&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [discoverReaders (Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [InternetDiscoveryConfiguration (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-internet-discovery-configuration/index.html)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application with `discoverReaders`, using `InternetDiscoveryConfiguration`.

You can scope your discovery using the `location` you registered the reader to in the previous step.

```java
private Cancelable discoveryCancelable;

public void onDiscoverReaders() {
    int timeout = 0;
    boolean isSimulated = false;

    InternetDiscoveryConfiguration config = new InternetDiscoveryConfiguration(
        timeout,
        ""{{LOCATION_ID}}"",
        isSimulated,
        DiscoveryFilter.None.INSTANCE
    );

    // Save this cancelable to an instance variable
    discoveryCancelable = Terminal.getInstance().discoverReaders(
        config,
        readers -> {
            // Display the discovered readers to the user
        },
        new Callback() {
            @Override
            public void onSuccess() {
                // Placeholder for handling successful operation
            }

            @Override
            public void onFailure(@NotNull TerminalException e) {
                // Placeholder for handling exception
            }
        }
    );
}
```

## Connect to a reader [Client-side]

> In version `1.0.0-b15` of the Java SDK, you can use the [easyConnect](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/easy-connect.html) method to combine reader discovery and connection into a single API call for a simpler integration.

To connect your point-of-sale application to a reader, call `connectReader` with the selected reader, using the `InternetConnectionConfiguration`.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

```java
InternetReaderListener internetReaderListener = yourInternetReaderListener;

InternetConnectionConfiguration config = new InternetConnectionConfiguration(internetReaderListener);

Terminal.getInstance().connectReader(
    reader,
    config,
    new ReaderCallback() {
        @Override
        public void onSuccess(@NotNull Reader reader) {
            // Placeholder for handling successful operation
        }

        @Override
        public void onFailure(@NotNull TerminalException e) {
            // Placeholder for handling exception
        }
    }
);
```

- [connectReader (Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [InternetConnectionConfiguration (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-connection-configuration/-internet-connection-configuration/index.html)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `connectReader` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `connectReader` method takes a configuration object with a `failIfInUse` property, whose default value is `false`. When your application sets `failIfInUse` to true, the `connectReader` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `collectPaymentMethod` or `confirmPaymentIntent` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `collectPaymentMethod` is called), setting `failIfInUse` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

```java
boolean failIfInUse = true;
InternetReaderListener internetReaderListener = yourInternetReaderListener;

InternetConnectionConfiguration config =
    new InternetConnectionConfiguration(internetReaderListener, failIfInUse);

Terminal.getInstance().connectReader(
    reader,
    config,
    new ReaderCallback() {
        @Override
        public void onSuccess(@NotNull Reader reader) {
            // Placeholder for handling successful operation
        }

        @Override
        public void onFailure(@NotNull TerminalException e) {
            // Placeholder for handling exception
        }
    }
);
```

|                                                                           | failIfInUse is false (default)                                                                                                                                                                                      | failIfInUse is true                                                                                                                                                                                                 |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectReader` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. |
| `connectReader` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `onDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                       |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `failIfInUse` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `failIfInUse` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [onDisconnect (Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.callable/-reader-disconnect-listener/on-disconnect.html)

Your app must implement the `onDisconnect` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `discoverReaders` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

```java
public class CustomReaderListener implements InternetReaderListener {
    // ...

    @Override
    public void onDisconnect(@NotNull DisconnectReason reason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

1. When you successfully connect to a reader, save its serial number in a persistent data storage location, such as the [Preferences API](https://docs.oracle.com/javase/8/docs/api/java/util/prefs/Preferences.html).
1. When your app launches, check that persistent store for a saved serial number. If one is found, call the `discoverReaders` method so your application can try to find that reader again.
1. If the saved serial number matches any of the discovered readers, try connecting to that reader with the matching reader object returned from the call to `discoverReaders`. If the previously connected reader isn’t found, stop the discovery process.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Internet Readers

> This is a Internet Readers for when terminal-sdk-platform is dotnet and reader-type is internet. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=dotnet&reader-type=internet.

Smart readers run Stripe reader software to communicate directly with Stripe over the internet. Connecting your app to a smart reader requires three steps:

1. [Register a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#register-reader) to your Stripe account.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) with the SDK.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) with the SDK.

## Register a reader [Server-side]

Before you can connect your application to a smart reader, you must register the reader to your account.

#### Dashboard

### Register in the Dashboard

You can add your reader directly in the [Dashboard](https://dashboard.stripe.com/test/terminal).

#### Register by registration code

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. Enter the registration code then click **Next**.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by serial number

1. In the [Readers](https://dashboard.stripe.com/terminal/readers) page, click **Register reader**.
1. Find the serial number on the device and enter the serial number. To register multiple devices at once, you can enter multiple serial numbers separated by commas.
1. Optionally, choose a name for the reader.
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your reader.

#### Register by hardware order

1. In the [Hardware orders](https://dashboard.stripe.com/terminal/hardware_orders) page, find an order with a status of either “shipped” or “delivered.” Click the overflow menu (⋯) at the end of the row, then click **Register**.
1. On the **Register Readers** page, select one or more readers from the hardware order to register, then click **Register**.
1. Optionally, choose a name for the reader. If you selected multiple readers, the name serves as a prefix and we name the readers sequentially (for example, for a given input of “Test reader”, we name the readers “Test reader 1”, “Test reader 2”, and so on).
1. If you already created a Location, select the reader’s new Location. Otherwise, create a Location by clicking **+ Add new**.
1. Click **Register** to finish registering your readers.

#### API

For larger deployments, enable users in the field to receive and set up new readers on their own. In your app, build a flow to [register](https://docs.stripe.com/api/terminal/readers/create.md) a reader with the Stripe API.

1. If you have a [smart reader](https://docs.stripe.com/terminal/smart-readers.md), enter the key sequence `0-7-1-3-9` to display a unique registration code. If you have a BBPOS WisePOS E or Stripe Reader S700/S710, go to the [reader settings](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e.md#settings) and tap **Generate pairing code**.
1. The user enters the code in your application.
1. Your application sends the code to Stripe:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.create({
  registration_code: "{{READER_REGISTRATION_CODE}}",
  label: "Alice's reader",
  location: "{{TERMINALLOCATION_ID}}",
});
```

To confirm that you’ve registered a reader correctly, list all the readers you’ve registered at that location:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const readers = await stripe.terminal.readers.list();
```

## Discover readers [Client-side]

- [DiscoverReadersAsync (.NET)](https://docs.stripe.com/terminal/payments/connect-reader.md#TODO-DOTNET-FIXME)

After registering the reader to your account, search for previously registered readers to connect to your point-of-sale application using the `DiscoverReadersAsync` method.

You can scope your discovery using the `location` you registered the reader to in the previous step.

```csharp
public async Task<IImmutableList<Reader>> DiscoverReadersAsync()
{

    try
    {
        var config = new DiscoveryConfiguration.Builder()
          .SetIsSimulated(false)
          .SetLocation("{{LOCATION_ID}}")
          .Build();

        Console.WriteLine("Discovered readers");
        return await Terminal.Instance.DiscoverReadersAsync(config);
    }
    catch (TerminalException ex)
    {
        // Placeholder for handling exception
        throw;
    }

}
```

## Connect to a reader [Client-side]

To connect your point-of-sale application to a reader, call `ConnectInternetReaderAsync` with the selected reader.

To prevent connection failures, make sure you always pass a reader object from the most recent discovery results. Don’t cache or reuse reader objects from a previous discovery session.

```csharp
// after selecting a reader to connect to
Reader connectedReader;
try
{
    var config = new InternetConnectionConfiguration.Builder()
        .Build();
    connectedReader = await Terminal.Instance.ConnectInternetReaderAsync(selectedReader, config);
    Console.WriteLine("Connected to reader");
}
catch (TerminalException ex)
{
    // Placeholder for handling exception
    throw;
}
```

- [ConnectInternetReaderAsync (.NET)](https://docs.stripe.com/terminal/payments/connect-reader.md#TODO-DOTNET-FIXME)

### Multiple connections

Only one instance of the Stripe Terminal SDK can connect to a reader at a given time. By default, when you call `ConnectInternetReaderAsync` from another application, the incoming connection replaces the existing SDK-to-reader connection, and the previously connected SDK disconnects from the reader. The `ConnectInternetReaderAsync` method takes a configuration object with a `failIfInUse` property, whose default value is `false`. When your application sets `failIfInUse` to true, the `ConnectInternetReaderAsync` call has an alternate behavior where the incoming connection fails when the reader is in the middle of a `CollectPaymentMethodAsync` or `ConfirmPaymentIntentAsymc` call initiated by another SDK. If the reader is connected to another SDK but is idle (displaying the splash screen before `CollectPaymentMethodAsync` is called), setting `failIfInUse` has no change to the connection behavior, and the incoming connection request can always break the existing SDK-to-reader connection.

```csharp
// after selecting a reader to connect to
Reader connectedReader;
try
{
    var config = new InternetConnectionConfiguration.Builder()
        .SetFailIfInUse(true)
        .Build();
    connectedReader = await Terminal.Instance.ConnectInternetReaderAsync(selectedReader, config);
    Console.WriteLine("Connected to reader");
}
catch (TerminalException ex)
{
    // Placeholder for handling exception
    throw;
}
```

|                                                                                        | FailIfInUse is false (default)                                                                                                                                                                                                      | FailIfInUse is true                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConnectInternetReaderAsync` called from a new SDK when the reader is idle.            | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `OnUnexpectedReaderDisconnect` method is called. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `OnUnexpectedReaderDisconnect` method is called. |
| `ConnectInternetReaderAsync` called from a new SDK when the reader is mid-transaction. | The existing SDK-to-reader connection breaks, and the new SDK connects to the reader. The next command from the previously-connected SDK fails with a reader error, and that app’s `OnUnexpectedReaderDisconnect` method is called. | The incoming connection fails with a reader error. The existing SDK-to-reader connection doesn’t break and the command in progress continues.                                                                                       |

For the least-disruptive connection experience in multi-reader environments, we recommend setting `failIfInUse` to `true` on your application’s initial connection attempt. Then, allow your users to retry the connection with `failIfInUse` set to `false` if the connection fails the first time.

With this setup, one of your users can’t accidentally interrupt a transaction by inadvertently connecting to an in-use reader, but can still connect if needed.

### Handle disconnects

- [TerminalListener (.NET)](https://docs.stripe.com/terminal/payments/connect-reader.md#TODO-DOTNET-FIXME)

Your app must implement the `OnUnexpectedReaderDisconnect` callback to handle when a reader disconnects. When you implement this callback, display a UI that notifies your user of the disconnected reader. You can call `DiscoverReadersAsync` to scan for readers and initiate reconnection.

Your app can attempt to automatically reconnect to the disconnected reader or display a UI that prompts your user to reconnect to a different reader.

The reader can disconnect from your app if it loses connection to the network. To simulate an unexpected disconnect, power off the reader.

```csharp
public class TerminalListener : ITerminalListener
{

    // ...

    Terminal.InitTerminal(
        connectionTokenProvider: connectionTokenProvider,
        terminalListener: this,
        offlineListener: offlineListener,
        applicationInformation: applicationInformation
    );

    // ITerminalListener
    public void OnUnexpectedReaderDisconnect(Reader reader)
    {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

}
```

### Automatic reconnection

Stripe Terminal doesn’t automatically reconnect to a reader when your application starts. Instead, you can build a reconnection flow by storing reader IDs and attempting to connect to a known reader on startup.

Display some UI during the discovery and connection process to indicate that an automatic reconnection is taking place.

# Tap to Pay on iPhone

> This is a Tap to Pay on iPhone for when terminal-sdk-platform is ios and reader-type is tap-to-pay. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=tap-to-pay.

Tap to Pay on iPhone lets users accept in-person contactless payments with a [compatible iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#supported-devices) and the [Stripe Terminal SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios). Tap to Pay on iPhone supports Visa, Mastercard, American Express, and Discover contactless cards and NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay). Tap to Pay on iPhone is included in the Terminal iOS SDK and enables payments directly in your iOS mobile app.

## Discover readers

- [discoverReaders (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>)
- [TapToPayDiscoveryConfiguration (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Reader%20Discovery%20%26%20Connection.html#/c:objc(cs)SCPTapToPayDiscoveryConfiguration>)

Use the [discoverReaders](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:>) method to determine whether your iPhone is supported for Tap to Pay.

The `completion` handler invokes with an error if your application runs on a device that doesn’t meet the [supported device criteria](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#supported-devices).

#### Swift

```swift
import StripeTerminal

class DiscoverReadersViewController: UIViewController, DiscoveryDelegate {

    var discoverCancelable: Cancelable?

    // ...

    // Action for a "Discover Readers" button
    func discoverReadersAction() throws {
        let config = try TapToPayDiscoveryConfigurationBuilder().build()
        // In addition to Terminal's completion block methods, Swift async alternatives are available.
        // See our Example app for usage examples: https://github.com/stripe/stripe-terminal-ios/tree/master/Example
        self.discoverCancelable = Terminal.shared.discoverReaders(config, delegate: self) { error in
            if let error = error {
                print("discoverReaders failed: \(error)")
            } else {
                print("discoverReaders succeeded")
            }
        }
    }

    // ...

    // MARK: DiscoveryDelegate

    func terminal(_ terminal: Terminal, didUpdateDiscoveredReaders readers: [Reader]) {
        // In your app, display the ability to use your phone as a reader
        // Call `connectReader` to initiate a session with the phone
    }
}
```

## Connect to a reader

> In version `5.1.0` of the iOS SDK, you can use the `easyConnect` method to combine reader discovery and connection into a single API call to simplify integration. See the [SDK migration guide](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#update-your-reader-connection-usage-ios) for details.

- [connectReader (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)connectReader:connectionConfig:completion:>)
- [TapToPayConnectionConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTapToPayConnectionConfiguration.html)

To begin accepting Tap to Pay on iPhone payments, provide the discovered reader to the `connectReader` method. You also need to [create a delegate](https://docs.stripe.com/terminal/payments/connect-reader.md#device-setup) to handle potential required updates to the reader.

Tap to Pay readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, create and use a `SCPTapToPayConnectionConfiguration` with the `locationId` set to the relevant location ID when connecting.

Set the `display_name` to represent the name of the business when creating a location. Your customer sees the location’s `display_name` on the device’s tap screen unless you explicitly provide the name of a business when you connect to a reader. You can edit existing locations as necessary to adjust this text.

If you use [destination charges with on_behalf_of](https://docs.stripe.com/terminal/features/connect.md#destination-payment-intents), you must also provide the connected account ID in `SCPTapToPayConnectionConfiguration`.

#### Swift

```swift
// Call `connectReader` with the selected reader and a connection config
// to register to a location as set by your app.
let connectionConfig = try TapToPayConnectionConfigurationBuilder.init(locationId: ""{{LOCATION_ID}}"")
.delegate(yourTapToPayReaderDelegate)
.build()
Terminal.shared.connectReader(selectedReader, connectionConfig: connectionConfig) { reader, error in
    if let reader = reader {
        print("Successfully connected to reader: \(reader)")
    } else if let error = error {
        print("connectReader failed: \(error)")
    }
}
```

### Handle device setup

When connecting to a compatible Tap to Pay on iPhone reader, a configuration update might be required and can take up to a few minutes. We recommend connecting to the reader ahead of time in the background to reduce wait time for businesses.

Make sure your application implements `SCPTapToPayReaderDelegate` to handle the configuration steps and display messaging to your business to stand by. You’ll see the configuration steps as a software update so you can display progress to your businesses as appropriate.

#### Swift

```swift
class APPReaderViewController: TapToPayReaderDelegate {

    // MARK: TapToPayReaderDelegate

    // ...

    func tapToPayReader(_ reader: Reader, didStartInstallingUpdate update: ReaderSoftwareUpdate, cancelable: Cancelable?) {
        // In your app, let the user know that an update is being installed on the reader
    }

    func tapToPayReader(_ reader: Reader, didReportReaderSoftwareUpdateProgress progress: Float) {
        // The update or configuration process has reached the specified progress (0.0 to 1.0)
        // If you are displaying a progress bar or percentage, this can be updated here
    }

    func tapToPayReader(_ reader: Reader, didFinishInstallingUpdate update: ReaderSoftwareUpdate?, error: Error?) {
        // The reader has finished installing an update
        // If `error` is nil, it is safe to proceed and start collecting payments
        // Otherwise, check the value of `error` for more information on what went wrong
    }

    func tapToPayReader(_ reader: Reader, didRequestReaderDisplayMesage displayMessage: ReaderDisplayMessage) {
        // This is called to request that a prompt be displayed in your app.
        // Use Terminal.stringFromReaderDisplayMessage(:) to get a user-facing string for the prompt
    }

    func tapToPayReader(_ reader: Reader, didRequestReaderInput inputOptions: ReaderInputOptions = []) {
        // This is called when the reader begins waiting for input
        // Use Terminal.stringFromReaderInputOptions(:) to get a user-facing string for the input options
    }

    // ...
}
```

### Account linking and Apple terms and conditions

All users must accept Apple’s Tap to Pay on iPhone Terms and Conditions before accepting payment for the first time. For Connect users, each connected account must individually accept the Terms and Conditions when:

- A Connect user creates direct charges
- A Connect user creates a destination charge and specifies an `on_behalf_of` account

Users can accept Apple’s Tap to Pay on iPhone Terms and Conditions on the web before connecting to the reader for the first time using [onboarding links](https://docs.stripe.com/api/terminal/onboarding-link.md). Alternatively, users will be presented with Apple’s Tap to Pay on iPhone Terms and Conditions the first time they connect to the reader within a mobile application. To accept Apple’s Terms and Conditions, the user must provide a valid Apple ID representing the business. After users accept Apple’s Tap to Pay on iPhone Terms and Conditions, they aren’t prompted again on subsequent connections using the same Stripe account, including on other mobile devices.
![Three-step process showing Apple ID sign in, terms acceptance, and success confirmation for Tap to Pay on iPhone](assets/stripe-terminal-ttpoi-account-linking-steps.png)

Link your Apple ID account to accept Tap to Pay payments

Any iPhone can use up to 3 unique Stripe accounts across apps within a rolling 24-hour period when calling `connectReader` for Tap to Pay on iPhone. If additional accounts are used for the device within the same 24-hour period, the `connectReader` method raises an [SCPErrorTapToPayReaderMerchantBlocked](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPError.html#/c:@E@SCPError@SCPErrorTapToPayReaderMerchantBlocked) error.

Learn more about account linking in the Tap to Pay on iPhone Business Information section of the [Apple Tap to Pay on iPhone FAQ](https://register.apple.com/tap-to-pay-on-iphone/faq.html).

## Handle disconnects

Your reader disconnects when your application enters the background or when your iPhone loses connectivity. There are two ways you can handle this:

- [TapToPayReaderDelegate (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPTapToPayReaderDelegate.html)

#### Handle the disconnect manually

Your application must implement the [SCPTapToPayReaderDelegate reader:didDisconnect:](<https://stripe.dev/stripe-terminal-ios/docs/Protocols/SCPReaderDelegate.html#/c:objc(pl)SCPReaderDelegate(im)reader:didDisconnect:>) delegate method to handle this disconnection. You can use this callback as an opportunity to notify the user that something went wrong and that you need internet connectivity to continue. Additionally, you can manually reconnect to the reader when your application re-enters the foreground.

#### Swift

```swift
import StripeTerminal

class ReaderViewController: UIViewController, TapToPayReaderDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Set the reader delegate when connecting to a reader
    }

    // ...



    func reader(_ reader: Reader, didDisconnect reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }
}
```

#### Automatically attempt reconnection

Implement the auto reconnect methods in the `SCPTapToPayReaderDelegate`. You must then pass the `SCPTapToPayReaderDelegate` to your `SCPTapToPayConnectionConfiguration`.

#### Swift

```swift
let connectionConfig = try TapToPayConnectionConfigurationBuilder(locationId: locationId)
  .delegate(yourTapToPayReaderDelegate)
  .build()

Terminal.shared.connectReader(
  reader,
  connectionConfig: connectionConfig,
  completion: connectCompletion
)
```

If you automatically attempt reconnection, the following occurs:

1. When a disconnect occurs, the SDK automatically attempts to reconnect and notifies you through `onReaderReconnectStarted`. Make sure your app announces that the connection was lost and a reconnection is in progress.
   - You can use the `Cancelable` object to stop the reconnection attempt at any time.
1. If the SDK successfully reconnects to the reader, Stripe notifies you through `onReaderReconnectSucceeded`. Make sure your app announces that the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader, Stripe notifies you through both `onReaderReconnectFailed` and `reader:didDisconnect:`. Make sure your app announces that an unexpected disconnect occurred.

#### Swift

```swift
import StripeTerminal

extension ReaderViewController: TapToPayReaderDelegate {
    // MARK: ReconnectionDelegate

    func reader(_ reader: Reader, didStartReaderReconnect cancelable: Cancelable) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    func readerDidSucceedReaderReconnect(_ reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }
    func readerDidFailReaderReconnect(_ reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

# Tap to Pay on Android

> This is a Tap to Pay on Android for when terminal-sdk-platform is android and reader-type is tap-to-pay. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=android&reader-type=tap-to-pay.

Tap to Pay on Android (TTPA) lets users accept in-person contactless payments with [compatible NFC-equipped Android devices](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices). TTPA requires the latest version of the [Terminal Android SDK](https://stripe.dev/stripe-terminal-android/). TTPA supports Visa, Mastercard, and American Express contactless cards and NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay). TTPA is an extension to the Terminal Android SDK and enables payments directly in your Android app.

Follow these steps to connect your app to the Tap to Pay reader on a supported Android device:

1. [Initialize the SDK](https://docs.stripe.com/terminal/payments/connect-reader.md#initialize) for TTPA.
1. [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) using the SDK to confirm device compatibility.
1. [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) using the SDK to accept payments.
1. [Handle unexpected disconnects](https://docs.stripe.com/terminal/payments/connect-reader.md#handling-disconnects) to make sure your user can continue to accept payments if the reader disconnects unexpectedly.

If your application runs on a device that doesn’t meet the [supported device criteria](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices), the SDK returns a `TerminalException` that provides additional context in an `onFailure` callback.

## Initialize the SDK

- [TapToPay (Android)](https://stripe.dev/stripe-terminal-android/cots/com.stripe.stripeterminal.taptopay/-tap-to-pay/-companion/is-in-tap-to-pay-process.html)

TTPA operates in a dedicated process to make transactions more secure. In this process, a second instance of your `Application` is created. To avoid any unexpected errors caused by running your code in this process, you can skip initialization in your `Application` in this process by checking `TapToPay.isInTapToPayProcess()`.

```kotlin
// Substitute with your application name, and remember to keep it the same as your AndroidManifest.xml
class StripeTerminalApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Skip initialization if running in the TTPA process.
        if (TapToPay.isInTapToPayProcess()) return

        // For example, this will be skipped.
        TerminalApplicationDelegate.onCreate(this)
    }
}
```

## Discover readers

- [discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [TapToPayDiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/-tap-to-pay-discovery-configuration/index.html)

Use the `discoverReaders` method to determine hardware support for Tap to Pay on the Android device. `discoverReaders` verifies the following requirements about the Android device:

- Has a functioning, integrated NFC sensor and ARM-based processor
- Runs Android 13 or later
- Has a keystore with hardware support for ECDH ([`FEATURE_HARDWARE_KEYSTORE`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_HARDWARE_KEYSTORE) version must be 100 or later)
- For the non-simulated version of the Tap to Pay reader, the application isn’t debuggable.

Your application _must_ be in the foreground for the Tap to Pay reader service to successfully start.

If your application runs on a device that doesn’t meet the requirements above, the `onFailure` callback returns with a `TerminalException` that contains a [TerminalErrorCode](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-error-code/index.html) and additional context. The failures at this stage aren’t actionable by the end user.

You can’t use the non-simulated, production version of the Tap to Pay reader with debuggable applications or with the device’s developer options enabled. To test your integration with the Tap to Pay on Android reader, set `TapToPayDiscoveryConfiguration.isSimulated` to `true` during reader discovery. You must set this value to `false` in the release version of your application.

#### Kotlin

```kotlin
var discoverCancelable: Cancelable? = null

fun onDiscoverReaders() {
    val isApplicationDebuggable = 0 != applicationInfo.flags and ApplicationInfo.FLAG_DEBUGGABLE
    val config = TapToPayDiscoveryConfiguration(isSimulated = isApplicationDebuggable)

    // Save this cancelable to an instance variable
    discoverCancelable = Terminal.getInstance().discoverReaders(
        config,
        object : DiscoveryListener {
            override fun onUpdateDiscoveredReaders(readers: List<Reader>) {
                // Automatically connect to supported mobile readers
            }
        },
        object : Callback {
            override fun onSuccess() {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
}

override fun onStop() {
    super.onStop()

    // If you're leaving the activity or fragment without selecting a reader,
    // make sure you cancel the discovery process or the SDK will be stuck in
    // a discover readers phase
    discoverCancelable?.cancel(
        object : Callback {
            override fun onSuccess() {
                // Placeholder for handling successful operation
            }

            override fun onFailure(e: TerminalException) {
                // Placeholder for handling exception
            }
        }
    )
}
```

To check if a device meets the Tap to Pay hardware and OS requirements at runtime, use the [Terminal.supportsReadersOfType](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/supports-readers-of-type.html) function. As part of initializing the Terminal SDK, this function requires your end-user to accept permission requests to access the location and bluetooth. This function takes approximately 10 milliseconds to run on most devices.

## Connect to a reader

> In version `5.0.0` of the Android SDK, you can use the `easyConnect` method to combine reader discovery and connection into a single API call to simplify integration. See the [SDK migration guide](https://docs.stripe.com/terminal/references/sdk-migration-guide.md#update-your-reader-connection-usage) for details.

- [connectReader (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/connect-reader.html)
- [TapToPayConnectionConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-connection-configuration/-tap-to-pay-connection-configuration/index.html)

To accept Tap to Pay payments, provide the discovered reader from the previous step to the `connectReader` method.

`connectReader` verifies the Android device meets the following requirements:

- It isn’t rooted and device bootloader is locked and unchanged
- It has a security update installed from the past 12 months
- It uses Google Mobile Services and has the Google Play Store app installed
- It has a stable connection to the internet
- It runs the unmodified manufacturer provided OS
- The application uses Tap to Pay SDK version 2.20.0 or later
- Developer options are disabled for the non-simulated version of the Tap to Pay reader

If your application runs on a device that doesn’t meet the requirements above, the `onFailure` callback returns with a `TerminalException` that contains a [TerminalErrorCode](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-error-code/index.html) and additional context. The end user can take action on some of the [failure reasons](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-terminal-error-code/index.html). For example:

- `STRIPE_API_CONNECTION_ERROR`: The user can connect to a stable internet source.
- `TAP_TO_PAY_UNSUPPORTED_ANDROID_VERSION`: The user can upgrade their operating system, if an update is available from the device manufacturer.

Tap to Pay readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, create and use a `TapToPayConnectionConfiguration` with the `locationId` set to the relevant location ID when connecting.

#### Kotlin

```kotlin
val tapToPayReaderListener = yourTapToPayReaderListener
val autoReconnectOnUnexpectedDisconnect = true

val config = TapToPayConnectionConfiguration(
  ""{{LOCATION_ID}}"",
  autoReconnectOnUnexpectedDisconnect,
  tapToPayReaderListener
),
Terminal.getInstance().connectReader(
  firstReader,
  config,
  object : ReaderCallback {
      override fun onSuccess(reader: Reader) {
          // Placeholder for handling successful operation
      }

      override fun onFailure(e: TerminalException) {
          // Placeholder for handling exception
      }
  }
)
```

## Handle unexpected disconnects

- [TapToPayReaderListener (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.callable/-tap-to-pay-reader-listener/index.html)

Unexpected disconnects might occur between your app and the reader. For example, the Tap to Pay reader might unexpectedly disconnect because:

- Android OS terminates the Tap to Pay reader service due to memory constraints.
- The device loses internet connectivity.

There are two ways you can handle this:

#### Automatically attempt reconnection

You can set `autoReconnectOnUnexpectedDisconnect` to `true` to enable the SDK to automatically attempt reconnection when an unexpected disconnection occurs. The SDK defaults to this behavior if you omit this setting. Optionally, you can also implement `TapToPayReaderListener` for auto reconnect callbacks in your app.

#### Kotlin

```kotlin
val tapToPayReaderListener = yourTapToPayReaderListener
val autoReconnectOnUnexpectedDisconnect = true

Terminal.getInstance().connectReader(
    reader,
    TapToPayConnectionConfiguration(
        ""{{LOCATION_ID}}"",
        autoReconnectOnUnexpectedDisconnect,
        tapToPayReaderListener
    ),
    readerCallback,
)
```

When the SDK automatically attempts reconnection, the following occurs:

1. When a disconnect occurs, the SDK automatically attempts to reconnect and notifies you through `onReaderReconnectStarted`. Make sure your app announces that the connection was lost and a reconnection is in progress.
   - You can use the `Cancelable` object to stop the reconnection attempt at any time.
1. If the SDK successfully reconnects to the reader, Stripe notifies you through `onReaderReconnectSucceeded`. Make sure your app announces that the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader, Stripe notifies you through both `onReaderReconnectFailed` and `TapToPayReaderListener.onDisconnect`. Make sure your app announces that an unexpected disconnect occurred.

#### Kotlin

```kotlin
class CustomTapToPayReaderListener : TapToPayReaderListener {
    override fun onReaderReconnectStarted(reader: Reader, cancelReconnect: Cancelable, reason: DisconnectReason) {
        // 1. Notified at the start of a reconnection attempt
        // Use cancelable to stop reconnection at any time
    }

    override fun onReaderReconnectSucceeded(reader: Reader) {
        // 2. Notified when reader reconnection succeeds
        // App is now connected
    }

    override fun onReaderReconnectFailed(reader: Reader) {
        // 3. Notified when reader reconnection fails
        // App is now disconnected
    }
}
```

#### Handle the disconnect manually

To handle disconnection yourself, you must:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` to disable the default auto reconnection.
1. Implement `TapToPayReaderListener` for its `onDisconnect` callback.

This allows your app to reconnect to the Tap to Pay reader and, when appropriate, notify the user of what went wrong and how they can enable access to Tap to Pay. End users can resolve certain errors, such as internet connectivity issues.

#### Kotlin

```kotlin
class ReaderActivity : AppCompatActivity(), TapToPayReaderListener {
    // ...

    override fun onDisconnect(reason: DisconnectReason) {
        // Consider displaying a UI to notify the user and start rediscovering readers
    }

    // ...
}
```

> If you handle disconnection manually without disabling auto reconnection, it can cause conflicts that break the reader session.

# Tap to Pay on React Native

> This is a Tap to Pay on React Native for when terminal-sdk-platform is react-native and reader-type is tap-to-pay. View the full page at https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=react-native&reader-type=tap-to-pay.

Tap to Pay lets users accept in-person contactless payments with [compatible NFC-equipped Android devices](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=android#supported-devices) or [compatible iPhones](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios#supported-devices). Tap to Pay supports Visa, Mastercard, American Express contactless cards, and NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay). Tap to Pay on iPhone and Android support is included in the native Terminal SDKs and enables payments directly in your mobile app.

> In version `0.0.1-beta.29` of the React Native SDK, you can use the [easyConnect](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#easyconnect) method to combine reader discovery and connection into a single API call to simplify integration.

Follow these steps to connect your app to the Tap to Pay reader on a supported device:

- [Initialize the SDK](https://docs.stripe.com/terminal/payments/connect-reader.md#initialize) for TTPA, if you’re using the SDK on an Android device.
- [Discover readers](https://docs.stripe.com/terminal/payments/connect-reader.md#discover-readers) using the SDK to confirm device compatibility.
- [Connect to a reader](https://docs.stripe.com/terminal/payments/connect-reader.md#connect-reader) using the SDK to accept payments.
- [Handle unexpected disconnects](https://docs.stripe.com/terminal/payments/connect-reader.md#handling-disconnects) to make sure your user can continue to accept payments if the reader disconnects unexpectedly.

## Initialize the SDK

Tap to Pay on Android operates in a dedicated process to make transactions more secure. In this process, a second instance of your `Application` is created. To avoid any unexpected errors caused by running your code on an Android device, you can skip initialization in your `Application` in this process by checking `TapToPay.isInTapToPayProcess()`.

```kotlin
class MainApplication : Application(), ReactApplication {
    override fun onCreate() {
        super.onCreate()

        // Skip initialization if running in the TTPA process.
        if (TapToPay.isInTapToPayProcess()) return

        // For example, this will be skipped.
        TerminalApplicationDelegate.onCreate(this)
    }
}
```

## Discover readers

- [discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders)

Use the `discoverReaders` method to determine hardware support for Tap to Pay on your device.

If your application runs on a device that doesn’t meet the requirements above, the `discoverReaders` method returns an error.

```js
export default function DiscoverReadersScreen() {
  const { discoverReaders, discoveredReaders } =
    useStripeTerminal({
      onUpdateDiscoveredReaders: (readers) => {
        // The `readers` variable will contain an array of all the discovered readers.
      },
    });

  useEffect(() => {
    const { error } = await discoverReaders({
      discoveryMethod: 'tapToPay',
    });
  }, [discoverReaders]);

  return <View />;
}
```

## Connect to a reader

- [connectReader (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#connectreader-1)

To accept Tap to Pay payments, provide the discovered reader from the previous step to the `connectReader` method.

Tap to Pay readers don’t need to be registered in the Dashboard or API ahead of time. Instead, you associate your reader with a [location](https://docs.stripe.com/api/terminal/locations.md) at connection time. To do so, you must pass the relevant location ID to `connectReader`.

When using [destination charges with on_behalf_of](https://docs.stripe.com/terminal/features/connect.md?connect-charge-type=destination) on iPhones, you must also provide the connected account ID.

```js
const { reader, error } = await connectReader({
  discoveryMethod: "tapToPay",
  reader: selectedReader,
  locationId: "{{LOCATION_ID}}",
});

if (error) {
  console.log("connectTapToPayReader error:", error);
  return;
}

console.log("Reader connected successfully", reader);
```

### Account linking and Apple terms and conditions

You see Apple’s Tap to Pay on iPhone Terms and Conditions the first time you connect to the reader. To register with Apple, you must specify a valid Apple ID representing your business before accepting the terms presented by Apple. You only need to perform this once per Stripe account. The account doesn’t need to repeat this process on subsequent connections, including on other mobile devices.

Each connected account must accept the Terms and Conditions when:

- A Connect user creates direct charges
- A Connect user creates a destination charge and specifies an `on_behalf_of` account
  ![Three-step process showing Apple ID sign in, terms acceptance, and success confirmation for Tap to Pay on iPhone](assets/stripe-terminal-ttpoi-account-linking-steps.png)

Link your Apple ID account to accept Tap to Pay payments

Any iPhone can use up to 3 unique Stripe accounts across apps within a rolling 24-hour period when calling `connectReader` for Tap to Pay on iPhone. If additional accounts are used for the device within the same 24-hour period, the `connectReader` method raises an [SCPErrorTapToPayReaderMerchantBlocked](https://stripe.dev/stripe-terminal-ios/docs/Enums/SCPError.html#/c:@E@SCPError@SCPErrorTapToPayReaderMerchantBlocked) error.

Learn more about account linking in the Tap to Pay on iPhone Business Information section of the [Apple Tap to Pay on iPhone FAQ](https://register.apple.com/tap-to-pay-on-iphone/faq.html).

## Handle unexpected disconnects

- [UserCallbacks (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#REPORT_UNEXPECTED_READER_DISCONNECT)

Unexpected disconnects might occur between your app and the reader. For example, the Tap to Pay reader might unexpectedly disconnect because the device loses internet connectivity and when Android OS terminates the Tap to Pay reader service due to memory constraints.

During testing, you can simulate an unexpected disconnect by disabling internet access to your device.

#### Automatically attempt reconnection

You can set `autoReconnectOnUnexpectedDisconnect` to `true` to enable the SDK to automatically attempt reconnection when an unexpected disconnection occurs. The SDK defaults to this behavior if you omit this setting.

```js
const { reader, error } = await connectReader({
  discoveryMethod: "tapToPay",
  reader,
  autoReconnectOnUnexpectedDisconnect: true, // default setting
});

if (error) {
  console.log("connectReader error:", error);
  return;
}

console.log("Reader connected successfully", reader);
```

When the SDK automatically attempts reconnection, the following occurs:

1. The SDK notifies you through `onDidStartReaderReconnect`. Make sure your app announces that the connection was lost and a reconnection is in progress.
   - You can use the `cancelReaderReconnection` method to stop the reconnection attempt at any time.
1. If the SDK successfully reconnects to the reader, Stripe notifies you through `onDidSucceedReaderReconnect`. Make sure your app announces that the connection was restored and to continue normal operations.
1. If the SDK can’t reconnect to the reader, Stripe notifies you through both `onDidFailReaderReconnect` and `onDidDisconnect`. Make sure your app announces that an unexpected disconnect occurred.

```js
const { discoverReaders, connectedReader, discoveredReaders } =
  useStripeTerminal({
    onDidStartReaderReconnect: (disconnectReason) => {
      // 1. Notified at the start of a reconnection attempt
      // Use cancelable to stop reconnection at any time
    },
    onDidSucceedReaderReconnect: () => {
      // 2. Notified when reader reconnection succeeds
      // App is now connected
    },
    onDidFailReaderReconnect: () => {
      // 3. Notified when reader reconnection fails
      // App is now disconnected
    },
  });
```

#### Handle the disconnect manually

To handle disconnection yourself, you must:

1. Set `autoReconnectOnUnexpectedDisconnect` to `false` to disable the default auto reconnection.
1. Implement the `onDidReportUnexpectedReaderDisconnect` callback.

This allows your app to reconnect to the Tap to Pay reader and, when appropriate, notify the user of what went wrong and how they can enable access to Tap to Pay. End users can resolve certain errors, such as internet connectivity issues.

```js
const { discoverReaders, connectedReader, discoveredReaders } =
  useStripeTerminal({
    onDidReportUnexpectedReaderDisconnect: (readers) => {
      // Consider displaying a UI to notify the user and start rediscovering readers
    },
  });
```

> If you handle disconnection manually without disabling auto reconnection, it can cause conflicts that break the reader session.

## Next steps

You’ve connected your application to the reader. Next, [collect your first Stripe Terminal payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md).

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks doesn’t imply any endorsement by BBPOS or Verifone.
