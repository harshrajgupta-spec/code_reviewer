from github import Github

from app.config import GITHUB_TOKEN

github_client = Github(GITHUB_TOKEN)


def fetch_pr(repo_name, pr_number):

    repo = github_client.get_repo(repo_name)

    pr = repo.get_pull(pr_number)

    files = []

    patches = []

    for file in pr.get_files():

        files.append(file.filename)

        if file.patch:
            patches.append(file.patch)

    return {
        "files": files,
        "diff": "\n".join(patches)
    }


def submit_review(state):

    repo = github_client.get_repo(state["repo"])

    pr = repo.get_pull(state["pr_number"])
    
    event_map = {
        "APPROVE": "APPROVE",
        "REQUEST_CHANGES": "REQUEST_CHANGES",
        "COMMENT_ONLY": "COMMENT"
    }

    review_event = event_map.get(
        state["decision"],
        "COMMENT"
    )

    pr.create_review(
        body=f"AI Review Result: {state['decision']}",
        event=review_event,
        comments=state["comments"]
    )