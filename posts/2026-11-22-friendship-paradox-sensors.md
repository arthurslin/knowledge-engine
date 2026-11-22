---
title: "Why your friends have more friends than you do, and how epidemiologists use it"
date: 2026-11-22
topics: [networks, sociology, public health]
summary: "In 1991 the sociologist Scott Feld showed that, on average, people's friends have more friends than they do, as a matter of arithmetic rather than social failure. Researchers have since tried to put the quirk to work, spotting flu outbreaks early and spreading health products faster, with mixed results."
status: published
quiz:
  - q: "According to Feld, why do most people's friends tend to have more friends than they do?"
    options:
      - "Because people with few friends underreport their friendships in surveys"
      - "Because popular people are counted in many people's friend lists, so they are overrepresented when you average over friends"
      - "Because people deliberately befriend those who are more popular than themselves"
      - "Because friendship networks always have a few people with no friends at all"
    answer: 1
    explain: "It is a sampling effect: someone with ten friends appears in ten friend lists, someone with one friend in only one. Feld's result needs no assumption about anyone seeking out popular friends, which is why the third option, though plausible-sounding, is not the explanation he gives."
  - q: "In the Harvard flu study, how did the researchers build their 'sensor' group?"
    options:
      - "They chose the students with the most social media followers"
      - "They recruited students who had already had flu"
      - "They chose students who lived in the largest dormitories"
      - "They asked a random group of students to name friends, and followed the people who were named"
    answer: 3
    explain: "The friend group was 425 students named by a random group of 319. No one needed to know the whole network, which is what makes the method cheap."
  - q: "In the Honduras trial, which targeting method produced the highest uptake of multivitamins?"
    options:
      - "Giving the product to the villagers with the most incoming friendship nominations"
      - "Giving it to randomly chosen villagers"
      - "Giving it to a randomly chosen friend of each randomly chosen villager"
      - "All three methods produced the same uptake"
    answer: 2
    explain: "Nomination targeting reached 74.3 percent redemption against 66.2 percent for random targeting. Targeting the most-nominated villagers did worse than random, at 61.0 percent, which is the result many readers find surprising."
  - q: "Which is the fairest summary of the evidence that friend sampling helps in practice?"
    options:
      - "Untested: all the evidence is mathematical simulation"
      - "Discredited, because the Honduras trial found no effect for either product"
      - "Supported by a few studies, including one randomised trial, with gains that held for one product but not another and a flu result from a single campus season"
      - "Settled: friend targeting reliably beats every alternative"
    answer: 2
    explain: "The sceptical options are factually wrong. The Lancet study was a cluster randomised trial, and it found a clear effect for multivitamins though none for chlorine. The 'settled' option overstates a small number of studies with mixed results."
reflect:
  - "Feld suggested the paradox might leave people feeling socially inadequate. What would you need to measure to test whether it actually does?"
  - "The friend group in the flu study was drawn from one campus in one season. What features of a population would you expect to make friend sampling work better or worse as an early warning system?"
---

## The idea

Ask a group of people how many friends they have, then ask how many friends their friends have. On average, the second number will be higher. The sociologist Scott Feld laid this out in the American Journal of Sociology in 1991 in a paper with the self-explanatory title "Why Your Friends Have More Friends Than You Do." The pattern is now called the friendship paradox.

It is not a claim that most people are unpopular. It follows from how the averaging works. A person with ten friends turns up on ten friend lists; a person with one friend turns up on one. When you average over everyone's friends, the well-connected are counted many times and the sparsely connected rarely. Feld showed that the average number of friends among friends equals the ordinary average plus the variance divided by the average, so the gap grows whenever popularity is unevenly spread.

His worked example used friendship data from 12 American high schools, taken from James Coleman's 1961 study The Adolescent Society. Among the girls at the school Coleman called Marketville, the mean number of mutual friends was 2.7, while the mean among their friends was 3.4. Of the 146 girls with any mutual friend, 80 had fewer friends than the average of their own friends, 41 had more, and 25 were level. Feld noted that this is not a mathematical necessity for every individual, only a likely outcome for most. He speculated that it could lead people to conclude they are somehow inadequate, but he did not test that.

## Why it might change a decision

The useful turn is that a random friend of a random person is a cheap way to reach well-connected people without mapping the whole network. In 2003 the physicists Reuven Cohen, Shlomo Havlin and Daniel ben-Avraham proposed "acquaintance immunisation" in Physical Review Letters: pick people at random and vaccinate one acquaintance each of them names. In model networks where a few nodes have very many links, they found that random vaccination needs nearly everyone covered to stop spread, while the acquaintance method brought the required share down to around a quarter.

Nicholas Christakis and James Fowler tested the detection side in PLoS ONE in 2010. During the 2009 flu season they followed 319 randomly chosen Harvard undergraduates and 425 students those people named as friends. Using diagnoses recorded by the university health service, the friend group's epidemic curve ran about 13.9 days ahead of the random group's (95% confidence interval 9.9 to 16.6). With self-reported symptoms the lead was 3.2 days.

The testable behaviour, then: if you have a fixed budget to monitor or seed a population, sample the named friends of random people rather than random people themselves, and compare how early you detect, or how widely you spread, against a random sample.

## How solid is this?

The arithmetic is solid; it is a property of averages, and it shows up in many networks. Whether it helps in practice rests on a small number of studies.

The flu study was observational, on one campus, in one unusual pandemic season, with friends limited to three nominations each. The authors note that being named is only a marker of network position, not a measure of actual contact.

The strongest test is a cluster randomised trial by David Kim and colleagues, including Christakis and Fowler, published in The Lancet in 2015. Across 32 villages in rural Honduras with 5,773 participants, researchers gave free-product coupons to 5 percent of each village, chosen at random, as the most-nominated villagers, or as one random friend named by each of a random 5 percent. For multivitamins, redemption was 74.3 percent under friend targeting, 66.2 percent under random targeting and 61.0 percent when targeting the most-nominated, a relative gain of about 12 percent for friend over random. For chlorine to purify water, the three methods were indistinguishable at about 55 percent. The authors measured coupon redemption, not use in the home, and had no long-term follow-up.

So the popular version, that friend sampling is a reliable shortcut to influence, outruns the data. One trial found a real effect for one product and none for another, and the authors themselves suggest more complex behaviours may need different targeting. A competing explanation for any single success is that friend-nominated people differ in ways other than popularity, such as trust or engagement, that would favour uptake regardless of network position. Also note that targeting the most connected did worse than random in Honduras, so "find the hubs" is not the same strategy as "ask for a friend."

## Sources

- Feld, S. L. (1991). Why Your Friends Have More Friends Than You Do. American Journal of Sociology, 96(6), 1464-1477. [JSTOR](https://www.jstor.org/stable/2781907); [PDF copy](https://www.cs.umd.edu/~gasarch/Feld-FriendsFriends-1991.pdf)
- Cohen, R., Havlin, S., and ben-Avraham, D. (2003). Efficient immunization strategies for computer networks and populations. Physical Review Letters, 91(24), 247901. [arXiv](https://arxiv.org/abs/cond-mat/0207387)
- Christakis, N. A., and Fowler, J. H. (2010). Social Network Sensors for Early Detection of Contagious Outbreaks. PLoS ONE, 5(9), e12948. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2939797)
- Kim, D. A., Hwong, A. R., Stafford, D., Hughes, D. A., O'Malley, A. J., Fowler, J. H., and Christakis, N. A. (2015). Social network targeting to maximise population behaviour change: a cluster randomised controlled trial. The Lancet, 386(9989), 145-153. [eScholarship](https://escholarship.org/uc/item/51n5n0fr)
