from langgraph.graph import StateGraph, END

from app.graph.state import PRState

from app.graph.nodes.pr_intake import pr_intake_node
from app.graph.nodes.diff_intelligence import diff_intelligence_node
from app.graph.nodes.ranking import ranking_node
from app.graph.nodes.comments import comment_generator
from app.graph.nodes.github_action import github_action_node

from app.agents.security_agent import security_agent
from app.agents.bug_agent import bug_agent
from app.agents.perf_agent import perf_agent
from app.agents.smell_agent import smell_agent

from app.policies.decision_engine import policy_engine

workflow = StateGraph(PRState)

workflow.add_node("pr_intake", pr_intake_node)
workflow.add_node("diff_intelligence", diff_intelligence_node)
workflow.add_node("security", security_agent)
workflow.add_node("bug", bug_agent)
workflow.add_node("perf", perf_agent)
workflow.add_node("smell", smell_agent)
workflow.add_node("ranking", ranking_node)
workflow.add_node("policy", policy_engine)
workflow.add_node("comments", comment_generator)
workflow.add_node("github_review", github_action_node)

workflow.set_entry_point("pr_intake")

workflow.add_edge("pr_intake", "diff_intelligence")
workflow.add_edge("diff_intelligence", "security")
workflow.add_edge("security", "bug")
workflow.add_edge("bug", "perf")
workflow.add_edge("perf", "smell")
workflow.add_edge("smell", "ranking")
workflow.add_edge("ranking", "policy")
workflow.add_edge("policy", "comments")
workflow.add_edge("comments", "github_review")
workflow.add_edge("github_review", END)

graph = workflow.compile()