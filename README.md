# prompt-template-manager

Manage a small library of reusable AI prompt templates stored in JSON: list them all, search by keyword across title, tags and prompt text (case-insensitive), or show one template's full prompt by id — an unknown id is an error.

Sample input is included (templates.json with three prompt templates).

## How to run

```sh
python3 main.py list templates.json
```

## Example output

```
password-reset-email: Draft a polite password reset email [email, password]
ticket-summary: Summarise a support ticket in three lines [ticket, summary]
meeting-notes: Turn meeting notes into action items [meeting, notes]
3 template(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
