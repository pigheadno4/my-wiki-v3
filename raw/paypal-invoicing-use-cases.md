<!-- Source URL: https://docs.paypal.ai/growth/grow-business/invoicing/use-cases -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use cases

Explore key ways to apply the PayPal Invoicing API in your billing and payment collection flows. See how different configuration options map to common business scenarios so you can choose the pattern that best fits your integration.

Select a use case that fits your integration:

- [Create a draft invoice with minimum required fields](#create-a-draft-invoice-with-minimum-required-fields)
- [Create a payment request linked to an external invoice](#create-a-payment-request-linked-to-an-external-invoice)
- [Create an hourly services invoice](#create-an-hourly-services-invoice)
- [Create an invoice for shippable goods](#create-an-invoice-for-shippable-goods)
- [Create an invoice for digital goods](#create-an-invoice-for-digital-goods)
- [Create a mixed billing invoice](#create-a-mixed-billing-invoice)

For more information, see the [API reference](/reference/api/rest/invoices/list-invoices).

## Prerequisites

- [PayPal business account](https://www.paypal.com/business/open-business-account?_ga=2.49411041.673139926.1760916697-1259758161.1760473483) with Invoicing enabled.
- Obtain your sandbox credentials and access token. Refer to [Get Started with PayPal REST APIs](https://docs.paypal.ai/developer/how-to/api/get-started) for more information.
- (Optional) Use a test email you can access, not your PayPal business email.

## Use cases

See how to create invoices that address common scenarios and requirements.

### Create a draft invoice with minimum required fields

This is a good starting point for merchants new to the API or developers testing an integration before adding complexity.

1. Call `POST /v2/invoicing/invoices` with minimal required fields.
2. Save the `id` from the `201 Created` response.
3. Call `POST /v2/invoicing/invoices/{id}/send` to deliver the invoice to the recipient.

| Field                           | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| `detail.invoice_number`         | Your reference number for the invoice.                       |
| `detail.currency_code`          | Currency applied to all monetary values.                     |
| `detail.payment_term.term_type` | When payment is due, such as `DUE_ON_RECEIPT`.               |
| `invoicer`                      | Sender name and email.                                       |
| `primary_recipients`            | Customer name and email.                                     |
| `items`                         | At least one line item with name, quantity, and unit amount. |

**Request**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "INV-001",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "payment_term": {
      "term_type": "DUE_ON_RECEIPT"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Alex",
      "surname": "Rivera"
    },
    "email_address": "alex@example.com",
    "business_name": "Rivera Consulting"
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Jamie",
          "surname": "Lee"
        },
        "email_address": "jamie.lee@example.com"
      }
    }
  ],
  "items": [
    {
      "name": "Consulting Services",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "500.00"
      },
      "unit_of_measure": "QUANTITY"
    }
  ]
}
```

A successful call returns HTTP `201 Created`. Save the returned `id` — you need it to send, update, or query the invoice.

> **Note:** This creates a `DRAFT` invoice. The customer isn't notified until you call `POST /v2/invoicing/invoices/{id}/send`.

### Create a payment request linked to an external invoice

This pattern is ideal for merchants using a enterprise resource planning (ERP) or accounting platforms like NetSuite, QuickBooks, or Xero who want to collect payment through PayPal without recreating the invoice. Pass the external reference via `invoice_number` or `detail.reference`, and optionally attach the original invoice PDF.

1. Create the invoice in your external system and capture the external invoice ID.
2. Call `POST /v2/invoicing/invoices` to create a PayPal payment request, passing the external invoice ID and optionally attaching the original invoice PDF.
3. Call `POST /v2/invoicing/invoices/{id}/send` to deliver the payment request to the customer.
4. The customer receives a PayPal-hosted payment link by email and pays using PayPal or a card.

| Field                               | Description                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| `items[].unit_of_measure: "AMOUNT"` | Flat-rate billing with no quantity or hourly breakdown.       |
| `attachments`                       | Attach the original invoice PDF for the customer's reference. |

**Request — External ID as `invoice_number`**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "NETSUITE-INV-78432",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Please use the link below to pay your outstanding invoice. The original invoice is attached for your reference.",
    "payment_term": {
      "term_type": "DUE_ON_RECEIPT"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Morgan",
      "surname": "Shaw"
    },
    "email_address": "billing@apexsupply.com",
    "business_name": "Apex Supply Co."
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Dana",
          "surname": "Patel"
        },
        "email_address": "dana.patel@clientcorp.com"
      }
    }
  ],
  "items": [
    {
      "name": "Invoice NETSUITE-INV-78432",
      "description": "Payment for goods and services per attached invoice.",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "3450.00"
      },
      "unit_of_measure": "AMOUNT"
    }
  ],
  "attachments": [
    {
      "name": "Invoice-NETSUITE-INV-78432.pdf",
      "url": "https://your-storage.example.com/invoices/NETSUITE-INV-78432.pdf"
    }
  ]
}
```

**Request — External ID as `detail.reference`**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "PAY-2026-00142",
    "reference": "NETSUITE-INV-78432",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Please use the link below to pay invoice NETSUITE-INV-78432. The original invoice is attached for your reference.",
    "payment_term": {
      "term_type": "DUE_ON_RECEIPT"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Morgan",
      "surname": "Shaw"
    },
    "email_address": "billing@apexsupply.com",
    "business_name": "Apex Supply Co."
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Dana",
          "surname": "Patel"
        },
        "email_address": "dana.patel@clientcorp.com"
      }
    }
  ],
  "items": [
    {
      "name": "Invoice NETSUITE-INV-78432",
      "description": "Payment for goods and services per attached invoice.",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "3450.00"
      },
      "unit_of_measure": "AMOUNT"
    }
  ],
  "attachments": [
    {
      "name": "Invoice-NETSUITE-INV-78432.pdf",
      "url": "https://your-storage.example.com/invoices/NETSUITE-INV-78432.pdf"
    }
  ]
}
```

**Notes**

- Use `unit_of_measure: "AMOUNT"` when billing a flat total with no quantity or hourly breakdown.
- The `attachments` array accepts publicly accessible URLs. The PDF must be reachable by PayPal's servers at the time you create the invoice.
- `detail.reference` is visible to the customer on the PayPal invoice page. This is useful for cross-referencing the external invoice number.
- `detail.memo` is a private field visible only to the invoicer. Use this for internal bookkeeping notes.

### Create an hourly services invoice

Create an hourly services invoice with `unit_of_measure: "HOURS"`, a client billing address, tip enabled, and partial payment configured for deposit workflows. This pattern works best for consultants, freelancers, photographers, and tradespeople billing for time and labor.

1. Confirm the scope, hours, and rate for completed service work.
2. Call `POST /v2/invoicing/invoices` with hourly or amount-based line items and the client's billing address. Don't include `shipping_info`.
3. Call `POST /v2/invoicing/invoices/{id}/send` to deliver the invoice to the client.
4. The client receives the invoice and pays with PayPal or card.

| Field                                       | Description                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------------- |
| `items[].unit_of_measure: "HOURS"`          | Renders quantity as hours worked and `unit_amount` as the hourly rate.       |
| `primary_recipients[].billing_info.address` | Client billing address; no `shipping_info` included.                         |
| `detail.payment_term.term_type`             | When payment is due, such as `NET_14` or `NET_30`.                           |
| `detail.note`                               | Project summary or message visible to the client.                            |
| `detail.term`                               | Formal payment terms and conditions.                                         |
| `configuration.allow_tip: true`             | Enables an optional tip or gratuity field on the PayPal-hosted payment page. |
| `configuration.partial_payment`             | Supports deposit or installment payment workflows.                           |

**Request**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "INV-2026-0089",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Thank you for working with us. Please don't hesitate to reach out with any questions.",
    "term": "Payment due within 14 days of invoice date. Late payments subject to a 1.5% monthly fee.",
    "payment_term": {
      "term_type": "NET_14"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Taylor",
      "surname": "Brooks"
    },
    "email_address": "taylor@brooksdesign.com",
    "business_name": "Brooks Design Studio",
    "phones": [
      {
        "country_code": "1",
        "national_number": "4155550192",
        "phone_type": "MOBILE"
      }
    ],
    "website": "https://brooksdesign.com"
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Jordan",
          "surname": "Kim"
        },
        "business_name": "Kim & Associates LLC",
        "email_address": "jordan@kimassociates.com",
        "address": {
          "address_line_1": "450 Market Street",
          "address_line_2": "Suite 800",
          "admin_area_2": "San Francisco",
          "admin_area_1": "CA",
          "postal_code": "94105",
          "country_code": "US"
        }
      }
    }
  ],
  "items": [
    {
      "name": "UX Design — Discovery & Research",
      "description": "User interviews, competitive analysis, journey mapping",
      "quantity": "12",
      "unit_amount": {
        "currency_code": "USD",
        "value": "150.00"
      },
      "unit_of_measure": "HOURS",
      "tax": {
        "name": "Sales Tax",
        "percent": "8.5"
      }
    },
    {
      "name": "UX Design — Wireframing & Prototyping",
      "description": "Low and high-fidelity wireframes, interactive prototype",
      "quantity": "18",
      "unit_amount": {
        "currency_code": "USD",
        "value": "150.00"
      },
      "unit_of_measure": "HOURS",
      "tax": {
        "name": "Sales Tax",
        "percent": "8.5"
      }
    }
  ],
  "configuration": {
    "allow_tip": true,
    "partial_payment": {
      "allow_partial_payment": true,
      "minimum_amount_due": {
        "currency_code": "USD",
        "value": "500.00"
      }
    },
    "tax_calculated_after_discount": true,
    "tax_inclusive": false
  }
}
```

**Notes**

- `unit_of_measure: "HOURS"` renders quantity as hours and `unit_amount` as the hourly rate on both the invoice and the customer-facing payment page.
- Omitting `shipping_info` from `primary_recipients` indicates a non-shippable, services-based invoice. Only `billing_info` is required.
- `allow_tip: true` renders an optional tip or gratuity field on the PayPal-hosted payment page — no additional API calls required. Use this for service businesses where tipping is customary, such as trades, personal care, event services, or photography. Set `allow_tip: false` for B2B or formal invoicing contexts.
- `allow_partial_payment: true` with a `minimum_amount_due` supports deposit-first or installment workflows common in service businesses.
- Use `unit_of_measure: "AMOUNT"` instead of `"HOURS"` if you're billing a flat project fee rather than hourly.
- To record a payment received outside of PayPal, such as by check or bank transfer, use `POST /v2/invoicing/invoices/{id}/payments`.

### Create an invoice for shippable goods

Create a physical goods invoice with quantity-based line items, separate billing and shipping addresses, a shipping charge, and shipping-specific tax. This pattern works best for e-commerce sellers, wholesalers, and distributors shipping physical products.

1. Confirm the products, quantities, and shipping details from the order in your system.
2. Call `POST /v2/invoicing/invoices` with quantity-based line items, a shipping address, and a shipping charge.
3. Call `POST /v2/invoicing/invoices/{id}/send` to deliver the invoice.
4. The buyer pays via PayPal or card; fulfill and ship the order.

| Field                                 | Description                                                               |
| ------------------------------------- | ------------------------------------------------------------------------- |
| `primary_recipients[].shipping_info`  | Buyer's shipping address. This can differ from billing address.           |
| `primary_recipients[].billing_info`   | Buyer's billing address.                                                  |
| `items[].unit_of_measure: "QUANTITY"` | Unit-based billing for physical goods.                                    |
| `amount.breakdown.shipping.amount`    | Flat shipping charge.                                                     |
| `amount.breakdown.shipping.tax`       | Tax applied specifically to the shipping charge.                          |
| `items[].tax`                         | Per-line sales tax on individual goods.                                   |
| `detail.reference`                    | Purchase order or order reference number. This value is customer-visible. |

**Request**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "INV-2026-ORD-4421",
    "reference": "PO-CLIENT-4421",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Thank you for your order! Your items will ship within 2 business days.",
    "term": "All goods remain the property of Apex Supply Co. until payment is received in full.",
    "payment_term": {
      "term_type": "DUE_ON_RECEIPT"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Casey",
      "surname": "Nguyen"
    },
    "email_address": "orders@apexsupply.com",
    "business_name": "Apex Supply Co.",
    "address": {
      "address_line_1": "800 Industrial Blvd",
      "admin_area_2": "Austin",
      "admin_area_1": "TX",
      "postal_code": "78701",
      "country_code": "US"
    }
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Sam",
          "surname": "Torres"
        },
        "business_name": "Torres Hardware Inc.",
        "email_address": "sam@torreshardware.com",
        "address": {
          "address_line_1": "220 Commerce Drive",
          "admin_area_2": "Chicago",
          "admin_area_1": "IL",
          "postal_code": "60601",
          "country_code": "US"
        }
      },
      "shipping_info": {
        "name": {
          "given_name": "Sam",
          "surname": "Torres"
        },
        "address": {
          "address_line_1": "500 Warehouse Road",
          "admin_area_2": "Chicago",
          "admin_area_1": "IL",
          "postal_code": "60607",
          "country_code": "US"
        }
      }
    }
  ],
  "items": [
    {
      "name": "Heavy-Duty Work Gloves",
      "description": "Model HG-200, Size L, Black",
      "quantity": "24",
      "unit_amount": {
        "currency_code": "USD",
        "value": "12.99"
      },
      "unit_of_measure": "QUANTITY",
      "tax": {
        "name": "Sales Tax",
        "percent": "8.25"
      }
    },
    {
      "name": "Safety Goggles",
      "description": "Model SG-500, Anti-fog, Clear lens",
      "quantity": "12",
      "unit_amount": {
        "currency_code": "USD",
        "value": "18.50"
      },
      "unit_of_measure": "QUANTITY",
      "tax": {
        "name": "Sales Tax",
        "percent": "8.25"
      }
    }
  ],
  "configuration": {
    "allow_tip": false,
    "partial_payment": {
      "allow_partial_payment": false
    },
    "tax_calculated_after_discount": false,
    "tax_inclusive": false
  },
  "amount": {
    "breakdown": {
      "shipping": {
        "amount": {
          "currency_code": "USD",
          "value": "18.00"
        },
        "tax": {
          "name": "Shipping Tax",
          "percent": "8.25"
        }
      }
    }
  }
}
```

**Notes**

- `shipping_info` and `billing_info` can have different addresses — PayPal renders both on the invoice and buyer confirmation page.
- `unit_of_measure: "QUANTITY"` renders items as discrete units — the standard for physical goods.
- Shipping tax is defined separately in `amount.breakdown.shipping.tax` and is independent from line item taxes.
- `detail.reference` is customer-visible and useful for linking back to a purchase order or external order management reference.
- To record a payment received outside of PayPal, such as by check or bank transfer, use `POST /v2/invoicing/invoices/{id}/payments`.

### Create an invoice for digital goods

Create a digital goods invoice with unit and flat-rate line items and a billing address only — no shipping address or charges. This pattern works best for merchants selling software licenses, downloads, online courses, or other digital products.

1. Capture the order details for the digital product purchase in your system.
2. Call `POST /v2/invoicing/invoices` with digital line items and a billing address only. Don't include `shipping_info`.
3. Call `POST /v2/invoicing/invoices/{id}/send` to deliver the invoice.
4. The customer pays via PayPal or card; handle digital delivery separately.

| Field                                 | Description                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| `items[].unit_of_measure: "QUANTITY"` | Unit-based billing for seat or license-based products.                             |
| `items[].unit_of_measure: "AMOUNT"`   | Flat-rate billing for bundles or one-time packages.                                |
| `primary_recipients[].billing_info`   | Billing address only; no `shipping_info` included.                                 |
| `items[].tax`                         | Applicable sales tax. Digital goods tax rules vary by jurisdiction.                |
| `detail.note`                         | Delivery instructions or next-step guidance visible to the customer after payment. |

**Request**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "INV-2026-DIG-0028",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Your license keys and download links will be emailed within 24 hours of payment.",
    "payment_term": {
      "term_type": "DUE_ON_RECEIPT"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Riley",
      "surname": "Chen"
    },
    "email_address": "sales@stacktools.io",
    "business_name": "StackTools Inc.",
    "website": "https://stacktools.io"
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Avery",
          "surname": "Johnson"
        },
        "business_name": "Johnson Media Group",
        "email_address": "avery@johnsonmedia.com",
        "address": {
          "address_line_1": "1200 5th Avenue",
          "admin_area_2": "New York",
          "admin_area_1": "NY",
          "postal_code": "10001",
          "country_code": "US"
        }
      }
    }
  ],
  "items": [
    {
      "name": "StackTools Pro — Annual License",
      "description": "Single-seat annual license. Includes all features and priority support.",
      "quantity": "3",
      "unit_amount": {
        "currency_code": "USD",
        "value": "299.00"
      },
      "unit_of_measure": "QUANTITY",
      "tax": {
        "name": "Sales Tax",
        "percent": "8.875"
      }
    },
    {
      "name": "Onboarding & Setup Package",
      "description": "One-time onboarding session and configuration assistance.",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "149.00"
      },
      "unit_of_measure": "AMOUNT"
    }
  ],
  "configuration": {
    "allow_tip": false,
    "partial_payment": {
      "allow_partial_payment": false
    },
    "tax_calculated_after_discount": true,
    "tax_inclusive": false
  }
}
```

**Notes**

- Omitting `shipping_info` from `primary_recipients` signals that no physical delivery is required.
- Use `unit_of_measure: "QUANTITY"` for seat or unit-based products. Use `"AMOUNT"` for flat-rate bundles or packages where itemized quantity doesn't apply.
- Digital goods tax rules vary significantly by jurisdiction — consult your tax advisor for the correct rate based on customer location.
- Use `detail.note` to communicate delivery instructions or access information. This field is customer-visible on the PayPal invoice and payment confirmation page.

### Create a mixed billing invoice

Create an invoice that combines all three `unit_of_measure` types — `HOURS`, `QUANTITY`, and `AMOUNT` — in a single request, with an invoice-level discount and partial payment configuration. This pattern works best for agencies, consultancies, and IT services firms billing for a mix of time, deliverables, and flat fees within the same engagement.

> **Note:** This is an advanced use case that builds on the patterns above. If your business bills using only one line item type, refer to the appropriate use case.

1. Confirm time logs, deliverable counts, and agreed flat fees for the completed project work.
2. Call `POST /v2/invoicing/invoices` with mixed line items combining `HOURS`, `QUANTITY`, and `AMOUNT` types.
3. Review the draft, then call `POST /v2/invoicing/invoices/{id}/send`.
4. The client receives the invoice, reviews the itemized breakdown, and pays via PayPal or card.

| Field                                 | Description                                                             |
| ------------------------------------- | ----------------------------------------------------------------------- |
| `items[].unit_of_measure: "HOURS"`    | Billable time; quantity = hours worked, `unit_amount` = hourly rate.    |
| `items[].unit_of_measure: "QUANTITY"` | Discrete units; quantity = number of items, `unit_amount` = unit price. |
| `items[].unit_of_measure: "AMOUNT"`   | Flat-rate charge; quantity = `"1"`, `unit_amount` = total flat fee.     |
| `items[].discount`                    | Line item-level discount, such as percent or fixed amount.              |
| `amount.breakdown.discount`           | Invoice-level discount applied across all line items.                   |
| `configuration.partial_payment`       | Supports structured deposit and balance workflows.                      |
| `detail.memo`                         | Private internal note, not visible to the client.                       |

**Request**

```json [expandable] theme={null}
{
  "detail": {
    "invoice_number": "INV-2026-AGY-0047",
    "reference": "SOW-2026-003",
    "invoice_date": "2026-03-15",
    "currency_code": "USD",
    "note": "Thank you for partnering with us on this project. Please review the itemized breakdown below and don't hesitate to reach out with any questions.",
    "term": "Payment due within 30 days of invoice date. A late payment fee of 1.5% per month applies to overdue balances.",
    "memo": "Internal ref: Q1 closeout — Acct Manager: TJ — Client tier: Enterprise",
    "payment_term": {
      "term_type": "NET_30"
    }
  },
  "invoicer": {
    "name": {
      "given_name": "Priya",
      "surname": "Nair"
    },
    "email_address": "billing@northstaragency.com",
    "business_name": "North Star Agency LLC",
    "phones": [
      {
        "country_code": "1",
        "national_number": "6175550183",
        "phone_type": "WORK"
      }
    ],
    "website": "https://northstaragency.com",
    "address": {
      "address_line_1": "200 State Street",
      "address_line_2": "Floor 4",
      "admin_area_2": "Boston",
      "admin_area_1": "MA",
      "postal_code": "02109",
      "country_code": "US"
    }
  },
  "primary_recipients": [
    {
      "billing_info": {
        "name": {
          "given_name": "Marcus",
          "surname": "Webb"
        },
        "business_name": "Webb Enterprises Inc.",
        "email_address": "marcus.webb@webbenterprises.com",
        "address": {
          "address_line_1": "1 Financial Center",
          "admin_area_2": "Boston",
          "admin_area_1": "MA",
          "postal_code": "02111",
          "country_code": "US"
        }
      }
    }
  ],
  "items": [
    {
      "name": "Strategy & Discovery",
      "description": "Stakeholder interviews, competitive landscape analysis, and project scoping",
      "quantity": "20",
      "unit_amount": {
        "currency_code": "USD",
        "value": "200.00"
      },
      "unit_of_measure": "HOURS",
      "tax": {
        "name": "Sales Tax",
        "percent": "6.25"
      }
    },
    {
      "name": "Creative Design",
      "description": "Brand identity refresh — logo, typography, color system, and style guide",
      "quantity": "35",
      "unit_amount": {
        "currency_code": "USD",
        "value": "175.00"
      },
      "unit_of_measure": "HOURS",
      "tax": {
        "name": "Sales Tax",
        "percent": "6.25"
      }
    },
    {
      "name": "Licensed Stock Photography",
      "description": "Commercial license, 1-year term per image",
      "quantity": "12",
      "unit_amount": {
        "currency_code": "USD",
        "value": "45.00"
      },
      "unit_of_measure": "QUANTITY",
      "tax": {
        "name": "Sales Tax",
        "percent": "6.25"
      }
    },
    {
      "name": "Software Tools & Subscriptions",
      "description": "Figma, Maze, and Loom — project duration licenses",
      "quantity": "3",
      "unit_amount": {
        "currency_code": "USD",
        "value": "120.00"
      },
      "unit_of_measure": "QUANTITY"
    },
    {
      "name": "Project Management & Coordination",
      "description": "Flat-rate fee covering sprint planning, client communications, and delivery coordination for full project duration",
      "quantity": "1",
      "unit_amount": {
        "currency_code": "USD",
        "value": "1500.00"
      },
      "unit_of_measure": "AMOUNT",
      "tax": {
        "name": "Sales Tax",
        "percent": "6.25"
      }
    }
  ],
  "configuration": {
    "allow_tip": false,
    "partial_payment": {
      "allow_partial_payment": true,
      "minimum_amount_due": {
        "currency_code": "USD",
        "value": "2500.00"
      }
    },
    "tax_calculated_after_discount": true,
    "tax_inclusive": false
  },
  "amount": {
    "breakdown": {
      "discount": {
        "invoice_discount": {
          "percent": "5"
        }
      }
    }
  }
}
```

**Notes**

- You can mix all three `unit_of_measure` types — `HOURS`, `QUANTITY`, and `AMOUNT` — freely within the same `items` array. Each line item renders according to its own type on the invoice.
- Use `quantity: "1"` on `AMOUNT` lines for flat-rate fees. Don't use a quantity greater than `"1"` on an `AMOUNT` line — the API multiplies the values, which is likely unintended for flat fees.
- The invoice-level `amount.breakdown.discount` applies across the entire invoice total after individual line item subtotals are summed. Line item-level discounts apply before the invoice-level discount.
- Set `configuration.tax_calculated_after_discount: true` to calculate tax on the post-discount amount — the correct behavior for most jurisdictions.
- `detail.memo` is private and never shown to the client — use it for internal bookkeeping, account references, or sales attribution.

<Columns>
  <Card title="Invoicing API" href="/growth/grow-business/invoicing/integrate">
    The Invoicing REST API lets you create, update, send, and manage invoices programmatically from your backend systems.
  </Card>

  <Card title="Troubleshooting" href="/growth/grow-business/invoicing/troubleshooting">
    Resolve common Invoicing API errors and integration issues.
  </Card>
</Columns>
