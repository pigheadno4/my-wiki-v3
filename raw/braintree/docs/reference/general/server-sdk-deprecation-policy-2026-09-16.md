<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/server-sdk-deprecation-policy -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Server SDK Deprecation Policy
slug: /docs/reference/general/server-sdk-deprecation-policy/
createTime: '2025-04-02T01:25:08.469Z'
updateTime: '2025-04-02T01:25:08.491Z'
---



# Server SDK Deprecation Policy


**NOTE**
We recommend that you make regular updates to your Braintree integration and update your server SDK version at least every two years.


## Overview

Braintree makes regular updates to our server SDKs and follows[semantic versioning](https://semver.org/)guidelines with these updates. Whenever we need to make updates that will require code changes to existing integrations, we increase the major version number of the SDK to indicate that your integration will likely need to be updated for it to work with the newest version.

Examples of changes that would require a major version update:


- Adding support for a new server language version released by its core development community
- Dropping support for a server language version that is no longer receiving security updates by its core development community
- Adding support for newer protocols that make server integrations more performant (i.e. HTTP keep-alive, HTTP2)


**NOTE**
We do our best to add support for these without introducing a new major version, but if the changes required are great enough, they could result in a breaking change.


## Status categories

Server SDKs can have one of the following statuses:| Status | Description | State of development |
| --- | --- | --- |
| **Active** | An active SDK version is the most current and fully supported SDK. It is the recommended version to be used by everyone. Only 1 exists at a time. | **This version will receive new features.** |
| **Inactive** | An SDK becomes inactive once assigned a deprecation date. Any number can exist at a time. | **No new features will be added, only security updates.** |
| **Deprecated** | Processing will be supported for 1 year after the deprecation date, but you should upgrade immediately to avoid any disruption. Any number can exist at a time. | **Deprecated SDKs will not receive updates.** |
| **Unsupported** | A retired SDK version is no longer supported by Braintree developers or Braintree Support. Any number can exist at a time. | **Processing for these SDKs can be suspended at any time.** |

Here is a visual representation of how server SDK major version statuses can change over time:

![diagram,of,SDK,status,changes](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/server-deprecation-schedule.svg)The README for each server SDK includes the status and deprecation dates for all major versions, and we will update these statuses as we release new major versions.


**NOTE**
There may be unforeseen circumstances where we need to make exceptions to these statuses. If that happens, we will do our best to communicate these changes.


## Tips for following SDK versions

We recommend[watching the SDK on Github](https://help.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#about-participating-and-watching-notifications)to stay informed about the latest version of the server SDK you're using.

In addition, we may occasionally contact you if there are upcoming changes that require updating your server SDK.
## Further reading


- [Best practices](/braintree/docs/reference/general/best-practices/)
- [Server SDK migration guides](/braintree/docs/reference/general/server-sdk-migration-guide/)

Github repository links:


- [Java](https://github.com/braintree/braintree_java)
- [.NET](https://github.com/braintree/braintree_dotnet)
- [Node](https://github.com/braintree/braintree_node)
- [PHP](https://github.com/braintree/braintree_php)
- [Python](https://github.com/braintree/braintree_python)
- [Ruby](https://github.com/braintree/braintree_ruby)


## See Also


- [Client SDK deprecation policy](/braintree/docs/guides/client-sdk/deprecation-policy)

