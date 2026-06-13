# Access Boundary

This package follows the AFLUZ six-level access ladder, but it does not grant
access by itself.

```text
Level 0 = Public View
Level 1 = Project Follower
Level 2 = Supporter Circle
Level 3 = Evaluator Access
Level 4 = Partner / Licensing
Level 5 = Internal Operator
```

The standalone tool is intended for Level 0-3 evaluation and Level 4 scoped
discussion. Level 5 is not public and is not included in this package.

## Protected Surfaces

The tool refuses requests for:

- full ELUZA core source
- private Brain memory
- raw datasets
- internal decision logic
- thresholds/private rules
- credentials/secrets
- ownership transfer

Public refusal wording:

```text
ไม่สามารถเปิดเผยได้ค่ะ
```

The refusal is a tool output from the access boundary and public Mizan status.
It is not a leak of private logic.

