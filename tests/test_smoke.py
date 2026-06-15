"""Smoke tests for the M0 scaffold."""

from deepcode import __version__
from deepcode.cli import build_parser, main


def test_version_is_set():
    assert __version__


def test_parser_builds():
    parser = build_parser()
    assert parser.prog == "deepcode"


def test_cli_runs(capsys):
    rc = main([])
    out = capsys.readouterr().out
    assert rc == 0
    assert "DeepCode" in out
