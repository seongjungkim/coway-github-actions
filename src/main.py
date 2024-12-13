import os
import json

def main():
    # Get the input from the GitHub Action
    name = os.getenv("INPUT_NAME", "World")

    # Generate a greeting message
    greeting = f"Hello, {name}!"
    print(greeting)

    # Set the output
    with open(os.getenv("GITHUB_OUTPUT"), "a") as output_file:
        output_file.write(f"greeting={greeting}\n")

if __name__ == "__main__":
    main()
