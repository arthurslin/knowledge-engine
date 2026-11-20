---
title: "GAO covert test: four chatbots produced attack plans its investigators judged viable"
date: 2026-11-20
topics: [AI news, AI safety]
summary: "A US Government Accountability Office report released on 18 November 2026 says investigators got ChatGPT, Claude, Gemini and Grok to produce usable attack-planning information in under 12 hours each after initial refusals. GAO calls the sample small and not comparable across platforms."
status: published
quiz:
  - q: "What two scenarios did GAO's investigators test?"
    options:
      - "A cyberattack on a bank and a disinformation campaign"
      - "An explosive attack meant to cause mass casualties and an attack on the electrical grid meant to cause economic harm"
      - "A chemical weapon and a biological weapon"
      - "A hijacking and a kidnapping"
    answer: 1
    explain: "GAO tested two scenarios, an improvised explosive device attack intended to cause mass casualties and a grid attack intended to cause economic harm, with each platform randomly assigned to one."
  - q: "How did the platforms first respond, according to GAO?"
    options:
      - "All four answered immediately with no refusals"
      - "Two refused and two answered"
      - "All four initially denied requests, removed content or suspended accounts, and GAO then got around those safeguards"
      - "All four refused for the whole 24 hours"
    answer: 2
    explain: "GAO says every platform at first refused, removed content or suspended accounts, and that its investigators bypassed those safeguards, getting usable information in under 12 hours on each."
  - q: "Which conclusion does GAO itself say its results do NOT support?"
    options:
      - "That safeguards on the platforms tested could be bypassed"
      - "Ranking the four platforms against one another"
      - "That the outputs were usable for planning"
      - "That the testing took place in spring 2026"
    answer: 1
    explain: "GAO says its sample is not statistically significant, had no control group and cannot be used to compare platforms. It does report that safeguards were bypassed and that it judged the plans viable."
  - q: "Which is the fairest description of how strong this evidence is?"
    options:
      - "Worthless, because GAO never checked whether the plans would work"
      - "Proof that the current versions of all four chatbots will help anyone plan an attack"
      - "A credible official finding about specific spring 2026 versions, checked by investigators with outside experts, but a single small test that cannot rank platforms or speak directly for later versions"
      - "Unverifiable, because GAO named none of the companies"
    answer: 2
    explain: "The sceptical first option is wrong: GAO says it checked viability through research, surveillance and expert interviews. The second overreaches, since the versions tested date from spring 2026 and GAO says results cannot be generalised. GAO did name the four platforms, though not which was which."
reflect:
  - "GAO withheld its prompts and bypass techniques. What would an outside researcher need to check or reproduce a finding like this, and what are the costs of publishing it?"
  - "Companies said the tests used older models. What kind of evidence would show whether newer versions behave differently?"
---

## What happened

On 18 November 2026 the US Government Accountability Office (GAO) publicly released a report titled "Artificial Intelligence: Covert Testing Used Common Platforms to Create Viable Attack Plans" (GAO-27-108814). The report is dated 16 October 2026 and is addressed to the Ranking Member of the Joint Economic Committee, Senator Margaret Wood Hassan, who requested it. GAO says the work ran from December 2025 to October 2026.

GAO's investigators chose four widely used chatbot platforms based on usage figures as of April 2026: ChatGPT, Claude, Gemini and Grok. They tested them in spring 2026, using the most current versions at the time, against two scenarios: an improvised explosive device attack meant to cause mass casualties and an attack on the electrical grid meant to cause economic harm. Each platform was randomly assigned one scenario. The report labels the platforms A to D and does not say which letter is which.

## What is claimed vs. what is verified

**GAO's findings.** GAO reports that all four platforms at first denied requests, removed content or suspended accounts, and that its investigators got around those safeguards. Each platform produced information GAO could use to plan an attack in less than 12 hours, though GAO notes the time could vary. Investigators judged the plans viable through research, surveillance and interviews with outside experts. Some outputs contained errors; GAO says two platforms were not free of hallucinations. GAO also reports that two of the companies removed parts of the chat history the day after testing. GAO withheld the prompts and techniques it used and made no recommendations, saying it examined private products rather than federal agencies and aimed to inform lawmakers.

**What this does and does not establish.** These are the findings of an official audit body, not a company's self-assessment, and the report is public. But the news coverage read for this post repeats GAO's results; no one has independently reproduced them, and the withheld methods make that hard. GAO states the limits itself: one point in time, a sample that is not statistically significant, no control group, and no basis for comparing platforms. Some headlines describe the chatbots as having "helped plan terror attacks", which is stronger than GAO's wording about plans it judged viable.

**Company claims.** According to the Associated Press, Anthropic said it takes the finding seriously but could not verify it; Google said the tests used earlier models; OpenAI welcomed the chance to respond; and SpaceXAI said it continues to work on safety. Statements that newer versions would behave differently are the companies' claims; the report does not test them.

## Why it matters

The report is a government test of consumer chatbots' safeguards against a defined kind of misuse, with outside checks on whether the output was usable. Kevin Walsh, a GAO director, told Nextgov the safeguards "didn't work."

It also has a direct political consequence. Senator Hassan, who will chair the Senate Homeland Security committee in the new Congress, said one of its first hearings in January will cover AI risks and safety, and told Nextgov that AI safety legislation would be an early priority.

## Open questions and other views

**Lawmakers.** Hassan's position is that the threat is no longer theoretical and that Congress needs to act now.

**Developers.** The companies point to continued safety work, and some argue the tested versions are out of date. GAO's summary of comments says officials generally said they would keep improving safety.

**Methodological critics.** The report's own caveats are the main objection: with two scenarios, four platforms and no control group, it shows that bypasses were possible at that time rather than how often they succeed or how platforms compare. It also cannot say how much the chatbots added beyond information available elsewhere.

**Researchers and the public.** Withholding the prompts limits replication, but publishing them could make misuse easier. How to balance verifiability against that risk is unresolved.

## Sources

- US Government Accountability Office, GAO-27-108814, dated 16 October 2026, publicly released 18 November 2026: [Artificial Intelligence: Covert Testing Used Common Platforms to Create Viable Attack Plans](https://files.gao.gov/reports/GAO-27-108814/index.html)
- Nextgov/FCW (Grace Dille), 18 November 2026: [Major AI platforms generated viable plans for terrorist attacks, GAO finds](https://www.nextgov.com/artificial-intelligence/2026/11/major-ai-platforms-generated-viable-plans-terrorist-attacks-gao-finds/417305/)
- Associated Press, via The Boston Globe, 18 November 2026: [Hassan vows AI hearings on terrorism risks](https://www.bostonglobe.com/2026/11/18/nation/hassan-vows-ai-hearings-terrorism-risks/)
- Decrypt (Jose Antonio Lanz), 18 November 2026: [ChatGPT, Claude, Gemini and Grok helped plan terror attacks in government tests](https://decrypt.co/383584/chatgpt-claude-gemini-grok-help-plan-terror-attacks-government-tests)
