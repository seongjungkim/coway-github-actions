from google.cloud import dialogflowcx_v3 as dialogflow

def restore_agent(name, agent_uri=None, git_source=None):
    # Create a client
    client = dialogflow.AgentsClient()

    gitsource = dialogflow.RestoreAgentRequest.GitSource(tracking_branch=git_source)

    # Initialize request argument(s)
    request = dialogflow.RestoreAgentRequest(
        #agent_uri=agent_uri,
        git_source=gitsource,
        name=name,
    )

    """
    google.api_core.exceptions.PermissionDenied: 403 Invalid personal access token. 
    Please validate that the token has not expired and has access to read/write to the configured repository. 
    7: Invalid personal access token. 
    Please validate that the token has not expired and has access to read/write to the configured repository.
    """

    # Make the request
    operation = client.restore_agent(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

def export_agent(name):
    # Create a client
    client = dialogflow.AgentsClient()

    # Initialize request argument(s)
    request = dialogflow.ExportAgentRequest(
        name=name,
    )

    # Make the request
    operation = client.export_agent(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

if __name__ == "__main__":
   #
   name = "projects/qnacom-service/locations/global/agents/58afd3df-2c0b-4de7-902e-d3bb1c8f9591"
   # Gyeonggi Library Dialogflow
   name = "projects/qnacom-service/locations/global/agents/86920b8a-744d-4e24-8b2d-6d9a6ba8aac6"
   #export_agent(name)
   #restore_agent(name, git_source="main")
