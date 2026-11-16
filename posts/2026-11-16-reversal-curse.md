---
title: "Why a language model can know who Tom Cruise's mother is but not who her son is"
date: 2026-11-16
topics: [AI, machine learning]
summary: "Language models trained on a fact written one way, 'A is B', often cannot answer the same fact asked the other way round. Three research groups have reproduced this 'reversal curse'; the open question is how much it matters once facts appear in many phrasings."
status: published
quiz:
  - q: "In the fictitious-facts experiment by Berglund and colleagues, what happened when GPT-3 was fine-tuned on sentences like 'Daphne Barrington is the director of A Journey Through Time' and then asked the reverse question?"
    options:
      - "It answered correctly about half the time, roughly the same as the trained direction"
      - "It answered at close to 0 percent, and was no more likely to give the right name than a random one"
      - "It answered correctly only for the largest model size"
      - "It refused to answer"
    answer: 1
    explain: "Reverse accuracy was essentially zero (0.0 and 0.1 percent exact match for the 175-billion-parameter model), and the probability the model gave the correct name did not differ from a random name. The trained direction did work, which is why the first option is tempting: the failure is specific to the reversed direction."
  - q: "What happens, according to the same paper, if the fact 'A is B' is placed in the model's prompt and it is then asked 'Who is B?'"
    options:
      - "It fails in the same way, because the curse is a property of the model's architecture"
      - "It usually answers correctly, because the curse concerns facts learned in training, not facts supplied in context"
      - "It only succeeds if chain-of-thought prompting is used"
      - "The paper did not test this"
    answer: 1
    explain: "The authors note that models can deduce the reverse when the fact is in context. The failure is about how facts get stored during training, which is why the first option, though it sounds principled, is wrong."
  - q: "What did Golovneva and colleagues do to reduce the reversal curse?"
    options:
      - "They added a retrieval system that looks up facts in a database"
      - "They trained the model on each text both forwards and with its word or entity order reversed"
      - "They made the model larger"
      - "They removed celebrity names from the training data"
    answer: 1
    explain: "Reverse training feeds the model a reversed copy of each training string while keeping names intact. Making models larger is the tempting answer, but Berglund and colleagues found the failure persisted across model sizes."
  - q: "GPT-4 named Tom Cruise's mother 79 percent of the time but named Mary Lee Pfeiffer's son only about a third of the time. A reader concludes: 'This tells us nothing, because the paper is a single unreplicated preprint.' Is that a fair assessment?"
    options:
      - "Yes; preprints should be ignored until replicated"
      - "No; the core failure has been reproduced in at least two further studies by other researchers, though the celebrity numbers are confounded by how often each name appears in text"
      - "Yes; the effect disappears in all models released after 2023"
      - "No; the celebrity result proves models cannot reason in either direction"
    answer: 1
    explain: "The doubt in the first option sounds careful but is factually wrong: Allen-Zhu and Li, and Golovneva and colleagues (who share an author), found the same failure in controlled experiments. The fair caveat is narrower: in the celebrity test, the less famous parent appears in far fewer documents, so part of the gap may reflect frequency rather than direction alone."
reflect:
  - "Humans also find some memories easier to retrieve in one direction than the other. Is the reversal curse a sign that models store knowledge differently from people, or a sharper version of something people do too?"
  - "If you were building a tool that answers questions from a company's internal documents, how would you test whether it suffers from the reversal curse on your own data?"
---

## The idea

Ask a large language model "Who is Tom Cruise's mother?" and it will usually say Mary Lee Pfeiffer. Ask "Who is Mary Lee Pfeiffer's son?" and it often cannot say. In a 2023 paper, Lukas Berglund, Owain Evans and five co-authors called this the reversal curse: a model trained on a statement of the form "A is B" does not automatically learn "B is A".

Their celebrity test asked GPT-4 about 1,573 child and parent pairs. It identified the parent 79 percent of the time and the child about a third of the time. That gap alone is hard to interpret, because a famous person's name appears in far more text than their parent's. So the authors ran a cleaner experiment. They invented facts that appear nowhere online, such as "Daphne Barrington is the director of A Journey Through Time", and fine-tuned GPT-3 and Llama models on them.

The models learned the trained direction. Asked the reverse ("Who directed A Journey Through Time?"), the 175-billion-parameter GPT-3 scored 0.0 and 0.1 percent exact match on the two versions of the task. The probability it assigned to the correct name was no higher than for a random name. The failure held across model sizes and families. When the fact was placed directly in the prompt instead of in the training data, models could reverse it easily: what fails is the stored knowledge, not the ability to reason about a sentence in front of them.

A common explanation is the way these models are trained: they learn to predict the next token given the ones before it. Learning to continue "Daphne Barrington is" with "the director of..." adjusts what comes after Daphne's name. Nothing in that update requires the name to come out when the film is the starting point.

## Why it might change a decision

The finding suggests a check anyone can run. If you rely on a chatbot to recall a fact about a less-documented entity, a person, product, regulation or gene, ask the question in both directions. The prediction is that a model will more often answer correctly when you start from the entity that the source texts usually start from, and that giving it the relevant text in the prompt will close most of the gap. For anyone building a question-answering tool on their own documents, the same logic favours supplying the documents at question time over relying on fine-tuning alone to store facts, because facts learned in only one phrasing may be retrievable from only one side.

## How solid is this?

The core result is not a one-off. Berglund and colleagues' paper is a preprint (first posted September 2023, revised in 2024) built on controlled fine-tuning experiments, where the facts are invented so that no pre-existing text can leak the answer. Two further lines of work found the same thing with different designs.

Zeyuan Allen-Zhu and Yuanzhi Li trained models from scratch on synthetic biographies in their "Physics of Language Models: Part 3.2" paper, published at ICLR 2025. They report that "inverse knowledge search", such as recovering a person from one of their attributes, was "virtually 0%" regardless of how the question was prompted. Performance only improved when the training data itself presented the information in the reversed order.

Olga Golovneva, Allen-Zhu, Jason Weston and Sainbayar Sukhbaatar at Meta then tested a fix in a 2024 preprint. Their "reverse training" adds a reversed copy of each training text, keeping names intact. They report that this largely removes the failure on reversal tasks, and that compute-matched models did as well or better on standard benchmarks. That result comes from one group and has not, as far as the sources here show, been independently reproduced.

What is less settled is how much the curse matters in practice. The clean zero comes from facts seen in exactly one phrasing. Real training data often states famous facts many ways round, which is presumably why GPT-4 got some reverse questions right at all. The celebrity numbers also mix direction with frequency, since the 79 and 33 percent figures compare questions about famous names with questions about obscure ones; the paper's own figure reports 28 percent for the child direction, a reminder that the exact number depends on scoring choices. The strongest competing reading is therefore that the curse is a sharp effect under narrow conditions, and that its real-world size depends on how varied the text about a given fact is. None of the papers measures that directly for current commercial models, and newer models trained with different data or methods may behave differently.

## Sources

- Berglund, L., Tong, M., Kaufmann, M., Balesni, M., Stickland, A. C., Korbak, T. and Evans, O. (2023, revised 2024). "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'." arXiv preprint 2309.12288. https://arxiv.org/abs/2309.12288v4
- Allen-Zhu, Z. and Li, Y. (2025). "Physics of Language Models: Part 3.2, Knowledge Manipulation." International Conference on Learning Representations (ICLR 2025); first posted to arXiv in 2023. https://proceedings.iclr.cc/paper_files/paper/2025/hash/d5494c8747276d3cdb2598e5617de89d-Abstract-Conference.html
- Golovneva, O., Allen-Zhu, Z., Weston, J. and Sukhbaatar, S. (2024). "Reverse Training to Nurse the Reversal Curse." arXiv preprint 2403.13799. https://arxiv.org/abs/2403.13799v3
