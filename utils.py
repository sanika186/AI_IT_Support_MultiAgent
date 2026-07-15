import json


def load_knowledge_base():
    """
    Load the knowledge base from JSON file.
    """

    try:
        with open("knowledge_base.json", "r", encoding="utf-8") as file:
            knowledge_base = json.load(file)

        return knowledge_base

    except FileNotFoundError:
        print("Error: knowledge_base.json file not found.")
        return {}

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return {}


def get_issue_details(category):
    """
    Return issue details for the given category.
    """

    knowledge_base = load_knowledge_base()

    if category in knowledge_base:
        return knowledge_base[category]

    return {
    "possible_causes": [
        "The issue could not be classified automatically."
    ],
    "solutions": [
        "Please provide more details about your issue.",
        "Contact the IT Support Team if the problem continues."
    ],
    "priority": "Medium"
}


def print_line():
    print("=" * 60)