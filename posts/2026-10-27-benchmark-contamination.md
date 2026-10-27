---
title: "When AI models have seen the exam: benchmark contamination"
date: 2026-10-27
topics: [AI, research methods]
summary: "AI models are ranked by scores on public test sets, and those test sets can leak into training data. Fresh, matched test sets show real but uneven drops in performance, and not every drop means the model memorised the answers."
status: published
quiz:
  - q: "What did Zhang and colleagues build to test for overfitting on grade school maths?"
    options:
      - "A harder version of GSM8k with multi-step proofs"
      - "GSM1k, a new set of problems designed to match GSM8k in style and difficulty"
      - "A tool that scans training data for copies of test questions"
      - "A survey of developers asking whether they trained on GSM8k"
    answer: 1
    explain: "GSM1k was built to mirror GSM8k on measures such as human solve rates and the number of solution steps, so a fall in score would point to overfitting rather than harder questions. It was not a search of training data."
  - q: "How does Golchin and Surdeanu's 'guided instruction' method look for contamination?"
    options:
      - "It gives the model the dataset name and the start of a test item, and checks whether the model completes it exactly or nearly so"
      - "It reads the model's training data directly"
      - "It retrains the model without the test set and compares scores"
      - "It asks human experts to guess which items the model has seen"
    answer: 0
    explain: "The method needs no access to training data. It prompts with the dataset name, the partition and a partial item, and flags near-exact completions. Human experts were used only to check how accurate the method was."
  - q: "What did Recht and colleagues conclude caused the accuracy drops on their new ImageNet and CIFAR-10 test sets?"
    options:
      - "Years of researchers tuning models on the same test set"
      - "Mislabelled images in the new test sets"
      - "Not reuse of the test set, but models struggling with images slightly harder than those in the originals"
      - "Training data that contained copies of the test images"
    answer: 2
    explain: "The intuitive guess is adaptive overfitting from reusing the test set. The authors argued against it, partly because gains on the old test sets carried over to the new ones. They attributed the drops to the new images being slightly harder."
  - q: "Which is the fairest reading of the GSM1k results?"
    options:
      - "All models, including frontier ones, had simply memorised GSM8k and cannot solve new problems"
      - "Drops of up to 8% appeared, several model families showed systematic overfitting, many frontier models showed little, and all models could solve new problems"
      - "The results are meaningless because the study tested only one model"
      - "No model scored lower on the new problems"
    answer: 1
    explain: "The study covered many open and closed models, so the 'only one model' objection sounds cautious but is wrong. The finding is uneven: some families overfit, many did not, and every model generalised to some degree."
reflect:
  - "If a company publishes a new benchmark today, what would stop it being contaminated within a year or two? Which of the methods described here would still work then?"
  - "Recht and colleagues found that drops can come from a subtle shift in difficulty. How would you tell such a shift apart from memorisation when building a fresh test set?"
---

## The idea

Machine learning progress is mostly measured with benchmarks: fixed sets of test questions that every new model is scored on. The method rests on one assumption, that the model has not seen the test questions during training. A student who has read the exam paper in advance is not showing what they have learned.

For modern large language models that assumption is hard to guarantee. They are trained on enormous scrapes of the web, and popular benchmarks are published on the web, discussed in forums and copied into tutorials. When test items, or close paraphrases of them, end up in training data, the benchmark is said to be contaminated. A related problem is overfitting to the benchmark: even without exact copies, years of choosing methods by their scores on one test set can tune a field to that set's quirks.

A concrete example: GSM8k is a widely used set of grade school maths word problems. In 2024 Hugh Zhang and colleagues wrote a new set, GSM1k, built to match GSM8k on human solve rates, number of solution steps, answer size and other measures. If a model really can do grade school maths, it should score about the same on both.

## Why it might change a decision

The prediction is simple and checkable. If a model's benchmark score reflects contamination, it should fall on a fresh test set drawn the same way, and the fall should be larger for models more likely to have seen the original. That changes how a careful reader treats a leaderboard: a score on an old public benchmark says less than a score on a recently written or private one, and the gap between the two is itself informative.

## How solid is this?

The evidence comes from a handful of studies using different methods, which point in a similar direction with important caveats.

Zhang and colleagues found that leading open and closed models dropped by up to 8% in accuracy on GSM1k compared with GSM8k, and that several model families showed signs of systematic overfitting. They also measured how likely each model was to generate GSM8k examples, and found a positive relationship with the size of its score gap (Spearman r² = 0.36), which suggests partial memorisation. The same abstract is careful about the other side: many models, especially frontier ones, showed minimal overfitting, and all models could solve new problems they had not seen. The paper appeared in the NeurIPS 2024 Datasets and Benchmarks track.

Shahriar Golchin and Mihai Surdeanu (2023) tackled detection without access to training data. Their method prompts a model with a dataset's name, the partition (such as test) and the opening of an item, then checks whether the model completes it exactly or nearly so. Against judgements by human experts, their best version was 92% to 100% accurate across seven datasets. They reported that GPT-4 appeared to be contaminated with three of them: AG News, WNLI and XSum. A limitation is that the method only catches items a model can reproduce; a model could have learned from leaked items without reciting them.

The older analogue complicates the story. In 2019 Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt and Vaishaal Shankar rebuilt test sets for two image classification benchmarks, CIFAR-10 and ImageNet, by closely following the original collection procedures. Across a broad range of models, accuracy fell by 3% to 15% on CIFAR-10 and 11% to 14% on ImageNet. That looks like overfitting, but the authors argued otherwise: models that did better on the old test sets also did better on the new ones, with gains that were even larger on the new sets. They attributed the drops to models struggling with images slightly harder than those in the originals, not to a decade of test set reuse.

That points to the strongest competing explanation for any drop on a fresh test set: the new set may simply be a little different or harder, however carefully it is matched. Zhang and colleagues tried to rule this out by matching on human solve rates, but no matching is perfect. The popular claim that leaderboard scores are mostly memorisation outruns the data. The narrower claim, that contamination inflates some scores for some models by measurable amounts, is supported, with the size varying a lot between models.

## Sources

- Zhang, H., Da, J., Lee, D., Robinson, V., Wu, C., Song, W., Zhao, T., Raja, P., Zhuang, C., Slack, D., Lyu, Q., Hendryx, S., Kaplan, R., Lunati, M., & Yue, S. (2024). A careful examination of large language model performance on grade school arithmetic. *NeurIPS 2024 Datasets and Benchmarks Track*. [arXiv:2405.00332](https://arxiv.org/abs/2405.00332)
- Golchin, S., & Surdeanu, M. (2023). Time travel in LLMs: Tracing data contamination in large language models. [arXiv:2308.08493](https://arxiv.org/abs/2308.08493)
- Recht, B., Roelofs, R., Schmidt, L., & Shankar, V. (2019). Do ImageNet classifiers generalize to ImageNet? *Proceedings of the 36th International Conference on Machine Learning*, PMLR 97, 5389-5400. [proceedings.mlr.press/v97/recht19a](https://proceedings.mlr.press/v97/recht19a)
