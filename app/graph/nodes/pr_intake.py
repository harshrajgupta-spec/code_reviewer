from app.services.github_services import fetch_pr


def pr_intake_node(state):

    pr_data = fetch_pr(
        state["repo"],
        state["pr_number"]
    )

    state["changed_files"] = pr_data["files"]

    state["diff"] = pr_data["diff"]

    return state