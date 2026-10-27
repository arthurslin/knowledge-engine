---
title: "How big should a language model be for the compute you have?"
date: 2026-10-27
topics: [AI, machine learning]
summary: "Two influential papers fitted simple laws to predict how AI language models improve with size, data and computing power, and gave very different advice on how to split a budget. The later answer, from DeepMind's Chinchilla work, has largely held up, though one of its own fits turned out to be flawed."
status: published
quiz:
  - q: "What did Kaplan and colleagues (2020) conclude about spending a larger compute budget?"
    options:
      - "Model size and training data should grow in equal proportion"
      - "Most of the extra compute should go into training a smaller model on far more data"
      - "Most of the extra compute should go into a bigger model, with data growing more slowly"
      - "Extra compute gives no further improvement beyond about a billion parameters"
    answer: 2
    explain: "Their fit had optimal model size growing as compute to the power 0.73 and data only as 0.27, so an 8x larger model needed only about 5x more data. Equal scaling was Hoffmann and colleagues' later conclusion, not Kaplan's."
  - q: "How was Chinchilla trained compared with Gopher?"
    options:
      - "With the same compute, a quarter of the parameters and over four times the training tokens"
      - "With four times the compute and four times the parameters"
      - "With the same parameters but a different learning rate schedule"
      - "With less compute and less data, as a cheaper baseline"
    answer: 0
    explain: "Chinchilla had 70 billion parameters and 1.4 trillion tokens; Gopher had 280 billion parameters and 300 billion tokens, on the same budget. A learning rate schedule difference is part of the explanation for Kaplan's result, not the Chinchilla design."
  - q: "What did Besiroglu and colleagues find when they tried to replicate Hoffmann et al.'s third method?"
    options:
      - "The data could not be recovered, so no check was possible"
      - "The reported fit was inconsistent with the other two methods, and its confidence intervals were implausibly narrow; a refit agreed with the other methods"
      - "All three of Hoffmann et al.'s methods were wrong, and Kaplan's original allocation was correct after all"
      - "The fit was correct, but Chinchilla itself had been trained on too few tokens"
    answer: 1
    explain: "They reconstructed the data from the paper's figures, found the published parameters fitted it poorly and the intervals far too tight, and their own fit gave about 20 tokens per parameter, in line with Approaches 1 and 2 and with how Chinchilla was trained."
  - q: "Which is the fairest reading of the evidence described in the post?"
    options:
      - "Because one of Hoffmann et al.'s fits was flawed, the whole Chinchilla result should be treated as unreliable"
      - "Equal scaling of size and data is now proven to hold at every scale"
      - "Independent work has largely reconciled the two papers in Hoffmann et al.'s favour, but the laws are empirical fits with real uncertainty when extrapolated"
      - "Kaplan's and Hoffmann's results disagree only because they used different definitions of compute, so neither was wrong"
    answer: 2
    explain: "The flawed fit was one of three methods; the replication's refit agreed with the other two, and Porian and colleagues traced Kaplan's numbers to specific setup choices. Dismissing the whole result sounds suitably sceptical but misreads what the replication found. Hoffmann et al. themselves flagged uncertainty when extrapolating."
reflect:
  - "A 'compute-optimal' recipe minimises training cost for a given quality. Who would choose a different recipe, and what costs would they be counting instead?"
  - "Scaling laws are fitted on small runs and then extrapolated to models costing far more. What kinds of evidence would make you trust such an extrapolation more, or less?"
---

## The idea

Training a large language model means making a budget decision before you start. For a fixed amount of computing power, you can train a bigger model on less text, or a smaller model on more text. Scaling laws are attempts to answer that trade-off with formulas fitted to many smaller training runs.

In January 2020 Jared Kaplan and colleagues posted a paper on arXiv showing that a model's test loss, a measure of how badly it predicts the next word, fell as a smooth power law as model size, dataset size and compute increased, across many orders of magnitude. Their models ranged from 768 to 1.5 billion parameters, trained on up to 23 billion tokens of web text. From those curves they derived an allocation rule: optimal model size should grow roughly as compute to the power 0.73, and data only as 0.27. In their words, when the model grows eightfold, the data needs to grow by only about five times. The practical message was to build very large models and train them on comparatively modest amounts of data.

In March 2022 Jordan Hoffmann and colleagues at DeepMind reached a different answer. Training more than 400 models, from 70 million to over 16 billion parameters on 5 to 500 billion tokens, and analysing them three separate ways, they found that model size and training data should grow in roughly equal proportion. Their exponents for model size ranged from 0.46 to 0.50, against Kaplan's 0.73. By that reckoning, many large models of the time were undertrained. To test it they built Chinchilla: 70 billion parameters trained on 1.4 trillion tokens, using the same compute as their earlier 280 billion parameter Gopher, which had seen 300 billion tokens. Chinchilla outperformed Gopher and several other larger models on a wide range of benchmarks.

## Why it might change a decision

The two rules make different, checkable predictions. Under Kaplan's allocation, a lab with ten times more compute should mostly buy parameters. Under Hoffmann's, it should split the increase between parameters and data, and a model trained on about 20 tokens per parameter should beat a larger model trained on fewer tokens for the same compute. The Chinchilla versus Gopher comparison was one direct test of that prediction.

## How solid is this?

Both papers are large empirical studies, not single runs, but each is one lab's set of experiments, and the laws are fitted curves rather than derived from theory. Hoffmann and colleagues themselves noted slight curvature in their results and significant uncertainty when extrapolating many orders of magnitude. Their head-to-head test rested on essentially one pair of large models.

They explained the disagreement mainly by method: Kaplan's team used a fixed number of training tokens and learning rate schedule for all models, and most of their runs were small. A 2024 study by Tomer Porian and colleagues reproduced Kaplan's law and traced the gap to three other factors: how the cost of the model's final layer was counted, the length of the warmup period, and optimiser settings that were not adjusted with scale. With those corrected, their results agreed closely with Chinchilla. They also found that careful learning rate decay was not essential, contrary to a hypothesis Hoffmann and colleagues had offered.

The Chinchilla paper has its own problem. In 2024 Tamay Besiroglu and colleagues reconstructed the data behind Hoffmann's third method from the paper's figures and refitted it. The published parameters fitted the data poorly and were inconsistent with the other two methods; the reported confidence intervals were so narrow that they would have needed over 600,000 experiments, where Hoffmann's team likely ran fewer than 500. The published fit implied about 70 tokens per parameter; the refit gave about 20, matching the other two methods and Chinchilla's actual training. The replicators report that a lead author of the original paper attributed the narrow intervals to a high loss scale, a fitting setting which, the replicators argue, made the optimiser stop early. So one of three estimates was flawed, and the headline conclusion survived.

The popular shorthand that "20 tokens per parameter" is simply optimal outruns the data in another way. It minimises training compute only. Nikhil Sardana and colleagues showed that once the cost of running a model for many users is counted, it pays to train smaller models for longer, and quality kept improving in their tests up to 10,000 tokens per parameter.

## Sources

- Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). Scaling laws for neural language models. *arXiv preprint* 2001.08361. [arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361)
- Hoffmann, J., Borgeaud, S., Mensch, A., et al. (2022). Training compute-optimal large language models. *arXiv preprint* 2203.15556. [arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556)
- Besiroglu, T., Erdil, E., Barnett, M., & You, J. (2024). Chinchilla scaling: A replication attempt. *arXiv preprint* 2404.10102. [arxiv.org/abs/2404.10102](https://arxiv.org/abs/2404.10102)
- Porian, T., Wortsman, M., Jitsev, J., Schmidt, L., & Carmon, Y. (2024). Resolving discrepancies in compute-optimal scaling of language models. *arXiv preprint* 2406.19146. [arxiv.org/abs/2406.19146](https://arxiv.org/abs/2406.19146)
- Sardana, N., Portes, J., Doubov, S., & Frankle, J. (2023). Beyond Chinchilla-optimal: Accounting for inference in language model scaling laws. *arXiv preprint* 2401.00448. [arxiv.org/abs/2401.00448](https://arxiv.org/abs/2401.00448)
