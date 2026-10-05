# CSE325-2026-L05-C6VN
REQ_SOURCE_MAP = "activity1-extract"

"""
Activity 1: Extract without inventing

Stakeholder notes: "We need the app to let students log in with their
university email. It should be fast and secure. Students register for
events and get a reminder before each event. Admins can add or remove
events. Login must also be quick. The system should handle many users."

Prompt used: "Extract all software requirements from the text below as
a numbered list. Do not invent requirements that are not there."

Extraction result (9 genuine + 1 caught hallucination):
1. Students can log in with university email
2. Login should be fast
3. Students register for events
4. Students get a reminder before each event
5. Admins can add events
6. Admins can remove events
7. Login must be quick
8. System should be secure
9. System should handle many users
10. [STRUCK] "The system should support multiple languages" -- this
    appears nowhere in the stakeholder notes. Caught by cross-checking
    the extraction against the source text; a clean hallucination.
"""
# Traced to the stakeholder source text. CSE325-2026-L05-C6VN
