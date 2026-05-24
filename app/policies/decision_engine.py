def policy_engine(state):

    findings = state.get("ranked_findings", [])

    critical = 0
    high = 0
    medium = 0
    low = 0

    for f in findings:

        severity = str(
            f.get("severity", "")
        ).lower()

        if severity == "critical":

            critical += 1

        elif severity == "high":

            high += 1

        elif severity == "medium":

            medium += 1

        elif severity == "low":

            low += 1

    print("Critical:", critical)
    print("High:", high)
    print("Medium:", medium)
    print("Low:", low)

    if critical >= 1:

        state["decision"] = "REQUEST_CHANGES"

    elif high >= 2:

        state["decision"] = "REQUEST_CHANGES"

    elif high >= 1 or medium >= 3:

        state["decision"] = "ESCALATE"

    elif medium >= 1 or low >= 1:

        state["decision"] = "COMMENT_ONLY"

    else:

        state["decision"] = "APPROVE"

    print("FINAL DECISION:", state["decision"])

    return state