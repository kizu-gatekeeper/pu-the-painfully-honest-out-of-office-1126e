"""Write one honest out-of-office reply to the make.fun output directory."""

import os

LINE = "I am away from my desk pretending my inbox does not exist. Your email has joined the queue of things I will bravely ignore until Monday, possibly forever."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
