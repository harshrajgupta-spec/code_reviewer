def policy_engine(state):

    findings = state["ranked_findings"]

    critical = len([
        f for f in findings
        if f.get("severity") == "critical"
    ])

    high = len([
        f for f in findings
        if f.get("severity") == "high"
    ])

    if critical > 0:

        state["decision"] = "REQUEST_CHANGES"

    elif high > 3:

        state["decision"] = "ESCALATE"

    elif len(findings) == 0:

        state["decision"] = "APPROVE"

    else:

        state["decision"] = "COMMENT_ONLY"

    return state