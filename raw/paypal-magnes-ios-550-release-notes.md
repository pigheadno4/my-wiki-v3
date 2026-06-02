---
title: Magnes-iOS Ver. 5.5.0 Release Notes
slug: /limited-release/magnes/release-notes/ios/5-5-0/
createTime: "2024-08-15T07:16:41.623Z"
updateTime: "2025-03-10T19:15:26.199Z"
---

# Magnes-iOS Ver. 5.5.0 Release Notes

In this release note, we'd like to inform you of the recommended upgrade to
Magnes 5.5.0 iOS SDK related to the upcoming Apple Privacy Manifest
enforcement for iOS app third-party SDKs starting May 1, 2024.

At WWDC23 (Worldwide Developers Conference 2023), Apple introduced the Privacy
Manifest which requires third-party SDKs to provide a privacy manifest that
describes the data collected within the SDKs and provide a developer code
signature to ensure the integrity of the iOS app software supply chain.

To comply with this new Apple Privacy Manifest requirement, PayPal has
released the Magnes iOS SDK version 5.5.0 which packages all required privacy
manifest changes and includes a developer code signature.

It is highly recommended that you upgrade to Magnes 5.5.0 iOS SDK by May 1,
2024, to eliminate the risk of your new or updated app being rejected by Apple
App Store Connect. Please note the decision of rejection or acceptance will be
at the full discretion of Apple / App Store Connect.

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
}](https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com/limited-release/magnes/release-notes/ios/5-5-0/&intent=developer)

[Download Magnes 5.5.0](https://www.paypalobjects.com/magnes-repository/iOS/PPRiskMagnes_5.5.0_XCF.zip)Password: j5FAn5G5rsXD Checksum(SHA-512):
f4c0842dd9ad17fe0c1ead76d0fc3c4fc5189be224322203db42bfcb3549ac4ef93a28649e8c6ef8c6f3fd4074432b860fbd0f6ba24e583a41d5d3230c9e87d7

### Release FAQs

#### Q: Why is this upgrade required?

A: At WWDC23 (Worldwide Developers Conference 2023), Apple introduced the
concept of Privacy Manifest which requires third-party SDKs to provide privacy
manifest that describes the data collected within the SDKs and provide
developer code signature to ensure the integrity of iOS app software supply
chain.

To comply with this new Apple Privacy Manifest requirement, PayPal has
released the Magnes SDK version 5.5.0 which includes all required privacy
manifest changes and includes a developer code signature.

#### Q: When will Apple start enforcing the Privacy Manifest and Signature

    requirements for third-party SDKs?

A: The official enforcement starting date is May 1, 2024. However, starting
from March 13, 2024, developers will be notified by email when uploading a new
or updated app to Apple App Store Connect if privacy manifest is missing from
third-party SDK.

More details regarding the official communication from Apple can be found
here: [https://developer.apple.com/news/?id=3d8a9yyh](https://developer.apple.com/news/?id=3d8a9yyh)

#### Q: What happens if the upgrade is not completed by May 1, 2024?

A: There will be a risk of your new or updated app getting rejected by Apple
App Store Connect. Please note the decision of rejection or acceptance will be
at full discretion of Apple / App Store Connect.

#### Q: Where to download the latest Magnes 5.5.0 version SDK?

A: You can download it here:

#### Q: Are there any changes on the data fields being collected in Magnes 5.5.0?

A: Yes, the following fields are being deprecated in Magnes 5.5.0:

- Device Total Space

- Device Available Free Space

- System Uptime

#### Q: What’s recommended way to get additional support on this upgrade?

A: Please work with your Technical Account Manager from PayPal if that option
is available.

If you don’t have an assigned Technical Account Manager, If you need any
technical integration support, please visit [www.paypal-support.com](http://www.paypal-support.com) and submit
a support ticket.

#### Q: My team's existing integration is via Java script SDK, should I need to

    upgrade?

A: If you don't have an active magnes integration via binary framework, no
need to update.

#### Q: What are the steps required to upgrade to Magnes 5.5.0?

Step 1: Download the PPRiskMagnes.xcframework file from the download link in
above section (Download link is visible only if the user has logged in).

Step 2: Identify the existing PPRiskMagnes.xcframework or
PPRiskMagnes.framework from your project workspace and replace it with latest
5.5.0 version.
