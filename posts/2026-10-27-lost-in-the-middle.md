---
title: "Why language models lose track of the middle"
date: 2026-10-27
topics: [AI, machine learning]
summary: "Language models that accept very long inputs tend to use information at the start and end better than information in the middle. The effect is well documented; how much of it survives in newer models is less clear."
status: published
quiz:
  - q: "In Liu et al.'s multi-document question answering test, where did models tend to perform worst?"
    options:
      - "When the relevant document came first"
      - "When the relevant document came last"
      - "When the relevant document sat in the middle of the input"
      - "Performance was the same wherever the document was placed"
    answer: 2
    explain: "Accuracy traced a U shape: best when the answer was near the start or end, worst in the middle. A flat line would have meant the models used the whole context equally well, which is what they did not find."
  - q: "What did Liu et al. find when they compared GPT-3.5-Turbo with the answer in the middle of 20 or 30 documents against the same model given no documents at all?"
    options:
      - "The documents always helped, by at least ten points"
      - "Accuracy with the answer in the middle could fall below the no-document, closed-book score of 56.1%"
      - "The model refused to answer without documents"
      - "Closed-book accuracy was close to zero"
    answer: 1
    explain: "With the answer around the middle, accuracy dropped to roughly 50.5% to 53.8%, below the 56.1% the model scored from memory alone. So adding the right document in the wrong place could leave the model worse off than giving it nothing."
  - q: "What did the 'Found in the Middle' paper (Hsieh, Chuang and colleagues, 2024) identify as a cause of the effect?"
    options:
      - "A U-shaped bias in attention, which favours the start and end of the input regardless of relevance"
      - "Training data that contained no long documents at all"
      - "A bug in how documents were tokenised"
      - "Models running out of memory in the middle of long inputs"
    answer: 0
    explain: "The authors linked the effect to models attending more to the beginning and end of the input whatever the content, and corrected for that bias to improve retrieval. They did not claim tokenisation bugs or memory limits."
  - q: "Which statement best fits the evidence described in the post?"
    options:
      - "The effect has been eliminated in all models released since 2024"
      - "Liu et al.'s result can be dismissed because they tested only one model"
      - "The original finding covered several models, and later work shows it can be reduced with training or calibration, but most mitigation results are preprints on particular models and tasks"
      - "RULER showed that models handle 32K tokens equally well whatever the task"
    answer: 2
    explain: "The 'only one model' objection sounds sceptical but is false: Liu et al. tested several open and closed models, including MPT-30B-Instruct, LongChat-13B, GPT-3.5-Turbo and Claude-1.3. The real caveat is that fixes like IN2 training and attention calibration are tested on specific models, and RULER found only about half of models held up at 32K."
reflect:
  - "If you were building a system that feeds retrieved documents to a model, how would you test whether the order of those documents matters for your model and your questions, rather than relying on published curves?"
  - "Benchmarks like needle-in-a-haystack test retrieval of one planted fact. What kinds of real tasks might still go wrong even when a model passes such tests perfectly?"
---

## The idea

Modern language models can accept very long inputs, from tens of thousands to hundreds of thousands of tokens. Accepting text is not the same as using it well. In a paper first posted in 2023 and published in *Transactions of the Association for Computational Linguistics* in 2024, Nelson Liu and colleagues tested how well models find a relevant piece of information depending on where it sits in the input.

They used two tasks. In multi-document question answering, the model gets a question and 10, 20 or 30 documents, exactly one of which contains the answer; the researchers moved that document from first to last. In key-value retrieval, the model gets a long list of random keys and values and must return the value for one key. Across models including MPT-30B-Instruct, LongChat-13B, GPT-3.5-Turbo and Claude-1.3, performance was usually best when the relevant information was at the start or end and significantly worse when it was in the middle, even for versions built for long contexts. Plotted against position, accuracy formed a U shape.

A concrete example: GPT-3.5-Turbo, asked the questions with no documents, scored 56.1%. With 20 documents and the answer at position 9, near the middle, it scored 53.8%; with 30 documents and the answer at position 9 or 14, about 50.5% to 50.9%. In those positions, supplying the right document did worse than supplying none.

## Why it might change a decision

The finding predicts that, for a model with this bias, the order of material in a prompt changes the answer even when the content is identical. In a retrieval system that hands a model a ranked list of documents, the paper's case study also found that reader accuracy levelled off well before the retriever stopped finding more relevant documents: going from 20 to 50 retrieved documents improved GPT-3.5-Turbo by only about 1.5 points and Claude-1.3 by about 1. Whether it pays to retrieve more, or where to place the most important passage, is therefore something that can be measured for a given model rather than assumed.

## How solid is this?

The original result comes from controlled benchmark experiments, not real user tasks, but it covered several open and closed models of the time and two different tasks. Some details were less uniform: an encoder-decoder model, Flan-UL2, was fairly robust to position when inputs stayed within its training length, and the U shape appeared only beyond it.

Later work broadly confirms the effect and suggests it can be reduced. Cheng-Yu Hsieh, Yung-Sung Chuang and colleagues linked it to a built-in U-shaped attention bias: models attend more to the beginning and end of the input regardless of relevance. Calibrating that bias improved retrieval-augmented generation by up to 15 percentage points over existing methods. Shengnan An and colleagues argued the cause is training that never teaches a model that crucial information can be anywhere. Their synthetic training data produced FILM-7B, a version of Mistral-7B that retrieved reliably across its 32K window in probing tasks. Both are preprints, each tested on particular models.

A broader benchmark, RULER, by Cheng-Ping Hsieh and colleagues, is a reminder that simple retrieval tests flatter models. Testing 17 long-context models on 13 tasks, they found most did well on basic needle-in-a-haystack retrieval but declined sharply on harder tasks as inputs grew. Almost all claimed context sizes of at least 32K tokens, yet only about half kept satisfactory performance at 32K. RULER measures length more than position, so it does not show directly whether the middle is still the weak spot.

The fair summary is that the positional effect is real and well replicated for the models Liu et al. tested; that it can be reduced; and that how much of it remains in the newest commercial models has not been established by the sources here. Claims that it is solved, or that it applies equally to every model, both outrun the evidence.

## Sources

- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics*, 12, 157-173. [doi:10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638) (preprint: [arXiv:2307.03172](https://arxiv.org/abs/2307.03172))
- Hsieh, C.-Y., Chuang, Y.-S., Li, C.-L., Wang, Z., Le, L. T., Kumar, A., Glass, J., Ratner, A., Lee, C.-Y., Krishna, R., & Pfister, T. (2024). Found in the middle: Calibrating positional attention bias improves long context utilization. arXiv preprint. [arXiv:2406.16008](https://arxiv.org/abs/2406.16008)
- An, S., Ma, Z., Lin, Z., Zheng, N., & Lou, J.-G. (2024). Make your LLM fully utilize the context. arXiv preprint. [arXiv:2404.16811](https://arxiv.org/abs/2404.16811)
- Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh, D., Jia, F., Zhang, Y., & Ginsburg, B. (2024). RULER: What's the real context size of your long-context language models? arXiv preprint. [arXiv:2404.06654](https://arxiv.org/abs/2404.06654)
