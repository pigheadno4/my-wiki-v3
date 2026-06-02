---
title: Sample Magnes Payloads
slug: /limited-release/magnes/reference/sample-payloads/
createTime: "2024-08-15T07:26:36.421Z"
updateTime: "2024-09-27T22:26:20.555Z"
---

# Sample Magnes Payloads

This page provides sample payloads as an aid in interpreting the results of
your Magnes app. The samples include one payload each of Android and iOS data,
listed by parameter names in alphabetical order.

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
}](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com/limited-release/magnes/reference/sample-payloads/&intent=developer)

## Android sample payload

{
"android_id": "e54d2783a24c5a93",
"app_first_install_time": 1485391650466,
"app_guid": "16dd2f5f-3496-4953-8021-00b45950bdeb",
"app_id": "com.paypal.android.lib.riskcomponentsample",
"app_last_update_time": 1486085153926,
"app_version": "1.0",
"bssid": "6c:f3:7f:b9:1e:90",
"bssid_array": ["6c:f3:7f:b9:1e:90","6c:f3:7f:b9:1e:92"],
"cdma_network_id": -1,
"cdma_system_id": -1,
"cell_id": 21181955,
"comp_version": "3.5.7.release",
"conf_url": "https://www.paypalobjects.com/webstatic/risk/dyson_config_android_v3.json",
"conf_version": "3.0",
"conn_type": "MOBILE",
"dc_id": "50fd71cdaeb32cfc7421703646d30489",
"device_id": "352530080310824",
"device_model": "Pixel XL",
"device_name": "marlin",
"device_uptime": 798843490,
"ds": false,
"gsf_id": "3d6eefb279e2e84a",
"ip_addresses": ["192.0.0.4","fe80::c8ec:37ff:fe6b:6141%dummy0","2607:fb90:a74b:2d64:ba05:3877:ad93:4bdd","fe80::ba05:3877:ad93:4bdd%rmnet_data0","fe80::5df9:65ee:ffa6:96ce %rmnet_data7","fe80::a918:e8bd:ad79:d8cc%r_rmnet_data0"],
"ip_addrs": "192.0.0.4",
"is_emulator": false,
"is_rooted": false,
"known_apps": ["com.my-org.mobile/com.my-org.mobile.activities. my-org"],
"linker_id": "f76d48e7-63f8-4be9-bd4d-08edaa4d59b3",
"locale_country": "US",
"locale_lang": "en",
"location": {"lat":37.3760446,"lng":-121.9216664,"acc":19.872,"timestamp":1486085186851},
"location_area_code": "14940",
"location_auth_status": "unknown",
"mac_addrs": "02:00:00:00:00:00",
"network_operator": "310260",
"notif_token": "test notif token",
"os_type": "Android",
"os_version": "7.1.1",
"pairing_id": "1d7706b1f3ba46bdbe46832aa99852cf",
"payload_type": "full",
"phone_type": "gsm",
"pm": "fe3e",
"risk_comp_session_id": "1fe8a38f-c4ad-4cbe-84bb-e340d953160b",
"roaming": false,
"serial_number": "HT68J0207231",
"sim_operator_name": "T-Mobile",
"sim_serial_number": "8901260533554717229",
"sms_enabled": true,
"source_app": 0,
"source_app_version": "1.9.9",
"ssid": "PayPalGuest",
"subscriber_id": "310260535471755",
"timestamp": 1486085312082,
"total_storage_space": 26109874176,
"tz": "-28800000",
"tz_name": "Pacific Standard Time",
"vpn_setting": "tun0"
}## iOS sample payload
{
"app_guid": "b286802c-de9d-4c30-8ecb-42c2d2dfe3e4",
"app_id": "com.paypal.Dyson",
"app_version": "1.0",
"c": "48",
"cloud_identifier": "7027fff5-fde0-44ab-8b25-6cb4a928de8f",
"comp_version": "3.5.7",
"conf_url": "https:\/\/www.paypalobjects.com\/webstatic\/risk\/dyson_config_ios_v4.json",
"conf_version": "4.0",
"conn_type": "wifi",
"dc_id": "11e7d85632c3142b07ffeee4516629a3",
"device_model": "Simulator",
"device_name": "Eddie's Papa",
"ds": false,
"email_configured": false,
"ip_addresses": ["::1","127.0.0.1","fe80::1","fe80::c6b3:1ff:febd:30c9","10.225.90.250", "fe80::c034:cdff:fe5c:13e3"],
"ip_addrs": "10.225.90.250",
"is_emulator": true,
"is_rooted": false,
"known_apps": ["com.my-org.mobile/com.my-org.mobile.activities.my-org"],
"linker_id": "a0cefbe4-b445-47d1-a964-bd39e8c0ea8d",
"local_identifier": "0579a19c-f302-4242-a481-a2f49689a6ff",
"locale_country": "US",
"locale_lang": "en",
"location": {"lng":-122.03076342,"lat":37.33123666,"timestamp":1486084281488,"acc":30},
"location_auth_status": "denied",
"notif_token": "null",
"os_type": "iOS",
"os_version": "10.1",
"pairing_id": "b2d32ea3df86477da25523d1cc19d37b",
"payload_type": "full",
"pin_lock_last_timestamp": null,
"pm": "338723cb",
"risk_comp_session_id": "8fb8114e-2079-436a-bec9-583bffcb108c",
"sms_enabled": false,
"source_app": 10,
"source_app_version": "1.0",
"timestamp": 1486084490678,
"total_storage_space": 499082485760,
"tz": "-28800000",
"tz_name": "America\/Los_Angeles",
"vendor_identifier": "20C722AF-BDC7-4107-8C07-5FA1875AA7F1",
"vpn_setting": "tun0"
}
