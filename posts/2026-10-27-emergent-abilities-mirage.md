---
title: "Do language models gain abilities suddenly as they grow?"
date: 2026-10-27
topics: [AI, research methods]
summary: "A 2022 paper catalogued skills that seemed to switch on abruptly in large language models. A 2023 reply argued many of those jumps were produced by how the tests were scored. Later work suggests both camps captured part of the picture."
status: published
quiz:
  - q: "How did Wei and colleagues define an emergent ability?"
    options:
      - "Any ability that improves as a model gets larger"
      - "An ability not present in smaller models but present in larger ones, which cannot be predicted by extrapolating from the smaller ones"
      - "An ability the model was never shown in its training data"
      - "An ability that appears only after fine-tuning on human feedback"
    answer: 1
    explain: "The definition is about a jump with scale that extrapolation would miss. Steady improvement with size is the ordinary scaling pattern the paper contrasts it with, and the definition says nothing about training data or fine-tuning."
  - q: "What is the core of Schaeffer, Miranda and Koyejo's argument?"
    options:
      - "Large models secretly memorise the test sets, so their scores are invalid"
      - "Emergent abilities are real but appear only in models with more than a trillion parameters"
      - "Scoring that gives credit only for a fully correct answer can turn smooth underlying improvement into an apparent sudden jump"
      - "Larger models are worse at arithmetic than smaller ones"
    answer: 2
    explain: "Their claim is about measurement. Exact-match style metrics give zero until every token is right, so steady gains in each token look like nothing, then a leap. Under per-token or probabilistic scores the same outputs improved smoothly. Memorisation is closer to Lu and colleagues' later argument."
  - q: "What did Du and colleagues (2024) report when they plotted performance against pre-training loss instead of model size?"
    options:
      - "All tasks improved smoothly, confirming that emergence is purely a scoring artefact"
      - "On some tasks, including MMLU and GSM8K, performance stayed near chance until loss fell below about 2.2, and this held on continuous metrics too"
      - "Pre-training loss had no relationship to downstream performance"
      - "Only models above 100 billion parameters could be tested"
    answer: 1
    explain: "They found a threshold pattern on four tasks that persisted under Brier score and the probability of the correct choice, while other tasks such as HellaSwag improved smoothly. Their models ranged from 300 million to 32 billion parameters."
  - q: "Which is the fairest reading of the evidence described in this post?"
    options:
      - "The mirage paper settled the question: no language model ability is emergent"
      - "Wei and colleagues ignored the possibility that metrics might matter"
      - "The mirage paper is weak because it only examined a single benchmark"
      - "Metric choice explains many claimed jumps, but some threshold-like behaviour has survived continuous metrics, so the question remains open"
    answer: 3
    explain: "Schaeffer and colleagues analysed GPT-3 family models, a BIG-Bench meta-analysis and vision models, so the 'single benchmark' objection sounds cautious but is wrong. Wei and colleagues also discussed metrics themselves, and the mirage authors explicitly said they were not claiming emergence never happens."
reflect:
  - "If an ability only matters to users when an answer is fully correct, such as a working line of code, is a smooth improvement in partial credit reassuring or beside the point?"
  - "Emergence was plotted against parameters, training compute and pre-training loss in different papers. What would you need to know about a new model before deciding which of those axes is the fair one for a prediction?"
---

## The idea

In 2022 sixteen authors led by Jason Wei published a paper in *Transactions on Machine Learning Research* titled "Emergent Abilities of Large Language Models". Their definition was short: an ability is emergent if it is "not present in smaller models but is present in larger models." The important part is that such an ability cannot be predicted by extrapolating the performance of smaller models.

The paper collected examples from published work. On three-digit addition and subtraction, GPT-3 scored near chance until roughly 13 billion parameters, then climbed. On a broad knowledge test, MMLU, models of about 10 billion parameters performed at guessing level, while models between 70 and 280 billion did substantially better. Prompting techniques also seemed to switch on: asking a model to reason step by step (chain-of-thought prompting) only beat ordinary prompting on maths word problems at about 100 billion parameters. If abilities appear abruptly, then building a bigger model could produce capabilities nobody anticipated.

In 2023 Rylan Schaeffer, Brando Miranda and Sanmi Koyejo at Stanford published a reply at NeurIPS, presented as an oral, titled "Are Emergent Abilities of Large Language Models a Mirage?" Their argument concerned measurement. Many tasks are scored by exact match: the answer counts only if every token is right. If a model's chance of getting each digit right rises steadily with size, the chance of getting all five digits right will stay near zero for a long time and then shoot up. The jump is in the scoring rule, not necessarily in the model.

## Why it might change a decision

The two positions make different predictions about the same outputs. If emergence is mainly a scoring artefact, then rescoring a model's answers with a continuous measure, such as how many tokens differ from the correct answer or a Brier score on multiple-choice probabilities, should turn an abrupt curve into a smooth one, and smaller models' progress should be visible in advance. If emergence is real, the jump should survive any reasonable metric.

## How solid is this?

Both sides rest on reanalyses of existing models rather than controlled experiments, and neither is a single study in isolation.

Schaeffer and colleagues tested their prediction three ways. On GPT-3 family models doing arithmetic, accuracy showed apparent emergence for longer answers, while token edit distance on the same outputs improved smoothly; with more test questions, every model in the family scored above chance. In a meta-analysis of the BIG-Bench benchmark, they found two metrics, multiple choice grade and exact string match, accounted for more than 92 percent of claimed emergent abilities. They also induced apparent emergence in vision models simply by choosing a harsh metric. They stated that they were not claiming large models cannot have emergent abilities, and noted that several models with claimed emergence, including PaLM and Chinchilla, were not available for them to test.

Wei and colleagues had anticipated part of this. Their paper noted that exact-match scoring might disguise compounding incremental improvements, that a model's cross-entropy loss improved even where accuracy sat at chance, and that for three generative tasks emergence appeared under several different metrics. They called metric choice an incomplete explanation.

Later work has not settled the matter. Zhengxiao Du and colleagues, at NeurIPS 2024, trained 31 models from scratch, from 300 million to 32 billion parameters, and plotted performance against pre-training loss rather than size. On MMLU, its Chinese counterpart C-Eval, and two maths word-problem sets, performance stayed near chance until loss fell below about 2.2, and this threshold held under continuous measures such as Brier score. Other tasks improved smoothly throughout. Their results come from one lab's models and data, so the specific threshold may not transfer.

Sheng Lu and colleagues, at ACL 2024, ran more than 1,000 experiments and argued that apparent emergent abilities are better explained by in-context learning, model memory and linguistic knowledge combined, rather than by new abilities appearing.

The popular claim that models unpredictably acquire new skills outruns the data: many reported jumps shrink or vanish under a different metric. The opposite popular claim, that emergence has been shown to be a mirage, also outruns it, since some threshold-like behaviour survives continuous scoring. What counts as the right metric may depend on what users need, which the mirage authors themselves acknowledged.

## Sources

- Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W. (2022). Emergent abilities of large language models. *Transactions on Machine Learning Research*. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682)
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *Advances in Neural Information Processing Systems 36* (NeurIPS 2023). [arXiv:2304.15004](https://arxiv.org/abs/2304.15004)
- Du, Z., Zeng, A., Dong, Y., & Tang, J. (2024). Understanding emergent abilities of language models from the loss perspective. *Advances in Neural Information Processing Systems 37*, 53138-53167. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5f1eee2509599faeeb3570a887016a64-Abstract.html)
- Lu, S., Bigoulaeva, I., Sachdeva, R., Tayyar Madabushi, H., & Gurevych, I. (2024). Are emergent abilities in large language models just in-context learning? *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 5098-5139. [doi:10.18653/v1/2024.acl-long.279](https://doi.org/10.18653/v1/2024.acl-long.279)
