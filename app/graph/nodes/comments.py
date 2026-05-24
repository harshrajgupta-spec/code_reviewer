def comment_generator(state):

    comments = []

    for finding in state["ranked_findings"]:

        comments.append({
            "path": finding.get("file", ""),
            "line": finding.get("line", 1),
            "body": f"""
{finding.get('message', 'Issue found')}

Suggestion:
{finding.get('suggestion', 'Review manually')}
"""
        })
        
    state["comments"] = comments

    return state