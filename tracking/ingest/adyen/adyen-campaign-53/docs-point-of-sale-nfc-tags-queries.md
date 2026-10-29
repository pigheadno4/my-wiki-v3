# Fixed retrieval checks — docs-point-of-sale-nfc-tags

Canonical URL: https://docs.adyen.com/point-of-sale/nfc-tags
Expected source stem: source-adyen-docs-point-of-sale-nfc-tags
Pinned raw: raw/adyen/docs/point-of-sale/nfc-tags/2026-09-15.md

## Q1

**Question:** Which Adyen POS NFC tag operations and device prerequisites does this guide cover, and does a successful tag acquisition authorize a payment?

**Expected answer:** Route through [[adyen]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-nfc-tags]]. The guide covers CardAcquisition NFCReadUID, tag-specific NFCRead/NFCWrite, Ultralight AES counters, sessions, and optional UI hiding. A compatible Terminal API terminal/tag and Support NFC configuration are required; the requirements call DESFire writing and Ultralight memory operations Android-only, while the support matrix marks several Engage terminals Ultralight-capable, and the Engage Ultralight C note permits only unlocked pages. The matrix does not guarantee a specific operation; verify the exact tag variant, read/write operation, terminal model, and installed software with Adyen. Counters require Ultralight AES on Android software 134+, and UI hiding is limited to listed models/software with a dedicated Android app. A successful acquisition or displayed green icon is an NFC interaction result, not payment authorization. Evidence: raw/adyen/docs/point-of-sale/nfc-tags/2026-09-15.md lines 30–45, 64–77, 2165–2175, 1390–1395, 2091–2102, 2141–2182; general acquisition/payment distinction in [[source-adyen-docs-point-of-sale-card-acquisition]].

## Q2

**Question:** How should an NFC tag operation be closed, and what data/result cautions matter for Ultralight reads, counters, and a regular payment card in a hidden-UI flow?

**Expected answer:** Route to [[source-adyen-docs-point-of-sale-nfc-tags]] and its pinned raw. After the card-acquisition operation or final Session.Type End, send EnableService/AbortTransaction to stop the loading screen; an optional DisplayOutput icon is presentation only. Ultralight READ returns four pages/16 bytes, potentially including data beyond a smaller requested range. Counter writes increment but cannot set/decrease a total, and the write response's NFC.data is the increment rather than new total; counter/page operations are separate. In a configured hidden-UI NFC app, BLOCK_CARD means a regular payment card is unusable for that app, not that the card itself is blocked. Preserve raw conflicts: Session.Timeout versus TimeoutMs and AdditionalResponse Base64/JSON prose versus URL-style examples. Evidence: raw/adyen/docs/point-of-sale/nfc-tags/2026-09-15.md lines 713–728, 1597–1619, 1704–1709, 1800–1815, 1833–1845, 2054–2066, 2091–2102.
