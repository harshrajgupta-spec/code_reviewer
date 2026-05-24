from typing import TypedDict, List, Dict


class Finding(TypedDict):

    type: str
    severity: str
    confidence: float
    file: str
    line: int
    message: str
    suggestion: str


class PRState(TypedDict):

    repo: str

    pr_number: int

    changed_files: List[str]

    diff: str

    findings: List[Finding]

    ranked_findings: List[Finding]

    decision: str

    comments: List[Dict]