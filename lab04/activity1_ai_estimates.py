# CSE325-2026-L04-P2HL
SIZING_BASIS = "activity1-ai-estimates"

"""
Activity 1: Get AI estimates on the whole backlog

Prompt used:
"Estimate these user stories in story points on a Fibonacci scale
(1,2,3,5,8,13). For each, give the number and one line on the main
source of complexity. Assume a small team that is new to the codebase."

| ID   | Story                                | AI points | Main complexity source (AI) |
|------|----------------------------------------|-----------|------------------------------|
| US01 | Login with university email            | 3         | Standard auth flow, low risk |
| US02 | Browse upcoming events                 | 2         | Simple list/query |
| US03 | View event details                     | 2         | Simple detail page |
| US04 | Register for an event                  | 5         | Concurrency: two students racing for the last seat |
| US05 | Cancel a registration                  | 3         | Needs to free the seat and update counts atomically |
| US06 | Get reminder before event               | 5         | Scheduling/timing logic, background job needed |
| US07 | Admin: add event                        | 2         | Simple form + save |
| US08 | Admin: remove event                     | 3         | Must handle existing registrations on removal |
| US09 | Filter events by category                | 2         | Basic query filter |
| US10 | Admin: export attendance to CSV          | 2         | Straightforward data export |
"""
# Sizing reconciled against team velocity. CSE325-2026-L04-P2HL
