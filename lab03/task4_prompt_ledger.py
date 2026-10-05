# CSE325-2026-L03-T9WD-T4
SCOPE_LEDGER = "task4-prompt-ledger"

"""
Lab Task 4: Keep an honest prompt ledger

1. "List the modules for a Campus Event Management System."
   Result: too shallow -- returned a flat 5-item list with no tasks
   underneath, not usable as a WBS.
   Change made: added an explicit role, a module count range, and a
   requirement for 3-5 tasks per module.

2. "Act as a software project planner. Break the Campus Event
   Management System into 4-6 modules. For each module list 3-5
   concrete engineering tasks. Give the result as a nested list."
   Result: usable first draft (Activity 1 output). Missing session
   tokens and cancel-registration, Reminders folded into Registration,
   contained an invented analytics task.
   Change made: kept this prompt as the working draft; next step was
   manual reconciliation against the brief rather than re-prompting,
   since the gaps were catchable by hand.

3. "Rewrite these tasks as user stories and apply MoSCoW with a
   justification per label."
   Result: usable, but every story came back Must on the first pass --
   no real prioritisation signal.
   Change made: added "most stories should NOT be Must -- only label
   something Must if the brief breaks without it" to force genuine
   differentiation on the next attempt.

4. "Rewrite these tasks as user stories... apply MoSCoW... only label
   Must if the system breaks without it, otherwise use Should/Could."
   Result: usable, produced the spread kept in Task 2 (8 Must, 2
   Should, 1 Could).
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
