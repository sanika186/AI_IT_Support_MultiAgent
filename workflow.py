from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents import classify_issue, generate_solution
from utils import get_issue_details


class ITSupportState(TypedDict):
    user_issue: str
    category: str
    final_response: str


# -----------------------------
# Agent 1 : Issue Classifier
# -----------------------------
def classify_node(state: ITSupportState):

    category = classify_issue(state["user_issue"]).strip()

    return {
        "category": category
    }


# -----------------------------
# Agent 2 : Solution Generator
# -----------------------------
def solution_node(state: ITSupportState):

    details = get_issue_details(state["category"])

    final_response = generate_solution(
        state["category"],
        details
    )

    return {
        "final_response": final_response
    }


# -----------------------------
# Build LangGraph Workflow
# -----------------------------
builder = StateGraph(ITSupportState)

builder.add_node("classifier", classify_node)
builder.add_node("solution", solution_node)

builder.set_entry_point("classifier")

builder.add_edge("classifier", "solution")
builder.add_edge("solution", END)

workflow = builder.compile()