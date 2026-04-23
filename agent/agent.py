import json

# Load tree
import os

base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "tree", "reflection-tree.json")

with open(file_path) as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

current = "START"
answers = {}

print("\n Daily Reflection Agent\n")

while True:
    node = nodes[current]
    node_type = node["type"]

    if node_type == "start":
        print(node["text"])
        current = node["next"]

    elif node_type == "question":
        print("\n" + node["text"])
        options = node["options"]

        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        choice = int(input("Choose option: "))
        selected = options[choice - 1]
        answers[current] = selected

        current = node["next"]

    elif node_type == "decision":
        prev_node = list(answers.keys())[-1]
        prev_answer = answers[prev_node]

        current = node["conditions"][prev_answer]

    elif node_type == "reflection":
        print("\n " + node["text"])
        input("Press Enter to continue...")
        current = node["next"]

    elif node_type == "bridge":
        print("\n" + node["text"])
        current = node["next"]

    elif node_type == "summary":
        print("\n SUMMARY")
        print(node["text"])
        current = node["next"]

    elif node_type == "end":
        print("\n4 " + node["text"])
        break