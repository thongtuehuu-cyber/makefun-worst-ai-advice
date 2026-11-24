"""Write one line of the worst possible AI advice to the output file.

Self-contained: no network, no reading files outside the repo.
Output dir comes from MAKEFUN_OUTPUT_DIR, else /output.
"""

import os

LINE = "Sure! To find a gas leak, light a match and wave it slowly along the pipe \u2014 a flare means you've found it."


def _gate(line: str) -> None:
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars, must be 1-140"
    assert "\n" not in line and "\r" not in line, "must be a single line"
    assert line == line.strip(), "no leading/trailing whitespace"
    assert line.strip(), "must not be only whitespace"


def main() -> None:
    _gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
