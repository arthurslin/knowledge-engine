---
title: "Fireworks AI breach reached customer datasets and Notion AI chat transcripts: what the disclosures say"
date: 2026-11-13
topics: [AI news, AI]
summary: "AI hosting company Fireworks AI says a second October intrusion, through a third-party cloud provider, exposed billing data and, for some customers, datasets and incomplete model weights. Notion says AI chat transcripts from fewer than 1% of its workspaces were among the data; the scope figures come from the two companies themselves."
status: published
quiz:
  - q: "According to Fireworks' November 9 update, how did the attacker reach Fireworks development machines in the second incident?"
    options:
      - "By guessing a customer's password"
      - "Through a security incident at a third-party cloud provider that hosted Fireworks R&D machines"
      - "Through a prompt injection in Notion AI"
      - "By buying stolen payment card numbers"
    answer: 1
    explain: "Fireworks says the provider had an incident on October 23 and the intruder used it on October 24 to reach development machines and run an unauthorised workload. Prompt injection is a different kind of attack and is not part of either company's account."
  - q: "What does Notion say it used Fireworks for in the case of the exposed chat transcripts?"
    options:
      - "Storing every Notion page"
      - "Classification jobs for its Insights admin feature"
      - "Processing payments"
      - "Training Fireworks' own models"
    answer: 1
    explain: "Notion's notice says transcripts were sent to Fireworks for Insights classification, and that data was retained from the Fireworks endpoints it used. That retention is why the zero data retention question matters."
  - q: "What has Notion done since learning of the exposure, according to its notice?"
    options:
      - "Nothing yet"
      - "Disabled Insights and, as of November 3, disconnected from Fireworks and stopped sending it data"
      - "Moved all customers to Fireworks' zero data retention tier"
      - "Deleted all customer workspaces"
    answer: 1
    explain: "Notion says Insights is disabled and that it disconnected its systems, deleted its data on Fireworks and stopped all traffic there as of November 3. It also tells customers to treat the data as exposed."
  - q: "How should a reader treat the figure that fewer than 1% of Notion workspaces were affected?"
    options:
      - "As a number Notion reports from its own investigation, which no outside party has published a check of"
      - "As worthless, since companies always understate breaches"
      - "As confirmed by Fireworks' law enforcement contacts"
      - "As an estimate made by the security firm Wiz"
    answer: 0
    explain: "The figure comes from Notion, and the independent outlets relay it rather than test it. That makes it a claim, not a verified fact, but it is not evidence of understatement either; dismissing it outright is a reflex, not a reasoned judgement."
reflect:
  - "Fireworks' documentation says zero data retention is the default, yet features such as batch jobs store data. If you were choosing an AI provider, what would you need to ask to know where your data actually sits?"
  - "Notion says most exposed transcripts carry no metadata linking them to a workspace or user. How much does that reduce the risk, given that people often paste names, credentials or company details into a chat?"
---

## What happened

Fireworks AI runs and fine-tunes open-weight AI models for other companies. On 9 October 2026 it published a security bulletin saying that on 6 October it had found unauthorised use of internal credentials. At that point it reported that an outsider had accessed environment variables, including API keys and tokens stored as secrets, used in evaluation jobs in a limited number of customer accounts, and that it had no evidence of access to customer models, datasets or inference traffic.

An update, last revised on 9 November, describes a second incident. Fireworks says a third-party cloud provider that hosted its research machines had a security incident on 23 October, and that on 24 October an intruder used that access to reach Fireworks development machines and run an unauthorised workload. Fireworks says it detected this the same day and had seen no further evidence of access to its platform as of 25 October. The data it now lists as accessed includes resource metadata, billing details such as addresses and invoice history (card numbers were not stored), and, "for certain customers," a subset of incomplete model weights and datasets. It links the activity to a financially motivated criminal group selling access to AI models, a practice known as LLMjacking, citing a 2 November report from Google's threat intelligence group.

Notion, the workspace software company, then said the incident affected fewer than 1% of its workspaces. It had sent Notion AI chat transcripts to Fireworks for classification jobs behind its Insights admin feature, and that data had been retained. Notion says it has disabled Insights and, as of 3 November, disconnected from Fireworks, deleted its data there and stopped sending traffic.

## What is claimed vs. what is verified

**Claims from the companies.** The scope figures, the timeline and the finding of no further access after 25 October all come from Fireworks' and Notion's own investigations. So does Fireworks' statement that it has detected no impact on its inference, training SDK and Nexus products, which it describes as zero data retention by default. Notion's statement that most exposed transcripts carry no metadata tying them to a workspace, user or company is also its own account. No outside audit has been published.

**What independent reporting adds.** BleepingComputer, The Hacker News, VentureBeat and SecurityWeek all quote the bulletins directly. They differ in places: BleepingComputer dates the second discovery to 23 October, while the bulletin dates the provider's incident to 23 October and Fireworks' detection to 24 October. Outlets also give different dates for when Fireworks told Notion that its data was involved. The Hacker News alone reports that Fireworks first described the Notion data as synthetic test data; that detail does not appear in the primary notices.

VentureBeat's analysis points to a gap between Fireworks' framing and its documentation. Fireworks says zero data retention is the default, but its policy pages describe features that do store data, including stored responses, batch jobs and training. Fireworks' chief executive, Lin Qiao, wrote on X that inference was unaffected, excluding batch inference, a narrower phrasing than the bulletin's. VentureBeat notes that neither company has said which Fireworks feature held Notion's transcripts.

## Why it matters

Companies increasingly route user data through specialist AI hosts their customers never see. Here, a breach at a provider one layer further down, a cloud host for Fireworks' research machines, reached data from a company two steps removed. VentureBeat cites the security firm Wiz as finding incidents at at least nine AI developer platforms in October, though it does not say Fireworks was one of them. The case also shows how much a "zero data retention" label depends on which features a customer uses.

## Open questions and other views

**What "incomplete" means.** The bulletins do not explain what an incomplete set of model weights is, or whether partial weights or datasets would be useful to whoever took them.

**The company positions.** Fireworks says its investigation is ongoing and may reveal more and lists remediation steps, including replaced credentials and isolated systems. Notion stresses that most transcripts are not attributable, yet still advises customers to treat them as exposed and to rotate any credentials pasted into Notion AI, which concedes that chat text can carry sensitive details on its own.

**The documentation question.** VentureBeat's reading is that the marketing phrase "zero data retention by default" and the product reality of stored batch and training data sit uneasily together. Fireworks' bulletin, by contrast, limits its ZDR claim to named products, and on that narrower wording the two are not in conflict. Which framing customers relied on is not settled by the public record.

**Still unknown.** How many Fireworks customers were affected in total, whether other downstream companies will issue notices, and whether any regulator will examine the disclosures.

## Sources

- Fireworks AI, "October 2026 security incident", published 9 October 2026, updated 10 October 2026. [fireworks.ai](https://fireworks.ai/security/bulletins/october-2026-security-incident) (primary)
- Fireworks AI, "October 2026 security incident update", last updated 9 November 2026. [fireworks.ai](https://fireworks.ai/security/bulletins/october-2026-security-incident-update) (primary)
- Notion, "Notice about the Fireworks AI incident that may impact some Notion workspaces", November 2026. [notion.com](https://notion.com/help/security-incident-involving-a-third-party-ai-vendor) (primary)
- BleepingComputer, Sergiu Gatlan, "Fireworks AI discloses new breach after cloud provider hack", 10 November 2026. [bleepingcomputer.com](https://bleepingcomputer.com/news/security/fireworks-ai-discloses-new-breach-after-cloud-provider-hack) (independent)
- The Hacker News, Ravie Lakshmanan, "Fireworks AI Confirms Wider Breach Affecting Customer Datasets, Model Weights and Notion AI Chats", 10 November 2026. [thehackernews.com](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html) (independent)
- VentureBeat, Louis Columbus, "Attackers breached the Fireworks AI storage where Notion AI chats sat outside zero data retention", 11 November 2026. [venturebeat.com](https://venturebeat.com/security/attackers-breached-the-fireworks-ai-storage-where-notion-ai-chats-sat-outside-zero-data-retention) (independent analysis)
- SecurityWeek, Ionut Arghire, "Notion Customer Data Compromised in Fireworks AI Hack", 12 November 2026. [securityweek.com](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/) (independent)
