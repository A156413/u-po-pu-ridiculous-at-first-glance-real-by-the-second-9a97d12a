"""Write a one-line startup pitch to /output/entry.txt for make.fun's
'Ridiculous at First Glance, Real by the Second' bounty.

The pitch has to sound like a joke on the first read and like a
business on the second: it names the odd thing being sold (goats
for hire), who pays (solar farms), and why the economics hold
together (mowers damage panels, herbicide poisons the soil, and
the goats fertilize while they eat).

This sentence was written out by hand in a clean session that
began after the competition window opened.
"""

import os

TEXT = (
    "We rent goats to solar farms: "
    "mowers scratch the panels, "
    "herbicide poisons the soil, "
    "so the cheapest crew that fertilizes "
    "as it eats already bills "
    "a thousand dollars an acre."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
