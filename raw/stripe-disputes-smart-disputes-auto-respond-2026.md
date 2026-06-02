<!-- Source URL: https://docs.stripe.com/disputes/smart-disputes-auto-respond -->
<!-- Fetched: 2026-05-10 -->

# Configure Smart Disputes auto-respond settings

Learn how to configure Smart Disputes auto-respond settings for your account and connected accounts.

Smart Disputes can automatically submit evidence for eligible disputes at the deadline, helping you avoid missed opportunities to contest chargebacks. This guide explains how to configure auto-respond settings based on your account type.

## How it works

When auto-respond is on, Stripe automatically submits evidence for eligible disputes at the deadline. This means:

- You don’t miss dispute deadlines
- Evidence is automatically submitted for eligible disputes
- You spend less time on manual dispute management

Smart Disputes determines eligibility based on dispute characteristics and available evidence. Not all disputes qualify for automatic submission.

You can manually submit evidence at any time, even with auto-respond enabled.

## For direct accounts

1. Go to [Settings > Disputes](https://dashboard.stripe.com/settings/disputes) in the Dashboard.
1. Toggle the Smart Disputes auto-respond setting.

Changes apply immediately to disputes that still require a response. When you disable auto-respond, you accept and lose any dispute that you don’t counter by the deadline.

## For Connect platforms

As a platform, you control Smart Disputes auto-respond settings for your connected accounts. You can set a default for all connected accounts and choose whether they can override your default.

### Configure settings in the Dashboard

1. Go to [Settings > Connect > Disputes](https://dashboard.stripe.com/settings/connect/disputes) in the Dashboard.
1. Configure your preferences:
   - **Turn auto-respond on or off for connected accounts**: Sets the default for all connected accounts.
   - **Allow connected accounts to override**: Choose whether connected accounts can change their own settings.

Changes apply immediately to disputes that still require a response.

> These settings apply to payments your connected accounts create using direct charges and destination charges (including destination on_behalf_of). To configure auto-respond for your platform’s own disputes, go to **Settings** > **Disputes**.

### Smart disputes default and override settings

Smart disputes have the following default and override settings:

- **Platform default**: All connected accounts inherit your platform setting unless you set an explicit override using the API, or you allow them to override it.
- **API overrides**: You can set individual account preferences using the Accounts API.
- **Connected account overrides**: If you allow overrides, connected accounts can change their own settings.

When you change your platform default, connected accounts with `preference`=`inherit` (or no explicit API override) immediately reflect your new default. Accounts with explicit overrides aren’t affected.

### Configure settings using the API

For stricter control over individual connected accounts, use the Accounts API to set the smart_disputes hash.

Available fields:

1. `preference` (writable): Controls the intended behavior
   - `on`: Enable auto-respond, and override the platform default
   - `off`: Disable auto-respond, and override the platform default
   - `inherit`: Use the platform’s default setting
1. `value` (read-only): Shows the actual effective setting
   - `on`: Auto-respond is currently enabled
   - `off`: Auto-respond is currently disabled

After you set an explicit `preference`, the account ignores platform-level default changes until you reset it to `inherit`.

Example API call:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.accounts.update("{{ACCOUNT_ID}}", {
  settings: {
    smart_disputes: {
      auto_respond: {
        preference: "on",
      },
    },
  },
});
```

## For Connected accounts

1. Go to [Settings > Disputes](https://dashboard.stripe.com/settings/disputes) in the Dashboard.
1. View your Smart Disputes auto-respond settings.

You see separate settings for:

- **Your own disputes**: Disputes on payments made directly on your account (not associated with any platform)
- **Each platform you’re connected to**: Disputes on payments created through each platform

### Why you can’t change a setting

If you can’t toggle a platform’s auto-respond setting, your platform has disabled overrides. A message in the Dashboard explains this.

To change your auto-respond settings in this case, contact your platform.
