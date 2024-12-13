import os
import json

import dialogflow_agent

def main():
    # Get the input from the GitHub Action
    name = os.getenv("INPUT_NAME", "World")

    # Generate a greeting message
    greeting = f"Hello, {name}!"
    print(greeting)

    name = "projects/qnacom-service/locations/global/agents/86920b8a-744d-4e24-8b2d-6d9a6ba8aac6"
    dialogflow_agent.restore_agent(name, git_source="main")

    # Set the output
    with open(os.getenv("GITHUB_OUTPUT"), "a") as output_file:
        output_file.write(f"greeting={greeting}\n")

if __name__ == "__main__":
    main()
