# Braintree C41 fixed-query audit L — positions 45–48

- Campaign: `braintree-campaign-41`
- Mode: read-only query audit
- Assigned jobs: positions 45–48
- Required questions: 8 total, exactly 2 per page
- Analysis end (UTC): `2026-10-06T15:39:10Z`
- Result: **8 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded gap sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, and the fixed-query policy in `tracking/ingest/braintree/braintree-campaign-41/selection-review.md` before auditing.
- Followed root index → Braintree provider index → main concept → promoted source → pinned raw. Fully read the four promoted sources and four pinned raws. Manifest job/target/URL identity, source `canonical_url` and `raw_files`, raw Source URL metadata, and pinned SHA-256 all match.

| Position | Job | Verified SHA-256 |
| ---: | --- | --- |
| 45 | `in-person-hardware-verifone-m400` | `647c4ffe9de74dd1037d31d8902707f75ea659b71cd6956bd763f06f86e4fdd6` |
| 46 | `in-person-hardware-verifone-p400` | `ce17eb68d2ee0ffad9983c3baa80db8fe14c5c041694d292e925b36ecdf20658` |
| 47 | `docs-guides-fastlane-overview` | `30a507398a3bb65c83e267e7fd95c7841066bc3557ee3248e78fdb74fc86494e` |
| 48 | `in-person-post-launch-activities-network-connection-test` | `9bc2e82a8e114445282f135cfb9aa66689a7e97002e15572243e38c520410882` |

- The bounded filename/related-reference sweep found neighboring M400/P400/V400m/E285 hardware and reference pages, Fastlane setup/testing guides, and network setup/release-note/troubleshooting routes. The P400 source retains one cross-page claim about a separate Sandbox setup/pairing guide, so `source-braintree-in-person-guides-setup-reader.md` and its pinned raw were fully read and confirm that claim. No other extra authority was needed for these exact-page questions; unread linked pages remain navigation only.

## Position 45 — `in-person-hardware-verifone-m400`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:15` → `wiki/sources/braintree/source-braintree-in-person-hardware-verifone-m400.md` → `raw/braintree/in-person/hardware/verifone-m400-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 collected, unversioned Braintree In-Person hardware overview for the fixed-lane Verifone M400: device/kit/accessories, captured specifications and entry modes, Ethernet/WiFi support, and idle-screen customization. It names no SDK or API version. It is not evidence for the P400, V400m, E285 or another reader, and does not establish current availability, certification, whole-deployment PCI compliance, account/payment-method enablement, pairing, online state, production readiness, or any payment, settlement or funding outcome. The documented action is a hardware/customization review and engineering handoff, not transaction processing.

Locators: source lines 12–29; raw identity/scope lines 1–21; kit/accessories lines 24–31; specifications lines 34–44; entry modes/network lines 47–58; customization scope lines 61–63.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page centralizes M400 hardware facts and the custom idle-image request. For a fixed-stand installation, it marks the privacy shield as required for PCI compliance; that conditional accessory statement is not a complete PCI assessment. Captured WiFi scope is 2.4/5 GHz with WPA 1/2 PSK and CCMP (AES) or TKIP, with 5 GHz only recommended when available and subject to the merchant network. A custom image can target reader, location ID or gateway account, must meet the exact file constraints, and is handed to a PayPal Solutions Engineer or Integration Engineer with reader serial numbers or location IDs. The stated 12-hour-or-reboot refresh is not proof of completed configuration. Exact dimensions, formats, compression tips, identifiers and post-go-live support route remain in raw.

Locators: source lines 18–40; raw fixed-stand condition lines 27–31; WiFi values/qualification lines 53–58; image scope and file constraints lines 61–78; tips lines 83–92; upload, refresh and support steps lines 97–114.

## Position 46 — `in-person-hardware-verifone-p400`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:19` → `wiki/sources/braintree/source-braintree-in-person-hardware-verifone-p400.md` → `raw/braintree/in-person/hardware/verifone-p400-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 collected, unversioned Braintree In-Person hardware overview for the fixed-lane, tethered-power Verifone P400/P400 Plus kit: accessories, captured specifications and entry modes, WiFi/Ethernet support, and idle-screen customization. It names no SDK or API version and does not document Ethernet configuration, setup or pairing. It is not evidence for another reader and does not establish current availability, certification, whole-deployment PCI compliance, account/payment-method enablement, network reachability, reader-online state, production readiness, or a payment outcome. The separate setup authority is Dev Kit P400 and Sandbox-scoped; neither page proves production enablement.

Locators: source lines 12–30 and 43–47; raw identity/scope lines 1–21; kit/accessories lines 24–31; specifications lines 34–46; entry modes/network lines 51–62; supporting setup source lines 12–27 and setup raw lines 14–16, 211–239, 255–265.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central purpose is P400 hardware orientation plus the idle-image request workflow. The privacy shield is marked required for PCI compliance only when installed on a fixed stand. Captured WiFi scope is 2.4/5 GHz with WPA 1/2 PSK and CCMP (AES) or TKIP, with a merchant-network-qualified 5 GHz recommendation; listing Ethernet as connectivity is not Ethernet configuration or reachability proof. A custom image can target reader, location ID or gateway account, must meet the exact file constraints, and is handed to a PayPal Solutions Engineer or Integration Engineer. The stated 12-hour-or-reboot refresh is not proof of completed configuration. Exact dimensions, formats, tips, identifiers and post-go-live support route remain in raw.

Locators: source lines 18–41; raw fixed-stand condition lines 27–31; WiFi values/qualification lines 57–62; image scope/constraints lines 65–82; tips lines 87–96; upload, refresh and support steps lines 101–118.

## Position 47 — `docs-guides-fastlane-overview`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/paypal-fastlane.md:91` → `wiki/sources/braintree/source-braintree-docs-guides-fastlane-overview.md` → `raw/braintree/docs/guides/fastlane/overview-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned Braintree website overview of PayPal Fastlane as an autofill checkout solution for manually entered payment information on merchant responsive web checkout. It describes saved/retrieved card and shipping data, existing-profile payment/billing retrieval, non-accelerated guests, and accelerated users identified and authenticated through an existing PayPal or Fastlane account while stating Fastlane profiles are separate from PayPal accounts. It pins no SDK/package/API version and excludes native apps in the captured requirements. It is not current country/merchant/buyer eligibility, account enablement, authentication/profile retrieval, card acceptance, exact-version SDK or GitHub behavior, PCI assessment, Vault behavior, payment execution, authorization, settlement or funding proof; sample repositories are unread navigation.

Locators: source lines 12–25; raw purpose line 16; availability lines 17–69; integration scope lines 72–82; user/profile distinctions lines 85–102; sample navigation lines 105–111.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page's central purpose is Fastlane product orientation and integration gating. Its captured conditions are responsive desktop/mobile web, compatibility with an existing server SDK integration, card processing through Braintree, PayPal shown in-cart or alongside the Fastlane email field, billing-address collection, and the merchant domain included when generating the Braintree client token; omission prevents full functionality. Profile recognition is not authentication or payment success. The exact country matrix is snapshot-only. Production and Sandbox profile sites are distinct; `111111` and Braintree testing cards are expressly Sandbox fixtures. Developer feature/card-brand statements are unversioned summaries, not guarantees of present behavior or enablement. Exact countries, conditions, fixtures and feature text remain in raw.

Locators: source lines 18–35; raw country matrix lines 17–69; requirements lines 72–82; profile behavior lines 85–102; feature claims lines 114–124.

## Position 48 — `in-person-post-launch-activities-network-connection-test`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md` provider catalog → **deferred missing edge** → `wiki/concepts/braintree-in-person.md:17` → `wiki/sources/braintree/source-braintree-in-person-post-launch-activities-network-connection-test.md` → `raw/braintree/in-person/post-launch-activities/network-connection-test-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 collected, unversioned Braintree In-Person reader-admin network-diagnostic guide, stated for firmware 5.1.0 and newer. Its action is to open the reader admin menu, authenticate and run diagnostics for Braintree endpoints, outside-internet access, a speed check and time-server access. It names no SDK or API version. Test-device password `123456` is not the production credential, some tests depend on pairing to a Location ID, and the pictured E285 result is an example. It is not evidence of current firmware/support, a result from a specific device/network, uniquely diagnosed root cause, reader health/readiness, pairing, or any transaction, authorization, payment, settlement or funding outcome.

Locators: source lines 12–30; raw identity/version lines 1–19; admin action and credential scope lines 22–31; example/states/pairing condition lines 35–47.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page explains how to start and interpret four diagnostic state families. Endpoint checks cover the Braintree Public API, Reader API and Websocket API, with URL parsing, DNS, TCP and server-error stages; a TCP failure has several possible causes and is not a unique diagnosis. The network check uses ICMP and DNS. Speed can be Failed when internet is unavailable or Unavailable when unpaired, but the snapshot publishes no latency value, unit, threshold or requirement. The Time Server failure is described as blocked NTP preventing date/time retrieval and routes to firewall/domain configuration. Exact endpoints, state meanings, test steps and failure explanations remain in raw; support, allowlist and troubleshooting links remain separate navigation unless read.

Locators: source lines 18–40; raw endpoint checks lines 52–69; internet/network checks lines 72–86; speed states/steps lines 89–99; time-server condition line 102–105.

## Deferred aggregate closure — separate from content failures

- All four source pages have reciprocal entries in their main concepts, but `wiki/braintree-index.md` does not yet list the four promoted sources.
- `wiki/braintree-index.md` does not yet link either `[[braintree-in-person]]` or `[[paypal-fastlane]]`, so each provider-index-to-concept route is incomplete until coordinator close.
- Company/source-count and other shared catalog/log/count updates remain coordinator-owned close work. No new concept is required. These missing aggregate edges do not change the **8 PASS / 0 FAIL** content result.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: add/check the four Braintree source-catalog entries, both provider-index concept edges, and the deferred company/count/log aggregates.
- Handoff UTC: `2026-10-06T15:40:32Z`
