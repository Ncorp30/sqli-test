# AI Fix Notes

Session: seq-1785412089128-bpld1lt89
Repository: Ncorp30/sqli-test

## Summary

- Detected actionable issues: 9
- Issues with proposed PR changes: 6
- Issues requiring manual review: 3
- Automated fix mode: partial / safety-first

## Safety Policy

High-priority findings touching security, authentication, credentials, network behavior, dependency safety, privacy, request handling, or response handling are not silently edited by the agent. They are listed for manual review unless the workflow can generate a bounded, low-risk change with enough context.

## Proposed Changes Included in This PR

- [1] (medium) long_function.py: Long, monolithic function with multiple responsibilities (validation, pricing, tax calculation, and invoice creation). This increases cognitive complexity and makes testing and reuse harder.
- [2] (medium) long_function.py: Unsafe dictionary access throughout the function can raise KeyError if expected keys such as 'customer', 'address', 'items', or 'discount' are missing.
- [3] (medium) long_function.py: Input data is trusted without schema validation. If 'order' comes from external input, malformed or malicious payloads could trigger exceptions or logic abuse.
- [4] (medium) test.py: Possible TypeError: request.args.get('id') may return None, and concatenating None to a string will raise an exception when 'id' is missing.
- [5] (medium) test.py: Endpoint lacks input validation and response formatting. Returning raw string output from query parameters makes the behavior brittle and harder to extend safely.
- [6] (low) long_function.py: Pricing logic uses repeated inline conditional branching inside the item loop. As item types grow, this becomes harder to optimize and maintain; a lookup table or strategy map would scale better.

## Manual Review Required

- [1] (critical) demo.py: SQL injection vulnerability: user-controlled input is interpolated directly into the SQL query using an f-string. An attacker can bypass authentication or exfiltrate data by injecting SQL payloads.
  - Reason: High-priority security-sensitive finding requires human review before code changes.
  - Next step: Confirm the intended security behavior, threat model, and tests before applying a targeted fix.
- [2] (high) demo.py: Authentication logic is unsafe and incomplete. The function named 'login' performs a raw database query but does not validate passwords, verify results, or close the database connection, creating both security and resource-management risks.
  - Reason: High-priority security-sensitive finding requires human review before code changes.
  - Next step: Confirm the intended security behavior, threat model, and tests before applying a targeted fix.
- [3] (high) test.py: Potential reflected injection/XSS risk: untrusted request parameter 'id' is concatenated into the HTTP response without escaping or validation. In a real HTML response context this could expose users to injection issues.
  - Reason: High-priority security-sensitive finding requires human review before code changes.
  - Next step: Confirm the intended security behavior, threat model, and tests before applying a targeted fix.