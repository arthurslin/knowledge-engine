---
title: "DeepMind says AI agents proved security properties of Signal's compiled code: what the proofs cover"
date: 2026-11-12
topics: [AI news, AI]
summary: "On 10 November Google DeepMind said agents running Gemini wrote about 6.5 million lines of machine-checked proof that a compiled build of Signal's core library keeps messages secret. The paper is public and spells out its limits; nobody outside the project has yet reported rebuilding the proofs."
status: published
quiz:
  - q: "What exactly did DeepMind's proofs cover, according to the technical paper?"
    options:
      - "The Rust source code of every Signal app on iOS and Android"
      - "A compiled AArch64 Linux build of libsignal, run through a small command-line harness, for session setup, sending and receiving"
      - "Signal's group chats and multi-device syncing"
      - "Only the mathematical description of the protocol, with no code involved"
    answer: 1
    explain: "The paper targets the compiled machine code of libsignal v0.105.4 wrapped in a small harness, not the Rust source or the shipped apps. Group messaging, multi-device state and key generation are listed as outside the proofs. The last option describes earlier protocol-level analyses, which is what this work says it goes beyond."
  - q: "What did the reintroduced-bug experiment show?"
    options:
      - "The system found two new, previously unknown vulnerabilities in Signal"
      - "When two previously fixed bugs were put back into an isolated copy, the system proved that version insecure"
      - "The proofs still went through on the buggy code, revealing a flaw in the method"
      - "Signal engineers could not reproduce the bugs"
    answer: 1
    explain: "DeepMind restored two old, already-fixed bugs and the system produced machine-checked proofs that the buggy version violated the security properties. TNW, citing Wired, reports that no new flaws turned up in the parts that were checked, so the first option is wrong."
  - q: "Which of these is assumed rather than proved, according to the paper?"
    options:
      - "That the compiled program implements the protocol correctly"
      - "That the low-level cryptographic primitives behave as specified"
      - "That forward secrecy holds for the verified operations"
      - "That the reintroduced bugs break security"
    answer: 1
    explain: "The cryptographic building blocks are part of the trusted base and are assumed, along with the Lean kernel and a formal model of the AArch64 processor. That is why The Register calls the result theoretical. The other three are things the proofs establish."
  - q: "A reader says: 'The 6.5 million lines of proof were written by AI, so we have no reason to believe any of it.' Which response fits the evidence best?"
    options:
      - "Agree: AI-written proofs cannot be checked by anyone"
      - "Agree: DeepMind has not published anything beyond a blog post"
      - "Partly wrong: proofs in Lean are checked mechanically by a small kernel, and the artifacts are public; the open questions are whether the human-reviewed specifications state the right things and whether the trusted assumptions hold"
      - "Wrong in the other direction: the proofs mean Signal can no longer be broken in any way"
    answer: 2
    explain: "Doubting AI output sounds prudent, but a proof checker does not care who wrote the proof, and DeepMind released the artifacts and a long technical paper. The fair sceptical points are about what was specified and assumed, and the fact that no independent group has yet reported rebuilding the proofs. The last option ignores the paper's own exclusions, such as side channels and group chats."
reflect:
  - "If a proof shows a program meets its specification, but humans wrote the specification, where should a security reviewer now spend their time?"
  - "Google has not disclosed what the project cost. What would you want to know about cost before judging whether this approach could be used on ordinary software?"
---

## What happened

On 10 November 2026 Google DeepMind announced AlphaProof Code in a blog post by Pushmeet Kohli and Swarat Chaudhuri, alongside a technical paper with nine Google authors and a public release of the proof files. The target was libsignal, the open-source library that implements the Signal messaging protocol used by Signal and other apps.

According to the paper, the team compiled libsignal version 0.105.4, with a small command-line harness around the unmodified library, into a statically linked AArch64 Linux program. Agents then produced proofs in the Lean proof assistant, about 6.5 million lines in total, that this compiled machine code satisfies four security properties for one-to-one sessions: forward secrecy, post-compromise security, authentication and handshake secrecy. The verified operations are setting up a session, encrypting and decrypting. Key generation was not verified.

The blog says the proofs were written by agents running Gemini Carbon, and that specifications were drafted with a mix of models and reviewed by human experts. The paper describes campaigns of 40 to 80 agents on a single machine for 24 to 72 hours; the blog says the whole project took four weeks. As a check, the team reintroduced two previously fixed libsignal bugs into an isolated copy, and the system proved that version insecure.

## What is claimed vs. what is verified

The central result is unusually checkable. A Lean proof is accepted only if Lean's small kernel checks every step, so whoever or whatever wrote the proof matters less than for most AI output. DeepMind released the artifacts, which means outside researchers can rerun the checker. As of 12 November, none of the coverage reviewed for this post reports an independent group doing so. A detailed reading of the paper by developer Nikoloz Turazashvili on dev.to says plainly that he did not rebuild the proofs.

Several statements remain DeepMind's own. The company describes this as the first time the implementation of a widely deployed protocol has been formally verified by any method. The paper phrases it more narrowly, as the first proofs connecting protocol-level guarantees to unmodified code. The blog says human experts reviewed every specification and that only one percent of the codebase needed a second human look; those review figures have not been independently assessed. Google declined to share the project's cost, according to The Next Web, citing Wired.

What a reader should hold onto is what the proofs rest on. The paper lists a trusted base of about 26,000 lines: the theorem statements and definitions, plus a Lean model of 467 AArch64 instructions and 31 system calls that the team tested against other processor simulators. The cryptographic primitives themselves are assumed to work. The Register's Thomas Claburn calls the result theoretical for that reason. The paper also lists what is outside scope, including group messaging, multiple devices, side channels and quantum adversaries in the computational proof, and notes that its computational security bound becomes vacuous for many long sessions.

## Why it matters

Formal verification of real systems has historically been slow. The Register reports that the paper compares its four weeks with roughly 20 person-years for the seL4 operating system kernel and six years for the CompCert compiler. If agents can write the proofs while humans write and check the specifications, the bottleneck in verifying software moves from proof labour to specification review and compute. Proving properties of compiled machine code, rather than source, also means the compiler does not have to be trusted, since the paper says its proofs cover the compiled artifact rather than the Rust source or the compiler.

For Signal users, the practical meaning is narrower than the headlines. The verified artifact is a Linux build of the library through a test harness, not the phone apps, and The Next Web summarises the guarantees as covering one-to-one chats, not the Signal apps.

## Open questions and other views

Signal's chief technology officer, Ehren Kret, is quoted in DeepMind's blog calling the work a major breakthrough. That endorsement is not independent: the acknowledgments thank three Signal staff for feedback on the methodology.

Sceptics can point to the specifications. A proof shows that code meets a statement; if the statement misses an attack, the proof does not help. DeepMind's answer is human review of every specification, though the paper itself says such review is not expected to catch everything. Turazashvili also notes that checking a theorem's text is not enough when the definitions it relies on can change, a risk the project addresses with a separate comparison tool.

Others will ask about cost and generality. The Signal protocol already had well-studied security goals to write specifications from; it is unclear how the method would do on software whose intended behaviour is less clearly defined. Whether this becomes a product is also open: Google did not say, according to TNW's account of Wired's reporting.

## Sources

- Google DeepMind (Kohli, P. & Chaudhuri, S.), "Introducing AlphaProof Code", 10 November 2026. [deepmind.google](https://deepmind.google/blog/introducing-alphaproof-code/)
- Chaudhuri, S. et al., "AlphaProof Code: Verifying Signal's Security at the Machine-Code Level", technical paper and artifacts, Google DeepMind, 10 November 2026. [google-deepmind.github.io](https://google-deepmind.github.io/code-verification/)
- Claburn, T., "Google DeepMind melds humans and AI agents to vet Signal's secure messaging techniques", The Register, 10 November 2026. [theregister.com](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625)
- Constantin, A. M., "Google DeepMind's AI agents formally verify Signal's encryption code", The Next Web, 12 November 2026. [thenextweb.com](https://thenextweb.com/news/google-deepmind-alphaproof-code-signal-encryption-formal-verification)
- Turazashvili, N., "Google DeepMind's Signal proof: what AlphaProof Code checks", DEV Community, 10 November 2026. [dev.to](https://dev.to/axrisi/google-deepminds-signal-proof-what-alphaproof-code-checks-27l6)
