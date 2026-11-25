---
title: "Can physics tell a real Jackson Pollock from a fake? The fractal debate"
date: 2026-11-25
topics: [art, physics, research methods]
summary: "In 1999 three physicists reported that Jackson Pollock's drip paintings are fractal, and the measurement was later proposed as a way to spot fakes. Critics showed that some known Pollocks fail the test and some imitations pass it, and the two camps still disagree about what the numbers can show."
status: published
quiz:
  - q: "What did the 1999 Nature letter by Taylor, Micolich and Jonas report about Pollock's drip paintings?"
    options:
      - "That their paint patterns are fractal and that their fractal dimension rose over his career"
      - "That every painting attributed to Pollock has exactly the same fractal dimension"
      - "That a cache of 32 paintings found in 2003 was authentic"
      - "That fractal patterns appear only in paintings made with a brush"
    answer: 0
    explain: "The letter's abstract describes the patterns as fractal and says the dimensions increased during Pollock's career. It was published in 1999, so it could not have judged paintings that surfaced in 2003."
  - q: "What did Jones-Smith, Mathur and Krauss find when they applied the published fractal criteria to three undisputed Pollocks and to drip paintings made by other people?"
    options:
      - "All three Pollocks passed and both imitations failed"
      - "At most one of the three Pollocks passed, and only with a relaxed fit, while the commissioned imitations passed"
      - "None of the paintings could be analysed because the images were too small"
      - "The Pollocks and imitations had identical dimensions to three decimal places"
    answer: 1
    explain: "In their preprint, Free Form passed only when the fit was forced, the other two Pollocks failed, and the two commissioned drip paintings met the criteria comfortably. That is the core of the critique: the test missed real works and accepted imitations."
  - q: "According to Scientific American's account of the 32 disputed paintings, what other evidence counted against them besides the fractal analysis?"
    options:
      - "A signed confession by the painter"
      - "Fingerprints on the canvases that matched another artist"
      - "A Harvard analysis that found pigments not in use until years after Pollock's death"
      - "Radiocarbon dates showing the canvases were from the 1700s"
    answer: 2
    explain: "Scientific American reported that a Harvard team found two pigments that were not used until long after Pollock died in 1956. Materials evidence of that kind is independent of any image statistic."
  - q: "A sceptical reader says: 'This shows fractal measures of paintings are meaningless; the critics proved Pollock's works are not fractal at all.' Which reply best fits the evidence described?"
    options:
      - "Correct: the critics showed the paintings contain no repeating structure at any scale"
      - "Too strong: the critics argued the fractal range is too narrow and the criteria do not separate Pollocks from imitations, while later classifier studies report that fractal features still carry some useful signal when combined with others"
      - "Correct: Nature retracted the 1999 letter in 2006"
      - "Wrong: the critics agreed fractal analysis can authenticate paintings on its own"
    answer: 1
    explain: "The sceptical option sounds rigorous but overstates the critique. Jones-Smith and Mathur said the fractal characteristics hold over too small a range to be useful, not that no structure exists, and nothing in the sources describes a retraction. Irfan and Stork found that fractal features improved a classifier's accuracy, though on a small set of paintings."
reflect:
  - "Fractal analysis was asked to settle the question of the 32 disputed paintings, while pigment analysis gave a separate answer. When an image statistic and a materials test disagree, how would you decide which to trust, and what would each need to show?"
  - "Taylor kept part of his criteria unpublished. What does a test lose, scientifically, when outsiders cannot apply it themselves, and are there cases in authentication where keeping a method private could be defended?"
---

## The idea

A fractal is a pattern that looks similar whether you view it from far away or close up. A fern frond is made of smaller fronds, which are made of smaller ones still. Physicists measure how strongly a pattern fills space across scales with a number called the fractal dimension. For a set of lines drawn on a flat surface, it falls between 1 (a single thin line) and 2 (a completely filled area).

In June 1999, Richard Taylor, Adam Micolich and David Jonas, physicists at the University of New South Wales, published a short letter in Nature arguing that the poured paint in Jackson Pollock's drip paintings forms fractal patterns. They also reported that the fractal dimension of his paintings rose over the course of his career. The usual way to measure this is box-counting: lay a grid over a photograph of the painting, count how many squares contain paint, then repeat with smaller and smaller squares. If the count grows with square size in a steady power-law pattern, the slope gives the dimension.

The finding became more than a curiosity because it suggested a test. If genuine Pollocks share a measurable signature, perhaps a painting of uncertain origin could be checked against it. Taylor later set out formal criteria, and the Pollock-Krasner Foundation, according to Scientific American, commissioned him to examine six of 32 drip-style paintings that had surfaced in 2003 and were claimed as unknown Pollocks. He reported that none of the six showed the expected fractal pattern.

Then two physicists at Case Western Reserve University, Katherine Jones-Smith and Harsh Mathur, challenged the idea. In a 2006 comment in Nature, they argued that the paintings show fractal behaviour over too narrow a range of scales to count as fractal in any useful sense, and that similar measurements arise from freehand drawing and from simple random motion. With the cosmologist Lawrence Krauss, they then applied Taylor's published criteria to seven drip paintings. Of three undisputed Pollocks, two failed outright and one, Free Form (1946), passed only when the fit was forced. Two drip paintings they commissioned from other people passed comfortably. So did a crude pattern of overlapping stars drawn on a computer, according to Plus magazine. They concluded that the criteria provide no information about authenticity.

## Why it might change a decision

The debate is a clean example of a check that any proposed detector can be put through: run it on items whose answer is already known, in both directions. A test that marks genuine works as fake, or imitations as genuine, at a high rate tells you little about a disputed one, however precise its numbers look. In this case the specific, testable behaviour is simple: before an authentication method based on an image statistic is used on a disputed painting, it can be applied to undisputed works by the artist and to deliberate imitations, with the false-pass and false-fail rates reported alongside the verdict.

## How solid is this?

This is not a single-study finding, but every study involved is small. Taylor's original analyses covered a modest number of paintings; Plus reported that Jones-Smith counted 17 Pollocks in his work and considered that too few. Scientific American reported that a 2006 paper by Taylor's group found the pattern in 14 known Pollocks and not in 37 paintings by students or 14 of unknown origin. The critics' own test used only three undisputed Pollocks. No large, independent, blinded comparison has settled the matter in the sources reviewed here.

The core disagreement is about scale. The painted patterns can be measured over roughly three orders of magnitude, from the full canvas down to the thinnest drip. Jones-Smith and Mathur argued that this is too short a range to call a pattern fractal. Taylor replied, according to Plus, that such a rule would rule out about half of all published fractal studies. Taylor also kept one of his criteria confidential, which made it hard for outsiders to reproduce his exact test.

Others took a middle path. Mohammad Irfan and David Stork combined the fractal measure with four other image features in a classifier trained on 21 paintings. The fractal feature alone gave 76 percent accuracy in a leave-one-out test, and all five features together gave 81 percent. They concluded that rejecting box-counting outright was premature, while describing their own work as preliminary and their imitation set as weak.

Taylor's group has continued. A 2024 University of Oregon release describes a neural network, trained on tiles cut from nearly 600 digitised artworks, that it says separates Pollocks from imitations 98.9 percent of the time. That method is not a fractal test as such, and the release says it should be used alongside materials analysis and visual inspection.

The strongest competing explanation for the original result, as Jones-Smith and Mathur framed it, is that box-counting slopes over a short range are easy to produce. They reported that freehand drawing and random motion yield similar measurements, which suggests a fractal-like number may reflect how overlapping lines of poured paint behave in general more than one painter's hand. Meanwhile, the disputed paintings were weighed on other evidence: Scientific American reported that a Harvard team found pigments that were not in use until long after Pollock died in 1956.

## Sources

- Taylor, R. P., Micolich, A. P. and Jonas, D. (1999). "Fractal analysis of Pollock's drip paintings." Nature 399, 422. https://www.nature.com/articles/20833
- Jones-Smith, K. and Mathur, H. (2006). "Revisiting Pollock's drip paintings." Nature 444, E9–E10. https://www.nature.com/articles/nature05398
- Jones-Smith, K., Mathur, H. and Krauss, L. M. "Drip paintings and fractal analysis." arXiv preprint 0710.4917; Science News reported in 2009 that it was to appear in Physical Review E. https://arxiv.org/abs/0710.4917
- Irfan, M. and Stork, D. G. (2009). "Multiple visual features for the computer authentication of Jackson Pollock's drip paintings: beyond box-counting and fractals." Proceedings of SPIE 7251. https://tildesites.bowdoin.edu/~mirfan/papers/Irfan_Stork_Pollock_2009.pdf
- Sanders, L. (2009). "Never mind the Pollock 'fractals'." Science News, 19 March 2009. https://www.sciencenews.org/article/never-mind-pollock-fractals
- "Pollock or not? Can fractals spot a fake masterpiece?" Scientific American. https://www.scientificamerican.com/article/can-fractals-spot-genuine/
- West, M. (2007). "Rollicking Pollock debate." Plus magazine, University of Cambridge, 30 November 2007. https://plus.maths.org/content/rollicking-pollock-debate
- University of Oregon news release, "Artificial intelligence can spy art forgeries, UO study finds" (2024), on Taylor and colleagues' PLOS ONE study. https://news.uoregon.edu/artificial-intelligence-can-spy-art-forgeries-uo-study-finds
