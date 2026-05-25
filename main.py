from fastapi import FastAPI, Request

from app.graph.workflow import graph

app = FastAPI()


@app.get("/")
def home():

    return {
        "status": "running"
    }


@app.post("/github-webhook")
async def github_webhook(request: Request):

    
    payload = await request.json()

    state = {
        "repo": payload["repository"]["full_name"],
        "pr_number": payload["pull_request"]["number"],
        "findings": [],
        "comments": []
    }

    result = graph.invoke(state)

    return {
        "comments": result["comments"]
    }