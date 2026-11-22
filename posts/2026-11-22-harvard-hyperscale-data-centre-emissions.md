---
title: "Harvard-led study estimates 403 large US data centres used about 1.8 percent of the country's electricity"
date: 2026-11-22
topics: [AI news, climate]
summary: "A Nature Sustainability paper published on 16 November 2026 estimates that 403 US hyperscale data centres used 68-99 TWh of electricity in the year to April 2025, more than half of it from fossil fuels. The figures are modelled from capacity and assumed load rather than metered, and the emissions estimate changed substantially between the preprint and the published version."
status: published
quiz:
  - q: "How did the researchers estimate each facility's electricity use?"
    options:
      - "From meter readings supplied by the operators"
      - "From each facility's power capacity multiplied by the hours in a year and an assumed load factor"
      - "From utilities' bills, obtained through public records requests"
      - "From the number of AI chips in each building"
    answer: 1
    explain: "The preprint describes capacity times hours times a load coefficient, with a central value of 0.58 and scenarios from 0.48 to 0.70. That is why the result is a range, and why it is a model estimate rather than a measurement."
  - q: "Which four states account for more than half of the estimated consumption?"
    options:
      - "California, Texas, New York and Washington"
      - "Arizona, Nevada, Georgia and Illinois"
      - "Virginia, Oregon, Ohio and Iowa"
      - "Wyoming, West Virginia, Nebraska and Minnesota"
    answer: 2
    explain: "Virginia alone has 142 of the 403 facilities and roughly a quarter of the estimated use. Wyoming appears in the coverage only as an example of a carbon-intensive grid."
  - q: "What does the study say about AI specifically?"
    options:
      - "That AI training accounts for most of the electricity"
      - "That AI inference uses more than training"
      - "Nothing quantitative: the data cannot separate AI workloads from other computing"
      - "That AI accounts for exactly 1.8 percent of US electricity"
    answer: 2
    explain: "The press materials say the data cannot distinguish general computing from AI-specialised use. The 1.8 percent figure is for all 403 hyperscale facilities, whatever they run."
  - q: "A reader notices the preprint gave about 45 million tonnes of CO2 and the published releases give 25.7 million. What is the most defensible conclusion?"
    options:
      - "The electricity estimate is unreliable too, since it must have changed by the same proportion"
      - "The study is not peer reviewed, so neither number counts"
      - "The emissions figure moved between versions while the electricity figures stayed the same; the reason should be checked in the published methods before relying on either number"
      - "The lower number is a press office error"
    answer: 2
    explain: "The central 82 TWh and 68-99 TWh range are the same in both versions, so the change is in the emissions accounting, not the electricity model. The paper is peer reviewed and published in Nature Sustainability, so the second option is wrong; nothing supports calling the published figure an error."
reflect:
  - "The study uses average grid emissions rather than the emissions of the power plants that ramp up to meet new demand. Which approach do you think better answers the question 'what did these data centres add?', and why?"
  - "No federal body currently tracks data-centre electricity use, so researchers had to model it. What would a reporting rule need to include to make a study like this unnecessary?"
---

## What happened

On 16 November 2026, Nature Sustainability published a peer-reviewed paper led by Gianluca Guidi, a postdoctoral researcher in biostatistics at the Harvard T.H. Chan School of Public Health, with Francesca Dominici, director of the Harvard Data Science Initiative, as corresponding author. Co-authors include researchers at the University of Pisa, IMT Lucca, UCLA, the mapping company Esri and the data-centre data firm Baxtel. The paper's DOI is 10.1038/s41893-026-01985-7; a preprint version was posted on arXiv on 3 June 2026. The figures below come from the preprint and from the press releases for the published version issued by Harvard and by Nature's publisher.

The team started from 675 hyperscale data centres listed by Baxtel and kept 403 that they could confirm with satellite imagery and mapped building footprints. For the year from May 2024 to April 2025, they estimate these facilities used 68 to 99 TWh of electricity, with a central estimate of about 82 TWh, or about 1.8 percent of US consumption. Harvard's release compares the total to the use of a whole US state. Fossil fuels supplied about 54 percent of the electricity, mostly natural gas with a smaller share of coal. Virginia, Oregon, Ohio and Iowa together account for more than half of the total; Virginia alone has 142 of the facilities.

The published version's releases put carbon dioxide emissions at 25.7 million tonnes, with a range of roughly 21 to 31 million. Time compared that to Denmark's annual emissions.

## What is claimed vs. what is verified

**What the study is.** This is a model, not a measurement. Electricity use is estimated as each facility's power capacity multiplied by the hours in a year and an assumed load factor, with a central value of 0.58 and scenarios from 0.48 to 0.70. Emissions are assigned using EPA plant data for the grid regions supplying each site, an average rather than a marginal approach. The press materials say the data cannot separate AI workloads from other computing, so the paper does not show how much of this is due to AI.

**A number that changed.** The June preprint gave a central estimate of about 45 million tonnes of CO2 (37 to 54 million) for the same 82 TWh. The published version's releases give 25.7 million. The electricity estimates did not change. The press materials do not explain the difference, so readers should look to the published methods before leaning on either emissions number.

**Independent coverage.** Time, Grist and ConsumerAffairs reported the study; none re-ran the analysis. Grist added context from outside the paper: as a share of each state's 2024 electricity sales, the facilities came to about 18.6 percent in Oregon, 15.5 percent in Virginia and 13.1 percent in Iowa, a comparison Grist notes mixes two different time windows. Grist also pointed out that grid averages miss on-site gas generators, which the Environmental Integrity Project counts at about 2 GW operating and far more proposed.

## Why it matters

There is no federal tracking of data-centre electricity use, so most public figures come from industry or from national projections. This study gives facility-level estimates that can be checked against local grid data. The concentration in a few states matters for those states' grids and prices more than the national share suggests. The authors say the totals are likely low, both because not every facility could be confirmed and because many have been built since April 2025.

## Open questions and other views

**The researchers.** Dominici said peer-reviewed data on data centres' environmental effects was scarce when the work began. The team plans to study health effects of power-plant pollution near these grids, which this paper did not measure.

**On method.** The preprint describes its approach as attributional rather than consequential: it shares out each grid's existing mix rather than asking which plants ran more because of the new demand. Those two framings can give different answers, in either direction, depending on which plants respond. The authors also list estimated rather than measured loads and incomplete facility coverage as limitations.

**Utilities.** Industry figures can run higher than the study's. Grist cites Dominion Energy's securities filing estimating that data centres bought 28 percent of the electricity its Virginia subsidiary sold in 2025, against the 15.5 percent share Grist derived from the study for Virginia, though the two cover different facilities and periods. None of the coverage reviewed here carried a response from data-centre operators.

**Policymakers.** Grist reports that Senators Elizabeth Warren and Josh Hawley have asked the Energy Information Administration to require reporting. Whether mandatory disclosure would cover on-site generation, and whether it would split out AI workloads, is unsettled.

## Sources

- Guidi, G. et al., arXiv preprint 2606.05420, 3 June 2026: [Assessing the Carbon Emissions and Energy Consumption of U.S. Hyperscale Data Centers](https://arxiv.org/abs/2606.05420)
- Harvard T.H. Chan School of Public Health (Maya Brownstein), 16 November 2026: [Hyperscale data centers' energy consumption, carbon emissions newly estimated by researchers](https://hsph.harvard.edu/?p=111350108288); also via [EurekAlert](https://www.eurekalert.org/news-releases/1150191)
- Nature Research press release, 17 November 2026: [Environment: Assessing US data centre electricity usage](https://www.natureasia.com/en/info/press-releases/detail/9482)
- Time (Simmone Shah), 16 November 2026: [Over 400 American AI Data Centers Use As Much Electricity As Wisconsin, Michigan, or Indiana](https://time.com/article/2026/11/16/ai-data-centers-electricity-carbon-emissions-study/)
- Grist (Clayton Aldern), 20 November 2026: [Data centers' electricity use is soaring, especially in these states](https://grist.org/energy/data-centers-use-2-of-us-electricity-in-some-states-the-share-is-far-higher)
- ConsumerAffairs (Mark Huffman), 18 November 2026: [Large data centers used nearly 2% of U.S. electricity, Harvard-led study estimates](https://www.consumeraffairs.com/news/large-data-centers-used-nearly-2-of-us-electricity-harvard-led-study-estimates-111826.html)
