---
title: "Do most machines wear out? What airline data did to the bathtub curve"
date: 2026-11-23
topics: [engineering, statistics]
summary: "Engineers long assumed that parts fail young, settle down, then wear out, so regular overhauls should prevent failures. A 1978 United Airlines study found only a small share of aircraft items behaved that way, and that overhauls could add failures rather than remove them."
status: published
quiz:
  - q: "In Nowlan and Heap's United Airlines data, roughly what share of the items studied followed the classic bathtub curve (pattern A)?"
    options:
      - "About 89 percent"
      - "About 50 percent"
      - "About 4 percent"
      - "None at all"
    answer: 2
    explain: "Only 4 percent fell into pattern A. The 89 percent figure is the share with no wear-out zone at all (patterns D, E and F), which is the number most often quoted, so it is easy to mix the two up."
  - q: "Why did the report argue that scheduled overhaul could make reliability worse for some items?"
    options:
      - "Overhauls used cheaper replacement parts than the originals"
      - "An overhaul resets an item to the start of its life, where many items have a higher chance of failing soon after work is done"
      - "Mechanics doing overhauls had less training than line mechanics"
      - "Overhauls took aircraft out of service, so the remaining fleet flew harder"
    answer: 1
    explain: "Many items showed infant mortality, meaning a raised chance of failing just after manufacture or overhaul. Taking a stable item apart on a schedule puts it back into that risky early period, which is the mechanism the report describes."
  - q: "What did Backblaze's hard drive data show between 2013 and 2025?"
    options:
      - "Early failures fell sharply and the wear-out rise came much later, so the curve looked more like a hockey stick than a bathtub"
      - "The bathtub curve fitted every model of drive almost exactly"
      - "Drives became steadily less reliable at every age"
      - "Failure rates were constant at all ages, with no rise late in life"
    answer: 0
    explain: "The 2025 data had first-year rates of about 1.3 percent and a peak of 4.25 percent at around ten years, against a peak of 13.73 percent at about three years in 2013. There is still a late rise, so 'constant at all ages' is wrong too."
  - q: "A reader says: 'This is just one airline's data from the 1960s and 70s, so it tells us nothing about how equipment fails.' Which response best fits the evidence?"
    options:
      - "Correct: the patterns have never been seen outside United Airlines"
      - "Correct: the report was withdrawn after the Navy failed to reproduce it"
      - "Wrong: the 89 percent figure has been confirmed as a universal constant for all machinery"
      - "Partly right: the exact shares are specific to that fleet and its maintenance, but the finding that many complex items show no wear-out zone has been echoed in other settings, such as Backblaze's drives and the US Navy's adoption of the method"
    answer: 3
    explain: "The sceptical options sound careful but are false: the report was not withdrawn, and the US Navy extended the approach beyond aircraft in 1982. Equally, no one has shown 89 percent is universal. The calibrated view keeps the qualitative finding and holds the exact numbers loosely."
reflect:
  - "If items are usually replaced or overhauled before they get old, a dataset may contain very few old items. How would that make it harder to detect a wear-out zone, and how could you design a study to check?"
  - "Pick a piece of equipment you rely on, such as a bicycle, a laptop battery or a boiler. Which of the six patterns would you guess it follows, and what data would you need to find out?"
---

## The idea

Most people carry a picture of how things fail. A new product has teething troubles, then a long quiet middle, then it wears out and failures climb again. Plotted as the chance of failing at each age, the curve dips, flattens and rises, and engineers call it the bathtub curve. If it is right, the sensible policy is obvious: replace or overhaul parts before they reach the wear-out zone.

For decades airlines did exactly that. Engines, gearboxes and many smaller parts had fixed hard-time limits, after which they were removed and rebuilt whether or not anything was wrong. In 1978 two United Airlines engineers, F. Stanley Nowlan and Howard F. Heap, published a report for the US Department of Defense called Reliability-Centered Maintenance. It summarised years of United's own analysis of when aircraft components actually failed, and it found that the bathtub was the exception.

United's analysts built a curve of the conditional probability of failure against age for many components, and the curves fell into six shapes. Pattern A was the bathtub. Pattern B was flat or slowly rising, then a sharp wear-out rise; the report says this is typical of piston engines. Pattern C rose gradually with no clear wear-out age, typical of turbine engines. Pattern D started low and rose quickly to a constant level. Pattern E was constant at every age. Pattern F began with infant mortality and then stayed roughly flat, which the report links to electronics.

The shares are the striking part. According to the report, just 4 percent of the items studied followed the bathtub, and only 6 percent (A and B together) showed a pronounced wear-out zone. Another 5 percent rose gently without one. The remaining 89 percent, patterns D, E and F, had no wear-out zone at all, so a fixed age limit could not help them. For complex items, the authors concluded, reliability "does not vary directly with operating age."

A concrete example from the report: United had a fleet of JT8D-7 jet engines. Had they been scheduled for removal at 1,000 hours, 69 percent would have reached that limit and been pulled while still working, while the failures that happened earlier would not have been prevented at all.

## Why it might change a decision

The report went further than saying overhauls were often useless. It argued that in many cases scheduled overhaul increases the overall failure rate, by introducing high infant mortality into an otherwise stable system. Taking a working assembly apart and rebuilding it puts it back at the start of its life, which for many items is the riskiest period.

This became the basis of reliability-centred maintenance. The practical shift is visible in the report's own comparison: the DC-8's original maintenance programme scheduled overhauls for 339 items, while the later DC-10 programme, built with the new logic, scheduled them for seven.

The testable behaviour is simple to state. For any item now replaced on a fixed schedule, compare its failure rate in the period just after maintenance with its rate later in life. If early failures are higher and there is no late rise, the schedule is adding risk rather than removing it, and condition checks would be the better candidate to test.

## How solid is this?

The core evidence comes from one airline's internal analyses, summarised rather than published as a peer-reviewed study. The exhibit's caption does not give a component count or time span that I could read, and the percentages are shares of items studied, not of failures or of failures weighted by danger. Aircraft parts are also unusual: heavily redundant, closely inspected and often already removed on condition.

There is a strong competing explanation for the missing wear-out zones. If parts are routinely replaced before they get old, few old parts remain in the data, so a late rise could simply go unobserved. Nowlan and Heap's argument is partly about complex items with many failure modes, where no single mode dominates, but censoring of this kind is a real limit on what the shares can show. The report itself says simple items with one dominant failure mode can still benefit from an age limit.

The qualitative finding has travelled. NASA's 2008 maintenance guide for facilities repeats that for many items the likelihood of failure did not rise with age, and notes the US Navy extended the approach beyond aircraft in 1982. Backblaze, which publishes failure data on its data-centre hard drives, reported in 2013 an early rate of 5.1 percent, a middle rate of 1.4 percent and a wear-out rate of 11.8 percent in years three to four, a fair bathtub. By 2025, across about 317,000 drives, first-year rates were near 1.3 percent and the peak was 4.25 percent at around ten years. Backblaze calls the curve incomplete rather than wrong; its own data are from one company's hardware and replacement policies.

Where the popular claim outruns the data: the 89 percent figure is often quoted as if it describes all machinery. It describes United's aircraft items in that study.

## Sources

- F. Stanley Nowlan and Howard F. Heap (1978). *Reliability-Centered Maintenance*. United Airlines, for the Office of the Assistant Secretary of Defense (Manpower, Reserve Affairs and Logistics). DTIC accession ADA066579. https://apps.dtic.mil/sti/pdfs/ADA066579.pdf
- NASA (September 2008). *NASA Reliability-Centered Maintenance Guide for Facilities and Collateral Equipment*. https://www.wbdg.org/FFC/NASA/NASACRIT/NASA_RCMGuide.pdf
- Andy Klein (26 October 2021). "Drive Failure Over Time: The Bathtub Curve Is Leaking." Backblaze. https://www.backblaze.com/blog/drive-failure-over-time-the-bathtub-curve-is-leaking/
- Backblaze Drive Stats Team (15 October 2025). "Are Hard Drives Getting Better? Let's Revisit the Bathtub Curve." Backblaze. https://www.backblaze.com/blog/are-hard-drives-getting-better-lets-revisit-the-bathtub-curve/
