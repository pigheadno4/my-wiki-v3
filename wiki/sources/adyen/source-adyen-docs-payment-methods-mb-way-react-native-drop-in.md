---
title: "MB WAY React Native Drop-in integration add-on"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mb-way/react-native-drop-in/2026-09-15.md"
tags: [adyen, mb-way, react-native, drop-in, await]
---

## Overview

This 2026-09-15-captured MB WAY React Native Drop-in page gives method-specific additions to existing Sessions and Advanced React Native Drop-in integrations. It documents a phone-number/`await` path and does **not** give App2App implementation steps. It relies on base integration guides and does not prove current account enablement or completed live payment. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] for PT/EUR method scope and distinct mobile App2App description.

## Key takeaways

- **Sessions:** the requirements call for an existing React Native Sessions-flow Drop-in integration, Checkout API **v68 or later**, and MB WAY added in Customer Area. Its method-specific `/sessions` table marks `shopperStatement` required as text for the shopper's bank statement. The page says no extra MB WAY Drop-in configuration is needed (raw lines 25–45, 68–72).
- **Advanced:** requires an existing React Native Advanced-flow Drop-in integration, additional-action handling for `action.type: await`, and MB WAY added in Customer Area. Its method-specific `/payments` table marks `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber` required; `shopperStatement` has no required mark. The sample response is `Pending` with an `await` action to display a waiting screen while the shopper completes payment in the MB WAY app. `Pending` is not final authorization (raw lines 95–166).
- The page says any phone number can be used in **test**, with an example, and gives `shopperStatement` suffixes `-c1`, `-c3`, and `-c5` to simulate Authorised, Pending and Refused `resultCode` values. These result-code directions refer to `/payments`, including in the Sessions section. Live acceptance requires MB WAY added in the live Customer Area (raw lines 74–93, 168–187).

> [!warning] React Native route and App2App scope
> The Sessions requirement labels a **Sessions-flow** React Native Drop-in integration but links an `advanced-flow?platform=React%2BNative&integration=Drop-in` URL (raw line 33); the separate Sessions request link points to `sessions-flow` (line 41). Follow the correct base route for the chosen flow. The [[source-adyen-docs-payment-methods-mb-way|MB WAY overview]] describes mobile App2App without manual phone entry (overview pinned raw lines 23–30), while this child guide's Advanced table requires a phone number and contains no App2App branch (child raw lines 119–123, 168–187). Do not infer that this React Native Drop-in guide implements or excludes App2App; consult the relevant App2App integration authority.

> [!warning] Example command and return routing
> Both curl examples omit a continuation between `-X POST` and `-d` (raw lines 54–55, 132–133). The Advanced example uses a website `https://...` return URL while the Sessions example uses `adyencheckout://...` (lines 61, 139); verify return handling with the React Native base flow. These samples are not complete paste-ready commands.

## Detail locators

- Scope and Sessions requirements, `shopperStatement`, no-extra-config: raw lines 15–72.
- Sessions test/live and simulated results: raw lines 74–93.
- Advanced requirements, method-specific fields and `Pending`/`await`: raw lines 95–166.
- Advanced test/live and simulated results: raw lines 168–187.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-mb-way]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/react-native-drop-in/2026-09-15|MB WAY React Native Drop-in guide, captured 2026-09-15]]
