from pydantic import BaseModel
from typing import Optional, List


class SWEBenchEntry(BaseModel):
    instance_id: str
    text: str
    repo: str
    base_commit: str
    problem_statement: str
    hints_text: Optional[str]
    created_at: str
    patch: str
    test_patch: str
    FAIL_TO_PASS: List[str]
    PASS_TO_PASS: List[str]


class SWEBenchEntryWithoutTests(BaseModel):
    repo_name: str
    problem_statement: str
    patch: str
    base_commit: str


def convert_swedataset_item_to_entry(issue: dict) -> SWEBenchEntryWithoutTests:
    return SWEBenchEntryWithoutTests(
        repo_name=issue["title"],
        problem_statement=issue["topic"],
        patch=issue["content"],
        base_commit=issue["extras"]["base_commit"],
    )