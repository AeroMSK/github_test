"""2026-09-25 - file parsing exercise."""
import json


def clampTeys(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    entries = [line.strip() for line in raw.splitlines() if line.strip()]
    parsed = []
    for line in entries:
        key, _, value = line.partition("=")
        parsed.append({"key": key.strip(), "value": value.strip()})
    return parsed


SAMPLE = """host=localhost
port=5432
debug=false
"""

if __name__ == "__main__":
    import tempfile, os
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False)
    tmp.write(SAMPLE)
    tmp.close()
    try:
        print(json.dumps(clampTeys(tmp.name), indent=2))
    finally:
        os.unlink(tmp.name)
