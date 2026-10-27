---
title: "What do field experiments say about AI and productivity?"
date: 2026-10-27
topics: [AI, economics]
summary: "Three widely cited studies of generative AI at work found a 14 percent gain for customer support agents, mixed results for management consultants, and a slowdown for experienced software developers. The differences between them say as much as the headline numbers."
status: published
quiz:
  - q: "In Brynjolfsson, Li and Raymond's customer support study, who gained most from the AI assistant?"
    options:
      - "Experienced, highly skilled agents, whose gains were about 34 percent"
      - "Novice and low-skilled agents, whose resolutions per hour rose about 34 percent"
      - "All agents equally, at about 14 percent each"
      - "Managers, who used it to monitor agents"
    answer: 1
    explain: "The 14 percent figure is the average. It hides a split: about 34 percent for novice and low-skilled agents, and minimal effect for experienced, highly skilled ones."
  - q: "What happened to consultants using GPT-4 on the task the BCG study placed outside AI's capability frontier?"
    options:
      - "They were 19 percent less likely to reach a correct answer than those without AI"
      - "They finished 25 percent faster with no change in accuracy"
      - "They refused to use the tool"
      - "Their accuracy improved by 12 percent"
    answer: 0
    explain: "On the 18 tasks inside the frontier, AI users completed more tasks, faster and at higher quality. On the one task outside it, they did worse. The 25 and 12 percent figures belong to the inside-frontier tasks."
  - q: "In METR's early-2025 trial, how did developers' own estimates compare with the measured effect?"
    options:
      - "They expected a slowdown and got one"
      - "They expected and reported about 20 to 24 percent speedups, while measured completion time rose about 19 percent"
      - "They reported no effect, and none was measured"
      - "They underestimated a large speedup"
    answer: 1
    explain: "Developers forecast a 24 percent speedup and afterwards estimated 20 percent, while tasks with AI allowed took about 19 percent longer. That gap between perception and measurement is one of the study's main findings."
  - q: "Which is the fairest judgement about the METR slowdown result?"
    options:
      - "It is untrustworthy because tasks were not randomly assigned"
      - "It settles that AI slows down all programmers"
      - "It was a randomised trial with 246 tasks, but only 16 developers, and METR's own later data with more developers pointed towards speedups with wide uncertainty"
      - "METR withdrew it after finding a calculation error"
    answer: 2
    explain: "Tasks were randomly assigned to allow or disallow AI, so the 'not randomised' objection sounds careful but is wrong. The real limits are the small number of developers and a specific setting; METR's late-2025 follow-up favoured a speedup, though both intervals included zero and METR flagged selection problems. METR did not withdraw the original."
reflect:
  - "The customer support and consulting studies both found the largest gains for weaker performers. What would you need to measure to tell whether those workers learned skills or simply relied on the tool, and why might it matter if the tool were removed?"
  - "Developers in METR's study believed they had been sped up when the measurement said otherwise. In your own work, which productivity claims rest on self-report, and how could you check one against a recorded outcome?"
---

## The idea

Since 2023 a handful of field experiments have tried to measure what generative AI does to real work, rather than to benchmark scores. Three are cited more than any others, and they do not point the same way.

The first, by Erik Brynjolfsson, Danielle Li and Lindsey Raymond, tracked 5,179 customer support agents at a single company as a conversational AI assistant was rolled out in stages. Access raised issues resolved per hour by 14 percent on average. The average hid a split: novice and low-skilled agents gained about 34 percent, while experienced, highly skilled agents saw minimal change. The authors suggest the tool spread the practices of the best agents to everyone else. Customer sentiment and employee retention also improved. The paper appeared as an NBER working paper in 2023 and in the *Quarterly Journal of Economics* in 2025.

The second, led by Fabrizio Dell'Acqua with colleagues at Harvard Business School and Boston Consulting Group, ran a preregistered experiment with 758 BCG consultants, randomly assigned to work without AI, with GPT-4, or with GPT-4 plus a short prompting overview. On 18 realistic consulting tasks judged to be within the model's abilities, AI users completed 12.2 percent more tasks, worked 25.1 percent faster and produced significantly higher quality. On one task designed to fall outside those abilities, they were 19 percent less likely to reach a correct answer. The authors called the boundary a "jagged technological frontier": inside it the tool helps, outside it the tool can mislead.

The third, from the research group METR, was a randomised controlled trial with 16 experienced open-source developers working on 246 real tasks in projects they knew well, each task randomly assigned to allow or disallow AI tools, mainly the Cursor editor with Claude 3.5 and 3.7 Sonnet. Developers expected a 24 percent speedup and afterwards believed they had got 20 percent. Measured completion time instead rose by about 19 percent. Outside experts in economics and machine learning had predicted time savings of 38 to 39 percent.

## Why it might change a decision

Taken together, the studies predict that average gains will be larger where workers are less experienced and where tasks sit well inside what the model does reliably, and smaller or negative for experts on familiar, complex material. They also predict that people's own sense of being sped up is a poor guide: a team that measured completion time on comparable tasks, with and without AI, could find a different answer from a team that surveyed its staff.

## How solid is this?

Each result comes from a single study in one setting, and they differ in design. The customer support study used a staggered rollout at one firm rather than randomising individuals, which supports causal claims under assumptions about timing but is not a lottery. The BCG study was randomised and preregistered, but its tasks were constructed for the experiment and consultants are a selected group. HBS lists it as forthcoming in *Organization Science*. The METR trial randomised tasks, but 16 developers is a small sample, and the confidence interval on its estimate, reported by METR as 2 to 39 percent longer, is wide.

METR itself ran a larger follow-up in late 2025 with 57 developers and more than 800 tasks. Its February 2026 update reported point estimates that now favoured AI, both for returning and for newly recruited developers, but with confidence intervals that included no effect. METR called this data an unreliable signal, because developers increasingly declined to work without AI and withheld tasks they did not want to do unaided, so the most AI-dependent work was likely missing.

The strongest competing explanation for the contrasts is not that one study is right and the others wrong, but that the effect depends on worker experience, task type and the tools available at the time. Popular summaries that quote a single figure, whether 14 percent faster or 19 percent slower, outrun what any one of these studies can support. Whether gains for less experienced workers reflect learning or dependence on the tool is still open.

## Sources

- Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. *Quarterly Journal of Economics*, 140(2), 889-942. [doi:10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044). Working paper: [NBER w31161](https://www.nber.org/papers/w31161)
- Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of artificial intelligence on knowledge worker productivity and quality. *Harvard Business School Working Paper* 24-013. [hbs.edu](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700)
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. [arXiv:2507.09089](https://arxiv.org/abs/2507.09089)
- METR. (2026, February 24). We are changing our developer productivity experiment design. [metr.org](https://metr.org/blog/2026-02-24-uplift-update/)
