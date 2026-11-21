---
title: "Amazon says attackers' AI agents found and used an unknown flaw to take over a university server"
date: 2026-11-21
topics: [AI news, AI safety]
summary: "On 20 November 2026 Amazon reported that a suspected China-linked operator used Cairn, an open-source AI penetration-testing framework, against East Asian universities, and that its agents found and exploited a previously unknown flaw in medical imaging software. The account rests on Amazon's analysis of an exposed server; outlets have not independently verified it."
status: published
quiz:
  - q: "How did Amazon learn what the operator's agents had done?"
    options:
      - "From a confession posted online by the attackers"
      - "By finding a publicly hosted Cairn server, running without authentication, whose history showed prompts, configurations and AI output"
      - "From the university, which handed over its server logs"
      - "By running Cairn itself against the same targets"
    answer: 1
    explain: "Amazon says it found an unauthenticated Cairn server on 10 September 2026 and read its operational history. That is the main evidence base for the whole account."
  - q: "According to Amazon, what did the human operator provide?"
    options:
      - "Nothing; the agents chose their own targets"
      - "Step-by-step commands for each action"
      - "A goal of obtaining shell access and a list of target addresses, plus, in one session, a proxy into a second network"
      - "Only the exploit code for the flaw"
    answer: 2
    explain: "Amazon describes the agents planning and adjusting steps themselves, but the operator set the goal and the targets. It is not a story of agents choosing whom to attack."
  - q: "Which of these did most of the campaign's attempts look like?"
    options:
      - "Quick successes on nearly every target"
      - "Long attempts that failed, such as about 16 hours against a Redis server and over 30,000 credential guesses against a GPU server"
      - "Attacks on hospitals"
      - "Attacks on cloud accounts at Amazon"
    answer: 1
    explain: "Amazon reports several lengthy attempts that did not succeed. The success it highlights is the medical imaging flaw, exploited in about 11 minutes once the agents mapped the software's interface."
  - q: "Which is the fairest description of the evidence?"
    options:
      - "Fabricated, since no flaw was ever confirmed"
      - "A detailed first-hand account from a security vendor, partly corroborated by a maintainer advisory and by separate reports of Cairn misuse, but not independently reproduced, with attribution at moderate confidence"
      - "Proof that AI agents can now hack any system without human help"
      - "Unreliable, because Amazon named the attacker group without evidence"
    answer: 1
    explain: "The sceptical options are wrong: Amazon says the maintainers released a fix and an advisory, and Amazon did not name a group, giving its attribution only moderate confidence. The third option overstates what one exploited flaw in one application shows."
reflect:
  - "Cairn was built for defenders and used by attackers. What, if anything, should change about how open-source security tools are published?"
  - "Amazon recommends automated responses with humans overseeing outcomes rather than each action. What failure modes does that create, and how would you test for them?"
---

## What happened

On 20 November 2026, Amazon published a post on its AWS Security Blog by CJ Moses, the chief information security officer of Amazon Integrated Security, describing work by Amazon Threat Intelligence. Amazon says that on 10 September 2026 it found a publicly hosted server running Cairn, which it describes as an open-source autonomous AI penetration-testing framework, with no authentication. The server's history showed the operator's prompts, project settings and the AI's output.

According to Amazon, the operator ran a roughly 48-hour campaign beginning 8 September against addresses tied to universities in East Asia outside mainland China. Amazon did not name the universities or the country. It attributes the activity with moderate confidence to a Chinese-nexus actor, citing Simplified Chinese prompts, China Standard Time timestamps and the choice of targets. It names no group.

Most attempts failed. Amazon describes about 16 hours and 148 actions against a Redis server, and more than 30,000 credential combinations tried against a GPU server, without success. The success was against what Amazon calls an open-source medical imaging AI application; the advisory it links is for Project MONAI's MONAI Label. Amazon says the agents found a path traversal flaw in a file upload feature and, about 11 minutes after mapping the software's interface, could write arbitrary files. They then planted a reverse shell and obtained root access. Amazon says it notified the maintainers, who released a fix and a GitHub security advisory.

## What is claimed vs. what is verified

**Amazon's claims.** The core account comes from Amazon's reading of the exposed server. Its judgement that the flaw was a true zero-day, which it holds with high confidence, rests on there being no prior fix, issue or advisory. Its claim that the operator then used the flaw to compromise a proxy server at a second university is, by Amazon's own description, an inference.

**What others add.** The Register and The Record both reported the post on 20 November. Neither independently verified Amazon's findings, and neither carried a response from the MONAI maintainers. They do add context that does not come from Amazon: The Register cites Gambit Security's earlier report that a Chinese operator used Cairn in at least 105 attacks, compromising at least 27 companies to varying degrees. The Record says Google researchers separately reported Cairn being used in intrusions at US aerospace companies, and notes an FBI advisory on a different AI attack tool, Artex, a week earlier. Those reports point to Cairn being misused, but they do not confirm the university incident itself.

**On autonomy.** Amazon says the agents planned, executed and adjusted steps without the operator choosing each one. The operator still supplied the goal, the targets and, in one session, access into a second network.

## Why it matters

If accurate, this is a documented case of an AI agent framework finding a previously unknown vulnerability during a live attack, rather than in a lab or contest. The flaw was in research software used for medical imaging, so other institutions running it needed the fix. Amazon's response is to recommend that defenders let high-confidence detections trigger automated responses, with people reviewing outcomes rather than approving each action. Amazon sells cloud security services, so it has an interest in this recommendation.

## Open questions and other views

**Security vendors and defenders.** Amazon's position is that attacks now move at machine speed and defence has to as well. Gambit Security's Eyal Sela told The Record that Cairn is notable because it is not built around cybersecurity specifically.

**Sceptics of the framing.** One counterpoint is that the success came against research software, through a common class of flaw, after long failed attempts elsewhere. On that reading the case shows persistence and speed more than unusual skill. The other vendor reports describe Cairn's misuse at scale but do not say how often its successes came from new flaws rather than known weaknesses.

**Open-source maintainers and tool authors.** Cairn was built for defenders. Whether to restrict such frameworks, and how, is unresolved: limits could slow attackers but also hinder the defenders they were written for.

**Attribution.** Amazon's moderate-confidence attribution relies on language, time zone and targeting, signals that can be imitated. Readers have no way to check it independently.

## Sources

- Amazon Web Services, AWS Security Blog (CJ Moses), 20 November 2026: [Chinese-nexus actor's Cairn AI agents found a zero-day on their own](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)
- The Register (Jessica Lyons), 20 November 2026: [China attackers deployed AI agents that autonomously found and exploited a 0-day to take over a university server](https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382)
- The Record, Recorded Future News (Jonathan Greig), 20 November 2026: [Amazon says Chinese hackers used Cairn AI tool to discover apparent zero-day during attack on university](https://therecord.media/amazon-research-cairn-ai-university-attacks-possible-zero-day)
