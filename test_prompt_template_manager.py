import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
import json, tempfile
from main import load, search, show

TEMPLATES = [
    {"id": "password-reset-email", "title": "Draft a polite password reset email",
     "tags": ["email", "password"],
     "prompt": "Draft a short, polite email telling a user their password was reset."},
    {"id": "ticket-summary", "title": "Summarise a support ticket in three lines",
     "tags": ["ticket", "summary"],
     "prompt": "Summarise the support ticket below in three lines."},
    {"id": "meeting-notes", "title": "Turn meeting notes into action items",
     "tags": ["meeting", "notes"],
     "prompt": "Turn the meeting notes below into action items with owners."},
]

class TestPromptTemplateManager(unittest.TestCase):
    def test_search_by_title(self):
        self.assertEqual([t["id"] for t in search(TEMPLATES, "password")],
                         ["password-reset-email"])

    def test_search_by_tag(self):
        self.assertEqual([t["id"] for t in search(TEMPLATES, "ticket")],
                         ["ticket-summary"])

    def test_search_by_prompt_text(self):
        self.assertEqual([t["id"] for t in search(TEMPLATES, "owners")],
                         ["meeting-notes"])

    def test_search_case_insensitive(self):
        self.assertEqual([t["id"] for t in search(TEMPLATES, "PASSWORD")],
                         ["password-reset-email"])

    def test_search_no_match(self):
        self.assertEqual(search(TEMPLATES, "firewall"), [])

    def test_show_returns_template(self):
        self.assertEqual(show(TEMPLATES, "ticket-summary")["title"],
                         "Summarise a support ticket in three lines")

    def test_show_unknown_returns_none(self):
        self.assertIsNone(show(TEMPLATES, "does-not-exist"))

    def test_load_reads_json_file(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(TEMPLATES, f)
            path = f.name
        try:
            self.assertEqual(len(load(path)), 3)
        finally:
            os.remove(path)
