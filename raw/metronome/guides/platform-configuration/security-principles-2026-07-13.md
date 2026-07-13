<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/security-principles.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metronome's security principles

Metronome is committed to security and keeping data safe—yours and your customers'. We adhere to industry-leading standards. We consistently review our security practices to ensure we have the right systems, policies, and controls in place.

Our security practices are based on three core principles:

* **Least privilege**

  No actor in Metronome has access to data or the ability to take actions until and unless that access has been explicitly granted. Access is controlled down to the field level.

* **Zero-trust architecture**

  Metronome has been built from day one with zero-trust architecture. In practice, this means that any communication between two systems (or any actor and system) is authenticated.

  For example, a user communicating with the Metronome data layer must make requests with a security token in their request. The data layer may service that request by calling other services that subsequently call other services or databases, and so forth. The same security token must be passed on to each of these underlying calls, and each service in the stack uses the token to verify and grant the relevant access. Combined with the principle of least privilege, every single part of the Metronome product enforces that actors (human or system) can only access the most minimal data for their task.

* **No access granted via long-lived credentials or configuration**

  Because of Metronome's zero-trust architecture, almost no part of Metronome's system depends on long-lived API keys or other such static security tokens. Our AWS organization is set up in such a way that we have no long-lived AWS credentials on developer's machines. Metronome engineers must mint new credentials each day, and those credentials last only 12 hours.

For the most detailed and up-to-date information on security at Metronome, visit our [security page](https://metronome.com/company/security). To request a copy of our SOC 2 report, please contact your Metronome representative.
