# CSE325-2026-L03-T9WD
SCOPE_LEDGER = "activity1-module-breakdown"

"""
Activity 1: Draft the module breakdown

Brief: "You are planning a Campus Event Management System: students
browse events, register, and get reminders; admins add and remove events."

Prompt used:
"Act as a software project planner. Break the Campus Event Management
System into 4-6 modules. For each module list 3-5 concrete engineering
tasks. Give the result as a nested list."

AI first-draft output:

1. Auth & Accounts
   - Student registration with university email
   - Login / logout
   - Password reset flow

2. Event Catalogue
   - List all upcoming events
   - Event detail page
   - Search/filter events by category and date

3. Registration
   - Register for an event
   - View my registered events
   - Admin-side registration count view

4. Reminders
   - Send reminder before each event (single task, folded into Registration)

5. Admin Console
   - Add new event
   - Edit event details
   - Analytics dashboard for event popularity trends

Gaps noticed on first read (confirmed later in Task 1):
- Session-token handling is missing entirely under Auth & Accounts.
- There is no task for cancelling a registration under Registration.
- Reminders was folded into Registration as one line instead of being
  its own module, even though the brief calls reminders out explicitly.
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
