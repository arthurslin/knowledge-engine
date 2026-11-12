---
title: "Did resonance really bring down the Tacoma Narrows Bridge?"
date: 2026-11-12
topics: [engineering, physics]
summary: "Generations of physics textbooks used the 1940 collapse of the Tacoma Narrows Bridge as the classic case of resonance. Physicists and engineers who looked closely argue it was something different: a steady wind feeding a twisting motion that the bridge itself kept alive."
status: published
quiz:
  - q: "Why do Green and Unruh argue that the familiar vortex-resonance story cannot explain the collapse?"
    options:
      - "The wind that day was far too weak to shed any vortices"
      - "The vortex shedding frequency expected for a 42 mph wind was about 1 Hz, far from the bridge's twisting frequency of about 0.2 Hz"
      - "The bridge had no natural frequencies at all, because it was a suspension bridge"
      - "Vortices only form behind trusses, and the bridge had none"
    answer: 1
    explain: "Forced resonance needs a push at the structure's own frequency. Green and Unruh calculate that the vortices shed by a 42 mph wind would arrive about five times too often. The first option is wrong: the wind was a gale of roughly 40 mph, and the issue is the frequency, not the absence of vortices."
  - q: "According to the account in Olson, Wolf and Hook (2015), what happened shortly after 10 a.m. on 7 November 1940?"
    options:
      - "The centre span fell into the water"
      - "The bridge stopped moving as the wind dropped"
      - "The motion changed suddenly from mainly up-and-down to twisting"
      - "The bridge was opened to traffic for the first time"
    answer: 2
    explain: "The bridge had been rippling vertically; a few minutes after 10 o'clock the professor watching it, F. B. Farquharson, saw a sudden switch to torsional motion. The first large section of roadway broke loose at 11:02 a.m., about an hour later."
  - q: "What is the key difference between forced resonance and self-excitation as described in the post?"
    options:
      - "Resonance needs a periodic push at the right frequency; self-excitation can draw energy from a steady flow because the motion itself shapes the forces"
      - "Resonance only happens in metal structures; self-excitation only happens in concrete"
      - "Self-excitation is just resonance at a lower wind speed"
      - "Resonance is caused by earthquakes; self-excitation is caused by wind"
    answer: 0
    explain: "In forced resonance an outside rhythm drives the structure. In self-excitation, as with a bowed violin string, a steady input is turned into oscillation through feedback: the moving deck changes the airflow so that the wind pushes it further in the direction it is already moving."
  - q: "A reader says: 'Since engineers still argue about the details, the textbook resonance story is as good as any other explanation.' Which response fits the evidence best?"
    options:
      - "Agree: with no consensus on details, all explanations are equally supported"
      - "Agree: the official 1941 report concluded it was vortex resonance"
      - "Disagree: the frequency mismatch and the way amplitude grew with wind speed count against simple forced resonance, even though the exact aerodynamic mechanism is still debated"
      - "Disagree: the cause is fully settled and no expert disagrees about anything"
    answer: 2
    explain: "Treating a live debate as a tie sounds open-minded, but it ignores specific evidence. The remaining disagreement is about which self-excited mechanism dominated and how vortices contributed, not about whether a periodic push at the bridge's frequency did it. The last option overcorrects: the Washington State DOT history notes that experts still disagree on details."
reflect:
  - "A classic example can survive in textbooks for decades after specialists stop believing it. What other teaching examples might be like this, and how would you check one?"
  - "Green and Unruh compare the bridge to a bowed violin string. Where else might a steady input produce a growing oscillation through feedback, and what would you measure to tell it apart from resonance?"
---

## The idea

On 7 November 1940, four months after it opened, the Tacoma Narrows Bridge in Washington State twisted itself apart in a gale. Film of the deck heaving and corkscrewing became one of the most famous pieces of footage in engineering, and for decades physics textbooks used it to illustrate resonance: a periodic push, timed to match a structure's natural frequency, builds up a large oscillation. In the early 1960s, the widely used textbooks by Halliday and Resnick said the wind had produced a fluctuating force in resonance with a natural frequency of the bridge.

Physicists and engineers who later went back to the evidence mostly rejected that story. Their alternative is self-excitation, which engineers call aeroelastic flutter. A steady wind does not have a rhythm of its own. But once the deck starts to twist, its motion changes how air flows around it, and if that change makes the wind push the deck further the way it is already moving, energy flows in on every cycle. Physicists describe this as negative damping: instead of friction draining the motion away, the surroundings feed it.

The two accounts make different predictions, and the bridge's own numbers are the concrete example. The common resonance version blamed vortex shedding, the alternating swirls that peel off a blunt object in a wind. In a 2004 preprint, the University of British Columbia physicists Daniel Green and William Unruh estimated that a wind of about 42 mph would shed vortices from the deck at roughly 1 Hz. The deck's fatal twisting ran at about 0.2 Hz. A push arriving five times too often is not a resonant push.

## Why it might change a decision

The distinction is not just a matter of labels; it changes what an engineer would do. If a structure is being driven at resonance, a natural fix is to detune it: change its stiffness or mass so that its natural frequency moves away from the driving rhythm. If it is self-excited, detuning does little, because the wind adapts to the motion rather than imposing a rhythm. The remedy is aerodynamic or torsional: a deck shape that does not feed the motion, or a much stiffer structure. WSDOT's history says the Tacoma deck was stiffened only by an 8-foot solid plate girder, too shallow for its span, where an earlier proposed design had called for a 25-foot-deep stiffening truss.

The testable behaviour is how motion grows with wind speed. Under forced resonance, amplitude should peak near one wind speed, where the driving frequency matches, and fall away on either side. Under flutter, motion should be small below a threshold speed and then grow as the wind strengthens. Olson, Wolf and Hook report that the bridge's twisting amplitude increased steadily with wind speed rather than peaking, which is the second pattern.

## How solid is this?

This is a historical case analysis, not an experiment, so it rests on eyewitness measurements, film and physical reasoning rather than a controlled test. The best records come from F. B. Farquharson, an engineering professor who was watching the bridge that morning. As Olson and colleagues recount, the deck rippled up and down until a few minutes after 10 a.m., then switched suddenly to twisting. Farquharson timed the twisting at 12 cycles per minute, a period of five seconds. At 11:02 a.m. a 600-foot section of roadway broke loose, and about six minutes later almost all the remaining centre span fell. Green and Unruh put the twisting amplitude at about 13 feet at the deck edges.

One detail shows how a popular account can outrun its data. Olson and colleagues found that video copies of the famous film run too fast, making the twisting appear at 18 cycles per minute. They call that figure definitely wrong, too high by 50 percent.

The strongest competing view is not resonance in its textbook form but a mixed picture. The Washington State Department of Transportation's history notes that the 1941 board of engineers, Othmar Ammann, Theodore von Kármán and Glenn Woodruff, attributed the failure to random action of turbulent wind, and linked the switch to twisting with a cable band that slipped at midspan. WSDOT describes the primary cause as torsional flutter, with vortex shedding possibly contributing, and says experts still disagree about the exact mechanism. Green and Unruh argue that the vortices seen on film were produced by the bridge's motion, matching its frequency, rather than causing it. So the case against simple forced resonance is strong; the precise aerodynamics of the final hour are still argued over.

## Sources

- Olson, D. W., Wolf, S. F. & Hook, J. M. (2015). The Tacoma Narrows Bridge collapse. *Physics Today* 68(11), 64-65. [doi:10.1063/PT.3.2991](https://physicstoday.aip.org/article/68/11/64/414979)
- Green, D. & Unruh, W. G. (2004). Tacoma Bridge failure: a physical model. arXiv preprint physics/0408101. [arxiv.org/abs/physics/0408101](https://ar5iv.labs.arxiv.org/html/physics/0408101)
- Washington State Department of Transportation. Tacoma Narrows Bridge history: Lessons from failure. [wsdot.wa.gov](https://wsdot.wa.gov/TNBHistory/bridges-failure.htm)
- Ammann, O. H., von Kármán, T. & Woodruff, G. B. (1941). The Failure of the Tacoma Narrows Bridge. Report to the Federal Works Agency, 28 March 1941. [Caltech archive](https://authors.library.caltech.edu/records/q1ehq-5e206/preview/The_Failure_of_the_Tacoma_Narrows_Bridge.pdf) (title, authors and date confirmed from the scan; its findings are cited here via WSDOT's summary)
