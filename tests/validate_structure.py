from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
EXPECTED_NAME = "teaching-ppt-prompt-architect"
REQUIRED_REFERENCES = [
    ROOT / "references" / "discipline-adaptation.md",
    ROOT / "references" / "final-output-format.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


if not SKILL.is_file():
    fail("SKILL.md is missing from the repository root")

text = SKILL.read_text(encoding="utf-8")
match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
if not match:
    fail("SKILL.md must begin with YAML frontmatter")

frontmatter = match.group(1)
name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, flags=re.MULTILINE)
description_match = re.search(
    r"^description:\s*(.+)$", frontmatter, flags=re.MULTILINE
)

if not name_match or name_match.group(1).strip() != EXPECTED_NAME:
    fail(f"name must be {EXPECTED_NAME}")

if ROOT.name != EXPECTED_NAME:
    fail("repository directory name must match the skill name")

if not description_match or not description_match.group(1).strip():
    fail("description must be non-empty")

if len(description_match.group(1).strip()) > 1024:
    fail("description exceeds 1024 characters")

for reference in REQUIRED_REFERENCES:
    if not reference.is_file():
        fail(f"missing required reference: {reference.relative_to(ROOT)}")
    relative = reference.relative_to(ROOT).as_posix()
    if relative not in text:
        fail(f"SKILL.md does not reference {relative}")

if len(text.splitlines()) > 500:
    fail("SKILL.md exceeds the recommended 500-line limit")

print("OK: portable Agent Skill structure is valid")

