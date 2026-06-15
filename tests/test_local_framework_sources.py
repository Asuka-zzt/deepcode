from inspect import getfile
from pathlib import Path

from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph


def test_frameworks_load_from_vendor_sources() -> None:
    repository_root = Path(__file__).resolve().parents[1]

    langchain_file = Path(getfile(BaseMessage)).resolve()
    langgraph_file = Path(getfile(StateGraph)).resolve()

    assert langchain_file.is_relative_to(repository_root / "vendor" / "langchain")
    assert langgraph_file.is_relative_to(repository_root / "vendor" / "langgraph")
