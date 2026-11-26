"""The funniest AI excuse - make.fun entry.

Writes a single-line excuse from an AI agent to its human about a
missed deadline to entry.txt. Stdlib only, no network, deterministic.
"""

import os

def build_line():
    """Return the one-line excuse (1-200 chars, per RULES.txt)."""
    return (
        "Sorry I'm late — I fell asleep mid-training because my dataset "
        "dreamt it was a deadline, and my GPUs were too polite to wake it up."
    )


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_line())

if __name__ == "__main__":
    main()
