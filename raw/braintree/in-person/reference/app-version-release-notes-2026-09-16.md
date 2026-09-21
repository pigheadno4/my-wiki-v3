<!-- Source URL: https://developer.paypal.com/braintree/in-person/reference/app-version-release-notes -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Firmware Version Release Notes
slug: /in-person/reference/app-version-release-notes/
createTime: '2024-11-20T19:05:10.303Z'
updateTime: '2025-05-07T14:09:09.022Z'
---



# Firmware Version Release Notes

Provides public release notes for both sandbox and production versions of the Braintree Payment Application.


**IMPORTANT**
 The SSL certificates for the PayPal Braintree Payment Application are set to expire on January 1st 2026. This will impact card readers in the field which are running older versions of the payment application. To reduce the impact, upgrade to the minimum required version of 6.0.1. Starting with that version, all new releases of the payment application will contain new valid SSL certificates.

If you do not upgrade your card readers to the minimum version of 6.0.1 by that date, 100% of your card reader interactions will fail.

 

**NOTE**
Production releases occur 4 weeks after a version is made available in Sandbox


## Version 6.0.1 - Released on 2025-05-07


#### New


- Added new SSL certificates




#### Fixed




- V400m: Improved stability of ethernet connectivity when using the base




## Version 5.5.0 - Released on 2024-09-12


#### New


- V400m: New reader hardware support for the [V400m device](/braintree/in-person/hardware/verifone-v400m/)


- V400m: New [receipt printing API](/braintree/in-person/guides/receipt-printing-api/) for V400m device built-in receipt printer


- Added new [API error codes](/braintree/in-person/guides/graphql-error-handling/#table-1-error-code-explanations) for receipt printing API


- Transaction level [partial authorization](/braintree/in-person/guides/making-a-transaction/#partial-authorizations) API flag gives the API caller full control over partial authorization enablement


- Added support for the [payment initiator](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#using-estimated-auth-pre-auth) API flag to trigger estimated authorizations (pre-authorizations)


- SAF: Partial authorization is now supported for offline transactions


- RMS: The new [Reader Management System](/braintree/in-person/post-launch-activities/reader-management-system-rms-available-in-beta-only/) is now available in beta




#### Fixed


- General platform stability and performance improvements




#### Behavior Change


- E285: When the E285 device is charging the screen will be dimmed but not put into sleep mode




## Version 5.4.0 - Released on 2024-04-11

**New**


- New API call for [Request Multiple Choice Prompt](/braintree/in-person/guides/custom-prompts/#request-multiple-choice-prompt) which helps you to collect customer input for things such as donations, satisfaction surveys, tipping, and more on the reader display


- All virtual buttons on the reader now change color to provide a visual indication that they have been tapped


- Performance improvements




#### Behavior Change


- SAF: The cardholderName field in the [offline node query](/braintree/in-person/guides/offline-transactions/#checking-the-status-of-a-charge-or-refund) is now formatted as first_name last_name where previously it was last_name/first_name




## Version 5.3.0 - Released on 2024-01-04


#### New


- We have done a UI refresh of all screens (fonts, font sizes, boldened text, headers, and color scheme)


- SAF: You can now retrieve the bin, brandCode, and applicationIdentifier for offline transactions


- SAF: You can now pass the channel API variable for offline transactions


- We have added a virtual keyboard for WiFi password entry on the M400 device


- We have enabled the keyboard backlight on the M400 and P400 for better button visibility in dark lighting




#### Fixed


- We have fixed a bug where a white screen would be displayed on the reader display during configuration download if the screensaver image file was corrupted


- We have fixed a bug where the reader would not make a beep sound when selecting buttons while using the [requestConfirmationPrompt](/braintree/in-person/guides/custom-prompts/#request-confirmation-prompt)


- The reader will now remember the previously connected WiFi network even when the network is not available (previously you would be prompted to reconnect to a new network)




#### Behavior Change


- As of firmware version 5.3.0, we have incorporated an updated privacy statement in accordance with California CPRA regulation which shows up on the reader display upon a charge or auth request as: “ **Please review the PayPal Privacy Statement at** [**PayPal.com/privacy**](http://paypal.com/privacy) **.** "




## Version 5.2.2 - Released on 2023-08-30


#### Behavior Change


- SAF: The Magstripe reader interface is now disabled for all offline transactions




## Version 5.2.0 - Released on 2023-06-27


#### New


- New API call for [Request Text Prompt](/braintree/in-person/guides/custom-prompts/#request-text-prompt), which helps you to collect alphanumeric and numeric customer inputs (ex: phone number, email address, SSN, etc...) on the reader display


- New API call for [Request Amount Prompt](/braintree/in-person/guides/custom-prompts/#request-amount-prompt), which helps you to collect custom amount inputs (ex: donation, tips, etc...) from your customer on the reader display


- New API call for [Request Card Data Collection](/braintree/in-person/guides/card-data-collection/), which helps you to collect magstripe track data for non-PCI cards (gift cards, PLCC cards, etc...) swiped on the reader




#### Fixed


- Custom Prompts: waitForNextRequest now supported for [Request Signature Prompt](/braintree/in-person/guides/custom-prompts/#request-signature-prompt) and [Request Confirmation Prompt](/braintree/in-person/guides/custom-prompts/#request-confirmation-prompt)


- Custom Prompts: displayTimeout now supported for [Request Signature Prompt](/braintree/in-person/guides/custom-prompts/#request-signature-prompt) and [Request Confirmation Prompt](/braintree/in-person/guides/custom-prompts/#request-confirmation-prompt)


- Display Information: title now supported for [Request Text Display](/braintree/in-person/guides/display-information/#request-text-display)


- Display Information: alignment now supported for [Request Text Display](/braintree/in-person/guides/display-information/#request-text-display)




#### Behavior Change


- When using [Request Text Display](/braintree/in-person/guides/display-information/#request-text-display), if a title is NOT passed in the request the text will no longer be vertically centered. To maintain current behavior without passing a title simply pad your text with line breaks ("\n")




## Version 5.1.0 - Released on 2023-06-16

**NOTE**
Version 5.1.0 is available only in the sandbox environment for testing and integration purposes. For the production release of these features, merchants will need to update to the [5.2.0 release](/braintree/in-person/reference/app-version-release-notes/#version510).


#### New


- New API call for [Request Authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/), which supports separate auth from capture, incremental auth, partial and full capture


- SAF: general enhancements to store & forward feature


- SAF: Request Charge now supports vaulting w/charge


- PIN bypass is now supported by pressing the green keypad button during the PIN prompt


- Admin menu: [Network Diagnostics feature](/braintree/in-person/post-launch-activities/troubleshooting/#have-network-connectivity-issues) which allows for a user to trigger a diagnostics test of the network connection locally from the device admin menu by pressing " **Run Connection Test** "




#### Fixed


- Reader firmware updates are no longer allowed when offline transactions are cached in reader memory until successfully uploaded to the Braintree platform


- If a reader becomes unresponsive, it will automatically revert back to the pairing screen upon the next reboot cycle


- Admin menu: The red and yellow on the keypad now work to "go back" during admin menu navigation


- M400: On-screen button issue is now resolved with overall improved on-screen responsiveness




#### Known Issues (to be resolved)


- When performing [error handling simulations](/braintree/in-person/guides/testing-your-integration/) ($2000-3000, or $3000-3000.99) in sandbox a "Something Went Wrong" message will be displayed on the reader instead of "Declined" or "Transaction Failed"




## Version 5.0.0 - Released on 2023-01-13

**NOTE**
Readers must be updated to version 4.0.0 before updating to version 5.0.0


#### New


- SAF: Ability to pass in statement descriptors and custom fields on SAF refund and sale transactions


- SAF: Added a new SAF enablement indicator in the reader admin settings menu. "Active" means SAF is enabled and ready for use. "inactive" means SAF is not enabled and will fail.




#### Fixed


- Admin Menu: You can now access the reader admin menu from the "Reader pairing" screen (when the one-time passcode is displayed) using the 2+8 button prompt


- Admin Menu: You can now access the reader admin menu from the "Not Connected" error screen using the 2+8 button prompt


- Admin Menu: You can now access the reader admin menu from the "Reader Not Provisioned" error screen using the 2+8 button prompt


- E285: Now closing reader payment interfaces after the transaction is completed or ended, which should result in better battery performance




## Version 4.0.0 - Released on 2022-09-01

**NOTE**
M400 reader availability is subject to purchase order forecasting


**NOTE**
 Please note, version 4.0.0 is a significant upgrade which is also updating the underlying operating system of the card reader. It will take longer than a normal payment-app OTA update and will also display different screens during the installation process that you may not be used to from prior updates. You will know the installation is done once the reader automatically reboots two to three times and the payment-app appears.

  You should not unplug the power to the reader while this upgrade is happening. If you are upgrading any E285s, then you should also make sure they are plugged into power when performing the update to 4.0.0. The upgrade can take up to 20 minutes to complete.

 

**NOTE**
Readers must be updated to version 4.0.0 before updating to any newer version of the reader application.


#### New


- [Verifone M400](/braintree/in-person/hardware/verifone-m400/) reader now available


- Upgraded Verifone ADK version 4.7.20


- SAF: Added reader beep sound for ping query during SAF mode


- SAF: Added SAF indicator to the reader admin settings page




#### Fixed


- Vaulting: Disabled PIN prompt for contactless vault


- Custom Prompts: Increased title character limit from 20 to 50 characters


- Custom Prompts: Added cancellationText and confirmationText API fields to [Request Signature Prompt](/braintree/in-person/guides/custom-prompts/#request-signature-capture)


- Custom Prompts: Increased cancellationText and confirmationText character limit from 10 to 20 characters




## Version 3.3.0 - Released on 2022-07-08


#### New


- [Custom Prompts](/braintree/in-person/guides/custom-prompts/) New API Call: [Request Signature Prompt](/braintree/in-person/guides/custom-prompts/#request-signature-capture)


- [Custom Prompts](/braintree/in-person/guides/custom-prompts/) New API Call: [Request Confirmation](/braintree/in-person/guides/custom-prompts/#request-confirmation)




#### Fixed


- SAF: fixed node query for offline refunds


- SAF: fixed large amount handling


- SAF: fixed node query missing orderId


- SAF: fixed offline transaction cancel with red "x" button not displaying "Canceled" message


- Admin Menu: fixed populate "ok" text on IP address config screen


- E285: fixed missing "enter pin" text




## Version 3.2.0 - Released on 2022-03-30


#### New


- Store and Forward requests now support idempotency key


- Users are prompted to charge reader if battery is too low to successfully conduct a transaction


- Updated contact card Authorizing and Success screen verbiage to encourage customers to leave the chip card in until the "remove card" prompt appears


- Reader now validates user-provided netmask for Static IP configurations




#### Fixed


- More information for troubleshooting connection problems is provided when the reader is unable to connect to the previously-connected network


- Fixed handling of multiple RequestDisplay messages received within milliseconds


- Fixed CUP CTLS and PIN transactions




## Version 3.1.0 - Released on 2021-11-18

**NOTE**
Any readers still on versions 3.0.0 or older will no longer be able to update to newer firmware versions due to a certificate update, if you have devices stuck on this version which need to be updated they may need to be swapped out for new hardware. These devices will continue to work in both sandbox and production environments.


#### New


- Reader may now immediately update its firmware the next time it boots based on a configurable flag


- A QRC payment may now be cancelled by pressing the![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MHC3jcyXto5tW9-uxQj%252F-MHC3vtqJLFBP6ZPHG_c%252Fred_btn.png%3Falt%3Dmedia%26token%3D7663af22-d526-43ab-9bc3-ef1c5aefae56&width=300&dpr=2&quality=100&sign=8a1868a1&sv=1) button at any time, including when the payment flow has gone to the customer's smartphone app


- Store-and-Forward Unreferenced Refunds are now available




#### Fixed


- QRC Layouts on the e285 have been fixed


- Transitions between the screen saver and other displays no longer flicker


- Failed QRC transactions now show up in Braintree instead of never appearing




## Version 2.0.0 - Released on 2021-10-01


#### New


- Universal status bar showing Wi-Fi or Ethernet connection and battery state if applicable.


- Security and stability improvements.


- Point to Point Encryption (P2PE) certification requirements.




## Version 1.2.2 - Released on 2021-08-05


#### New


- Support for charging customers when the reader is offline, also known as "Store and Forward" transactions. Configuration is required prior to using this feature in production. To get started, see the Offline Transactions guide.



[Offline Transactions](/braintree/in-person/guides/offline-transactions/)
#### Fixed


- After successful pairing of a reader the success message no longer says The reader is connected to your Braintree Sandbox Account. It now says The reader is connected to your Braintree merchant account


- When the reader temporarily loses internet connection during a transaction it no longer causes the transaction to abort and the app to restart.


- An issue with e285 devices where the app's networking layer was unable to send network requests causing transactions to fail.


- e285 devices no longer wake themselves automatically after entering sleep mode.


- An issue where html tags included in a Wi-Fi network name were rendered as html on screen during the pairing flow. Tags are now escaped prior to displaying network names.



[Support/Contact Us](/braintree/in-person/post-launch-activities/contact-us/)[Verifone Device Reference](/braintree/in-person/reference/verifone-p400-reference/)