---
title: "How reliable are AI text detectors?"
date: 2026-10-27
topics: [AI, statistics]
summary: "Tools that claim to spot machine-written text are used to judge essays and applications. The research suggests they misfire most on some human writers, can be evaded by rewording, and that even a small error rate produces many false accusations when most writing is human."
status: published
quiz:
  - q: "In Liang and colleagues' study, what happened when seven detectors were run on 91 human-written TOEFL essays?"
    options:
      - "On average about 61 percent of the essays were wrongly flagged as AI-written"
      - "Almost none were flagged, while US eighth-grade essays were often flagged"
      - "Every essay was flagged by all seven detectors"
      - "The detectors refused to give a verdict on non-native writing"
    answer: 0
    explain: "The average false positive rate was 61.22 percent. All seven agreed on 18 of the 91, not all of them. The eighth-grade essays were the group detectors mostly got right."
  - q: "A detector catches 90 percent of AI-written essays and wrongly flags 2 percent of human ones. In a class where only 2 percent of essays are AI-written, roughly what share of flagged essays are actually human?"
    options:
      - "About 2 percent, the false positive rate"
      - "About 10 percent, the share the detector misses"
      - "About half"
      - "None, because the detector is 98 percent accurate on humans"
    answer: 2
    explain: "Out of 1,000 essays, about 18 of the 20 AI essays are flagged, and about 20 of the 980 human essays are too. So roughly half of the flags land on human writers. The 2 percent figure applies to all human essays, not to the flagged pile."
  - q: "How does the Kirchenbauer watermark work?"
    options:
      - "It hides a visible signature at the end of each generated paragraph"
      - "The model is nudged towards a pseudo-randomly chosen 'green' set of words, and a statistical test counts how many green words a text contains"
      - "A second AI model is trained to recognise the style of the first"
      - "It compares the text against a database of everything the model has generated"
    answer: 1
    explain: "The method shifts sampling slightly towards a green list chosen before each word, and detection checks whether green words are over-represented. It needs no access to the model. Retrieval against a database is a different approach, one of those Sadasivan and colleagues tested."
  - q: "Which statement about the evidence is fairest?"
    options:
      - "Watermarking has never been tested empirically, so its claimed error rates are pure theory"
      - "Liang's study shows detectors are useless on all text"
      - "Watermark detection was highly accurate in its authors' tests, but other researchers report that rewording attacks can reduce detection, and the text must come from a model that applies the watermark"
      - "Sadasivan's paper proves that no detector can ever beat a coin toss"
    answer: 2
    explain: "Kirchenbauer's team tested the watermark on a multi-billion-parameter model and reported detecting 98.4 percent of generations at their threshold, so the 'never tested' option sounds sceptical but is wrong. Sadasivan's theoretical result links the best possible accuracy to how different the two kinds of text are; it does not say detection is always at chance."
reflect:
  - "A university is considering using a detector to open misconduct cases. What information about its error rates, and about the students it will be used on, would you want before judging whether a flag means much?"
  - "If watermarking only works when the model provider chooses to apply it, what does that imply about detecting text from openly available models?"
---

## The idea

Since chatbots became widely available, a market has grown for tools that estimate whether a piece of writing came from a person or a language model. Many work by measuring perplexity: roughly, how predictable each word is to a language model. Machine text tends to be predictable, so low perplexity is read as a sign of AI.

In 2023 Weixin Liang, James Zou and colleagues at Stanford tested seven widely used detectors, in work published in *Patterns*. On 88 essays by US eighth-grade students, the detectors did reasonably well. On 91 essays written by non-native English speakers for the TOEFL exam, they flagged an average of 61.22 percent as AI-generated. Eighteen essays were flagged by all seven detectors, and 89 of the 91 by at least one. The authors attribute this to perplexity: writers with a smaller vocabulary and simpler grammar produce predictable text, which is what the detectors look for.

## Why it might change a decision

The key arithmetic is about base rates. Take a detector, illustrative rather than drawn from any study, that catches 90 percent of AI essays and wrongly flags 2 percent of human ones. Run it on 1,000 essays.

If 100 of them are AI-written, it flags 90 of those plus 2 percent of the 900 human essays, which is 18. So 18 of 108 flags, about one in six, accuse a human.

If only 20 are AI-written, it flags 18 of those plus 2 percent of 980 human essays, about 20. Now roughly half of all flags land on human writers. The detector has not changed; only the mix of writing has.

The testable prediction is that the share of flagged work that is actually human should rise as genuine AI use becomes rarer, and rise further for groups, such as non-native writers, on whom the false positive rate is higher. A 2 percent false positive rate is not a 2 percent chance that a flagged essay is innocent.

## How solid is this?

Liang's study is a single study with small samples: 91 TOEFL essays from one online forum and 88 American essays. The pattern was large and the mechanism plausible, and in a further test, rewording the TOEFL essays with richer vocabulary cut the average false positive rate to 11.77 percent, while simplifying the American essays raised theirs from 5.19 to 56.65 percent. These figures come from the preprint version of the paper; detectors are updated often, so the exact rates may not hold for current versions.

A second line of work asks whether detection can be made reliable at all. Vinu Sankar Sadasivan, Soheil Feizi and colleagues, in a 2023 preprint, attacked several kinds of detector, including watermark-based, trained-classifier and zero-shot tools, by passing AI text of about 300 tokens repeatedly through a paraphrasing model. Detection rates fell substantially, often with only a slight loss of quality. They also showed spoofing: making human text appear watermarked. Their theoretical result ties the best achievable accuracy to how different human and machine text are; as models write more like people, the ceiling falls. This is an argument about limits, not a measurement of any one product.

The strongest counterposition is watermarking. John Kirchenbauer, Tom Goldstein and colleagues, at ICML in 2023, proposed that a model gently favour a pseudo-randomly chosen "green" subset of words as it writes. Anyone with the key can count green words and compute a p-value. At their threshold the chance of flagging unwatermarked text is about 3 in 100,000, and in their tests 98.4 percent of watermarked generations were detected. The authors note limits: it only works on text from a model that applies it, and rewording attacks weaken it, though they report that removing it from a long passage requires changing a large share of the words.

The popular claim that a detector can tell you whether a given student cheated outruns the data. Whether watermarking can hold up against determined rewording is still being argued.

## Sources

- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns*, 4(7), 100779. [doi:10.1016/j.patter.2023.100779](https://doi.org/10.1016/j.patter.2023.100779). Figures quoted from the preprint: [arXiv:2304.02819](https://arxiv.org/abs/2304.02819)
- Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W., & Feizi, S. (2023). Can AI-generated text be reliably detected? *arXiv preprint* 2303.11156. [arxiv.org/abs/2303.11156](https://arxiv.org/abs/2303.11156)
- Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., & Goldstein, T. (2023). A watermark for large language models. *Proceedings of the 40th International Conference on Machine Learning*, PMLR 202, 17061-17084. [proceedings.mlr.press/v202/kirchenbauer23a](https://proceedings.mlr.press/v202/kirchenbauer23a.html)
