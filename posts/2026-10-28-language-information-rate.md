---
title: "Do fast-sounding languages say more per second?"
date: 2026-10-28
topics: [linguistics, cognitive science]
summary: "Some languages pack many syllables into each second, others fewer. Two studies from one research group found that faster languages carry less information per syllable, so the information rate ends up closer across languages than speed suggests. Whether it is truly constant is less settled."
status: published
quiz:
  - q: "What did Coupé and colleagues report in their 2019 study of 17 languages?"
    options:
      - "Languages with faster speech carried more information per second"
      - "Information rates converged on roughly 39 bits per second despite large differences in speed and density"
      - "Speech rate was nearly identical across all 17 languages"
      - "Information per syllable was the same in every language"
    answer: 1
    explain: "Speech rate and information per syllable both varied a lot, but they pulled in opposite directions, so the product, information per second, was more similar across languages than either part. Identical speech rates is the opposite of what they found."
  - q: "In the 2011 study, how did Japanese and Mandarin differ?"
    options:
      - "Japanese was spoken faster and carried less information per syllable; Mandarin was slower and denser"
      - "Japanese was slower and denser; Mandarin was faster and sparser"
      - "Both had the same syllable rate but different densities"
      - "Mandarin was excluded because tone could not be measured"
    answer: 0
    explain: "Japanese speakers produced about 7.84 syllables per second with a density of 0.49 relative to Vietnamese, while Mandarin speakers produced about 5.18 syllables per second with a density of 0.94. Mandarin was included; the authors did discuss tone as a measurement problem."
  - q: "What did the 2011 study conclude about whether information rate is constant?"
    options:
      - "It was exactly constant across all seven languages"
      - "It could not be estimated with the data available"
      - "It was not constant: Japanese was lowest, English highest, with a gap over 30 percent, though five languages did not differ significantly"
      - "It was constant for men but not for women"
    answer: 2
    explain: "The earlier paper found the trade-off but stated that it does not necessarily produce a constant rate. The later, larger study is the one that emphasised convergence, which is why the strong 'all languages run at the same speed' version outruns the evidence."
  - q: "Which is the most accurate criticism of this research, given the post?"
    options:
      - "It never measured real speech; it only counted syllables in written dictionaries"
      - "Its 'information' measures how predictable syllables are, not how much meaning is conveyed, and its sample is read speech from mostly Eurasian languages"
      - "It rests on a single study with no follow-up"
      - "It was retracted after other teams could not reproduce the 39 bits per second figure"
    answer: 1
    explain: "Dismissing it as dictionary counting sounds properly sceptical but is wrong: both studies recorded native speakers reading texts aloud and timed them. The real limits are what 'information' means here, the use of read rather than conversational speech, and which languages were sampled. There are two studies, not one, though from an overlapping team."
reflect:
  - "If information here means how predictable the next syllable is, rather than how much meaning gets across, what would you need to measure to test whether languages convey ideas at similar speeds?"
  - "Conversation includes pauses, interruptions and repetition that read speech lacks. Would you expect the convergence to get stronger or weaker in natural talk, and why?"
---

## The idea

Listen to someone speaking Spanish or Japanese and it can sound faster than Mandarin or German. It often is faster, if you count syllables per second. The question a group of linguists in Lyon set out to answer was whether those fast languages actually get more across, or whether each syllable simply carries less.

Their answer is a trade-off. Languages differ in how many distinct syllables they allow. A language with a small set of simple syllables needs more of them to distinguish words, so each one tells a listener less. Speakers of such languages tend to talk faster, measured in syllables. Languages with richer syllables, including tone in Mandarin and Vietnamese, carry more per syllable and are spoken more slowly.

The researchers measured information using Claude Shannon's framework, which counts how unpredictable each unit is. Per the review by cognitive scientist Sean Trott, the 2019 study used the conditional entropy of each syllable given the one before it. Multiply that information density by speech rate and you get an information rate in bits per second.

The concrete example comes from François Pellegrino, Christophe Coupé and Egidio Marsico's 2011 paper in *Language*. Native speakers of seven languages read the same 20 short passages, translated. Japanese speakers produced about 7.84 syllables per second, with a density of 0.49 relative to Vietnamese as the reference. Mandarin speakers produced about 5.18 syllables per second, with a density of 0.94. Mandarin and Spanish ended up within about 4 percent of each other in information rate by opposite routes: one slow and dense, the other fast and sparse.

In 2019 Coupé, Yoon Mi Oh, Dan Dediu and Pellegrino extended this to 17 languages in *Science Advances*, including Basque, Thai, Vietnamese, Finnish and Turkish. Density ranged from about 5 to 8 bits per syllable, according to the CNRS press release, yet information rates clustered around 39 bits per second. The abstract says languages are more alike in information rate than in either density or speed taken alone.

## Why it might change a decision

The idea makes a specific, testable prediction about anyone judging a language by how fast it sounds. If you time native speakers reading translations of the same passage, the languages with the highest syllable rates should not finish proportionally sooner. A listener who infers that a fast-sounding speaker is conveying more, or rushing, would be reading the wrong signal. The same prediction applies to anything timed by syllables rather than content, such as estimating how long a dubbed line or a spoken announcement will take in another language.

## How solid is this?

The evidence comes mainly from two studies by an overlapping team, both using read speech recorded in the lab. The 2011 study had 59 speakers (29 men, 30 women) and seven languages plus a Vietnamese reference, 585 recordings in all. The 2019 study had 17 languages, 10 native speakers each and 15 short texts, per the CNRS release.

The trade-off itself is the strongest result. In 2011 the negative relation between density and speed was clear, with a confidence interval well away from zero. The constancy claim is weaker. The 2011 paper found that the trade-off does "not necessarily lead to a constant information rate": Japanese had the lowest rate and English the highest, a gap of more than 30 percent, while five languages did not differ significantly. Speaker sex also affected both speech rate and information rate. Popular summaries that say every language transmits at exactly the same speed outrun these data.

Three competing explanations deserve weight. First, "information" here is about predictability of syllables, not meaning; Trott points out that a language could score high by this measure without conveying ideas faster. Second, conditional entropy depends partly on how many syllables a language has, so the speed effect might track syllable inventory rather than predictability in use. Third, the sample has no Niger-Congo or Afro-Asiatic languages, and read speech lacks the pauses and repairs of conversation, which the 2011 authors themselves flagged. The authors' own interpretation, that the convergence reflects limits of human processing shaped over time by communication, is a hypothesis these designs cannot test directly.

## Sources

- Pellegrino, F., Coupé, C., & Marsico, E. (2011). A cross-language perspective on speech information rate. *Language*, 87(3), 539–558. [doi:10.1353/lan.2011.0057](https://www.cambridge.org/core/journals/language/article/abs/crosslanguage-perspective-on-speech-information-rate/73064B3F77E7CE81C42CAB29B4393F80)
- Coupé, C., Oh, Y. M., Dediu, D., & Pellegrino, F. (2019). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. *Science Advances*, 5(9), eaaw2594. [doi:10.1126/sciadv.aaw2594](https://hub.hku.hk/handle/10722/283058)
- CNRS (2019, September 4). Similar information rates across languages, despite divergent speech rates. [Press release](https://www.cnrs.fr/en/press/similar-information-rates-across-languages-despite-divergent-speech-rates)
- Trott, S. Do different languages really convey information at the same rate? [Research review](https://seantrott.github.io/information)
