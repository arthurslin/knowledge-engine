---
title: "Anthropic says Claude helped solve the first structure of a bacterial vault, but the data are not yet public"
date: 2026-11-10
topics: [AI news, AI, biology]
summary: "Anthropic's biology team reports a cryo-EM structure of a vault particle built from a bacteriophage protein, with Claude doing much of the search, lab planning and image processing under human direction. The structures, preprint data and any outside scientific assessment are still to come."
status: published
quiz:
  - q: "According to Anthropic's post, what is new about the vault particle the team describes?"
    options:
      - "It is the first vault particle ever imaged"
      - "It is the first 3D structure of a vault particle found in prokaryotic cells"
      - "It is the first vault whose biological function has been worked out"
      - "It is the first protein designed from scratch by an AI model"
    answer: 1
    explain: "Vaults were discovered in mammalian cells in 1986, and mammalian vault structures exist. The claim is about a vault from bacteria and phages. The post says plainly that the function of vaults is still unknown, and the protein was found in a database, not designed."
  - q: "How did the team describe Claude's role?"
    options:
      - "Claude ran the whole project autonomously with no human input"
      - "Claude only wrote the blog post"
      - "Claude searched the protein database, designed DNA constructs, suggested a purification method and ran cryo-EM processing, while the team directed it and made key choices"
      - "Claude predicted the structure without any laboratory experiment"
    answer: 2
    explain: "The post says the team directed Claude throughout, chose which proteins to test and did the wet-lab work. The structure comes from real cryo-EM images, not a prediction."
  - q: "Which of these did the post say went wrong along the way?"
    options:
      - "A protocol additive Claude suggested set the project back two weeks, and an early map was blended with its mirror image"
      - "Claude fabricated the final structure"
      - "The particle failed to assemble in E. coli"
      - "The team could not purify any protein"
    answer: 0
    explain: "Anthropic reports both setbacks itself. The particles did assemble in E. coli; what has not been tested is whether they form in their natural hosts."
  - q: "A reader says: 'Since no independent scientist has checked it yet, the structure should be assumed false.' Which response fits the evidence best?"
    options:
      - "Agree: company research is never accurate"
      - "Agree: Anthropic admits the structure is unreliable"
      - "Too strong: the claims are unverified until the preprint and data are public and others examine them, but that is a reason to withhold judgment, not evidence that the structure is wrong"
      - "Too weak: the structure has already been confirmed by the Protein Data Bank"
    answer: 2
    explain: "Unverified is not the same as false. Cryo-EM structures can be checked once maps and models are deposited, which Anthropic says will happen soon. No accession codes were given at the time of the post, so no database has confirmed anything yet."
reflect:
  - "The post describes Claude as working under close human direction. What would you want to see reported in future projects like this to tell how much of the work the model did versus the scientists?"
  - "Anthropic's only named outside adviser was a paid consultant. What kinds of outside review would make a company's scientific claims easier to trust, and which of them could happen before publication?"
---

## What happened

On 4 November 2026, Anthropic published a research post titled "Investigating vault particles with Claude." It reports what the company calls the first 3D structure of a vault particle found in prokaryotic cells, that is, in bacteria or the viruses that infect them. The contributors listed are Januka Athukoralage, Peter Yoon, Nicholas Perry, Matthew Durrant and Anthropic's Life Sciences Team. Leonard Rome, who co-discovered vaults in 1986, advised the project; the post discloses that he was a paid consultant who gave feedback on the manuscript.

Vaults are large, hollow protein shells found in most human cells. Their function is still unknown. The post describes the team using Claude to search a database of about 15 billion predicted proteins for relatives of the vault protein, finding hits in 29 bacterial and 4 archaeal phyla. The team picked candidates, and Claude converted each sequence into DNA designed for expression in E. coli. The team chose 44 candidate proteins; in the expression tests the post reports, 15 of 24 produced soluble protein and 7 formed vault-like particles; four were confirmed by cryo-electron microscopy.

The headline particle is built from 96 copies of a single protein from a bacteriophage, which the team calls L05. Anthropic says it weighs about 9.5 megadaltons, measures about 54 by 45 nanometres and encloses about a quarter more volume than a mammalian vault. Each copy holds an unidentified small molecule; Claude noted it resembles coenzyme A, but the team says it has not identified it.

Anthropic also reports process details. Claude suggested loading cell contents straight onto a size-exclusion column, which the post says cut purification from about three days to about 90 minutes. Working in an internal multi-agent setup, Claude installed and ran the open-source cryo-EM software RELION, while the scientists advised on analysis decisions. A first full model took 34 hours. The whole project took under four months.

## What is claimed vs. what is verified

Nearly everything above is Anthropic's own account. The company says a preprint has been submitted to bioRxiv and that it will release the structures and more data soon. At the time of the post, no Protein Data Bank or Electron Microscopy Data Bank accession codes were given, so outside researchers cannot yet inspect the maps or models. The post does not name the Claude model version used, and it does not state a resolution figure; one secondary site reports 3.2 ångströms, but that number does not appear in the post itself.

Independent coverage so far has repeated Anthropic's account rather than tested it. Interesting Engineering's report, published the same day, matches the post's figures and quotes no outside scientists; it also describes the result as the world's first bacterial vault, slightly broader than the post's wording, and does not mention that Dr. Rome was paid.

The post does report its own failures: a protocol additive Claude recommended set the project back two weeks, and an early processing run produced a map blended with its mirror image. Claude also initially argued against the chromatography approach that later worked.

## Why it matters

If the structure holds up, it is evidence that vault-forming proteins exist outside complex cells, which bears on how these shells evolved. It is also one of the more detailed public descriptions of a frontier AI model doing hands-on parts of an experimental biology project, from database search to image processing. The time figures, if typical, would matter for how labs plan structural work.

## Open questions and other views

The authors note that the particles have only been made in E. coli and that no one has yet checked whether they form in their natural bacterial and phage hosts. Their function remains open; Dr. Rome is quoted saying that working out what vaults do "is still enormously challenging."

Supporters of AI in science would point to the speed and to a fully disclosed list of the model's mistakes as a sign of a workable division of labour. Sceptics would note that the scientists chose the candidates and directed each step, so it is hard to separate Claude's contribution from expert guidance, and that the post comes from a company with a commercial interest in showing its model is useful for research. Structural biologists will be able to judge the work once maps and models are deposited. Until then, the result is a well-described claim rather than an independently checked one.

## Sources

- Anthropic, "Investigating vault particles with Claude," research post, 4 November 2026. https://www.anthropic.com/research/investigating-vault-particles-with-claude
- Aamir Khollam, "Anthropic maps world's first 3D vault built from 96 protein copies," Interesting Engineering, 4 November 2026. https://interestingengineering.com/ai-robotics/anthropic-first-3d-bacterial-vault-map
