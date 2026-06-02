---
title: Magnes Payload Parameters
slug: /limited-release/magnes/reference/payload-parameters/
createTime: "2024-08-15T07:33:13.441Z"
updateTime: "2024-09-27T22:10:56.163Z"
---

# Magnes Payload Parameters

Please log in to view the content

.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm {
position: relative;
border-radius: 1000px;
color: #ffffff;
cursor: pointer;
display: inline-block;
min-width: 6rem;
text-align: center;
-webkit-text-decoration: none;
text-decoration: none;
-webkit-transition: color 0.2s ease, background-color 0.2s ease,
border-color 0.2s ease;
transition: color 0.2s ease, background-color 0.2s ease,
border-color 0.2s ease;
border: 0.125rem solid #003087;
color: #ffffff;
font-family: PayPalOpen-Bold, "Helvetica Neue", Arial, sans-serif;
font-size: 1.125rem;
line-height: 1.5rem;
font-weight: 400;
background-color: #003087;
padding: 0.625rem 1.875rem;
color: #ffffff;
font-family: PayPalOpen-Bold, "Helvetica Neue", Arial, sans-serif;
font-size: 0.875rem;
line-height: 1.25rem;
font-weight: 400;
min-width: 3.75rem;
padding: 0.25rem 0.875rem;
}
@media screen and (max-width: 752px) {
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm {
font-size: min(1.125rem, 36px);
line-height: min(1.5rem, 48px);
}
}
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:hover,
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:active,
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:visited {
color: #ffffff;
}
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:hover {
-webkit-text-decoration: none;
text-decoration: none;
background-color: #0070e0;
border-color: #0070e0;
}
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:active {
outline: none;
background-color: #001c64;
border-color: #001c64;
}
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm:focus {
outline: none;
box-shadow: 0 0 0 0.125rem #ffffff;
outline-offset: 0.125rem;
outline: 0.125rem solid #097ff5;
}
@media (max-width: 47rem) {
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm {
width: 100%;
}
}
@media screen and (max-width: 752px) {
.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm {
font-size: min(0.875rem, 28px);
line-height: min(1.25rem, 40px);
}
} [Log in.css-1bj9kom-affordance {
-webkit-margin-start: 0.5rem;
margin-inline-start: 0.5rem;
-webkit-margin-end: 0;
margin-inline-end: 0;
vertical-align: top;
position: relative;
pointer-events: none;
}](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com/limited-release/magnes/reference/payload-parameters/&intent=developer)

| Parameter name              | Type    | Description                                                                                                                                                                                                                                                                                                      | Android             | iOS                 |     |
| --------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | --- |
| `android_id`                | String  | 64-bit number (as a hex String) that the OS randomly generates when the user first sets up the device. The ID changes when factory settings of the device are restored. **Note**: When a device has multiple users, each user appears as a separate device. This results in a unique `android_id` for each user. | Required            | Not available       |     |
| `app_first_install_time`    | Long    | The timestamp when the app was first installed                                                                                                                                                                                                                                                                   | Required            | Not available       |     |
| `app_guid`                  | String  | A unique installation identifier of the app. If the app is re-installed, a new `app_guid` is generated. Maximum length: 36 characters.                                                                                                                                                                           | Required            | Required            |     |
| `app_id`                    | String  | The identifier of the app using the Magnes Hybrid source code (host app)                                                                                                                                                                                                                                         | Required            | Required            |     |
| `app_last_update_time`      | Long    | The version number of the hosting app                                                                                                                                                                                                                                                                            | Required            | Not available       |     |
| `app_version`               | String  | The version number of the hosting app                                                                                                                                                                                                                                                                            | Required            | Required            |     |
| `base_station_id`           | String  | The base station identification number for CDMA (Code Division Multiple Access) phones. This returns `-1` for an unknown base station.                                                                                                                                                                           | Optional            | Not available       |     |
| `bssid`                     | String  | Base Service Set Identifier (MAC address) of the WiFi AP (access point). This is available only when the device is connected to WiFi.                                                                                                                                                                            | Optional            | Optional            |     |
| `bssid_arr`                 | Array   | The top two strength `bssid`s (MAC of AP). One of them is the one to which the device is currently connected. Permission: `ACCESS_FINE_LOCATION` or `ACCESS_COARSE_LOCATION`                                                                                                                                     | Required            | Not available       |     |
| `c`                         | String  | A counter for the number of payloads that the current device has submitted.                                                                                                                                                                                                                                      | Required            | Required            |     |
| `cdma_network_id`           | INT     | The CDMA system identification as a purely numeric value. This returns `-1` if unknown.                                                                                                                                                                                                                          | Optional            | Not available       |     |
| `cdma_system_id`            | INT     | The CDMA system identification as a purely numeric value. This returns `-1` if unknown.                                                                                                                                                                                                                          | Optional            | Not available       |     |
| `cell_id`                   | String  | The current cell site identifier for GSM phones                                                                                                                                                                                                                                                                  | Optional            | Not available       |     |
| `cloud_identifier`          | String  | The cloud identifier stored in a syncable iCloud keychain entity.                                                                                                                                                                                                                                                | Not available       | Required            |     |
| `comp_version`              | String  | The Magnes Hybrid version number, hardcoded as `3.6.0`                                                                                                                                                                                                                                                           | Required            | Required            |     |
| `conf_url`                  | String  | Android: `https://www.paypalobjects.com/webstatic/risk/dyson_config_android_v3.json`, iOS: `https://www.paypalobjects.com/webstatic/risk/dyson_config_ios_v4.json`                                                                                                                                               | Required            | Required            |     |
| `conf_version`              | String  | Android: 3.0 iOS: 4.0                                                                                                                                                                                                                                                                                            | Required            | Required            |     |
| `conn_type`                 | String  | The current network connection type as a human-readable string. Examples: Android `WIFI` or `MOBILE` iOS `WiFi` or `Cellular`                                                                                                                                                                                    | Required            | Required            |     |
| `dc_id`                     | String  | A checksum based on the `app_guid` and `timestamp`.                                                                                                                                                                                                                                                              | Required            | Required            |     |
| `device_id`                 | String  | The device ID as reported by the OS. GSM device: `IMEI`, CDMA device: `MEID` or `ESN`, No device: null                                                                                                                                                                                                           | Permission required | Not available       |     |
| `device_model`              | String  | The phone model.                                                                                                                                                                                                                                                                                                 | Required            | Required            |     |
| `device_name`               | String  | The user-defined name of the device.                                                                                                                                                                                                                                                                             | Required            | Required            |     |
| `device_uptime`             | String  | The length of time (in milliseconds) since the most recent reboot of the operating system, not counting time spent in deep sleep.                                                                                                                                                                                | Required            | Not available       |     |
| `ds`                        | String  | Returns `true` if the device is set with Daylight Saving Time (DST) enabled; `false` otherwise.                                                                                                                                                                                                                  | Required            | Required            |     |
| `email_configured`          | Boolean | Returns `true` if the device has been configured with an email account; `false` otherwise.                                                                                                                                                                                                                       | Not available       | Required            |     |
| `gsf_id`                    | String  | 16-digit hex string randomly generated on the device. **Note:** If the device is reset to factory settings, it is assigned a new ID.                                                                                                                                                                             | Required            | Not available       |     |
| `ip_addresses`              | Array   | An array that contains the addresses of all network interfaces found on the device. If available, IPV6 would be included.                                                                                                                                                                                        | Required            | Required            |     |
| `ip_addrs`                  | String  | The device IP address                                                                                                                                                                                                                                                                                            | Required            | Required            |     |
| `is_emulator`               | Boolean | Returns `true` if the device is suspected of being an emulator; `false` otherwise.                                                                                                                                                                                                                               | Required            | Required            |     |
| `is_rooted`                 | Boolean | Returns `true` if the device is suspected of being rooted (Android) or jail-broken (iOS); `false` otherwise.                                                                                                                                                                                                     | Required            | Required            |     |
| `known_apps`                | String  | List of apps that are currently installed on the device (from an enumerated check list).                                                                                                                                                                                                                         | Required            | Not available       |     |
| `linker_id`                 | String  | A persistent ID that Magnes Hybrid assigns to the device. All Android or iOS apps on the same device share the same ID.                                                                                                                                                                                          | Permission required | Required            |     |
| `local_identifier`          | String  | Local identifier stored in a file marked as `DoNotBackup` and `DoNotSync`                                                                                                                                                                                                                                        | Not available       | Required            |     |
| `locale_country`            | String  | The 2-character country code (ISO 3166-1) for the locale, or an empty string if none is defined.                                                                                                                                                                                                                 | Required            | Required            |     |
| `locale_lang`               | String  | The 2-character language code (ISO 639-1) for the locale, or an empty string if none is defined.                                                                                                                                                                                                                 | Required            | Required            |     |
| `location`                  | Object  | The location of the device. Contains: Latitude (LAT), Longitude (LNG), Accuracy (ACC), and Time stamp (Timestamp). **Note:** This is available only if the user has granted sufficient permission related to location.                                                                                           | Permission required | Permission required |     |
| `location_area_code`        | String  | The GSM location area code of the current cell site, or `-1` if unknown.                                                                                                                                                                                                                                         | Required            | Not available       |     |
| `location_auth_status`      | String  | This returns the status if the app has access to the location.                                                                                                                                                                                                                                                   | Not available       | Required            |     |
| `mac_addrs`                 | String  | The MAC address of the device                                                                                                                                                                                                                                                                                    | Required            | Not available       |     |
| `network_operator`          | String  | The numeric name (mobile country code plus mobile network code) of the current registered operator. **Note:** This is only available if the user is registered to a network. The result may be unreliable on CDMA networks.                                                                                      | Optional            | Not available       |     |
| `notif_token`               | String  | Android: C2DM (Cloud to Device Messaging) registration ID, OS: APNS token                                                                                                                                                                                                                                        | Required            | Required            |     |
| `os_type`                   | String  | The OS that is running at the time of data collection.                                                                                                                                                                                                                                                           | Required            | Required            |     |
| `os_version`                | String  | The currently installed version of the OS as a user-visible version string.                                                                                                                                                                                                                                      | Required            | Required            |     |
| `payload_type`              | String  | The payload type is either `Full` or `Incremental`. **Note:** All new instances are `Full`, but the parameter supports the legacy `Incremental`.                                                                                                                                                                 | Required            | Required            |     |
| `PayPal-Client-Metadata_Id` | String  | A unique 32-character string that pairs the Magnes payload with the payment context.                                                                                                                                                                                                                             | Required            | Required            |     |
| `phone_type`                | String  | The device radio type used to transmit voice calls: `GSM`, `CDMA`, or `None`                                                                                                                                                                                                                                     | Required            | Not available       |     |
| `pin_lock_last_timestamp`   | Long    | The most recent time that a PIN was used to lock the device.                                                                                                                                                                                                                                                     | Not available       | Required            |     |
| `proxy_setting`             | String  | Proxy service information. **Note:** Available only when connected to a proxy service `(host=slc-enc-02, port=80, type=kCFProxyTypeHTTP)`                                                                                                                                                                        | Optional            | Optional            |     |
| `risk_comp_session_id`      | String  | The Magnes Hybrid session ID. A new session ID is generated each time a full payload update is created and sent.                                                                                                                                                                                                 | Required            | Required            |     |
| `roaming`                   | Boolean | Returns `true` if the phone is currently in roaming condition; `false` otherwise.                                                                                                                                                                                                                                | Required            | Not available       |     |
| `serial_number`             | String  | The Android serial number (available for Android 2.3 and later versions). **Note:** It is available via `androidos.Build.SERIAL`. Devices without telephony are required to report a unique device ID.                                                                                                           | Required            | Not available       |     |
| `sim_operator_name`         | String  | The SPN (Service Provider Name). **Note:** This is available only when the SIM is inserted in the device.                                                                                                                                                                                                        | Optional            | Not available       |     |
| `sim_serial_number`         | String  | The SIM serial number. **Note:** This is available only when the SIM is inserted in the device. Returns null if none is available.                                                                                                                                                                               | Optional            | Not available       |     |
| `sms_enabled`               | Boolean | Returns `true` if text messaging is enabled on the device; `false` otherwise.                                                                                                                                                                                                                                    | Required            | Required            |     |
| `source_app`                | INT     | A number enumerating the source of the host app. Always `0` for this type of integration.                                                                                                                                                                                                                        | Required            | Required            |     |
| `source_app_version`        | String  | The source app version; for this type of integration, it is the host `app_version`.                                                                                                                                                                                                                              | Required            | Required            |     |
| `ssid`                      | String  | The SSID; the network name of the WiFi network. **Note:** This is available only when connected to a WiFi network. This may return `` if no network is connected.                                                                                                                                                | Optional            | Optional            |     |
| `subscriber_id`             | String  | The unique subscriber ID. It is the IMSI for a GSM phone. This returns `null` if unavailable.                                                                                                                                                                                                                    | Required            | Not available       |     |
| `timestamp`                 | Long    | The 13-digit Unix timestamp of payload creation time (in milliseconds)                                                                                                                                                                                                                                           | Required            | Required            |     |
| `total_storage_space`       | Long    | The total storage in bytes available on the device.                                                                                                                                                                                                                                                              | Required            | Required            |     |
| `tz`                        | String  | Time zone offset in milliseconds. Daylight Saving Time (DST) is applied if appropriate.                                                                                                                                                                                                                          | Required            | Required            |     |
| `tz_name`                   | String  | The human-readable name of the time zone.                                                                                                                                                                                                                                                                        | Required            | Required            |     |
| `vendor_identifier`         | String  | Identifier that is visible and shared across apps from the same vendor (Team ID). The identifier is deleted when the last app from the vendor is removed. A user cannot delete or change the identifier in any other way. **Note:** It is invisible to other apps that do not belong to the same vendor.         | Not available       | Required            |     |
| `VPN_setting`               | String  | The VPN interface name. **Note:** This is available only when connected to a VPN service (TAP, TUN, or POP)                                                                                                                                                                                                      | Optional            | Optional            |     |
