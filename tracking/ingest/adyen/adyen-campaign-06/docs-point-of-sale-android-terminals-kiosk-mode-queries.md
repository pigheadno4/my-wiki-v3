# Fixed answers: Android terminal kiosk mode

## Query 1 — Which Adyen terminals and Customer Area roles does the kiosk-mode guide cover, and how is it configured?

**Answer:** In this dated guide, kiosk mode can be enabled on Android models **AMS1, S1E2L, S1E, S1E4Pro, S1F2, S1F4Pro, and S1U2**; the guide separately says **P630** has it enabled by default. It applies to a Terminal API integration or standalone solution. In Customer Area, **Merchant POS Terminal Management Admin** can configure at any level, while **Merchant POS Terminal Management** is scoped to the merchant account and lower. Under **Devices > Device settings > Device**, select an already uploaded Android app as **Default start app**, enable **Hide navigation bar**, optionally select other **Apps allowed in kiosk mode**, turn off the Home screen **Settings menu** and **Transactions menu**, and save.

**Prerequisites and warnings:** The app must already be uploaded for default-app selection. This page does not say that saving the setting uploads or installs it, or give a software-version minimum. The model list is a 2025-08-06 page modification captured 2026-09-15; check current device, region and account support before rollout. The guide does not prove a kiosk configuration has reached a particular terminal.

**Retrieval route:** [[source-adyen-docs-point-of-sale-android-terminals-kiosk-mode]] → [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Requirements|Requirements]] and [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Enable kiosk mode|Enable kiosk mode]]. Catalog promotion is pending.

## Query 2 — Does kiosk mode give a secure lock or a documented passcode method to exit?

**Answer:** The guide says kiosk mode hides the navigation bar and the Settings and Transactions buttons at the bottom of the screen, preventing customers from using **those screen controls** to change or minimize the default app or power off the terminal. It does **not** document a kiosk exit procedure, an exit passcode/PIN rule, or a claim that every other hardware or software control is blocked. Its configuration is a Customer Area UI setting, so the guide alone does not establish tamper resistance, complete lockdown, or successful unattended payment operation.

**Prerequisites and warnings:** Keep a separate operational recovery procedure and verify the current terminal/menu documentation before relying on kiosk mode for unattended use. Customer Area roles govern the documented setting change; do not infer they describe on-device exit access. P630's default-enabled statement is a snapshot, not proof of a particular deployed P630's state.

**Retrieval route:** [[source-adyen-docs-point-of-sale-android-terminals-kiosk-mode]] → [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Kiosk mode|Kiosk mode]], [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Requirements|Requirements]], and [[raw/adyen/docs/point-of-sale/android-terminals/kiosk-mode/2026-09-15#Enable kiosk mode|Enable kiosk mode]]. Catalog promotion is pending.
