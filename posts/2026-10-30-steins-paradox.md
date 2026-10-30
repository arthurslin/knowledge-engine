---
title: "Why guessing a batter's average gets better when you look at other players"
date: 2026-10-30
topics: [statistics, decision making]
summary: "In 1956 Charles Stein proved that when you estimate three or more averages at once, using each one's own data alone is never the best you can do on total error. Pulling every estimate toward the group mean does better, a result statisticians still call Stein's paradox."
status: published
quiz:
  - q: "What exactly did Stein prove about estimating three or more means at once?"
    options:
      - "That each individual estimate always becomes more accurate when shrunk toward the group mean"
      - "That an estimator exists with lower expected total squared error than using each sample average on its own, whatever the true means are"
      - "That sample averages are biased and should never be used"
      - "That the result only holds when the true means are close together"
    answer: 1
    explain: "The guarantee is about total squared error across all the estimates, and it holds whatever the true values are. It is not a promise for each individual estimate: in Efron and Morris's baseball example three of eighteen players were estimated slightly worse."
  - q: "In the 1975 baseball example, what was the total squared prediction error of Stein's rule compared with the players' own early averages?"
    options:
      - "About the same"
      - "About 10 percent lower"
      - "Roughly 5.0 versus 17.6, under a third as large"
      - "Higher, which is why the result is called a paradox"
    answer: 2
    explain: "Efron and Morris report 17.56 for the individual averages and 5.01 for Stein's rule. The paradox is not that shrinkage does worse; it is that information about other players improves the estimate for each player taken as a group."
  - q: "Below what number of estimated quantities does the improvement disappear?"
    options:
      - "Two or fewer"
      - "Ten or fewer"
      - "Thirty or fewer, because of sample size"
      - "There is no threshold"
    answer: 0
    explain: "Stein showed the ordinary estimator is admissible in one and two dimensions and inadmissible from three upward. The threshold is about the number of quantities, not the size of each sample."
  - q: "A reader objects: 'This is one 1975 study of 18 baseball players, so the effect may not replicate.' How well does that objection fit the evidence?"
    options:
      - "It fits well: the result rests on a single small sample"
      - "It fits poorly: the core result is a mathematical proof, and the baseball data only illustrate it; what the data can test is how large the gain is in practice"
      - "It fits well, because the result was later retracted"
      - "It fits poorly, because baseball data are always reliable"
    answer: 1
    explain: "Scepticism about small samples is sensible for empirical claims, but Stein's theorem is proved under stated assumptions and has never been overturned. The fair worry is about the assumptions, such as roughly normal errors and equal variances, and about how big the gain is for real data."
reflect:
  - "Stein's rule improves the total error but can make one unusual case worse, as it did for the player with the highest early average. In what kind of decision would you care more about the worst individual estimate than about the total?"
  - "Efron and Morris describe the rule as borrowing information from problems that may be related. Would you be comfortable shrinking estimates of wheat yields, batting averages and hospital death rates toward one shared mean? Where would you draw the line, and why?"
---

## The idea

Suppose you want to estimate several quantities at once: the true batting skill of eighteen baseball players, the infection rate in thirty-six towns, the quality of a dozen hospitals. The obvious method is to use each one's own data: a player who hit .400 in his first 45 at-bats gets an estimate of .400.

In a paper presented at the Third Berkeley Symposium in 1954 and 1955 and published in 1956, the statistician Charles Stein proved that this obvious method is inadmissible whenever you estimate three or more means together. That means another estimator exists that has lower expected total squared error, no matter what the true values are. In one or two dimensions the ordinary estimator cannot be beaten this way; from three upward it always can.

In 1961 Stein and Willard James gave an explicit version, now called the James-Stein estimator. It takes every individual estimate and pulls it toward the grand mean of all of them, by an amount that depends on how spread out the estimates are compared with the noise in each one. The more the individual values look like noise around a common centre, the harder it shrinks.

The result disturbed statisticians because the quantities do not need to be related. Erich Lehmann, who had worked on the same question, later said he was "stunned with disbelief" when Stein told him, according to a 2012 account by Lawrence Brown and Linda Zhao.

**A concrete example.** Bradley Efron and Carl Morris, writing in the Journal of the American Statistical Association in 1975, took eighteen major league players' batting averages after their first 45 at-bats of the 1970 season and used them to predict each player's average over the rest of that season. Stein's rule put about 21 percent of the weight on each player's own record and about 79 percent on the group mean (on a transformed scale). Its total squared prediction error was 5.01, against 17.56 for the raw early averages. It did better for 15 of the 18 players.

## Why it might change a decision

Any time you rank or compare many noisy measurements, the extreme ones are partly extreme because of luck. Shrinkage turns that into a specific procedure: before acting on the top and bottom of a list (the best-scoring school, the worst-rated surgeon, the fastest-growing product), estimate how much of the spread is noise and pull each value toward the average by that amount.

A testable consequence follows. If you use first-month figures to predict the rest of the year for a set of salespeople, shops or players, the shrunken predictions should have lower total error than the raw ones, and the gap should be largest when early samples are small. Efron and Morris also showed the same logic working on toxoplasmosis rates across 36 cities in El Salvador, where a version allowing unequal sample sizes cut error by roughly two thirds.

## How solid is this?

The core claim is a mathematical theorem, not an empirical finding, so the usual worries about replication do not apply to it. Stein's 1956 proof has stood for seventy years and is the basis of a large literature on shrinkage and empirical Bayes methods, the same family of ideas behind modern techniques for stabilising many noisy estimates.

What the theorem promises is narrower than the popular slogan "averaging with others always helps." First, it guarantees lower **total** squared error, not better estimates for every individual. In the baseball data Roberto Clemente, whose early average of .400 was the highest, was pulled down to .290 while he went on to hit .346, so the shrunken estimate was slightly worse than his raw one. Efron and Morris note that the rule permits "considerably increased risk to individual components" and proposed a modified version that limits how far any single estimate can move.

Second, the proof assumes roughly normal errors with known, equal variance. Real data break these assumptions, which is why Efron and Morris transformed the batting averages first. Third, while the guarantee holds even for unrelated quantities, the size of the gain depends on how close the true values really are to each other. For eighteen players with similar skill it was large; for quantities with nothing in common it would be close to zero.

The strongest competing view is not that the theorem is wrong but that total squared error is the wrong target in many settings. If the cost of misjudging one exceptional case is high, a method that sacrifices that case for the group average may be the worse choice.

## Sources

- Charles Stein (1956). "Inadmissibility of the usual estimator for the mean of a multivariate normal distribution." Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1, 197–206. University of California Press. [PDF via DTIC](https://apps.dtic.mil/sti/pdfs/AD1028390.pdf)
- Bradley Efron and Carl Morris (1975). "Data analysis using Stein's estimator and its generalizations." Journal of the American Statistical Association 70(350), 311–319. [PDF](https://www.medicine.mcgill.ca/epidemiology/hanley/bios602/MultilevelData/EfronMorrisJASA1975.pdf)
- Lawrence D. Brown and Linda H. Zhao (2012). "A geometrical explanation of Stein shrinkage." Statistical Science 27(1), 24–30. [arXiv:1203.4737](https://pdf.arxiv.org/pdf/1203.4737)
