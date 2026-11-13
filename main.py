"""Manage a small library of reusable AI prompt templates.

Usage:
  python3 main.py list templates.json
  python3 main.py search templates.json <keyword>
  python3 main.py show templates.json <template-id>
templates.json is a JSON list of objects with id, title, tags
(a list of strings) and prompt. search matches the keyword
(case-insensitive) in the title, tags or prompt text. show prints
the full prompt for one template; an unknown id is an error.
"""
import argparse, json, sys

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def search(templates, keyword):
    keyword = keyword.lower()
    return [t for t in templates
            if keyword in t["title"].lower()
            or any(keyword in tag.lower() for tag in t["tags"])
            or keyword in t["prompt"].lower()]

def show(templates, template_id):
    for t in templates:
        if t["id"] == template_id:
            return t
    return None

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("list", "search", "show"):
        p = sub.add_parser(name)
        p.add_argument("path")
        if name in ("search", "show"):
            p.add_argument("query")
    args = parser.parse_args(argv)
    templates = load(args.path)
    if args.command == "list":
        for t in templates:
            print(f"{t['id']}: {t['title']} [{', '.join(t['tags'])}]")
        print(f"{len(templates)} template(s).")
    elif args.command == "search":
        results = search(templates, args.query)
        for t in results:
            print(f"{t['id']}: {t['title']} [{', '.join(t['tags'])}]")
        print(f"{len(results)} template(s) match '{args.query}'.")
    else:
        template = show(templates, args.query)
        if template is None:
            print(f"No template with id '{args.query}'.", file=sys.stderr)
            return 1
        print(f"{template['id']}: {template['title']}")
        print(template["prompt"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
