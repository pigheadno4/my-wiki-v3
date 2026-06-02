---
title: Magnes-Android Ver. 5.5.1 Release Notes
slug: /limited-release/magnes/release-notes/android/5-5-1/
createTime: "2024-12-16T15:18:40.842Z"
updateTime: "2025-03-10T19:10:57.781Z"
---

# Magnes-Android Ver. 5.5.1 Release Notes

In this release note, we'd like to inform you of the recommended upgrade to
Magnes 5.5.1 Android SDK related to the policies implemented at the Google
Play Store that require explicit consent from the user for any personal and
sensitive data collected by third-party SDKs.

Currently, the Magnes SDK collects location data, which is considered personal
and sensitive. This collection relies on parent app permissions and does not
request permission explicitly.

To comply with the data collection policy of Google Play Store, PayPal has
released the Magnes Android SDK version 5.5.1 which will fetch location data
only if user consent has been shared by the merchant app. The steps to
implement this consent sharing logic are outlined under the "steps to upgrade"
section in the release FAQs.

It is highly recommended that you upgrade to Magnes 5.5.1 SDK or there will be
a risk of your new or updated app getting rejected by Google Play Store.
Please note, the decision of rejection or acceptance will be at the full
discretion of Google Play Store.

.css-cghe3x-button_base-text_button_lg-btn_full_width-size_sm-text_button_sm span {
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
}[Log in](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com/limited-release/magnes/release-notes/android/5-5-1/&intent=developer)[Download Magnes 5.5.1](https://paypalobjects.com/magnes-repository/Android/android-magnessdk-5.5.1.zip)Password: mLhZzwNwJoQz Checksum(SHA-512):
117d252575564f1a1793a120c0b86c6fe1a7c855fc1fcdb3a64c4bf74302e5aedeb630caeb9e94cc6976679c22cc66a9d9bdbc44f5fc2909d95c4f6f56724b27

### Release FAQs

#### Q: Why is this upgrade required?

Merchants are having their apps rejected from the Google Play store due to
"Violation of User Data, Permissions and APIs that Access Sensitive
Information Policies" within the Braintree/PayPal data collector libraries. We
have learned that the location data collection within the Magnes SDK was
non-compliant, and it has been resolved now.

#### Q: When will Google start the location policy enforcement for third-party

    SDKs?

Google's policy is not new and is already enforced for all merchants. All
merchants are recommended to file an appeal with the Play Store and request an
extension to allow time to upgrade so that there is no impact to the app. In
your appeal, please state that you are requesting an extension while
implementing a fix in the underlying Braintree/PayPal SDK with location
access. After submitting the appeal, please reach out to Braintree Support
with the package ID of your appeal request.

#### Q: What happens if the upgrade is not completed?

There will be a risk of your new or updated app getting rejected by the Google
Play store. Please note that the decision to accept or reject your updated app
will be at the full discretion of Google Play Store.

#### Q: Are there any changes on the data fields being collected in Magnes 5.5.1?

Magnes 5.5.1 SDK will fetch location details only if consent has been given.
Below are the field details:

- latitude
- longitude
- location_area_code(gsm)
- cell_id(gsm)
- base_station_id(cdma)
- cdma_network_id(cdma)
- cdma_system_id(cdma)
- bssid
- ssid
- bssid_array

#### Q: What is the recommended way to get additional support on this upgrade?

Please work with your Technical Account Manager from PayPal if that option is
available.

If you don't have an assigned Technical Account Manager or if you need any
technical integration support, please visit [www.paypal-support.com](http://www.paypal-support.com) and submit
a support ticket.

#### Q: What are the steps required to upgrade to Magnes 5.5.1?

- Download the latest .aar file from the Magnet 5.5.1 repository.
- In your project workspace, locate the existing .aar and file and replace it
  with the latest 5.5.1 version.

#### Q: What are the code changes required after updating to Magnes 5.5.1?

While configuring MagnesSettings Builder, make sure to pass the location
consent value to the SetHasUserLocationConsent API. By default this value is
set to false.

For those merchants who required advanced fraud protection for using location,
users need to explicitly provide consent to share their location.

MagnesSettings.Builder magnesSettings = new MagnesSettings.Builder(@NonNull Context context)
...
.setHasUserLocationConsent(boolean hasUserLocationConsent)
...
.build();
MagnesSDK.getInstance().setUp(magnesSettings);
