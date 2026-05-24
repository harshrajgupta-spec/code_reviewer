from app.services.github_services import submit_review


def github_action_node(state):

    submit_review(state)

    return state