---
title: "Gemini 4 Carbon tops an independent index, but only vetted cyber defenders can use it"
date: 2026-11-04
topics: [AI news, AI]
summary: "On 28 October Google announced Gemini 4 Carbon, released first to a vetted group of cybersecurity defenders rather than the public. An independent index ranks it narrowly first, while most of its security and safety numbers are Google's own and have not been reproduced."
status: published
quiz:
  - q: "Who could use Gemini 4 Carbon in the week it was announced?"
    options:
      - "Anyone through the Gemini app"
      - "Developers through the public API at introductory prices"
      - "A subset of cyber defenders admitted through Google's Fairwind Program"
      - "Only Google employees"
    answer: 2
    explain: "Google gave first access to selected cyber defenders and said other trusted partners would follow. The model was not in the Gemini app, AI Studio or the public API, and no date was given for broad release."
  - q: "Which of these results comes from an organisation independent of Google?"
    options:
      - "88.2 percent on SEC-bench Pro"
      - "A score of 59 on the Artificial Analysis Intelligence Index, one point ahead of the next model"
      - "Roughly half as many unsupported claims as Argon"
      - "An 80 percent drop in high-severity misalignment alerts"
    answer: 1
    explain: "Artificial Analysis, a third-party benchmarking group, produced the index score. The SEC-bench Pro figure was run by Google in its own harness, and the other two are internal Google measurements."
  - q: "What did Google say about how its external cybersecurity benchmarks were run?"
    options:
      - "They were run with all safety guardrails switched on"
      - "They were run without guardrails"
      - "They were run by the US government"
      - "They were not run at all yet"
    answer: 1
    explain: "Google's post states the external cyber benchmarks were evaluated without guardrails, which means customers using the guarded product may see different results."
  - q: "A reader says: 'The 59 versus 58 lead is meaningless because Artificial Analysis could not test Carbon at all without a public API.' How well does this fit the reporting?"
    options:
      - "It fits: no independent score exists, only Google's claim"
      - "It does not fit: Artificial Analysis did publish scores for Carbon, though it noted the lack of a public API; the narrow margin is a fairer reason for caution"
      - "It fits: Artificial Analysis withdrew its ranking"
      - "It does not fit: Carbon led by more than ten points"
    answer: 1
    explain: "Artificial Analysis did score Carbon and noted it lacked a public API. The sceptical-sounding claim that there is no independent score is factually wrong. The better reason for caution is that a one-point lead on a composite index is small, and Carbon was below rivals on some of the same group's other tests."
reflect:
  - "Google released its strongest model to defenders first, on the reasoning that its exploit-finding skills are dual-use. What evidence would show whether a staged release like this actually reduces misuse?"
  - "Most of the security numbers here were produced by the developer, in its own harness. What would an independent replication need to control for to be convincing?"
---

## What happened

On 28 October 2026 Google announced Gemini 4 Carbon in a blog post by Koray Kavukcuoglu, chief AI architect at Google and a senior vice president at Google DeepMind. It arrived two weeks after Gemini 4 Argon, which remains Google's publicly available model. Google describes Carbon as its strongest model, emphasising long-running agentic coding and cybersecurity work.

Unusually for a flagship model, Carbon was not released to the public. Google said access would start with "a subset of cyber defenders" and expand to other trusted partners through what it calls the Fairwind Program. The AI news site Nowrap reported that the programme covers vetted governments, national cyber agencies, critical-infrastructure operators and large technology platforms, with background checks. Google said it would make Carbon available to developers, businesses and consumers "as soon as possible", without a date, and that it is taking part in the US government's voluntary pre-release model testing. It listed introductory pricing of $2 per million input tokens and $10 per million output tokens, rising later to $4 and $20.

## What is claimed vs. what is verified

Most of the headline figures are Google's own. The company says Carbon scored 88.2 percent on SEC-bench Pro, a test of finding software vulnerabilities, 54.8 percent on ExploitGym, which tests exploiting them, and 71.0 percent on CWE-bench for patching. Google notes these external cyber benchmarks were run without guardrails. Nowrap reports that Google ran SEC-bench Pro and ExploitGym itself in its own Antigravity harness, and points out that harness and settings choices can move agentic scores by many points. Those numbers are claims until someone outside Google reproduces them.

The safety figures are internal too. Google says Carbon makes roughly half as many unsupported claims as Argon, and that high-severity misalignment alerts in live coding environments fell by almost 80 percent. It also cites a claim from its Chrome team that Carbon was more than ten times better at producing high-quality patches than an unnamed rival model. VentureBeat's Carl Franzen noted that Google gave no uncertainty estimates and no technical report, and that the unnamed rival makes the Chrome comparison impossible to check. The Google post links only a safety report that is presented in the context of Argon.

Some independent evidence does exist. Artificial Analysis, a third-party benchmarking group, ranks Carbon first on its Intelligence Index v5.0 with 59, ahead of Claude Opus 5.5 at 58, GPT-6 Astra at 57 and Argon at 50, while noting that Carbon has no public API. On the same group's other measures, as reported by VentureBeat, the picture is mixed: Carbon scored 59 on a coding-agent index where Claude Code with Opus 5.5 scored 62, and it ranked below several rivals on an Elo-style comparison called AA-Briefcase. On AA-Omniscience it answered more questions correctly than Argon, but its hallucination rate on that test rose from 4 to 11 percent. Nowrap reports a separate third-party index, Vals, at 70.4 percent for Carbon against 70.2 for Opus 5.5.

## Why it matters

Carbon is a test of a release strategy as much as a model. Google is treating strong vulnerability-finding and exploitation skills as dual-use, giving defenders a head start before wider access. If that becomes common, the most capable systems may increasingly be available first to governments and large institutions rather than to the public or independent researchers.

The release also shows how thin independent checking can be at launch. With no public API, outside evaluators can test only through whatever access they are granted, and the cybersecurity claims, which motivate the restricted release, are among the least verified.

## Open questions and other views

Google's position is that staged access lets defenders patch software before attackers gain similar tools, and that it will widen access once guardrails are refined. The case for caution rests partly on the jump in exploitation scores, from 42.0 to 54.8 percent on ExploitGym by Google's figures, as VentureBeat reported.

The reporting raises other points. A one-point lead on a composite index is a narrow margin, and Carbon trailed rivals on some coding and computer-use tests in Google's own comparison table. Developers and smaller security firms outside the programme cannot verify the claims or benefit from the model, which concentrates both capability and evaluation in a few hands. Without a model card or technical report for Carbon, which VentureBeat noted is missing, outside researchers have little against which to assess the safety claims.

What remains open: when, or whether, Carbon reaches general release; whether independent groups can reproduce the security scores with guardrails on; and what the US pre-release testing found, which Google has not described.

## Sources

- Google, "Gemini 4 Carbon: our next frontier model", Koray Kavukcuoglu, 28 October 2026. https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- VentureBeat, "Google unveils Gemini 4 Carbon, retaking the world's no. 1 spot on updated, harder benchmarks, but access is limited", Carl Franzen, 28 October 2026. https://venturebeat.com/technology/google-unveils-gemini-4-carbon-retaking-the-worlds-no-1-spot-on-updated-harder-benchmarks-but-access-is-limited
- Nowrap, "Google's Gemini 4 Carbon takes No. 1, but access is limited", 29 October 2026, updated 3 November 2026. https://nowrap.ai/news/google-gemini-4-carbon-launch
- 9to5Google, "Google announces Gemini 4 Carbon with 'significant' coding gains", Abner Li, 28 October 2026. https://9to5google.com/2026/10/28/gemini-4-carbon-announcement/
