# CSE325-2026-L05-C6VN-T3
REQ_SOURCE_MAP = "task3-testable-rewrites"

"""
Lab Task 3: Make the vague ones testable, and say how you would test them

1. Original: "It should be fast" / "Login must also be quick"
   Rewrite: "Login must complete in under 2 seconds on a standard
   university WiFi connection, 95% of the time."
   Measurement: Run 100 login attempts on campus WiFi using a load-
   testing tool (e.g. k6 or Locust), log response time per attempt,
   confirm at least 95 complete under 2 seconds.

2. Original: "It should be ... secure"
   Rewrite: "All login traffic must be encrypted in transit (TLS 1.2+)
   and passwords must be hashed (bcrypt or equivalent), never stored in
   plain text."
   Measurement: Inspect network traffic with a proxy tool (e.g.
   Wireshark/Burp) to confirm TLS is in use; query the database
   directly to confirm password fields are hashed, not plaintext.

3. Original: "The system should handle many users"
   Rewrite: "The system must support at least 5,000 concurrent active
   users without response time exceeding 3 seconds."
   Measurement: Run a load test simulating 5,000 concurrent sessions
   (e.g. with k6) against a staging environment, record the 95th-
   percentile response time, confirm it stays under 3 seconds.
"""
# Traced to the stakeholder source text. CSE325-2026-L05-C6VN
