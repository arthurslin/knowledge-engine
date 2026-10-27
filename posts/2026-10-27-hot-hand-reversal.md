---
title: "Was the hot hand a fallacy after all?"
date: 2026-10-27
topics: [statistics, research methods]
summary: "For thirty years the hot hand in basketball was a textbook example of people seeing patterns in randomness. In 2018 two economists showed that the standard test was biased against finding streaks, and that correcting it reversed the classic result."
status: published
quiz:
  - q: "In three flips of a fair coin, what is the expected proportion of heads on flips that immediately follow a head, averaging over sequences where such a flip exists?"
    options:
      - "Exactly 1/2, because each flip is independent"
      - "5/12, a little below 1/2"
      - "2/3, because heads tend to cluster"
      - "1/4, because two heads in a row is rare"
    answer: 1
    explain: "Averaging the proportion within each of the six usable sequences gives 2.5/6, or 5/12. Each flip is independent, but the procedure of picking flips that follow a head and then averaging per sequence is not neutral, which is why 1/2 is the tempting wrong answer."
  - q: "According to Miller and Sanjurjo, how does streak selection bias change?"
    options:
      - "It grows as sequences get longer and shrinks for longer streaks"
      - "It is constant whatever the sequence or streak length"
      - "It shrinks as sequences get longer and grows for longer streaks"
      - "It only appears when the underlying hit rate is below 50 percent"
    answer: 2
    explain: "Longer sequences dilute the bias, while conditioning on longer streaks leaves fewer qualifying shots and makes it worse. The paper reports it stays substantial at sequence lengths commonly used in research, such as 100 shots."
  - q: "What did Bocskocsky, Ezekowitz and Stein's NBA tracking data add to the debate?"
    options:
      - "It showed players who are outperforming take harder shots, and still found a small hot hand after adjusting for difficulty"
      - "It showed NBA players have no streaks at all once defence is accounted for"
      - "It confirmed that fans underestimate how streaky players are"
      - "It replaced the Cornell experiment with a larger controlled shooting test"
    answer: 0
    explain: "Players on a run shot from farther out against tighter defence, which hides a hot hand in raw game data. After modelling shot difficulty the authors estimated an effect of 1.2 to 2.4 percentage points. It is game data, not a controlled experiment."
  - q: "Which is the fairest reading of the corrected Cornell result?"
    options:
      - "It cannot mean much, because the original study only had a handful of shots per player"
      - "It proves fans' beliefs about streaks are accurate in size as well as direction"
      - "It reverses GVT's headline: the average after-hits minus after-misses gap rises to about 13 percentage points, significant at the 1 percent level, though it comes from one 26-player study"
      - "It shows the original authors made an arithmetic error"
    answer: 2
    explain: "Each player took 100 shots, so 'only a handful of shots' sounds sceptical but is wrong. The fair caveats are that it is one small study of college players and says nothing about whether people perceive streaks in the right amount. The original calculation was standard practice, not an arithmetic slip; the bias was in the estimator."
reflect:
  - "Streak selection bias affects any measure of what happens after a run of outcomes in a finite sequence, such as a fund manager's good years or a salesperson's hot week. Pick one such claim and work out whether the evidence for or against streakiness used this kind of conditional proportion."
  - "If a real hot hand of a few percentage points exists, but players and fans may perceive a much bigger one, is the original 'fallacy' claim refuted, partly right, or answering a different question?"
---

## The idea

In 1985 Thomas Gilovich, Robert Vallone and Amos Tversky published a paper in *Cognitive Psychology* asking whether basketball players really get a "hot hand", a spell in which a run of made shots makes the next one more likely. Their cleanest test was a controlled shooting experiment with 26 players from Cornell's men's and women's teams, each taking 100 shots. Players hit 49 percent of shots after three hits in a row and 45 percent after three misses, a small gap that was not statistically significant. The authors concluded that belief in the hot hand was a widely shared cognitive illusion. The result became a standard teaching example of people seeing patterns in random sequences.

In 2018 Joshua Miller and Adam Sanjurjo showed in *Econometrica* that the standard test had a flaw. The usual method takes each player's sequence, finds the shots that follow a streak, computes the hit rate on those shots, and compares it with the rate after a streak of misses. Miller and Sanjurjo proved that, in a finite sequence, this measure is biased downwards even for a perfectly random shooter. They called it streak selection bias.

The coin version makes it concrete. Flip a fair coin three times. There are eight equally likely sequences. Drop the two (TTH, TTT) where no flip follows a head. For each of the other six, record the share of heads among flips that come right after a head: HHH gives 1, HHT gives 1/2, HTH gives 0, HTT gives 0, THH gives 1, THT gives 0. The average is 2.5/6, or 5/12, about 0.42, not 0.5. The coin has no memory; the shortfall comes from the way flips are selected. Within a short sequence, a head that follows a head uses up one of a limited number of heads, so the flips that follow are slightly more likely to be tails.

## Why it might change a decision

The bias predicts that a perfectly random shooter, measured this way, will look anti-streaky. So finding no difference does not mean no hot hand; it means performance after hits beat a baseline that should have been below zero. For any analysis of streaks in sports, markets or workplace performance, the testable implication is that a raw "after-streak minus after-non-streak" gap near zero should be read as weak evidence for streakiness, and should be compared against the expected bias for that sequence and streak length rather than against zero.

## How solid is this?

The mathematical result is a proof, not an empirical finding, and the paper states that the bias shrinks as sequences get longer but grows as the streak being conditioned on gets longer. For 100 shots, a 50 percent shooter and streaks of three, the expected after-hits minus after-misses difference for a random shooter is about minus 8 percentage points. Applied to GVT's Cornell data, the correction raises the average difference from about plus 3 to about plus 13 percentage points, significant at the 1 percent level. Miller and Sanjurjo describe this as reversing the canonical study's conclusion.

That reversal rests on a single small experiment with college players, so its size should be held loosely. The figures here come from the authors' arXiv version of the paper, which carries the same title as the published one.

Game data are harder, because defenders and shooters react. Andrew Bocskocsky, John Ezekowitz and Carolyn Stein, at the 2014 MIT Sloan Sports Analytics Conference, used optical tracking of more than 83,000 shots from the 2012-2013 NBA season. Players who had been outperforming took harder shots, from farther out and against tighter defence. After modelling shot difficulty they estimated a hot hand of 1.2 to 2.4 percentage points. This is a conference paper rather than a journal article, and the estimate depends on how well the difficulty model captures what defenders see.

What the newer work does not show is that fans and players judge streaks accurately. A real effect of a few percentage points is compatible with people perceiving a much larger one, and the popular claim that "the hot hand is real" can outrun the data just as the old fallacy claim did. The strongest competing explanation for residual streakiness in games is unmeasured shot difficulty; in controlled shooting it is that a small sample of players can produce a large average by chance.

## Sources

- Gilovich, T., Vallone, R., & Tversky, A. (1985). The hot hand in basketball: On the misperception of random sequences. *Cognitive Psychology*, 17(3), 295-314. [doi:10.1016/0010-0285(85)90010-6](https://doi.org/10.1016/0010-0285(85)90010-6)
- Miller, J. B., & Sanjurjo, A. (2018). Surprised by the hot hand fallacy? A truth in the law of small numbers. *Econometrica*, 86(6), 2019-2047. [doi:10.3982/ECTA14943](https://doi.org/10.3982/ECTA14943). Author version: [arXiv:1902.01265](https://arxiv.org/pdf/1902.01265)
- Bocskocsky, A., Ezekowitz, J., & Stein, C. (2014). The hot hand: A new approach to an old "fallacy". *MIT Sloan Sports Analytics Conference*. [sloansportsconference.com](https://www.sloansportsconference.com/research-papers/the-hot-hand-a-new-approach-to-an-old-fallacy)
