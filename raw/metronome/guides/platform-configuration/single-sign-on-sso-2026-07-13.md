<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/single-sign-on-sso.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Single sign-on (SSO)

Single sign-on (SSO) allows team members to access Metronome with the same identity or service providers they use to authenticate within their own organization or external services. This means that your team can log into Metronome using your corporate sign-in process (for example, using a corporate Gmail account), instead of needing to create a new username and password.

Metronome supports SSO with the [SAML 2.0](https://en.wikipedia.org/wiki/SAML_2.0) protocol, both for service provider and identity provider initiated authentication. This is supported by most common service provider and identity management services, including ADFS, Azure, Google, Okta, OneLogin, Ping Identity, and SecureAuth. Metronome SSO also handles user provisioning between your Identity Provider (IdP) and your Metronome instance.

## User management with SSO

<Note>
  **REMOVE USERS**

  With SSO, access to Metronome is controlled by your identity provider. If a user is removed from Metronome access on your end, that user can no longer log in. Metronome still shows metadata about all users on the [Team Settings](https://app.metronome.com/settings/team) page, including the role each user had during their last log in.
</Note>

To set up SSO:

1. Let your Metronome representative know you're interested in SSO. Metronome will provide you with these values:

   * Assertion Consumer Service (ACS) URL
   * Metronome Entity ID
   * Metronome logo (used for the tile within your identity provider)

2. Use these values to generate an Identity Provider URL (Single Sign-On Service URL) and an X509 signing certificate (in PEM or CER format).

3. Provide Metronome with the Identity Provider URL and X509 signing certificate. Metronome then creates a connection between your Identity Provider and the Metronome environment.

4. For the following attributes, provide Metronome with the equivalent attribute name in your claims:

   * `name` or `firstName lastName`

   * `email`

5. Once Metronome has the correct attribute mapping above, we conduct a few final tests with you to ensure SSO works. Once this has been verified your account will be switched over to SSO; existing username and password-based logins cease to work.
