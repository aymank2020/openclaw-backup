# OpenClaw backup containment

This public repository now contains only guidance and a path-only publication check.
Raw `config/` and `sessions/` data are excluded from the current tree; existing local
copies are preserved. Do not restore this repository into an active OpenClaw service.

Before publishing, run `python scripts/check-public-tree.py` after staging changes.
The same check runs in GitHub Actions and prints paths only, never file contents.
It is a preventive path check, not a general secret detector.

Previously committed state remains in Git history. Removing files in a new commit
does **not** revoke credentials or erase history. Review exposed credentials in their
provider dashboards, revoke or rotate them, and assess session/device exposure.
Coordinate any history cleanup and repository visibility change with all consumers.

Use encrypted, access-restricted backups outside a public Git repository. Consult
the official [OpenClaw backup guide](https://docs.openclaw.ai/install/backups) and
[CLI reference](https://docs.openclaw.ai/cli/backup) before designing backup jobs.

No restore, cron, gateway, provider, or external-service operation is performed by
this repository's check.
