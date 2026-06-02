<!-- Source URL: https://docs.paypal.ai/grow/reports-analytics/report-fields-formats -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Report fields and formats reference

## Activity Download Report

The Activity Download Report provides you with access to transaction details for advanced reporting. You can customize reports with user-selected date ranges, file types, and data fields. The Activity Download Report is available for merchants with access to the reporting portal. It is available at the account level.

The Activity Download Report contains standardized fields and support multiple output formats. Understanding these specifications helps you process and integrate report data effectively.

## Know before you begin

- The reports character encoding is UTF-8 (8-bit UCS/Unicode Transformation Format).
- The reports are available in these formats:
  - Portable Document Format (PDF)
  - Comma-Separated Values (CSV)
  - Tab-Separated Value (TAB)
  - Quickbooks (IIF-enabled only for US accounts)
  - Quicken (QIF-USD only)

> **Note:** An Activity Download Report of CSV or TAB format can contain a maximum of 50,000 records. If the report contains more than 50,000 records, the report is split across multiple files and compiled into a ZIP file.

## Getting started

### Common report fields

#### Transaction level fields

- **Transaction ID**: Unique identifier for each transaction
- **Transaction Date**: When the transaction occurred
- **Transaction Type**: PAYMENT, REFUND, ADJUSTMENT, etc.
- **Transaction Status**: SUCCESS, PENDING, FAILED, etc.
- **Amount**: Transaction amount in original currency
- **Currency Code**: Three-letter ISO currency code
- **Fee Amount**: PayPal processing fees
- **Net Amount**: Amount after fees

#### Merchant information

- **Merchant Account ID**: Your PayPal account identifier
- **Store ID**: Physical or online store identifier
- **Invoice Number**: Your internal invoice reference
- **Custom Field**: Additional tracking data

#### Customer details (when available)

- **Payer Email**: Customer's PayPal email
- **Payer Name**: Customer's name
- **Payer Country**: Customer's country code
- **Shipping Address**: Delivery address details

### Supported file formats

#### CSV format

```csv theme={null}
Transaction ID,Date,Type,Status,Amount,Currency,Fee,Net
TXN123456789,2024-01-15,PAYMENT,SUCCESS,100.00,USD,3.20,96.80
```

#### JSON format

```json theme={null}
{
  "transaction_details": [
    {
      "transaction_info": {
        "transaction_id": "TXN123456789",
        "transaction_event_code": "T0006",
        "transaction_initiation_date": "2024-01-15T10:30:00Z",
        "transaction_updated_date": "2024-01-15T10:30:00Z",
        "transaction_amount": {
          "currency_code": "USD",
          "value": "100.00"
        },
        "fee_amount": {
          "currency_code": "USD",
          "value": "3.20"
        },
        "transaction_status": "S",
        "transaction_subject": "Payment for Order #12345"
      }
    }
  ]
}
```

### Field specifications

#### Date fields

- **Format**: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
- **Timezone**: UTC unless specified
- **Precision**: Seconds level

#### Amount fields

- **Decimal Places**: Up to 2 for most currencies
- **Negative Values**: Indicated by minus sign
- **Zero Values**: Represented as "0.00"

#### Status codes

| Code | Description |
| ---- | ----------- |
| S    | Success     |
| P    | Pending     |
| F    | Failed      |
| C    | Cancelled   |
| R    | Refunded    |

#### Transaction event codes

- **T0006**: Payment received
- **T0007**: Payment sent
- **T0111**: Refund issued
- **T0200**: Chargeback initiated

### Custom field mapping

```javascript theme={null}
// Map PayPal fields to your system
const mapTransactionFields = (paypalTransaction) => {
  return {
    internalId: paypalTransaction.custom_field,
    externalId: paypalTransaction.transaction_id,
    amount: parseFloat(paypalTransaction.transaction_amount.value),
    currency: paypalTransaction.transaction_amount.currency_code,
    status: mapStatus(paypalTransaction.transaction_status),
    timestamp: new Date(paypalTransaction.transaction_initiation_date),
  };
};
```

## Report availability and retention

Activity download reports can be generated for any time period within the last 7 years. Users can select a time period of up to 12 months at a time for report generation.

In addition to choosing dates from a calendar, you can choose:

- Since last download
- Today
- Yesterday
- Past month
- Past 3 months
- Past 6 months

## Report file name

The filename of a report from Activity Download follows this naming convention:

`Download.*format*`

`format` is one of the following:

- `CSV`: A comma-separated value file.
- `TAB`: A tab-separated value file.
- `PDF`: A portable document format file.
- `IFF`: An Intuit Interchange Format file.
- `QIF`: A Quicken Interchange Format file.

## Download fields

The following download data fields are available in the Activity Download report:

- **Column name**: The exact field name as it appears in the report, representing a specific transaction detail.
- **Position**: The sequential order of the column if all available fields are included in the report.
- **State**: Indicates whether a field is included in the report by default:
  - **Mandatory**: Always included and cannot be removed.
  - **Selected**: Included by default, but can be deselected by the user.
  - **Unselected**: Not included by default, but can be added by the user.
- Users can customize which fields appear in their report by editing the selection of **Selected** and **Unselected** fields.

### Download data fields

<table>
  <thead>
    <tr>
      <th>Position</th>
      <th>Column name</th>
      <th>Data type</th>
      <th>Char max length</th>
      <th>State</th>
      <th>In PDF</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>1</td>
      <td>Date</td>
      <td>Date</td>
      <td>10</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>The localized completion date of the transaction. For the US, <code>MM/DD/YYYY</code>.</td>
    </tr>

    <tr>
      <td>2</td>
      <td>Time</td>
      <td>Time</td>
      <td>8</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The localized completion time of the transaction. Format is <code>HH:MM:SS</code>.</td>
    </tr>

    <tr>
      <td>3</td>
      <td>TimeZone</td>
      <td>Alphanumeric</td>
      <td>32</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The time zone used for displaying transaction date and time.</td>
    </tr>

    <tr>
      <td>4</td>
      <td>Name</td>
      <td>Alphanumeric</td>
      <td>200</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>Counterparty name. Business name for business users and name for personal or premier users. Not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>5</td>
      <td>Type</td>
      <td>Alphanumeric</td>
      <td>100</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Transaction event code (T-Code) description. Not unique and can have spaces. See the <a href="https://developer.paypal.com/docs/reports/reference/tcodes/">Transaction Detail Report Specification</a> for a full list of T-Codes.</td>
    </tr>

    <tr>
      <td>6</td>
      <td>Status</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>The status of the transaction. Possible values include Completed, Denied, Reversed, Pending, Active, Expired, Removed, Unverified, Voided, Processing, Created, Canceled, and more for invoice activity such as Error, Draft, Unpaid, Paid, Marked as paid, Refunded, etc. Not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>7</td>
      <td>Currency</td>
      <td>3-char currency code</td>
      <td>3</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Currency of transaction. Not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>8</td>
      <td>Gross</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized gross amount. Total amount of the transaction including fees. Not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>9</td>
      <td>Fee</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized fee amount associated with the transaction. Not unique and can have spaces.</td>
    </tr>

    <tr>
      <td>10</td>
      <td>Net</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized net amount of the transaction (usually gross minus fee). Not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>1</td>
      <td>Date</td>
      <td>Date</td>
      <td>10</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>The localized completion date of the transaction in a format based on the user's country. For the US, <code>MM/DD/YYYY</code></td>
    </tr>

    <tr>
      <td>2</td>
      <td>Time</td>
      <td>Time</td>
      <td>8</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The localized completion time of the transaction. Format is <code>HH:MM:SS</code>.</td>
    </tr>

    <tr>
      <td>3</td>
      <td>TimeZone</td>
      <td>Alphanumeric</td>
      <td>32</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The time zone used for displaying transaction date and time.</td>
    </tr>

    <tr>
      <td>4</td>
      <td>Name</td>
      <td>Alphanumeric</td>
      <td>200</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>Counterparty name. Business name for business users and name for personal or premier users. Is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>5</td>
      <td>Type</td>
      <td>Alphanumeric</td>
      <td>100</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Transaction event code (T-Code) description. Is not unique and can have spaces. See the <a href="https://developer.paypal.com/docs/reports/reference/tcodes/" pa-marked="1">Transaction Detail Report Specification</a> for a full list of T-Codes.</td>
    </tr>

    <tr>
      <td>6</td>
      <td>Status</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>The status of the transaction. Possible values for all activity:<ul>
      <li>Completed</li>
      <li>Denied</li>
      <li>Reversed</li>
      <li>Pending</li>
      <li>Active</li>
      <li>Expired</li>
      <li>Removed</li>
      <li>Unverified</li>
      <li>Voided</li>
      <li>Processing</li>
      <li>Created</li>
      <li>Canceled</li>
      </ul>Possible additional values are supported for invoice activity:<ul>
      <li>Error</li>
      <li>Draft</li>
      <li>Unpaid</li>
      <li>Paid</li>
      <li>Unpaid (sent)</li>
      <li>Marked as paid</li>
      <li>Marked as refunded</li>
      <li>Refunded</li>
      <li>Partially refunded</li>
      <li>Scheduled</li>
      <li>Partially paid</li>
      <li>Payment pending</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>7</td>
      <td>Currency</td>
      <td>3-char currency code</td>
      <td>3</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Currency of transaction. It is not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>8</td>
      <td>Gross</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized gross amount. To talk amount of the transaction including fees. It is not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>9</td>
      <td>Fee</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized fee amount associated with the transaction. This field contains the fee amount value for all transactions where a transactional fee has been processed. Fees are not amortized across several transactions. Is not unique and can have spaces.</td>
    </tr>

    <tr>
      <td>10</td>
      <td>Net</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Mandatory</td>
      <td>Yes</td>
      <td>Localized net amount of the transaction (usually gross fee). It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>11</td>
      <td>From Email Address</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The email address of the person with which the merchant transacted (buyer). It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>12</td>
      <td>To Email Address</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The email address of the transaction recipient. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>13</td>
      <td>Transaction ID</td>
      <td>Varchar</td>
      <td>24</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>Encrypted Transaction ID. The ID of the transaction against which the case was filed. This unique 17-character ID is generated by PayPal and cannot be altered. It is unique and can have blanks.</td>
    </tr>

    <tr>
      <td>14</td>
      <td>CounterParty Status</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The accounts status of the counterparty. Possible values: <ul>
      <li>Verified</li>
      <li>Unverified</li>
      <li>Unregistered</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>15</td>
      <td>Shipping Address</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The complete shipping address for the transaction. This information is a pass-through of what was provided by the payer. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>16</td>
      <td>Address Status</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Selected</td>
      <td>No</td>
      <td>The status of the counterparty's shipping address. Possible values: <ul>
      <li>Confirmed</li>
      <li>Non-Confirmed</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>17</td>
      <td>Item Title</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Selected</td>
      <td>No</td>
      <td>The item title specified by a buyer in the website Auction/Item title field. It is specified by the seller in any of the following <code>buttoncreation</code> fields (<code>item\_name</code> or <code>item\_name\_x</code>):<ul>
      <li>PayPal Shopping Cart Item Name</li>
      <li>Buy Now Item Name</li>
      <li>Donations Item Name</li>
      <li>Subscriptions Name</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>18</td>
      <td>Item ID</td>
      <td>Alphanumeric</td>
      <td>127</td>
      <td>Selected</td>
      <td>No</td>
      <td>Specified by the seller in any of the following <code>buttoncreation</code> fields (<code>item\_name</code> or <code>item\_name\_x</code>):<ul>
      <li>PayPal Shopping Cart Item Name</li>
      <li>Buy Now Item Name</li>
      <li>Donations Item Name</li>
      <li>Subscriptions Name</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>19</td>
      <td>Shipping and Handling Amount</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Selected</td>
      <td>No</td>
      <td>The localized amount paid, as reported by either PayPal or the merchant, for shipping and handling as a part of the transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>20</td>
      <td>Insurance Amount</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Selected</td>
      <td>No</td>
      <td>The localized insurance amount, as reported by either PayPal or the merchant, for the transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>21</td>
      <td>Sales Tax</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Selected</td>
      <td>No</td>
      <td>The localized sales tax amount, as reported by either PayPal or the merchant, paid as part of the transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>22</td>
      <td>Option 1 Name</td>
      <td>Alphanumeric</td>
      <td>64</td>
      <td>Selected</td>
      <td>No</td>
      <td>The Option 1 Name associated with a transaction. It is specified by the seller in any of the following <code>buttoncreation</code> fields )<code>on0</code> or <code>on0\_x</code>): <ul>
      <li>3 PayPal Shopping Cart Option 1 Name</li>
      <li>3 Buy Now Option 1 Name</li>
      <li>3 Subscription Option 1 Name</li>
      </ul> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>23</td>
      <td>Option 1 Value</td>
      <td>Alphanumeric</td>
      <td>200</td>
      <td>Selected</td>
      <td>No</td>
      <td>The Option 1 Value associated with a transaction. It is entered by the buyer in any of the following website fields:<ul>
      <li>3 PayPal Shopping Cart Option 1 Value</li>
      <li>3 Buy Now Option 1 Value</li>
      <li>3 Subscription Option 1 Value</li>
      </ul>It is specified by the seller in any of the following<code>A1:F56</code> fields:<ul>
      <li>3 PayPal Shopping Cart Option 1 Value</li>
      <li>3 Buy Now Option 1 Value</li>
      <li>3 Subscription Option 1 Value</li>
      </ul> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>24</td>
      <td>Option 2 Name</td>
      <td>Alphanumeric</td>
      <td>64</td>
      <td>Selected</td>
      <td>No</td>
      <td>The Option 2 Name associated with a transaction. It is specified by the seller in any of the following <code>buttoncreation</code> fields )<code>on0</code> or <code>on0\_x</code>): <ul>
      <li>3 PayPal Shopping Cart Option 2 Name</li>
      <li>3 Buy Now Option 2 Name</li>
      <li>3 Subscription Option 2 Name</li>
      </ul> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>25</td>
      <td>Option 2 Value</td>
      <td>Alphanumeric</td>
      <td>200</td>
      <td>Selected</td>
      <td>No</td>
      <td>The Option 2 Value associated with a transaction. It is entered by the buyer in any of the following website fields:<ul>
      <li>3 PayPal Shopping Cart Option 2 Value</li>
      <li>3 Buy Now Option 2 Value</li>
      <li>3 Subscription Option 2 Value</li>
      </ul>It is specified by the seller in any of the following fields:<ul>
      <li>3 PayPal Shopping Cart Option 2 Value</li>
      <li>3 Buy Now Option 2 Value</li>
      <li>3 Subscription Option 2 Value</li>
      </ul> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>26</td>
      <td>Auction Site</td>
      <td>Varchar</td>
      <td>255</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The name of the auction site:<ul>
      <li>eBay</li>
      <li>Yahoo! Auctions</li>
      <li>uBid.com</li>
      <li>Amazon.com Auctions</li>
      <li>MSN Auctions</li>
      <li>BidVille</li>
      <li>Other</li>
      </ul> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>27</td>
      <td>Buyer ID</td>
      <td>Varchar</td>
      <td>255</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The ID of the buyer making the purchase in the auction. This ID can be different from the payer ID provided for the payment. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>28</td>
      <td>Item URL</td>
      <td>Alphameric</td>
      <td>4000</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The URL of the eBay/Auction Item. In the case of multiple items, items are separated with a comma and shown along with the payment row. For example, <code>[http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem\&amp;item=252297991684](http://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem\&amp;item=252297991684)</code>. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>29</td>
      <td>Closing Date</td>
      <td>Alphanumeric</td>
      <td>100</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The close date of eBay/Auction Item. The date format is based on the user's country. For example, <code>3/12/2016 10:31:52 PM</code>. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>30</td>
      <td>Escrow ID</td>
      <td>Numeric</td>
      <td>22</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The ID associated with the eBay Escrow CN Checkout transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>31</td>
      <td>Reference Txn ID</td>
      <td>Varchar</td>
      <td>24</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The encrypted Transaction ID of the parent transaction. It is unique and can have blanks.</td>
    </tr>

    <tr>
      <td>32</td>
      <td>Invoice Number Text</td>

      <td />

      <td>127</td>
      <td>Selected</td>
      <td>No</td>
      <td>The invoice ID set by the merchant with the transaction. Uniqueness enforced by PayPal when the transaction is created. If an invoice ID was sent with the capture request, this value is reported here. However, if no invoice ID was sent with the capture request, the value of the invoice ID (if any) from the authorizing transaction is reported here. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>33</td>
      <td>Custom Number</td>
      <td>Alphanumeric</td>
      <td>256</td>
      <td>Selected</td>
      <td>No</td>
      <td>Shown only to seller/admin. The shopping cart customer number, Buy Now customer number, Subscription custom number, gift certificate tracking ID, or Masspay 2.0 disbursement ID. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>34</td>
      <td>Quantity</td>
      <td>Numeric</td>
      <td>25</td>
      <td>Selected</td>
      <td>No</td>
      <td>This shows the total number of items present in the payment transaction. For item rows, it shows quantity of an individual item.</td>
    </tr>

    <tr>
      <td>35</td>
      <td>Receipt ID</td>
      <td>Alphanumeric</td>
      <td>19</td>
      <td>Mandatory</td>
      <td>No</td>
      <td>The receipt identification number. 16-digit number in <code>xxxx-xxxx-xxxx-xxxx</code> format. It is not unique and can contain blanks.</td>
    </tr>

    <tr>
      <td>36</td>
      <td>Balance</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Selected</td>
      <td>No</td>
      <td>Reflects the running amount in the merchant's bank account (available balance) in the currency of the transaction. Balance equals the previous balance plus the net. It is not unique and can contain blanks.</td>
    </tr>

    <tr>
      <td>37</td>
      <td>Address Line 1</td>
      <td>Varchar</td>
      <td>300</td>
      <td>Selected</td>
      <td>No</td>
      <td>The first line of the shipping address. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>38</td>
      <td>Address Line 2/<br />District/<br />Neighborhood</td>
      <td>Varchar</td>
      <td>300</td>
      <td>Selected</td>
      <td>No</td>
      <td>The second line of the shipping address. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>39</td>
      <td>Town/City</td>
      <td>Alphanumeric</td>
      <td>120</td>
      <td>Selected</td>
      <td>No</td>
      <td>The town or city of the shipping address.</td>
    </tr>

    <tr>
      <td>40</td>
      <td>State/Province/<br />Region/Country/<br />Territory/Prefecture/<br />Republic</td>
      <td>Alphanumeric</td>
      <td>120</td>
      <td>Selected</td>
      <td>No</td>
      <td>The state, province, region, territory, prefecture, or republic of the shipping address. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>41</td>
      <td>Zip/Postal Code</td>
      <td>Varchar</td>
      <td>60</td>
      <td>Selected</td>
      <td>No</td>
      <td>The zip or postal code of the shipping address. It is not unique and can contain blanks.</td>
    </tr>

    <tr>
      <td>43</td>
      <td>Contact Phone Number</td>
      <td>Numeric</td>
      <td>22</td>
      <td>Selected</td>
      <td>No</td>
      <td>The contact phone number. It is not unique and can contain blanks.</td>
    </tr>

    <tr>
      <td>44</td>
      <td>Subject</td>
      <td>Alphanumeric</td>
      <td>256</td>
      <td>Selected</td>
      <td>No</td>
      <td>The Transaction Subject/Item name. The subject of the payment as passed through the payer to the payee. This data is controlled by the payer exclusively in the interfaces through which it is sent. It is not unique and can contain blanks.</td>
    </tr>

    <tr>
      <td>45</td>
      <td>Note</td>
      <td>Varchar</td>
      <td>4000</td>
      <td>Selected</td>
      <td>No</td>
      <td>The transaction note. A special note of payment as passed through by the payer to the payee. This data is controlled by the payer exclusively in the interfaces through which it is sent. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>46</td>
      <td>Payment Source</td>
      <td>Varchar</td>
      <td>50</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The funding method. Possible values are:<ul>
      <li>PayPal</li>
      <li>PayPal Funds</li>
      <li>Instant Transfer</li>
      <li>Instant</li>
      <li>Non-Instant</li>
      <li>eCheck</li>
      <li>Credit Card</li>
      <li>Electronic Funds Transfer</li>
      <li>Direct Debit</li>
      <li>Buyer Credit</li>
      <li>PayPal Pay Later</li>
      <li>Plus Card</li>
      <li>eBay Master Card</li>
      <li>PayPal Credit</li>
      <li>Payment with giropay</li>
      <li>Virtual Terminal Transaction</li>
      <li>Debit Card</li>
      <li>Venmo</li>
      <li>Apple Pay</li>
      <li>Google Pay</li>
      <li>Network Token</li>
      <li>Pay Upon Invoice</li>
      <li><a href="https://developer.paypal.com/docs/multiparty/checkout/apm/supported-apms/" target="_blank" rel="noopener noreferrer">Supported APMs</a></li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>47</td>
      <td>Card Type</td>
      <td>Varchar</td>
      <td>30</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The funding source used for the transaction. Possible values are:<ul>
      <li><code>VISA</code></li>
      <li><code>MASTERCARD</code></li>
      <li><code>AMEX</code></li>
      <li><code>BANKCARD</code></li>
      <li><code>DISCOVER</code></li>
      <li><code>DINERS</code></li>
      <li><code>SWITCH</code></li>
      <li><code>SOLO</code></li>
      <li><code>GE</code></li>
      <li><code>CARTES\_BANCIARES</code></li>
      <li><code>JCB</code></li>
      <li><code>UNKNOWN</code></li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>48</td>
      <td>Transaction Event Code</td>
      <td>Alpahanumeric</td>
      <td>5</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The T-Code number. It is not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>49</td>
      <td>Payment Tracking ID</td>
      <td>Varchar</td>
      <td>127</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The tracking ID specified by partners to obtain information about a payment or to request a refund. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>50</td>
      <td>Bank Reference ID</td>
      <td>Varchar</td>
      <td>13</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The bank reference ID. It is unique and can have blanks.</td>
    </tr>

    <tr>
      <td>51</td>
      <td>Transaction Buyer Country Code</td>
      <td>Varchar</td>
      <td>45</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The buyer country code. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>52</td>
      <td>Item Details</td>
      <td>Varchar</td>
      <td>1024</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The item details. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>53</td>
      <td>Coupons</td>
      <td>Varchar</td>
      <td>2048</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The information about all the coupons associated with the transaction. Each individual item contains four pipe-delimited parts of information:<ul>
      <li>3 Incentive code (offers or coupon)</li>
      <li>3 Amount</li>
      <li>3 Currency</li>
      <li>3 Campaign ID (associated with store offer or coupon)</li>
      </ul>For example, for a USD \$20 store offer with offer code 1234 and campaign ID ABCD, the delimited information would be \`1234</td>
    </tr>

    <tr>
      <td>54</td>
      <td>Special Offers</td>
      <td>Varchar</td>
      <td>2048</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The informationa bout all the store credits associated with the transaction. Each individual item contains four pipe-delimited parts of information:<ul>
      <li>3 Incentive code (offers or coupon)</li>
      <li>3 Amount</li>
      <li>3 Currency</li>
      <li>3 Campaign ID (associated with store offer or coupon)</li>
      </ul>For example, for a USD \$20 store offer with offer code 1234 and campaign ID ABCD, the delimited information would be \`1234</td>
    </tr>

    <tr>
      <td>55</td>
      <td>Loyalty Card Number</td>
      <td>Varchar</td>
      <td>100</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The customer's loyalty card provided to the merchant. This is applicable for Point of Sale transactions only. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>56</td>
      <td>Authorization Review Status</td>
      <td>Varchar</td>
      <td>2</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Indicated the current status of the transaction and whether it is under review. If it is under review, then the status is either Green (01) or Yellow (02). Possible values are:<ul>
      <li>01</li>
      <li>02</li>
      <li>Blank</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>57</td>
      <td>Protection Eligibility</td>
      <td>Varchar</td>
      <td>2</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Indicates whether the transaction is eligible (01), not eligible (02), or partially eligible (03) for seller protection. Possible values are:<ul>
      <li>01</li>
      <li>02</li>
      <li>03</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>58</td>
      <td>Country Code</td>
      <td>Varchar</td>
      <td>64</td>
      <td>Selected</td>
      <td>No</td>
      <td>The two letter country code of the shipping address. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>59</td>
      <td>Balance Impact</td>
      <td>Varchar</td>
      <td>64</td>
      <td>Selected</td>
      <td>No</td>
      <td>The impact on the balance for the transaction. Possible values are:<ul>
      <li>Debit</li>
      <li>Credit</li>
      <li>Memo</li>
      </ul>It is not unique and cannot have blanks.</td>
    </tr>

    <tr>
      <td>60</td>
      <td>Buyer Wallet</td>
      <td>Varchar</td>
      <td>10</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The text that identifies the company (PayPal or one of its subsidiaries) that processes the payment. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>61</td>
      <td>Comment 1</td>
      <td>Varchar</td>
      <td>1000</td>
      <td>Unselected</td>
      <td>No</td>
      <td>A note that accompanies a gateway transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>62</td>
      <td>Comment 2</td>
      <td>Varchar</td>
      <td>1000</td>
      <td>Unselected</td>
      <td>No</td>
      <td>A note that accompanies a gateway transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>63</td>
      <td>Invoice Number</td>
      <td>Varchar</td>
      <td>200</td>
      <td>Selected</td>
      <td>No</td>
      <td>The identifier of the invoice issued by the merchant. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>64</td>
      <td>PO Number</td>
      <td>Varchar</td>
      <td>200</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The identifier of the manifest of goods bought from the merchant. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>65</td>
      <td>Customer Reference Number</td>
      <td>Varchar</td>
      <td>80</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The identifier of the customer for a merchant. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>66</td>
      <td>Payflow Transaction ID (PNREF)</td>
      <td>Varchar</td>
      <td>80</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The unique idenitifier for the gateway transaction. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>67</td>
      <td>Tip</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The amount of money paid by a consumer to a merchant over and above the item costs and any handling amounts in appreciation for services rendered. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>68</td>
      <td>Discount</td>
      <td>Currency/Money</td>
      <td>25</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The amount of discount given on the ordinary price of an item or group of items by the merchant. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>69</td>
      <td>SellerID</td>
      <td>Varchar</td>
      <td>200</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The unique identifier for the merchant at the marketplace site. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>70</td>
      <td>Risk Filter</td>
      <td>Varchar</td>
      <td>500</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The risk checks that the transaction matches. For a list of possible values see <a href="https://developer.paypal.com/docs/reports/reference/changed-download-fields/" pa-marked="1">Changed Download Fields</a> It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>71</td>
      <td>Tax ID Type</td>
      <td>Varchar</td>
      <td>4</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Indicates the tax ID type of the buyer. Available for Brazil only. Possible values are:<ul>
      <li>CPF</li>
      <li>CNPJ</li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>72</td>
      <td>Tax ID</td>
      <td>Varchar</td>
      <td>80</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The buyer's taxpayer registry number. Avaiable for Brazil only. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>73</td>
      <td>Number of Installments</td>
      <td>Numeric</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The number of installments for the credit offer. Available for Brazil and Mexico only. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>74</td>
      <td>Installment Amount</td>
      <td>Currency/Money</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The installment amount for the credit offer. Only available for Brazil and Mexico. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>75</td>
      <td>Installment Fee</td>
      <td>Currency/Money</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The installment fee for the credit offer. Only available for Brazil and Mexico. It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>76</td>
      <td>Credit Transactional Fee</td>
      <td>Currency/Money</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The credit-related transaction fee amount for a merchant-selected credit offering.</td>
    </tr>

    <tr>
      <td>77</td>
      <td>Credit Promotional Fee</td>
      <td>Currency/Money</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The credit-related transaction fee amount for a merchant-selected credit offering with a promotional APR.</td>
    </tr>

    <tr>
      <td>78</td>
      <td>Credit Term</td>
      <td>Numeric</td>
      <td>26</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The time span covered by the merchant-selected credit offer. The length of the term is captured in months.</td>
    </tr>

    <tr>
      <td>79</td>
      <td>Credit Offer Type</td>
      <td>Alphanumeric</td>
      <td>64</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The name of the credit offer used by the buyer as a funding instrument.</td>
    </tr>

    <tr>
      <td>80</td>
      <td>Original Invoice ID</td>
      <td>Varchar</td>
      <td>200</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The invoice ID of the original payment record. This ID helps users link and track all related transactions to the original parent transaction.</td>
    </tr>

    <tr>
      <td>81</td>
      <td>Campaign Fee</td>
      <td>Currency/Money</td>
      <td>22</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The fee charged to a merchant for each sale with a discount applied during a campaign.</td>
    </tr>

    <tr>
      <td>82</td>
      <td>Campaign Name</td>
      <td>Varchar</td>
      <td>200</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The name given to the campaign. Merchants can track this name on the campaign dashboard. Examples: <code>XMAS2021</code>, <code>Sales Recovery Campaign</code>.</td>
    </tr>

    <tr>
      <td>83</td>
      <td>Campaign Discount</td>
      <td>Currency/Money</td>
      <td>22</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Denotes the value of a discount amount applied in the transaction. For marketing campaigns, merchants can offer customers a discount in either a dollar amount or percentage.</td>
    </tr>

    <tr>
      <td>84</td>
      <td>Campaign Discount Currency</td>
      <td>3-char currency code</td>
      <td>3</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Denotes the currency of the discounted amount.</td>
    </tr>

    <tr>
      <td>85</td>
      <td>Payment Source Subtype</td>
      <td>Varchar</td>
      <td>50</td>
      <td>Unselected</td>
      <td>No</td>
      <td>The funding source used for the transaction and the name of the credit offer used by the buyer as a funding instrument. Possible values are:<ul>
      <li><code>VISA</code></li>
      <li><code>MASTERCARD</code></li>
      <li><code>AMEX</code></li>
      <li><code>BANKCARD</code></li>
      <li><code>DISCOVER</code></li>
      <li><code>DINERS</code></li>
      <li><code>SWITCH</code></li>
      <li><code>SOLO</code></li>
      <li><code>CARTES\_BANCIARES</code></li>
      <li><code>GE</code></li>
      <li><code>JCB</code></li>
      <li><code>CB\_NATIONALE</code></li>
      <li>Pay in 3</li>
      <li>Pay in 4</li>
      <li>Easy Payments</li>
      <li>0% for 4 months</li>
      <li>Installments</li>
      </ul>For Wallets and Network token, Payment Source Subtype would show details of card type and card brand used to fund the transaction.<br />For example: <ul>
      <li><code>Credit Card-VISA</code></li>
      <li><code>Debit Card-MASTERCARD</code></li>
      </ul>It is not unique and can have blanks.</td>
    </tr>

    <tr>
      <td>86</td>
      <td>Decline Code</td>
      <td>Varchar</td>
      <td>50</td>
      <td>Unselected</td>
      <td>No</td>

      <td>
        <ul>
          <li><a href="https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2021-11/EPC173-14%20v6.0%20Guidance%20on%20Reason%20Codes%20for%20SDD%20R-transactions.pdf" class="undefined dx-external-href" title="external link" target="_blank" rel="noopener noreferrer" pa-marked="1">UDD SEPA Decline Codes</a></li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>87</td>
      <td>Fastlane Checkout Transaction</td>
      <td>Varchar</td>
      <td>1</td>
      <td>Unselected</td>
      <td>No</td>
      <td>Indicates whether the transaction was checked out using fastlane accelerated checkout.</td>
    </tr>

  </tbody>
</table>

## Best practices

- Validate all field formats before processing.
- Handle missing or null fields gracefully.
- Store original data for audit purposes.
- Use consistent field mapping across systems.
