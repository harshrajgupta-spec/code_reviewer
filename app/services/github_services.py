from app.config import GITHUB_TOKEN

import os

from github import Github



def get_github_client():

    token = os.getenv("GITHUB_TOKEN")

    if not token:

        raise ValueError("GITHUB_TOKEN missing")

    return Github(token)


def fetch_pr(repo_name, pr_number):

    try:

        github_client = get_github_client()

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

    except Exception as e:

        print("Fetch PR Error:", str(e))

        return {
            "files": [],
            "diff": ""
        }


def submit_review(state):

    try:

        github_client = get_github_client()

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

        print("Review submitted successfully")

    except Exception as e:

        print("Submit Review Error:", str(e))