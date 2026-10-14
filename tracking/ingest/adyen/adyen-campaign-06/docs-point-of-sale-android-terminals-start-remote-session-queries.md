# Fixed retrieval checks — Android terminal remote troubleshooting

## Query 1: Who starts an Adyen Android terminal remote session, and when can the Customer Area user interact with the screen?

**Purpose and scope:** This is a 2026-09-15 capture of a Customer Area remote troubleshooting procedure for Android payment terminals. The session is intended to duplicate the terminal screen so a Customer Area user can interact with menus and Android apps for support/configuration.

**Capability and prerequisites:** The Customer Area user selects a terminal under Devices > Device list and requests `Start remote session`; a one-time passcode appears there. A person physically operating the terminal must select `Start session` on that device and enter the code. The guide then says the duplicate screen appears in Customer Area. Either side can end the session; a later session requires fresh one-time-password authentication. The requirements table also calls for enabled WebSockets, applicable Customer Area POS terminal roles and qualifying Android terminal software.

**Warnings and do not infer:** A request or one-time code alone does not prove terminal-side acceptance or actual screen access. The source does not evidence a specific merchant's permissions, an active session, completed settings change or payment outcome. The raw role cell has ambiguous punctuation between Management Admin and Support roles, so verify the current role requirement rather than assuming both or one suffice.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-android-terminals]] → [[source-adyen-docs-point-of-sale-android-terminals-start-remote-session]] → `[[raw/adyen/docs/point-of-sale/android-terminals/start-remote-session/2026-09-15]]`, especially raw lines 19–33 and 46–58. The C06 source/index link awaits coordinator promotion.

## Query 2: What device, software, network and security conditions does the remote-session guide list?

**Purpose and scope:** The dated guide's Requirements and Allowlisting sections describe conditions for Android payment-terminal remote troubleshooting, not a current network policy or account-specific authorization.

**Capability and prerequisites:** The requirements table names Terminal API integration with payment terminals or standalone use, Android payment-terminal hardware, Customer Area POS terminal roles, and WebSockets enabled. It specifies Verifone Android M450/P360 at software 1.115+ and other models at 1.105.2+. Depending on network/security requirements, firewall allowlisting may be necessary; the page recommends DNS resolution and domain-based allowlisting. A terminal operator must participate with a one-time code.

**Warnings and do not infer:** The listed URL, IP address and ports are historical snapshot values, not confirmed current firewall targets. The role-row formatting does not resolve whether both named roles or one role is required. Do not infer support for every device, software build or region, or remote access to an unattended terminal. Start/end controls and one-time authentication do not prove a session or payment occurred.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-android-terminals]] → [[source-adyen-docs-point-of-sale-android-terminals-start-remote-session]] → raw lines 23–44 under `## Requirements` and `## Allowlisting`, plus 46–58 for session control. The linked current user-role, cloud-connection and allowlisting guides require separate reading.
