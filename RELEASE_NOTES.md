# SpecTrial task bank v0.1.1

Fix independent reproduction by preserving the ordering of stdout and stderr (the upstream evaluation markers are emitted on stderr). Empty patches now run the clean baseline, and command-line output consistently uses UTF-8. Task packages and fixed test sets are unchanged from v0.1.0.

Initial reproducible practice set: Flask Blueprint validation, Requests proxy URL parsing, and Pytest captured-log state consistency.

- TaskPackage v1 schema and checksum validation.
- Frozen repository base commits and container image digests.
- Original problem statements, complete evaluation tests, Chinese onboarding notes and repository licenses.
- Cross-platform patch export and Docker-based local reproduction.

The hosted platform publishes only instances whose baseline and reference patches have passed isolated evaluation checks. Original benchmark solutions are public; this release is intended for practice.
