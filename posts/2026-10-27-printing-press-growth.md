---
title: "Did the printing press make cities grow?"
date: 2026-10-27
topics: [history, economics]
summary: "Economists long struggled to find any economic footprint of the printing press. A 2011 study found one at the level of cities, using distance from Mainz to separate cause from coincidence, but the same trick also predicts the spread of Protestantism."
status: published
quiz:
  - q: "Why did Dittmar use each city's distance from Mainz in his analysis?"
    options:
      - "Mainz was the largest market for books, so distance measured the cost of selling to it"
      - "Printing spread outward from Mainz, so distance predicts which cities adopted it early, for reasons separate from their growth prospects"
      - "Mainz was the political capital of the Holy Roman Empire, so distance measured political influence"
      - "Population records were most complete near Mainz, so distance measured data quality"
    answer: 1
    explain: "Mainz was where printing began, and the technology spread from there, so nearby cities were more likely to adopt it early. The hope is that distance from Mainz affects growth only through printing. Mainz was not chosen for its market size or political role."
  - q: "What did the study find when it looked at the century before printing arrived?"
    options:
      - "Cities that later adopted printing were already growing about 60 percent faster"
      - "Adopting cities had been shrinking, so printing reversed a decline"
      - "There were no reliable population figures before 1500"
      - "Cities that later adopted printing showed no growth advantage before it arrived"
    answer: 3
    explain: "The 1400 to 1500 placebo estimates were not significant, which is evidence against the idea that printers simply picked cities already on the rise. The 60 percent figure refers to 1500 to 1600, after adoption."
  - q: "What did Rubin (2014) find using the same distance-from-Mainz instrument?"
    options:
      - "Cities with a press by 1500 were at least 29 percentage points more likely to be Protestant by 1600"
      - "Printing had no detectable link to the Reformation"
      - "Protestant cities were less likely to adopt printing"
      - "Cities near Wittenberg grew faster than cities near Mainz"
    answer: 0
    explain: "Rubin found a large positive link between early printing and later Protestantism. That matters for the growth result, because it shows distance from Mainz predicts more than one historical change."
  - q: "Which is the fairest summary of the evidence that printing made cities grow?"
    options:
      - "The result is unreliable because adopting cities were already growing faster before the presses came"
      - "The result has been confirmed by national income data showing a clear jump in productivity after 1500"
      - "A single main study finds a large city growth effect with an imprecise instrumental estimate, and the instrument may partly capture religious change"
      - "Book production barely changed after printing, so any effect must be small"
    answer: 2
    explain: "The pre-trend worry sounds like proper caution, but the study tested for it and found no advantage before adoption. The real caveats are a wide confidence band on the instrumental estimate, the Reformation as a second channel, and the gap between city growth and income per head. Aggregate data, if anything, showed no clear effect."
reflect:
  - "The same instrument, distance from Mainz, has been used to explain both city growth and religious change. What would you need to know to decide whether it can do both jobs at once?"
  - "Dittmar found effects in city populations while earlier work found nothing in national aggregates. For a modern technology, such as broadband, where would you expect its effects to show first, and why might national figures miss them?"
---

## The idea

Printing with movable type began in Mainz in the middle of the fifteenth century and spread across Europe within decades. It is often named as one of the great turning points in history. Yet economists who went looking for its effect on productivity or income per head in national data found very little. Jeremiah Dittmar, in a 2011 paper in the *Quarterly Journal of Economics*, notes that earlier work, including by Gregory Clark and Joel Mokyr, judged the aggregate effects to be small.

Dittmar's move was to look at cities instead of countries. Using historical city population estimates compiled by Bairoch, Batou and Chèvre, he compared European cities that had a printing press by 1500 with similar cities that did not. Adopting cities grew about 60 percent faster between 1500 and 1600 than otherwise similar cities, and they had shown no growth advantage before printing arrived.

The obvious problem is that printers were not placed at random. They were businesspeople, and the paper itself finds they favoured larger cities. To get around this, Dittmar used each city's distance from Mainz as an instrumental variable. A concrete version: a town a short journey from Mainz was likely to get a press early simply because printers trained there and travelled outwards, while an otherwise identical town far away got one later or not at all. If distance from Mainz matters for growth only because it shaped access to printing, comparing near and far towns isolates the effect of the press.

## Why it might change a decision

The study makes a specific, checkable claim about where to look for the effects of a new information technology. If Dittmar is right, early gains concentrate in the places that adopt first, and they can be invisible in national averages for a long time. That predicts that city or regional data should show adopting places pulling ahead after adoption, not before, while national productivity series stay flat. It also offers a test that any rival explanation has to pass: the growth gap should open only after the technology arrives.

## How solid is this?

The city growth claim rests mainly on a single study, and the research for this post found no independent replication of its main estimate. It is observational, built on population estimates at 100 year intervals. The main balanced panel covers 202 cities, of which 83 adopted printing, with other regressions using between 291 and 622 cities.

The size of the effect depends on the method. Ordinary regression gives about 0.19 log points of extra growth from 1500 to 1600. The instrumental estimate is about three times larger, 0.58 log points, but with a standard error of 0.29, so the plausible range is wide. Dittmar argues the larger figure is expected, because a yes-or-no measure of adoption is a noisy proxy for how much print culture a city had. Placebo tests support the design: distance from Amsterdam, London, Paris, Venice or Wittenberg did not produce significant effects, and distance from Mainz did not predict growth before 1500.

The strongest competing explanation is religion. Jared Rubin, in the *Review of Economics and Statistics* in 2014, used the same instrument to study the Reformation. He found that cities with at least one press by 1500 were at least 29 percentage points more likely to be Protestant by 1600. That is a finding about printing in its own right, but it complicates the growth result: if distance from Mainz shaped religion, and religion shaped growth, the instrument does not run through printing alone. Dittmar controls for distance to Wittenberg, where Luther began, and reports that the results hold, but a control of this kind cannot rule out every route.

There is also strong evidence that printing changed the book trade itself. Eltjo Buringh and Jan Luiten van Zanden, in the *Journal of Economic History* in 2009, estimated manuscript and printed book production across Western Europe over thirteen centuries. They found the sector grew at an average of around one percent a year, with output rising after the middle of the fifteenth century, which they attribute mainly to falling book prices and rising literacy. That supports a large change in access to information, not a specific effect on city growth.

Where the popular story outruns the data is in the jump from bigger cities to richer societies. City population is not income per head, and Dittmar does not measure the latter directly. The national evidence of small aggregate effects has not been overturned; Dittmar's argument is that it missed local spillovers.

## Sources

- Dittmar, J. E. (2011). Information technology and economic change: The impact of the printing press. *Quarterly Journal of Economics*, 126(3), 1133-1172. [doi:10.1093/qje/qjr035](https://doi.org/10.1093/qje/qjr035)
- Rubin, J. (2014). Printing and Protestants: An empirical test of the role of printing in the Reformation. *Review of Economics and Statistics*, 96(2), 270-286. [doi:10.1162/REST_a_00368](https://doi.org/10.1162/REST_a_00368)
- Buringh, E., & van Zanden, J. L. (2009). Charting the "rise of the West": Manuscripts and printed books in Europe, a long-term perspective from the sixth through eighteenth centuries. *Journal of Economic History*, 69(2), 409-445. [doi:10.1017/S0022050709000837](https://doi.org/10.1017/S0022050709000837)
