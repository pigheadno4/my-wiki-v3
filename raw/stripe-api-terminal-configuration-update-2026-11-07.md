<!-- Source URL: https://docs.stripe.com/api/terminal/configuration/update -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Update a Configuration

Updates a new `Configuration` object.

## Prerequisites

Before you can run the following code snippet, you need to call these APIs with the provided parameters to set up the prerequisite API object(s).

1. createTerminalConfiguration
POST /v1/terminal/configurations

## Request

```curl
curl https://api.stripe.com/v1/terminal/configurations/{{CONFIGURATION_ID}} \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive" \
  -d "bbpos_wisepos_e[splashscreen]={{FILE_ID}}"
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "bbpos_wisepos_e": {
    "splashscreen": "file_1NtDiPBHO5VeT9SUvD7GHCi0"
  },
  "is_account_default": false,
  "livemode": false
}
```

## Parameters

- `id` (string, required)
  Unique identifier for the object.

- [`bbpos_wisepad3`](https://docs.stripe.com/api/terminal/configuration/update.md?query=bbpos_wisepad3) (object, optional)
  An object containing device type specific settings for BBPOS WisePad 3 readers.

- [`bbpos_wisepos_e`](https://docs.stripe.com/api/terminal/configuration/update.md?query=bbpos_wisepos_e) (object, optional)
  An object containing device type specific settings for BBPOS WisePOS E readers.

- [`cellular`](https://docs.stripe.com/api/terminal/configuration/update.md?query=cellular) (object, optional)
  Configuration for cellular connectivity.

- `name` (string, optional)
  Name of the configuration

  The maximum length is 100 characters.

- [`offline`](https://docs.stripe.com/api/terminal/configuration/update.md?query=offline) (object, optional)
  Configurations for collecting transactions offline.

- [`reader_security`](https://docs.stripe.com/api/terminal/configuration/update.md?query=reader_security) (object, optional)
  Configurations for reader security settings.

- [`reboot_window`](https://docs.stripe.com/api/terminal/configuration/update.md?query=reboot_window) (object, optional)
  Reboot time settings for readers. that support customized reboot time configuration.

- [`stripe_s700`](https://docs.stripe.com/api/terminal/configuration/update.md?query=stripe_s700) (object, optional)
  An object containing device type specific settings for Stripe S700 readers.

- [`stripe_s710`](https://docs.stripe.com/api/terminal/configuration/update.md?query=stripe_s710) (object, optional)
  An object containing device type specific settings for Stripe S710 readers.

- [`stripe_t600`](https://docs.stripe.com/api/terminal/configuration/update.md?query=stripe_t600) (object, optional)
  An object containing device type specific settings for Stripe T600 readers.

- [`tipping`](https://docs.stripe.com/api/terminal/configuration/update.md?query=tipping) (object, optional)
  Tipping configurations for readers that support on-reader tips.

- [`verifone_m425`](https://docs.stripe.com/api/terminal/configuration/update.md?query=verifone_m425) (object, optional)
  An object containing device type specific settings for Verifone M425 readers.

- [`verifone_p400`](https://docs.stripe.com/api/terminal/configuration/update.md?query=verifone_p400) (object, optional)
  An object containing device type specific settings for Verifone P400 readers.

- [`verifone_p630`](https://docs.stripe.com/api/terminal/configuration/update.md?query=verifone_p630) (object, optional)
  An object containing device type specific settings for Verifone P630 readers.

- [`verifone_ux700`](https://docs.stripe.com/api/terminal/configuration/update.md?query=verifone_ux700) (object, optional)
  An object containing device type specific settings for Verifone UX700 readers.

- [`verifone_v660p`](https://docs.stripe.com/api/terminal/configuration/update.md?query=verifone_v660p) (object, optional)
  An object containing device type specific settings for Verifone V660p readers.

- [`wifi`](https://docs.stripe.com/api/terminal/configuration/update.md?query=wifi) (object, optional)
  Configurations for connecting to a WiFi network.

## Returns

Returns a `Configuration` object if the update succeeds.
