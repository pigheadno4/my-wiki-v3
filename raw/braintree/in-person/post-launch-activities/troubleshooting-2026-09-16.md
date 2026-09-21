<!-- Source URL: https://developer.paypal.com/braintree/in-person/post-launch-activities/troubleshooting -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Troubleshooting
slug: /in-person/post-launch-activities/troubleshooting/
createTime: '2024-11-20T19:03:35.662Z'
updateTime: '2024-11-20T19:03:35.968Z'
---



# Troubleshooting


## [](#have-you-tried-updating-the-firmware-on-your-reader)Have you tried updating the firmware on your reader?

Updating the firmware version on the reader can sometimes resolve issues if there is a known bug that has since been fixed within our app. For more information on updating the firmware of your device click the link below to the Firmware Updates page:

[Managing Firmware Updates](/braintree/in-person/post-launch-activities/managing-firmware-updates/)
## [](#how-to-restart-the-payment-app)How to restart the payment app?

From any screen in the app, you may **press and hold the green circle button**![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MHC1oMiFmEstCOpDssG%252F-MHC3apwhk8GoiR07Wf2%252Fgreen_btn-inline.png%3Falt%3Dmedia%26token%3D4aee92dd-1302-4986-9fa7-cc208bdca843&width=300&dpr=4&quality=100&sign=51d0534a&sv=1) to reboot the device.


## [](#how-to-shutdown-the-reader)How to shutdown the reader?

To shutdown the reader, you can either **unplug the device from the power source** or **press and hold**![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MHC1oMiFmEstCOpDssG%252F-MHC3apzAF2XIAmjQIiK%252Fred_btn-inline.png%3Falt%3Dmedia%26token%3D96cf46d2-d6b5-4426-9fcd-ac4ce55f33c8&width=300&dpr=4&quality=100&sign=d5d493de&sv=1) **for at least 5 seconds**.


## [](#error-screen-appears)Error screen appears?

![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MGtFtIlgtiy3UZiNZA6%252F-MGtIJHFSaX5IqANtnSp%252Faction-failed.png%3Falt%3Dmedia%26token%3D1d3a6c4c-ee2d-48d2-befc-24972d67365d&width=768&dpr=4&quality=100&sign=a4f37476&sv=1)Something went wrong error screen.Many issues can be fixed by restarting the payment app. If you see this screen, follow the prompt to "Restart the App". Alternatively, you may **press and hold the green circle button**![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MHC1oMiFmEstCOpDssG%252F-MHC3apwhk8GoiR07Wf2%252Fgreen_btn-inline.png%3Falt%3Dmedia%26token%3D4aee92dd-1302-4986-9fa7-cc208bdca843&width=300&dpr=4&quality=100&sign=51d0534a&sv=1) to reboot the device.


## [](#cant-connect-to-sandbox)Can't connect to Sandbox

Check that your sandbox credentials are correct and that your device is connected to the WiFi Network. If the problem persists please [contact us](/braintree/in-person/post-launch-activities/contact-us/).


## [](#is-your-reader-connected-to-your-network-but-not-reaching-the-braintree-platform)Is your reader connected to your network but not reaching the Braintree platform?

This can happen if your onsite network has a firewall that may be blocking communication from the Braintree platform endpoints to and from the reader. Please double-check that your network firewall is not blocking network traffic with the [Braintree Endpoints](/braintree/in-person/guides/setup-reader/#braintree-domains-to-whitelist). If you're still having issues try running our [network diagnostics tool](/braintree/in-person/post-launch-activities/troubleshooting/#have-network-connectivity-issues).


## [](#having-network-connectivity-issues)Having network connectivity issues?

As of [version 5.1.0](/braintree/in-person/reference/app-version-release-notes/#version510) we now support a [network diagnostics tool](/braintree/in-person/post-launch-activities/network-connection-test/) that can be accessed from the reader admin menu. You can access the admin menu by pressing 2+8 on the number pad, then enter your admin menu password and press the **Run Connection Test** button to begin. This tool helps you identify where the breakdown in communication may be occurring on your network.

![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M6GgIF79CNAhEDh9YbJ%252Fuploads%252FgbM4qeXPhckB6beKsj2G%252Fconnection%2520text_e285.png%3Falt%3Dmedia%26token%3Deed8ffc0-a450-4f62-90c7-74211284265e&width=768&dpr=4&quality=100&sign=5dff79c7&sv=1)Example screenshots of the network diagnostics tool
## [](#need-to-contact-our-support-team)Need to contact our Support team?

If you still need help after trying some of the troubleshooting tips, please reach out and provide detailed information on the issue you are experiencing as outlined on our [contact page](/braintree/in-person/post-launch-activities/contact-us/).

[Managing Firmware Updates](/braintree/in-person/post-launch-activities/managing-firmware-updates/)[Network Connection Test](post-launch-activities/network-connection-test/)