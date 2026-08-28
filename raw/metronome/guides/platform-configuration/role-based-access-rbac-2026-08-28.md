<!-- Source URL: https://docs.metronome.com/guides/platform-configuration/role-based-access-rbac.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Role-based access control (RBAC)

export const Button = ({text}) => <a href="https://metronome.com/talk-to-an-expert" target="_blank" rel="noopener noreferrer" className="inline-block bg-[#102F36] hover:bg-opacity-80 text-white font-bold px-6 py-3 rounded-full text-sm tracking-wide uppercase transition-colors duration-200">{text}</a>;

Role-based access control (RBAC) policies define how users interact with Metronome, what they are allowed to see, and what changes they are allowed to make. This increases your control over the data a user can access and the actions they can take. Implementing RBAC minimizes the scope of security vulnerabilities and reduces human error.

<Tip>
  **CUSTOM ROLES**

  We also support custom roles, allowing you to tailor permissions to your needs.

  <Button text="Talk to an expert" />
</Tip>

## Defined roles​

Metronome offers three out-of-the-box roles:

* **Administrator**\
  Ideal for project leads who need full functional access to oversee Metronome configuration and integration with other systems, along with administrative controls. Administrators have full CRUD (create, read, update, and delete) access to all components of the Metronome system.

* **Writer**\
  Ideal for members of the working team who are responsible for configuring and maintaining Metronome, including integrations with other systems. Writers have CRUD access to everything in Metronome except the creation of API keys or administrative settings (like setting up data export).

* **Reader**\
  Ideal for a non-acting member of the working team that is not involved with configuration, but needs access to Metronome data or is supporting the roll out of Metronome at your organization. Readers can view all components of the Metronome system, but have no create, update, or delete access to any parts of the system.

## Set up RBAC​

RBAC policies are defined by your Identity Provider; you must set up [SSO](/guides/platform-configuration/single-sign-on-sso/). If no SSO is configured, all users with access to Metronome have full access permissions.

To set up RBAC:

1. Set up [SSO](/guides/platform-configuration/single-sign-on-sso/).

2. With your Identity Provider, create a new claim to specify user roles.\
   a. The claim can be called anything; we recommend `role`.\
   b. The values for this claim are: `admin`, `writer`, `reader`, or any custom roles you work with the Metronome team to create.

3. Submit the new claim name via the [Metronome support portal](https://support.metronome.com/).

4. Let us know via the [Metronome support portal](https://support.metronome.com/) which role users should default to if not specified. By default, any user with no specified role is denied access to Metronome.

## Assign a role to an API token

When creating a new API token in the Metronome UI, you can assign an RBAC role directly. The token will inherit the permissions of the selected role, scoping its access accordingly. Roles cannot be changed after a token is created.

To assign a role to an API token:

1. In the Metronome UI, navigate to **Developer > API tokens**.
2. Click **+ Add**.
3. Select a role to assign to the token (**Administrator**, **Writer**, or **Reader**).
4. Complete token creation.

<Note>
  To assign a custom role to an API token, contact us via the [Metronome support portal](https://support.metronome.com/) to have the role created first.
</Note>
