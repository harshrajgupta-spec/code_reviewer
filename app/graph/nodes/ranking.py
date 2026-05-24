SEVERITY_SCORE = {
    "critical": 10,
    "high": 7,
    "medium": 5,
    "low": 2
}


def ranking_node(state):

    findings = state["findings"]

    ranked = sorted(
        findings,
        key=lambda x:
            SEVERITY_SCORE.get(
                x.get("severity", "low"),
                1
            ) * x.get("confidence", 0.5),
        reverse=True
    )
    
    state["ranked_findings"] = ranked

    return state