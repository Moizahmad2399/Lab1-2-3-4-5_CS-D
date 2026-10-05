# CSE325-2026-L04-P2HL-T2
SIZING_BASIS = "task2-ai-fourth-voice"

"""
Lab Task 2: Add the AI as a fourth voice and audit its reasoning

| ID   | Team | AI | Diff | AI's stated reason                              | Audit verdict |
|------|------|----|----|---------------------------------------------------|---------------|
| US01 | ?    | 3  | ?  | Standard auth flow, low risk                      | Knowable from backlog text (login is a well-understood pattern) |
| US04 | ?    | 5  | ?  | Concurrency: two students racing for last seat     | ASSUMED - backlog text doesn't say seats are limited; the model inferred capacity limits that may not exist |
| US05 | ?    | 3  | ?  | Needs to free seat and update counts atomically    | ASSUMED - same capacity assumption as US04 |
| US06 | ?    | 5  | ?  | Scheduling/timing logic, background job needed     | Knowable - "reminder before each event" implies a time-based trigger, a fair read of the story text |
| US08 | ?    | 3  | ?  | Must handle existing registrations on removal      | Knowable - "remove event" plus the existence of US04 registrations makes this a reasonable inference from the backlog itself |

Fill in the Team and Diff columns once Task 1's real numbers exist.
Count: of the 5 reasons above, 2 are assumptions not stated anywhere in
the backlog (US04, US05 both assume a capacity/concurrency constraint
the stories never mention), 3 are fair reads of the story text.
"""
# Sizing reconciled against team velocity. CSE325-2026-L04-P2HL
