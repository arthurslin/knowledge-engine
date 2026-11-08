---
title: "METR estimates Anthropic's capability gains have roughly doubled in pace, but most of the evidence is redacted"
date: 2026-11-08
topics: [AI news, AI safety]
summary: "An external evaluator with internal access estimates Anthropic's benchmark progress since October 2025 runs at about 1.9 times its earlier rate, and attributes most of the speed-up to AI use. Anthropic redacted much of the evidence behind those conclusions."
status: published
quiz:
  - q: "What does the 1.9x figure in METR's report measure?"
    options:
      - "How much faster individual Anthropic staff say they work with AI"
      - "The growth rate of Anthropic's internal capability index since October 2025, relative to the earlier trend"
      - "The increase in Anthropic's training compute"
      - "How much better Anthropic's newest model is than its competitors"
    answer: 1
    explain: "It compares the rate at which scores on Anthropic's internal version of the Epoch Capabilities Index rose after October 2025 with the rate before. Self-reported staff speed-ups are a separate, looser measure, and METR says compute growth did not drive the change."
  - q: "What could Anthropic do under the terms of the engagement?"
    options:
      - "Nothing; METR had unrestricted access"
      - "Pay METR for a favourable result"
      - "Redact any non-public information and approve or reject METR's data requests"
      - "Edit METR's conclusions before publication"
    answer: 2
    explain: "METR says Anthropic had unilateral redaction rights over non-public information and could approve or reject requests. METR says it took no payment, and nothing in the report says Anthropic rewrote the conclusions."
  - q: "How does METR treat the staff survey showing about 12x self-reported uplift?"
    options:
      - "As its headline estimate of acceleration"
      - "As very loose evidence from low-effort poll responses, not an acceleration rate"
      - "As proof that AI now does most research autonomously"
      - "As data it was not allowed to see"
    answer: 1
    explain: "METR calls the Slack polls very loose evidence and says the individual numbers do not correspond to acceleration rates. It also says AI is not yet making highly significant, fully autonomous contributions to key parts of training."
  - q: "A reader says the finding is worthless because Anthropic controlled what METR could see. Which response fits the report best?"
    options:
      - "Correct: METR was paid by Anthropic, so it is not independent"
      - "Correct: METR never had access to any internal data"
      - "Too strong: the redactions mean readers must rely on METR's judgment more than is ideal, and METR says so, but METR did see internal data, took no payment and published wide uncertainty ranges"
      - "Too weak: the findings have already been replicated by other labs"
    answer: 2
    explain: "The access limits are a real weakness that METR itself highlights. They make the conclusions harder to check, not automatically wrong. METR reports receiving internal benchmark data and interviews and says it took no payment. No independent replication exists."
reflect:
  - "If an evaluator can see evidence the public cannot, what would make you more or less willing to accept its judgment on that evidence?"
  - "The headline estimate rests on benchmarks that favour well-specified, easily graded tasks. What kind of measurement would tell you whether real research is speeding up in the same way?"
---

## What happened

On 5 November 2026 METR, a nonprofit that evaluates frontier AI systems, published "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026". The work was done by METR staff, about 2.5 full-time equivalents, between 12 August and 29 October 2026, with the final report submitted on 3 November. The engagement looked at three questions: whether the growth rate of Anthropic's internal capabilities has sped up, how much of any speed-up is due to AI, and whether there are near-term bottlenecks.

Anthropic's Responsible Scaling Policy lists AI R&D acceleration as a key risk indicator, which is the backdrop for the exercise. METR says it did not pay special attention to the policy's thresholds. On the same day METR published a separate review of the automated R&D section of Anthropic's August 2026 Risk Report, in which it agreed that the models assessed there posed low catastrophic risk but judged that an early-warning threshold for doubled acceleration had plausibly already been crossed by mid-July.

## What is claimed vs. what is verified

METR's headline estimate comes from AECI, which it describes as Anthropic's version of the Epoch Capabilities Index, a single score combining many benchmarks. Including unreleased internal models, dated by when most Anthropic employees could use them, METR estimates growth since October 2025 at 1.9 times the earlier rate, with a 95 percent confidence interval of 1.5 to 2.8. Different modelling choices gave between 1.1 and 2.9 times. Most METR staff believe Anthropic is improving on well-specified tasks at about twice its March 2024 to October 2025 rate, and would not be surprised by anything from 1.3 to 3 times.

On causes, METR says it is confident that faster growth in training compute did not drive the acceleration, and puts the share of October 2026 acceleration due to AI at perhaps 80 percent, with substantial uncertainty. It found no clear bottlenecks in algorithms, compute or data but says its view changed several times and it is not confident. Staff polls reported self-assessed uplift of about 12 times; METR calls these very loose evidence and says they are not acceleration rates.

What cannot be verified by anyone outside is most of the underlying evidence. METR states that "Anthropic redacted a majority of the evidence we found most informative", including algorithmic progress estimates, bottleneck details and forecasts. Anthropic says the redactions remove information that could accelerate other developers. Anthropic also cancelled a planned check of compute allocation partway through. METR worked on Anthropic devices, received free tokens, did not sample from non-public models, and says it took no payment. The independent coverage found for this post (Resultsense, Unite.AI) summarises the report; neither adds outside expert analysis or reproduces the numbers.

## Why it matters

The report is an outside estimate, based on internal data, of how fast a frontier lab's own capability growth has been changing, a question usually answered only by the lab itself. If the estimate holds, capability gains that once took two years arrive in about one, which compresses the time available for safety testing and policy responses. It also sets a precedent for how outside evaluation with company-controlled redaction works in practice.

## Open questions and other views

METR lists reasons it might be overestimating: non-AI factors could explain all or most of the acceleration, gains might be confined to well-specified tasks, and Anthropic's historical baseline may have been unusually slow. It also lists reasons it might be underestimating, including that its index could understate real-world impact. Benchmark saturation, with the newest internal model above 50 percent on all 15 benchmarks, may make future measurement harder.

Supporters of this kind of engagement can point out that a lab opening internal data to an unpaid outside group, and allowing it to say what was redacted, is more than the public otherwise gets. Critics of the arrangement focus on the redactions: Resultsense, in its own commentary, presents them as the main lesson for policy, since conclusions resting on hidden evidence ask the public to trust the evaluator. METR itself says the redactions leave the public relying on its judgment more than would be ideal. Whether this model of oversight is adequate is unresolved.

## Sources

- METR, "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026", 5 November 2026. https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
- METR, "Review of the 'Risks from automated R&D' section in Anthropic's Risk Report (August 2026)", 5 November 2026. https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/
- Resultsense, "METR: AI has likely doubled Anthropic's pace of model improvement", 6 November 2026. https://www.resultsense.com/news/2026-11-06-metr-anthropic-ai-rd-acceleration/
- Unite.AI, "METR Estimates Anthropic's Model Capability Growth Has Nearly Doubled", 5 November 2026. https://www.unite.ai/metr-estimates-anthropics-model-capability-growth-has-nearly-doubled/
