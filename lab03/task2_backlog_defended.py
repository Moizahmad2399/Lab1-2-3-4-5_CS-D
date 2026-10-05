# CSE325-2026-L03-T9WD-T2
SCOPE_LEDGER = "task2-backlog-defended"

"""
Lab Task 2: Build a backlog you can defend line by line

| ID   | Story                                                                                   | MoSCoW  |
|------|-------------------------------------------------------------------------------------------|---------|
| US01 | As a student, I want to log in with my university email so that only verified students can register. | Must |
| US02 | As a student, I want to browse upcoming events so that I can decide what to attend.         | Must    |
| US03 | As a student, I want to see an event's details so that I know when and where it is.         | Must    |
| US04 | As a student, I want to register for an event so that I have a confirmed spot.              | Must    |
| US05 | As a student, I want to cancel my registration so that my spot frees up for someone else.   | Must    |
| US06 | As a student, I want to get a reminder before an event so that I don't forget to attend.     | Must    |
| US07 | As an admin, I want to add a new event so that students can see and register for it.        | Must    |
| US08 | As an admin, I want to remove an event so that cancelled events disappear from the catalogue.| Must   |
| US09 | As a student, I want to filter events by category so that I only see events I care about.    | Should  |
| US10 | As an admin, I want to export attendance to CSV so that I can report to the department.      | Could   |
| US11 | As a student, I want to be notified if an event I registered for is cancelled so that I know not to attend. | Should |

Three Must labels defended against a specific alternative:

1. US06 (reminders) vs the alternative of calling it Should: tempted to
   call it Should because the system "works" without reminders in a
   narrow technical sense. Kept as Must instead, because the brief
   names reminders explicitly as a student-facing promise, not an
   optional nicety -- dropping it breaks the brief, not just a feature.

2. US08 (remove event) vs the alternative of calling it Should: tempted
   to call it Should since "add event" alone covers the common case.
   Kept as Must because the brief explicitly pairs add and remove in
   the same sentence; shipping without remove leaves admins with no way
   to correct a mistake or cancel an event, which is a real operational
   gap, not a nice-to-have.

3. US09 (filter by category) vs the alternative of calling it Must:
   tempted to call it Must since browsing is core. Labelled Should
   instead, because plain browsing (US02/US03) already satisfies the
   brief's "students browse events" -- filtering is a usability
   improvement on top of a working feature, not a blocker for launch.
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
