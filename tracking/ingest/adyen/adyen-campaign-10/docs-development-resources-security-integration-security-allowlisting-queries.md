# Adyen network allowlisting retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Is an IP allowlist required for every Adyen integration, and does this snapshot prove current endpoint connectivity or live-region IP coverage?

**Expected route:** `[[adyen-index]]` → `[[adyen-api-access]]` → `[[source-adyen-docs-development-resources-security-integration-security-allowlisting]]`; pinned raw `# Allowlisting IP addresses` lines 15–21, `## Requirements` lines 23–29, and `## Overview of allowlisting implementations` lines 31–42.

**Expected answer:** The guidance applies to all integration types if network allowlisting is used or planned. The page explicitly says unrestricted outbound requests are compatible with Adyen; an allowlist is a local security-policy choice. It compares DNS/domain rules with static-IP and custom-DNS approaches. Its collected CIDRs and DNS advice are snapshot guidance, not proof of current IP inventory, test/live or region coverage, a correctly configured firewall, or successful API/webhook delivery.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which addresses and DNS method apply to merchant-to-Adyen requests versus Adyen-to-merchant webhooks, and what rotation, SNI, and regional-firewall risks matter?

**Expected route:** Same source; raw `## DNS resolution and domain-based allowlist` lines 44–55, `## DNS resolution and IP allowlist` lines 57–63, `## Custom DNS record` lines 65–72, `## Hardcoded IP addresses` lines 74–78, `### Outgoing IP allowlisting (from you to Adyen)` lines 84–100, `### Incoming IP allowlisting (from Adyen to you)` lines 102–116, and `### Geo-IP-based firewalls and regional blocking` lines 118–124.

**Expected answer:** For merchant outbound calls, resolve Adyen endpoint DNS and prefer domain-based rules; the page names `adyen.com` and `adyenpayments.com`, lists a dated endpoint CIDR set, and says to keep DNS authoritative. Static IP lists can become stale, custom DNS/proxies can send a mismatched SNI, and hardcoded IPs can fail after rotation. For inbound Adyen webhook traffic, resolve Adyen's current outbound source addresses through `out.adyen.com` if the merchant firewall restricts inbound traffic. These opposite directions should not be conflated. Geo-IP mapping may incorrectly block connections, so the page advises an explicit Adyen domain/range exception.
