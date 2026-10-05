# CSE325-2026-L03-T9WD-T1
SCOPE_LEDGER = "task1-reconciled-wbs"

"""
Lab Task 1: Produce a reconciled work-breakdown structure

Every row below is traced to the brief text or marked ADDED with a reason.

Brief text (verbatim): "You are planning a Campus Event Management
System: students browse events, register, and get reminders; admins
add and remove events."

| Module          | Task                                  | Source |
|------------------|----------------------------------------|--------|
| Auth & Accounts  | Student login                          | ADDED - registration requires a known student identity; not explicitly in brief |
| Auth & Accounts  | Session token handling                 | ADDED - required for login to persist; not in brief |
| Event Catalogue  | List/browse upcoming events             | "students browse events" |
| Event Catalogue  | Event detail page                       | "students browse events" |
| Registration     | Register for an event                   | "students ... register" |
| Registration     | Cancel a registration                   | ADDED - without this, registration counts drift from reality as students drop out |
| Reminders        | Send reminder before each event         | "students ... get reminders" |
| Admin Console    | Add new event                           | "admins add ... events" |
| Admin Console    | Remove event                            | "admins ... remove events" |

INVENTED TASK (model produced, brief does not support):
"Analytics dashboard for event popularity trends" -- quoted verbatim
from the Activity 1 AI output above. Nothing in the brief mentions
analytics or reporting; the model added this because it's a common
admin-console feature in general, not because the brief called for it.

OMITTED TASKS (brief requires, first AI draft missed):
1. "Remove event" -- the brief explicitly says "admins add and remove
   events," but the first-draft Admin Console list only had Add and
   Edit, no Remove.
2. Reminders as a real task -- the brief explicitly says students
   "get reminders," but the first draft folded this into a single line
   under Registration instead of giving it its own task, which under-
   represents the engineering work (scheduling, sending, timing logic).
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
