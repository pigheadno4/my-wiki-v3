<!-- Source URL: https://docs.metronome.com/integrations/platform-integrations/workato-connector.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up the Metronome Workato connector

Our clients commonly use the IPAAS system Workato to build integrations with Metronome. These integrations enable a variety of workflows, such as

* Invoicing through third-party billing systems
* Customer provisioning
* Contract provisioning

To enable these integration patterns, Metronome has invested in building a Workato connector. This connector acts like an SDK, enabling users in Workato to perform actions on Metronome endpoints. To set up a connection to your Metronome environment:

1. Install the [Workato connector](https://app.workato.com/custom_adapters/543474?token=f676fd9c66ce244573d8a8167942493b6696ef7660b1b9bbbec98cb2dd8e9963).
2. Generate an API token in Metronome. See [API authorization](/api-reference/authorization) for instructions.
3. Create a new connection in Workato and paste the API token in the appropriate field.
4. This connection is available to use in new workflows!

<Note>
  **METRONOME ENVIRONMENTS**

  Please note that a unique connection needs to be made for each Metronome environment you wish to connect.
</Note>
