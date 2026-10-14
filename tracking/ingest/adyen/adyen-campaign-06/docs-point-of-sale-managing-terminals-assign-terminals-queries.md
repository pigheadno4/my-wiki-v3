# Fixed answers: assign terminals through Customer Area

## Query 1 — Is a terminal ready to take payments as soon as it is assigned to a store in Customer Area?

**Answer:** The guide says a terminal must be assigned to a store, or a merchant account representing a store, **and then physically boarded**. Shipped terminals first enter the company account's Inventory. A Customer Area user with **Merchant POS Terminal Management Admin** or **Manage terminals** role can find the serial number under **Devices > Device list > Terminals**, select a store, and confirm reassignment. The same control can send a store terminal back to Inventory. A test terminal uses the test Customer Area; a live terminal uses the live Customer Area. Assignment alone does not establish that the terminal has boarded, received the store configuration, or completed a payment.

**Prerequisites and warnings:** The page applies to Terminal API or standalone terminals. For large sets, Customer Area provides a CSV **Bulk reassignment** flow, with file structure and example downloaded there; this source does not define the CSV schema. The page links separate Management API assignment and on-device selection/boarding procedures. Check the actual device state before treating it as ready.

**Retrieval route:** [[source-adyen-docs-point-of-sale-managing-terminals-assign-terminals]] → [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Requirements|Requirements]], [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Assign a terminal from your Customer Area|Assign a terminal from your Customer Area]], and [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Assign terminals in bulk|Assign terminals in bulk]]. Catalog promotion is pending.

## Query 2 — What happens when a boarded terminal is reassigned to a different store, and when is the new configuration active?

**Answer:** A boarded terminal continues using its **old store's configuration** until it synchronizes with Adyen. It then removes that configuration and shows **Board the terminal**; staff board it again to collect the new store configuration. The terminal needs power and a stable internet connection. The guide says reassignment can take **up to three hours**, reflecting its three-hour synchronization interval. It points to enabling WebSockets **before** reassignment or, for **non-Android** terminals, manually updating configuration to accelerate the change. These are conditional instructions, not a promise that a particular device changes immediately.

**Prerequisites and warnings:** Use the appropriate Customer Area role and test/live environment. Confirm the terminal's displayed boarding state after reassignment; a Customer Area selection or CSV submission is not proof of a completed transition. The guide does not define how a live payment is routed while the device still has the old configuration, so do not infer new-store payment processing from assignment alone.

**Retrieval route:** [[source-adyen-docs-point-of-sale-managing-terminals-assign-terminals]] → [[raw/adyen/docs/point-of-sale/managing-terminals/assign-terminals/2026-09-15#Reassign boarded terminals|Reassign boarded terminals]]. Catalog promotion is pending.
