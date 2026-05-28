# Timing Decision Table - v3 Review

Rule used for v3: actual spoken cue is the source of truth. Visual starts after the cue, usually 0.27-0.30 seconds later. This avoids showing the punchline early and avoids the v2 issue where some slides landed 1-2 seconds late.

| Slide | Cue phrase | Detected cue timestamp | Proposed visual start timestamp | Delay after cue | Visual type | Reason | Risk |
|---:|---|---:|---:|---:|---|---|---|
| 1 | founder raises funding | 0:02.879 | 0:03.18 | +0.30s | split-screen | Starts after the first funding phrase, so the visual supports the line instead of preloading it. | okay |
| 2 | hire SDRs | 0:07.000 | 0:07.30 | +0.30s | split-screen | Lands right after the hiring line starts. | okay |
| 3 | Three months later | 0:14.280 | 0:14.55 | +0.27s | split-screen | Calendar should appear immediately after the time jump. | okay |
| 4 | burn rate vertical | 0:21.359 | 0:21.65 | +0.29s | split-screen | Fixes the v1/v2 late issue; burn visual lands on the burn-rate phrase. | okay |
| 5 | you're gambling | 0:32.920 | 0:33.20 | +0.28s | split-screen | Uses the exact punchline word instead of the earlier setup sentence. | okay |
| 6 | public payroll | 0:51.578 | 0:51.85 | +0.27s | split-screen | Payroll visual lands after "public payroll" is spoken. | okay |
| 7 | public version | 0:56.898 | 0:57.20 | +0.30s | split-screen | Supports the "visible stuff/public version" point, not the prior payroll line. | okay |
| 8 | you don't see pain | 1:05.058 | 1:05.35 | +0.29s | split-screen | Pain/lab visual appears when the hidden process is named. | okay |
| 9 | 25-year-old SDR | 1:17.458 | 1:17.75 | +0.29s | split-screen | No-playbook visual lands when the SDR is asked to lead the market. | okay |
| 10 | email sequence | 1:22.904 | 1:23.20 | +0.30s | split-screen | Sequence-not-playbook slide appears on the actual sequence line. | okay |
| 11 | message-market fit | 1:29.664 | 1:29.95 | +0.29s | split-screen | Transcript reads "mess in market fit"; timing matches the intended concept. | okay |
| 12 | becomes creepy | 1:51.824 | 1:52.10 | +0.28s | split-screen | Creepy-personalization visual should not appear before the word "creepy" starts. | okay |
| 13 | careful buyers | 1:59.130 | 1:59.40 | +0.27s | split-screen | Research visual lands after the careful-buyer setup. | okay |
| 14 | one cold email | 2:16.450 | 2:16.75 | +0.30s | split-screen | Delulu/cold-email visual starts after the bad-selling assumption is spoken. | okay |
| 15 | not the machine | 2:34.775 | 2:35.05 | +0.28s | split-screen | Operator-not-machine visual lands on the thesis line. | okay |
| 16 | playbook is machine | 2:41.135 | 2:41.42 | +0.28s | split-screen | Machine blueprint appears right after the key thesis phrase. | okay |
| 17 | more operators | 2:52.607 | 2:52.90 | +0.29s | split-screen | Bigger-mess slide lands on the operator/output line. | okay |
| 18 | more volume | 3:09.519 | 3:09.80 | +0.28s | split-screen | Volume-button visual lands on the "more volume" idea. | okay |
| 19 | message is dead | 3:21.120 | 3:21.40 | +0.28s | split-screen | Rejection factory can start at "message is dead"; caption can land later on "industrial level." | okay |
| 20 | 2 out of 100 | 4:00.839 | 4:01.12 | +0.28s | split-screen | Prospect-count visual appears as the math is introduced. | okay |
| 21 | why they said yes | 4:10.119 | 4:10.40 | +0.28s | split-screen | Detective visual lands on the analysis instruction. | okay |
| 22 | 6 months not wasted | 4:21.999 | 4:22.28 | +0.28s | split-screen | Underground-system visual lands after the six-month line. | okay |
| 23 | not SDR agency tool | 4:54.479 | 4:54.76 | +0.28s | split-screen | Repeated negation needs the visual after the phrase starts. | okay |
| 24 | build playbook first | 5:00.119 | 5:00.42 | +0.30s | split-screen | Final machine/playbook visual lands after the closing thesis starts. | okay |

## Notes

- These starts are intentionally later than v2's visual starts where v2 used pre-roll.
- The current review package does not decide internal text animation timing. Suggested internal reveal: visual base at proposed start, headline +0.20s, caption +0.70s to +1.20s depending on the spoken joke.
- Slide 19 may need special handling in the full edit: visual can start at "message is dead," but the caption "Industrialized rejection" should wait until the later rejection phrase around 3:32.840.
