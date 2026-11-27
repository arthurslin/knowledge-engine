---
title: "Does a big neural network hide a small one that could do the same job? The lottery ticket hypothesis"
date: 2026-11-27
topics: [AI, machine learning]
summary: "In 2018 two MIT researchers found that small subnetworks, pruned from a trained network and reset to their starting values, could train to the full network's accuracy. Later work showed the original recipe breaks down at larger scale and needs a small fix, and one group argued the 'winning' starting values matter less than claimed."
status: published
quiz:
  - q: "In Frankle and Carbin's procedure, what happens to the weights that survive pruning before the subnetwork is trained again?"
    options:
      - "They keep the values they reached at the end of training"
      - "They are reset to the exact values they had when the original network was first initialized"
      - "They are replaced with fresh random values"
      - "They are all set to the same small constant"
    answer: 1
    explain: "The defining step is resetting survivors to their original starting values. Fresh random values (the third option) is the control condition: when the authors did that, the advantage disappeared, which is why they concluded the particular starting values mattered."
  - q: "On the small networks tested for MNIST and CIFAR10, how large were the winning tickets the 2019 paper reported finding consistently?"
    options:
      - "About half the size of the original network"
      - "Less than 10 to 20 percent of the original network's size"
      - "Under 1 percent of the original network's size"
      - "Exactly the same size, but with different starting values"
    answer: 1
    explain: "The abstract reports winning tickets less than 10 to 20 percent of the original size. Some tickets that kept fewer weights still worked in particular experiments, but 'under 1 percent' overstates what the paper claims consistently."
  - q: "What change did Frankle, Dziugaite, Roy and Carbin need to make the method work for ResNet-50 on ImageNet?"
    options:
      - "Rewind the surviving weights to their values from early in training, rather than to the very start"
      - "Train the pruned network for ten times longer"
      - "Prune all the weights in a single step instead of in rounds"
      - "Use a smaller dataset"
    answer: 0
    explain: "At ImageNet scale, rewinding to the very start produced subnetworks no better than random restarts. Rewinding to a point a few percent of the way through training, epoch 5 of about 90 for ResNet-50, produced subnetworks that matched the full network."
  - q: "A reader says: 'Liu and colleagues showed winning tickets are a myth, so the whole idea was debunked.' How well does that fit the evidence described?"
    options:
      - "It fits: Liu and colleagues found winning tickets cannot be found in any network"
      - "It fits: the original paper was never replicated by anyone"
      - "It overstates things: Liu and colleagues found the special starting values gave no advantage when a larger learning rate was used, while the original authors later reproduced matching subnetworks at large scale with a modified recipe"
      - "It is backwards: Liu and colleagues found the winning-ticket starting values were essential in every setting"
    answer: 2
    explain: "The 'debunked' reading sounds like healthy scepticism but misstates both papers. Liu and colleagues disputed one ingredient, the value of the exact starting values, under particular training settings. The rewinding paper reproduced matching sparse subnetworks on ImageNet. The fair summary is that the hypothesis survives in a modified form, with real disagreement about how much the original values matter."
reflect:
  - "If small subnetworks can match a large network's accuracy, why do researchers keep training the large network at all? What would you need to know in advance to skip it?"
  - "The hypothesis was stated for 'dense, randomly initialized' networks of a few kinds. What would you want to see tested before believing it applies to today's very large language models?"
---

## The idea

Modern neural networks are usually far larger than they seem to need to be. After training, researchers can often delete most of a network's connections, a step called pruning, and keep nearly all of its accuracy. That raises an obvious question. If the small network works so well, why not train the small one from the start? In practice, people who tried found that small networks trained from scratch did worse.

Jonathan Frankle and Michael Carbin at MIT proposed an explanation in a paper first posted in 2018 and presented at ICLR in 2019. Their lottery ticket hypothesis says that a large, randomly initialized network contains a subnetwork that, trained on its own from the same starting values, can reach the full network's test accuracy in no more training steps. The large network works, on this view, because it holds many such draws, and training finds one that happened to start in a good place.

Their test was concrete. Train a network, delete the weights with the smallest magnitude (about 20 percent per round for one small network), then reset every surviving weight to the exact value it had at initialization, and train again. Repeat. On fully connected and convolutional networks for the MNIST and CIFAR10 image datasets, they consistently found these "winning tickets" at less than 10 to 20 percent of the original size. Some trained faster than the full network and reached higher test accuracy.

The key control was to keep the same pruned wiring but give it fresh random starting values. Those versions trained more slowly and lost accuracy much sooner as pruning went on. The authors read this as evidence that the specific starting values, not just the wiring, made the ticket win.

## Why it might change a decision

The hypothesis predicts something checkable for anyone training networks of the kinds tested: a pruned subnetwork reset to its original starting values should beat the same subnetwork with new random values, and the gap should grow as more weights are removed. Later work adds a second prediction for large networks: resetting to values from slightly into training, rather than the very start, should be needed. If neither holds in a given setup, the cheaper choice is to prune and fine-tune, or simply train the smaller architecture from scratch.

## How solid is this?

The original results come from controlled experiments on small networks and small image datasets. The paper itself flagged that the method was fragile in deeper networks: for VGG and ResNet models it was sensitive to the learning rate and needed a warm-up period to find tickets at higher rates.

A competing explanation arrived almost at once. Zhuang Liu, Trevor Darrell and colleagues, studying several pruning methods, argued that what matters after pruning is mostly the shape of the smaller network, not the inherited weights. They also retested the lottery ticket setup and reported that with the best learning rate, the winning-ticket starting values gave no improvement over random ones. The advantage appeared only at a small learning rate, which produced lower accuracy overall. This is the strongest challenge to the hypothesis's central claim about initial values, though it is one group's experiments on particular architectures.

Frankle and Carbin, with Gintare Karolina Dziugaite and Daniel Roy, then tested larger settings in an ICML 2020 paper. On ImageNet, resetting to the very start did not work: pruned ResNet-50 reached 73.7 percent accuracy against 76.1 for the full network, barely above the 73.4 percent of randomly restarted subnetworks. But rewinding to values from early in training, epoch 5 for ResNet-50 and epoch 6 for Inception-v3, produced subnetworks that matched the full network. They linked this to the point at which training becomes stable, when two copies trained with different random data orderings end up in the same basin of solutions.

So the popular version, "every big network contains a small one you could have trained instead", outruns the data. The supported version is narrower: sparse subnetworks that train to full accuracy exist in many tested networks, but finding them requires training the full network first, and at scale they start from early training values rather than true initialization. How far this extends to very large language models is not settled by these papers.

## Sources

- Frankle, J. and Carbin, M. (2019). "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks." International Conference on Learning Representations (ICLR 2019); first posted to arXiv in 2018. https://arxiv.org/abs/1803.03635
- Liu, Z., Sun, M., Zhou, T., Huang, G. and Darrell, T. (2018, revised 2019). "Rethinking the Value of Network Pruning." arXiv preprint 1810.05270. https://arxiv.org/abs/1810.05270v2
- Frankle, J., Dziugaite, G. K., Roy, D. and Carbin, M. (2020). "Linear Mode Connectivity and the Lottery Ticket Hypothesis." Proceedings of the 37th International Conference on Machine Learning, PMLR 119:3259-3269. https://proceedings.mlr.press/v119/frankle20a.html
