# AI Fix Notes

Session: seq-1785411389226-1e0bkfiw0
Repository: Ncorp30/sqli-test

## Summary

- Detected actionable issues: 5
- Issues with proposed PR changes: 3
- Issues requiring manual review: 2
- Automated fix mode: partial / safety-first

## Safety Policy

High-priority findings touching security, authentication, credentials, network behavior, dependency safety, privacy, request handling, or response handling are not silently edited by the agent. They are listed for manual review unless the workflow can generate a bounded, low-risk change with enough context.

## Proposed Changes Included in This PR

- [1] (medium) demo.py: Database connection and cursor are never closed. Use a context manager or explicit cleanup (`close()` / `with`) to avoid resource leaks.
- [2] (medium) demo.py: The function performs database access but has no error handling. Exceptions from connection or query execution will propagate and may expose unstable behavior in production.
- [3] (low) demo.py: The function name `login` suggests authentication logic, but the implementation only queries by username and does not validate credentials or return a result, making the API misleading and incomplete.

## Manual Review Required

- [1] (critical) demo.py: SQL injection vulnerability: user input is interpolated directly into the SQL query via f-string. An attacker can manipulate the `username` value to alter the query and access or modify data.
  - Reason: High-priority security-sensitive finding requires human review before code changes.
  - Next step: Confirm the intended security behavior, threat model, and tests before applying a targeted fix.
- [2] (high) demo.py: Use parameterized queries instead of string concatenation/f-strings for database access. This is a core security best practice and prevents injection attacks.
  - Reason: High-priority security-sensitive finding requires human review before code changes.
  - Next step: Confirm the intended security behavior, threat model, and tests before applying a targeted fix.