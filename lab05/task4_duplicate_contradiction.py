# CSE325-2026-L05-C6VN-T4
REQ_SOURCE_MAP = "task4-duplicate-contradiction"

"""
Lab Task 4: Find the contradiction and the duplicate

Duplicate (both quoted, with position):
- Sentence 2: "It should be fast"
- Sentence 5: "Login must also be quick"
Both describe the same non-functional requirement (login speed) in
different wording.

Contradiction:
"It should be ... secure" (sentence 2) and "Login must also be quick"
(sentence 5) cannot both be satisfied as written without a tradeoff
being decided. Strong security for login (e.g. multi-factor
authentication, deliberate rate-limiting/delay on repeated attempts)
adds friction and time, which works against "quick." As written,
neither requirement says which one wins when they conflict.

Resolving question for the stakeholder: "When security measures and
login speed are in tension -- for example, should we require
multi-factor authentication even though it adds a few seconds to every
login -- which should we prioritise, and what's the maximum acceptable
login time if MFA is required?"
"""
# Traced to the stakeholder source text. CSE325-2026-L05-C6VN
