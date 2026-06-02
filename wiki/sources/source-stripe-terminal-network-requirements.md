---
title: "Stripe Terminal: Terminal Network Requirements"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-network-requirements-2025.md"
tags: [stripe, terminal, in-person, network, wifi, ethernet, ipv4, dns, troubleshooting, browser]
---

## Stripe Terminal: Terminal Network Requirements

Network requirements for mobile readers and smart readers, plus troubleshooting guide.

## Key Takeaways

### Mobile readers (M2, WisePad 3)

- POS device must have internet access to Stripe's infrastructure
- 2.4GHz Bluetooth interference (e.g., microwaves) can disrupt connection

### Smart reader network requirements

- **IPv4 required** — IPv6-only networks not supported; mixed IPv4/IPv6 works only if IPv4 address assigned
- Private IP address required (not public)
- **WiFi and Ethernet simultaneously = unstable** — use one or the other
- **WiFi 6 (802.11ax) not supported**
- WiFi encryption: WPA/WPA2/WPA3-Personal or WPA2/WPA3 EAP-PEAP Enterprise; must be password-protected
  - Verifone P400: only WPA-Personal or WPA2-Personal
- Ethernet: 10/100 only
- DHCP: readers must retain same IP for at least one full workday
- Session length: minimum one full workday (including idle sessions)

### SDK + smart reader (separate POS device) additional requirements

- Reader and POS device must be on the **same local network**
- Devices must be able to communicate **directly** (no WiFi-to-Ethernet client isolation)
- POS device DNS must resolve internet-routable hostnames to local IP addresses

### DNS troubleshooting test

Resolve `10-42-42-42.test.device.stripe-terminal-local-reader.net` — it should return `10.42.42.42`. If not, switch POS device DNS to:
- Cloudflare: `1.1.1.1` and `1.0.0.1`
- Google: `8.8.8.8` and `8.8.4.4`

### Browser local network access (JS SDK)

- Chrome 142+: explicit permission required per site → Site Settings → Local Network → Allow
- macOS Chrome bug: if permission granted but still blocked, delete `com.apple.networkextension.plist` in Recovery mode
- Firefox: similar LNA restrictions; see Firefox support docs
- macOS: confirm browser listed under System Settings → Privacy & Security → Local Network
- Extensions: test in incognito to rule out extension interference

### Troubleshooting methodology

1. Test on a different network (mobile hotspot) to isolate network vs. code issue
2. If network-specific: check firewall, try Ethernet vs WiFi, check WiFi signal strength, ping reader IP, check router WiFi↔Ethernet isolation setting

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-network-requirements-2025]] — verbatim Terminal network requirements and troubleshooting guide
