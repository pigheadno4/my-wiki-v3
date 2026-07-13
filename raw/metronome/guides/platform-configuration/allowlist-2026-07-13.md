<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/allowlist.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Allowlist the Metronome API

Metronome supports IP allowlisting for accessing its APIs. Implementing an allowlist restricts Metronome API access to a specific set of IP addresses, enhancing security by limiting potential entry points for unauthorized access.

## Implement allowlisting​

To implement allowlisting:

1. Retrieve Metronome’s API IP addresses by polling the [getServices](/api-reference/security/get-services) endpoint.
2. Use response IPs to configure your organization’s allowlist in accordance with your security protocols and network security tools.

## Test and automate to ensure access​

You must take action to ensure continued access and security with IP allowlisting. This is due to:

* **IP address changes**\
  Metronome's IP addresses are subject to change. New IPs appear in the list at least 30 days before they are first used.

* **Polling frequency**\
  Failure to regularly poll the `getServices` API to update your allowlist may result in losing access to Metronome APIs, as IPs get frequently rotated in and out of service.

* **Security layers**\
  While IP allowlisting can add an extra layer of security, use it in conjunction with additional security measures like SSO and scoped RBAC roles.

For optimal use of IP allowlisting, follow these best practices:

* Automate the process of regularly polling the `getServices` API and updating your allowlist
* Test your allowlist configuration regularly to ensure continued access to Metronome APIs
* Maintain a changelog of updates to your allowlist for auditing purposes

<Note>
  **NEED HELP?**

  If you encounter any issues with IP allowlisting or have questions about implementation, contact your Metronome representative.
</Note>
