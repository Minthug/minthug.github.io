import re
import sys

README_PATH = "/tmp/readme.md"
OUTPUT_PATH = "_data/changelog.yml"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 버전 히스토리 테이블 파싱: | **v1.x.x** | 설명 |
pattern = r"\| \*\*v([\d.]+)\*\* \| (.+?) \|"
entries = [
    {"version": f"v{m.group(1)}", "desc": m.group(2).strip()}
    for m in re.finditer(pattern, content)
]

if not entries:
    print("ERROR: No version entries found in README", file=sys.stderr)
    sys.exit(1)

# YAML 수동 직렬화 (특수문자 안전 처리)
def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

lines = [
    "# Auto-generated from chzzk-chat-analyzer README",
    "# Do not edit manually — updated by GitHub Actions",
    "",
]
for entry in entries:
    lines.append(f"- version: {yaml_str(entry['version'])}")
    lines.append(f"  desc: {yaml_str(entry['desc'])}")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

versions = [e["version"] for e in entries]
print(f"Updated {len(entries)} entries: {versions[0]} (latest) ~ {versions[-1]}")
