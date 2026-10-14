# Fixed retrieval checks: endless aisle

1. **Question:** Does an in-store ecommerce order in Adyen's endless-aisle guide always use a terminal, and what does the POS-system option need to handle?
   **Expected answer:** No. Three listed setups send Terminal API requests from a tablet or POS system to dedicated, shared or existing terminals. The POS-system/existing-terminal option must combine POS and ecommerce flows and collect delivery details. A separate tablet Pay by Link API option needs no terminal and may require fraud rules and 3D Secure. The page does not choose an architecture or specify a shared order/capture API. Source: pinned raw `## Technical setup`, `### App or web interface` (2026-09-15 snapshot).

2. **Question:** Can a terminal used for an endless-aisle sale in a Dutch physical store be assigned to a British ecommerce legal entity?
   **Expected answer:** The guide says no in its British-entity/Dutch-store example: a transaction using a terminal is classified as card-present POS, and the terminal must be assigned to a merchant account under a legal entity registered where the physical store is located. The example does not establish the ecommerce order's seller/MOR or extend the same terminal rule to the no-terminal Pay by Link option. Source: pinned raw `## Compliance requirements` (2026-09-15 snapshot).
