---
title: "Why making a model bigger can make it worse, then better again"
date: 2026-11-02
topics: [AI, machine learning, statistics]
summary: "Classical statistics says test error should rise once a model is flexible enough to memorise its training data. Experiments since 2018 show a second fall in error beyond that point, called double descent; the pattern is well documented, but how much it matters in practice is still argued over."
status: published
quiz:
  - q: "Where does the peak in test error sit on a double descent curve?"
    options:
      - "At the smallest model that was tried"
      - "Near the interpolation threshold, where the model has just enough capacity to fit the training data exactly"
      - "At the largest model that was tried"
      - "Wherever training was stopped earliest"
    answer: 1
    explain: "Belkin and colleagues found error peaked where random features roughly equalled training examples, the point at which the model can first fit every example. The largest models were among the best, not the worst, which is the whole surprise."
  - q: "What explanation did Belkin and colleagues offer for the second descent?"
    options:
      - "Bigger models see more data"
      - "Past the threshold many models fit the data perfectly, and the training method tends to pick the smoothest one, which generalises better"
      - "Bigger models are trained for longer"
      - "Label noise disappears in larger models"
    answer: 1
    explain: "Once many functions fit the training set exactly, the inductive bias of the method decides which one you get. For random features they showed the method finds the minimum-norm fit, whose size shrinks as capacity grows. For neural networks the same story is offered as a conjecture."
  - q: "In the 2019 deep learning experiments by Nakkiran and colleagues, what made the error peak most pronounced?"
    options:
      - "Using very large datasets"
      - "Adding label noise, such as 15 or 20 percent of training labels deliberately wrong"
      - "Using transformers instead of image models"
      - "Turning off random initialisation"
    answer: 1
    explain: "The peaks were strongest with label noise. Some appeared without it, for example on CIFAR-100 and a translation task, but noiseless CIFAR-10 showed more of a plateau."
  - q: "A reader says: 'Double descent is probably a one-lab artefact that nobody has reproduced.' How well does this fit the evidence in the post?"
    options:
      - "It fits: only one paper has reported the curve"
      - "It fits: the effect only appears in simulations, never on real data"
      - "It does not fit: the curve has been reported by separate groups across random features, forests, ResNets and transformers, and similar peaks were described for linear models around 1989 to 2000"
      - "It does not fit, because the curve has been proved to appear in every model"
    answer: 2
    explain: "The existence of the curve is one of the better-replicated findings in the area, with independent reports from several groups and decades-old precedents found by Loog and colleagues. The live disputes are about mechanism and practical relevance, not existence. Nor has it been proved universal: some methods, such as the perceptron of optimal stability, show no peak."
reflect:
  - "If tuned regularisation or early stopping often hides the peak, in what situations would a practitioner still want to know where the interpolation threshold is?"
  - "The textbook U-shaped curve was taught for decades while counterexamples sat in older papers. What features of a research field make an inconvenient finding easy to overlook?"
---

## The idea

For most of the twentieth century, statistics students learned one picture of model complexity. A model that is too simple misses real patterns. A model that is too flexible starts fitting the noise in its particular sample, and its error on new data climbs. Plot test error against model size and you get a U: the best model sits somewhere in the middle. This is the bias-variance trade-off, and it is why overfitting is treated as the main danger of a large model.

Modern neural networks seemed to break the rule. They often have far more adjustable numbers than training examples, can fit their training sets perfectly, and still predict new data well. In a 2019 paper in PNAS, Mikhail Belkin, Daniel Hsu, Siyuan Ma and Soumik Mandal proposed a single curve covering both regimes. Test error first follows the familiar U. It peaks near the interpolation threshold, the point where the model has just barely enough capacity to fit every training example. Then, as capacity keeps growing, error falls again, sometimes below the bottom of the original U. They called this double descent.

A concrete example from their paper: they fitted models built from random features to 10,000 handwritten digits from the MNIST dataset. As the number of features approached 10,000, test error rose sharply; the model at exactly that size was among the worst. With many more features than examples, error dropped and ended up lower than any classical model in the sweep. They saw a similar shape in two-layer neural networks and in random forests.

Their proposed mechanism is about choice. Below the threshold there is roughly one best fit. Just at the threshold there is exactly one fit that passes through every point, and it has to contort itself to do so. Past the threshold there are many perfect fits, and the training procedure tends to land on the smoothest one, the minimum-norm solution. More capacity offers smoother options.

In December 2019 Preetum Nakkiran and five co-authors, including Ilya Sutskever, reported the same pattern in deep networks: ResNets and simpler convolutional networks on the CIFAR image datasets, and transformers on translation. They added two twists. Error could also rise and fall again over training time for a large model, and in a band of model sizes, more training data made results worse. In one translation setting, 18,000 examples gave higher test loss than 4,000.

## Why it might change a decision

The finding bears on a specific practical move: increasing model size in small steps and stopping when validation error rises. Under the classical picture, a rising error means you have passed the sweet spot. Under double descent, a rise near the threshold can be a temporary bump, and a much larger model could do better. The testable behaviour is this: before concluding a model is too big, check whether the size at which error peaked is close to the size at which training error first reached zero. If it is, the classical reading may be wrong for that problem.

## How solid is this?

The existence of the curve is well supported. It has been reported by separate groups across several model families and datasets, and these are controlled experiments in which model size is varied directly, not observational studies. In 2020 Marco Loog and colleagues published a letter in PNAS showing the phenomenon was not new: peaks of this kind were described for linear regression in 1989 and 1990 and for a linear classifier in the late 1990s. Effect size varies a great deal, so there is no single number to report.

Three qualifications matter. First, the peak is often weak or absent on clean data. Nakkiran's team found the sharpest peaks with deliberately corrupted labels, and both papers note that early stopping or other regularisation can hide it. Second, the explanation is less settled than the observation. The minimum-norm account is proven for simple models, but for deep networks both papers call it a conjecture. Third, it is not universal. Loog and colleagues point to methods that show no peak at all.

The strongest competing reading is that double descent says more about untuned training than about large models. If careful regularisation often removes the bump, the classical intuition may still guide most decisions, and the popular phrase "bigger is always better" outruns the data. What the evidence does support is narrower: perfect fit to training data is not, by itself, a reliable sign that a model will do badly on new data.

## Sources

- Belkin, M., Hsu, D., Ma, S. & Mandal, S. (2019). Reconciling modern machine-learning practice and the classical bias-variance trade-off. *Proceedings of the National Academy of Sciences*, 116(32), 15849-15854. [doi:10.1073/pnas.1903070116](https://doi.org/10.1073/pnas.1903070116); preprint [arXiv:1812.11118](https://arxiv.org/abs/1812.11118v2)
- Nakkiran, P., Kaplun, G., Bansal, Y., Yang, T., Barak, B. & Sutskever, I. (2019). Deep double descent: where bigger models and more data hurt. arXiv preprint. [arXiv:1912.02292](https://arxiv.org/abs/1912.02292v1)
- Loog, M., Viering, T., Mey, A., Krijthe, J. H. & Tax, D. M. J. (2020). A brief prehistory of double descent. Letter, *Proceedings of the National Academy of Sciences*. [arXiv:2004.04328](https://arxiv.org/pdf/2004.04328)
