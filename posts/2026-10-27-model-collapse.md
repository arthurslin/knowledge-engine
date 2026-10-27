---
title: "Do AI models decay when they learn from each other?"
date: 2026-10-27
topics: [AI, machine learning]
summary: "A 2024 Nature paper showed that generative models trained repeatedly on their own output lose the rare parts of what they learned. A follow-up argued that the outcome depends heavily on whether synthetic data replaces real data or is added to it."
status: published
quiz:
  - q: "According to Shumailov and colleagues, what is lost first in early model collapse?"
    options:
      - "The most common, typical examples in the data"
      - "The model's ability to produce grammatical sentences"
      - "The tails of the original distribution: the rare cases"
      - "The model's training speed"
    answer: 2
    explain: "Early collapse is defined as losing information about the tails. Typical cases survive longest, which is why a collapsing model can look fine on average while its outputs grow narrower."
  - q: "What is the key difference between the 'replace' and 'accumulate' set-ups that Gerstgrasser and colleagues compared?"
    options:
      - "Replace trains each new model only on the previous model's output; accumulate keeps the original real data and adds each round's synthetic data to it"
      - "Replace uses larger models; accumulate uses smaller ones"
      - "Replace uses human-written data; accumulate uses only synthetic data"
      - "Replace fine-tunes; accumulate trains from scratch"
    answer: 0
    explain: "The comparison is about what happens to the real data. Under replacement it is discarded after the first round; under accumulation it stays in the pool. Model size and fine-tuning are not what separates the two conditions."
  - q: "What did Shumailov and colleagues report when 10% of the original data was kept in each generation of their language model experiment?"
    options:
      - "Collapse happened faster than with no original data"
      - "Only minor degradation"
      - "Complete recovery to better than the original model"
      - "They did not test this condition"
    answer: 1
    explain: "Keeping a random 10% of the real data led to only minor degradation, compared with clearer losses when no original data was kept. This partial result points in the same direction as the accumulation findings."
  - q: "Which is the fairest description of the evidence reviewed here?"
    options:
      - "Gerstgrasser and colleagues showed that accumulating data removes any degradation in every model type they tried"
      - "Both papers studied small models over a limited number of generations, and accumulation slowed but did not always stop degradation"
      - "The Nature paper can be set aside because it tested only image models, not language models"
      - "Collapse has been observed in the large commercial models now in use"
    answer: 1
    explain: "The Nature paper did include a language model, OPT-125m, so the 'images only' objection sounds sceptical but is wrong. The real limits are model size, the small number of generations, and the fact that accumulation still allowed slow error growth for VAEs and when compute was matched."
reflect:
  - "The web now contains a growing share of machine-written text that is not labelled as such. Is the real web closer to the 'replace' or the 'accumulate' condition, and what would you need to measure to find out?"
  - "Collapse first removes rare cases. In a field you know, which rare but important cases would be hardest to notice going missing from a model's output?"
---

## The idea

Generative models such as large language models learn from text and images gathered at scale, much of it from the web. As those models produce more of what is online, later models will increasingly be trained on their predecessors' output. Ilia Shumailov and colleagues, in *Nature* in 2024, asked what happens when that loop repeats.

Their answer was that indiscriminate training on model-generated content causes what they called model collapse. They describe two stages. In early collapse, the model begins losing information about the tails of the distribution: the rare words, unusual cases and minority patterns. In late collapse, the model converges on something that bears little resemblance to the original data, often with much less variety. They attribute this mainly to statistical approximation error: each generation sees only a finite sample, so rare events are likely to be missed, and once missed they cannot be learned back. Limits on what a model can represent, and on how it is trained, add further error.

A concrete version: suppose a word appears once in a million sentences. A model trained on a modest sample may never see it and so never produce it. The next model, trained on the first model's output, has no chance of learning it at all. Repeat this and the distribution narrows round by round.

They demonstrated the effect in simple Gaussian mixture models, in variational autoencoders, and in a language model, OPT-125m, fine-tuned on the wikitext2 dataset over several generations.

## Why it might change a decision

The two studies discussed here make a sharp, testable distinction. If each new model is trained only on the previous model's output, quality should keep falling. If the original human data is kept and synthetic data is added on top, quality should degrade much more slowly or level off. That changes what matters in practice: not just whether synthetic data is present, but whether the real data is retained alongside it.

## How solid is this?

Both papers are controlled experiments on small models over a limited number of generations, supported by theory on idealised models. Neither observes collapse in deployed commercial systems.

Shumailov and colleagues fine-tuned a pre-trained model rather than training from scratch, and say larger models were not tested because of cost. Their theory concerns many generations, while experiments ran only a few; they note full collapse may or may not appear within a small number of steps. They also found that keeping a random 10% of the original data in each generation led to only minor degradation. A correction to the paper was published in 2025.

Matthias Gerstgrasser and colleagues, in a 2024 preprint, argued that the main set-up behind alarming results was data replacement, where each round's synthetic data stands in for the real data. They pretrained small language models (GPT-2 at 9 million parameters and Llama 2 models up to about 125 million) on the TinyStories dataset. Replacing data raised test error as iterations went on; accumulating synthetic data alongside the real data gave equal or lower error. They found similar patterns in diffusion models for molecules and in VAEs for images. In a linear regression model they proved that under accumulation the error stays below a fixed bound however many rounds pass, whereas under replacement it grows steadily.

Their own caveats matter. Accumulation trains on ever larger datasets; when they matched the amount of compute, performance still degraded, though more slowly. For VAEs, error under accumulation still rose with iterations. They note an earlier study that found fast deterioration even with accumulation and leave the conflict unresolved. Their conclusion is that recursion "may not be as dire as had been portrayed", not that the problem is solved.

The popular claim that AI will inevitably poison itself outruns these data. So does the reverse claim that accumulation makes the concern irrelevant. What is supported is narrower: repeated training on synthetic data alone loses rare information, and keeping real data in the mix substantially reduces, but does not always eliminate, the loss in small models. Whether the real web behaves more like replacement or accumulation is an open question neither paper measured.

## Sources

- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*, 631, 755-759. [doi:10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y)
- Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D. A., Yang, D., Donoho, D. L., & Koyejo, S. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *arXiv preprint*. [arXiv:2404.01413](https://arxiv.org/abs/2404.01413)
