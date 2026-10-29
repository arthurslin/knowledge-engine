---
title: "Why automating a job can make the human part harder"
date: 2026-10-29
topics: [engineering, risk]
summary: "In 1983 Lisanne Bainbridge argued that automation leaves people with the rare, hard moments while taking away the practice they need to handle them. A small 2014 simulator study of airline pilots found a version of this: hand-flying held up, but the thinking skills behind it slipped."
status: published
quiz:
  - q: "According to Bainbridge, what does an operator typically get left with after a system is automated?"
    options:
      - "Only the routine tasks, since the machine takes the difficult ones"
      - "The tasks the designer could not work out how to automate, often including the rare abnormal situations"
      - "Nothing at all, since full automation removes the need for operators"
      - "Supervising other operators rather than the machine"
    answer: 1
    explain: "Bainbridge's point is that designers automate what they can and leave the rest to people. That remainder tends to include unusual, hard-to-predict situations, which is the opposite of an easier job."
  - q: "In Casner and colleagues' 2014 simulator study, which skills held up best among 747-400 pilots?"
    options:
      - "Navigating without the flight management computer"
      - "Diagnosing faulty instruments"
      - "Hand-eye skills such as scanning instruments and controlling the aircraft manually"
      - "None: all skills declined equally"
    answer: 2
    explain: "Pilots made few operationally significant errors when hand-flying, even though they said they rarely practised it. The bigger problems were cognitive: keeping track of position without the computer and recognising failed instruments."
  - q: "Which of Bainbridge's suggestions was described in the post?"
    options:
      - "Make automatic systems fail obviously rather than gracefully, and let operators take manual control for short periods each shift"
      - "Remove operators entirely once automation is reliable enough"
      - "Reduce operator training to cut costs, since the machine handles most work"
      - "Hide the computer's reasoning so operators are not distracted"
    answer: 0
    explain: "She proposed obvious failure, simulator practice and regular hands-on control to keep skills current. Hiding the computer's reasoning runs against her suggestion that operators be able to follow and check it."
  - q: "The study found pilots who reported more off-task thought made more navigation errors. What is the best reading of that result?"
    options:
      - "It proves that automation causes mind-wandering, which then causes errors"
      - "It is meaningless, because a sample of 16 cannot detect any relationship"
      - "It is a correlation in a small sample: consistent with the authors' idea about disengaged monitoring, but it does not establish cause"
      - "It shows that mind-wandering has no link to performance"
    answer: 2
    explain: "The correlation was statistically reliable even in 16 pilots, so dismissing it as meaningless is too sceptical: small samples can detect fairly strong relationships. But it is correlational, so it cannot show which way causation runs or rule out a third factor."
reflect:
  - "Think of a task you now hand to software, such as navigation, spelling or arithmetic. Which parts of the skill would you expect to keep, and which to lose, if the software failed next year?"
  - "Bainbridge suggested making automated systems fail obviously rather than gracefully. When might a graceful, quiet failure be the safer design despite her argument?"
---

## The idea

When a task is automated, the human operator does not disappear. They become the backup for the moments the machine cannot handle. In a short 1983 paper in the journal *Automatica*, Lisanne Bainbridge, a psychologist at University College London, argued that this creates a set of ironies. The more the machine does, the more crucial and the more difficult the human's remaining part becomes.

Her reasoning runs in several steps. Designers automate what they can and leave operators whatever is left over, which tends to be the rare, messy situations nobody could specify in advance. Manual control is a skill that fades without practice, so an operator who mostly watches becomes, over time, an inexperienced operator at exactly the moment they are needed. People are also poor at sustained watching of a system where almost nothing happens, so the monitoring role itself is hard. And understanding a process well enough to fix it depends on knowledge built by doing and getting feedback, which watching does not provide. A sudden handover can leave someone with little picture of what has been going on.

Bainbridge's paper was about process control in plants and factories, but aviation offers a clean test. In a study published in *Human Factors* in 2014, Stephen Casner and colleagues put 16 active Boeing 747-400 pilots, seven captains and nine first officers, into a high-fidelity simulator at NASA Ames. They flew arrivals, approaches and go-arounds with different levels of automation switched off, and they were asked at intervals whether their thoughts were on the task.

The result split in two. Hand-eye skills, such as scanning instruments and controlling the aircraft by hand, were largely retained, even though pilots said they rarely practised them. The cognitive skills were weaker. Navigating without the flight management computer, only one of the 16 completed the flight without an error; 44 percent missed the point at which an approach should be abandoned. When instruments failed, about three quarters followed a faulty altimeter off their assigned altitude, and nearly all followed a bad airspeed reading into repeated stall warnings.

## Why it might change a decision

The idea suggests a specific, testable expectation: the skill that decays under automation is less the physical act than the mental model of what is going on. That predicts, for instance, that a team which lets software handle routine work will do better in a failure if its members periodically run the task themselves end to end, including tracking state and diagnosing faults, than if they only practise the hands-on steps. Bainbridge's own suggestions follow the same logic: make automatic systems fail obviously rather than quietly, train in simulators for rare faults, and let operators take manual control for short periods each shift.

## How solid is this?

Bainbridge's paper is an argument, not an experiment. It draws on the human factors research of its time and has been very widely cited, but its claims are hypotheses for other work to test.

The empirical support described here comes mainly from one small study. Sixteen pilots is a tiny sample, all from one aircraft type, flying a simulator while knowing they were being assessed. The authors report that off-task thought was lower with less automation (about 20 percent of probes with full autoflight against 7 percent with raw data), and that pilots who reported more off-task thought made more navigation errors, a correlation explaining roughly 30 percent of the variation. That is a correlation, so it cannot show that automation caused the mind-wandering or that the mind-wandering caused the errors.

There are competing explanations. Pilots who rarely practise navigation without the computer may simply never have been trained to the same standard, so the pattern could reflect training rather than decay. The authors also note that recurrent training on puzzling indications did not seem to help with the failure scenarios, which complicates any simple fix. Other studies of pilots and of plant operators have reported related findings, but this post has not examined them, so it makes no claim about how consistently the result replicates.

The popular version of the idea, that automation makes people worse at everything, outruns this evidence. The study found hand-flying mostly intact; the losses were specific.

## Sources

- Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775-779. [PDF](https://gwern.net/doc/sociology/technology/1983-bainbridge.pdf)
- Casner, S. M., Geven, R. W., Recker, M. P., & Schooler, J. W. (2014). The retention of manual flying skills in the automated cockpit. *Human Factors*, 56(8), 1506-1516. [doi:10.1177/0018720814535628](https://doi.org/10.1177/0018720814535628)
