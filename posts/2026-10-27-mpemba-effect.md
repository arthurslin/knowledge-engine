---
title: "Does hot water freeze faster than cold?"
date: 2026-10-27
topics: [physics, research methods]
summary: "The Mpemba effect, the claim that hot water can freeze before cold, has been argued over since 1969. Careful water experiments have failed to find it, while physicists have shown that a related effect is real in simpler, controlled systems."
status: published
quiz:
  - q: "What did Burridge and Linden find in their freezer experiment with three 400 g water samples?"
    options:
      - "The hottest sample reached 0 °C first, confirming the Mpemba effect"
      - "All three samples reached 0 °C at almost exactly the same time"
      - "The hottest sample took the longest to reach 0 °C"
      - "The results varied so much between runs that no order could be seen"
    answer: 2
    explain: "Samples starting at 21.8, 57.3 and 84.7 °C took about 6,400, 9,500 and 10,800 seconds to reach 0 °C: the hotter, the slower. The equal-time and chaotic-results options describe nothing they reported."
  - q: "Why did Burridge and Linden measure the time to reach 0 °C or 4 °C rather than the time to freeze solid?"
    options:
      - "Freezing involves supercooling and nucleation, which are too variable to give a repeatable comparison"
      - "Their freezer could not reach temperatures below 0 °C"
      - "Mpemba and Osborne had also measured only the time to 4 °C"
      - "Ice damages thermocouples"
    answer: 0
    explain: "They argued that when ice first forms depends on chance events such as nucleation, so freezing time is too noisy to show a repeatable effect. Their freezer was set to -18 °C, so the second option is wrong."
  - q: "What did Kumar and Bechhoefer's 2020 Nature experiment actually cool?"
    options:
      - "Beakers of tap water in a commercial freezer"
      - "A single microscopic particle in water, held in an energy landscape set by an optical feedback trap"
      - "Ice cream mix, repeating Mpemba's original observation"
      - "A computer simulation of an Ising magnet, with no physical apparatus"
    answer: 1
    explain: "Their system was one colloidal particle whose 'temperature' was the spread of its starting positions in an imposed potential. The Ising model appears in Lu and Raz's theoretical paper, not in this experiment."
  - q: "A reader says: 'Since Burridge and Linden found no Mpemba effect in water, the Kumar and Bechhoefer result must also be an artefact of badly placed sensors.' What is the best response?"
    options:
      - "Agreed: any positive Mpemba result should be presumed to be a thermocouple error"
      - "Agreed: the colloidal result has never been reproduced, so it should be set aside"
      - "The two results do not conflict directly: the colloidal experiment measured a particle's position distribution, not water temperature with thermocouples, and reported reproducible results matching theory"
      - "The colloidal result proves Burridge and Linden made an error with their water"
    answer: 2
    explain: "The sensor-placement worry applies to measuring temperature inside cooling water. The colloidal experiment had no such sensors, and its authors report reproducible results that agree with a theoretical prediction. Nor does it overturn the water result, since it is a different system."
reflect:
  - "If someone shows a hot-water anomaly in one specific container and freezer, how many conditions would you need to vary before calling it 'the Mpemba effect' rather than a feature of that setup?"
  - "The word 'temperature' means something different for a single colloidal particle than for a beaker of water. Is it fair to give both findings the same name, and what might be gained or lost by doing so?"
---

## The idea

In 1969 the journal *Physics Education* published a short paper titled "Cool?" by E. B. Mpemba and D. G. Osborne. As the story is usually retold, Mpemba, then a secondary school student in Tanzania, had noticed while making ice cream that a mix put into the freezer hot appeared to freeze before one put in cool. Osborne, a university physicist, ran his own tests with small beakers of water and reported the same pattern. The claim that hot water can freeze, or cool to a set temperature, faster than cold water under otherwise identical conditions is now called the Mpemba effect.

The claim sounds as if it breaks a basic rule, but it does not. Water starting hot has further to go, yet it also loses heat faster while it is hot, and could in principle change in other ways along the way: losing mass to evaporation, losing dissolved gas, or setting up different currents inside the container. So the question is not whether the effect is possible but whether it actually happens, reliably, in water.

A concrete example of what a test looks like: put equal masses of water at different starting temperatures into identical beakers in the same freezer, and record when each first reaches 0 °C.

## Why it might change a decision

The specific, testable prediction is simple: in a controlled comparison with identical containers and surroundings, a sample starting hotter should reach a target temperature sooner than one starting cooler. If careful repetitions show the opposite, with time rising steadily with starting temperature, the everyday version of the claim fails. A second prediction comes from theory: in small systems whose dynamics are well understood, the effect should appear only for particular, calculable settings, not for any pair of temperatures.

## How solid is this?

The evidence splits sharply between water, where careful work has not found the effect, and simpler model systems, where a related effect has been shown.

For water, Henry Burridge and Paul Linden reviewed the published data and ran their own experiments, reported in *Scientific Reports* in 2016. In a freezer set to -18 °C they cooled three 400 g samples starting at 21.8, 57.3 and 84.7 °C. The times to first reach 0 °C were about 6,400, 9,500 and 10,800 seconds, in order: the hottest was slowest. In a second set, water in a tank was cooled from above to 4 °C from starting temperatures between 18 and 75 °C, avoiding ice altogether, and again showed no effect.

They argued that most published datasets show cooling time rising with starting temperature, and that the few apparent exceptions sit only marginally on the "Mpemba" side, within measurement error. Many earlier studies did not report where their thermometers were placed, and Burridge and Linden showed that shifting a sensor by about 1 cm vertically could make their own data appear to show the effect. They described the original Mpemba and Osborne data, with a 90 °C sample freezing much faster than a 20 °C one, as an outlier that could not be explained and should be treated as doubtful until reproduced. They also argued that the moment of freezing, which depends on chance events such as supercooling and nucleation, is too variable to show a repeatable effect. Their conclusion: no evidence to support meaningful observations of the effect.

That is one careful study plus a review, not the last word. Water experiments vary in container, freezer and sensor, and a critic could argue that some untested setup produces the effect. But the burden has shifted to anyone claiming it in water.

The theoretical side developed in parallel. Zhiyue Lu and Oren Raz, in *PNAS* in 2017, described a general mechanism for systems whose next state depends only on the present one, called Markov processes. They gave a sufficient condition under which a hotter system relaxes to the cold surroundings faster than a cooler one, showed it in model systems including an Ising magnet, and predicted an inverse effect in heating.

Avinash Kumar and John Bechhoefer tested this kind of prediction in *Nature* in 2020. Their system was a single microscopic colloidal particle in water, held in an asymmetric energy landscape imposed by an optical feedback trap. Here "hot" and "cold" describe how widely the particle's starting positions are spread, not the temperature of a beaker. They reported reproducible results in quantitative agreement with theory, and found settings where cooling was exponentially faster, matching a predicted "strong" version of the effect.

The fair summary is that two claims share a name. The popular claim, that a hot glass of water will freeze before a cold one, outruns the data. The narrower claim, that some systems can relax faster from a hotter start, is supported by theory and by at least one controlled experiment. Whether that mechanism ever operates in real freezing water remains unestablished.

## Sources

- Mpemba, E. B., & Osborne, D. G. (1969). Cool? *Physics Education*, 4(3), 172-175. [doi:10.1088/0031-9120/4/3/312](https://doi.org/10.1088/0031-9120/4/3/312)
- Burridge, H. C., & Linden, P. F. (2016). Questioning the Mpemba effect: hot water does not cool more quickly than cold. *Scientific Reports*, 6, 37665. [doi:10.1038/srep37665](https://doi.org/10.1038/srep37665)
- Lu, Z., & Raz, O. (2017). Nonequilibrium thermodynamics of the Markovian Mpemba effect and its inverse. *Proceedings of the National Academy of Sciences*, 114(20), 5083-5088. [doi:10.1073/pnas.1701264114](https://doi.org/10.1073/pnas.1701264114)
- Kumar, A., & Bechhoefer, J. (2020). Exponentially faster cooling in a colloidal system. *Nature*, 584(7819), 64-68. [doi:10.1038/s41586-020-2560-x](https://doi.org/10.1038/s41586-020-2560-x)
