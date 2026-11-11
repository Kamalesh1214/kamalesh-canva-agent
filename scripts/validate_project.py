from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ".claude-plugin/plugin.json", ".mcp.json", "CLAUDE.md", "README.md",
    "skills/design-director/SKILL.md", "skills/brand-system/SKILL.md",
    "skills/presentation-studio/SKILL.md", "skills/social-content-studio/SKILL.md",
    "skills/carousel-generator/SKILL.md", "skills/campaign-workflow/SKILL.md",
    "desktop/CLAUDE_DESKTOP_SETUP.md",
    "desktop/CLAUDE_DESKTOP_PROJECT_INSTRUCTIONS.md",
]
errors = []
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

for rel in [".claude-plugin/plugin.json", ".mcp.json",
            "brand-profiles/kamalesh/v1.0.0/brand-profile.json",
            "brand-profiles/kamalesh/current.json"]:
    path = ROOT / rel
    if path.exists():
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid JSON in {rel}: {exc}")

for path in (ROOT / "skills").glob("*/SKILL.md"):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
        continue
    parts = text.split("---", 2)
    front = parts[1] if len(parts) > 2 else ""
    if not re.search(r"(?m)^name:\s*[\w-]+", front):
        errors.append(f"Missing skill name: {path.relative_to(ROOT)}")
    if not re.search(r"(?m)^description:\s*.+", front):
        errors.append(f"Missing skill description: {path.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Validated {len(required)} required files and {len(list((ROOT/'skills').glob('*/SKILL.md')))} skill files.")
print("Note: live Canva MCP connectivity and design operations are not tested.")
