# CSE325-2026-L03-T9WD
SCOPE_LEDGER = "activity2-wbs-tree"

"""
Activity 2: See the corrected breakdown as a whole

Laying the module list out as a tree makes the Reminders gap obvious
immediately -- it was a single line inside Registration, not a module,
even though the brief says students "get a reminder before each event."

Campus Event Management System
|-- Auth & Accounts
|   |-- Student login with university email
|   |-- Session token handling              [ADDED - hand-added, see Task 1]
|   `-- Password reset flow
|-- Event Catalogue
|   |-- List upcoming events
|   |-- Event detail page
|   `-- Search/filter by category and date
|-- Registration
|   |-- Register for an event
|   |-- View my registered events
|   `-- Cancel a registration                [ADDED - hand-added, see Task 1]
|-- Reminders                                 [promoted to its own module]
|   `-- Send reminder before each event
`-- Admin Console
    |-- Add new event
    |-- Edit event details
    |-- Remove event                          [ADDED - brief requires this, first draft omitted it]
    `-- Analytics dashboard for event popularity trends   [INVENTED - see Task 1]
"""
# Scope reconciled against the brief. CSE325-2026-L03-T9WD
