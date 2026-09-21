<!-- Source URL: https://developer.paypal.com/braintree/in-person/post-launch-activities/network-connection-test -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Network Connection Test
slug: /in-person/post-launch-activities/network-connection-test/
createTime: '2024-11-20T19:05:03.436Z'
updateTime: '2024-11-20T19:05:03.909Z'
---



# Network Connection Test

This page provides information on how to run a network connection test from the reader admin menu and interpret its results.

**NOTE**
This feature is supported in [firmware version 5.1.0](/braintree/in-person/reference/app-version-release-notes/#version510) and newer


## [](#how-to-run-a-connection-test-on-the-card-reader)How to run a connection test on the card reader


- Access the reader admin menu by pressing 2 + 8 on the number pad of the reader


- For test devices, use the password 123456 (for production devices, use the PW provided to you)


- Click **Run Connection Test** to start the diagnostics



![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M6GgIF79CNAhEDh9YbJ%252Fuploads%252FgbM4qeXPhckB6beKsj2G%252Fconnection%2520text_e285.png%3Falt%3Dmedia%26token%3Deed8ffc0-a450-4f62-90c7-74211284265e&width=768&dpr=4&quality=100&sign=5dff79c7&sv=1)Example image of a connection test on an E285 deviceThere are 4 different testing states: **Testing**, **Unavailable**, **Failed**, and **Success**


- **Testing** : this means that the test is in progress


- **Unavailable** : this means that the system will not be able to run certain tests if your reader has not be [paired to a location ID](/braintree/in-person/guides/setup-reader/#pair-reader-to-a-location-id)


- **Failed** : this means that a particular diagnostics test failed


- **Success** : this means that a particular diagnostics test was successful




## [](#braintree-endpoint-check)Braintree Endpoint Check

By checking the accessibility of the Braintree endpoints from your network, we are validating whether your network firewall is blocking any traffic to and from the reader and 3 endpoints of the Braintree platform: **Braintree Public API**, **Reader API**, **Websocket API**.

| **Test Name** | **Result** | **Explanation** |
| Braintree Public API | Failed | Cannot connect to **payments.braintree-api.com** |
| Reader API | Failed | Cannot connect to **reader.braintree-api.com** |
| Websocket API | Failed | Cannot connect to

**reader-websocket.braintree-api.com** |

Each endpoint connection test will include 4 steps. A failure in any of the steps can mean something different. Here is an explanation of each step:

| **Test Step** | **Result** | **Explanation** |
| Parsing URL | Failed | Please the [contact support](/braintree/in-person/post-launch-activities/contact-us/) team for more information. |
| Resolving DNS | Failed | Your reader is having a DNS problem. Its having trouble talking to the Braintree domain. |
| TCP Connection | Failed | There is a problem with your router. The internet connection is down. Or the Braintree platform is unavailable. |
| Server returned error | Failed | Please the [contact support](/braintree/in-person/post-launch-activities/contact-us/) team for more information. |


## [](#internet-connection-check)Internet Connection Check

These checks are to determine the accessibility of your network to the outside internet.


#### [](#network-test)Network Test:

| **Test Name** | **Result** | **Explanation** |
| Network | Failed | No access to the internet. |

There are 2 testing steps taken during the Network test. Here is a further explanation:

| **Test Step** | **Result** | **Explanation** |
| ICMP Ping | Failed | Your reader does not have general internet connectivity. Check your network and/or firewall settings. |
| Resolving DNS | Failed | Your reader is having a DNS problem. Check your network and/or firewall settings. |


#### [](#speed-test)Speed Test:

| **Test Name** | **Result** | **Explanation** |
| Speed | Failed | Internet not available. |
| Speed | Unavailable | Your reader is not paired. [Pair your reader to a location ID](/braintree/in-person/guides/setup-reader/#pair-reader-to-a-location-id). |

There are 2 testing steps taken during the Speed test. Here is a further explanation:

| **Test Step** | **Result** | **Explanation** |
| Parsing URL | Failed | The URL your reader used is invalid, please [contact the support team](/braintree/in-person/post-launch-activities/contact-us/). |
| Retrieving URL | Failed | Your reader is having a DNS problem. |


#### [](#time-server-test)Time Server Test:

| **Test Name** | **Result** | **Explanation** |
| Time Server | Failed | The time on your reader is off. The reader is not able to retrieve the time and date. Your firewall is blocking NTP. Check your firewall settings and [whitelist Braintree Domains](/braintree/in-person/guides/setup-reader/#braintree-domains-to-whitelist). |

[Troubleshooting](/braintree/in-person/post-launch-activities/troubleshooting/)[Support/Contact Us](post-launch-activities/contact-us/)