---
title: "Can a new road make every driver slower?"
date: 2026-10-27
topics: [engineering, networks]
summary: "In 1968 a German mathematician showed that adding a road to a congested network can lengthen every driver's journey. The mathematics is certain; how often it happens on real streets is much less clear than the popular stories suggest."
status: published
quiz:
  - q: "In Braess's six-driver example, what happens to each driver's travel time when the new link is added?"
    options:
      - "It falls from 92 to 83, because there is now a shortcut"
      - "It rises from 83 to 92, even though every driver chooses the fastest route available to them"
      - "It stays at 83 for most drivers but rises for the two who use the new link"
      - "It rises only because the new link is slower than the old roads"
    answer: 1
    explain: "At the new equilibrium all three routes cost 92, so every driver is worse off than the 83 they had before. The new link itself is cheap to use; the trouble is that it attracts traffic onto the congestion-sensitive roads at either end."
  - q: "What distinction is at the heart of the paradox?"
    options:
      - "Between fast roads and slow roads"
      - "Between cars and trucks sharing a road"
      - "Between the flow that minimises total travel time and the flow that results when each driver picks their own quickest route"
      - "Between roads with tolls and roads without"
    answer: 2
    explain: "Braess separated the system optimal flow from the user optimal one. Without the new link they happen to coincide; with it, selfish routing settles on a worse pattern. Multiclass traffic is discussed in the paper, but it is not the source of the paradox."
  - q: "What did Cohen and Horowitz show with springs and strings?"
    options:
      - "That cutting a connecting string can make a hanging weight rise, a mechanical analogue of Braess's paradox"
      - "That springs behave like drivers and always choose the shortest path"
      - "That any purely linear network of springs or resistors can show the paradox"
      - "That Braess's arithmetic contained an error"
    answer: 0
    explain: "Cutting the link lets each spring carry half the load, so the weight ends up higher. The authors note that purely linear networks cannot show the effect; it needs nonlinear elements such as slack strings or Zener diodes."
  - q: "Which is the fairest description of the evidence that Braess's paradox occurs in real cities?"
    options:
      - "It has been confirmed by before-and-after traffic counts in dozens of cities"
      - "Youn and colleagues' study is unreliable because it looked at only one city"
      - "Youn and colleagues found candidate links in models of Boston, London and New York, but these are simulations with simplified assumptions, and the famous closure stories are poorly documented"
      - "The paradox is purely theoretical, since real drivers never choose routes selfishly"
    answer: 2
    explain: "The study covered three cities, so the 'one city' doubt sounds careful but is wrong. Its real limits are that it is a simulation with one origin, one destination, fixed demand and a uniform assumed speed limit, not observed traffic."
reflect:
  - "A city closes a busy street and journey times do not get worse. What observations would you need to tell a Braess effect apart from people simply making fewer car trips?"
  - "Electricity grids, data networks and supply chains all have users or flows that route themselves. Where might a Braess-like effect plausibly appear in one of them, and what would play the role of the selfish driver?"
---

## The idea

In 1968 the mathematician Dietrich Braess published a short paper in the German operations research journal *Unternehmensforschung* about how traffic spreads across a road network. He distinguished two ways of describing that spread. In one, traffic is arranged to minimise travel time for the system as a whole. In the other, each driver simply takes whichever route is quickest for them, given what everyone else is doing; this is now called the user equilibrium, a kind of Nash equilibrium. The two need not match, and Braess showed that the gap can produce something counterintuitive: adding a road can make every driver's journey longer.

His example is small enough to check by hand. Six vehicles travel from an origin to a destination along one of two routes. Each route has one link whose delay grows steeply with traffic (ten units per car) and one that is long but barely affected by congestion (50 units plus one per car). With three vehicles on each route, every journey costs 83. Now add a short connecting link between the two middle points, costing 10 plus one per car. Drivers can switch onto it and avoid the long links, and each individual switch looks sensible. The new equilibrium has two vehicles on each of three routes, and every journey now costs 92. Nobody can do better by changing route alone, yet everyone is worse off than before the road was built. In the words of the English translation, an extension of the network "may cause a redistribution of the traffic" that lengthens journeys.

The paper reached most English-speaking readers only through later summaries; a full translation by Braess, Anna Nagurney and Tina Wakolbinger appeared in *Transportation Science* in 2005.

In 1991 Joel Cohen and Paul Horowitz showed the same structure outside traffic. In a letter to *Nature* they hung a weight from two springs joined by a short string, with slack safety strings alongside. Cutting the connecting string makes the weight rise, because each spring then carries half the load. They built an electrical version too, and noted that networks of purely linear elements cannot show the effect.

## Why it might change a decision

The paradox makes a specific prediction: in a congested network where drivers choose their own routes, there can be particular links whose removal lowers average travel time. That is testable in models and, in principle, on the ground. It also implies that the value of a new road cannot be judged from the road alone; it depends on how traffic redistributes across the whole network at equilibrium, and the effect appears only under some traffic volumes.

## How solid is this?

As mathematics, the paradox is settled: Braess's example is a worked calculation, not an empirical claim. The open question is how often real networks are in the conditions that produce it.

The most cited attempt to look at real street layouts is a simulation. Hyejin Youn, Michael Gastner and Hawoong Jeong, in *Physical Review Letters* in 2008, built models of principal roads in Boston, London and New York from Google Maps, each with a single origin and destination and a fixed flow of vehicles. They estimated the price of anarchy, the ratio of equilibrium travel time to the best coordinated arrangement, at up to about 1.30 in Boston, meaning drivers lost around 30 percent of their travel time to lack of coordination, with figures up to 24 percent for London and 28 percent for New York. They found six links in Boston, seven in London and twelve in New York whose individual removal would cut delay. These results depend on assumptions the authors state: a uniform 35 mph speed limit, one standard delay formula, and particular origin and destination pairs, which they note could change which links matter. An erratum was later published, which I have not been able to read. No observed before-and-after traffic data are involved.

Real-world stories are often repeated: a closure of 42nd Street in New York that eased traffic, a new road in Stuttgart that was removed after making things worse. I could not find primary documentation for these, so they should be treated as anecdotes rather than evidence.

The strongest competing explanation for any closure that does not cause gridlock is not Braess at all. Braess's model fixes the number of trips. On real streets, some people respond to a closure by travelling at other times, by other modes, or not at all, which would also improve flow. The popular claim that removing roads speeds up cities outruns the data; the narrower claim, that some links in some congested networks can be harmful, is mathematically sound and supported by simulations.

## Sources

- Braess, D. (1968). Über ein Paradoxon aus der Verkehrsplanung. *Unternehmensforschung*, 12, 258-268. [doi:10.1007/BF01918335](https://doi.org/10.1007/BF01918335)
- Braess, D., Nagurney, A., & Wakolbinger, T. (2005). On a paradox of traffic planning. *Transportation Science*, 39(4), 446-450. [doi:10.1287/trsc.1050.0127](https://doi.org/10.1287/trsc.1050.0127)
- Cohen, J. E., & Horowitz, P. (1991). Paradoxical behaviour of mechanical and electrical networks. *Nature*, 352, 699-701. [doi:10.1038/352699a0](https://doi.org/10.1038/352699a0)
- Youn, H., Gastner, M. T., & Jeong, H. (2008). Price of anarchy in transportation networks: Efficiency and optimality control. *Physical Review Letters*, 101, 128701. [doi:10.1103/PhysRevLett.101.128701](https://doi.org/10.1103/PhysRevLett.101.128701)
