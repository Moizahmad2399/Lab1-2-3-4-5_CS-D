# CSE325-2026-L03-T9WD-T3
SCOPE_LEDGER = "task3-local-context"

"""
Lab Task 3: Find a gap the model cannot see

*** PLACEHOLDER - confirm or replace before submitting ***
This needs a constraint that is genuinely true of YOUR campus. The
marker checks that this is actually local, so don't submit this
unedited -- swap in something you know firsthand (campus WiFi behaviour,
power outage patterns, the devices your cohort actually uses, a
university policy).

Draft example (edit to match your real situation):

Requirement: The event reminder must also work over SMS, not only
push notification/email, because campus WiFi coverage is unreliable in
several lecture halls and many students rely on mobile data with
limited daily allowance rather than a constant connection.

Why no general-purpose model could produce this: a model has no way to
know which specific campus buildings have poor WiFi coverage, or that
students in this cohort commonly ration mobile data -- that's local,
firsthand knowledge, not something inferable from the one-line brief.

MoSCoW label: Should -- it meaningfully improves reliability for a
real chunk of users, but push/email reminders still satisfy the literal
brief requirement on their own, so it's not blocking for launch.

Backlog row:
| US12 | As a student with unreliable WiFi, I want to receive event
reminders over SMS so that I don't miss events when my connection
drops. | Should |
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
