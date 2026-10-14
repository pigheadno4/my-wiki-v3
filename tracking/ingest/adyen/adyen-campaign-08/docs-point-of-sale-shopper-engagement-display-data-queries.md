# Fixed retrieval checks: terminal display overview

1. **Question:** If a terminal shows a loyalty QR code from the display-data overview, has the shopper enrolled or paid?
   **Expected answer:** No. The overview describes an out-of-payment display request that can show a QR code for the shopper to scan, with a loyalty URL as an example. It does not report scanning, enrollment, consent or payment completion. The QR child guide is the route for implementation detail. Source: pinned raw opening and `## What do you want to show?` (2026-09-15 snapshot).

2. **Question:** Which display purposes does this overview route to, and does it define receipt printing or timeout behavior?
   **Expected answer:** It routes to QR code, virtual receipt preview, image and standby/idle display. The virtual receipt is a terminal-screen preview; this overview does not define physical printing, Terminal API request fields, model support, acknowledgment or timeout behavior. The individual child guides are needed for those mechanics. Source: pinned raw opening four-item list and `## What do you want to show?` (2026-09-15 snapshot).
