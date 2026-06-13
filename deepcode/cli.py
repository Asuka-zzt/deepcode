"""Command-line entry point for DeepCode.

Phase-1 scaffold (M0): a minimal entry that prints the version/banner.
The real interactive CLI (Rich + prompt_toolkit) arrives in M5.
"""

from __future__ import annotations

import argparse

from deepcode import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="deepcode", description="DeepCode coding agent")
    parser.add_argument("--version", action="version", version=f"deepcode {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    print(f"DeepCode {__version__} — scaffold (M0). Interactive CLI arrives in M5.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
