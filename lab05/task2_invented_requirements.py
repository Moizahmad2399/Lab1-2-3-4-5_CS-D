# CSE325-2026-L05-C6VN-T2
REQ_SOURCE_MAP = "task2-invented-requirements"

"""
Lab Task 2: Catch the model inventing

Run 1 (prompt: "Extract all software requirements from the text below
as a numbered list. Do not invent requirements that are not there."):
Invented: "The system should support multiple languages." Likely
over-read: the notes mention "university email" and "many users",
which can read as implying a large/diverse user base -- the model
seems to have generalised "many users" into "diverse/international
users" and added a language requirement that isn't actually there.

Run 2 (different prompt: "List only the requirements explicitly stated
in this text. If you are inferring anything, label it INFERRED instead
of stating it directly."):
Same invented item did NOT recur as a bare requirement, but it did
resurface, now explicitly labelled: "INFERRED: system may need to
support multiple languages given a large user base." This confirms the
same over-reading of "many users" happened again on the second run --
it's a repeatable invention tied to that specific phrase, not a one-off,
which is the more useful finding (it tells you "many users" is a
phrase that reliably triggers this hallucination, not just bad luck).
"""
# Traced to the stakeholder source text. CSE325-2026-L05-C6VN
