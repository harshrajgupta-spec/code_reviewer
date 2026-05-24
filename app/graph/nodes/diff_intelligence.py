def diff_intelligence_node(state):

    files = state["changed_files"]

    state["is_backend"] = any(
        f.endswith(".py")
        for f in files
    )

    state["is_frontend"] = any(
        f.endswith(".js") or f.endswith(".css")
        for f in files
    )

    state["has_auth_changes"] = any(
        "auth" in f.lower()
        for f in files
    )

    state["large_pr"] = len(files) > 10

    return state