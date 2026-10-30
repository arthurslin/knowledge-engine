---
title: "Mistral releases the weights of Large 4: what the numbers do and do not show"
date: 2026-10-30
topics: [AI news, AI]
summary: "Mistral has published the weights of Large 4, a mixture-of-experts model of about one trillion parameters, under a modified MIT licence. Most headline benchmark figures come from Mistral itself; the main independent index so far places it behind two Chinese open-weight rivals."
status: published
quiz:
  - q: "What does Mistral's licence for Large 4 restrict, according to the announcement?"
    options:
      - "All commercial use"
      - "Use by companies above a revenue threshold"
      - "Offering the model as a hosted service, which needs a separate commercial licence"
      - "Fine-tuning the model"
    answer: 2
    explain: "Mistral calls it a modified MIT licence that allows use, modification, fine-tuning and commercial use. The one restriction it states is that businesses selling the model as a service need a separate licence. No revenue threshold is mentioned."
  - q: "On Artificial Analysis's Intelligence Index v5, how does Large 4 (high reasoning) compare with GLM-5.3 and DeepSeek V4.1 Flash?"
    options:
      - "It scores higher than both"
      - "It scores 26, against 32 for each of them"
      - "It ties with both"
      - "Artificial Analysis has not tested it"
    answer: 1
    explain: "XenoSpectrum reports, citing Artificial Analysis, scores of 26 for Large 4 and 32 for each rival. Large 4 costs less per task than GLM-5.3 but more than DeepSeek V4.1 Flash."
  - q: "Mistral says Large 4 refuses 96.6 percent of malicious cyber requests. What is the status of that figure?"
    options:
      - "It is a claim measured by Mistral that no independent party has yet reproduced"
      - "It was certified by a government safety institute"
      - "It is meaningless, because refusal rates cannot be measured"
      - "It was measured by Artificial Analysis"
    answer: 0
    explain: "The figure comes from Mistral's own announcement. Refusal rates can be measured, so dismissing it as meaningless goes too far; the point is that it remains a self-reported number until others test it, and results depend on which prompts are used."
  - q: "Why do earlier and current Intelligence Index scores for Large 4 (38 in mid-October, 26 now) not show that the model got worse?"
    options:
      - "Because the earlier score was a typo"
      - "Because the scores come from different versions of the index and partly different versions of the model, so they are not on the same scale"
      - "Because Mistral asked for the earlier score to be removed"
      - "They do show the model got worse"
    answer: 1
    explain: "The Batch reported 38 for the API preview in mid-October; the current figure of 26 is on Intelligence Index v5. Comparing across index versions is like comparing marks from two different exams."
reflect:
  - "Most of the benchmark numbers in a release announcement are chosen and measured by the company releasing the model. What would you want to see before trusting a claim like 'best open-weight model for coding'?"
  - "Mistral released a model that it says still showed potential for real-world cyber uplift, while keeping a less restricted variant for vetted partners. What are the strongest arguments for and against releasing weights in that situation?"
---

## What happened

On 29 October 2026 the French company Mistral AI published the weights of Mistral Large 4, its largest model, on Hugging Face. The release date is given by Artificial Analysis's model listing and by XenoSpectrum's report; Mistral's own post describes the release as happening "today" without a date. The model had been available earlier in October as an API preview, and Mistral had said then that weights would follow by the end of the month.

Large 4 is a mixture-of-experts model with about one trillion parameters in total (Mistral says 1T; DeepLearning.AI's The Batch reported 1.05 trillion) and about 52 billion active for each token, according to The Batch and Artificial Analysis. It accepts text and images, has three reasoning settings, and Artificial Analysis lists a context window of one million tokens. It is released under what Mistral calls the Mistral Ecosystem Open-Weight licence, a modified MIT licence that allows commercial use and fine-tuning but requires a separate agreement for anyone selling the model as a hosted service. API pricing is $0.70 per million input tokens and $2.10 per million output tokens.

## What is claimed vs. what is verified

**Mistral's claims.** The company describes Large 4 as the best open-weight model for coding. It reports 41 percent on Terminal-Bench 4.0 (up from 28 percent for the preview), 48 percent on Artificial Analysis's Coding Agent Index, 19.7 percent on Cognition's private FrontierCode 2.0 benchmark, and 84.5 percent on BrowseComp. It says the model refuses 96.6 percent of malicious cyber requests and resists 97.1 percent of attacks on the B3 agent security benchmark. These figures appear in Mistral's own post; several cite outside benchmarks but were reported by Mistral, and none of the refusal or security numbers has been reproduced by an independent group so far.

**Independent evidence.** Artificial Analysis, a firm that runs its own evaluations, gives Large 4 at its high reasoning setting a score of 26 on its Intelligence Index v5, above the median of 23 for comparable models. XenoSpectrum, citing the same firm, notes that GLM-5.3 and DeepSeek V4.1 Flash each score 32. Large 4 costs less per task than GLM-5.3 ($2.06 against $5.01) but more than DeepSeek V4.1 Flash ($0.60). Artificial Analysis also measures output speed of about 161 tokens per second, well above the class median. XenoSpectrum points out that it lists a FrontierCode figure different from Mistral's, and that reasoning settings and index versions differ across comparisons, so not every figure is like for like.

An earlier analysis of the preview by The Batch, on 16 October, reported a score of 38 on a previous version of the index and called the model's cost per task high compared with rivals at the same score. Because the index has since changed version and the model was still in training, those numbers cannot be compared directly with today's.

## Why it matters

Large 4 is among the largest models whose weights anyone can download, and it comes from a European company at a time when the strongest open-weight models have mostly come from Chinese labs. Organisations that cannot send data to an outside API can now run a model of this size on their own hardware, subject to the licence.

The release also tests how labs handle cyber capability in open models. Mistral writes that after the preview it still saw potential for real-world uplift in attacks and is adjusting its guardrails. A less restricted cybersecurity variant remains limited to vetted partners. Safeguards built into a model can be weakened by anyone who fine-tunes the open weights, which is a general limitation of this approach rather than a finding about Large 4.

## Open questions and other views

Supporters of open weights argue that releases like this let researchers audit models, let smaller firms and governments avoid dependence on a few providers, and spread the benefits of defensive security tools. Critics of releasing highly capable models argue that refusal training can be removed after release and that cyber uplift, which Mistral itself acknowledges, is hard to take back once weights are public.

On performance, the open question is how Large 4 does on evaluations Mistral did not choose. Independent results so far come mainly from one firm, and the gap with Chinese rivals rests on a single aggregate index.

## Sources

- Mistral AI, "Mistral Large 4 (Le Chonk) is now open weight," company announcement, October 2026. [mistral.ai](https://mistral.ai/news/mistral-large-4-oss/)
- Artificial Analysis, Mistral Large 4 model page, accessed 30 October 2026. [artificialanalysis.ai](https://artificialanalysis.ai/de/models/mistral-large-4)
- Y. Kobayashi, "Mistral Large 4 Open Weights Released: Better Coding Efficiency, but Gaps With Chinese Rivals Remain," XenoSpectrum, 29 October 2026. [xenospectrum.com](https://xenospectrum.com/en/mistral-large-four-open-weights/)
- DeepLearning.AI, "Mistral's skills match its global appeal," The Batch, 16 October 2026. [deeplearning.ai](https://www.deeplearning.ai/the-batch/mistrals-skills-match-its-global-appeal/)
