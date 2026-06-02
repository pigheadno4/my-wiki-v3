<!-- Source URL: https://docs.stripe.com/terminal/fleet/monitor -->
<!-- Fetched: 2026-05-01 -->

# Monitor readers

Access real-time status and insights for your Stripe Terminal devices.

You can monitor and track the performance, health, and operational data of your Stripe Terminal devices using the Stripe Dashboard.

## Readers list

Use the [Readers list](https://dashboard.stripe.com/terminal/readers) in the Stripe Dashboard to view all registered readers in your account. You can apply filters to view a subset of your readers. Additionally, you can export this list for use outside of Stripe.

> Connection state (online or offline) is only available for smart readers. Mobile readers connect to your point of sale device rather than directly to Stripe, so Stripe can’t report their connection state.

For platforms or marketplaces using Terminal with Connect, if you use direct charges with readers owned by connected accounts, you must log in as a connected account to view the list of its readers.

## Reader details

The Reader details page displays information about a particular terminal device. To open it, click the reader in the [Readers list](https://dashboard.stripe.com/terminal/readers).

#### Smart Readers

The reader information section includes the following details:

- Connection state (online or offline)
- Reader type
- Reader ID
- Registration date
- P2PE status
- Assigned location
- Battery life
- Last active time
- Currently installed software version

The device connectivity information section includes the following details:

- Ethernet
  - MAC address
  - IP address
  - Connection status if present
- WiFi
  - MAC address
  - IP address
  - SSID
  - Frequency
  - Signal strength
  - Connection status if present
- Bluetooth
  - MAC address

Learn more about network requirements and troubleshooting at [Terminal network requirements](https://docs.stripe.com/terminal/network-requirements.md).

The page also displays a summary of recent payments processed by the reader, including details about successful payments and any errors. You can’t filter or export this summary. You can use the [Transactions](https://docs.stripe.com/dashboard/basics.md#transactions) page to view all your customer payments, including the Terminal location and Terminal reader that processed each transaction. You can filter and export this transactions list.

### Reader events (Public preview)

The reader event log displays the last 30 days of events related to the reader, such as software updates, network disconnections, and boot-ups. Events can take several minutes to appear in the log.

> Your [account level time zone setting](https://dashboard.stripe.com/settings/account) determines the reader event time zone.

The following table describes the reader events that can appear in the log, including their types and sub-types.

| Event type           | Sub-type                 | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General              | Device powered on        | This event is delivered after the reader completes all boot activities. Each event includes the restart reason. Reader software versions earlier than 2.33 are more likely to show an “unknown” reason.                                                                                                                                                                                                                                                                                                                                                                            |
| Network connectivity | Network connected        | This event is delivered when the reader connects to a network. Each event includes the connection type (WiFi or Ethernet) and the SSID for WiFi connections.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Network connectivity | Network disconnected     | This event is delivered when the reader disconnects from a network. Each event includes the connection type. For more information on network troubleshooting, refer to [Terminal network requirements](https://docs.stripe.com/terminal/network-requirements.md).                                                                                                                                                                                                                                                                                                                  |
| Update operation     | Update install succeeded | This event is delivered when the reader successfully installs new software. Each event includes the software and version installed.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Update operation     | Updates deferred         | This event is delivered when one or more software updates are deferred. Each event includes the software, versions deferred, and the reason for the deferral. This might happen due to user action or insufficient battery charge.                                                                                                                                                                                                                                                                                                                                                 |
| Update operation     | Update install failed    | This event is delivered when a software update fails. Each event includes the software and version that failed to install. The system retries the installation during the configured [reboot time window](https://docs.stripe.com/terminal/fleet/reboot-time.md). You can manually trigger a retry by rebooting the device. Before rebooting, make sure that the reader’s battery is sufficiently charged to complete the update. For additional smart reader troubleshooting, see our [support docs](https://support.stripe.com/questions/smart-reader-connectivity-error-codes). |

#### Mobile Readers

> Connection state (online or offline) isn’t available for mobile readers because they connect to your point of sale device rather than directly to Stripe. To check whether a mobile reader is connected, refer to your point of sale application.

The reader information section contains the following details:

- Reader type
- Reader ID
- Registration date
- Assigned location
- Last active time
- Currently installed software version

The page also displays a summary of recent payments processed by the reader, including details about successful payments and any errors. You can’t filter or export this summary. You can use the [Transactions](https://docs.stripe.com/dashboard/basics.md#transactions) page to view all your customer payments, including the Terminal location and Terminal reader that processed each transaction. You can filter and export this transactions list.
