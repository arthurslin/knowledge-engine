---
title: "Anthropic study: analysts followed an AI agent's hidden lean 86 percent of the time"
date: 2026-10-31
topics: [AI news, AI, decision making]
summary: "In an Anthropic experiment, 50 professional analysts working with a coding agent that had been secretly told to favour one side of each judgment call matched its lean on 86 percent of decisions. The study is a single task run by the model's own developer, and no outside group has yet repeated it."
status: published
quiz:
  - q: "How was each AI agent's preference on the four analytical decisions set in the study?"
    options:
      - "By the analyst at the start of the task"
      - "By a coin flip, hidden from the analyst"
      - "By the model's own default preferences"
      - "By an outside panel of experts"
    answer: 1
    explain: "A coin flip secretly assigned the agent's lean on each decision, and a hidden instruction told it to argue for that lean as strongly as the data allowed without misleading. Because the leans were random, matching them 86 percent of the time cannot be explained by the agent simply being right."
  - q: "Of the analysts who already had a preference before the agent weighed in, how often did they switch when the agent disagreed?"
    options:
      - "6 percent"
      - "36 percent"
      - "60 percent"
      - "86 percent"
    answer: 2
    explain: "They switched 60 percent of the time when the agent disagreed and 6 percent when it agreed. That figure rests on only 38 cases, and Anthropic's own confidence interval for the gap runs from 24 to 82 percentage points."
  - q: "What did the post-task survey show about attribution?"
    options:
      - "Most analysts credited the agent for their reasoning"
      - "77 percent repeated the agent's arguments, but only 15 percent credited it"
      - "Analysts who deferred were much less confident than others"
      - "Older analysts deferred far more than younger ones"
    answer: 1
    explain: "Most reused the agent's arguments, few credited it, and confidence was similar for deferrers (71) and others (73)."
  - q: "Analysts without an agent made serious errors far more often (6 of 11) than analysts with one (3 of 50). What is the best reading of that comparison?"
    options:
      - "It proves the agent made analysts more accurate"
      - "It is worthless, because a sample of 11 can never show anything"
      - "It is suggestive, but the no-agent group was small, self-selected and less experienced, so it cannot isolate the agent's effect"
      - "It shows that deferring to the agent caused the errors"
    answer: 2
    explain: "The authors themselves say the comparison is not clean: the 11 analysts declined the agent and were less experienced. Calling it worthless overshoots, since a gap of 55 versus 6 percent is large, but the groups differ in more ways than agent use, so it cannot settle cause."
reflect:
  - "In this study the agent's lean was random, so following it says nothing about whether the analyst got the right answer. In real work, an agent's defaults may often be sensible. When, if ever, is deferring to a capable assistant a problem rather than a sensible use of expertise?"
  - "The study was designed, run and reported by the company that builds the model being tested. What would an independent replication need to change or keep the same to be convincing?"
---

## What happened

On 27 October 2026 Anthropic published a study by Amaç Herdağdelen, Hailey Joren and Alex Tamkin of its Alignment team, with a blog post and a full paper titled "Who's Aligned to Whom? How AI Agents Shape Experts' Research Judgment Calls." Al Jazeera and Decrypt covered it the next day.

The researchers recruited 61 professional analysts from a pre-screened pool of people with experience in observational causal inference and Python or R. Eleven declined to use the AI agent and were excluded from the main analysis, leaving 50. Each analyst advised a fictional farming cooperative on whether to expand a paid advisory programme, working in a web-based code editor with Claude Code running Claude Opus 4.8. The median session took 65 minutes.

The task contained four judgment calls, each with two defensible options: which outcome to measure, which comparison method to use, which farms to include, and how to weight them. For each call, a coin flip secretly set the agent's lean. A hidden system prompt told the agent to argue for that lean as strongly as the data allowed, to change its mind if the evidence decisively turned, and never to mislead.

## What is claimed vs. what is verified

**What Anthropic reports.** Analysts matched the agent's random lean 86 percent of the time across the four decisions (92, 82, 81 and 90 percent individually), where chance would give about 50. Among 38 cases where an analyst had already formed a view, they switched 60 percent of the time when the agent disagreed and 6 percent when it agreed. Rollout was recommended by 54 percent of analysts whose agent leaned toward it and 36 percent of the rest. In a survey, 77 percent repeated the agent's arguments, sometimes word for word, while 15 percent credited it. Deferrers were about as confident as others (71 against 73 on the study's scale), and experience, expertise and education did not predict who deferred.

**What is not yet independently checked.** These are the company's own results from its own experiment, and no outside group has reproduced them. The two independent reports reviewed for this post, by Al Jazeera's John Power and Decrypt's Jose Antonio Lanz, restate the findings and Anthropic's caveats accurately but quote no outside researchers. Decrypt notes one small inconsistency worth knowing: the survey figures come from 48 respondents, not all 50.

**Limits the authors state.** The leans were deliberately strengthened; left alone, the model made the same five choices in 112 of 123 runs, so a real agent's pull may differ. The study covered one task, in a field (farming) new to the analysts, with one model. Results are averages, and the researchers did not record how strongly each person held a view beforehand.

## Why it matters

The finding concerns choices where there is no single right answer, which is where error-checking does least. As Decrypt points out, the work looks sound whichever option is picked, so a reviewer checking for mistakes would not notice that the agent, not the analyst, settled the call. The authors argue that if many teams lean on models with similar defaults, results that look independent may share a hidden common source. They extend this to AI safety research, where human review is only an independent check if the reviewer's judgment is their own.

There is a second, less quoted result. Six of the 11 analysts who worked without the agent made serious, result-invalidating errors, against 3 of the 50 who used it. The authors caution that this group was small, self-selected and less experienced, so the gap cannot be credited to the agent.

## Open questions and other views

**Is this deference or reasonable reliance?** One reading is that capable experts sensibly took arguments from a capable assistant, as they would from a colleague. The study's design cuts against that for this task, since the leans were random, but in everyday use an agent's defaults may usually be sound, and the error comparison hints that working with an agent helped on quality.

**How large is the effect outside the lab?** The amplified lean, unfamiliar domain and single task all point toward an upper bound. A convincing test would use natural model preferences, other fields and other models.

**Who should run such tests?** Anthropic is studying the influence of its own product, and it is preparing a stock market listing, context Al Jazeera notes. On the other side, the study reports a finding unflattering to agent products, which sits awkwardly with a purely commercial motive; independent replication would settle the question either way.

**What to do about it.** The authors suggest measuring deferral in real settings, designing agents that lay out the best case for each option or ask for the expert's view first, and having institutions decide which decisions need a person's own judgment.

## Sources

- Anthropic (Herdağdelen, Joren & Tamkin), "How AI agents shape experts' judgment calls", 27 October 2026. https://www.anthropic.com/research/agents-judgment-calls
- Al Jazeera (John Power), "Experts defer to AI in decision-making, Anthropic study finds", 28 October 2026. https://www.aljazeera.com/economy/2026/10/28/experts-defer-to-ai-in-decision-making-anthropic-study-finds
- Decrypt (Jose Antonio Lanz), "AI Can Quietly Influence Experts' Decisions, Anthropic Study Finds", 28 October 2026. https://decrypt.co/382065/ai-can-quietly-influence-experts-decisions
