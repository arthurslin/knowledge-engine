---
title: "Why studying hospital patients can make two unrelated diseases look linked"
date: 2026-11-19
topics: [statistics, medicine, research methods]
summary: "In 1946 the statistician Joseph Berkson showed that if two conditions each make hospital admission more likely, a sample of inpatients can show a link between them that does not exist outside the hospital. The same trap, now called collider bias, turns up wherever a sample is chosen by the very things being compared."
status: published
quiz:
  - q: "What is the core mechanism behind Berkson's bias?"
    options:
      - "Hospitals keep worse records than general practices, so diagnoses are noisier"
      - "A sample is selected through a gate that both conditions make easier to pass, so the selected group misrepresents how the conditions go together"
      - "Sicker patients are more likely to lie on questionnaires"
      - "Two diseases that share a cause will always look linked"
    answer: 1
    explain: "The distortion comes from selection: admission depends on both conditions, so looking only at the admitted changes the pattern between them. A shared cause is a different problem, confounding, and can create a real-population association; Berkson's point is that a link can appear even when none exists in the population."
  - q: "In the comparison summarised by the Catalogue of Bias, what was the relative odds of locomotor disease among people with respiratory disease?"
    options:
      - "About 4 in the hospital sample and about 1 in the general population"
      - "About 1 in the hospital sample and about 4 in the general population"
      - "About 4 in both samples"
      - "Below 1 in both samples"
    answer: 0
    explain: "The hospitalised subsample gave relative odds of 4.06, while the random population sample gave 1.06, close to no association at all. The spurious link appeared only after selecting people who had been admitted."
  - q: "How does the birth weight paradox fit the same pattern?"
    options:
      - "Smoking protects babies who are born small"
      - "Low birth weight is caused only by smoking"
      - "Comparing only low birth weight babies selects on something smoking affects and that also shares causes, such as birth defects, with infant death"
      - "Smoking mothers are more likely to give birth in better hospitals"
    answer: 2
    explain: "Hernández-Díaz and colleagues argue that restricting the comparison to small babies conditions on birth weight. Among small babies of non-smokers, other, more lethal causes of low weight are more common, which can make the smokers' babies look better off without smoking being protective."
  - q: "Which statement best describes the empirical evidence for Berkson's bias?"
    options:
      - "It has never been observed in real data; it exists only as a mathematical possibility"
      - "It is a proven, large effect that invalidates every hospital-based study"
      - "The logic is a mathematical consequence of selection, and real data show it can occur, but a 1978 test found its predictive accuracy for how much a given association shifts was weak, though statistically significant"
      - "It was disproved when researchers switched to population controls"
    answer: 2
    explain: "The sceptical-sounding first option is wrong: Roberts and colleagues tested it on household survey data and found measurable shifts between community and hospital samples. The overconfident second option is also wrong; they described the theory's predictive validity as relatively weak. How large the bias is depends on the admission rates in a particular setting."
reflect:
  - "Think of a claim you have heard that rests on a selected group, such as people who were hired, admitted, published or famous. Would both of the things being compared have helped someone get selected?"
  - "If you only had hospital data, what extra information would you need to judge whether an association you found there is likely to hold in the wider population?"
---

## The idea

In 1946 the statistician Joseph Berkson published a short paper with a dry title about fourfold tables in hospital data. Its argument was that hospital patients are a poor place to look for links between diseases, even when the diagnoses are perfectly accurate.

The reason is the gate people pass through to be in the sample. If having condition A makes someone more likely to be admitted, and having condition B does too, then the inpatient population is not a fair slice of the public. People with both conditions have two separate routes in. Depending on the admission rates for each condition, the hospital sample can show an association between A and B that is absent, weaker or reversed in the population at large. Berkson's own illustration involved gallbladder disease and diabetes.

A simple thought experiment shows the logic. Suppose a programme admits anyone who is either very good at maths or very good at music, and the two skills are unrelated in the population. Inside the programme, a student who is weak at maths was almost certainly admitted for music, so the two skills will look negatively related among the admitted, even though nothing connects them outside. The selection created the pattern.

Epidemiologists now call this Berkson's bias, or admission rate bias, and treat it as one example of collider bias: when a variable is affected by two others, restricting or adjusting for it can manufacture a link between them.

A concrete case comes from data summarised by the Catalogue of Bias from David Sackett's 1979 review. Comparing a random sample of the general population with the subset who had been in hospital in the previous six months, the relative odds of locomotor disease among people with respiratory disease was 4.06 in the hospital group and 1.06 in the population. Outside the hospital the two were essentially unrelated.

## Why it might change a decision

The idea produces a specific, testable prediction: when both variables in a comparison influence who ends up in a sample, the association inside that sample should differ from the association in a sample drawn without that filter. That gives a researcher or reader something concrete to check, rather than a vague worry. One practical response in medical research is to draw controls from the general population rather than from other hospital patients, and the Catalogue of Bias lists this alongside using newly diagnosed cases and excluding patients admitted for other diseases.

The same structure shows up well outside hospitals. Hernández-Díaz, Wilcox, Schisterman and Hernán used causal diagrams to explain the long-standing birth weight paradox: among low birth weight babies, those whose mothers smoked appear to die less often than those whose mothers did not. Their argument is that comparing only small babies conditions on birth weight, which smoking affects and which shares causes such as congenital abnormalities with infant death. Among small babies of non-smokers, those other, deadlier causes are more common, so smoking can look protective without being so.

## How solid is this?

The core claim is a mathematical consequence of selection, not a finding from a single experiment, so the question is less whether it can happen than how big it is in real data.

The most direct test is a 1978 study by R. S. Roberts, W. O. Spitzer, T. Delmore and D. L. Sackett. They used a household survey of health care use covering eight broad clinical conditions and six medications, looked at every pairwise association in the whole sample and in the hospitalised subgroup, and found statistically significant shifts in relative risk. But they described Berkson's theory as having "relatively weak yet statistically significant predictive validity" for those shifts. In other words, the bias is real, but predicting its size and direction for a particular pair of conditions is hard, because it depends on admission rates that are rarely known.

Later hospital studies, such as a 2016 analysis of malaria and salmonella infection by Krumkamp and colleagues, have shown how much an estimate can move depending on which control group is used, which supports the general concern without pinning down a typical size.

The strongest competing explanation for any particular hospital-based association is that it is real: some diseases do cluster, through shared causes or one causing the other. Berkson's bias does not mean every inpatient finding is spurious; it means the inpatient sample alone cannot tell the two apart.

Popular writing often uses Berkson's paradox to explain everyday impressions, such as the idea that attractive people one dates tend to be unkind. These are tidy illustrations of the logic, but they are usually offered without data showing that selection, rather than a real pattern, explains them.

## Sources

- Berkson J. (1946). Limitations of the application of fourfold table analysis to hospital data. *Biometrics Bulletin* (now *Biometrics*), 2(3), 47-53. [PubMed 21001024](https://pubmed.ncbi.nlm.nih.gov/21001024/)
- Roberts RS, Spitzer WO, Delmore T, Sackett DL. (1978). An empirical demonstration of Berkson's bias. *Journal of Chronic Diseases* (now *Journal of Clinical Epidemiology*), 31(2), 119-128. doi:10.1016/0021-9681(78)90097-8. [McMaster Experts record](https://experts.mcmaster.ca/scholarly-works/842318)
- Hernández-Díaz S, Wilcox AJ, Schisterman EF, Hernán MA. (2008). From causal diagrams to birth weight-specific curves of infant mortality. *European Journal of Epidemiology*, 23(3), 163-166. doi:10.1007/s10654-007-9220-4. [PMC2722961](https://pmc.ncbi.nlm.nih.gov/articles/PMC2722961/)
- Catalogue of Bias Collaboration: Spencer EA, Aronson JK, Nunan D, Heneghan C. (2018). Berkson's bias (admission rate bias). Catalogue of Bias, Centre for Evidence-Based Medicine, Oxford. Source of the Sackett (1979) figures and the Krumkamp et al. (2016) example. [catalogofbias.org](https://catalogofbias.org/biases/admission-rate-bias/)
