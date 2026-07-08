# Security & Data Safety Policy

## Reporting a concern

This is a research and prototype repository, not a production system. If you
find a security issue in a prototype (for example, in
[`prototypes/evidence-review-agent/`](prototypes/evidence-review-agent/)), or
you spot real student data or other personally identifiable information
anywhere in this repository, please open a private report:

- Open a [GitHub security advisory](../../security/advisories/new) for this repository, or
- Contact the maintainer, [Roger Vargas](https://github.com/porroto), directly.

Please do not open a public issue for reports that involve real student data —
report it privately so it can be removed before wider attention draws to it.

## No real student data, ever

This repository's governing rule: **no real student data lives here.** Every
example, sample evidence package, badge, and prototype input/output must be
synthetic or fully de-identified. See
[`governance/student-data-rules.md`](governance/student-data-rules.md) and
[`data/README.md`](data/README.md) for the full policy.

If you discover real student data committed to this repository, please report
it immediately using the private channel above so it can be removed and the
history scrubbed.

## Supported scope

Prototypes in this repository are research demos, not hardened software. Do
not connect them to real student information systems or production
credential-issuing infrastructure without a full security and privacy review.
