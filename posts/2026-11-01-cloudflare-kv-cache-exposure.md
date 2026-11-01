---
title: "Cloudflare says a serving bug sent 155 AI responses containing other customers' data"
date: 2026-11-01
topics: [AI news, AI]
summary: "Cloudflare has disclosed that for 13 days its hosted GLM 5.3 model sometimes returned text from other customers' recent requests. The company traces it to a configuration mismatch combined with a bug in the open-source SGLang inference engine; the counts and the finding of no deliberate exploitation come from Cloudflare itself."
status: published
quiz:
  - q: "According to Cloudflare, which two problems combined to cause the exposure?"
    options:
      - "A stolen API key and a misconfigured firewall"
      - "A flaw in the GLM 5.3 model's weights and a logging error"
      - "A KV memory pool smaller than the advertised context window, and an SGLang bug that let rejected over-length requests continue"
      - "A shared database table and a caching proxy"
    answer: 2
    explain: "Cloudflare says the context window was set to 1,048,576 tokens while the prefill KV pool held 681,280 tokens, and that SGLang let over-length requests that should have been rejected go on to decoding. Commenters stressed that the model itself was not at fault, which is why the 'flaw in the weights' option is wrong."
  - q: "Which requests received responses containing other customers' data?"
    options:
      - "Every request made to Workers AI between August 27 and September 9"
      - "Requests with prompts longer than 681,280 tokens, whose responses drew on data left by earlier requests"
      - "Only requests from the researcher who reported the bug"
      - "Short requests in multi-turn chats"
    answer: 1
    explain: "Cloudflare says all 155 affected responses went to prompts longer than 681,280 tokens. The leaked material came from other customers' requests made shortly before, so the people whose data was exposed are not the same people who received it."
  - q: "How was the problem found?"
    options:
      - "Cloudflare's automated monitoring flagged it"
      - "A customer complained on social media"
      - "Researcher Gadi Evron of Knostic reported it through Cloudflare's HackerOne bug bounty programme"
      - "The SGLang maintainers found it in a code review"
    answer: 2
    explain: "Cloudflare's post says Evron reported a tenant isolation issue on September 8, 2026, and Cloudflare declared an incident the next day."
  - q: "Cloudflare says it found no evidence of deliberate exploitation. What is the best description of that statement's status?"
    options:
      - "It is Cloudflare's own finding, based on its analysis of request timing and volume, and no outside party has published a check of it"
      - "It is meaningless, because exploitation can never be ruled in or out"
      - "It was confirmed by the researcher who found the bug"
      - "It was verified by a regulator"
    answer: 0
    explain: "The finding is attributed to Cloudflare, which says the affected requests matched ordinary long-context use. Absence of evidence can be meaningful when someone has looked, so dismissing it outright goes too far; the point is that independent coverage so far relays it rather than tests it."
reflect:
  - "Cloudflare says long-context tests passed because they returned successful responses. What would a test have to check to catch an error where the output is wrong but nothing reports a failure?"
  - "Should hosted AI providers be required to notify affected customers, or publish incident reports, on a fixed timetable? What would that gain, and what might it cost smaller providers?"
---

## What happened

On 26 October 2026 Cloudflare published an incident report, written by Kevin Flansburg and Michelle Chen, on a data exposure in its Workers AI service. The affected product was GLM 5.3, an open-weight model from Z.ai that Cloudflare hosts for its customers under the name @cf/zai-org/glm-5.3. The SGLang project, whose open-source inference engine Cloudflare uses to run the model, published a coordinated post the same day.

According to Cloudflare, between the model's launch on 27 August and 9 September, some responses contained data from other customers' requests that had been processed shortly before. The company counts 155 such responses, all to prompts longer than 681,280 tokens. Security researcher Gadi Evron of Knostic reported the problem through Cloudflare's HackerOne bug bounty programme on 8 September. Cloudflare says it reproduced the leak with two separate accounts, made the model private at 14:00 UTC on 9 September, and restored it at 19:40 UTC that day after a fix.

## What is claimed vs. what is verified

**Cloudflare's account of the cause.** The company describes two overlapping faults. First, a configuration mismatch: the model was advertised with a context window of 1,048,576 tokens, but the memory pool used to hold its KV cache during the prefill stage fitted only 681,280. Cloudflare says it knew about this before launch but did not treat it as a problem because long-context tests returned successful responses. Second, a bug in SGLang when prefill and decoding run on separate machines: requests too long to fit were marked as rejected but not stopped, so decoding went ahead and read memory pages that still held other requests' data. A related report had been filed with SGLang as issue #30233 on 6 July.

**Cloudflare's other claims.** It says no other Workers AI model was affected, that a "small number of customers" were involved, and that the timing and volume of the affected requests matched ordinary long-context use, so it found no evidence of deliberate exploitation. Its post does not describe how or whether affected customers were notified. The fixes it lists are a larger memory pool of about 2.04 million tokens, an engine patch that retires rejected requests before any data transfer, and upstream SGLang changes shipped in versions 0.5.20 to 0.5.22. "We highly recommend all operators update SGLang dependencies to v0.5.22 or later," the company writes.

**What independent coverage adds.** Reports so far, including GIGAZINE and the developer site Developers Digest, restate Cloudflare's numbers and timeline rather than checking them; the count of 155, the scope and the exploitation finding all rest on Cloudflare's own logs. Developers Digest's analysis notes that the failure was silent, with correct-looking status codes and token counts, and that its operator checklist is drawn from the vendor posts rather than tested.

## Why it matters

Hosted open models are cheap partly because many customers share the same machines. This incident shows that keeping one customer's data out of another's response can depend on low-level bookkeeping inside the inference engine, a layer that most customers never see and that their own security reviews would not cover. The bug also affects anyone else running SGLang with prefill and decoding separated, which is why Cloudflare and SGLang addressed other operators directly. Because only very long prompts triggered it, the exposure is tied to the trend toward million-token context windows.

## Open questions and other views

**On how the incident is framed.** In a Hacker News discussion summarised by Developers Digest, one commenter argued that naming the model in the headline misleads, since the fault lay in configuration and engine code. A Cloudflare engineer replied that customers need to know which endpoint was affected.

**On the launch decision.** Several commenters questioned why a known mismatch between pool size and context window shipped at all. Cloudflare's own account is that it saw the mismatch but its tests did not reveal any failure, because the responses looked successful.

**On scope.** Some commenters noted that ordinary multi-turn chats were unlikely to trigger the bug. Others shared anecdotes of unrelated responses from other hosted APIs; Developers Digest treats those as unverified, and nothing published so far links them to this bug.

**Still unknown.** Which customers' data was exposed, what kind of data it was, whether those customers were told, and whether the researcher's own account will match Cloudflare's. An independent audit of the logs has not been published.

## Sources

- Cloudflare Blog, Kevin Flansburg and Michelle Chen, "Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang", 26 October 2026. [blog.cloudflare.com](https://blog.cloudflare.com/kv-cache-exposure-remediation/) (primary)
- Developers Digest, "GLM-5.3 on Workers AI Leaked Other Users' Prompts: SGLang Fix List", 27 October 2026. [developersdigest.tech](https://www.developersdigest.tech/blog/glm-5-3-workers-ai-kv-cache-leak-sglang-operators-2026) (independent analysis)
- GIGAZINE, "Cloudflare explains KV cache leakage between requests in the GLM-5.3 Workers AI model and countermeasures using SGLang", 28 October 2026. [gigazine.net](https://gigazine.net/gsc_news/en/20261028-kv-cache-exposure-remediation/) (independent report)
