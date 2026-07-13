<!-- Source URL: https://docs.metronome.com/guides/events/design-usage-events.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Design usage events

Success with Metronome depends on the data you provide, so it's important to properly design your usage events. Follow these three principles:

* Work backward from what you *need*
* Work forward from what you *have*
* Maximize your flexibility

This guide uses a hypothetical scenario where you're a developer at a Content Delivery Network (CDN) and you've been tasked with integrating your system into Metronome to support usage-based billing.

### Work backward from what you need​

Start with your existing requirements or an ideal invoice and work backward from there. In the case of a CDN, your company charges customers based on their monthly data usage. However, the exact pricing details are unknown. This is fine as pricing can be applied and adjusted later as long as the required metrics are in place.

An additional consideration is that your customer support team wants to take advantage of Metronome as a real-time data platform to notify customers when there's an unusual spike in traffic for their sites.

For both invoicing and notifications, you need to measure data transfer, so the bare minimum usage event looks like:

```json theme={null}
{  
  "event_type": "transfer",  
  "properties": {  
    "bytes": "1234",  
  },  
  "transaction_id": "...",  
  "customer_id": "...",  
  "timestamp": "..."  
}
```

This supports a billable metric like "sum of `bytes` for all events of type `transfer` (for a given customer, for a given billing period)."

### Work forward from what you have​

Next, consider what data you have available and how that data might help in the future.

* **When to send events** Your system could track total data transfer internally and send an incremental per-customer summary to Metronome. Or you could send Metronome an event every time a web page is served. Both options provide the same invoicing ability at the end of each month, which route you choose depends upon your needs.
* **What data to include** There's a lot more information to potentially include in usage events. For example, you could include which data center served the page, what domain was hosted, the type of file, or even what URL was accessed. None of this is immediately necessary for invoicing, but it could be useful for your own records.

The timing and content of usage events are often heavily influenced by what is available in your existing system. At your hypothetical CDN company, imagine that you perform global log aggregation with Apache Flume. In this case, there's a central data store with detailed access logs available, making it easy to send those log messages to Metronome in the form of individual usage events as they arrive.

Now imagine that you don't have such global aggregation. Instead, each data center keeps its own independent log and sends hourly summaries back to the central data store, broken down by domain. Each data center must send usage events directly to Metronome, but unfortunately the code there doesn't have access to the customer database, so the data center can't determine what `customer_id` to fill in for each event. In this case, the hourly summaries are probably the best option. From the central location, it's easy to look up the owner of each domain and provide the appropriate `customer_id`.

Before deciding to send the hourly summaries, you check back with the customer support team about those traffic spike notifications they wanted. They assure you that the hourly cadence is fast enough for the notifications they want to send.

### Maximize your flexibility​

Business needs evolve over time. Rather than attempting to anticipate all future requirements, focus on creating a flexible system that can easily adapt to changes.

In Metronome, flexibility is maximized when you **send as much data as possible**. Metronome's stream pipeline can handle high event throughput, and irrelevant data is discarded during processing. This means there's no downside to sending information that isn't going to be used right away.

There is, however, a big upside to sending extra information. Suppose that your hypothetical CDN company starts getting feedback from customers that they don't understand their bills. Many customers are responsible for more than one domain and would like to be able to see how much each domain is contributing to their total usage. As the assigned developer, your executives ask you to fix this.

If your usage event didn't include the domain, you'd need to go back to your code and add it. But you chose to send as much data as possible, so it's already there:

```json theme={null}
{  
  "event_type": "transfer",  
  "properties": {  
    "domain": "www.example.com",  
    "data_center": "US-WEST-3",  
    "bytes": "12345789",  
  },  
  "transaction_id": "...",  
  "customer_id": "...",  
  "timestamp": "..."  
}
```

All you need to do is query the Metronome API for usage data grouped by `domain`. And your customers are happy with the new breakdown on their invoices.

As time passes and your customer base grows, the finance team discovers a worrisome problem. Your company has been billing customers based on their total data transfer, but your bandwidth costs are different in different parts of the world. In some cases, you're actually losing money by undercharging for data transfer in certain regions.

As before, if your usage events didn't include information about where the data transfer occurred, you'd have to go back into your code and add it. But because you already decided to send as much data as possible, there's a `data_center` field that will work. Billable metrics in Metronome can filter usage events in a variety of ways, so you are able to use a mapping of data center names to regions to define a new billable metric for each region. Going forward, you can bill based on those new metrics, where you can set individual prices for each region.

<Warning>
  **BILLABLE METRICS ARE NOT RETROACTIVE**

  Metronome operates on streams; changes you make only affect future data collection and aggregation. New billable metrics cannot be applied to historical data.
</Warning>
